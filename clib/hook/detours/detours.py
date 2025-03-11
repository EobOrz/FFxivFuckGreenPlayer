import ctypes
import os.path
import sys

_dll = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(sys.executable if getattr(sys, "frozen", False) else __file__), 'DetoursEx.dll'))


def _make_api(name, restype, argtypes):
    if f := getattr(_dll, name, None):
        f.restype = restype
        f.argtypes = argtypes
        return f


class _GUID(ctypes.Structure):
    _fields_ = [
        ('Data1', ctypes.c_uint32),
        ('Data2', ctypes.c_uint16),
        ('Data3', ctypes.c_uint16),
        ('Data4', ctypes.c_uint8 * 8),
    ]


class _DETOUR_SECTION_HEADER(ctypes.Structure):
    _fields_ = [
        ('cbHeaderSize', ctypes.c_uint32),
        ('nSignature', ctypes.c_uint32),
        ('nDataOffset', ctypes.c_uint32),
        ('cbDataSize', ctypes.c_uint32),
        ('nOriginalImportVirtualAddress', ctypes.c_uint32),
        ('nOriginalImportSize', ctypes.c_uint32),
        ('nOriginalBoundImportVirtualAddress', ctypes.c_uint32),
        ('nOriginalBoundImportSize', ctypes.c_uint32),
        ('nOriginalIatVirtualAddress', ctypes.c_uint32),
        ('nOriginalIatSize', ctypes.c_uint32),
        ('nOriginalSizeOfImage', ctypes.c_uint32),
        ('cbPrePE', ctypes.c_uint32),
        ('nOriginalClrFlags', ctypes.c_uint32),
        ('reserved1', ctypes.c_uint32),
        ('reserved2', ctypes.c_uint32),
        ('reserved3', ctypes.c_uint32),
    ]


class _DETOUR_SECTION_RECORD(ctypes.Structure):
    _fields_ = [
        ('cbBytes', ctypes.c_uint32),
        ('nReserved', ctypes.c_uint32),
        ('guid', _GUID),
    ]


class _DETOUR_CLR_HEADER(ctypes.Structure):
    _fields_ = [
        ('cb', ctypes.c_ulong),
        ('MajorRuntimeVersion', ctypes.c_uint16),
        ('MinorRuntimeVersion', ctypes.c_uint16),
        ('MetaData', ctypes.c_uint32 * 2),
        ('Flags', ctypes.c_ulong),
    ]


class _DETOUR_EXE_RESTORE(ctypes.Structure):
    _fields_ = [
        ('cb', ctypes.c_uint32),
        ('cbidh', ctypes.c_uint32),
        ('cbinh', ctypes.c_uint32),
        ('cbclr', ctypes.c_uint32),
        ('pidh', ctypes.POINTER(ctypes.c_uint8)),
        ('pinh', ctypes.POINTER(ctypes.c_uint8)),
        ('pclr', ctypes.POINTER(ctypes.c_uint8)),
        ('idh', ctypes.c_uint32 * 25),
        ('clr', _DETOUR_CLR_HEADER),
    ]


class _DETOUR_EXE_HELPER(ctypes.Structure):
    _fields_ = [
        ('cb', ctypes.c_uint32),
        ('pid', ctypes.c_uint32),
        ('nDlls', ctypes.c_uint32),
        ('rDlls', ctypes.c_char * 4),
    ]


DetourTransactionBegin = _make_api('DetourTransactionBegin', ctypes.c_long, (
))

DetourTransactionAbort = _make_api('DetourTransactionAbort', ctypes.c_long, (
))

DetourTransactionCommit = _make_api('DetourTransactionCommit', ctypes.c_long, (
))

DetourTransactionCommitEx = _make_api('DetourTransactionCommitEx', ctypes.c_long, (
    ctypes.c_void_p,  # pppFailedPointer
))

DetourUpdateThread = _make_api('DetourUpdateThread', ctypes.c_long, (
    ctypes.c_void_p,  # hThread
))

