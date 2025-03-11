import typing

from nylib import imguiutils
from nylib.pyimgui import imgui
from . import *

_T = typing.TypeVar('_T')


class _MonoInspector(imguiutils.Inspector[_T]):
    def item_name(self, item):
        return item[0]

    def on_item_selected(self, item):
        super().on_item_selected(item)
        self.selected_inspector = None
        if item is None: return
        _, t = item
        if isinstance(t, str):
            imgui.SetClipboardText(t)
        elif isinstance(t, MonoType):
            if cls := t.cls or t.cls_from_ptr:
                self.selected_inspector = MonoClassInspector(cls)
        elif isinstance(t, MonoField):
            self.selected_inspector = MonoFieldInspector(t)
        elif isinstance(t, MonoMethod):
            self.selected_inspector = MonoMethodInspector(t)
        elif isinstance(t, MonoClass_):
            self.selected_inspector = MonoClassInspector(t)
        elif isinstance(t, MonoImage):
            self.selected_inspector = MonoImageInspector(t)


class MonoMethodInspector(_MonoInspector[MonoMethod]):
    def init_items(self):
        return [
            [
                *[
                    (f"{i}({MonoTypeEnum(param.type.type).name}): {param.type.name} {param.name}", param.type)
                    for i, param in enumerate(self.target.params)
                ],
                (f"=> ({MonoTypeEnum(self.target.return_type.type)}) {self.target.return_type.name}", self.target.return_type),
            ]
        ]


class MonoFieldInspector(_MonoInspector[MonoField]):
    def init_items(self):
        return [
            [
                (f"name: {self.target.name}", self.target.name),
                (f"type: {self.target.type.name}", self.target.type),
                (f"offset: {self.target.offset:#X}", f"{self.target.offset:#x}"),
                (f"flags: {self.target.flags:#X}", f"{self.target.flags:#x}")
            ]
        ]


class MonoClassInspector(_MonoInspector[MonoClass_]):
    def init_items(self):
        return [
            [(f"{field.type.name} {field.name}", field) for field in self.target.fields],
            [(method.name + f"({','.join(p.type.name for p in method.params)})", method) for method in self.target.methods]
        ]


class MonoImageInspector(_MonoInspector[MonoImage]):
    def init_items(self):
        return [
            [(f"{cls.namespace}::{cls.name}", cls) for cls in self.target.clss]
        ]


class MonoInspector(_MonoInspector[Mono]):
    def init_items(self):
        return [
            [(asm.image.name, asm.image) for asm in self.target.assemblies]
        ]
