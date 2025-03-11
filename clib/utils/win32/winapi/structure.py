import _winapi
import enum
import locale
import struct

import ctypes
from ctypes import wintypes

DEFAULT_CODING = locale.getpreferredencoding()
if ctypes.sizeof(ctypes.c_void_p) == 4:
    setattr(ctypes, 'c_address', ctypes.c_uint32)
    c_address = ctypes.c_uint32
else:
    setattr(ctypes, 'c_address', ctypes.c_uint64)
    c_address = ctypes.c_uint64
NTSTATUS = ctypes.c_uint32


# DEFAULT_CODING='utf-8'

class LUID(ctypes.Structure):
    _fields_ = [
        ("LowPart", ctypes.c_ulong),
        ("HighPart", ctypes.c_long)
    ]


class LUID_AND_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ("Luid", LUID),
        ("Attributes", ctypes.c_ulong),
    ]

    def is_enabled(self):
        return bool(self.attributes & SE_TOKEN_PRIVILEGE.SE_PRIVILEGE_ENABLED)

    def enable(self):
        self.attributes |= SE_TOKEN_PRIVILEGE.SE_PRIVILEGE_ENABLED

    def get_name(self):
        from . import advapi32

        size = ctypes.c_ulong(10240)
        buf = ctypes.create_unicode_buffer(size.value)
        res = advapi32.LookupPrivilegeName(None, self.LUID, buf, size)
        if res == 0:
            raise RuntimeError("Could not LookupPrivilegeName")
        return buf[:size.value]

    def __str__(self):
        res = self.get_name()
        if self.is_enabled():
            res += ' (enabled)'
        return res


class TOKEN_PRIVILEGES(ctypes.Structure):
    _fields_ = [
        ("count", ctypes.c_ulong),
        ("Privileges", LUID_AND_ATTRIBUTES * 1)
    ]

    def get_array(self):
        array_type = LUID_AND_ATTRIBUTES * self.count
        privileges = ctypes.cast(self.Privileges, ctypes.POINTER(array_type)).contents
        return privileges

    def __iter__(self):
        return iter(self.get_array())


PTOKEN_PRIVILEGES = ctypes.POINTER(TOKEN_PRIVILEGES)

MAX_MODULE_NAME32 = 255


class ModuleEntry32(ctypes.Structure):
    """Describes an entry from a list of the modules belonging to the specified process.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms684225%28v=vs.85%29.aspx
    """
    _fields_ = [
        ('dwSize', ctypes.c_ulong),
        ('th32ModuleID', ctypes.c_ulong),
        ('th32ProcessID', ctypes.c_ulong),
        ('GlblcntUsage', ctypes.c_ulong),
        ('ProccntUsage', ctypes.c_ulong),
        ('modBaseAddr', ctypes.POINTER(c_address)),
        ('modBaseSize', ctypes.c_ulong),
        ('hModule', ctypes.c_ulong),
        ('szModule', ctypes.c_char * (MAX_MODULE_NAME32 + 1)),
        ('szExePath', ctypes.c_char * ctypes.wintypes.MAX_PATH)
    ]

    def __init__(self, *args, **kwds):
        super(ModuleEntry32, self).__init__(*args, **kwds)
        self.dwSize = ctypes.sizeof(self)

    @property
    def base_address(self):
        return ctypes.addressof(self.modBaseAddr.contents)

    @property
    def name(self):
        return self.szModule.decode(DEFAULT_CODING)


LPMODULEENTRY32 = ctypes.POINTER(ModuleEntry32)


class ProcessEntry32(ctypes.Structure):
    """Describes an entry from a list of the processes residing in the system address space when a snapshot was taken.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms684839(v=vs.85).aspx
    """
    _fields_ = [
        ('dwSize', ctypes.c_ulong),
        ('cntUsage', ctypes.c_ulong),
        ('th32ProcessID', ctypes.c_ulong),
        ('th32DefaultHeapID', ctypes.POINTER(ctypes.c_ulong)),
        ('th32ModuleID', ctypes.c_ulong),
        ('cntThreads', ctypes.c_ulong),
        ('th32ParentProcessID', ctypes.c_ulong),
        ('pcPriClassBase', ctypes.c_ulong),
        ('dwFlags', ctypes.c_ulong),
        ('szExeFile', ctypes.c_char * ctypes.wintypes.MAX_PATH)
    ]

    @property
    def szExeFile(self):
        return self.szExeFile.decode(DEFAULT_CODING)

    def __init__(self, *args, **kwds):
        super(ProcessEntry32, self).__init__(*args, **kwds)
        self.dwSize = ctypes.sizeof(self)


class FILETIME(ctypes.Structure):
    _fields_ = [
        ("dwLowDateTime", ctypes.c_ulong),
        ("dwHighDateTime", ctypes.c_ulong)
    ]

    @property
    def value(self):
        v = struct.unpack('>Q', struct.pack('>LL', self.dwHighDateTime, self.dwLowDateTime))
        v = v[0]
        return v