DetourAttach = _make_api('DetourAttach', ctypes.c_long, (
    ctypes.c_void_p,  # ppPointer
    ctypes.c_void_p,  # pDetour
))

DetourAttachEx = _make_api('DetourAttachEx', ctypes.c_long, (
    ctypes.c_void_p,  # ppPointer
    ctypes.c_void_p,  # pDetour
    ctypes.c_void_p,  # ppRealTrampoline
    ctypes.c_void_p,  # ppRealTarget
    ctypes.c_void_p,  # ppRealDetour
))

DetourDetach = _make_api('DetourDetach', ctypes.c_long, (
    ctypes.c_void_p,  # ppPointer
    ctypes.c_void_p,  # pDetour
))

DetourSetIgnoreTooSmall = _make_api('DetourSetIgnoreTooSmall', ctypes.c_bool, (
    ctypes.c_bool,  # fIgnore
))

DetourSetRetainRegions = _make_api('DetourSetRetainRegions', ctypes.c_bool, (
    ctypes.c_bool,  # fRetain
))

DetourSetSystemRegionLowerBound = _make_api('DetourSetSystemRegionLowerBound', ctypes.c_void_p, (
    ctypes.c_void_p,  # pSystemRegionLowerBound
))

DetourSetSystemRegionUpperBound = _make_api('DetourSetSystemRegionUpperBound', ctypes.c_void_p, (
    ctypes.c_void_p,  # pSystemRegionUpperBound
))

DetourFindFunction = _make_api('DetourFindFunction', ctypes.c_void_p, (
    ctypes.c_char_p,  # pszModule
    ctypes.c_char_p,  # pszFunction
))

DetourCodeFromPointer = _make_api('DetourCodeFromPointer', ctypes.c_void_p, (
    ctypes.c_void_p,  # pPointer
    ctypes.c_void_p,  # ppGlobals
))

DetourCopyInstruction = _make_api('DetourCopyInstruction', ctypes.c_void_p, (
    ctypes.c_void_p,  # pDst
    ctypes.c_void_p,  # ppDstPool
    ctypes.c_void_p,  # pSrc
    ctypes.c_void_p,  # ppTarget
    ctypes.c_void_p,  # plExtra
))

DetourSetCodeModule = _make_api('DetourSetCodeModule', ctypes.c_bool, (
    ctypes.c_void_p,  # hModule
    ctypes.c_bool,  # fLimitReferencesToModule
))

DetourAllocateRegionWithinJumpBounds = _make_api('DetourAllocateRegionWithinJumpBounds', ctypes.c_void_p, (
    ctypes.c_void_p,  # pbTarget
    ctypes.POINTER(ctypes.c_uint32),  # pcbAllocatedSize
))

DetourIsFunctionImported = _make_api('DetourIsFunctionImported', ctypes.c_bool, (
    ctypes.POINTER(ctypes.c_uint8),  # pbCode
    ctypes.POINTER(ctypes.c_uint8),  # pbAddress
))

DetourGetContainingModule = _make_api('DetourGetContainingModule', ctypes.c_void_p, (
    ctypes.c_void_p,  # pvAddr
))

DetourEnumerateModules = _make_api('DetourEnumerateModules', ctypes.c_void_p, (
    ctypes.c_void_p,  # hModuleLast
))

DetourGetEntryPoint = _make_api('DetourGetEntryPoint', ctypes.c_void_p, (
    ctypes.c_void_p,  # hModule
))

DetourGetModuleSize = _make_api('DetourGetModuleSize', ctypes.c_ulong, (
    ctypes.c_void_p,  # hModule
))

DetourEnumerateExports = _make_api('DetourEnumerateExports', ctypes.c_bool, (
    ctypes.c_void_p,  # hModule
    ctypes.c_void_p,  # pContext
    ctypes.c_void_p,  # pfExport
))

DetourEnumerateImports = _make_api('DetourEnumerateImports', ctypes.c_bool, (
    ctypes.c_void_p,  # hModule
    ctypes.c_void_p,  # pContext
    ctypes.c_void_p,  # pfImportFile
    ctypes.c_void_p,  # pfImportFunc
))

