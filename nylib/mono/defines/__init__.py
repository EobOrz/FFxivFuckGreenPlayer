import ctypes

from nylib import winapi
from .enums import *


class _MonoObj:
    def __new__(cls, ptr):
        if not ptr:
            return None
        return super().__new__(cls)

    def __init__(self, ptr):
        self.ptr = ptr

    def __eq__(self, other):
        if isinstance(other, _MonoObj):
            return self.ptr == other.ptr
        return False

    def __str__(self):
        if hasattr(self, 'name'):
            return f"{self.__class__.__name__}({self.name})"
        return f"{self.__class__.__name__}({self.ptr:#x})"


class _MonoApi:
    _cached_ = {}

    def __new__(cls, mono_handle, function, argtypes=None, restype=None):
        key = (mono_handle, function)
        if key in cls._cached_:
            return cls._cached_[key]
        else:
            obj = super().__new__(cls)
            cls._cached_[key] = obj
            return obj

    def __init__(self, mono_handle, function, argtypes=None, restype=None):
        if hasattr(self, "mono_handle"): return
        self.mono_handle = mono_handle
        self.function = function
        if argtypes is None: argtypes = ()
        try:
            self.func_ptr = winapi.GetProcAddress(mono_handle, function)
        except OSError:
            self.func_ptr = None
            self.c_func = None
        else:
            if restype is ctypes.c_void_p: restype = ctypes.c_size_t  # auto cast to pyint
            self.c_func = ctypes.CFUNCTYPE(restype, *argtypes)(self.func_ptr)

    def __bool__(self):
        return bool(self.func_ptr)

    def __call__(self, *args):
        if self.c_func is None:
            raise OSError(f"Function {self.function} not found in mono")
        return self.c_func(*args)


MonoDomainFunc = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], None)
GFunc = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], None)
G_FREE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], None)
MONO_GET_ROOT_DOMAIN = lambda h, f: _MonoApi(h, f, [], ctypes.c_void_p)
MONO_THREAD_ATTACH = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_THREAD_DETACH = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], None)
MONO_THREAD_CLEANUP = lambda h, f: _MonoApi(h, f, [], None)
MONO_OBJECT_GET_CLASS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_DOMAIN_FOREACH = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], None)
MONO_DOMAIN_SET = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_bool], ctypes.c_int)
MONO_DOMAIN_GET = lambda h, f: _MonoApi(h, f, [], ctypes.c_void_p)
MONO_ASSEMBLY_FOREACH = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_int)
MONO_ASSEMBLY_GET_IMAGE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_ASSEMBLY_OPEN = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)], ctypes.c_void_p)
MONO_IMAGE_GET_ASSEMBLY = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_IMAGE_GET_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_char_p)
MONO_IMAGE_OPEN = lambda h, f: _MonoApi(h, f, [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)], ctypes.c_void_p)
MONO_IMAGE_GET_FILENAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_char_p)
MONO_IMAGE_GET_TABLE_INFO = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_int], ctypes.c_void_p)
MONO_TABLE_INFO_GET_ROWS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
MONO_METADATA_DECODE_ROW_COL = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_int, ctypes.c_uint], ctypes.c_int)
MONO_METADATA_STRING_HEAP = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_uint], ctypes.c_char_p)
MONO_CLASS_FROM_NAME_CASE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p], ctypes.c_void_p)
MONO_CLASS_FROM_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p], ctypes.c_void_p)
MONO_CLASS_GET_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_char_p)
MONO_CLASS_GET_NAMESPACE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_char_p)
MONO_CLASS_GET = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_uint], ctypes.c_void_p)
MONO_CLASS_FROM_TYPEREF = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_uint], ctypes.c_void_p)
MONO_CLASS_NAME_FROM_TOKEN = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_uint], ctypes.c_char_p)

MONO_CLASS_GET_METHODS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
MONO_CLASS_GET_METHOD_FROM_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int], ctypes.c_void_p)
MONO_CLASS_GET_FIELDS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
MONO_CLASS_GET_FIELD_FROM_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_char_p], ctypes.c_void_p)
MONO_CLASS_GET_INTERFACES = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
MONO_CLASS_GET_PROPERTIES = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
MONO_CLASS_GET_PROPERTY_FROM_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_char_p], ctypes.c_void_p)
MONO_CLASS_GET_EVENTS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
MONO_CLASS_GET_PARENT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_CLASS_GET_IMAGE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_CLASS_VTABLE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
MONO_CLASS_INSTANCE_SIZE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
MONO_CLASS_FROM_MONO_TYPE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_CLASS_GET_ELEMENT_CLASS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_CLASS_IS_GENERIC = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
MONO_CLASS_IS_ENUM = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_bool)
MONO_CLASS_IS_VALUETYPE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_bool)
MONO_CLASS_IS_SUBCLASS_OF = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool], ctypes.c_bool)

MONO_CLASS_NUM_FIELDS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
MONO_CLASS_NUM_METHODS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)

MONO_FIELD_GET_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_char_p)
MONO_FIELD_GET_TYPE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_FIELD_GET_PARENT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_FIELD_GET_OFFSET = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
MONO_FIELD_GET_FLAGS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
MONO_FIELD_GET_VALUE_OBJECT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)

MONO_PROPERTY_GET_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_char_p)
MONO_PROPERTY_GET_GET_METHOD = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_PROPERTY_GET_SET_METHOD = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_PROPERTY_GET_PARENT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_PROPERTY_GET_FLAGS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)

MONO_TYPE_GET_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_char_p)
MONO_TYPE_GET_CLASS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_TYPE_GET_TYPE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
MONO_TYPE_IS_BYREF = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
MONO_TYPE_GET_OBJECT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
IL2CPP_TYPE_GET_OBJECT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_METHOD_GET_OBJECT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
IL2CPP_METHOD_GET_OBJECT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
MONO_PTR_GET_CLASS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_TYPE_GET_PTR_TYPE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)