class ThreadEntry32(ctypes.Structure):
    """Describes an entry from a list of the threads executing in the system when a snapshot was taken.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms686735(v=vs.85).aspx
    """

    _fields_ = [
        ('dwSize', ctypes.c_ulong),
        ("cntUsage", ctypes.c_ulong),
        ("th32ThreadID", ctypes.c_ulong),
        ("th32OwnerProcessID", ctypes.c_ulong),
        ("tpBasePri", ctypes.c_ulong),
        ("tpDeltaPri", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong)
    ]

    @property
    def szExeFile(self):
        return self.szExeFile.decode(DEFAULT_CODING)

    # XXX: save it somehow
    @property
    def creation_time(self):
        from . import kernel32
        THREAD_QUERY_INFORMATION = 0x0040
        handle = kernel32.OpenThread(
            THREAD_QUERY_INFORMATION, False, self.th32ThreadID
        )

        ctime = FILETIME()
        etime = FILETIME()
        ktime = FILETIME()
        utime = FILETIME()

        kernel32.GetThreadTimes(
            handle, ctypes.pointer(ctime), ctypes.pointer(etime), ctypes.pointer(ktime), ctypes.pointer(utime)
        )
        kernel32.CloseHandle(handle)
        return ctime.value

    def __init__(self, *args, **kwds):
        super(ThreadEntry32, self).__init__(*args, **kwds)
        self.dwSize = ctypes.sizeof(self)


class TOKEN(enum.IntEnum):
    STANDARD_RIGHTS_REQUIRED = 0x000F0000
    TOKEN_ASSIGN_PRIMARY = 0x0001
    TOKEN_DUPLICATE = 0x0002
    TOKEN_IMPERSONATE = 0x0004
    TOKEN_QUERY = 0x0008
    TOKEN_QUERY_SOURCE = 0x0010
    TOKEN_ADJUST_PRIVILEGES = 0x0020
    TOKEN_ADJUST_GROUPS = 0x0040
    TOKEN_ADJUST_DEFAULT = 0x0080
    TOKEN_ADJUST_SESSIONID = 0x0100
    TOKEN_ALL_ACCESS = (
            STANDARD_RIGHTS_REQUIRED |
            TOKEN_ASSIGN_PRIMARY |
            TOKEN_DUPLICATE |
            TOKEN_IMPERSONATE |
            TOKEN_QUERY |
            TOKEN_QUERY_SOURCE |
            TOKEN_ADJUST_PRIVILEGES |
            TOKEN_ADJUST_GROUPS |
            TOKEN_ADJUST_DEFAULT
    )


class SE_TOKEN_PRIVILEGE(enum.IntEnum):
    """An access token contains the security information for a logon session.
    The system creates an access token when a user logs on, and every process executed on behalf of the user has a copy of the token."""

    SE_PRIVILEGE_ENABLED_BY_DEFAULT = 0x00000001
    SE_PRIVILEGE_ENABLED = 0x00000002
    SE_PRIVILEGE_REMOVED = 0x00000004
    SE_PRIVILEGE_USED_FOR_ACCESS = 0x80000000


class MEMORY_STATE(enum.IntEnum):
    """The type of memory allocation"""
    #: Allocates memory charges (from the overall size of memory and the paging files on disk) for the specified reserved memory pages. The function also guarantees that when the caller later initially accesses the memory, the contents will be zero. Actual physical pages are not allocated unless/until the virtual addresses are actually accessed.
    MEM_COMMIT = 0x1000
    #: XXX
    MEM_FREE = 0x10000
    #: XXX
    MEM_RESERVE = 0x2000
    #: Decommits the specified region of committed pages. After the operation, the pages are in the reserved state.
    #: https://msdn.microsoft.com/en-us/library/windows/desktop/aa366894(v=vs.85).aspx
    MEM_DECOMMIT = 0x4000
    #: Releases the specified region of pages. After the operation, the pages are in the free state.
    #: https://msdn.microsoft.com/en-us/library/windows/desktop/aa366894(v=vs.85).aspx
    MEM_RELEASE = 0x8000


class MEMORY_TYPES(enum.IntEnum):
    #: XXX
    MEM_IMAGE = 0x1000000
    #: XXX
    MEM_MAPPED = 0x40000
    #: XXX
    MEM_PRIVATE = 0x20000


class MEMORY_PROTECTION(enum.IntEnum):
    """The following are the memory-protection options;
    you must specify one of the following values when allocating or protecting a page in memory
    https://msdn.microsoft.com/en-us/library/windows/desktop/aa366786(v=vs.85).aspx"""

    #: Enables execute access to the committed region of pages. An attempt to write to the committed region results in an access violation.
    PAGE_EXECUTE = 0x10
    #: Enables execute or read-only access to the committed region of pages. An attempt to write to the committed region results in an access violation.
    PAGE_EXECUTE_READ = 0x20
    #: Enables execute, read-only, or read/write access to the committed region of pages.
    PAGE_EXECUTE_READWRITE = 0x40
    #: Enables execute, read-only, or copy-on-write access to a mapped view of a file mapping object. An attempt to write to a committed copy-on-write page results in a private copy of the page being made for the process. The private page is marked as PAGE_EXECUTE_READWRITE, and the change is written to the new page.
    PAGE_EXECUTE_WRITECOPY = 0x80
    #: Disables all access to the committed region of pages. An attempt to read from, write to, or execute the committed region results in an access violation.
    PAGE_NOACCESS = 0x01
    #: Enables read-only access to the committed region of pages. An attempt to write to the committed region results in an access violation. If Data Execution Prevention is enabled, an attempt to execute code in the committed region results in an access violation.
    PAGE_READONLY = 0x02
    #: Enables read-only or read/write access to the committed region of pages. If Data Execution Prevention is enabled, attempting to execute code in the committed region results in an access violation.
    PAGE_READWRITE = 0x04
    #: Enables read-only or copy-on-write access to a mapped view of a file mapping object. An attempt to write to a committed copy-on-write page results in a private copy of the page being made for the process. The private page is marked as PAGE_READWRITE, and the change is written to the new page. If Data Execution Prevention is enabled, attempting to execute code in the committed region results in an access violation.
    PAGE_WRITECOPY = 0x08
    #: Pages in the region become guard pages. Any attempt to access a guard page causes the system to raise a STATUS_GUARD_PAGE_VIOLATION exception and turn off the guard page status. Guard pages thus act as a one-time access alarm. For more information, see Creating Guard Pages.
    PAGE_GUARD = 0x100
    #: Sets all pages to be non-cachable. Applications should not use this attribute except when explicitly required for a device. Using the interlocked functions with memory that is mapped with SEC_NOCACHE can result in an EXCEPTION_ILLEGAL_INSTRUCTION exception.
    PAGE_NOCACHE = 0x200
    #: Sets all pages to be write-combined.
    #: Applications should not use this attribute except when explicitly required for a device. Using the interlocked functions with memory that is mapped as write-combined can result in an EXCEPTION_ILLEGAL_INSTRUCTION exception.
    PAGE_WRITECOMBINE = 0x400