DetourEnumerateImportsEx = _make_api('DetourEnumerateImportsEx', ctypes.c_bool, (
    ctypes.c_void_p,  # hModule
    ctypes.c_void_p,  # pContext
    ctypes.c_void_p,  # pfImportFile
    ctypes.c_void_p,  # pfImportFuncEx
))

DetourFindPayload = _make_api('DetourFindPayload', ctypes.c_void_p, (
    ctypes.c_void_p,  # hModule
    ctypes.c_void_p,  # rguid
    ctypes.c_void_p,  # pcbData
))

DetourFindPayloadEx = _make_api('DetourFindPayloadEx', ctypes.c_void_p, (
    ctypes.c_void_p,  # rguid
    ctypes.c_void_p,  # pcbData
))

DetourGetSizeOfPayloads = _make_api('DetourGetSizeOfPayloads', ctypes.c_uint32, (
    ctypes.c_void_p,  # hModule
))

DetourFreePayload = _make_api('DetourFreePayload', ctypes.c_bool, (
    ctypes.c_void_p,  # pvData
))

DetourBinaryOpen = _make_api('DetourBinaryOpen', ctypes.POINTER(None), (
    ctypes.c_void_p,  # hFile
))

DetourBinaryEnumeratePayloads = _make_api('DetourBinaryEnumeratePayloads', ctypes.c_void_p, (
    ctypes.POINTER(None),  # pBinary
    ctypes.c_void_p,  # pGuid
    ctypes.c_void_p,  # pcbData
    ctypes.c_void_p,  # pnIterator
))

DetourBinaryFindPayload = _make_api('DetourBinaryFindPayload', ctypes.c_void_p, (
    ctypes.POINTER(None),  # pBinary
    ctypes.c_void_p,  # rguid
    ctypes.c_void_p,  # pcbData
))

DetourBinarySetPayload = _make_api('DetourBinarySetPayload', ctypes.c_void_p, (
    ctypes.POINTER(None),  # pBinary
    ctypes.c_void_p,  # rguid
    ctypes.c_void_p,  # pData
    ctypes.c_uint32,  # cbData
))

DetourBinaryDeletePayload = _make_api('DetourBinaryDeletePayload', ctypes.c_bool, (
    ctypes.POINTER(None),  # pBinary
    ctypes.c_void_p,  # rguid
))

DetourBinaryPurgePayloads = _make_api('DetourBinaryPurgePayloads', ctypes.c_bool, (
    ctypes.POINTER(None),  # pBinary
))

DetourBinaryResetImports = _make_api('DetourBinaryResetImports', ctypes.c_bool, (
    ctypes.POINTER(None),  # pBinary
))

DetourBinaryEditImports = _make_api('DetourBinaryEditImports', ctypes.c_bool, (
    ctypes.POINTER(None),  # pBinary
    ctypes.c_void_p,  # pContext
    ctypes.c_void_p,  # pfByway
    ctypes.c_void_p,  # pfFile
    ctypes.c_void_p,  # pfSymbol
    ctypes.c_void_p,  # pfCommit
))

DetourBinaryWrite = _make_api('DetourBinaryWrite', ctypes.c_bool, (
    ctypes.POINTER(None),  # pBinary
    ctypes.c_void_p,  # hFile
))

DetourBinaryClose = _make_api('DetourBinaryClose', ctypes.c_bool, (
    ctypes.POINTER(None),  # pBinary
))

DetourFindRemotePayload = _make_api('DetourFindRemotePayload', ctypes.c_void_p, (
    ctypes.c_void_p,  # hProcess
    ctypes.c_void_p,  # rguid
    ctypes.c_void_p,  # pcbData
))