MONO_TYPE_GET_NAME_FULL = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_int], ctypes.c_char_p)
MONO_TYPE_IS_STRUCT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_bool)

MONO_METHOD_GET_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_char_p)
MONO_METHOD_GET_FULL_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_char_p)
MONO_COMPILE_METHOD = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_FREE_METHOD = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], None)

MONO_JIT_INFO_TABLE_FIND = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)

MONO_JIT_INFO_GET_METHOD = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_JIT_INFO_GET_CODE_START = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_JIT_INFO_GET_CODE_SIZE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)

MONO_JIT_EXEC = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p)], ctypes.c_int)

MONO_METHOD_GET_FLAGS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)], ctypes.c_uint32)
MONO_METHOD_GET_HEADER = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_METHOD_GET_CLASS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_METHOD_SIG = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_METHOD_GET_PARAM_NAMES = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p)], ctypes.c_void_p)

MONO_METHOD_HEADER_GET_CODE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32)], ctypes.c_void_p)
MONO_DISASM_CODE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p], ctypes.c_char_p)

MONO_SIGNATURE_GET_DESC = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_int], ctypes.c_char_p)
MONO_SIGNATURE_GET_PARAMS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)], ctypes.c_void_p)
MONO_SIGNATURE_GET_PARAM_COUNT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
MONO_SIGNATURE_GET_RETURN_TYPE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)

MONO_IMAGE_RVA_MAP = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_uint32], ctypes.c_void_p)
MONO_VTABLE_GET_STATIC_FIELD_DATA = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)

MONO_METHOD_DESC_NEW = lambda h, f: _MonoApi(h, f, [ctypes.c_char_p, ctypes.c_int], ctypes.c_void_p)
MONO_METHOD_DESC_FROM_METHOD = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_METHOD_DESC_FREE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], None)

MONO_ASSEMBLY_NAME_NEW = lambda h, f: _MonoApi(h, f, [ctypes.c_char_p], ctypes.c_void_p)
MONO_ASSEMBLY_LOADED = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_IMAGE_LOADED = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)

MONO_STRING_NEW = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_char_p], ctypes.c_void_p)
MONO_STRING_TO_UTF8 = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_char_p)
MONO_ARRAY_NEW = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint)], ctypes.c_void_p)
IL2CPP_ARRAY_NEW = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint)], ctypes.c_void_p)
MONO_ARRAY_ELEMENT_SIZE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
MONO_CLASS_GET_RANK = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
MONO_OBJECT_TO_STRING = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)], ctypes.c_void_p)
MONO_OBJECT_NEW = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)

MONO_FREE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], None)

MONO_METHOD_DESC_SEARCH_IN_IMAGE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
MONO_RUNTIME_INVOKE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_void_p)], ctypes.c_void_p)
MONO_RUNTIME_INVOKE_ARRAY = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)], ctypes.c_void_p)
MONO_RUNTIME_OBJECT_INIT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)

MONO_FIELD_STATIC_GET_VALUE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
MONO_FIELD_STATIC_SET_VALUE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)

IL2CPP_FIELD_STATIC_GET_VALUE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
IL2CPP_FIELD_STATIC_SET_VALUE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)

MONO_VALUE_BOX = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
MONO_OBJECT_UNBOX = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_OBJECT_ISINST = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)
MONO_GET_ENUM_CLASS = lambda h, f: _MonoApi(h, f, [], ctypes.c_void_p)
MONO_CLASS_GET_TYPE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
MONO_CLASS_GET_NESTING_TYPE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)

MONO_CLASS_GET_NESTED_TYPES = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p)

MONO_RUNTIME_IS_SHUTTING_DOWN = lambda h, f: _MonoApi(h, f, [], ctypes.c_int)

# il2cpp:
IL2CPP_DOMAIN_GET_ASSEMBLIES = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t)], ctypes.POINTER(ctypes.POINTER(ctypes.c_uint)))

IL2CPP_IMAGE_GET_CLASS_COUNT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
IL2CPP_IMAGE_GET_CLASS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_int], ctypes.c_void_p)

IL2CPP_TYPE_GET_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_char_p)
IL2CPP_TYPE_GET_ASSEMBLY_QUALIFIED_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_char_p)

IL2CPP_METHOD_GET_PARAM_COUNT = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_int)
IL2CPP_METHOD_GET_PARAM_NAME = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_int], ctypes.c_char_p)
IL2CPP_METHOD_GET_PARAM = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p, ctypes.c_int], ctypes.c_void_p)
IL2CPP_METHOD_GET_RETURN_TYPE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
IL2CPP_CLASS_FROM_TYPE = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_void_p)
IL2CPP_STRING_CHARS = lambda h, f: _MonoApi(h, f, [ctypes.c_void_p], ctypes.c_wchar_p)


def _find_mono():
    from ...process import Process
    for ldr in Process.current.enum_ldr_data():
        handle = ldr.DllBase
        try:
            if winapi.GetProcAddress(handle, b"mono_thread_attach"):
                return handle, False
        except OSError:
            pass
        try:
            if winapi.GetProcAddress(handle, b"il2cpp_thread_attach"):
                return handle, True
        except OSError:
            pass
    else:
        raise OSError("mono.dll not found in this process")