SIZE_OF_80387_REGISTERS = 80


class FLOATING_SAVE_AREA(ctypes.Structure):
    """Undocumented ctypes.Structure used for ThreadContext."""
    _fields_ = [
        ('ControlWord', ctypes.c_uint),
        ('StatusWord', ctypes.c_uint),
        ('TagWord', ctypes.c_uint),
        ('ErrorOffset', ctypes.c_uint),
        ('ErrorSelector', ctypes.c_uint),
        ('DataOffset', ctypes.c_uint),
        ('DataSelector', ctypes.c_uint),
        ('RegisterArea', ctypes.c_byte * SIZE_OF_80387_REGISTERS),
        ('Cr0NpxState', ctypes.c_uint)
    ]


MAXIMUM_SUPPORTED_EXTENSION = 512


class ThreadContext(ctypes.Structure):
    """Represents a thread context"""

    _fields_ = [
        ('ContextFlags', ctypes.c_uint),
        ('Dr0', ctypes.c_uint),
        ('Dr1', ctypes.c_uint),
        ('Dr2', ctypes.c_uint),
        ('Dr3', ctypes.c_uint),
        ('Dr6', ctypes.c_uint),
        ('Dr7', ctypes.c_uint),
        ('FloatSave', FLOATING_SAVE_AREA),
        ('SegGs', ctypes.c_uint),
        ('SegFs', ctypes.c_uint),
        ('SegEs', ctypes.c_uint),
        ('SegDs', ctypes.c_uint),
        ('Edi', ctypes.c_uint),
        ('Esi', ctypes.c_uint),
        ('Ebx', ctypes.c_uint),
        ('Edx', ctypes.c_uint),
        ('Ecx', ctypes.c_uint),
        ('Eax', ctypes.c_uint),
        ('Ebp', ctypes.c_uint),
        ('Eip', ctypes.c_uint),
        ('SegCs', ctypes.c_uint),
        ('EFlags', ctypes.c_uint),
        ('Esp', ctypes.c_uint),
        ('SegSs', ctypes.c_uint),
        ('ExtendedRegisters', ctypes.c_byte * MAXIMUM_SUPPORTED_EXTENSION)
    ]


class MODULEINFO(ctypes.Structure):
    """Contains the module load address, size, and entry point.

    attributes:
      lpBaseOfDll
      SizeOfImage
      EntryPoint

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms684229(v=vs.85).aspx
    """

    _fields_ = [
        ("lpBaseOfDll", ctypes.c_void_p),  # remote pointer
        ("SizeOfImage", ctypes.c_ulong),
        ("EntryPoint", ctypes.c_void_p),  # remote pointer
    ]

    def __init__(self, handle):
        self.process_handle = handle

    @property
    def name(self):
        from . import psapi
        modname = ctypes.c_buffer(ctypes.wintypes.MAX_PATH)
        psapi.GetModuleBaseNameA(
            self.process_handle,
            ctypes.c_void_p(self.lpBaseOfDll),
            modname,
            ctypes.sizeof(modname)
        )
        return modname.value

    @property
    def filename(self):
        from . import psapi
        _filename = ctypes.c_buffer(ctypes.wintypes.MAX_PATH)
        psapi.GetModuleFileNameExA(
            self.process_handle,
            ctypes.c_void_p(self.lpBaseOfDll),
            _filename,
            ctypes.sizeof(_filename)
        )
        return _filename.value


class SYSTEM_INFO(ctypes.Structure):
    """Contains information about the current computer system.
    This includes the architecture and type of the processor, the number
    of processors in the system, the page size, and other such information.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms724958(v=vs.85).aspx
    """

    _fields_ = [
        ("wProcessorArchitecture", ctypes.c_ushort),
        ("wReserved", ctypes.c_ushort),
        ("dwPageSize", ctypes.c_ulong),
        ("lpMinimumApplicationAddress", ctypes.c_ulong),
        ("lpMaximumApplicationAddress", ctypes.c_ulonglong),
        ("dwActiveProcessorMask", ctypes.c_ulong),
        ("dwNumberOfProcessors", ctypes.c_ulong),
        ("dwProcessorType", ctypes.c_ulong),
        ("dwAllocationGranularity", ctypes.c_ulong),
        ("wProcessorLevel", ctypes.c_ushort),
        ("wProcessorRevision", ctypes.c_ushort)
    ]


class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    """Contains information about a range of pages in the virtual address space of a process.
    The VirtualQuery and VirtualQueryEx functions use this structure.

    https://msdn.microsoft.com/en-us/library/windows/desktop/aa366775(v=vs.85).aspx
    """
    _fields_ = [
        ("BaseAddress", ctypes.c_ulonglong),
        ("AllocationBase", ctypes.c_ulonglong),
        ("AllocationProtect", ctypes.c_ulong),
        ("RegionSize", ctypes.c_ulonglong),
        ("State", ctypes.c_ulong),
        ("Protect", ctypes.c_ulong),
        ("Type", ctypes.c_ulong)
    ]

    @property
    def type(self):
        enum_type = [e for e in MEMORY_TYPES if e.value == self.Type] or None
        enum_type = enum_type[0] if enum_type else None
        return enum_type

    @property
    def state(self):
        enum_type = [e for e in MEMORY_STATE if e.value == self.State] or None
        enum_type = enum_type[0] if enum_type else None
        return enum_type

    @property
    def protect(self):
        enum_type = [e for e in MEMORY_PROTECTION if e.value == self.Protect]
        enum_type = enum_type[0] if enum_type else None
        return enum_type


