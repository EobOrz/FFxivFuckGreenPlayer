import ctypes
import enum
import functools
import typing

from .defines import *
from .defines import _MonoObj
from .type_cast import py2mono, mono2py


class MonoObject_(_MonoObj):
    def init(self):
        MonoApi.get_instance().mono_runtime_object_init(self.ptr)

    @functools.cached_property
    def cls(self):
        return MonoClass_(MonoApi.get_instance().mono_object_get_class(self.ptr))

    def unbox(self):
        return MonoApi.get_instance().mono_object_unbox(self.ptr)


class MonoMethodHeader(_MonoObj):
    @functools.cached_property
    def il_code(self):
        res = MonoApi.get_instance().mono_method_header_get_code(self.ptr, ctypes.byref(code := ctypes.c_uint32()), None)
        return res, code.value


class MonoReflectionType_(_MonoObj):
    pass


class MonoType(_MonoObj):
    @functools.cached_property
    def name(self) -> str:
        return MonoApi.get_instance().mono_type_get_name(self.ptr).decode('utf-8')

    @functools.cached_property
    def cls(self):
        # mono_class_from_mono_type?
        return MonoClass_(MonoApi.get_instance().mono_type_get_class(self.ptr))

    @functools.cached_property
    def cls_from_ptr(self):
        return MonoClass_(MonoApi.get_instance().mono_ptr_class_get(self.ptr))

    @functools.cached_property
    def type_from_ptr(self):
        return MonoType(MonoApi.get_instance().mono_type_get_ptr_type(self.ptr))

    @functools.cached_property
    def type(self) -> int:
        return MonoTypeEnum(MonoApi.get_instance().mono_type_get_type(self.ptr))

    @functools.cached_property
    def reflect_type(self):
        api = MonoApi.get_instance()
        if api.is_il2cpp:
            return MonoReflectionType_(api.il2cpp_type_get_object(self.ptr))
        else:
            return MonoReflectionType_(api.mono_type_get_object(api.mono_get_root_domain(), self.ptr))


class MonoField(_MonoObj):
    @functools.cached_property
    def type(self):
        return MonoType(MonoApi.get_instance().mono_field_get_type(self.ptr))

    @functools.cached_property
    def name(self) -> str:
        return MonoApi.get_instance().mono_field_get_name(self.ptr).decode('utf-8')

    @functools.cached_property
    def parent(self):
        return MonoClass_(MonoApi.get_instance().mono_field_get_parent(self.ptr))

    @functools.cached_property
    def offset(self):
        return MonoApi.get_instance().mono_field_get_offset(self.ptr)

    @functools.cached_property
    def flags(self):
        return MonoApi.get_instance().mono_field_get_flags(self.ptr)

    def get_value_addr(self, instance: 'MonoObject_' = None):
        if self.flags & MONO_FIELD_ATTR_STATIC:
            assert self.offset >= 0, "special static field not supported"
            return self.parent.static_field_data + self.offset
        else:
            if instance is None:
                raise ValueError('instance required')
            return instance.ptr + self.offset


class MonoProperty(_MonoObj):
    @functools.cached_property
    def name(self) -> str:
        return MonoApi.get_instance().mono_property_get_name(self.ptr).decode('utf-8')

    @functools.cached_property
    def flags(self):
        return MonoApi.get_instance().mono_property_get_flags(self.ptr)

    @functools.cached_property
    def get_method(self):
        return MonoMethod(MonoApi.get_instance().mono_property_get_get_method(self.ptr))

    @functools.cached_property
    def set_method(self):
        return MonoMethod(MonoApi.get_instance().mono_property_get_set_method(self.ptr))

    @functools.cached_property
    def parent(self):
        return MonoClass_(MonoApi.get_instance().mono_property_get_parent(self.ptr))


class MonoReflectionMethod(_MonoObj):
    pass