class MonoApi:
    instance: 'MonoApi'

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = cls()
        return cls.instance

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, mono_handle=None, is_il2cpp=False):
        if mono_handle is None:
            try:
                self.mono_handle = winapi.GetModuleHandle("mono.dll")
            except OSError:
                self.mono_handle, self.is_il2cpp = _find_mono()
            else:
                self.is_il2cpp = False
        else:
            self.mono_handle = mono_handle
            self.is_il2cpp = is_il2cpp

        if self.is_il2cpp:
            self._init_il2cpp()
        else:
            self._init_mono()

    def _init_il2cpp(self):
        self.g_free = (G_FREE(self.mono_handle, b"g_free") or
                       G_FREE(self.mono_handle, b"il2cpp_free") or
                       (lambda ptr: None))  # if all else fails, do nothing
        self.mono_free = MONO_FREE(self.mono_handle, b"il2cpp_free")
        self.mono_get_root_domain = (MONO_GET_ROOT_DOMAIN(self.mono_handle, b"il2cpp_get_root_domain") or
                                     MONO_GET_ROOT_DOMAIN(self.mono_handle, b"mono_get_root_domain"))
        self.mono_thread_attach = MONO_THREAD_ATTACH(self.mono_handle, b"il2cpp_thread_attach")
        self.mono_thread_detach = MONO_THREAD_DETACH(self.mono_handle, b"il2cpp_thread_detach")
        self.mono_object_get_class = MONO_OBJECT_GET_CLASS(self.mono_handle, b"il2cpp_object_get_class")
        self.mono_domain_foreach = MONO_DOMAIN_FOREACH(self.mono_handle, b"il2cpp_domain_foreach")
        self.mono_domain_set = MONO_DOMAIN_SET(self.mono_handle, b"il2cpp_domain_set")
        self.mono_domain_get = MONO_DOMAIN_GET(self.mono_handle, b"il2cpp_domain_get")
        self.mono_assembly_foreach = MONO_ASSEMBLY_FOREACH(self.mono_handle, b"il2cpp_assembly_foreach")
        self.mono_assembly_get_image = MONO_ASSEMBLY_GET_IMAGE(self.mono_handle, b"il2cpp_assembly_get_image")
        self.mono_image_get_assembly = MONO_IMAGE_GET_ASSEMBLY(self.mono_handle, b"il2cpp_image_get_assembly")
        self.mono_image_get_name = MONO_IMAGE_GET_NAME(self.mono_handle, b"il2cpp_image_get_name")
        self.mono_image_get_table_info = MONO_IMAGE_GET_TABLE_INFO(self.mono_handle, b"il2cpp_image_get_table_info")
        self.mono_image_rva_map = MONO_IMAGE_RVA_MAP(self.mono_handle, b"il2cpp_image_rva_map")
        self.mono_table_info_get_rows = MONO_TABLE_INFO_GET_ROWS(self.mono_handle, b"il2cpp_table_info_get_rows")
        self.mono_metadata_decode_row_col = MONO_METADATA_DECODE_ROW_COL(self.mono_handle, b"il2cpp_metadata_decode_row_col")
        self.mono_metadata_string_heap = MONO_METADATA_STRING_HEAP(self.mono_handle, b"il2cpp_metadata_string_heap")

        self.mono_class_get = MONO_CLASS_GET(self.mono_handle, b"il2cpp_class_get")
        self.mono_class_from_typeref = MONO_CLASS_FROM_TYPEREF(self.mono_handle, b"il2cpp_class_from_typeref")
        self.mono_class_name_from_token = MONO_CLASS_NAME_FROM_TOKEN(self.mono_handle, b"il2cpp_class_name_from_token")
        self.mono_class_from_name_case = MONO_CLASS_FROM_NAME_CASE(self.mono_handle, b"il2cpp_class_from_name_case")
        self.mono_class_from_name = MONO_CLASS_FROM_NAME_CASE(self.mono_handle, b"il2cpp_class_from_name")
        self.mono_class_get_name = MONO_CLASS_GET_NAME(self.mono_handle, b"il2cpp_class_get_name")
        self.mono_class_get_namespace = MONO_CLASS_GET_NAMESPACE(self.mono_handle, b"il2cpp_class_get_namespace")
        self.mono_class_get_methods = MONO_CLASS_GET_METHODS(self.mono_handle, b"il2cpp_class_get_methods")
        self.mono_class_get_method_from_name = MONO_CLASS_GET_METHOD_FROM_NAME(self.mono_handle, b"il2cpp_class_get_method_from_name")
        self.mono_class_get_fields = MONO_CLASS_GET_FIELDS(self.mono_handle, b"il2cpp_class_get_fields")
        self.mono_class_get_field_from_name = MONO_CLASS_GET_FIELD_FROM_NAME(self.mono_handle, b"il2cpp_class_get_field_from_name")
        self.mono_class_get_interfaces = MONO_CLASS_GET_INTERFACES(self.mono_handle, b"il2cpp_class_get_interfaces")
        self.mono_class_get_properties = MONO_CLASS_GET_PROPERTIES(self.mono_handle, b"il2cpp_class_get_properties")
        self.mono_class_get_property_from_name = MONO_CLASS_GET_PROPERTY_FROM_NAME(self.mono_handle, b"il2cpp_class_get_property_from_name")
        self.mono_class_get_parent = MONO_CLASS_GET_PARENT(self.mono_handle, b"il2cpp_class_get_parent")
        self.mono_class_get_image = MONO_CLASS_GET_IMAGE(self.mono_handle, b"il2cpp_class_get_image")

        self.mono_class_is_generic = MONO_CLASS_IS_GENERIC(self.mono_handle, b"il2cpp_class_is_generic")
        self.mono_class_is_enum = MONO_CLASS_IS_ENUM(self.mono_handle, b"il2cpp_class_is_enum")
        self.mono_class_is_valuetype = MONO_CLASS_IS_VALUETYPE(self.mono_handle, b"il2cpp_class_is_valuetype")
        self.mono_class_is_subclass_of = MONO_CLASS_IS_SUBCLASS_OF(self.mono_handle, b"il2cpp_class_is_subclass_of")
        self.mono_class_vtable = MONO_CLASS_VTABLE(self.mono_handle, b"il2cpp_class_vtable")
        self.mono_class_from_mono_type = MONO_CLASS_FROM_MONO_TYPE(self.mono_handle, b"il2cpp_class_from_mono_type")
        self.mono_class_get_element_class = MONO_CLASS_GET_ELEMENT_CLASS(self.mono_handle, b"il2cpp_class_get_element_class")
        self.mono_class_instance_size = MONO_CLASS_INSTANCE_SIZE(self.mono_handle, b"il2cpp_class_instance_size")

        self.mono_class_num_fields = MONO_CLASS_NUM_FIELDS(self.mono_handle, b"il2cpp_class_num_fields")
        self.mono_class_num_methods = MONO_CLASS_NUM_METHODS(self.mono_handle, b"il2cpp_class_num_methods")

        self.mono_field_get_name = MONO_FIELD_GET_NAME(self.mono_handle, b"il2cpp_field_get_name")
        self.mono_field_get_type = MONO_FIELD_GET_TYPE(self.mono_handle, b"il2cpp_field_get_type")
        self.mono_field_get_parent = MONO_FIELD_GET_PARENT(self.mono_handle, b"il2cpp_field_get_parent")
        self.mono_field_get_offset = MONO_FIELD_GET_OFFSET(self.mono_handle, b"il2cpp_field_get_offset")
        self.mono_field_get_flags = MONO_FIELD_GET_FLAGS(self.mono_handle, b"il2cpp_field_get_flags")
        self.mono_field_get_value_object = MONO_FIELD_GET_VALUE_OBJECT(self.mono_handle, b"il2cpp_field_get_value_object")

        self.mono_property_get_name = MONO_PROPERTY_GET_NAME(self.mono_handle, b"il2cpp_property_get_name")
        self.mono_property_get_get_method = MONO_PROPERTY_GET_GET_METHOD(self.mono_handle, b"il2cpp_property_get_get_method")
        self.mono_property_get_set_method = MONO_PROPERTY_GET_SET_METHOD(self.mono_handle, b"il2cpp_property_get_set_method")
        self.mono_property_get_parent = MONO_PROPERTY_GET_PARENT(self.mono_handle, b"il2cpp_property_get_parent")
        self.mono_property_get_flags = MONO_PROPERTY_GET_FLAGS(self.mono_handle, b"il2cpp_property_get_flags")

        self.mono_type_get_name = MONO_TYPE_GET_NAME(self.mono_handle, b"il2cpp_type_get_name")
        self.mono_type_get_type = MONO_TYPE_GET_TYPE(self.mono_handle, b"il2cpp_type_get_type")
        self.mono_type_get_name_full = MONO_TYPE_GET_NAME_FULL(self.mono_handle, b"il2cpp_type_get_name_full")
        self.mono_type_is_byref = MONO_TYPE_IS_BYREF(self.mono_handle, b"il2cpp_type_is_byref")
        self.il2cpp_type_get_object = IL2CPP_TYPE_GET_OBJECT(self.mono_handle, b"il2cpp_type_get_object")
        self.il2cpp_method_get_object = IL2CPP_METHOD_GET_OBJECT(self.mono_handle, b"il2cpp_method_get_object")

        self.mono_method_get_name = MONO_METHOD_GET_NAME(self.mono_handle, b"il2cpp_method_get_name")
        self.mono_method_get_full_name = (MONO_METHOD_GET_FULL_NAME(self.mono_handle, b"il2cpp_method_get_full_name") or
                                          MONO_METHOD_GET_FULL_NAME(self.mono_handle, b"mono_method_full_name") or
                                          MONO_METHOD_GET_FULL_NAME(self.mono_handle, b"mono_method_get_full_name"))
        self.mono_method_get_class = MONO_METHOD_GET_CLASS(self.mono_handle, b"il2cpp_method_get_class")
        self.mono_method_get_header = MONO_METHOD_GET_HEADER(self.mono_handle, b"il2cpp_method_get_header")
        self.mono_method_get_flags = MONO_METHOD_GET_FLAGS(self.mono_handle, b"il2cpp_method_get_flags")
        self.mono_method_signature = MONO_METHOD_SIG(self.mono_handle, b"il2cpp_method_signature")
        self.mono_method_get_param_names = MONO_METHOD_GET_PARAM_NAMES(self.mono_handle, b"il2cpp_method_get_param_names")

        self.mono_signature_get_desc = MONO_SIGNATURE_GET_DESC(self.mono_handle, b"il2cpp_signature_get_desc")
        self.mono_signature_get_params = MONO_SIGNATURE_GET_PARAMS(self.mono_handle, b"il2cpp_signature_get_params")
        self.mono_signature_get_param_count = MONO_SIGNATURE_GET_PARAM_COUNT(self.mono_handle, b"il2cpp_signature_get_param_count")
        self.mono_signature_get_return_type = MONO_SIGNATURE_GET_RETURN_TYPE(self.mono_handle, b"il2cpp_signature_get_return_type")

        self.mono_compile_method = MONO_COMPILE_METHOD(self.mono_handle, b"il2cpp_compile_method")
        self.mono_free_method = MONO_FREE_METHOD(self.mono_handle, b"il2cpp_free_method")
        self.mono_jit_info_table_find = MONO_JIT_INFO_TABLE_FIND(self.mono_handle, b"il2cpp_jit_info_table_find")
        self.mono_jit_info_get_method = MONO_JIT_INFO_GET_METHOD(self.mono_handle, b"il2cpp_jit_info_get_method")
        self.mono_jit_info_get_code_start = MONO_JIT_INFO_GET_CODE_START(self.mono_handle, b"il2cpp_jit_info_get_code_start")
        self.mono_jit_info_get_code_size = MONO_JIT_INFO_GET_CODE_SIZE(self.mono_handle, b"il2cpp_jit_info_get_code_size")
        self.mono_jit_exec = MONO_JIT_EXEC(self.mono_handle, b"il2cpp_jit_exec")

        self.mono_method_header_get_code = MONO_METHOD_HEADER_GET_CODE(self.mono_handle, b"il2cpp_method_header_get_code")
        self.mono_disasm_code = MONO_DISASM_CODE(self.mono_handle, b"il2cpp_disasm_code")

        self.mono_vtable_get_static_field_data = MONO_VTABLE_GET_STATIC_FIELD_DATA(self.mono_handle, b"il2cpp_vtable_get_static_field_data")

        self.mono_method_desc_new = MONO_METHOD_DESC_NEW(self.mono_handle, b"il2cpp_method_desc_new")
        self.mono_method_desc_from_method = MONO_METHOD_DESC_FROM_METHOD(self.mono_handle, b"il2cpp_method_desc_from_method")
        self.mono_method_desc_free = MONO_METHOD_DESC_FREE(self.mono_handle, b"il2cpp_method_desc_free")

        self.mono_string_new = MONO_STRING_NEW(self.mono_handle, b"mono_string_new") or MONO_STRING_NEW(self.mono_handle, b"il2cpp_string_new")  # il2cpp also has b"mono_string_new". The il2cpp_string_new is a different function
        self.mono_string_to_utf8 = MONO_STRING_TO_UTF8(self.mono_handle, b"il2cpp_string_to_utf8")
        self.il2cpp_array_new = IL2CPP_ARRAY_NEW(self.mono_handle, b"il2cpp_array_new")
        self.mono_array_element_size = MONO_ARRAY_ELEMENT_SIZE(self.mono_handle, b"il2cpp_array_element_size")
        self.mono_class_get_rank = MONO_CLASS_GET_RANK(self.mono_handle, b"il2cpp_class_get_rank")
        self.mono_value_box = MONO_VALUE_BOX(self.mono_handle, b"il2cpp_value_box")
        self.mono_object_unbox = MONO_OBJECT_UNBOX(self.mono_handle, b"il2cpp_object_unbox")
        self.mono_object_new = MONO_OBJECT_NEW(self.mono_handle, b"il2cpp_object_new")
        self.mono_object_to_string = MONO_OBJECT_TO_STRING(self.mono_handle, b"il2cpp_object_to_string")
        self.mono_class_get_type = MONO_CLASS_GET_TYPE(self.mono_handle, b"il2cpp_class_get_type")
        self.mono_type_get_class = MONO_TYPE_GET_CLASS(self.mono_handle, b"il2cpp_type_get_class") or MONO_TYPE_GET_CLASS(self.mono_handle, b"il2cpp_type_get_class_or_element_class")

        self.mono_method_desc_search_in_image = MONO_METHOD_DESC_SEARCH_IN_IMAGE(self.mono_handle, b"il2cpp_method_desc_search_in_image")
        self.mono_runtime_invoke = MONO_RUNTIME_INVOKE(self.mono_handle, b"il2cpp_runtime_invoke")
        self.mono_runtime_object_init = MONO_RUNTIME_OBJECT_INIT(self.mono_handle, b"il2cpp_runtime_object_init")

        self.mono_ptr_class_get = MONO_PTR_GET_CLASS(self.mono_handle, b"il2cpp_ptr_class_get") or MONO_PTR_GET_CLASS(self.mono_handle, b"mono_ptr_class_get")

        self.mono_type_get_ptr_type = MONO_PTR_GET_CLASS(self.mono_handle, b"il2cpp_type_get_ptr_type") or MONO_PTR_GET_CLASS(self.mono_handle, b"mono_type_get_ptr_type")

        self.mono_assembly_name_new = MONO_ASSEMBLY_NAME_NEW(self.mono_handle, b"il2cpp_assembly_name_new")
        self.mono_assembly_loaded = MONO_ASSEMBLY_LOADED(self.mono_handle, b"il2cpp_assembly_loaded")
        self.mono_assembly_open = MONO_ASSEMBLY_OPEN(self.mono_handle, b"il2cpp_assembly_open")
        self.mono_image_open = MONO_IMAGE_OPEN(self.mono_handle, b"il2cpp_image_open")
        self.mono_image_get_filename = MONO_IMAGE_GET_FILENAME(self.mono_handle, b"il2cpp_image_get_filename")

        self.mono_class_get_nesting_type = MONO_CLASS_GET_NESTING_TYPE(self.mono_handle, b"mono_class_get_nesting_type") or MONO_CLASS_GET_NESTING_TYPE(self.mono_handle, b"il2cpp_class_get_nesting_type")
        self.mono_class_get_nested_types = MONO_CLASS_GET_NESTED_TYPES(self.mono_handle, b"mono_class_get_nested_types") or MONO_CLASS_GET_NESTED_TYPES(self.mono_handle, b"l2cpp_class_get_nested_types")

        self.il2cpp_field_static_get_value = IL2CPP_FIELD_STATIC_GET_VALUE(self.mono_handle, b"il2cpp_field_static_get_value")
        self.il2cpp_field_static_set_value = IL2CPP_FIELD_STATIC_SET_VALUE(self.mono_handle, b"il2cpp_field_static_set_value")

        self.il2cpp_domain_get_assemblies = IL2CPP_DOMAIN_GET_ASSEMBLIES(self.mono_handle, b"il2cpp_domain_get_assemblies")
        self.il2cpp_image_get_class_count = IL2CPP_IMAGE_GET_CLASS_COUNT(self.mono_handle, b"il2cpp_image_get_class_count")
        self.il2cpp_image_get_class = IL2CPP_IMAGE_GET_CLASS(self.mono_handle, b"il2cpp_image_get_class")

        self.il2cpp_type_get_name = IL2CPP_TYPE_GET_NAME(self.mono_handle, b"il2cpp_type_get_name")
        self.il2cpp_type_get_assembly_qualified_name = IL2CPP_TYPE_GET_ASSEMBLY_QUALIFIED_NAME(self.mono_handle, b"il2cpp_type_get_assembly_qualified_name")

        self.il2cpp_method_get_param_count = IL2CPP_METHOD_GET_PARAM_COUNT(self.mono_handle, b"il2cpp_method_get_param_count")
        self.il2cpp_method_get_param_name = IL2CPP_METHOD_GET_PARAM_NAME(self.mono_handle, b"il2cpp_method_get_param_name")
        self.il2cpp_method_get_param = IL2CPP_METHOD_GET_PARAM(self.mono_handle, b"il2cpp_method_get_param")
        self.il2cpp_method_get_return_type = IL2CPP_METHOD_GET_RETURN_TYPE(self.mono_handle, b"il2cpp_method_get_return_type")

        self.il2cpp_class_from_type = IL2CPP_CLASS_FROM_TYPE(self.mono_handle, b"il2cpp_class_from_type")
        self.il2cpp_string_chars = IL2CPP_STRING_CHARS(self.mono_handle, b"il2cpp_string_chars")

        self.mono_runtime_is_shutting_down = MONO_RUNTIME_IS_SHUTTING_DOWN(self.mono_handle, b"il2cpp_runtime_is_shutting_down") or MONO_RUNTIME_IS_SHUTTING_DOWN(self.mono_handle, b"mono_runtime_is_shutting_down")

    def _init_mono(self):
        self.g_free = (G_FREE(self.mono_handle, b"g_free") or
                       G_FREE(self.mono_handle, b"mono_unity_g_free") or
                       (lambda ptr: None))  # if all else fails, do nothing

        self.mono_free = MONO_FREE(self.mono_handle, b"mono_free")

        self.mono_get_root_domain = MONO_GET_ROOT_DOMAIN(self.mono_handle, b"mono_get_root_domain")
        self.mono_thread_attach = MONO_THREAD_ATTACH(self.mono_handle, b"mono_thread_attach")
        self.mono_thread_detach = MONO_THREAD_DETACH(self.mono_handle, b"mono_thread_detach")
        self.mono_thread_cleanup = MONO_THREAD_CLEANUP(self.mono_handle, b"mono_thread_cleanup")

        self.mono_object_get_class = MONO_OBJECT_GET_CLASS(self.mono_handle, b"mono_object_get_class")

        self.mono_domain_foreach = MONO_DOMAIN_FOREACH(self.mono_handle, b"mono_domain_foreach")
        self.mono_domain_set = MONO_DOMAIN_SET(self.mono_handle, b"mono_domain_set")
        self.mono_domain_get = MONO_DOMAIN_GET(self.mono_handle, b"mono_domain_get")
        self.mono_assembly_foreach = MONO_ASSEMBLY_FOREACH(self.mono_handle, b"mono_assembly_foreach")
        self.mono_assembly_get_image = MONO_ASSEMBLY_GET_IMAGE(self.mono_handle, b"mono_assembly_get_image")
        self.mono_image_get_assembly = MONO_IMAGE_GET_ASSEMBLY(self.mono_handle, b"mono_image_get_assembly")

        self.mono_image_get_name = MONO_IMAGE_GET_NAME(self.mono_handle, b"mono_image_get_name")
        self.mono_image_get_filename = MONO_IMAGE_GET_FILENAME(self.mono_handle, b"mono_image_get_filename")

        self.mono_image_get_table_info = MONO_IMAGE_GET_TABLE_INFO(self.mono_handle, b"mono_image_get_table_info")
        self.mono_image_rva_map = MONO_IMAGE_RVA_MAP(self.mono_handle, b"mono_image_rva_map")

        self.mono_table_info_get_rows = MONO_TABLE_INFO_GET_ROWS(self.mono_handle, b"mono_table_info_get_rows")
        self.mono_metadata_decode_row_col = MONO_METADATA_DECODE_ROW_COL(self.mono_handle, b"mono_metadata_decode_row_col")
        self.mono_metadata_string_heap = MONO_METADATA_STRING_HEAP(self.mono_handle, b"mono_metadata_string_heap")

        self.mono_class_get = MONO_CLASS_GET(self.mono_handle, b"mono_class_get")
        self.mono_class_from_typeref = MONO_CLASS_FROM_TYPEREF(self.mono_handle, b"mono_class_from_typeref")
        self.mono_class_name_from_token = MONO_CLASS_NAME_FROM_TOKEN(self.mono_handle, b"mono_class_name_from_token")
        self.mono_class_from_name_case = MONO_CLASS_FROM_NAME_CASE(self.mono_handle, b"mono_class_from_name_case")
        self.mono_class_from_name = MONO_CLASS_FROM_NAME_CASE(self.mono_handle, b"mono_class_from_name")
        self.mono_class_get_name = MONO_CLASS_GET_NAME(self.mono_handle, b"mono_class_get_name")
        self.mono_class_get_namespace = MONO_CLASS_GET_NAMESPACE(self.mono_handle, b"mono_class_get_namespace")
        self.mono_class_get_methods = MONO_CLASS_GET_METHODS(self.mono_handle, b"mono_class_get_methods")
        self.mono_class_get_method_from_name = MONO_CLASS_GET_METHOD_FROM_NAME(self.mono_handle, b"mono_class_get_method_from_name")
        self.mono_class_get_fields = MONO_CLASS_GET_FIELDS(self.mono_handle, b"mono_class_get_fields")
        self.mono_class_get_field_from_name = MONO_CLASS_GET_FIELD_FROM_NAME(self.mono_handle, b"mono_class_get_field_from_name")
        self.mono_class_get_interfaces = MONO_CLASS_GET_INTERFACES(self.mono_handle, b"mono_class_get_interfaces")
        self.mono_class_get_properties = MONO_CLASS_GET_PROPERTIES(self.mono_handle, b"mono_class_get_properties")
        self.mono_class_get_property_from_name = MONO_CLASS_GET_PROPERTY_FROM_NAME(self.mono_handle, b"mono_class_get_property_from_name")
        self.mono_class_get_parent = MONO_CLASS_GET_PARENT(self.mono_handle, b"mono_class_get_parent")
        self.mono_class_get_image = MONO_CLASS_GET_IMAGE(self.mono_handle, b"mono_class_get_image")
        self.mono_class_is_generic = MONO_CLASS_IS_GENERIC(self.mono_handle, b"mono_class_is_generic")
        self.mono_class_is_enum = MONO_CLASS_IS_ENUM(self.mono_handle, b"mono_class_is_enum")
        self.mono_class_is_valuetype = MONO_CLASS_IS_VALUETYPE(self.mono_handle, b"mono_class_is_valuetype")
        self.mono_class_is_subclass_of = MONO_CLASS_IS_SUBCLASS_OF(self.mono_handle, b"mono_class_is_subclass_of")

        self.mono_class_vtable = MONO_CLASS_VTABLE(self.mono_handle, b"mono_class_vtable")
        self.mono_class_from_mono_type = MONO_CLASS_FROM_MONO_TYPE(self.mono_handle, b"mono_class_from_mono_type")
        self.mono_class_get_element_class = MONO_CLASS_GET_ELEMENT_CLASS(self.mono_handle, b"mono_class_get_element_class")
        self.mono_class_instance_size = MONO_CLASS_INSTANCE_SIZE(self.mono_handle, b"mono_class_instance_size")

        self.mono_class_num_fields = MONO_CLASS_NUM_FIELDS(self.mono_handle, b"mono_class_num_fields")
        self.mono_class_num_methods = MONO_CLASS_NUM_METHODS(self.mono_handle, b"mono_class_num_methods")

        self.mono_field_get_name = MONO_FIELD_GET_NAME(self.mono_handle, b"mono_field_get_name")
        self.mono_field_get_type = MONO_FIELD_GET_TYPE(self.mono_handle, b"mono_field_get_type")
        self.mono_field_get_parent = MONO_FIELD_GET_PARENT(self.mono_handle, b"mono_field_get_parent")
        self.mono_field_get_offset = MONO_FIELD_GET_OFFSET(self.mono_handle, b"mono_field_get_offset")
        self.mono_field_get_flags = MONO_FIELD_GET_FLAGS(self.mono_handle, b"mono_field_get_flags")
        self.mono_field_get_value_object = MONO_FIELD_GET_VALUE_OBJECT(self.mono_handle, b"mono_field_get_value_object")

        self.mono_property_get_name = MONO_PROPERTY_GET_NAME(self.mono_handle, b"mono_property_get_name")
        self.mono_property_get_get_method = MONO_PROPERTY_GET_GET_METHOD(self.mono_handle, b"mono_property_get_get_method")
        self.mono_property_get_set_method = MONO_PROPERTY_GET_SET_METHOD(self.mono_handle, b"mono_property_get_set_method")
        self.mono_property_get_parent = MONO_PROPERTY_GET_PARENT(self.mono_handle, b"mono_property_get_parent")
        self.mono_property_get_flags = MONO_PROPERTY_GET_FLAGS(self.mono_handle, b"mono_property_get_flags")

        self.mono_type_get_name = MONO_TYPE_GET_NAME(self.mono_handle, b"mono_type_get_name")
        self.mono_type_get_type = MONO_TYPE_GET_TYPE(self.mono_handle, b"mono_type_get_type")
        self.mono_type_get_object = MONO_TYPE_GET_OBJECT(self.mono_handle, b"mono_type_get_object")
        self.mono_type_get_name_full = MONO_TYPE_GET_NAME_FULL(self.mono_handle, b"mono_type_get_name_full")
        self.mono_type_is_byref = MONO_TYPE_IS_BYREF(self.mono_handle, b"mono_type_is_byref")
        self.mono_method_get_object = MONO_METHOD_GET_OBJECT(self.mono_handle, b"mono_method_get_object")

        self.mono_method_get_name = MONO_METHOD_GET_NAME(self.mono_handle, b"mono_method_get_name")
        self.mono_method_get_full_name = MONO_METHOD_GET_FULL_NAME(self.mono_handle, b"mono_method_get_full_name")
        self.mono_method_get_class = MONO_METHOD_GET_CLASS(self.mono_handle, b"mono_method_get_class")
        self.mono_method_get_header = MONO_METHOD_GET_HEADER(self.mono_handle, b"mono_method_get_header")
        self.mono_method_get_flags = MONO_METHOD_GET_FLAGS(self.mono_handle, b"mono_method_get_flags")
        self.mono_method_signature = MONO_METHOD_SIG(self.mono_handle, b"mono_method_signature")
        self.mono_method_get_param_names = MONO_METHOD_GET_PARAM_NAMES(self.mono_handle, b"mono_method_get_param_names")

        self.mono_signature_get_desc = MONO_SIGNATURE_GET_DESC(self.mono_handle, b"mono_signature_get_desc")
        self.mono_signature_get_params = MONO_SIGNATURE_GET_PARAMS(self.mono_handle, b"mono_signature_get_params")
        self.mono_signature_get_param_count = MONO_SIGNATURE_GET_PARAM_COUNT(self.mono_handle, b"mono_signature_get_param_count")
        self.mono_signature_get_return_type = MONO_SIGNATURE_GET_RETURN_TYPE(self.mono_handle, b"mono_signature_get_return_type")

        self.mono_compile_method = MONO_COMPILE_METHOD(self.mono_handle, b"mono_compile_method")
        self.mono_free_method = MONO_FREE_METHOD(self.mono_handle, b"mono_free_method")
        self.mono_jit_info_table_find = MONO_JIT_INFO_TABLE_FIND(self.mono_handle, b"mono_jit_info_table_find")
        self.mono_jit_info_get_method = MONO_JIT_INFO_GET_METHOD(self.mono_handle, b"mono_jit_info_get_method")
        self.mono_jit_info_get_code_start = MONO_JIT_INFO_GET_CODE_START(self.mono_handle, b"mono_jit_info_get_code_start")
        self.mono_jit_info_get_code_size = MONO_JIT_INFO_GET_CODE_SIZE(self.mono_handle, b"mono_jit_info_get_code_size")
        self.mono_jit_exec = MONO_JIT_EXEC(self.mono_handle, b"mono_jit_exec")

        self.mono_method_header_get_code = MONO_METHOD_HEADER_GET_CODE(self.mono_handle, b"mono_method_header_get_code")
        self.mono_disasm_code = MONO_DISASM_CODE(self.mono_handle, b"mono_disasm_code")

        self.mono_vtable_get_static_field_data = MONO_VTABLE_GET_STATIC_FIELD_DATA(self.mono_handle, b"mono_vtable_get_static_field_data")

        self.mono_method_desc_new = MONO_METHOD_DESC_NEW(self.mono_handle, b"mono_method_desc_new")
        self.mono_method_desc_from_method = MONO_METHOD_DESC_FROM_METHOD(self.mono_handle, b"mono_method_desc_from_method")
        self.mono_method_desc_free = MONO_METHOD_DESC_FREE(self.mono_handle, b"mono_method_desc_free")

        self.mono_string_new = MONO_STRING_NEW(self.mono_handle, b"mono_string_new")
        self.mono_string_to_utf8 = MONO_STRING_TO_UTF8(self.mono_handle, b"mono_string_to_utf8")
        self.mono_array_new = MONO_ARRAY_NEW(self.mono_handle, b"mono_array_new")
        self.mono_array_element_size = MONO_ARRAY_ELEMENT_SIZE(self.mono_handle, b"mono_array_element_size")
        self.mono_class_get_rank = MONO_CLASS_GET_RANK(self.mono_handle, b"mono_class_get_rank")
        self.mono_value_box = MONO_VALUE_BOX(self.mono_handle, b"mono_value_box")
        self.mono_object_unbox = MONO_OBJECT_UNBOX(self.mono_handle, b"mono_object_unbox")
        self.mono_object_new = MONO_OBJECT_NEW(self.mono_handle, b"mono_object_new")
        self.mono_object_to_string = MONO_OBJECT_TO_STRING(self.mono_handle, b"mono_object_to_string")
        self.mono_object_isinst = MONO_OBJECT_ISINST(self.mono_handle, b"mono_object_isinst")
        self.mono_get_enum_class = MONO_GET_ENUM_CLASS(self.mono_handle, b"mono_get_enum_class")

        self.mono_class_get_type = MONO_CLASS_GET_TYPE(self.mono_handle, b"mono_class_get_type")
        self.mono_type_get_class = MONO_TYPE_GET_CLASS(self.mono_handle, b"mono_type_get_class")
        self.mono_class_get_nesting_type = MONO_CLASS_GET_NESTING_TYPE(self.mono_handle, b"mono_class_get_nesting_type")
        self.mono_class_get_nested_types = MONO_CLASS_GET_NESTED_TYPES(self.mono_handle, b"mono_class_get_nested_types")

        self.mono_method_desc_search_in_image = MONO_METHOD_DESC_SEARCH_IN_IMAGE(self.mono_handle, b"mono_method_desc_search_in_image")
        self.mono_runtime_invoke = MONO_RUNTIME_INVOKE(self.mono_handle, b"mono_runtime_invoke")
        self.mono_runtime_object_init = MONO_RUNTIME_OBJECT_INIT(self.mono_handle, b"mono_runtime_object_init")

        self.mono_ptr_class_get = MONO_PTR_GET_CLASS(self.mono_handle, b"mono_ptr_class_get")
        self.mono_type_get_ptr_type = MONO_PTR_GET_CLASS(self.mono_handle, b"mono_type_get_ptr_type")

        self.mono_assembly_name_new = MONO_ASSEMBLY_NAME_NEW(self.mono_handle, b"mono_assembly_name_new")
        self.mono_assembly_loaded = MONO_ASSEMBLY_LOADED(self.mono_handle, b"mono_assembly_loaded")
        self.mono_assembly_open = MONO_ASSEMBLY_OPEN(self.mono_handle, b"mono_assembly_open")
        self.mono_image_open = MONO_IMAGE_OPEN(self.mono_handle, b"mono_image_open")

        self.mono_field_static_get_value = MONO_FIELD_STATIC_GET_VALUE(self.mono_handle, b"mono_field_static_get_value")
        self.mono_field_static_set_value = MONO_FIELD_STATIC_SET_VALUE(self.mono_handle, b"mono_field_static_set_value")

        self.mono_runtime_is_shutting_down = MONO_RUNTIME_IS_SHUTTING_DOWN(self.mono_handle, b"mono_runtime_is_shutting_down")

    def __getattr__(self, item):
        # return none if the attribute is not found
        return None

    def imgui_render_api_table(self):
        if getattr(self, '_cached_api_table', None) is None:
            self._cached_api_table = {}
            for name in dir(self):
                o = getattr(self, name)
                if isinstance(o, _MonoApi):
                    self._cached_api_table[name] = o
        from nylib.pyimgui import imgui
        from nylib.pyimgui.imgui import ctx as imgui_ctx

        with imgui_ctx.BeginTable("mono_api_table", 3) as show:
            if show:
                imgui.TableNextRow()
                imgui.TableNextColumn()
                imgui.Text("Is IL2CPP")
                imgui.TableNextColumn()
                imgui.Text(str(self.is_il2cpp))

                imgui.TableNextRow()
                imgui.TableNextColumn()
                imgui.Text("Module Handle")
                imgui.TableNextColumn()
                imgui.Text(f"{self.mono_handle:X}")

                for name, o in self._cached_api_table.items():
                    imgui.TableNextRow()
                    imgui.TableNextColumn()
                    imgui.Text(name)
                    imgui.TableNextColumn()
                    imgui.Text(o.function)
                    imgui.TableNextColumn()
                    imgui.Text(f"{o.func_ptr or 0:X}")
