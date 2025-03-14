from __future__ import annotations
import typing
from . import detours
from . import gUtils
from . import imgui
__all__ = ['Dx10Inbound', 'Dx10Render', 'Dx10Window', 'Dx11Inbound', 'Dx11TextureHelper', 'Dx11Window', 'Dx12Inbound', 'Dx12Render', 'Dx12TextureHelper', 'Dx12Window', 'Dx9Inbound', 'Dx9Window', 'detours', 'gUtils', 'imgui']
class Dx10Inbound(Dx10Render):
    def Attach(self) -> None:
        ...
    def Detach(self) -> None:
        ...
    def __init__(self, arg0: typing.Callable) -> None:
        ...
class Dx10Render:
    def Close(self) -> None:
        ...
    def __init__(self, arg0: typing.Callable) -> None:
        ...
class Dx10Window(Dx10Render):
    ClearColor: imgui.ImVec4
    def Serve(self) -> None:
        ...
    def __init__(self, arg0: typing.Callable) -> None:
        ...
class Dx11Inbound(_Dx11Render):
    def Attach(self) -> None:
        ...
    def Detach(self) -> None:
        ...
    def __init__(self, renderCallback: typing.Callable = None) -> None:
        ...
    @property
    def isInLogic(self) -> bool:
        ...
class Dx11TextureHelper:
    def LoadTextureFromFile(self, arg0: str) -> None:
        ...
    def __bool__(self) -> bool:
        ...
    @property
    def handle(self) -> int:
        ...
    @property
    def height(self) -> int:
        ...
    @property
    def size(self) -> imgui.ImVec2:
        ...
    @property
    def width(self) -> int:
        ...
class Dx11Window(_Dx11Render):
    ClearColor: imgui.ImVec4
    def Serve(self) -> None:
        ...
    def __init__(self, renderCallback: typing.Callable = None) -> None:
        ...
class Dx12Inbound(Dx12Render):
    def Attach(self) -> None:
        ...
    def Detach(self) -> None:
        ...
    def __init__(self, arg0: typing.Callable) -> None:
        ...
    @property
    def isInLogic(self) -> bool:
        ...
class Dx12Render(_RenderBase):
    @staticmethod
    def CreateDeviceObjects() -> bool:
        ...
    @staticmethod
    def InvalidateDeviceObjects() -> None:
        ...
    @typing.overload
    def CreateTexture(self, arg0: str) -> Dx12TextureHelper:
        ...
    @typing.overload
    def CreateTexture(self) -> Dx12TextureHelper:
        ...
class Dx12TextureHelper:
    def LoadTextureFromFile(self, arg0: str) -> None:
        ...
    def __bool__(self) -> bool:
        ...
    @property
    def handle(self) -> int:
        ...
    @property
    def height(self) -> int:
        ...
    @property
    def size(self) -> imgui.ImVec2:
        ...
    @property
    def width(self) -> int:
        ...
class Dx12Window(Dx12Render):
    ClearColor: imgui.ImVec4
    def Serve(self) -> None:
        ...
    def __init__(self, arg0: typing.Callable) -> None:
        ...
class Dx9Inbound(_Dx9Render):
    def Attach(self) -> None:
        ...
    def Detach(self) -> None:
        ...
    def __init__(self, arg0: typing.Callable) -> None:
        ...
class Dx9Window(_Dx9Render):
    ClearColor: imgui.ImVec4
    def Serve(self) -> None:
        ...
    def __init__(self, arg0: typing.Callable) -> None:
        ...
class _Dx11Render(_RenderBase):
    @staticmethod
    def CreateDeviceObjects() -> bool:
        ...
    @staticmethod
    def InvalidateDeviceObjects() -> None:
        ...
    @typing.overload
    def CreateTexture(self, filename: str) -> Dx11TextureHelper:
        ...
    @typing.overload
    def CreateTexture(self) -> Dx11TextureHelper:
        ...
class _Dx9Render(_RenderBase):
    @staticmethod
    def CreateDeviceObjects() -> bool:
        ...
    @staticmethod
    def InvalidateDeviceObjects() -> None:
        ...
class _RenderBase:
    renderCallback: typing.Callable | None
    def CallBeforeFrameOnce(self, arg0: typing.Callable) -> None:
        ...
    def Close(self) -> None:
        ...