class EnumProcessModuleEX(object):
    """The following are the EnumProcessModuleEX flags

    https://msdn.microsoft.com/ru-ru/library/windows/desktop/ms682633(v=vs.85).aspx
    """
    #: List the 32-bit modules
    LIST_MODULES_32BIT = 0x01
    #: List the 64-bit modules.
    LIST_MODULES_64BIT = 0x02
    #: List all modules.
    LIST_MODULES_ALL = 0x03
    #: Use the default behavior.
    LIST_MODULES_DEFAULT = 0x00


class SECURITY_ATTRIBUTES(ctypes.Structure):
    """The SECURITY_ATTRIBUTES structure contains the security descriptor for an
    object and specifies whether the handle retrieved by specifying this structure
    is inheritable.

    https://msdn.microsoft.com/en-us/library/windows/desktop/aa379560(v=vs.85).aspx
    """
    _fields_ = [('nLength', ctypes.c_ulong),
                ('lpSecurityDescriptor', ctypes.c_void_p),
                ('bInheritHandle', ctypes.c_long)
                ]


LPSECURITY_ATTRIBUTES = ctypes.POINTER(SECURITY_ATTRIBUTES)


class CLIENT_ID(ctypes.Structure):
    #: http://terminus.rewolf.pl/terminus/structures/ntdll/_CLIENT_ID64_x64.html
    _fields_ = [
        ("UniqueProcess", ctypes.c_void_p),
        ("UniqueThread", ctypes.c_void_p),
    ]


class THREAD_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("ExitStatus", NTSTATUS),
        ("TebBaseAddress", ctypes.c_void_p),
        ("ClientId", CLIENT_ID),
        ("AffinityMask", ctypes.c_long),
        ("Priority", ctypes.c_long),
        ("BasePriority", ctypes.c_long)
    ]


# TEB
class TIB_UNION(ctypes.Union):
    _fields_ = [
        ("FiberData", ctypes.c_void_p),
        ("Version", ctypes.c_ulong),
    ]


class NT_TIB(ctypes.Structure):
    _fields_ = [
        ("ExceptionList", ctypes.c_void_p),  # PEXCEPTION_REGISTRATION_RECORD
        ("StackBase", ctypes.c_void_p),
        ("StackLimit", ctypes.c_void_p),
        ("SubSystemTib", ctypes.c_void_p),
        ("u", TIB_UNION),
        ("ArbitraryUserPointer", ctypes.c_void_p),
        ("Self", ctypes.c_void_p),  # PNTTIB
    ]


class SMALL_TEB(ctypes.Structure):
    _pack_ = 1

    _fields_ = [
        ("NtTib", NT_TIB),
        ("EnvironmentPointer", ctypes.c_void_p),
        ("ClientId", CLIENT_ID),
        ("ActiveRpcHandle", ctypes.c_void_p),
        ("ThreadLocalStoragePointer", ctypes.c_void_p)
    ]


class SYSTEM_HANDLE(ctypes.Structure):
    _fields_ = [
        ("ProcessId", ctypes.c_int),
        ("ObjectTypeNumber", ctypes.c_byte),
        ("Flags", ctypes.c_byte),
        ("Handle", ctypes.c_ushort),
        ("Object", ctypes.c_void_p),
        ("AccessMask", ctypes.c_int),
    ]


class MODULEENTRY32(ctypes.Structure):
    _fields_ = [
        ('dwSize', ctypes.c_ulong),
        ('th32ModuleID', ctypes.c_ulong),
        ('th32ProcessID', ctypes.c_ulong),
        ('GlblcntUsage', ctypes.c_ulong),
        ('ProccntUsage', ctypes.c_ulong),
        ('modBaseAddr', ctypes.c_void_p),
        ('modBaseSize', ctypes.c_ulong),
        ('hModule', ctypes.c_void_p),
        ('szModule', ctypes.c_char * 256),
        ('szExePath', ctypes.c_char * 260)
    ]


class OBJECT_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ('Length', ctypes.c_ulong),
        ('RootDirectory', ctypes.c_void_p),
        ('ObjectName', ctypes.c_void_p),
        ('Attributes', ctypes.c_ulong),
        ('SecurityDescriptor', ctypes.c_void_p),
        ('SecurityQualityOfService', ctypes.c_void_p),
    ]