class MonoMethod(_MonoObj):
    class ParamType(typing.NamedTuple):
        name: str
        type: MonoType

        def __repr__(self):
            return f"{self.type.name} {self.name}"

    @functools.cached_property
    def name(self) -> str:
        return MonoApi.get_instance().mono_method_get_name(self.ptr).decode('utf-8')

    @functools.cached_property
    def full_name(self) -> str:
        return MonoApi.get_instance().mono_method_get_full_name(self.ptr).decode('utf-8')

    @functools.cached_property
    def flags(self):
        return MonoApi.get_instance().mono_method_get_flags(self.ptr, None)

    @functools.cached_property
    def cls(self):
        return MonoClass_(MonoApi.get_instance().mono_method_get_class(self.ptr))

    @functools.cached_property
    def header(self):
        return MonoMethodHeader(MonoApi.get_instance().mono_method_get_header(self.ptr))

    @functools.cached_property
    def param_count(self):
        api = MonoApi.get_instance()
        if api.is_il2cpp:
            return api.il2cpp_method_get_param_count(self.ptr)
        sign = api.mono_method_signature(self.ptr)
        return api.mono_signature_get_param_count(sign)

    @functools.cached_property
    def params(self) -> tuple[ParamType, ...]:
        api = MonoApi.get_instance()
        res = []
        if api.is_il2cpp:
            for i in range(api.il2cpp_method_get_param_count(self.ptr)):
                res.append(self.ParamType(
                    name=api.il2cpp_method_get_param_name(self.ptr, i).decode('utf-8'),
                    type=MonoType(api.il2cpp_method_get_param(self.ptr, i))
                ))
        else:
            sign = api.mono_method_signature(self.ptr)
            param_count = api.mono_signature_get_param_count(sign)
            names = (ctypes.c_char_p * param_count)()
            api.mono_method_get_param_names(self.ptr, names)
            it = ctypes.c_void_p(0)
            for i in range(param_count):
                res.append(self.ParamType(
                    name=names[i].decode('utf-8'),
                    type=MonoType(api.mono_signature_get_params(sign, ctypes.byref(it)))
                ))
        return tuple(res)

    @functools.cached_property
    def return_type(self):
        api = MonoApi.get_instance()
        if api.is_il2cpp:
            return MonoType(api.il2cpp_method_get_return_type(self.ptr))
        return MonoType(api.mono_signature_get_return_type(api.mono_method_signature(self.ptr)))

    @functools.cached_property
    def signature(self):
        s_ret = self.return_type.name
        s_params = ', '.join(param.type.name for param in self.params)
        return f"{s_ret} {self.name}({s_params})"

    def get_reflection_method(self, cls: 'MonoClass_' = None):
        api = MonoApi.get_instance()
        if api.is_il2cpp:
            return api.il2cpp_method_get_object(self.ptr, cls.ptr if cls else None)
        return MonoReflectionMethod(api.mono_method_get_object(api.mono_get_root_domain(), self.ptr, cls.ptr if cls else None))

    def compile(self):
        api = MonoApi.get_instance()
        if api.is_il2cpp:
            return self.ptr
        cls = self.cls
        if api.mono_class_is_generic(cls.ptr):
            return api.mono_compile_method(self.ptr)
        return None

    def free(self):
        MonoApi.get_instance().mono_free_method(self.ptr)

    def disasm(self):
        api = MonoApi.get_instance()
        if api.is_il2cpp:
            raise NotImplementedError('il2cpp disasm not implemented')
        il_code, code = self.header.il_code
        disassembly = api.mono_disasm_code(None, self.ptr, il_code, il_code + code)
        return disassembly.decode('utf-8')

    def invoke(self, this: int | MonoObject_ = None, *args):
        if this is None:
            this = 0
        elif isinstance(this, MonoObject_):
            this = this.ptr

        param_count = self.param_count
        if len(args) != param_count:
            raise ValueError(f'args length not match, expect {param_count}, got {len(args)}')

        p_params = None
        if args:
            keeper = []
            params = (ctypes.c_size_t * (param_count + 1))()
            for i, (param, arg) in enumerate(zip(self.params, args)):
                params[i] = py2mono(param.type.type, arg, keeper)
            p_params = ctypes.cast(params, ctypes.c_void_p)

        c_exception = ctypes.c_void_p(0)
        api = MonoApi.get_instance()
        raw_res = api.mono_runtime_invoke(self.ptr, this, p_params, c_exception)
        if c_exception.value:
            if exc := api.mono_object_to_string(c_exception, ctypes.byref(c_exception)):
                exc = api.mono_string_to_utf8(exc)
                raise RuntimeError(exc.decode('utf-8'))
            raise RuntimeError('unknown exception')
        return mono2py(self.return_type.type, raw_res)


