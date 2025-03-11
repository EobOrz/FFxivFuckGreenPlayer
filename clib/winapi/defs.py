import ctypes
import locale

import ctypes.wintypes

IS_64BIT = ctypes.sizeof(ctypes.c_void_p) == 8
DEFAULT_ENCODING = locale.getpreferredencoding()
NT_SUCCESS = lambda res: 0 <= res < 0x80000000

NT_STATUS = ctypes.c_ulong
HANDLE = ctypes.c_uint64 if IS_64BIT else ctypes.c_uint32
INVALID_HANDLE_VALUE = (1 << 64) - 1 if IS_64BIT else (1 << 32) - 1


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


class OBJECT_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ('Length', ctypes.c_ulong),
        ('RootDirectory', ctypes.c_void_p),
        ('ObjectName', ctypes.c_void_p),
        ('Attributes', ctypes.c_ulong),
        ('SecurityDescriptor', ctypes.c_void_p),
        ('SecurityQualityOfService', ctypes.c_void_p),
    ]


class IO_STATUS_BLOCK(ctypes.Structure):
    _fields_ = [
        ('Status', ctypes.c_ulong),
        ('Information', ctypes.c_void_p),
    ]


class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("BaseAddress", ctypes.c_ulonglong),
        ("AllocationBase", ctypes.c_ulonglong),
        ("AllocationProtect", ctypes.c_ulong),
        ("RegionSize", ctypes.c_ulonglong),
        ("State", ctypes.c_ulong),
        ("Protect", ctypes.c_ulong),
        ("Type", ctypes.c_ulong)
    ]


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


class TOKEN_PRIVILEGES(ctypes.Structure):
    _fields_ = [
        ("count", ctypes.c_ulong),
        ("Privileges", LUID_AND_ATTRIBUTES * 1)
    ]


class LIST_ENTRY(ctypes.Structure):
    _fields_ = [
        ("Flink", ctypes.c_size_t),
        ("Blink", ctypes.c_size_t),
    ]


class UNICODE_STRING(ctypes.Structure):
    _fields_ = [
        ('Length', ctypes.c_ushort),
        ('MaximumLength', ctypes.c_ushort),
        ('Buffer', ctypes.c_size_t),
    ]

    @classmethod
    def from_str(cls, s: str):
        length = len(s) * 2
        _s = cls(length, length + 2, ctypes.addressof(_buf := ctypes.create_unicode_buffer(s)))
        setattr(_s, '_buf', _buf)
        return _s

    @property
    def value(self):
        return ctypes.cast(self.Buffer, ctypes.c_wchar_p).value

    def remote_value(self, process: 'Process'):
        return process.read(self.Buffer, self.Length).decode('utf-16-le', 'ignore')


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


class PROCESS_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("ExitStatus", ctypes.c_ulong),
        ("PebBaseAddress", ctypes.c_void_p),
        ("AffinityMask", ctypes.c_void_p),
        ("BasePriority", ctypes.c_void_p),
        ("UniqueProcessId", ctypes.c_void_p),
        ("InheritedFromUniqueProcessId", ctypes.c_void_p)
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
        ("ProcessParameters", ctypes.c_void_p),
    ]


class CURDIR(ctypes.Structure):
    _fields_ = [
        ("DosPath", UNICODE_STRING),
        ("Handle", ctypes.c_void_p),
    ]


class RTL_USER_PROCESS_PARAMETERS(ctypes.Structure):
    _fields_ = [
        ("MaximumLength", ctypes.c_ulong),
        ("Length", ctypes.c_ulong),
        ("Flags", ctypes.c_ulong),
        ("DebugFlags", ctypes.c_ulong),
        ("ConsoleHandle", ctypes.c_void_p),
        ("ConsoleFlags", ctypes.c_ulong),
        ("StandardInput", ctypes.c_void_p),
        ("StandardOutput", ctypes.c_void_p),
        ("StandardError", ctypes.c_void_p),
        ("CurrentDirectory", CURDIR),
        ("DllPath", UNICODE_STRING),
        ("ImagePathName", UNICODE_STRING),
        ("CommandLine", UNICODE_STRING),
        ("Environment", ctypes.c_void_p),
    ]


class OVERLAPPED(ctypes.Structure):
    _fields_ = [
        ("Internal", ctypes.c_void_p),
        ("InternalHigh", ctypes.c_void_p),
        ("Offset", ctypes.c_ulong),
        ("OffsetHigh", ctypes.c_ulong),
        ("hEvent", ctypes.c_void_p)
    ]


class ProcessEntry32(ctypes.Structure):
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


class STARTUPINFOA(ctypes.Structure):
    _fields_ = [
        ('cb', ctypes.c_ulong),
        ('lpReserved', ctypes.c_char_p),
        ('lpDesktop', ctypes.c_char_p),
        ('lpTitle', ctypes.c_char_p),
        ('dwX', ctypes.c_ulong),
        ('dwY', ctypes.c_ulong),
        ('dwXSize', ctypes.c_ulong),
        ('dwYSize', ctypes.c_ulong),
        ('dwXCountChars', ctypes.c_ulong),
        ('dwYCountChars', ctypes.c_ulong),
        ('dwFillAttribute', ctypes.c_ulong),
        ('dwFlags', ctypes.c_ulong),
        ('wShowWindow', ctypes.wintypes.WORD),
        ('cbReserved2', ctypes.wintypes.WORD),
        ('lpReserved2', ctypes.c_char_p),
        ('hStdInput', ctypes.c_void_p),
        ('hStdOutput', ctypes.c_void_p),
        ('hStdError', ctypes.c_void_p),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cb = ctypes.sizeof(self)


class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('hProcess', ctypes.c_void_p),
        ('hThread', ctypes.c_void_p),
        ('dwProcessId', ctypes.c_ulong),
        ('dwThreadId', ctypes.c_ulong),
    ]