class SYSTEM_INFORMATION_CLASS(enum.IntEnum):
    SystemBasicInformation = enum.auto()
    SystemProcessorInformation = enum.auto()
    SystemPerformanceInformation = enum.auto()
    SystemTimeOfDayInformation = enum.auto()
    SystemPathInformation = enum.auto()
    SystemProcessInformation = enum.auto()
    SystemCallCountInformation = enum.auto()
    SystemDeviceInformation = enum.auto()
    SystemProcessorPerformanceInformation = enum.auto()
    SystemFlagsInformation = enum.auto()
    SystemCallTimeInformation = enum.auto()
    SystemModuleInformation = enum.auto()
    SystemLocksInformation = enum.auto()
    SystemStackTraceInformation = enum.auto()
    SystemPagedPoolInformation = enum.auto()
    SystemNonPagedPoolInformation = enum.auto()
    SystemHandleInformation = enum.auto()
    SystemObjectInformation = enum.auto()
    SystemPageFileInformation = enum.auto()
    SystemVdmInstemulInformation = enum.auto()
    SystemVdmBopInformation = enum.auto()
    SystemFileCacheInformation = enum.auto()
    SystemPoolTagInformation = enum.auto()
    SystemInterruptInformation = enum.auto()
    SystemDpcBehaviorInformation = enum.auto()
    SystemFullMemoryInformation = enum.auto()
    SystemLoadGdiDriverInformation = enum.auto()
    SystemUnloadGdiDriverInformation = enum.auto()
    SystemTimeAdjustmentInformation = enum.auto()
    SystemSummaryMemoryInformation = enum.auto()
    SystemMirrorMemoryInformation = enum.auto()
    SystemPerformanceTraceInformation = enum.auto()
    SystemCrashDumpInformation = enum.auto()
    SystemExceptionInformation = enum.auto()
    SystemCrashDumpStateInformation = enum.auto()
    SystemKernelDebuggerInformation = enum.auto()
    SystemContextSwitchInformation = enum.auto()
    SystemRegistryQuotaInformation = enum.auto()
    SystemExtendServiceTableInformation = enum.auto()
    SystemPrioritySeperation = enum.auto()
    SystemVerifierAddDriverInformation = enum.auto()
    SystemVerifierRemoveDriverInformation = enum.auto()
    SystemProcessorIdleInformation = enum.auto()
    SystemLegacyDriverInformation = enum.auto()
    SystemCurrentTimeZoneInformation = enum.auto()
    SystemLookasideInformation = enum.auto()
    SystemTimeSlipNotification = enum.auto()
    SystemSessionCreate = enum.auto()
    SystemSessionDetach = enum.auto()
    SystemSessionInformation = enum.auto()
    SystemRangeStartInformation = enum.auto()
    SystemVerifierInformation = enum.auto()
    SystemVerifierThunkExtend = enum.auto()
    SystemSessionProcessInformation = enum.auto()
    SystemLoadGdiDriverInSystemSpace = enum.auto()
    SystemNumaProcessorMap = enum.auto()
    SystemPrefetcherInformation = enum.auto()
    SystemExtendedProcessInformation = enum.auto()
    SystemRecommendedSharedDataAlignment = enum.auto()
    SystemComPlusPackage = enum.auto()
    SystemNumaAvailableMemory = enum.auto()
    SystemProcessorPowerInformation = enum.auto()
    SystemEmulationBasicInformation = enum.auto()
    SystemEmulationProcessorInformation = enum.auto()
    SystemExtendedHandleInformation = enum.auto()
    SystemLostDelayedWriteInformation = enum.auto()
    SystemBigPoolInformation = enum.auto()
    SystemSessionPoolTagInformation = enum.auto()
    SystemSessionMappedViewInformation = enum.auto()
    SystemHotpatchInformation = enum.auto()
    SystemObjectSecurityMode = enum.auto()
    SystemWatchdogTimerHandler = enum.auto()
    SystemWatchdogTimerInformation = enum.auto()
    SystemLogicalProcessorInformation = enum.auto()
    SystemWow64SharedInformationObsolete = enum.auto()
    SystemRegisterFirmwareTableInformationHandler = enum.auto()
    SystemFirmwareTableInformation = enum.auto()
    SystemModuleInformationEx = enum.auto()
    SystemVerifierTriageInformation = enum.auto()
    SystemSuperfetchInformation = enum.auto()
    SystemMemoryListInformation = enum.auto()
    SystemFileCacheInformationEx = enum.auto()
    SystemThreadPriorityClientIdInformation = enum.auto()
    SystemProcessorIdleCycleTimeInformation = enum.auto()
    SystemVerifierCancellationInformation = enum.auto()
    SystemProcessorPowerInformationEx = enum.auto()
    SystemRefTraceInformation = enum.auto()
    SystemSpecialPoolInformation = enum.auto()
    SystemProcessIdInformation = enum.auto()
    SystemErrorPortInformation = enum.auto()
    SystemBootEnvironmentInformation = enum.auto()
    SystemHypervisorInformation = enum.auto()
    SystemVerifierInformationEx = enum.auto()
    SystemTimeZoneInformation = enum.auto()
    SystemImageFileExecutionOptionsInformation = enum.auto()
    SystemCoverageInformation = enum.auto()
    SystemPrefetchPatchInformation = enum.auto()
    SystemVerifierFaultsInformation = enum.auto()
    SystemSystemPartitionInformation = enum.auto()
    SystemSystemDiskInformation = enum.auto()
    SystemProcessorPerformanceDistribution = enum.auto()
    SystemNumaProximityNodeInformation = enum.auto()
    SystemDynamicTimeZoneInformation = enum.auto()
    SystemCodeIntegrityInformation = enum.auto()
    SystemProcessorMicrocodeUpdateInformation = enum.auto()
    SystemProcessorBrandString = enum.auto()
    SystemVirtualAddressInformation = enum.auto()
    SystemLogicalProcessorAndGroupInformation = enum.auto()
    SystemProcessorCycleTimeInformation = enum.auto()
    SystemStoreInformation = enum.auto()
    SystemRegistryAppendString = enum.auto()
    SystemAitSamplingValue = enum.auto()
    SystemVhdBootInformation = enum.auto()
    SystemCpuQuotaInformation = enum.auto()
    SystemNativeBasicInformation = enum.auto()
    SystemErrorPortTimeouts = enum.auto()
    SystemLowPriorityIoInformation = enum.auto()
    SystemBootEntropyInformation = enum.auto()
    SystemVerifierCountersInformation = enum.auto()
    SystemPagedPoolInformationEx = enum.auto()
    SystemSystemPtesInformationEx = enum.auto()
    SystemNodeDistanceInformation = enum.auto()
    SystemAcpiAuditInformation = enum.auto()
    SystemBasicPerformanceInformation = enum.auto()
    SystemQueryPerformanceCounterInformation = enum.auto()
    SystemSessionBigPoolInformation = enum.auto()
    SystemBootGraphicsInformation = enum.auto()
    SystemScrubPhysicalMemoryInformation = enum.auto()
    SystemBadPageInformation = enum.auto()
    SystemProcessorProfileControlArea = enum.auto()
    SystemCombinePhysicalMemoryInformation = enum.auto()
    SystemEntropyInterruptTimingInformation = enum.auto()
    SystemConsoleInformation = enum.auto()
    SystemPlatformBinaryInformation = enum.auto()
    SystemThrottleNotificationInformation = enum.auto()
    SystemHypervisorProcessorCountInformation = enum.auto()
    SystemDeviceDataInformation = enum.auto()
    SystemDeviceDataEnumerationInformation = enum.auto()
    SystemMemoryTopologyInformation = enum.auto()
    SystemMemoryChannelInformation = enum.auto()
    SystemBootLogoInformation = enum.auto()
    SystemProcessorPerformanceInformationEx = enum.auto()
    SystemSpare0 = enum.auto()
    SystemSecureBootPolicyInformation = enum.auto()
    SystemPageFileInformationEx = enum.auto()
    SystemSecureBootInformation = enum.auto()
    SystemEntropyInterruptTimingRawInformation = enum.auto()
    SystemPortableWorkspaceEfiLauncherInformation = enum.auto()
    SystemFullProcessInformation = enum.auto()
    MaxSystemInfoClass = enum.auto()