class MonoVtable(_MonoObj):
    @functools.cached_property
    def static_field_data(self):
        return MonoApi.get_instance().mono_vtable_get_static_field_data(self.ptr)


class MonoClass_(_MonoObj):
    def new_object(self):
        api = MonoApi.get_instance()
        if api.is_il2cpp:
            return MonoObject_(api.mono_object_new(self.ptr, self.ptr))
        else:
            domain = (api.mono_get_root_domain or api.mono_domain_get)()
            return MonoObject_(api.mono_object_new(domain, self.ptr))

    @functools.cached_property
    def namespace(self) -> str:
        return MonoApi.get_instance().mono_class_get_namespace(self.ptr).decode('utf-8')

    @functools.cached_property
    def name(self) -> str:
        return MonoApi.get_instance().mono_class_get_name(self.ptr).decode('utf-8')

    @functools.cached_property
    def image(self):
        return MonoImage(MonoApi.get_instance().mono_class_get_image(self.ptr))

    @functools.cached_property
    def type(self):
        return MonoType(MonoApi.get_instance().mono_class_get_type(self.ptr))

    @functools.cached_property
    def parent(self):
        return MonoClass_(MonoApi.get_instance().mono_class_get_parent(self.ptr))

    @functools.cached_property
    def vtable(self):
        return self.get_vtable()

    def get_vtable(self, domain: "MonoDomain" = None):
        api = MonoApi.get_instance()
        return MonoVtable(api.mono_class_vtable(domain.ptr if domain else api.mono_get_root_domain(), self.ptr))

    @functools.cached_property
    def static_field_data(self):
        return self.get_static_field_data()

    def get_static_field_data(self, domain: "MonoDomain" = None):
        return self.get_vtable(domain).static_field_data

    @functools.cached_property
    def nesting_type(self):
        return MonoClass_(MonoApi.get_instance().mono_class_get_nesting_type(self.ptr))

    @functools.cached_property
    def rank(self):
        return MonoApi.get_instance().mono_class_get_rank(self.ptr)

    @functools.cached_property
    def element_class(self):
        if self.rank:
            return MonoClass_(MonoApi.get_instance().mono_class_get_element_class(self.ptr))

    @functools.cached_property
    def nested_types(self):
        api = MonoApi.get_instance()
        it = ctypes.c_size_t(0)
        res = []
        while nested := api.mono_class_get_nested_types(self.ptr, ctypes.byref(it)):
            res.append(nested)
        return tuple(res)

    @functools.cached_property
    def fields(self) -> tuple[MonoField, ...]:
        api = MonoApi.get_instance()
        it = ctypes.c_size_t(0)
        res = []
        while field := api.mono_class_get_fields(self.ptr, ctypes.byref(it)):
            res.append(MonoField(field))
        return tuple(res)

    @functools.cached_property
    def implemented_interfaces(self) -> tuple:
        api = MonoApi.get_instance()
        it = ctypes.c_size_t(0)
        res = []
        while interface := api.mono_class_get_interfaces(self.ptr, ctypes.byref(it)):
            res.append(interface)
        return tuple(res)

    @functools.cached_property
    def methods(self) -> tuple[MonoMethod, ...]:
        api = MonoApi.get_instance()
        it = ctypes.c_size_t(0)
        res = []
        while method := api.mono_class_get_methods(self.ptr, ctypes.byref(it)):
            res.append(MonoMethod(method))
        return tuple(res)

    def find_method(self, methodname: str, param_count: int = -1) -> MonoMethod | None:
        return MonoMethod(MonoApi.get_instance().mono_class_get_method_from_name(
            self.ptr, methodname.encode('utf-8'), param_count
        ))