DetourCreateProcessWithDllA = _make_api('DetourCreateProcessWithDllA', ctypes.c_bool, (
    ctypes.c_char_p,  # lpApplicationName
    ctypes.c_char_p,  # lpCommandLine
    ctypes.c_void_p,  # lpProcessAttributes
    ctypes.c_void_p,  # lpThreadAttributes
    ctypes.c_bool,  # bInheritHandles
    ctypes.c_uint32,  # dwCreationFlags
    ctypes.c_void_p,  # lpEnvironment
    ctypes.c_char_p,  # lpCurrentDirectory
    ctypes.c_void_p,  # lpStartupInfo
    ctypes.c_void_p,  # lpProcessInformation
    ctypes.c_char_p,  # lpDllName
    ctypes.c_void_p,  # pfCreateProcessA
))

DetourCreateProcessWithDllW = _make_api('DetourCreateProcessWithDllW', ctypes.c_bool, (
    ctypes.c_wchar_p,  # lpApplicationName
    ctypes.c_wchar_p,  # lpCommandLine
    ctypes.c_void_p,  # lpProcessAttributes
    ctypes.c_void_p,  # lpThreadAttributes
    ctypes.c_bool,  # bInheritHandles
    ctypes.c_uint32,  # dwCreationFlags
    ctypes.c_void_p,  # lpEnvironment
    ctypes.c_wchar_p,  # lpCurrentDirectory
    ctypes.c_void_p,  # lpStartupInfo
    ctypes.c_void_p,  # lpProcessInformation
    ctypes.c_char_p,  # lpDllName
    ctypes.c_void_p,  # pfCreateProcessW
))

DetourCreateProcessWithDllExA = _make_api('DetourCreateProcessWithDllExA', ctypes.c_bool, (
    ctypes.c_char_p,  # lpApplicationName
    ctypes.c_char_p,  # lpCommandLine
    ctypes.c_void_p,  # lpProcessAttributes
    ctypes.c_void_p,  # lpThreadAttributes
    ctypes.c_bool,  # bInheritHandles
    ctypes.c_uint32,  # dwCreationFlags
    ctypes.c_void_p,  # lpEnvironment
    ctypes.c_char_p,  # lpCurrentDirectory
    ctypes.c_void_p,  # lpStartupInfo
    ctypes.c_void_p,  # lpProcessInformation
    ctypes.c_char_p,  # lpDllName
    ctypes.c_void_p,  # pfCreateProcessA
))

DetourCreateProcessWithDllExW = _make_api('DetourCreateProcessWithDllExW', ctypes.c_bool, (
    ctypes.c_wchar_p,  # lpApplicationName
    ctypes.c_wchar_p,  # lpCommandLine
    ctypes.c_void_p,  # lpProcessAttributes
    ctypes.c_void_p,  # lpThreadAttributes
    ctypes.c_bool,  # bInheritHandles
    ctypes.c_uint32,  # dwCreationFlags
    ctypes.c_void_p,  # lpEnvironment
    ctypes.c_wchar_p,  # lpCurrentDirectory
    ctypes.c_void_p,  # lpStartupInfo
    ctypes.c_void_p,  # lpProcessInformation
    ctypes.c_char_p,  # lpDllName
    ctypes.c_void_p,  # pfCreateProcessW
))

DetourCreateProcessWithDllsA = _make_api('DetourCreateProcessWithDllsA', ctypes.c_bool, (
    ctypes.c_char_p,  # lpApplicationName
    ctypes.c_char_p,  # lpCommandLine
    ctypes.c_void_p,  # lpProcessAttributes
    ctypes.c_void_p,  # lpThreadAttributes
    ctypes.c_bool,  # bInheritHandles
    ctypes.c_uint32,  # dwCreationFlags
    ctypes.c_void_p,  # lpEnvironment
    ctypes.c_char_p,  # lpCurrentDirectory
    ctypes.c_void_p,  # lpStartupInfo
    ctypes.c_void_p,  # lpProcessInformation
    ctypes.c_uint32,  # nDlls
    ctypes.c_void_p,  # rlpDlls
    ctypes.c_void_p,  # pfCreateProcessA
))