class DuplicateOptions(enum.IntFlag):
    DUPLICATE_CLOSE_SOURCE = 0x00000001
    DUPLICATE_SAME_ACCESS = 0x00000002


class SYSTEM_HANDLE_ENTRY(ctypes.Structure):
    _fields_ = [
        ("OwnerPid", ctypes.c_ulong),
        ("ObjectType", ctypes.c_ubyte),
        ("HandleFlags", ctypes.c_ubyte),
        ("HandleValue", ctypes.c_ushort),
        ("ObjectPointer", ctypes.c_void_p),
        ("AccessMask", ctypes.c_ulong),
    ]


class Margins(ctypes.Structure):
    _fields_ = [
        ("cxLeftWidth", ctypes.c_int),
        ("cxRightWidth", ctypes.c_int),
        ("cyTopHeight", ctypes.c_int),
        ("cyBottomHeight", ctypes.c_int),
    ]


class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long),
    ]


class HANDLE_TABLE_ENTRY(ctypes.Structure):
    _fields_ = [
        ("Value", ctypes.c_void_p),
        ("GrantedAccess", ctypes.c_ulong),
    ]


class OSVERSIONINFOEXW(ctypes.Structure):
    _fields_ = [
        ("dwOSVersionInfoSize", ctypes.c_ulong),
        ("dwMajorVersion", ctypes.c_ulong),
        ("dwMinorVersion", ctypes.c_ulong),
        ("dwBuildNumber", ctypes.c_ulong),
        ("dwPlatformId", ctypes.c_ulong),
        ("szCSDVersion", ctypes.c_wchar * 128),
        ("wServicePackMajor", ctypes.c_ushort),
        ("wServicePackMinor", ctypes.c_ushort),
        ("wSuiteMask", ctypes.c_ushort),
        ("wProductType", ctypes.c_ubyte),
        ("wReserved", ctypes.c_ubyte),
    ]


class RTL_PROCESS_MODULE_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("Section", ctypes.c_void_p),
        ("MappedBase", ctypes.c_void_p),
        ("ImageBase", ctypes.c_void_p),
        ("ImageSize", ctypes.c_ulong),
        ("Flags", ctypes.c_ulong),
        ("LoadOrderIndex", ctypes.c_ushort),
        ("InitOrderIndex", ctypes.c_ushort),
        ("LoadCount", ctypes.c_ushort),
        ("OffsetToFileName", ctypes.c_ubyte),
        ("FullPathName", ctypes.c_wchar * 256),
    ]


class RTL_PROCESS_MODULES(ctypes.Structure):
    _fields_ = [
        ("NumberOfModules", ctypes.c_ulong),
        ("_Modules", RTL_PROCESS_MODULE_INFORMATION * 1),
    ]

    @property
    def Modules(self):
        return (RTL_PROCESS_MODULE_INFORMATION * self.NumberOfModules).from_address(
            ctypes.addressof(self._Modules)
        )


class SERVICE_ACCEPT(enum.IntEnum):
    STOP = 1 << 0
    PAUSE_CONTINUE = 1 << 1
    SHUTDOWN = 1 << 2
    PARAMCHANGE = 1 << 3
    NETBINDCHANGE = 1 << 4
    HARDWAREPROFILECHANGE = 1 << 5
    POWEREVENT = 1 << 6
    SESSIONCHANGE = 1 << 7


class SERVICE_START(enum.IntEnum):
    BOOT_START = 0
    SYSTEM_START = 1
    AUTO_START = 2
    DEMAND_START = 3
    DISABLED = 4