class MonoJitInfo(_MonoObj):
    @functools.cached_property
    def method(self):
        return MonoMethod(MonoApi.get_instance().mono_jit_info_get_method(self.ptr))

    @functools.cached_property
    def code_start(self):
        return MonoApi.get_instance().mono_jit_info_get_code_start(self.ptr)

    @functools.cached_property
    def code_size(self):
        return MonoApi.get_instance().mono_jit_info_get_code_size(self.ptr)


class MonoDomain(_MonoObj):
    def set(self):
        api = MonoApi.get_instance()
        return api.mono_domain_set(self.ptr, False) if not api.mono_domain_set else 0

    def get_jit_info(self, address):
        return MonoJitInfo(MonoApi.get_instance().mono_jit_info_table_find(self.ptr, address))


class MonoAssembly(_MonoObj):
    @functools.cached_property
    def image(self):
        return MonoImage(MonoApi.get_instance().mono_assembly_get_image(self.ptr))


class MonoImage(_MonoObj):
    @functools.cached_property
    def name(self) -> str:
        return MonoApi.get_instance().mono_image_get_name(self.ptr).decode('utf-8')

    @functools.cached_property
    def filename(self) -> str:
        return MonoApi.get_instance().mono_image_get_filename(self.ptr).decode('utf-8')

    def get_rva_map(self, i):
        return MonoApi.get_instance().mono_image_rva_map(self.ptr, i)

    @functools.cached_property
    def clss(self) -> tuple[MonoClass_, ...]:
        api = MonoApi.get_instance()
        res = []
        if api.is_il2cpp:
            for i in range(api.il2cpp_image_get_class_count(self.ptr)):
                res.append(MonoClass_(api.il2cpp_image_get_class(self.ptr, i)))
        else:
            tdef = api.mono_image_get_table_info(self.ptr, MONO_TABLE_TYPEDEF)
            for i in range(api.mono_table_info_get_rows(tdef)):
                res.append(MonoClass_(api.mono_class_get(self.ptr, MONO_TABLE_TYPEDEF | (i + 1))))
        return tuple(res)

    def find_class(self, classname: str, namespace: str = '') -> MonoClass_ | None:
        api = MonoApi.get_instance()
        return MonoClass_((api.mono_class_from_name_case or api.mono_class_from_name)(
            self.ptr, namespace.encode('utf-8'), classname.encode('utf-8')
        ))

    def find_method_by_desc(self, fqMethodName: str):
        api = MonoApi.get_instance()
        mmd = api.mono_method_desc_new(fqMethodName.encode('utf-8'), 1)
        return MonoMethod(api.mono_method_desc_search_in_image(mmd, self.ptr))


class Mono:
    instance: 'Mono'

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
        if hasattr(self, 'api'):  return
        self.api = MonoApi(mono_handle, is_il2cpp)
        self.is_il2cpp = self.api.is_il2cpp
        self.domain = self.api.mono_get_root_domain()

        # self.mono_selfthread = None
        # self.is_attached = False
        # self.uwp_mode = False

    def connect_thread_to_mono_runtime(self):
        return self.api.mono_thread_attach(self.api.mono_get_root_domain())

    @functools.cached_property
    def domains(self) -> tuple[MonoDomain, ...]:
        if self.is_il2cpp:
            return MonoDomain(self.api.mono_domain_get()),
        domains = []
        c_iterator = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)(lambda domain: domains.append(MonoDomain(domain)))
        self.api.mono_domain_foreach(c_iterator)
        return tuple(domains)

    @functools.cached_property
    def assemblies(self) -> tuple[MonoAssembly, ...]:
        res = []
        if self.is_il2cpp:
            ptr = self.api.il2cpp_domain_get_assemblies(self.api.mono_domain_get(), ctypes.byref(cnt := ctypes.c_size_t()))
            for i in range(cnt.value):
                res.append(MonoAssembly(ptr[i]))
        else:
            c_iterator = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)(lambda assembly: res.append(MonoAssembly(assembly)))
            self.api.mono_assembly_foreach(c_iterator, None)
        return tuple(res)

    def find_class(self, classname: str, namespace: str = '') -> MonoClass_ | None:
        for assembly in self.assemblies:
            if cls := assembly.image.find_class(classname, namespace):
                return cls