DetourCreateProcessWithDllsW = _make_api('DetourCreateProcessWithDllsW', ctypes.c_bool, (
    ctypes.c_wchar_p,  # lpApplicationName
    ctypes.c_wchar_p,  # lpCommandLine
    ctypes.c_void_p,  # lpProcessAttributes
    ctypes.c_void_p,  # lpThreadAttributes
    ctypes.c_bool,  # bInheritHandles
    ctypes.c_uint32,  # dwCreationFlags
    ctypes.c_void_p,  # lpEnvironment
    ctypes.c_wchar_p,  # lpCurrentDirectory
    ctypes.c_void_p,  # lpStartupInfo
    ctypes.c_void_p,  # lpProcessInformation
    ctypes.c_uint32,  # nDlls
    ctypes.c_void_p,  # rlpDlls
    ctypes.c_void_p,  # pfCreateProcessW
))

DetourProcessViaHelperA = _make_api('DetourProcessViaHelperA', ctypes.c_bool, (
    ctypes.c_uint32,  # dwTargetPid
    ctypes.c_char_p,  # lpDllName
    ctypes.c_void_p,  # pfCreateProcessA
))

DetourProcessViaHelperW = _make_api('DetourProcessViaHelperW', ctypes.c_bool, (
    ctypes.c_uint32,  # dwTargetPid
    ctypes.c_char_p,  # lpDllName
    ctypes.c_void_p,  # pfCreateProcessW
))

DetourProcessViaHelperDllsA = _make_api('DetourProcessViaHelperDllsA', ctypes.c_bool, (
    ctypes.c_uint32,  # dwTargetPid
    ctypes.c_uint32,  # nDlls
    ctypes.c_void_p,  # rlpDlls
    ctypes.c_void_p,  # pfCreateProcessA
))

DetourProcessViaHelperDllsW = _make_api('DetourProcessViaHelperDllsW', ctypes.c_bool, (
    ctypes.c_uint32,  # dwTargetPid
    ctypes.c_uint32,  # nDlls
    ctypes.c_void_p,  # rlpDlls
    ctypes.c_void_p,  # pfCreateProcessW
))

DetourUpdateProcessWithDll = _make_api('DetourUpdateProcessWithDll', ctypes.c_bool, (
    ctypes.c_void_p,  # hProcess
    ctypes.c_void_p,  # rlpDlls
    ctypes.c_uint32,  # nDlls
))

DetourUpdateProcessWithDllEx = _make_api('DetourUpdateProcessWithDllEx', ctypes.c_bool, (
    ctypes.c_void_p,  # hProcess
    ctypes.c_void_p,  # hImage
    ctypes.c_bool,  # bIs32Bit
    ctypes.c_void_p,  # rlpDlls
    ctypes.c_uint32,  # nDlls
))

DetourCopyPayloadToProcess = _make_api('DetourCopyPayloadToProcess', ctypes.c_bool, (
    ctypes.c_void_p,  # hProcess
    ctypes.c_void_p,  # rguid
    ctypes.c_void_p,  # pvData
    ctypes.c_uint32,  # cbData
))

DetourCopyPayloadToProcessEx = _make_api('DetourCopyPayloadToProcessEx', ctypes.c_void_p, (
    ctypes.c_void_p,  # hProcess
    ctypes.c_void_p,  # rguid
    ctypes.c_void_p,  # pvData
    ctypes.c_uint32,  # cbData
))

DetourRestoreAfterWith = _make_api('DetourRestoreAfterWith', ctypes.c_bool, (
))

DetourRestoreAfterWithEx = _make_api('DetourRestoreAfterWithEx', ctypes.c_bool, (
    ctypes.c_void_p,  # pvData
    ctypes.c_uint32,  # cbData
))

DetourIsHelperProcess = _make_api('DetourIsHelperProcess', ctypes.c_bool, (
))

DetourFinishHelperProcess = _make_api('DetourFinishHelperProcess', None, (
    ctypes.c_void_p,  # a1
    ctypes.c_void_p,  # a2
    ctypes.c_char_p,  # a3
    ctypes.c_int,  # a4
))