class ACCESS_MASK(enum.IntEnum):
    DELETE = 0x00010000
    READ_CONTROL = 0x00020000
    WRITE_DAC = 0x00040000
    WRITE_OWNER = 0x00080000
    SYNCHRONIZE = 0x00100000
    STANDARD_RIGHTS_REQUIRED = WRITE_OWNER | WRITE_DAC | READ_CONTROL | DELETE  # 0x000F0000
    STANDARD_RIGHTS_READ = READ_CONTROL  # 0x00020000
    STANDARD_RIGHTS_WRITE = STANDARD_RIGHTS_READ  # 0x00020000
    STANDARD_RIGHTS_EXECUTE = STANDARD_RIGHTS_WRITE  # 0x00020000
    STANDARD_RIGHTS_ALL = STANDARD_RIGHTS_EXECUTE | SYNCHRONIZE | WRITE_OWNER | WRITE_DAC | DELETE  # 0x001F0000
    SPECIFIC_RIGHTS_ALL = 0x0000FFFF
    ACCESS_SYSTEM_SECURITY = 0x01000000
    MAXIMUM_ALLOWED = 0x02000000
    GENERIC_READ = 0x80000000
    GENERIC_WRITE = 0x40000000
    GENERIC_EXECUTE = 0x20000000
    GENERIC_ALL = 0x10000000
    DESKTOP_READOBJECTS = 1
    DESKTOP_CREATEWINDOW = 2
    DESKTOP_CREATEMENU = 4
    DESKTOP_HOOKCONTROL = 8
    DESKTOP_JOURNALRECORD = 0x00000010
    DESKTOP_JOURNALPLAYBACK = 0x00000020
    DESKTOP_ENUMERATE = 0x00000040
    DESKTOP_WRITEOBJECTS = 0x00000080
    DESKTOP_SWITCHDESKTOP = 0x00000100
    WINSTA_ENUMDESKTOPS = DESKTOP_READOBJECTS  # 0x00000001
    WINSTA_READATTRIBUTES = DESKTOP_CREATEWINDOW  # 0x00000002
    WINSTA_ACCESSCLIPBOARD = DESKTOP_CREATEMENU  # 0x00000004
    WINSTA_CREATEDESKTOP = DESKTOP_HOOKCONTROL  # 0x00000008
    WINSTA_WRITEATTRIBUTES = DESKTOP_JOURNALRECORD  # 0x00000010
    WINSTA_ACCESSGLOBALATOMS = DESKTOP_JOURNALPLAYBACK  # 0x00000020
    WINSTA_EXITWINDOWS = DESKTOP_ENUMERATE  # 0x00000040
    WINSTA_ENUMERATE = DESKTOP_SWITCHDESKTOP  # 0x00000100
    WINSTA_READSCREEN = 0x00000200
    WINSTA_ALL_ACCESS = WINSTA_READSCREEN | WINSTA_ENUMERATE | WINSTA_EXITWINDOWS | WINSTA_ACCESSGLOBALATOMS | WINSTA_WRITEATTRIBUTES | WINSTA_CREATEDESKTOP | WINSTA_ACCESSCLIPBOARD | WINSTA_READATTRIBUTES | WINSTA_ENUMDESKTOPS  # 0x0000037F


class SERVICE_ACCESS(enum.IntEnum):
    QUERY_CONFIG = 0x0001
    CHANGE_CONFIG = 0x0002
    QUERY_STATUS = 0x0004
    ENUMERATE_DEPENDENTS = 0x0008
    START = 0x0010
    STOP = 0x0020
    PAUSE_CONTINUE = 0x0040
    INTERROGATE = 0x0080
    USER_DEFINED_CONTROL = 0x0100
    ALL_ACCESS = (
            ACCESS_MASK.STANDARD_RIGHTS_REQUIRED
            | QUERY_CONFIG
            | CHANGE_CONFIG
            | QUERY_STATUS
            | ENUMERATE_DEPENDENTS
            | START
            | STOP
            | PAUSE_CONTINUE
            | INTERROGATE
            | USER_DEFINED_CONTROL
    )  # 0x000F01FF


class SERVICE_STATE(enum.IntEnum):
    STOPPED = 0x00000001
    START_PENDING = 0x00000002
    STOP_PENDING = 0x00000003
    RUNNING = 0x00000004
    CONTINUE_PENDING = 0x00000005
    PAUSE_PENDING = 0x00000006
    PAUSED = 0x00000007


class SERVICE_CONTROL(enum.IntEnum):
    STOP = 0x00000001
    PAUSE = 0x00000002
    CONTINUE = 0x00000003
    INTERROGATE = 0x00000004
    SHUTDOWN = 0x00000005
    PARAMCHANGE = 0x00000006
    NETBINDADD = 0x00000007
    NETBINDREMOVE = 0x00000008
    NETBINDENABLE = 0x00000009
    NETBINDDISABLE = 0x0000000A
    DEVICEEVENT = 0x0000000B
    HARDWAREPROFILECHANGE = 0x0000000C
    POWEREVENT = 0x0000000D
    SESSIONCHANGE = 0x0000000E
    PRESHUTDOWN = 0x0000000F


class SERVICE_TYPE(enum.IntEnum):
    KERNEL_DRIVER = 0x00000001
    FILE_SYSTEM_DRIVER = 0x00000002
    ADAPTER = 0x00000004
    RECOGNIZER_DRIVER = 0x00000008
    WIN32_OWN_PROCESS = 0x00000010
    WIN32_SHARE_PROCESS = 0x00000020
    INTERACTIVE_PROCESS = 0x00000100
    WIN32 = WIN32_OWN_PROCESS | WIN32_SHARE_PROCESS


class SERVICE_START_TYPE(enum.IntEnum):
    BOOT_START = 0x00000000
    SYSTEM_START = 0x00000001
    AUTO_START = 0x00000002
    DEMAND_START = 0x00000003
    DISABLED = 0x00000004


