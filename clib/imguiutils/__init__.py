import typing

from ..pyimgui import imgui
from ..pyimgui.imgui import ctx

_T = typing.TypeVar('_T')


def BeginFullScreenBackGround(name: str = '', open: bool = True, flags: int = 0):
    viewport = imgui.GetMainViewport()
    cls = imgui.ImGuiWindowClass()
    cls.DockNodeFlagsOverrideSet = imgui.ImGuiDockNodeFlags_NoDocking
    imgui.SetNextWindowClass(cls)
    imgui.SetNextWindowPos(viewport.Pos)
    imgui.SetNextWindowSize(viewport.Size)
    return ctx.Begin(
        name,
        open,
        flags | imgui.ImGuiWindowFlags_NoDecoration |
        imgui.ImGuiWindowFlags_NoMove |
        imgui.ImGuiWindowFlags_NoSavedSettings |
        imgui.ImGuiWindowFlags_NoBringToFrontOnFocus
    )


class Inspector(typing.Generic[_T]):
    selected_item = None
    selected_inspector: 'Inspector|None' = None

    def __init__(self, target: _T):
        self.filter_string = ''

        self.target = target
        self.items = self.init_items()
        self.displayed_items = self.items

    def init_items(self):
        return []

    def item_name(self, item):
        return str(item)

    def on_item_selected(self, item):
        self.selected_item = item

    def is_item_match(self, item):
        return self.filter_string.lower() in self.item_name(item).lower()

    def update_displayed_items(self):
        if not self.filter_string:
            self.displayed_items = self.items
        else:
            self.displayed_items = [[item for item in items if self.is_item_match(item)] for items in self.items]

    def render(self):
        menu_width = 0
        if self.selected_inspector is not None:
            # menu_width = imgui.CalcTextSize(self.item_name(self.selected_item)).x + imgui.GetStyle().ItemSpacing.x * 2 + 10
            # menu_width = max(menu_width, 200)
            menu_width = 200
        with ctx.BeginChild('left', imgui.ImVec2(menu_width, 0)):
            changed, self.filter_string = imgui.InputText('Filter', self.filter_string)
            if changed:
                self.update_displayed_items()
            if self.displayed_items:
                each_height = imgui.GetContentRegionAvail().y // len(self.displayed_items) - imgui.GetStyle().ItemSpacing.y
                for i, items in enumerate(self.displayed_items):
                    with ctx.BeginChild(
                            f'left_{i}', imgui.ImVec2(0, each_height),
                            window_flags=imgui.ImGuiWindowFlags_HorizontalScrollbar,
                            child_flags=imgui.ImGuiChildFlags_Border,
                    ):
                        clipper = imgui.ImGuiListClipper()
                        clipper.Begin(len(items))
                        while clipper.Step():
                            for j in range(clipper.DisplayStart, clipper.DisplayEnd):
                                item = items[j]
                                is_selected = self.selected_item == item
                                if imgui.Selectable(f"{self.item_name(item)}##item_{j}", is_selected):
                                    self.on_item_selected(None if is_selected else item)
        if menu_width:
            imgui.SameLine()
            with ctx.BeginChild('right'):
                if self.selected_inspector:
                    self.selected_inspector.render()