class SERVICE_ERROR_CONTROL(enum.IntEnum):
    IGNORE = 0x00000000
    NORMAL = 0x00000001
    SEVERE = 0x00000002
    CRITICAL = 0x00000003


class UNICODE_STRING(ctypes.Structure):
    _fields_ = [
        ('Length', ctypes.c_ushort),
        ('MaximumLength', ctypes.c_ushort),
        ('Buffer', ctypes.c_void_p),
    ]

    @classmethod
    def from_str(cls, s: str):
        _buf = ctypes.create_unicode_buffer(s)
        length = len(s) * 2
        max_length = length + 2
        _s = cls(length, max_length, ctypes.addressof(_buf))
        setattr(_s, '_buf', _buf)
        return _s

    @property
    def value(self):
        return ctypes.cast(self.Buffer, ctypes.c_wchar_p).value


class IO_STATUS_BLOCK(ctypes.Structure):
    _fields_ = [
        ('Status', ctypes.c_ulong),
        ('Information', ctypes.c_void_p),
    ]


class SERVICE_STATUS(ctypes.Structure):
    _fields_ = [
        ('dwServiceType', ctypes.c_ulong),
        ('dwCurrentState', ctypes.c_ulong),
        ('dwControlsAccepted', ctypes.c_ulong),
        ('dwWin32ExitCode', ctypes.c_ulong),
        ('dwServiceSpecificExitCode', ctypes.c_ulong),
        ('dwCheckPoint', ctypes.c_ulong),
        ('dwWaitHint', ctypes.c_ulong),
    ]


class SCM_ACCESS(enum.IntEnum):
    CONNECT = 0x0001
    CREATE_SERVICE = 0x0002
    ENUMERATE_SERVICE = 0x0004
    LOCK = 0x0008
    QUERY_LOCK_STATUS = 0x0010
    MODIFY_BOOT_CONFIG = 0x0020
    STANDARD_RIGHTS_REQUIRED = 0x000F0000
    ALL_ACCESS = (
            STANDARD_RIGHTS_REQUIRED
            | CONNECT
            | CREATE_SERVICE
            | ENUMERATE_SERVICE
            | LOCK
            | QUERY_LOCK_STATUS
            | MODIFY_BOOT_CONFIG
    )  # 0x000F003F


class PAGE_PROTECT(enum.IntEnum):
    EXECUTE = 0x10
    EXECUTE_READ = 0x20
    EXECUTE_READWRITE = 0x40
    EXECUTE_WRITECOPY = 0x80
    NOACCESS = 0x01
    READONLY = 0x02
    READWRITE = 0x04
    WRITECOPY = 0x08
    GUARD = 0x100
    NOCACHE = 0x200
    WRITECOMBINE = 0x400


class LIST_ENTRY(ctypes.Structure):
    _fields_ = [
        ("Flink", ctypes.c_void_p),
        ("Blink", ctypes.c_void_p),
    ]


class PEB_LDR_DATA(ctypes.Structure):
    _fields_ = [
        ("Length", ctypes.c_uint32),
        ("Initialized", ctypes.c_uint8),
        ("SsHandle", ctypes.c_void_p),
        ("InLoadOrderModuleList", LIST_ENTRY),
        ("InMemoryOrderModuleList", LIST_ENTRY),
        ("InInitializationOrderModuleList", LIST_ENTRY),
        ("EntryInProgress", ctypes.c_void_p),
    ]


class RTL_USER_PROCESS_PARAMETERS(ctypes.Structure):
    _fields_ = [
        ("Reserved1", ctypes.c_byte * 16),
        ("Reserved2", ctypes.c_void_p * 10),
        ("ImagePathName", UNICODE_STRING),
        ("CommandLine", UNICODE_STRING),
    ]


class PEB(ctypes.Structure):
    _fields_ = [
        ("InheritedAddressSpace", ctypes.c_uint8),
        ("ReadImageFileExecOptions", ctypes.c_uint8),
        ("BeingDebugged", ctypes.c_uint8),
        ("SpareBool", ctypes.c_uint8),
        ("Mutant", ctypes.c_void_p),
        ("ImageBaseAddress", ctypes.c_void_p),
        ("Ldr", ctypes.c_void_p),
        # ...
    ]


class PROCESS_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("ExitStatus", NTSTATUS),
        ("PebBaseAddress", ctypes.c_void_p),
        ("AffinityMask", ctypes.c_void_p),
        ("BasePriority", ctypes.c_void_p),
        ("UniqueProcessId", ctypes.c_void_p),
        ("InheritedFromUniqueProcessId", ctypes.c_void_p)
    ]


class LDR_DATA_TABLE_ENTRY(LIST_ENTRY):
    _fields_ = [
        ("InLoadOrderLinks", LIST_ENTRY),
        ("InMemoryOrderLinks", LIST_ENTRY),
        ("InInitializationOrderLinks", LIST_ENTRY),
        ("DllBase", ctypes.c_void_p),
        ("EntryPoint", ctypes.c_void_p),
        ("SizeOfImage", ctypes.c_uint32),
        ("FullDllName", UNICODE_STRING),
        ("BaseDllName", UNICODE_STRING),
        ("Flags", ctypes.c_uint32),
        ("LoadCount", ctypes.c_uint16),
        ("TlsIndex", ctypes.c_uint16),
        ("HashLinks", LIST_ENTRY),
        ("SectionPointer", ctypes.c_void_p),
        ("CheckSum", ctypes.c_uint32),
        ("TimeDateStamp", ctypes.c_uint32),
        ("LoadedImports", ctypes.c_void_p),
        ("EntryPointActivationContext", ctypes.c_void_p),
        ("PatchInformation", ctypes.c_void_p),

    ]
