from __future__ import annotations
import typing
from . import ctx
__all__ = ['AcceptDragDropPayload', 'ActivateItemByID', 'AddContextHook', 'AddDrawListToDrawDataEx', 'AddSettingsHandler', 'AlignTextToFramePadding', 'Arr_ImGuiDebugAllocEntry', 'Arr_ImGuiKeyData', 'Arr_ImGuiKeyOwnerData', 'Arr_ImRect', 'Arr_ImVec2', 'Arr_ImVec4', 'Arr_StbUndoRecord', 'Arr_bool', 'Arr_char', 'Arr_double', 'Arr_float', 'Arr_int', 'Arr_p_ImDrawList', 'Arr_p_ImGuiDockNode', 'Arr_p_ImVector_ImDrawListPtr', 'Arr_p_const_char', 'Arr_signed_short', 'Arr_unsigned_char', 'Arr_unsigned_int', 'Arr_unsigned_short', 'ArrowButton', 'ArrowButtonEx', 'Begin', 'BeginChild', 'BeginChildEx', 'BeginColumns', 'BeginCombo', 'BeginComboPopup', 'BeginComboPreview', 'BeginDisabled', 'BeginDisabledOverrideReenable', 'BeginDockableDragDropSource', 'BeginDockableDragDropTarget', 'BeginDocked', 'BeginDragDropSource', 'BeginDragDropTarget', 'BeginDragDropTargetCustom', 'BeginGroup', 'BeginItemTooltip', 'BeginListBox', 'BeginMainMenuBar', 'BeginMenu', 'BeginMenuBar', 'BeginMenuEx', 'BeginPopup', 'BeginPopupContextItem', 'BeginPopupContextVoid', 'BeginPopupContextWindow', 'BeginPopupEx', 'BeginPopupModal', 'BeginTabBar', 'BeginTabBarEx', 'BeginTabItem', 'BeginTable', 'BeginTableEx', 'BeginTooltip', 'BeginTooltipEx', 'BeginTooltipHidden', 'BeginViewportSideBar', 'BringWindowToDisplayBack', 'BringWindowToDisplayBehind', 'BringWindowToDisplayFront', 'BringWindowToFocusFront', 'Bullet', 'Button', 'ButtonBehavior', 'ButtonEx', 'CalcItemSize', 'CalcItemWidth', 'CalcRoundingFlagsForRectInRect', 'CalcTextSize', 'CalcTypematicRepeatAmount', 'CalcWindowNextAutoFitSize', 'CalcWrapWidthForPos', 'CallContextHooks', 'Checkbox', 'CheckboxFlags', 'ClearActiveID', 'ClearDragDrop', 'ClearIniSettings', 'ClearWindowSettings', 'CloseButton', 'CloseCurrentPopup', 'ClosePopupToLevel', 'ClosePopupsExceptModals', 'ClosePopupsOverWindow', 'CollapseButton', 'CollapsingHeader', 'ColorButton', 'ColorConvertFloat4ToU32', 'ColorConvertHSVtoRGB', 'ColorConvertRGBtoHSV', 'ColorConvertU32ToFloat4', 'ColorEdit3', 'ColorEdit4', 'ColorEditOptionsPopup', 'ColorPicker3', 'ColorPicker4', 'ColorPickerOptionsPopup', 'ColorTooltip', 'Columns', 'Combo', 'ConvertSingleModFlagToKey', 'CreateContext', 'CreateNewWindowSettings', 'DataTypeApplyFromText', 'DataTypeApplyOp', 'DataTypeClamp', 'DataTypeCompare', 'DataTypeFormatString', 'DataTypeGetInfo', 'DebugAllocHook', 'DebugBreakButton', 'DebugBreakButtonTooltip', 'DebugBreakClearData', 'DebugCheckVersionAndDataLayout', 'DebugDrawCursorPos', 'DebugDrawItemRect', 'DebugDrawLineExtents', 'DebugFlashStyleColor', 'DebugHookIdInfo', 'DebugLocateItem', 'DebugLocateItemOnHover', 'DebugLocateItemResolveWithLastItem', 'DebugNodeColumns', 'DebugNodeDockNode', 'DebugNodeDrawCmdShowMeshAndBoundingBox', 'DebugNodeDrawList', 'DebugNodeFont', 'DebugNodeFontGlyph', 'DebugNodeInputTextState', 'DebugNodeStorage', 'DebugNodeTabBar', 'DebugNodeTable', 'DebugNodeTableSettings', 'DebugNodeTypingSelectState', 'DebugNodeViewport', 'DebugNodeWindow', 'DebugNodeWindowSettings', 'DebugNodeWindowsList', 'DebugRenderKeyboardPreview', 'DebugRenderViewportThumbnail', 'DebugStartItemPicker', 'DebugTextEncoding', 'DebugTextUnformattedWithLocateItem', 'DestroyContext', 'DestroyPlatformWindow', 'DestroyPlatformWindows', 'DockBuilderAddNode', 'DockBuilderCopyDockSpace', 'DockBuilderCopyNode', 'DockBuilderCopyWindowSettings', 'DockBuilderDockWindow', 'DockBuilderFinish', 'DockBuilderGetCentralNode', 'DockBuilderGetNode', 'DockBuilderRemoveNode', 'DockBuilderRemoveNodeChildNodes', 'DockBuilderRemoveNodeDockedWindows', 'DockBuilderSetNodePos', 'DockBuilderSetNodeSize', 'DockBuilderSplitNode', 'DockContextCalcDropPosForDocking', 'DockContextClearNodes', 'DockContextEndFrame', 'DockContextFindNodeByID', 'DockContextGenNodeID', 'DockContextInitialize', 'DockContextNewFrameUpdateDocking', 'DockContextNewFrameUpdateUndocking', 'DockContextProcessUndockNode', 'DockContextProcessUndockWindow', 'DockContextQueueDock', 'DockContextQueueUndockNode', 'DockContextQueueUndockWindow', 'DockContextRebuildNodes', 'DockContextShutdown', 'DockNodeBeginAmendTabBar', 'DockNodeEndAmendTabBar', 'DockNodeGetDepth', 'DockNodeGetRootNode', 'DockNodeGetWindowMenuButtonId', 'DockNodeIsInHierarchyOf', 'DockNodeWindowMenuHandler_Default', 'DockSpace', 'DockSpaceOverViewport', 'DragBehavior', 'DragFloat', 'DragFloat2', 'DragFloat3', 'DragFloat4', 'DragFloatRange2', 'DragInt', 'DragInt2', 'DragInt3', 'DragInt4', 'DragIntRange2', 'DragScalar', 'DragScalarN', 'Dummy', 'End', 'EndChild', 'EndColumns', 'EndCombo', 'EndComboPreview', 'EndDisabled', 'EndDisabledOverrideReenable', 'EndDragDropSource', 'EndDragDropTarget', 'EndFrame', 'EndGroup', 'EndListBox', 'EndMainMenuBar', 'EndMenu', 'EndMenuBar', 'EndPopup', 'EndTabBar', 'EndTabItem', 'EndTable', 'EndTooltip', 'ErrorCheckEndFrameRecover', 'ErrorCheckEndWindowRecover', 'ErrorCheckUsingSetCursorPosToExtendParentBoundaries', 'FindBestWindowPosForPopup', 'FindBestWindowPosForPopupEx', 'FindBlockingModal', 'FindBottomMostVisibleWindowWithinBeginStack', 'FindHoveredViewportFromPlatformWindowStack', 'FindOrCreateColumns', 'FindRenderedTextEnd', 'FindSettingsHandler', 'FindViewportByID', 'FindViewportByPlatformHandle', 'FindWindowByID', 'FindWindowByName', 'FindWindowDisplayIndex', 'FindWindowSettingsByID', 'FindWindowSettingsByWindow', 'FixupKeyChord', 'FocusItem', 'FocusTopMostWindowUnderOne', 'FocusWindow', 'GcAwakeTransientWindowBuffers', 'GcCompactTransientMiscBuffers', 'GcCompactTransientWindowBuffers', 'GetActiveID', 'GetBackgroundDrawList', 'GetClipboardText', 'GetColorU32', 'GetColumnIndex', 'GetColumnNormFromOffset', 'GetColumnOffset', 'GetColumnOffsetFromNorm', 'GetColumnWidth', 'GetColumnsCount', 'GetColumnsID', 'GetContentRegionAvail', 'GetContentRegionMax', 'GetContentRegionMaxAbs', 'GetCurrentContext', 'GetCurrentFocusScope', 'GetCurrentTabBar', 'GetCurrentTable', 'GetCurrentWindow', 'GetCurrentWindowRead', 'GetCursorPos', 'GetCursorPosX', 'GetCursorPosY', 'GetCursorScreenPos', 'GetCursorStartPos', 'GetDefaultFont', 'GetDragDropPayload', 'GetDrawData', 'GetDrawListSharedData', 'GetFocusID', 'GetFont', 'GetFontSize', 'GetFontTexUvWhitePixel', 'GetForegroundDrawList', 'GetFrameCount', 'GetFrameHeight', 'GetFrameHeightWithSpacing', 'GetHoveredID', 'GetID', 'GetIDWithSeed', 'GetIO', 'GetInputTextState', 'GetItemFlags', 'GetItemID', 'GetItemRectMax', 'GetItemRectMin', 'GetItemRectSize', 'GetItemStatusFlags', 'GetKeyChordName', 'GetKeyData', 'GetKeyMagnitude2d', 'GetKeyName', 'GetKeyOwner', 'GetKeyOwnerData', 'GetKeyPressedAmount', 'GetMainViewport', 'GetMouseClickedCount', 'GetMouseCursor', 'GetMouseDragDelta', 'GetMousePos', 'GetMousePosOnOpeningCurrentPopup', 'GetNavTweakPressedAmount', 'GetPlatformIO', 'GetPopupAllowedExtentRect', 'GetScrollMaxX', 'GetScrollMaxY', 'GetScrollX', 'GetScrollY', 'GetShortcutRoutingData', 'GetStateStorage', 'GetStyle', 'GetStyleColorName', 'GetStyleColorVec4', 'GetStyleVarInfo', 'GetTextLineHeight', 'GetTextLineHeightWithSpacing', 'GetTime', 'GetTopMostAndVisiblePopupModal', 'GetTopMostPopupModal', 'GetTreeNodeToLabelSpacing', 'GetTypematicRepeatRate', 'GetTypingSelectRequest', 'GetVersion', 'GetViewportPlatformMonitor', 'GetWindowAlwaysWantOwnTabBar', 'GetWindowContentRegionMax', 'GetWindowContentRegionMin', 'GetWindowDockID', 'GetWindowDockNode', 'GetWindowDpiScale', 'GetWindowDrawList', 'GetWindowHeight', 'GetWindowPos', 'GetWindowResizeBorderID', 'GetWindowResizeCornerID', 'GetWindowScrollbarID', 'GetWindowScrollbarRect', 'GetWindowSize', 'GetWindowViewport', 'GetWindowWidth', 'GlyphRanges', 'ImAbs', 'ImAlphaBlendColors', 'ImBezierCubicCalc', 'ImBezierCubicClosestPoint', 'ImBezierCubicClosestPointCasteljau', 'ImBezierQuadraticCalc', 'ImBitArrayClearAllBits', 'ImBitArrayClearBit', 'ImBitArrayGetStorageSizeInBytes', 'ImBitArraySetBit', 'ImBitArraySetBitRange', 'ImBitArrayTestBit', 'ImBitVector', 'ImCharIsBlankA', 'ImCharIsBlankW', 'ImChunkStream_ImGuiTableSettings', 'ImChunkStream_ImGuiWindowSettings', 'ImClamp', 'ImColor', 'ImDot', 'ImDrawChannel', 'ImDrawCmd', 'ImDrawCmdHeader', 'ImDrawData', 'ImDrawDataBuilder', 'ImDrawFlags_', 'ImDrawFlags_Closed', 'ImDrawFlags_None', 'ImDrawFlags_RoundCornersAll', 'ImDrawFlags_RoundCornersBottom', 'ImDrawFlags_RoundCornersBottomLeft', 'ImDrawFlags_RoundCornersBottomRight', 'ImDrawFlags_RoundCornersDefault_', 'ImDrawFlags_RoundCornersLeft', 'ImDrawFlags_RoundCornersMask_', 'ImDrawFlags_RoundCornersNone', 'ImDrawFlags_RoundCornersRight', 'ImDrawFlags_RoundCornersTop', 'ImDrawFlags_RoundCornersTopLeft', 'ImDrawFlags_RoundCornersTopRight', 'ImDrawList', 'ImDrawListFlags_', 'ImDrawListFlags_AllowVtxOffset', 'ImDrawListFlags_AntiAliasedFill', 'ImDrawListFlags_AntiAliasedLines', 'ImDrawListFlags_AntiAliasedLinesUseTex', 'ImDrawListFlags_None', 'ImDrawListSharedData', 'ImDrawListSplitter', 'ImDrawVert', 'ImExponentialMovingAverage', 'ImFileClose', 'ImFileGetSize', 'ImFileLoadToMemory', 'ImFileOpen', 'ImFileRead', 'ImFileWrite', 'ImFloor', 'ImFont', 'ImFontAtlas', 'ImFontAtlasBuildFinish', 'ImFontAtlasBuildInit', 'ImFontAtlasBuildMultiplyCalcLookupTable', 'ImFontAtlasBuildMultiplyRectAlpha8', 'ImFontAtlasBuildPackCustomRects', 'ImFontAtlasBuildRender32bppRectFromString', 'ImFontAtlasBuildRender8bppRectFromString', 'ImFontAtlasBuildSetupFont', 'ImFontAtlasCustomRect', 'ImFontAtlasFlags_', 'ImFontAtlasFlags_NoBakedLines', 'ImFontAtlasFlags_NoMouseCursors', 'ImFontAtlasFlags_NoPowerOfTwoHeight', 'ImFontAtlasFlags_None', 'ImFontAtlasGetBuilderForStbTruetype', 'ImFontAtlasUpdateConfigDataPointers', 'ImFontBuilderIO', 'ImFontConfig', 'ImFontGlyph', 'ImFontGlyphRangesBuilder', 'ImGuiActivateFlags_', 'ImGuiActivateFlags_FromShortcut', 'ImGuiActivateFlags_FromTabbing', 'ImGuiActivateFlags_None', 'ImGuiActivateFlags_PreferInput', 'ImGuiActivateFlags_PreferTweak', 'ImGuiActivateFlags_TryToPreserveState', 'ImGuiAxis', 'ImGuiAxis_None', 'ImGuiAxis_X', 'ImGuiAxis_Y', 'ImGuiBackendFlags_', 'ImGuiBackendFlags_HasGamepad', 'ImGuiBackendFlags_HasMouseCursors', 'ImGuiBackendFlags_HasMouseHoveredViewport', 'ImGuiBackendFlags_HasSetMousePos', 'ImGuiBackendFlags_None', 'ImGuiBackendFlags_PlatformHasViewports', 'ImGuiBackendFlags_RendererHasViewports', 'ImGuiBackendFlags_RendererHasVtxOffset', 'ImGuiButtonFlagsPrivate_', 'ImGuiButtonFlags_', 'ImGuiButtonFlags_AlignTextBaseLine', 'ImGuiButtonFlags_AllowOverlap', 'ImGuiButtonFlags_DontClosePopups', 'ImGuiButtonFlags_FlattenChildren', 'ImGuiButtonFlags_MouseButtonLeft', 'ImGuiButtonFlags_MouseButtonMask_', 'ImGuiButtonFlags_MouseButtonMiddle', 'ImGuiButtonFlags_MouseButtonRight', 'ImGuiButtonFlags_NoHoldingActiveId', 'ImGuiButtonFlags_NoHoveredOnFocus', 'ImGuiButtonFlags_NoKeyModifiers', 'ImGuiButtonFlags_NoNavFocus', 'ImGuiButtonFlags_NoSetKeyOwner', 'ImGuiButtonFlags_NoTestKeyOwner', 'ImGuiButtonFlags_None', 'ImGuiButtonFlags_PressedOnClick', 'ImGuiButtonFlags_PressedOnClickRelease', 'ImGuiButtonFlags_PressedOnClickReleaseAnywhere', 'ImGuiButtonFlags_PressedOnDefault_', 'ImGuiButtonFlags_PressedOnDoubleClick', 'ImGuiButtonFlags_PressedOnDragDropHold', 'ImGuiButtonFlags_PressedOnMask_', 'ImGuiButtonFlags_PressedOnRelease', 'ImGuiButtonFlags_Repeat', 'ImGuiChildFlags_', 'ImGuiChildFlags_AlwaysAutoResize', 'ImGuiChildFlags_AlwaysUseWindowPadding', 'ImGuiChildFlags_AutoResizeX', 'ImGuiChildFlags_AutoResizeY', 'ImGuiChildFlags_Border', 'ImGuiChildFlags_FrameStyle', 'ImGuiChildFlags_NavFlattened', 'ImGuiChildFlags_None', 'ImGuiChildFlags_ResizeX', 'ImGuiChildFlags_ResizeY', 'ImGuiCol_', 'ImGuiCol_Border', 'ImGuiCol_BorderShadow', 'ImGuiCol_Button', 'ImGuiCol_ButtonActive', 'ImGuiCol_ButtonHovered', 'ImGuiCol_COUNT', 'ImGuiCol_CheckMark', 'ImGuiCol_ChildBg', 'ImGuiCol_DockingEmptyBg', 'ImGuiCol_DockingPreview', 'ImGuiCol_DragDropTarget', 'ImGuiCol_FrameBg', 'ImGuiCol_FrameBgActive', 'ImGuiCol_FrameBgHovered', 'ImGuiCol_Header', 'ImGuiCol_HeaderActive', 'ImGuiCol_HeaderHovered', 'ImGuiCol_MenuBarBg', 'ImGuiCol_ModalWindowDimBg', 'ImGuiCol_NavHighlight', 'ImGuiCol_NavWindowingDimBg', 'ImGuiCol_NavWindowingHighlight', 'ImGuiCol_PlotHistogram', 'ImGuiCol_PlotHistogramHovered', 'ImGuiCol_PlotLines', 'ImGuiCol_PlotLinesHovered', 'ImGuiCol_PopupBg', 'ImGuiCol_ResizeGrip', 'ImGuiCol_ResizeGripActive', 'ImGuiCol_ResizeGripHovered', 'ImGuiCol_ScrollbarBg', 'ImGuiCol_ScrollbarGrab', 'ImGuiCol_ScrollbarGrabActive', 'ImGuiCol_ScrollbarGrabHovered', 'ImGuiCol_Separator', 'ImGuiCol_SeparatorActive', 'ImGuiCol_SeparatorHovered', 'ImGuiCol_SliderGrab', 'ImGuiCol_SliderGrabActive', 'ImGuiCol_Tab', 'ImGuiCol_TabDimmed', 'ImGuiCol_TabDimmedSelected', 'ImGuiCol_TabDimmedSelectedOverline', 'ImGuiCol_TabHovered', 'ImGuiCol_TabSelected', 'ImGuiCol_TabSelectedOverline', 'ImGuiCol_TableBorderLight', 'ImGuiCol_TableBorderStrong', 'ImGuiCol_TableHeaderBg', 'ImGuiCol_TableRowBg', 'ImGuiCol_TableRowBgAlt', 'ImGuiCol_Text', 'ImGuiCol_TextDisabled', 'ImGuiCol_TextSelectedBg', 'ImGuiCol_TitleBg', 'ImGuiCol_TitleBgActive', 'ImGuiCol_TitleBgCollapsed', 'ImGuiCol_WindowBg', 'ImGuiColorEditFlags_', 'ImGuiColorEditFlags_AlphaBar', 'ImGuiColorEditFlags_AlphaPreview', 'ImGuiColorEditFlags_AlphaPreviewHalf', 'ImGuiColorEditFlags_DataTypeMask_', 'ImGuiColorEditFlags_DefaultOptions_', 'ImGuiColorEditFlags_DisplayHSV', 'ImGuiColorEditFlags_DisplayHex', 'ImGuiColorEditFlags_DisplayMask_', 'ImGuiColorEditFlags_DisplayRGB', 'ImGuiColorEditFlags_Float', 'ImGuiColorEditFlags_HDR', 'ImGuiColorEditFlags_InputHSV', 'ImGuiColorEditFlags_InputMask_', 'ImGuiColorEditFlags_InputRGB', 'ImGuiColorEditFlags_NoAlpha', 'ImGuiColorEditFlags_NoBorder', 'ImGuiColorEditFlags_NoDragDrop', 'ImGuiColorEditFlags_NoInputs', 'ImGuiColorEditFlags_NoLabel', 'ImGuiColorEditFlags_NoOptions', 'ImGuiColorEditFlags_NoPicker', 'ImGuiColorEditFlags_NoSidePreview', 'ImGuiColorEditFlags_NoSmallPreview', 'ImGuiColorEditFlags_NoTooltip', 'ImGuiColorEditFlags_None', 'ImGuiColorEditFlags_PickerHueBar', 'ImGuiColorEditFlags_PickerHueWheel', 'ImGuiColorEditFlags_PickerMask_', 'ImGuiColorEditFlags_Uint8', 'ImGuiColorMod', 'ImGuiComboFlagsPrivate_', 'ImGuiComboFlags_', 'ImGuiComboFlags_CustomPreview', 'ImGuiComboFlags_HeightLarge', 'ImGuiComboFlags_HeightLargest', 'ImGuiComboFlags_HeightMask_', 'ImGuiComboFlags_HeightRegular', 'ImGuiComboFlags_HeightSmall', 'ImGuiComboFlags_NoArrowButton', 'ImGuiComboFlags_NoPreview', 'ImGuiComboFlags_None', 'ImGuiComboFlags_PopupAlignLeft', 'ImGuiComboFlags_WidthFitPreview', 'ImGuiComboPreviewData', 'ImGuiCond_', 'ImGuiCond_Always', 'ImGuiCond_Appearing', 'ImGuiCond_FirstUseEver', 'ImGuiCond_None', 'ImGuiCond_Once', 'ImGuiConfigFlags_', 'ImGuiConfigFlags_DockingEnable', 'ImGuiConfigFlags_DpiEnableScaleFonts', 'ImGuiConfigFlags_DpiEnableScaleViewports', 'ImGuiConfigFlags_IsSRGB', 'ImGuiConfigFlags_IsTouchScreen', 'ImGuiConfigFlags_NavEnableGamepad', 'ImGuiConfigFlags_NavEnableKeyboard', 'ImGuiConfigFlags_NavEnableSetMousePos', 'ImGuiConfigFlags_NavNoCaptureKeyboard', 'ImGuiConfigFlags_NoKeyboard', 'ImGuiConfigFlags_NoMouse', 'ImGuiConfigFlags_NoMouseCursorChange', 'ImGuiConfigFlags_None', 'ImGuiConfigFlags_ViewportsEnable', 'ImGuiContext', 'ImGuiContextHook', 'ImGuiContextHookType', 'ImGuiContextHookType_EndFramePost', 'ImGuiContextHookType_EndFramePre', 'ImGuiContextHookType_NewFramePost', 'ImGuiContextHookType_NewFramePre', 'ImGuiContextHookType_PendingRemoval_', 'ImGuiContextHookType_RenderPost', 'ImGuiContextHookType_RenderPre', 'ImGuiContextHookType_Shutdown', 'ImGuiDataAuthority_', 'ImGuiDataAuthority_Auto', 'ImGuiDataAuthority_DockNode', 'ImGuiDataAuthority_Window', 'ImGuiDataTypeInfo', 'ImGuiDataTypePrivate_', 'ImGuiDataTypeStorage', 'ImGuiDataType_', 'ImGuiDataType_COUNT', 'ImGuiDataType_Double', 'ImGuiDataType_Float', 'ImGuiDataType_ID', 'ImGuiDataType_Pointer', 'ImGuiDataType_S16', 'ImGuiDataType_S32', 'ImGuiDataType_S64', 'ImGuiDataType_S8', 'ImGuiDataType_String', 'ImGuiDataType_U16', 'ImGuiDataType_U32', 'ImGuiDataType_U64', 'ImGuiDataType_U8', 'ImGuiDataVarInfo', 'ImGuiDebugAllocEntry', 'ImGuiDebugAllocInfo', 'ImGuiDebugLogFlags_', 'ImGuiDebugLogFlags_EventActiveId', 'ImGuiDebugLogFlags_EventClipper', 'ImGuiDebugLogFlags_EventDocking', 'ImGuiDebugLogFlags_EventFocus', 'ImGuiDebugLogFlags_EventIO', 'ImGuiDebugLogFlags_EventInputRouting', 'ImGuiDebugLogFlags_EventMask_', 'ImGuiDebugLogFlags_EventNav', 'ImGuiDebugLogFlags_EventPopup', 'ImGuiDebugLogFlags_EventSelection', 'ImGuiDebugLogFlags_EventViewport', 'ImGuiDebugLogFlags_None', 'ImGuiDebugLogFlags_OutputToTTY', 'ImGuiDebugLogFlags_OutputToTestEngine', 'ImGuiDir', 'ImGuiDir_COUNT', 'ImGuiDir_Down', 'ImGuiDir_Left', 'ImGuiDir_None', 'ImGuiDir_Right', 'ImGuiDir_Up', 'ImGuiDockContext', 'ImGuiDockNode', 'ImGuiDockNodeFlagsPrivate_', 'ImGuiDockNodeFlags_', 'ImGuiDockNodeFlags_AutoHideTabBar', 'ImGuiDockNodeFlags_CentralNode', 'ImGuiDockNodeFlags_DockSpace', 'ImGuiDockNodeFlags_DockedWindowsInFocusRoute', 'ImGuiDockNodeFlags_HiddenTabBar', 'ImGuiDockNodeFlags_KeepAliveOnly', 'ImGuiDockNodeFlags_LocalFlagsTransferMask_', 'ImGuiDockNodeFlags_NoCloseButton', 'ImGuiDockNodeFlags_NoDocking', 'ImGuiDockNodeFlags_NoDockingOverCentralNode', 'ImGuiDockNodeFlags_NoDockingOverEmpty', 'ImGuiDockNodeFlags_NoDockingOverMe', 'ImGuiDockNodeFlags_NoDockingOverOther', 'ImGuiDockNodeFlags_NoDockingSplit', 'ImGuiDockNodeFlags_NoDockingSplitOther', 'ImGuiDockNodeFlags_NoResize', 'ImGuiDockNodeFlags_NoResizeFlagsMask_', 'ImGuiDockNodeFlags_NoResizeX', 'ImGuiDockNodeFlags_NoResizeY', 'ImGuiDockNodeFlags_NoTabBar', 'ImGuiDockNodeFlags_NoUndocking', 'ImGuiDockNodeFlags_NoWindowMenuButton', 'ImGuiDockNodeFlags_None', 'ImGuiDockNodeFlags_PassthruCentralNode', 'ImGuiDockNodeFlags_SavedFlagsMask_', 'ImGuiDockNodeFlags_SharedFlagsInheritMask_', 'ImGuiDockNodeState', 'ImGuiDockNodeState_HostWindowHiddenBecauseSingleWindow', 'ImGuiDockNodeState_HostWindowHiddenBecauseWindowsAreResizing', 'ImGuiDockNodeState_HostWindowVisible', 'ImGuiDockNodeState_Unknown', 'ImGuiDragDropFlags_', 'ImGuiDragDropFlags_AcceptBeforeDelivery', 'ImGuiDragDropFlags_AcceptNoDrawDefaultRect', 'ImGuiDragDropFlags_AcceptNoPreviewTooltip', 'ImGuiDragDropFlags_AcceptPeekOnly', 'ImGuiDragDropFlags_None', 'ImGuiDragDropFlags_PayloadAutoExpire', 'ImGuiDragDropFlags_PayloadNoCrossContext', 'ImGuiDragDropFlags_PayloadNoCrossProcess', 'ImGuiDragDropFlags_SourceAllowNullID', 'ImGuiDragDropFlags_SourceExtern', 'ImGuiDragDropFlags_SourceNoDisableHover', 'ImGuiDragDropFlags_SourceNoHoldToOpenOthers', 'ImGuiDragDropFlags_SourceNoPreviewTooltip', 'ImGuiFocusRequestFlags_', 'ImGuiFocusRequestFlags_None', 'ImGuiFocusRequestFlags_RestoreFocusedChild', 'ImGuiFocusRequestFlags_UnlessBelowModal', 'ImGuiFocusScopeData', 'ImGuiFocusedFlags_', 'ImGuiFocusedFlags_AnyWindow', 'ImGuiFocusedFlags_ChildWindows', 'ImGuiFocusedFlags_DockHierarchy', 'ImGuiFocusedFlags_NoPopupHierarchy', 'ImGuiFocusedFlags_None', 'ImGuiFocusedFlags_RootAndChildWindows', 'ImGuiFocusedFlags_RootWindow', 'ImGuiGroupData', 'ImGuiHoveredFlagsPrivate_', 'ImGuiHoveredFlags_', 'ImGuiHoveredFlags_AllowWhenBlockedByActiveItem', 'ImGuiHoveredFlags_AllowWhenBlockedByPopup', 'ImGuiHoveredFlags_AllowWhenDisabled', 'ImGuiHoveredFlags_AllowWhenOverlapped', 'ImGuiHoveredFlags_AllowWhenOverlappedByItem', 'ImGuiHoveredFlags_AllowWhenOverlappedByWindow', 'ImGuiHoveredFlags_AllowedMaskForIsItemHovered', 'ImGuiHoveredFlags_AllowedMaskForIsWindowHovered', 'ImGuiHoveredFlags_AnyWindow', 'ImGuiHoveredFlags_ChildWindows', 'ImGuiHoveredFlags_DelayMask_', 'ImGuiHoveredFlags_DelayNone', 'ImGuiHoveredFlags_DelayNormal', 'ImGuiHoveredFlags_DelayShort', 'ImGuiHoveredFlags_DockHierarchy', 'ImGuiHoveredFlags_ForTooltip', 'ImGuiHoveredFlags_NoNavOverride', 'ImGuiHoveredFlags_NoPopupHierarchy', 'ImGuiHoveredFlags_NoSharedDelay', 'ImGuiHoveredFlags_None', 'ImGuiHoveredFlags_RectOnly', 'ImGuiHoveredFlags_RootAndChildWindows', 'ImGuiHoveredFlags_RootWindow', 'ImGuiHoveredFlags_Stationary', 'ImGuiIDStackTool', 'ImGuiIO', 'ImGuiInputEvent', 'ImGuiInputEventAppFocused', 'ImGuiInputEventKey', 'ImGuiInputEventMouseButton', 'ImGuiInputEventMousePos', 'ImGuiInputEventMouseViewport', 'ImGuiInputEventMouseWheel', 'ImGuiInputEventText', 'ImGuiInputEventType', 'ImGuiInputEventType_COUNT', 'ImGuiInputEventType_Focus', 'ImGuiInputEventType_Key', 'ImGuiInputEventType_MouseButton', 'ImGuiInputEventType_MousePos', 'ImGuiInputEventType_MouseViewport', 'ImGuiInputEventType_MouseWheel', 'ImGuiInputEventType_None', 'ImGuiInputEventType_Text', 'ImGuiInputFlagsPrivate_', 'ImGuiInputFlags_', 'ImGuiInputFlags_CondActive', 'ImGuiInputFlags_CondDefault_', 'ImGuiInputFlags_CondHovered', 'ImGuiInputFlags_CondMask_', 'ImGuiInputFlags_LockThisFrame', 'ImGuiInputFlags_LockUntilRelease', 'ImGuiInputFlags_None', 'ImGuiInputFlags_Repeat', 'ImGuiInputFlags_RepeatMask_', 'ImGuiInputFlags_RepeatRateDefault', 'ImGuiInputFlags_RepeatRateMask_', 'ImGuiInputFlags_RepeatRateNavMove', 'ImGuiInputFlags_RepeatRateNavTweak', 'ImGuiInputFlags_RepeatUntilKeyModsChange', 'ImGuiInputFlags_RepeatUntilKeyModsChangeFromNone', 'ImGuiInputFlags_RepeatUntilMask_', 'ImGuiInputFlags_RepeatUntilOtherKeyPress', 'ImGuiInputFlags_RepeatUntilRelease', 'ImGuiInputFlags_RouteActive', 'ImGuiInputFlags_RouteAlways', 'ImGuiInputFlags_RouteFocused', 'ImGuiInputFlags_RouteFromRootWindow', 'ImGuiInputFlags_RouteGlobal', 'ImGuiInputFlags_RouteOptionsMask_', 'ImGuiInputFlags_RouteOverActive', 'ImGuiInputFlags_RouteOverFocused', 'ImGuiInputFlags_RouteTypeMask_', 'ImGuiInputFlags_RouteUnlessBgFocused', 'ImGuiInputFlags_SupportedByIsKeyPressed', 'ImGuiInputFlags_SupportedByIsMouseClicked', 'ImGuiInputFlags_SupportedBySetItemKeyOwner', 'ImGuiInputFlags_SupportedBySetKeyOwner', 'ImGuiInputFlags_SupportedBySetNextItemShortcut', 'ImGuiInputFlags_SupportedByShortcut', 'ImGuiInputFlags_Tooltip', 'ImGuiInputSource', 'ImGuiInputSource_COUNT', 'ImGuiInputSource_Gamepad', 'ImGuiInputSource_Keyboard', 'ImGuiInputSource_Mouse', 'ImGuiInputSource_None', 'ImGuiInputTextCallbackData', 'ImGuiInputTextDeactivatedState', 'ImGuiInputTextFlagsPrivate_', 'ImGuiInputTextFlags_', 'ImGuiInputTextFlags_AllowTabInput', 'ImGuiInputTextFlags_AlwaysOverwrite', 'ImGuiInputTextFlags_AutoSelectAll', 'ImGuiInputTextFlags_CallbackAlways', 'ImGuiInputTextFlags_CallbackCharFilter', 'ImGuiInputTextFlags_CallbackCompletion', 'ImGuiInputTextFlags_CallbackEdit', 'ImGuiInputTextFlags_CallbackHistory', 'ImGuiInputTextFlags_CallbackResize', 'ImGuiInputTextFlags_CharsDecimal', 'ImGuiInputTextFlags_CharsHexadecimal', 'ImGuiInputTextFlags_CharsNoBlank', 'ImGuiInputTextFlags_CharsScientific', 'ImGuiInputTextFlags_CharsUppercase', 'ImGuiInputTextFlags_CtrlEnterForNewLine', 'ImGuiInputTextFlags_DisplayEmptyRefVal', 'ImGuiInputTextFlags_EnterReturnsTrue', 'ImGuiInputTextFlags_EscapeClearsAll', 'ImGuiInputTextFlags_LocalizeDecimalPoint', 'ImGuiInputTextFlags_MergedItem', 'ImGuiInputTextFlags_Multiline', 'ImGuiInputTextFlags_NoHorizontalScroll', 'ImGuiInputTextFlags_NoMarkEdited', 'ImGuiInputTextFlags_NoUndoRedo', 'ImGuiInputTextFlags_None', 'ImGuiInputTextFlags_ParseEmptyRefVal', 'ImGuiInputTextFlags_Password', 'ImGuiInputTextFlags_ReadOnly', 'ImGuiInputTextState', 'ImGuiItemFlags_', 'ImGuiItemFlags_AllowOverlap', 'ImGuiItemFlags_ButtonRepeat', 'ImGuiItemFlags_Disabled', 'ImGuiItemFlags_HasSelectionUserData', 'ImGuiItemFlags_Inputable', 'ImGuiItemFlags_MixedValue', 'ImGuiItemFlags_NoNav', 'ImGuiItemFlags_NoNavDefaultFocus', 'ImGuiItemFlags_NoTabStop', 'ImGuiItemFlags_NoWindowHoverableCheck', 'ImGuiItemFlags_None', 'ImGuiItemFlags_ReadOnly', 'ImGuiItemFlags_SelectableDontClosePopup', 'ImGuiItemStatusFlags_', 'ImGuiItemStatusFlags_Deactivated', 'ImGuiItemStatusFlags_Edited', 'ImGuiItemStatusFlags_HasClipRect', 'ImGuiItemStatusFlags_HasDeactivated', 'ImGuiItemStatusFlags_HasDisplayRect', 'ImGuiItemStatusFlags_HasShortcut', 'ImGuiItemStatusFlags_HoveredRect', 'ImGuiItemStatusFlags_HoveredWindow', 'ImGuiItemStatusFlags_None', 'ImGuiItemStatusFlags_ToggledOpen', 'ImGuiItemStatusFlags_ToggledSelection', 'ImGuiItemStatusFlags_Visible', 'ImGuiKey', 'ImGuiKeyData', 'ImGuiKeyOwnerData', 'ImGuiKeyRoutingData', 'ImGuiKeyRoutingTable', 'ImGuiKey_0', 'ImGuiKey_1', 'ImGuiKey_2', 'ImGuiKey_3', 'ImGuiKey_4', 'ImGuiKey_5', 'ImGuiKey_6', 'ImGuiKey_7', 'ImGuiKey_8', 'ImGuiKey_9', 'ImGuiKey_A', 'ImGuiKey_Apostrophe', 'ImGuiKey_AppBack', 'ImGuiKey_AppForward', 'ImGuiKey_B', 'ImGuiKey_Backslash', 'ImGuiKey_Backspace', 'ImGuiKey_C', 'ImGuiKey_COUNT', 'ImGuiKey_CapsLock', 'ImGuiKey_Comma', 'ImGuiKey_D', 'ImGuiKey_Delete', 'ImGuiKey_DownArrow', 'ImGuiKey_E', 'ImGuiKey_End', 'ImGuiKey_Enter', 'ImGuiKey_Equal', 'ImGuiKey_Escape', 'ImGuiKey_F', 'ImGuiKey_F1', 'ImGuiKey_F10', 'ImGuiKey_F11', 'ImGuiKey_F12', 'ImGuiKey_F13', 'ImGuiKey_F14', 'ImGuiKey_F15', 'ImGuiKey_F16', 'ImGuiKey_F17', 'ImGuiKey_F18', 'ImGuiKey_F19', 'ImGuiKey_F2', 'ImGuiKey_F20', 'ImGuiKey_F21', 'ImGuiKey_F22', 'ImGuiKey_F23', 'ImGuiKey_F24', 'ImGuiKey_F3', 'ImGuiKey_F4', 'ImGuiKey_F5', 'ImGuiKey_F6', 'ImGuiKey_F7', 'ImGuiKey_F8', 'ImGuiKey_F9', 'ImGuiKey_G', 'ImGuiKey_GamepadBack', 'ImGuiKey_GamepadDpadDown', 'ImGuiKey_GamepadDpadLeft', 'ImGuiKey_GamepadDpadRight', 'ImGuiKey_GamepadDpadUp', 'ImGuiKey_GamepadFaceDown', 'ImGuiKey_GamepadFaceLeft', 'ImGuiKey_GamepadFaceRight', 'ImGuiKey_GamepadFaceUp', 'ImGuiKey_GamepadL1', 'ImGuiKey_GamepadL2', 'ImGuiKey_GamepadL3', 'ImGuiKey_GamepadLStickDown', 'ImGuiKey_GamepadLStickLeft', 'ImGuiKey_GamepadLStickRight', 'ImGuiKey_GamepadLStickUp', 'ImGuiKey_GamepadR1', 'ImGuiKey_GamepadR2', 'ImGuiKey_GamepadR3', 'ImGuiKey_GamepadRStickDown', 'ImGuiKey_GamepadRStickLeft', 'ImGuiKey_GamepadRStickRight', 'ImGuiKey_GamepadRStickUp', 'ImGuiKey_GamepadStart', 'ImGuiKey_GraveAccent', 'ImGuiKey_H', 'ImGuiKey_Home', 'ImGuiKey_I', 'ImGuiKey_Insert', 'ImGuiKey_J', 'ImGuiKey_K', 'ImGuiKey_Keypad0', 'ImGuiKey_Keypad1', 'ImGuiKey_Keypad2', 'ImGuiKey_Keypad3', 'ImGuiKey_Keypad4', 'ImGuiKey_Keypad5', 'ImGuiKey_Keypad6', 'ImGuiKey_Keypad7', 'ImGuiKey_Keypad8', 'ImGuiKey_Keypad9', 'ImGuiKey_KeypadAdd', 'ImGuiKey_KeypadDecimal', 'ImGuiKey_KeypadDivide', 'ImGuiKey_KeypadEnter', 'ImGuiKey_KeypadEqual', 'ImGuiKey_KeypadMultiply', 'ImGuiKey_KeypadSubtract', 'ImGuiKey_KeysData_OFFSET', 'ImGuiKey_KeysData_SIZE', 'ImGuiKey_L', 'ImGuiKey_LeftAlt', 'ImGuiKey_LeftArrow', 'ImGuiKey_LeftBracket', 'ImGuiKey_LeftCtrl', 'ImGuiKey_LeftShift', 'ImGuiKey_LeftSuper', 'ImGuiKey_M', 'ImGuiKey_Menu', 'ImGuiKey_Minus', 'ImGuiKey_MouseLeft', 'ImGuiKey_MouseMiddle', 'ImGuiKey_MouseRight', 'ImGuiKey_MouseWheelX', 'ImGuiKey_MouseWheelY', 'ImGuiKey_MouseX1', 'ImGuiKey_MouseX2', 'ImGuiKey_N', 'ImGuiKey_NamedKey_BEGIN', 'ImGuiKey_NamedKey_COUNT', 'ImGuiKey_NamedKey_END', 'ImGuiKey_None', 'ImGuiKey_NumLock', 'ImGuiKey_O', 'ImGuiKey_P', 'ImGuiKey_PageDown', 'ImGuiKey_PageUp', 'ImGuiKey_Pause', 'ImGuiKey_Period', 'ImGuiKey_PrintScreen', 'ImGuiKey_Q', 'ImGuiKey_R', 'ImGuiKey_ReservedForModAlt', 'ImGuiKey_ReservedForModCtrl', 'ImGuiKey_ReservedForModShift', 'ImGuiKey_ReservedForModSuper', 'ImGuiKey_RightAlt', 'ImGuiKey_RightArrow', 'ImGuiKey_RightBracket', 'ImGuiKey_RightCtrl', 'ImGuiKey_RightShift', 'ImGuiKey_RightSuper', 'ImGuiKey_S', 'ImGuiKey_ScrollLock', 'ImGuiKey_Semicolon', 'ImGuiKey_Slash', 'ImGuiKey_Space', 'ImGuiKey_T', 'ImGuiKey_Tab', 'ImGuiKey_U', 'ImGuiKey_UpArrow', 'ImGuiKey_V', 'ImGuiKey_W', 'ImGuiKey_X', 'ImGuiKey_Y', 'ImGuiKey_Z', 'ImGuiLastItemData', 'ImGuiLayoutType_', 'ImGuiLayoutType_Horizontal', 'ImGuiLayoutType_Vertical', 'ImGuiListClipper', 'ImGuiListClipperData', 'ImGuiListClipperRange', 'ImGuiLocEntry', 'ImGuiLocKey', 'ImGuiLocKey_COUNT', 'ImGuiLocKey_DockingDragToUndockOrMoveNode', 'ImGuiLocKey_DockingHideTabBar', 'ImGuiLocKey_DockingHoldShiftToDock', 'ImGuiLocKey_TableResetOrder', 'ImGuiLocKey_TableSizeAllDefault', 'ImGuiLocKey_TableSizeAllFit', 'ImGuiLocKey_TableSizeOne', 'ImGuiLocKey_VersionStr', 'ImGuiLocKey_WindowingMainMenuBar', 'ImGuiLocKey_WindowingPopup', 'ImGuiLocKey_WindowingUntitled', 'ImGuiLogType', 'ImGuiLogType_Buffer', 'ImGuiLogType_Clipboard', 'ImGuiLogType_File', 'ImGuiLogType_None', 'ImGuiLogType_TTY', 'ImGuiMenuColumns', 'ImGuiMetricsConfig', 'ImGuiMod_Alt', 'ImGuiMod_Ctrl', 'ImGuiMod_Mask_', 'ImGuiMod_None', 'ImGuiMod_Shift', 'ImGuiMod_Super', 'ImGuiMouseButton_', 'ImGuiMouseButton_COUNT', 'ImGuiMouseButton_Left', 'ImGuiMouseButton_Middle', 'ImGuiMouseButton_Right', 'ImGuiMouseCursor_', 'ImGuiMouseCursor_Arrow', 'ImGuiMouseCursor_COUNT', 'ImGuiMouseCursor_Hand', 'ImGuiMouseCursor_None', 'ImGuiMouseCursor_NotAllowed', 'ImGuiMouseCursor_ResizeAll', 'ImGuiMouseCursor_ResizeEW', 'ImGuiMouseCursor_ResizeNESW', 'ImGuiMouseCursor_ResizeNS', 'ImGuiMouseCursor_ResizeNWSE', 'ImGuiMouseCursor_TextInput', 'ImGuiMouseSource', 'ImGuiMouseSource_COUNT', 'ImGuiMouseSource_Mouse', 'ImGuiMouseSource_Pen', 'ImGuiMouseSource_TouchScreen', 'ImGuiNavHighlightFlags_', 'ImGuiNavHighlightFlags_AlwaysDraw', 'ImGuiNavHighlightFlags_Compact', 'ImGuiNavHighlightFlags_NoRounding', 'ImGuiNavHighlightFlags_None', 'ImGuiNavItemData', 'ImGuiNavLayer', 'ImGuiNavLayer_COUNT', 'ImGuiNavLayer_Main', 'ImGuiNavLayer_Menu', 'ImGuiNavMoveFlags_', 'ImGuiNavMoveFlags_Activate', 'ImGuiNavMoveFlags_AllowCurrentNavId', 'ImGuiNavMoveFlags_AlsoScoreVisibleSet', 'ImGuiNavMoveFlags_DebugNoResult', 'ImGuiNavMoveFlags_FocusApi', 'ImGuiNavMoveFlags_Forwarded', 'ImGuiNavMoveFlags_IsPageMove', 'ImGuiNavMoveFlags_IsTabbing', 'ImGuiNavMoveFlags_LoopX', 'ImGuiNavMoveFlags_LoopY', 'ImGuiNavMoveFlags_NoClearActiveId', 'ImGuiNavMoveFlags_NoSelect', 'ImGuiNavMoveFlags_NoSetNavHighlight', 'ImGuiNavMoveFlags_None', 'ImGuiNavMoveFlags_ScrollToEdgeY', 'ImGuiNavMoveFlags_WrapMask_', 'ImGuiNavMoveFlags_WrapX', 'ImGuiNavMoveFlags_WrapY', 'ImGuiNavTreeNodeData', 'ImGuiNextItemData', 'ImGuiNextItemDataFlags_', 'ImGuiNextItemDataFlags_HasOpen', 'ImGuiNextItemDataFlags_HasRefVal', 'ImGuiNextItemDataFlags_HasShortcut', 'ImGuiNextItemDataFlags_HasWidth', 'ImGuiNextItemDataFlags_None', 'ImGuiNextWindowData', 'ImGuiNextWindowDataFlags_', 'ImGuiNextWindowDataFlags_HasBgAlpha', 'ImGuiNextWindowDataFlags_HasChildFlags', 'ImGuiNextWindowDataFlags_HasCollapsed', 'ImGuiNextWindowDataFlags_HasContentSize', 'ImGuiNextWindowDataFlags_HasDock', 'ImGuiNextWindowDataFlags_HasFocus', 'ImGuiNextWindowDataFlags_HasPos', 'ImGuiNextWindowDataFlags_HasRefreshPolicy', 'ImGuiNextWindowDataFlags_HasScroll', 'ImGuiNextWindowDataFlags_HasSize', 'ImGuiNextWindowDataFlags_HasSizeConstraint', 'ImGuiNextWindowDataFlags_HasViewport', 'ImGuiNextWindowDataFlags_HasWindowClass', 'ImGuiNextWindowDataFlags_None', 'ImGuiOldColumnData', 'ImGuiOldColumnFlags_', 'ImGuiOldColumnFlags_GrowParentContentsSize', 'ImGuiOldColumnFlags_NoBorder', 'ImGuiOldColumnFlags_NoForceWithinWindow', 'ImGuiOldColumnFlags_NoPreserveWidths', 'ImGuiOldColumnFlags_NoResize', 'ImGuiOldColumnFlags_None', 'ImGuiOldColumns', 'ImGuiOnceUponAFrame', 'ImGuiPayload', 'ImGuiPlatformIO', 'ImGuiPlatformImeData', 'ImGuiPlatformMonitor', 'ImGuiPlotType', 'ImGuiPlotType_Histogram', 'ImGuiPlotType_Lines', 'ImGuiPopupData', 'ImGuiPopupFlags_', 'ImGuiPopupFlags_AnyPopup', 'ImGuiPopupFlags_AnyPopupId', 'ImGuiPopupFlags_AnyPopupLevel', 'ImGuiPopupFlags_MouseButtonDefault_', 'ImGuiPopupFlags_MouseButtonLeft', 'ImGuiPopupFlags_MouseButtonMask_', 'ImGuiPopupFlags_MouseButtonMiddle', 'ImGuiPopupFlags_MouseButtonRight', 'ImGuiPopupFlags_NoOpenOverExistingPopup', 'ImGuiPopupFlags_NoOpenOverItems', 'ImGuiPopupFlags_NoReopen', 'ImGuiPopupFlags_None', 'ImGuiPopupPositionPolicy', 'ImGuiPopupPositionPolicy_ComboBox', 'ImGuiPopupPositionPolicy_Default', 'ImGuiPopupPositionPolicy_Tooltip', 'ImGuiPtrOrIndex', 'ImGuiScrollFlags_', 'ImGuiScrollFlags_AlwaysCenterX', 'ImGuiScrollFlags_AlwaysCenterY', 'ImGuiScrollFlags_KeepVisibleCenterX', 'ImGuiScrollFlags_KeepVisibleCenterY', 'ImGuiScrollFlags_KeepVisibleEdgeX', 'ImGuiScrollFlags_KeepVisibleEdgeY', 'ImGuiScrollFlags_MaskX_', 'ImGuiScrollFlags_MaskY_', 'ImGuiScrollFlags_NoScrollParent', 'ImGuiScrollFlags_None', 'ImGuiSelectableFlagsPrivate_', 'ImGuiSelectableFlags_', 'ImGuiSelectableFlags_AllowDoubleClick', 'ImGuiSelectableFlags_AllowOverlap', 'ImGuiSelectableFlags_Disabled', 'ImGuiSelectableFlags_DontClosePopups', 'ImGuiSelectableFlags_NoHoldingActiveID', 'ImGuiSelectableFlags_NoPadWithHalfSpacing', 'ImGuiSelectableFlags_NoSetKeyOwner', 'ImGuiSelectableFlags_None', 'ImGuiSelectableFlags_SelectOnClick', 'ImGuiSelectableFlags_SelectOnNav', 'ImGuiSelectableFlags_SelectOnRelease', 'ImGuiSelectableFlags_SetNavIdOnHover', 'ImGuiSelectableFlags_SpanAllColumns', 'ImGuiSelectableFlags_SpanAvailWidth', 'ImGuiSeparatorFlags_', 'ImGuiSeparatorFlags_Horizontal', 'ImGuiSeparatorFlags_None', 'ImGuiSeparatorFlags_SpanAllColumns', 'ImGuiSeparatorFlags_Vertical', 'ImGuiSettingsHandler', 'ImGuiShrinkWidthItem', 'ImGuiSizeCallbackData', 'ImGuiSliderFlagsPrivate_', 'ImGuiSliderFlags_', 'ImGuiSliderFlags_AlwaysClamp', 'ImGuiSliderFlags_InvalidMask_', 'ImGuiSliderFlags_Logarithmic', 'ImGuiSliderFlags_NoInput', 'ImGuiSliderFlags_NoRoundToFormat', 'ImGuiSliderFlags_None', 'ImGuiSliderFlags_ReadOnly', 'ImGuiSliderFlags_Vertical', 'ImGuiSliderFlags_WrapAround', 'ImGuiSortDirection', 'ImGuiSortDirection_Ascending', 'ImGuiSortDirection_Descending', 'ImGuiSortDirection_None', 'ImGuiStackLevelInfo', 'ImGuiStackSizes', 'ImGuiStorage', 'ImGuiStoragePair', 'ImGuiStyle', 'ImGuiStyleMod', 'ImGuiStyleVar_', 'ImGuiStyleVar_Alpha', 'ImGuiStyleVar_ButtonTextAlign', 'ImGuiStyleVar_COUNT', 'ImGuiStyleVar_CellPadding', 'ImGuiStyleVar_ChildBorderSize', 'ImGuiStyleVar_ChildRounding', 'ImGuiStyleVar_DisabledAlpha', 'ImGuiStyleVar_DockingSeparatorSize', 'ImGuiStyleVar_FrameBorderSize', 'ImGuiStyleVar_FramePadding', 'ImGuiStyleVar_FrameRounding', 'ImGuiStyleVar_GrabMinSize', 'ImGuiStyleVar_GrabRounding', 'ImGuiStyleVar_IndentSpacing', 'ImGuiStyleVar_ItemInnerSpacing', 'ImGuiStyleVar_ItemSpacing', 'ImGuiStyleVar_PopupBorderSize', 'ImGuiStyleVar_PopupRounding', 'ImGuiStyleVar_ScrollbarRounding', 'ImGuiStyleVar_ScrollbarSize', 'ImGuiStyleVar_SelectableTextAlign', 'ImGuiStyleVar_SeparatorTextAlign', 'ImGuiStyleVar_SeparatorTextBorderSize', 'ImGuiStyleVar_SeparatorTextPadding', 'ImGuiStyleVar_TabBarBorderSize', 'ImGuiStyleVar_TabBorderSize', 'ImGuiStyleVar_TabRounding', 'ImGuiStyleVar_TableAngledHeadersAngle', 'ImGuiStyleVar_TableAngledHeadersTextAlign', 'ImGuiStyleVar_WindowBorderSize', 'ImGuiStyleVar_WindowMinSize', 'ImGuiStyleVar_WindowPadding', 'ImGuiStyleVar_WindowRounding', 'ImGuiStyleVar_WindowTitleAlign', 'ImGuiTabBar', 'ImGuiTabBarFlagsPrivate_', 'ImGuiTabBarFlags_', 'ImGuiTabBarFlags_AutoSelectNewTabs', 'ImGuiTabBarFlags_DockNode', 'ImGuiTabBarFlags_DrawSelectedOverline', 'ImGuiTabBarFlags_FittingPolicyDefault_', 'ImGuiTabBarFlags_FittingPolicyMask_', 'ImGuiTabBarFlags_FittingPolicyResizeDown', 'ImGuiTabBarFlags_FittingPolicyScroll', 'ImGuiTabBarFlags_IsFocused', 'ImGuiTabBarFlags_NoCloseWithMiddleMouseButton', 'ImGuiTabBarFlags_NoTabListScrollingButtons', 'ImGuiTabBarFlags_NoTooltip', 'ImGuiTabBarFlags_None', 'ImGuiTabBarFlags_Reorderable', 'ImGuiTabBarFlags_SaveSettings', 'ImGuiTabBarFlags_TabListPopupButton', 'ImGuiTabItem', 'ImGuiTabItemFlagsPrivate_', 'ImGuiTabItemFlags_', 'ImGuiTabItemFlags_Button', 'ImGuiTabItemFlags_Leading', 'ImGuiTabItemFlags_NoAssumedClosure', 'ImGuiTabItemFlags_NoCloseButton', 'ImGuiTabItemFlags_NoCloseWithMiddleMouseButton', 'ImGuiTabItemFlags_NoPushId', 'ImGuiTabItemFlags_NoReorder', 'ImGuiTabItemFlags_NoTooltip', 'ImGuiTabItemFlags_None', 'ImGuiTabItemFlags_SectionMask_', 'ImGuiTabItemFlags_SetSelected', 'ImGuiTabItemFlags_Trailing', 'ImGuiTabItemFlags_UnsavedDocument', 'ImGuiTabItemFlags_Unsorted', 'ImGuiTable', 'ImGuiTableBgTarget_', 'ImGuiTableBgTarget_CellBg', 'ImGuiTableBgTarget_None', 'ImGuiTableBgTarget_RowBg0', 'ImGuiTableBgTarget_RowBg1', 'ImGuiTableCellData', 'ImGuiTableColumn', 'ImGuiTableColumnFlags_', 'ImGuiTableColumnFlags_AngledHeader', 'ImGuiTableColumnFlags_DefaultHide', 'ImGuiTableColumnFlags_DefaultSort', 'ImGuiTableColumnFlags_Disabled', 'ImGuiTableColumnFlags_IndentDisable', 'ImGuiTableColumnFlags_IndentEnable', 'ImGuiTableColumnFlags_IndentMask_', 'ImGuiTableColumnFlags_IsEnabled', 'ImGuiTableColumnFlags_IsHovered', 'ImGuiTableColumnFlags_IsSorted', 'ImGuiTableColumnFlags_IsVisible', 'ImGuiTableColumnFlags_NoClip', 'ImGuiTableColumnFlags_NoDirectResize_', 'ImGuiTableColumnFlags_NoHeaderLabel', 'ImGuiTableColumnFlags_NoHeaderWidth', 'ImGuiTableColumnFlags_NoHide', 'ImGuiTableColumnFlags_NoReorder', 'ImGuiTableColumnFlags_NoResize', 'ImGuiTableColumnFlags_NoSort', 'ImGuiTableColumnFlags_NoSortAscending', 'ImGuiTableColumnFlags_NoSortDescending', 'ImGuiTableColumnFlags_None', 'ImGuiTableColumnFlags_PreferSortAscending', 'ImGuiTableColumnFlags_PreferSortDescending', 'ImGuiTableColumnFlags_StatusMask_', 'ImGuiTableColumnFlags_WidthFixed', 'ImGuiTableColumnFlags_WidthMask_', 'ImGuiTableColumnFlags_WidthStretch', 'ImGuiTableColumnSettings', 'ImGuiTableColumnSortSpecs', 'ImGuiTableFlags_', 'ImGuiTableFlags_Borders', 'ImGuiTableFlags_BordersH', 'ImGuiTableFlags_BordersInner', 'ImGuiTableFlags_BordersInnerH', 'ImGuiTableFlags_BordersInnerV', 'ImGuiTableFlags_BordersOuter', 'ImGuiTableFlags_BordersOuterH', 'ImGuiTableFlags_BordersOuterV', 'ImGuiTableFlags_BordersV', 'ImGuiTableFlags_ContextMenuInBody', 'ImGuiTableFlags_Hideable', 'ImGuiTableFlags_HighlightHoveredColumn', 'ImGuiTableFlags_NoBordersInBody', 'ImGuiTableFlags_NoBordersInBodyUntilResize', 'ImGuiTableFlags_NoClip', 'ImGuiTableFlags_NoHostExtendX', 'ImGuiTableFlags_NoHostExtendY', 'ImGuiTableFlags_NoKeepColumnsVisible', 'ImGuiTableFlags_NoPadInnerX', 'ImGuiTableFlags_NoPadOuterX', 'ImGuiTableFlags_NoSavedSettings', 'ImGuiTableFlags_None', 'ImGuiTableFlags_PadOuterX', 'ImGuiTableFlags_PreciseWidths', 'ImGuiTableFlags_Reorderable', 'ImGuiTableFlags_Resizable', 'ImGuiTableFlags_RowBg', 'ImGuiTableFlags_ScrollX', 'ImGuiTableFlags_ScrollY', 'ImGuiTableFlags_SizingFixedFit', 'ImGuiTableFlags_SizingFixedSame', 'ImGuiTableFlags_SizingMask_', 'ImGuiTableFlags_SizingStretchProp', 'ImGuiTableFlags_SizingStretchSame', 'ImGuiTableFlags_SortMulti', 'ImGuiTableFlags_SortTristate', 'ImGuiTableFlags_Sortable', 'ImGuiTableHeaderData', 'ImGuiTableInstanceData', 'ImGuiTableRowFlags_', 'ImGuiTableRowFlags_Headers', 'ImGuiTableRowFlags_None', 'ImGuiTableSettings', 'ImGuiTableSortSpecs', 'ImGuiTableTempData', 'ImGuiTextBuffer', 'ImGuiTextFilter', 'ImGuiTextFlags_', 'ImGuiTextFlags_NoWidthForLargeClippedText', 'ImGuiTextFlags_None', 'ImGuiTextIndex', 'ImGuiTextRange', 'ImGuiTooltipFlags_', 'ImGuiTooltipFlags_None', 'ImGuiTooltipFlags_OverridePrevious', 'ImGuiTreeNodeFlagsPrivate_', 'ImGuiTreeNodeFlags_', 'ImGuiTreeNodeFlags_AllowOverlap', 'ImGuiTreeNodeFlags_Bullet', 'ImGuiTreeNodeFlags_ClipLabelForTrailingButton', 'ImGuiTreeNodeFlags_CollapsingHeader', 'ImGuiTreeNodeFlags_DefaultOpen', 'ImGuiTreeNodeFlags_FramePadding', 'ImGuiTreeNodeFlags_Framed', 'ImGuiTreeNodeFlags_Leaf', 'ImGuiTreeNodeFlags_NavLeftJumpsBackHere', 'ImGuiTreeNodeFlags_NoAutoOpenOnLog', 'ImGuiTreeNodeFlags_NoTreePushOnOpen', 'ImGuiTreeNodeFlags_None', 'ImGuiTreeNodeFlags_OpenOnArrow', 'ImGuiTreeNodeFlags_OpenOnDoubleClick', 'ImGuiTreeNodeFlags_Selected', 'ImGuiTreeNodeFlags_SpanAllColumns', 'ImGuiTreeNodeFlags_SpanAvailWidth', 'ImGuiTreeNodeFlags_SpanFullWidth', 'ImGuiTreeNodeFlags_SpanTextWidth', 'ImGuiTreeNodeFlags_UpsideDownArrow', 'ImGuiTypingSelectFlags_', 'ImGuiTypingSelectFlags_AllowBackspace', 'ImGuiTypingSelectFlags_AllowSingleCharMode', 'ImGuiTypingSelectFlags_None', 'ImGuiTypingSelectRequest', 'ImGuiTypingSelectState', 'ImGuiViewport', 'ImGuiViewportFlags_', 'ImGuiViewportFlags_CanHostOtherWindows', 'ImGuiViewportFlags_IsFocused', 'ImGuiViewportFlags_IsMinimized', 'ImGuiViewportFlags_IsPlatformMonitor', 'ImGuiViewportFlags_IsPlatformWindow', 'ImGuiViewportFlags_NoAutoMerge', 'ImGuiViewportFlags_NoDecoration', 'ImGuiViewportFlags_NoFocusOnAppearing', 'ImGuiViewportFlags_NoFocusOnClick', 'ImGuiViewportFlags_NoInputs', 'ImGuiViewportFlags_NoRendererClear', 'ImGuiViewportFlags_NoTaskBarIcon', 'ImGuiViewportFlags_None', 'ImGuiViewportFlags_OwnedByApp', 'ImGuiViewportFlags_TopMost', 'ImGuiViewportP', 'ImGuiWindow', 'ImGuiWindowClass', 'ImGuiWindowDockStyle', 'ImGuiWindowDockStyleCol', 'ImGuiWindowDockStyleCol_COUNT', 'ImGuiWindowDockStyleCol_TabDimmed', 'ImGuiWindowDockStyleCol_TabDimmedSelected', 'ImGuiWindowDockStyleCol_TabDimmedSelectedOverline', 'ImGuiWindowDockStyleCol_TabFocused', 'ImGuiWindowDockStyleCol_TabHovered', 'ImGuiWindowDockStyleCol_TabSelected', 'ImGuiWindowDockStyleCol_TabSelectedOverline', 'ImGuiWindowDockStyleCol_Text', 'ImGuiWindowFlags_', 'ImGuiWindowFlags_AlwaysAutoResize', 'ImGuiWindowFlags_AlwaysHorizontalScrollbar', 'ImGuiWindowFlags_AlwaysVerticalScrollbar', 'ImGuiWindowFlags_ChildMenu', 'ImGuiWindowFlags_ChildWindow', 'ImGuiWindowFlags_DockNodeHost', 'ImGuiWindowFlags_HorizontalScrollbar', 'ImGuiWindowFlags_MenuBar', 'ImGuiWindowFlags_Modal', 'ImGuiWindowFlags_NoBackground', 'ImGuiWindowFlags_NoBringToFrontOnFocus', 'ImGuiWindowFlags_NoCollapse', 'ImGuiWindowFlags_NoDecoration', 'ImGuiWindowFlags_NoDocking', 'ImGuiWindowFlags_NoFocusOnAppearing', 'ImGuiWindowFlags_NoInputs', 'ImGuiWindowFlags_NoMouseInputs', 'ImGuiWindowFlags_NoMove', 'ImGuiWindowFlags_NoNav', 'ImGuiWindowFlags_NoNavFocus', 'ImGuiWindowFlags_NoNavInputs', 'ImGuiWindowFlags_NoResize', 'ImGuiWindowFlags_NoSavedSettings', 'ImGuiWindowFlags_NoScrollWithMouse', 'ImGuiWindowFlags_NoScrollbar', 'ImGuiWindowFlags_NoTitleBar', 'ImGuiWindowFlags_None', 'ImGuiWindowFlags_Popup', 'ImGuiWindowFlags_Tooltip', 'ImGuiWindowFlags_UnsavedDocument', 'ImGuiWindowRefreshFlags_', 'ImGuiWindowRefreshFlags_None', 'ImGuiWindowRefreshFlags_RefreshOnFocus', 'ImGuiWindowRefreshFlags_RefreshOnHover', 'ImGuiWindowRefreshFlags_TryToAvoidRefresh', 'ImGuiWindowSettings', 'ImGuiWindowStackData', 'ImGuiWindowTempData', 'ImHashData', 'ImHashStr', 'ImInvLength', 'ImIsFloatAboveGuaranteedIntegerPrecision', 'ImIsPowerOfTwo', 'ImLengthSqr', 'ImLerp', 'ImLineClosestPoint', 'ImLinearSweep', 'ImLog', 'ImLowerBound', 'ImMax', 'ImMin', 'ImModPositive', 'ImMul', 'ImParseFormatFindEnd', 'ImParseFormatFindStart', 'ImParseFormatPrecision', 'ImParseFormatSanitizeForPrinting', 'ImParseFormatSanitizeForScanning', 'ImParseFormatTrimDecorations', 'ImPool_ImGuiTabBar', 'ImPool_ImGuiTable', 'ImPow', 'ImRect', 'ImRotate', 'ImRsqrt', 'ImSaturate', 'ImSign', 'ImSpan_ImGuiTableCellData', 'ImSpan_ImGuiTableColumn', 'ImSpan_ImGuiTableColumnIdx', 'ImStrSkipBlank', 'ImStrTrimBlanks', 'ImStrbolW', 'ImStrchrRange', 'ImStrdup', 'ImStrdupcpy', 'ImStreolRange', 'ImStricmp', 'ImStristr', 'ImStrlenW', 'ImStrncpy', 'ImStrnicmp', 'ImTextCharFromUtf8', 'ImTextCharToUtf8', 'ImTextCountCharsFromUtf8', 'ImTextCountLines', 'ImTextCountUtf8BytesFromChar', 'ImTextCountUtf8BytesFromStr', 'ImTextFindPreviousUtf8Codepoint', 'ImTextStrToUtf8', 'ImToUpper', 'ImTriangleArea', 'ImTriangleBarycentricCoords', 'ImTriangleClosestPoint', 'ImTriangleContainsPoint', 'ImTriangleIsClockwise', 'ImTrunc', 'ImUpperPowerOfTwo', 'ImVec1', 'ImVec2', 'ImVec2ih', 'ImVec4', 'ImVector_ImDrawChannel', 'ImVector_ImDrawCmd', 'ImVector_ImDrawIdx', 'ImVector_ImDrawListPtr', 'ImVector_ImDrawVert', 'ImVector_ImFontAtlasCustomRect', 'ImVector_ImFontConfig', 'ImVector_ImFontGlyph', 'ImVector_ImFontPtr', 'ImVector_ImGuiColorMod', 'ImVector_ImGuiContextHook', 'ImVector_ImGuiDockNodeSettings', 'ImVector_ImGuiDockRequest', 'ImVector_ImGuiFocusScopeData', 'ImVector_ImGuiGroupData', 'ImVector_ImGuiID', 'ImVector_ImGuiInputEvent', 'ImVector_ImGuiItemFlags', 'ImVector_ImGuiKeyRoutingData', 'ImVector_ImGuiListClipperData', 'ImVector_ImGuiListClipperRange', 'ImVector_ImGuiNavTreeNodeData', 'ImVector_ImGuiOldColumnData', 'ImVector_ImGuiOldColumns', 'ImVector_ImGuiPlatformMonitor', 'ImVector_ImGuiPopupData', 'ImVector_ImGuiPtrOrIndex', 'ImVector_ImGuiSettingsHandler', 'ImVector_ImGuiShrinkWidthItem', 'ImVector_ImGuiStackLevelInfo', 'ImVector_ImGuiStoragePair', 'ImVector_ImGuiStyleMod', 'ImVector_ImGuiTabItem', 'ImVector_ImGuiTableColumnSortSpecs', 'ImVector_ImGuiTableHeaderData', 'ImVector_ImGuiTableInstanceData', 'ImVector_ImGuiTableTempData', 'ImVector_ImGuiTextRange', 'ImVector_ImGuiViewportPPtr', 'ImVector_ImGuiViewportPtr', 'ImVector_ImGuiWindowPtr', 'ImVector_ImGuiWindowStackData', 'ImVector_ImTextureID', 'ImVector_ImU32', 'ImVector_ImVec2', 'ImVector_ImVec4', 'ImVector_ImWchar', 'ImVector_char', 'ImVector_float', 'ImVector_int', 'ImVector_unsigned_char', 'Image', 'ImageButton', 'ImageButtonEx', 'Indent', 'Initialize', 'InputDouble', 'InputFloat', 'InputFloat2', 'InputFloat3', 'InputFloat4', 'InputInt', 'InputInt2', 'InputInt3', 'InputInt4', 'InputScalar', 'InputScalarN', 'InputText', 'InputTextDeactivateHook', 'InputTextEx', 'InputTextMultiline', 'InputTextWithHint', 'InvisibleButton', 'IsActiveIdUsingNavDir', 'IsAliasKey', 'IsAnyItemActive', 'IsAnyItemFocused', 'IsAnyItemHovered', 'IsAnyMouseDown', 'IsClippedEx', 'IsDragDropActive', 'IsDragDropPayloadBeingAccepted', 'IsGamepadKey', 'IsItemActivated', 'IsItemActive', 'IsItemClicked', 'IsItemDeactivated', 'IsItemDeactivatedAfterEdit', 'IsItemEdited', 'IsItemFocused', 'IsItemHovered', 'IsItemToggledOpen', 'IsItemToggledSelection', 'IsItemVisible', 'IsKeyChordPressed', 'IsKeyDown', 'IsKeyPressed', 'IsKeyReleased', 'IsKeyboardKey', 'IsLegacyKey', 'IsModKey', 'IsMouseClicked', 'IsMouseDoubleClicked', 'IsMouseDown', 'IsMouseDragPastThreshold', 'IsMouseDragging', 'IsMouseHoveringRect', 'IsMouseKey', 'IsMousePosValid', 'IsMouseReleased', 'IsNamedKey', 'IsNamedKeyOrMod', 'IsPopupOpen', 'IsRectVisible', 'IsWindowAbove', 'IsWindowAppearing', 'IsWindowChildOf', 'IsWindowCollapsed', 'IsWindowContentHoverable', 'IsWindowDocked', 'IsWindowFocused', 'IsWindowHovered', 'IsWindowNavFocusable', 'IsWindowWithinBeginStackOf', 'ItemAdd', 'ItemHoverable', 'ItemSize', 'KeepAliveID', 'LoadIniSettingsFromDisk', 'LoadIniSettingsFromMemory', 'LocalizeGetMsg', 'LocalizeRegisterEntries', 'LogBegin', 'LogButtons', 'LogFinish', 'LogRenderedText', 'LogSetNextTextDecoration', 'LogToBuffer', 'LogToClipboard', 'LogToFile', 'LogToTTY', 'MarkIniSettingsDirty', 'MarkItemEdited', 'MemAlloc', 'MemFree', 'MenuItem', 'MenuItemEx', 'MouseButtonToKey', 'NavClearPreferredPosForAxis', 'NavHighlightActivated', 'NavInitRequestApplyResult', 'NavInitWindow', 'NavMoveRequestApplyResult', 'NavMoveRequestButNoResultYet', 'NavMoveRequestCancel', 'NavMoveRequestForward', 'NavMoveRequestResolveWithLastItem', 'NavMoveRequestResolveWithPastTreeNode', 'NavMoveRequestSubmit', 'NavMoveRequestTryWrapping', 'NavRestoreHighlightAfterMove', 'NavUpdateCurrentWindowIsScrollPushableX', 'NewFrame', 'NewLine', 'NextColumn', 'OpenPopup', 'OpenPopupEx', 'OpenPopupOnItemClick', 'PlotHistogram', 'PlotLines', 'PopButtonRepeat', 'PopClipRect', 'PopColumnsBackground', 'PopFocusScope', 'PopFont', 'PopID', 'PopItemFlag', 'PopItemWidth', 'PopStyleColor', 'PopStyleVar', 'PopTabStop', 'PopTextWrapPos', 'ProgressBar', 'PushButtonRepeat', 'PushClipRect', 'PushColumnClipRect', 'PushColumnsBackground', 'PushFocusScope', 'PushFont', 'PushID', 'PushItemFlag', 'PushItemWidth', 'PushMultiItemsWidths', 'PushOverrideID', 'PushStyleColor', 'PushStyleVar', 'PushTabStop', 'PushTextWrapPos', 'RadioButton', 'RemoveContextHook', 'RemoveSettingsHandler', 'Render', 'RenderArrow', 'RenderArrowDockMenu', 'RenderArrowPointingAt', 'RenderBullet', 'RenderCheckMark', 'RenderColorRectWithAlphaCheckerboard', 'RenderDragDropTargetRect', 'RenderFrame', 'RenderFrameBorder', 'RenderMouseCursor', 'RenderNavHighlight', 'RenderPlatformWindowsDefault', 'RenderRectFilledRangeH', 'RenderRectFilledWithHole', 'RenderText', 'RenderTextClipped', 'RenderTextClippedEx', 'RenderTextEllipsis', 'RenderTextWrapped', 'ResetMouseDragDelta', 'STB_TexteditState', 'SameLine', 'SaveIniSettingsToDisk', 'SaveIniSettingsToMemory', 'ScaleWindowsInViewport', 'ScrollToBringRectIntoView', 'ScrollToItem', 'ScrollToRect', 'ScrollToRectEx', 'Scrollbar', 'ScrollbarEx', 'Selectable', 'Separator', 'SeparatorEx', 'SeparatorText', 'SeparatorTextEx', 'SetActiveID', 'SetActiveIdUsingAllKeyboardKeys', 'SetAllocatorFunctions', 'SetClipboardText', 'SetColorEditOptions', 'SetColumnOffset', 'SetColumnWidth', 'SetCurrentContext', 'SetCurrentFont', 'SetCurrentViewport', 'SetCursorPos', 'SetCursorPosX', 'SetCursorPosY', 'SetCursorScreenPos', 'SetDragDropPayload', 'SetFocusID', 'SetHoveredID', 'SetItemDefaultFocus', 'SetItemKeyOwner', 'SetKeyOwner', 'SetKeyOwnersForKeyChord', 'SetKeyboardFocusHere', 'SetLastItemData', 'SetMouseCursor', 'SetNavFocusScope', 'SetNavID', 'SetNavWindow', 'SetNextFrameWantCaptureKeyboard', 'SetNextFrameWantCaptureMouse', 'SetNextItemAllowOverlap', 'SetNextItemOpen', 'SetNextItemRefVal', 'SetNextItemSelectionUserData', 'SetNextItemShortcut', 'SetNextItemWidth', 'SetNextWindowBgAlpha', 'SetNextWindowClass', 'SetNextWindowCollapsed', 'SetNextWindowContentSize', 'SetNextWindowDockID', 'SetNextWindowFocus', 'SetNextWindowPos', 'SetNextWindowRefreshPolicy', 'SetNextWindowScroll', 'SetNextWindowSize', 'SetNextWindowSizeConstraints', 'SetNextWindowViewport', 'SetScrollFromPosX', 'SetScrollFromPosY', 'SetScrollHereX', 'SetScrollHereY', 'SetScrollX', 'SetScrollY', 'SetShortcutRouting', 'SetStateStorage', 'SetTabItemClosed', 'SetWindowClipRectBeforeSetChannel', 'SetWindowCollapsed', 'SetWindowDock', 'SetWindowFocus', 'SetWindowFontScale', 'SetWindowHiddenAndSkipItemsForCurrentFrame', 'SetWindowHitTestHole', 'SetWindowParentWindowForFocusRoute', 'SetWindowPos', 'SetWindowSize', 'SetWindowViewport', 'ShadeVertsLinearColorGradientKeepAlpha', 'ShadeVertsLinearUV', 'ShadeVertsTransformPos', 'Shortcut', 'ShowAboutWindow', 'ShowDebugLogWindow', 'ShowDemoWindow', 'ShowFontAtlas', 'ShowFontSelector', 'ShowIDStackToolWindow', 'ShowMetricsWindow', 'ShowStyleEditor', 'ShowStyleSelector', 'ShowUserGuide', 'ShrinkWidths', 'Shutdown', 'SliderAngle', 'SliderBehavior', 'SliderFloat', 'SliderFloat2', 'SliderFloat3', 'SliderFloat4', 'SliderInt', 'SliderInt2', 'SliderInt3', 'SliderInt4', 'SliderScalar', 'SliderScalarN', 'SmallButton', 'Spacing', 'SplitterBehavior', 'StartMouseMovingWindow', 'StartMouseMovingWindowOrNode', 'StbTexteditRow', 'StbUndoRecord', 'StbUndoState', 'StyleColorsClassic', 'StyleColorsDark', 'StyleColorsLight', 'TabBarAddTab', 'TabBarCloseTab', 'TabBarFindMostRecentlySelectedTabForActiveWindow', 'TabBarFindTabByID', 'TabBarFindTabByOrder', 'TabBarGetCurrentTab', 'TabBarGetTabName', 'TabBarGetTabOrder', 'TabBarProcessReorder', 'TabBarQueueFocus', 'TabBarQueueReorder', 'TabBarQueueReorderFromMousePos', 'TabBarRemoveTab', 'TabItemBackground', 'TabItemButton', 'TabItemCalcSize', 'TabItemEx', 'TabItemLabelAndCloseButton', 'TableAngledHeadersRow', 'TableAngledHeadersRowEx', 'TableBeginApplyRequests', 'TableBeginCell', 'TableBeginContextMenuPopup', 'TableBeginInitMemory', 'TableBeginRow', 'TableDrawBorders', 'TableDrawDefaultContextMenu', 'TableEndCell', 'TableEndRow', 'TableFindByID', 'TableFixColumnSortDirection', 'TableGcCompactSettings', 'TableGcCompactTransientBuffers', 'TableGetBoundSettings', 'TableGetCellBgRect', 'TableGetColumnCount', 'TableGetColumnFlags', 'TableGetColumnIndex', 'TableGetColumnName', 'TableGetColumnNextSortDirection', 'TableGetColumnResizeID', 'TableGetColumnWidthAuto', 'TableGetHeaderAngledMaxLabelWidth', 'TableGetHeaderRowHeight', 'TableGetHoveredColumn', 'TableGetHoveredRow', 'TableGetInstanceData', 'TableGetInstanceID', 'TableGetMaxColumnWidth', 'TableGetRowIndex', 'TableGetSortSpecs', 'TableHeader', 'TableHeadersRow', 'TableLoadSettings', 'TableMergeDrawChannels', 'TableNextColumn', 'TableNextRow', 'TableOpenContextMenu', 'TablePopBackgroundChannel', 'TablePushBackgroundChannel', 'TableRemove', 'TableResetSettings', 'TableSaveSettings', 'TableSetBgColor', 'TableSetColumnEnabled', 'TableSetColumnIndex', 'TableSetColumnSortDirection', 'TableSetColumnWidth', 'TableSetColumnWidthAutoAll', 'TableSetColumnWidthAutoSingle', 'TableSettingsAddSettingsHandler', 'TableSettingsCreate', 'TableSettingsFindByID', 'TableSetupColumn', 'TableSetupDrawChannels', 'TableSetupScrollFreeze', 'TableSortSpecsBuild', 'TableSortSpecsSanitize', 'TableUpdateBorders', 'TableUpdateColumnsWeightFromWidth', 'TableUpdateLayout', 'TeleportMousePos', 'TempInputIsActive', 'TempInputScalar', 'TempInputText', 'TestKeyOwner', 'TestShortcutRouting', 'Text', 'TextColored', 'TextDisabled', 'TextEx', 'TextUnformatted', 'TextWrapped', 'TranslateWindowsInViewport', 'TreeNode', 'TreeNodeBehavior', 'TreeNodeEx', 'TreeNodeSetOpen', 'TreeNodeUpdateNextOpen', 'TreePop', 'TreePush', 'TreePushOverrideID', 'Unindent', 'UpdateHoveredWindowAndCaptureFlags', 'UpdateInputEvents', 'UpdateMouseMovingWindowEndFrame', 'UpdateMouseMovingWindowNewFrame', 'UpdatePlatformWindows', 'UpdateWindowParentAndRootLinks', 'UpdateWindowSkipRefresh', 'VSliderFloat', 'VSliderInt', 'VSliderScalar', 'Value', 'WindowPosRelToAbs', 'WindowRectAbsToRel', 'WindowRectRelToAbs', 'ctx']
class Arr_ImGuiDebugAllocEntry:
    def __getitem__(self, arg0: int) -> ImGuiDebugAllocEntry:
        ...
    def __iter__(self) -> typing.Iterator[ImGuiDebugAllocEntry]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: ImGuiDebugAllocEntry) -> None:
        ...
class Arr_ImGuiKeyData:
    def __getitem__(self, arg0: int) -> ImGuiKeyData:
        ...
    def __iter__(self) -> typing.Iterator[ImGuiKeyData]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: ImGuiKeyData) -> None:
        ...
class Arr_ImGuiKeyOwnerData:
    def __getitem__(self, arg0: int) -> ImGuiKeyOwnerData:
        ...
    def __iter__(self) -> typing.Iterator[ImGuiKeyOwnerData]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: ImGuiKeyOwnerData) -> None:
        ...
class Arr_ImRect:
    def __getitem__(self, arg0: int) -> ImRect:
        ...
    def __iter__(self) -> typing.Iterator[ImRect]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: ImRect) -> None:
        ...
class Arr_ImVec2:
    def __getitem__(self, arg0: int) -> ImVec2:
        ...
    def __iter__(self) -> typing.Iterator[ImVec2]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: ImVec2) -> None:
        ...
class Arr_ImVec4:
    def __getitem__(self, arg0: int) -> ImVec4:
        ...
    def __iter__(self) -> typing.Iterator[ImVec4]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: ImVec4) -> None:
        ...
class Arr_StbUndoRecord:
    def __getitem__(self, arg0: int) -> StbUndoRecord:
        ...
    def __iter__(self) -> typing.Iterator[StbUndoRecord]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: StbUndoRecord) -> None:
        ...
class Arr_bool:
    def __getitem__(self, arg0: int) -> bool:
        ...
    def __iter__(self) -> typing.Iterator[bool]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: bool) -> None:
        ...
class Arr_char:
    def __getitem__(self, arg0: int) -> str:
        ...
    def __iter__(self) -> typing.Iterator[str]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: str) -> None:
        ...
class Arr_double:
    def __getitem__(self, arg0: int) -> float:
        ...
    def __iter__(self) -> typing.Iterator[float]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
class Arr_float:
    def __getitem__(self, arg0: int) -> float:
        ...
    def __iter__(self) -> typing.Iterator[float]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
class Arr_int:
    def __getitem__(self, arg0: int) -> int:
        ...
    def __iter__(self) -> typing.Iterator[int]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
class Arr_p_ImDrawList:
    def __getitem__(self, arg0: int) -> ImDrawList:
        ...
    def __iter__(self) -> typing.Iterator[ImDrawList]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: ImDrawList) -> None:
        ...
class Arr_p_ImGuiDockNode:
    def __getitem__(self, arg0: int) -> ImGuiDockNode:
        ...
    def __iter__(self) -> typing.Iterator[ImGuiDockNode]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: ImGuiDockNode) -> None:
        ...
class Arr_p_ImVector_ImDrawListPtr:
    def __getitem__(self, arg0: int) -> ImVector_ImDrawListPtr:
        ...
    def __iter__(self) -> typing.Iterator[ImVector_ImDrawListPtr]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: ImVector_ImDrawListPtr) -> None:
        ...
class Arr_p_const_char:
    def __getitem__(self, arg0: int) -> str:
        ...
    def __iter__(self) -> typing.Iterator[str]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: str) -> None:
        ...
class Arr_signed_short:
    def __getitem__(self, arg0: int) -> int:
        ...
    def __iter__(self) -> typing.Iterator[int]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
class Arr_unsigned_char:
    def __getitem__(self, arg0: int) -> int:
        ...
    def __iter__(self) -> typing.Iterator[int]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
class Arr_unsigned_int:
    def __getitem__(self, arg0: int) -> int:
        ...
    def __iter__(self) -> typing.Iterator[int]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
class Arr_unsigned_short:
    def __getitem__(self, arg0: int) -> int:
        ...
    def __iter__(self) -> typing.Iterator[int]:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
class GlyphRanges:
    def ToList(self) -> list[int]:
        ...
class ImBitVector:
    Storage: ImVector_ImU32
    def Clear(self) -> None:
        ...
    def ClearBit(self, n: int) -> None:
        ...
    def Create(self, sz: int) -> None:
        ...
    def SetBit(self, n: int) -> None:
        ...
    def TestBit(self, n: int) -> bool:
        ...
class ImChunkStream_ImGuiTableSettings:
    pass
class ImChunkStream_ImGuiWindowSettings:
    pass
class ImColor:
    Value: ImVec4
    @staticmethod
    def HSV(h: float, s: float, v: float, a: float = 1.0) -> ImColor:
        ...
    def SetHSV(self, h: float, s: float, v: float, a: float = 1.0) -> None:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, r: float, g: float, b: float, a: float = 1.0) -> None:
        ...
    @typing.overload
    def __init__(self, col: ImVec4) -> None:
        ...
    @typing.overload
    def __init__(self, r: int, g: int, b: int, a: int = 255) -> None:
        ...
    @typing.overload
    def __init__(self, rgba: int) -> None:
        ...
class ImDrawChannel:
    _CmdBuffer: ImVector_ImDrawCmd
    _IdxBuffer: ImVector_ImDrawIdx
class ImDrawCmd:
    ClipRect: ImVec4
    ElemCount: int
    IdxOffset: int
    TextureId: capsule
    UserCallbackData: capsule
    VtxOffset: int
    def GetTexID(self) -> capsule:
        ...
    def __init__(self) -> None:
        ...
    @property
    def UserCallback(*args, **kwargs):
        """
        (arg0: pyimgui.imgui.ImDrawCmd) -> void __cdecl(ImDrawList const * __ptr64,ImDrawCmd const * __ptr64)
        """
    @UserCallback.setter
    def UserCallback(self, arg1: ...) -> None:
        ...
class ImDrawCmdHeader:
    ClipRect: ImVec4
    TextureId: capsule
    VtxOffset: int
class ImDrawData:
    CmdLists: ImVector_ImDrawListPtr
    CmdListsCount: int
    DisplayPos: ImVec2
    DisplaySize: ImVec2
    FramebufferScale: ImVec2
    OwnerViewport: ImGuiViewport
    TotalIdxCount: int
    TotalVtxCount: int
    Valid: bool
    def AddDrawList(self, draw_list: ImDrawList) -> None:
        ...
    def Clear(self) -> None:
        ...
    def DeIndexAllBuffers(self) -> None:
        ...
    def ScaleClipRects(self, fb_scale: ImVec2) -> None:
        ...
    def __init__(self) -> None:
        ...
class ImDrawDataBuilder:
    LayerData1: ImVector_ImDrawListPtr
    def __init__(self) -> None:
        ...
    @property
    def Layers(self) -> Arr_p_ImVector_ImDrawListPtr:
        ...
class ImDrawFlags_:
    """
    Members:
    
      ImDrawFlags_None
    
      ImDrawFlags_Closed
    
      ImDrawFlags_RoundCornersTopLeft
    
      ImDrawFlags_RoundCornersTopRight
    
      ImDrawFlags_RoundCornersBottomLeft
    
      ImDrawFlags_RoundCornersBottomRight
    
      ImDrawFlags_RoundCornersNone
    
      ImDrawFlags_RoundCornersTop
    
      ImDrawFlags_RoundCornersBottom
    
      ImDrawFlags_RoundCornersLeft
    
      ImDrawFlags_RoundCornersRight
    
      ImDrawFlags_RoundCornersAll
    
      ImDrawFlags_RoundCornersDefault_
    
      ImDrawFlags_RoundCornersMask_
    """
    ImDrawFlags_Closed: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_Closed: 1>
    ImDrawFlags_None: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_None: 0>
    ImDrawFlags_RoundCornersAll: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersAll: 240>
    ImDrawFlags_RoundCornersBottom: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersBottom: 192>
    ImDrawFlags_RoundCornersBottomLeft: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersBottomLeft: 64>
    ImDrawFlags_RoundCornersBottomRight: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersBottomRight: 128>
    ImDrawFlags_RoundCornersDefault_: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersAll: 240>
    ImDrawFlags_RoundCornersLeft: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersLeft: 80>
    ImDrawFlags_RoundCornersMask_: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersMask_: 496>
    ImDrawFlags_RoundCornersNone: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersNone: 256>
    ImDrawFlags_RoundCornersRight: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersRight: 160>
    ImDrawFlags_RoundCornersTop: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersTop: 48>
    ImDrawFlags_RoundCornersTopLeft: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersTopLeft: 16>
    ImDrawFlags_RoundCornersTopRight: typing.ClassVar[ImDrawFlags_]  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersTopRight: 32>
    __members__: typing.ClassVar[dict[str, ImDrawFlags_]]  # value = {'ImDrawFlags_None': <ImDrawFlags_.ImDrawFlags_None: 0>, 'ImDrawFlags_Closed': <ImDrawFlags_.ImDrawFlags_Closed: 1>, 'ImDrawFlags_RoundCornersTopLeft': <ImDrawFlags_.ImDrawFlags_RoundCornersTopLeft: 16>, 'ImDrawFlags_RoundCornersTopRight': <ImDrawFlags_.ImDrawFlags_RoundCornersTopRight: 32>, 'ImDrawFlags_RoundCornersBottomLeft': <ImDrawFlags_.ImDrawFlags_RoundCornersBottomLeft: 64>, 'ImDrawFlags_RoundCornersBottomRight': <ImDrawFlags_.ImDrawFlags_RoundCornersBottomRight: 128>, 'ImDrawFlags_RoundCornersNone': <ImDrawFlags_.ImDrawFlags_RoundCornersNone: 256>, 'ImDrawFlags_RoundCornersTop': <ImDrawFlags_.ImDrawFlags_RoundCornersTop: 48>, 'ImDrawFlags_RoundCornersBottom': <ImDrawFlags_.ImDrawFlags_RoundCornersBottom: 192>, 'ImDrawFlags_RoundCornersLeft': <ImDrawFlags_.ImDrawFlags_RoundCornersLeft: 80>, 'ImDrawFlags_RoundCornersRight': <ImDrawFlags_.ImDrawFlags_RoundCornersRight: 160>, 'ImDrawFlags_RoundCornersAll': <ImDrawFlags_.ImDrawFlags_RoundCornersAll: 240>, 'ImDrawFlags_RoundCornersDefault_': <ImDrawFlags_.ImDrawFlags_RoundCornersAll: 240>, 'ImDrawFlags_RoundCornersMask_': <ImDrawFlags_.ImDrawFlags_RoundCornersMask_: 496>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImDrawList:
    CmdBuffer: ImVector_ImDrawCmd
    Flags: int
    IdxBuffer: ImVector_ImDrawIdx
    VtxBuffer: ImVector_ImDrawVert
    _ClipRectStack: ImVector_ImVec4
    _CmdHeader: ImDrawCmdHeader
    _Data: ImDrawListSharedData
    _FringeScale: float
    _IdxWritePtr: int
    _OwnerName: str
    _Path: ImVector_ImVec2
    _Splitter: ImDrawListSplitter
    _TextureIdStack: ImVector_ImTextureID
    _VtxCurrentIdx: int
    _VtxWritePtr: ImDrawVert
    def AddBezierCubic(self, p1: ImVec2, p2: ImVec2, p3: ImVec2, p4: ImVec2, col: int, thickness: float, num_segments: int = 0) -> None:
        ...
    def AddBezierQuadratic(self, p1: ImVec2, p2: ImVec2, p3: ImVec2, col: int, thickness: float, num_segments: int = 0) -> None:
        ...
    def AddCallback(self, callback: ..., callback_data: capsule) -> None:
        ...
    def AddCircle(self, center: ImVec2, radius: float, col: int, num_segments: int = 0, thickness: float = 1.0) -> None:
        ...
    def AddCircleFilled(self, center: ImVec2, radius: float, col: int, num_segments: int = 0) -> None:
        ...
    def AddConcavePolyFilled(self, points: ImVec2, num_points: int, col: int) -> None:
        ...
    def AddConvexPolyFilled(self, points: ImVec2, num_points: int, col: int) -> None:
        ...
    def AddDrawCmd(self) -> None:
        ...
    def AddEllipse(self, center: ImVec2, radius: ImVec2, col: int, rot: float = 0.0, num_segments: int = 0, thickness: float = 1.0) -> None:
        ...
    def AddEllipseFilled(self, center: ImVec2, radius: ImVec2, col: int, rot: float = 0.0, num_segments: int = 0) -> None:
        ...
    def AddImage(self, user_texture_id: capsule, p_min: ImVec2, p_max: ImVec2, uv_min: ImVec2 = ..., uv_max: ImVec2 = ..., col: int = 4294967295) -> None:
        ...
    def AddImageQuad(self, user_texture_id: capsule, p1: ImVec2, p2: ImVec2, p3: ImVec2, p4: ImVec2, uv1: ImVec2 = ..., uv2: ImVec2 = ..., uv3: ImVec2 = ..., uv4: ImVec2 = ..., col: int = 4294967295) -> None:
        ...
    def AddImageRounded(self, user_texture_id: capsule, p_min: ImVec2, p_max: ImVec2, uv_min: ImVec2, uv_max: ImVec2, col: int, rounding: float, flags: int = 0) -> None:
        ...
    def AddLine(self, p1: ImVec2, p2: ImVec2, col: int, thickness: float = 1.0) -> None:
        ...
    def AddNgon(self, center: ImVec2, radius: float, col: int, num_segments: int, thickness: float = 1.0) -> None:
        ...
    def AddNgonFilled(self, center: ImVec2, radius: float, col: int, num_segments: int) -> None:
        ...
    def AddPolyline(self, points: ImVec2, num_points: int, col: int, flags: int, thickness: float) -> None:
        ...
    def AddQuad(self, p1: ImVec2, p2: ImVec2, p3: ImVec2, p4: ImVec2, col: int, thickness: float = 1.0) -> None:
        ...
    def AddQuadFilled(self, p1: ImVec2, p2: ImVec2, p3: ImVec2, p4: ImVec2, col: int) -> None:
        ...
    def AddRect(self, p_min: ImVec2, p_max: ImVec2, col: int, rounding: float = 0.0, flags: int = 0, thickness: float = 1.0) -> None:
        ...
    def AddRectFilled(self, p_min: ImVec2, p_max: ImVec2, col: int, rounding: float = 0.0, flags: int = 0) -> None:
        ...
    def AddRectFilledMultiColor(self, p_min: ImVec2, p_max: ImVec2, col_upr_left: int, col_upr_right: int, col_bot_right: int, col_bot_left: int) -> None:
        ...
    @typing.overload
    def AddText(self, pos: ImVec2, col: int, text_begin: str, text_end: str = 0) -> None:
        ...
    @typing.overload
    def AddText(self, font: ImFont, font_size: float, pos: ImVec2, col: int, text_begin: str, text_end: str = 0, wrap_width: float = 0.0, cpu_fine_clip_rect: ImVec4 | None = None) -> None:
        ...
    def AddTriangle(self, p1: ImVec2, p2: ImVec2, p3: ImVec2, col: int, thickness: float = 1.0) -> None:
        ...
    def AddTriangleFilled(self, p1: ImVec2, p2: ImVec2, p3: ImVec2, col: int) -> None:
        ...
    def ChannelsMerge(self) -> None:
        ...
    def ChannelsSetCurrent(self, n: int) -> None:
        ...
    def ChannelsSplit(self, count: int) -> None:
        ...
    def CloneOutput(self) -> ImDrawList:
        ...
    def GetClipRectMax(self) -> ImVec2:
        ...
    def GetClipRectMin(self) -> ImVec2:
        ...
    def PathArcTo(self, center: ImVec2, radius: float, a_min: float, a_max: float, num_segments: int = 0) -> None:
        ...
    def PathArcToFast(self, center: ImVec2, radius: float, a_min_of_12: int, a_max_of_12: int) -> None:
        ...
    def PathBezierCubicCurveTo(self, p2: ImVec2, p3: ImVec2, p4: ImVec2, num_segments: int = 0) -> None:
        ...
    def PathBezierQuadraticCurveTo(self, p2: ImVec2, p3: ImVec2, num_segments: int = 0) -> None:
        ...
    def PathClear(self) -> None:
        ...
    def PathEllipticalArcTo(self, center: ImVec2, radius: ImVec2, rot: float, a_min: float, a_max: float, num_segments: int = 0) -> None:
        ...
    def PathFillConcave(self, col: int) -> None:
        ...
    def PathFillConvex(self, col: int) -> None:
        ...
    def PathLineTo(self, pos: ImVec2) -> None:
        ...
    def PathLineToMergeDuplicate(self, pos: ImVec2) -> None:
        ...
    def PathRect(self, rect_min: ImVec2, rect_max: ImVec2, rounding: float = 0.0, flags: int = 0) -> None:
        ...
    def PathStroke(self, col: int, flags: int = 0, thickness: float = 1.0) -> None:
        ...
    def PopClipRect(self) -> None:
        ...
    def PopTextureID(self) -> None:
        ...
    def PrimQuadUV(self, a: ImVec2, b: ImVec2, c: ImVec2, d: ImVec2, uv_a: ImVec2, uv_b: ImVec2, uv_c: ImVec2, uv_d: ImVec2, col: int) -> None:
        ...
    def PrimRect(self, a: ImVec2, b: ImVec2, col: int) -> None:
        ...
    def PrimRectUV(self, a: ImVec2, b: ImVec2, uv_a: ImVec2, uv_b: ImVec2, col: int) -> None:
        ...
    def PrimReserve(self, idx_count: int, vtx_count: int) -> None:
        ...
    def PrimUnreserve(self, idx_count: int, vtx_count: int) -> None:
        ...
    def PrimVtx(self, pos: ImVec2, uv: ImVec2, col: int) -> None:
        ...
    def PrimWriteIdx(self, idx: int) -> None:
        ...
    def PrimWriteVtx(self, pos: ImVec2, uv: ImVec2, col: int) -> None:
        ...
    def PushClipRect(self, clip_rect_min: ImVec2, clip_rect_max: ImVec2, intersect_with_current_clip_rect: bool = False) -> None:
        ...
    def PushClipRectFullScreen(self) -> None:
        ...
    def PushTextureID(self, texture_id: capsule) -> None:
        ...
    def _CalcCircleAutoSegmentCount(self, radius: float) -> int:
        ...
    def _ClearFreeMemory(self) -> None:
        ...
    def _OnChangedClipRect(self) -> None:
        ...
    def _OnChangedTextureID(self) -> None:
        ...
    def _OnChangedVtxOffset(self) -> None:
        ...
    def _PathArcToFastEx(self, center: ImVec2, radius: float, a_min_sample: int, a_max_sample: int, a_step: int) -> None:
        ...
    def _PathArcToN(self, center: ImVec2, radius: float, a_min: float, a_max: float, num_segments: int) -> None:
        ...
    def _PopUnusedDrawCmd(self) -> None:
        ...
    def _ResetForNewFrame(self) -> None:
        ...
    def _TryMergeDrawCmds(self) -> None:
        ...
    def __init__(self, shared_data: ImDrawListSharedData) -> None:
        ...
class ImDrawListFlags_:
    """
    Members:
    
      ImDrawListFlags_None
    
      ImDrawListFlags_AntiAliasedLines
    
      ImDrawListFlags_AntiAliasedLinesUseTex
    
      ImDrawListFlags_AntiAliasedFill
    
      ImDrawListFlags_AllowVtxOffset
    """
    ImDrawListFlags_AllowVtxOffset: typing.ClassVar[ImDrawListFlags_]  # value = <ImDrawListFlags_.ImDrawListFlags_AllowVtxOffset: 8>
    ImDrawListFlags_AntiAliasedFill: typing.ClassVar[ImDrawListFlags_]  # value = <ImDrawListFlags_.ImDrawListFlags_AntiAliasedFill: 4>
    ImDrawListFlags_AntiAliasedLines: typing.ClassVar[ImDrawListFlags_]  # value = <ImDrawListFlags_.ImDrawListFlags_AntiAliasedLines: 1>
    ImDrawListFlags_AntiAliasedLinesUseTex: typing.ClassVar[ImDrawListFlags_]  # value = <ImDrawListFlags_.ImDrawListFlags_AntiAliasedLinesUseTex: 2>
    ImDrawListFlags_None: typing.ClassVar[ImDrawListFlags_]  # value = <ImDrawListFlags_.ImDrawListFlags_None: 0>
    __members__: typing.ClassVar[dict[str, ImDrawListFlags_]]  # value = {'ImDrawListFlags_None': <ImDrawListFlags_.ImDrawListFlags_None: 0>, 'ImDrawListFlags_AntiAliasedLines': <ImDrawListFlags_.ImDrawListFlags_AntiAliasedLines: 1>, 'ImDrawListFlags_AntiAliasedLinesUseTex': <ImDrawListFlags_.ImDrawListFlags_AntiAliasedLinesUseTex: 2>, 'ImDrawListFlags_AntiAliasedFill': <ImDrawListFlags_.ImDrawListFlags_AntiAliasedFill: 4>, 'ImDrawListFlags_AllowVtxOffset': <ImDrawListFlags_.ImDrawListFlags_AllowVtxOffset: 8>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImDrawListSharedData:
    ArcFastRadiusCutoff: float
    CircleSegmentMaxError: float
    ClipRectFullscreen: ImVec4
    CurveTessellationTol: float
    Font: ImFont
    FontSize: float
    InitialFlags: int
    TempBuffer: ImVector_ImVec2
    TexUvLines: ImVec4
    TexUvWhitePixel: ImVec2
    def SetCircleTessellationMaxError(self, max_error: float) -> None:
        ...
    def __init__(self) -> None:
        ...
    @property
    def ArcFastVtx(self) -> Arr_ImVec2:
        ...
    @property
    def CircleSegmentCounts(self) -> Arr_unsigned_char:
        ...
class ImDrawListSplitter:
    _Channels: ImVector_ImDrawChannel
    _Count: int
    _Current: int
    def Clear(self) -> None:
        ...
    def ClearFreeMemory(self) -> None:
        ...
    def Merge(self, draw_list: ImDrawList) -> None:
        ...
    def SetCurrentChannel(self, draw_list: ImDrawList, channel_idx: int) -> None:
        ...
    def Split(self, draw_list: ImDrawList, count: int) -> None:
        ...
    def __init__(self) -> None:
        ...
class ImDrawVert:
    col: int
    pos: ImVec2
    uv: ImVec2
class ImFont:
    Ascent: float
    ConfigData: ImFontConfig
    ConfigDataCount: int
    ContainerAtlas: ImFontAtlas
    Descent: float
    DirtyLookupTables: bool
    EllipsisChar: int
    EllipsisCharCount: int
    EllipsisCharStep: float
    EllipsisWidth: float
    FallbackAdvanceX: float
    FallbackChar: int
    FallbackGlyph: ImFontGlyph
    FontSize: float
    Glyphs: ImVector_ImFontGlyph
    IndexAdvanceX: ImVector_float
    IndexLookup: ImVector_ImWchar
    MetricsTotalSurface: int
    Scale: float
    def AddGlyph(self, src_cfg: ImFontConfig, c: int, x0: float, y0: float, x1: float, y1: float, u0: float, v0: float, u1: float, v1: float, advance_x: float) -> None:
        ...
    def AddRemapChar(self, dst: int, src: int, overwrite_dst: bool = True) -> None:
        ...
    def BuildLookupTable(self) -> None:
        ...
    def CalcWordWrapPositionA(self, scale: float, text: str, text_end: str, wrap_width: float) -> str:
        ...
    def ClearOutputData(self) -> None:
        ...
    def FindGlyph(self, c: int) -> ImFontGlyph:
        ...
    def FindGlyphNoFallback(self, c: int) -> ImFontGlyph:
        ...
    def GetCharAdvance(self, c: int) -> float:
        ...
    def GetDebugName(self) -> str:
        ...
    def GrowIndex(self, new_size: int) -> None:
        ...
    def IsGlyphRangeUnused(self, c_begin: int, c_last: int) -> bool:
        ...
    def IsLoaded(self) -> bool:
        ...
    def RenderChar(self, draw_list: ImDrawList, size: float, pos: ImVec2, col: int, c: int) -> None:
        ...
    def RenderText(self, draw_list: ImDrawList, size: float, pos: ImVec2, col: int, clip_rect: ImVec4, text_begin: str, text_end: str, wrap_width: float = 0.0, cpu_fine_clip: bool = False) -> None:
        ...
    def SetGlyphVisible(self, c: int, visible: bool) -> None:
        ...
    def __init__(self) -> None:
        ...
    @property
    def Used4kPagesMap(self) -> Arr_unsigned_char:
        ...
class ImFontAtlas:
    ConfigData: ImVector_ImFontConfig
    CustomRects: ImVector_ImFontAtlasCustomRect
    Flags: int
    FontBuilderFlags: int
    FontBuilderIO: ImFontBuilderIO
    Fonts: ImVector_ImFontPtr
    Locked: bool
    PackIdLines: int
    PackIdMouseCursors: int
    TexDesiredWidth: int
    TexGlyphPadding: int
    TexHeight: int
    TexID: capsule
    TexPixelsAlpha8: int
    TexPixelsRGBA32: int
    TexPixelsUseColors: bool
    TexReady: bool
    TexUvScale: ImVec2
    TexUvWhitePixel: ImVec2
    TexWidth: int
    UserData: capsule
    def AddCustomRectFontGlyph(self, font: ImFont, id: int, width: int, height: int, advance_x: float, offset: ImVec2 = ...) -> int:
        ...
    def AddCustomRectRegular(self, width: int, height: int) -> int:
        ...
    def AddFont(self, font_cfg: ImFontConfig) -> ImFont:
        ...
    def AddFontDefault(self, font_cfg: ImFontConfig | None = None) -> ImFont:
        ...
    def AddFontFromFileTTF(self, filename: str, size_pixels: float, font_cfg: ImFontConfig | None = None, glyph_ranges: GlyphRanges | None = None) -> ImFont:
        ...
    def AddFontFromMemoryCompressedBase85TTF(self, compressed_font_data_base85: str, size_pixels: float, font_cfg: ImFontConfig | None = None, glyph_ranges: GlyphRanges | None = None) -> ImFont:
        ...
    def AddFontFromMemoryCompressedTTF(self, compressed_font_data: capsule, compressed_font_data_size: int, size_pixels: float, font_cfg: ImFontConfig | None = None, glyph_ranges: GlyphRanges | None = None) -> ImFont:
        ...
    def AddFontFromMemoryTTF(self, font_data: capsule, font_data_size: int, size_pixels: float, font_cfg: ImFontConfig | None = None, glyph_ranges: GlyphRanges | None = None) -> ImFont:
        ...
    def Build(self) -> bool:
        ...
    def CalcCustomRectUV(self, rect: ImFontAtlasCustomRect, out_uv_min: ImVec2, out_uv_max: ImVec2) -> None:
        ...
    def Clear(self) -> None:
        ...
    def ClearFonts(self) -> None:
        ...
    def ClearInputData(self) -> None:
        ...
    def ClearTexData(self) -> None:
        ...
    def GetCustomRectByIndex(self, index: int) -> ImFontAtlasCustomRect:
        ...
    def GetGlyphRangesChineseFull(self) -> GlyphRanges:
        ...
    def GetGlyphRangesChineseSimplifiedCommon(self) -> GlyphRanges:
        ...
    def GetGlyphRangesCyrillic(self) -> GlyphRanges:
        ...
    def GetGlyphRangesDefault(self) -> GlyphRanges:
        ...
    def GetGlyphRangesGreek(self) -> GlyphRanges:
        ...
    def GetGlyphRangesJapanese(self) -> GlyphRanges:
        ...
    def GetGlyphRangesKorean(self) -> GlyphRanges:
        ...
    def GetGlyphRangesThai(self) -> GlyphRanges:
        ...
    def GetGlyphRangesVietnamese(self) -> GlyphRanges:
        ...
    def GetMouseCursorTexData(self, cursor: int, out_offset: ImVec2, out_size: ImVec2, out_uv_border: ImVec2, out_uv_fill: ImVec2) -> bool:
        ...
    def IsBuilt(self) -> bool:
        ...
    def SetTexID(self, id: capsule) -> None:
        ...
    def __init__(self) -> None:
        ...
    @property
    def TexUvLines(self) -> Arr_ImVec4:
        ...
class ImFontAtlasCustomRect:
    Font: ImFont
    GlyphAdvanceX: float
    GlyphID: int
    GlyphOffset: ImVec2
    Height: int
    Width: int
    X: int
    Y: int
    def IsPacked(self) -> bool:
        ...
    def __init__(self) -> None:
        ...
class ImFontAtlasFlags_:
    """
    Members:
    
      ImFontAtlasFlags_None
    
      ImFontAtlasFlags_NoPowerOfTwoHeight
    
      ImFontAtlasFlags_NoMouseCursors
    
      ImFontAtlasFlags_NoBakedLines
    """
    ImFontAtlasFlags_NoBakedLines: typing.ClassVar[ImFontAtlasFlags_]  # value = <ImFontAtlasFlags_.ImFontAtlasFlags_NoBakedLines: 4>
    ImFontAtlasFlags_NoMouseCursors: typing.ClassVar[ImFontAtlasFlags_]  # value = <ImFontAtlasFlags_.ImFontAtlasFlags_NoMouseCursors: 2>
    ImFontAtlasFlags_NoPowerOfTwoHeight: typing.ClassVar[ImFontAtlasFlags_]  # value = <ImFontAtlasFlags_.ImFontAtlasFlags_NoPowerOfTwoHeight: 1>
    ImFontAtlasFlags_None: typing.ClassVar[ImFontAtlasFlags_]  # value = <ImFontAtlasFlags_.ImFontAtlasFlags_None: 0>
    __members__: typing.ClassVar[dict[str, ImFontAtlasFlags_]]  # value = {'ImFontAtlasFlags_None': <ImFontAtlasFlags_.ImFontAtlasFlags_None: 0>, 'ImFontAtlasFlags_NoPowerOfTwoHeight': <ImFontAtlasFlags_.ImFontAtlasFlags_NoPowerOfTwoHeight: 1>, 'ImFontAtlasFlags_NoMouseCursors': <ImFontAtlasFlags_.ImFontAtlasFlags_NoMouseCursors: 2>, 'ImFontAtlasFlags_NoBakedLines': <ImFontAtlasFlags_.ImFontAtlasFlags_NoBakedLines: 4>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImFontBuilderIO:
    pass
class ImFontConfig:
    DstFont: ImFont
    EllipsisChar: int
    FontBuilderFlags: int
    FontData: capsule
    FontDataOwnedByAtlas: bool
    FontDataSize: int
    FontNo: int
    GlyphExtraSpacing: ImVec2
    GlyphMaxAdvanceX: float
    GlyphMinAdvanceX: float
    GlyphOffset: ImVec2
    GlyphRanges: int
    MergeMode: bool
    OversampleH: int
    OversampleV: int
    PixelSnapH: bool
    RasterizerDensity: float
    RasterizerMultiply: float
    SizePixels: float
    def __init__(self) -> None:
        ...
    @property
    def Name(self) -> Arr_char:
        ...
class ImFontGlyph:
    AdvanceX: float
    Codepoint: int
    Colored: int
    U0: float
    U1: float
    V0: float
    V1: float
    Visible: int
    X0: float
    X1: float
    Y0: float
    Y1: float
class ImFontGlyphRangesBuilder:
    UsedChars: ImVector_ImU32
    def AddChar(self, c: int) -> None:
        ...
    def AddRanges(self, ranges: int) -> None:
        ...
    def AddText(self, text: str, text_end: str = 0) -> None:
        ...
    def BuildRanges(self, out_ranges: ImVector_ImWchar) -> None:
        ...
    def Clear(self) -> None:
        ...
    def GetBit(self, n: int) -> bool:
        ...
    def SetBit(self, n: int) -> None:
        ...
    def __init__(self) -> None:
        ...
class ImGuiActivateFlags_:
    """
    Members:
    
      ImGuiActivateFlags_None
    
      ImGuiActivateFlags_PreferInput
    
      ImGuiActivateFlags_PreferTweak
    
      ImGuiActivateFlags_TryToPreserveState
    
      ImGuiActivateFlags_FromTabbing
    
      ImGuiActivateFlags_FromShortcut
    """
    ImGuiActivateFlags_FromShortcut: typing.ClassVar[ImGuiActivateFlags_]  # value = <ImGuiActivateFlags_.ImGuiActivateFlags_FromShortcut: 16>
    ImGuiActivateFlags_FromTabbing: typing.ClassVar[ImGuiActivateFlags_]  # value = <ImGuiActivateFlags_.ImGuiActivateFlags_FromTabbing: 8>
    ImGuiActivateFlags_None: typing.ClassVar[ImGuiActivateFlags_]  # value = <ImGuiActivateFlags_.ImGuiActivateFlags_None: 0>
    ImGuiActivateFlags_PreferInput: typing.ClassVar[ImGuiActivateFlags_]  # value = <ImGuiActivateFlags_.ImGuiActivateFlags_PreferInput: 1>
    ImGuiActivateFlags_PreferTweak: typing.ClassVar[ImGuiActivateFlags_]  # value = <ImGuiActivateFlags_.ImGuiActivateFlags_PreferTweak: 2>
    ImGuiActivateFlags_TryToPreserveState: typing.ClassVar[ImGuiActivateFlags_]  # value = <ImGuiActivateFlags_.ImGuiActivateFlags_TryToPreserveState: 4>
    __members__: typing.ClassVar[dict[str, ImGuiActivateFlags_]]  # value = {'ImGuiActivateFlags_None': <ImGuiActivateFlags_.ImGuiActivateFlags_None: 0>, 'ImGuiActivateFlags_PreferInput': <ImGuiActivateFlags_.ImGuiActivateFlags_PreferInput: 1>, 'ImGuiActivateFlags_PreferTweak': <ImGuiActivateFlags_.ImGuiActivateFlags_PreferTweak: 2>, 'ImGuiActivateFlags_TryToPreserveState': <ImGuiActivateFlags_.ImGuiActivateFlags_TryToPreserveState: 4>, 'ImGuiActivateFlags_FromTabbing': <ImGuiActivateFlags_.ImGuiActivateFlags_FromTabbing: 8>, 'ImGuiActivateFlags_FromShortcut': <ImGuiActivateFlags_.ImGuiActivateFlags_FromShortcut: 16>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiAxis:
    """
    Members:
    
      ImGuiAxis_None
    
      ImGuiAxis_X
    
      ImGuiAxis_Y
    """
    ImGuiAxis_None: typing.ClassVar[ImGuiAxis]  # value = <ImGuiAxis.ImGuiAxis_None: -1>
    ImGuiAxis_X: typing.ClassVar[ImGuiAxis]  # value = <ImGuiAxis.ImGuiAxis_X: 0>
    ImGuiAxis_Y: typing.ClassVar[ImGuiAxis]  # value = <ImGuiAxis.ImGuiAxis_Y: 1>
    __members__: typing.ClassVar[dict[str, ImGuiAxis]]  # value = {'ImGuiAxis_None': <ImGuiAxis.ImGuiAxis_None: -1>, 'ImGuiAxis_X': <ImGuiAxis.ImGuiAxis_X: 0>, 'ImGuiAxis_Y': <ImGuiAxis.ImGuiAxis_Y: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiBackendFlags_:
    """
    Members:
    
      ImGuiBackendFlags_None
    
      ImGuiBackendFlags_HasGamepad
    
      ImGuiBackendFlags_HasMouseCursors
    
      ImGuiBackendFlags_HasSetMousePos
    
      ImGuiBackendFlags_RendererHasVtxOffset
    
      ImGuiBackendFlags_PlatformHasViewports
    
      ImGuiBackendFlags_HasMouseHoveredViewport
    
      ImGuiBackendFlags_RendererHasViewports
    """
    ImGuiBackendFlags_HasGamepad: typing.ClassVar[ImGuiBackendFlags_]  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_HasGamepad: 1>
    ImGuiBackendFlags_HasMouseCursors: typing.ClassVar[ImGuiBackendFlags_]  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_HasMouseCursors: 2>
    ImGuiBackendFlags_HasMouseHoveredViewport: typing.ClassVar[ImGuiBackendFlags_]  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_HasMouseHoveredViewport: 2048>
    ImGuiBackendFlags_HasSetMousePos: typing.ClassVar[ImGuiBackendFlags_]  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_HasSetMousePos: 4>
    ImGuiBackendFlags_None: typing.ClassVar[ImGuiBackendFlags_]  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_None: 0>
    ImGuiBackendFlags_PlatformHasViewports: typing.ClassVar[ImGuiBackendFlags_]  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_PlatformHasViewports: 1024>
    ImGuiBackendFlags_RendererHasViewports: typing.ClassVar[ImGuiBackendFlags_]  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_RendererHasViewports: 4096>
    ImGuiBackendFlags_RendererHasVtxOffset: typing.ClassVar[ImGuiBackendFlags_]  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_RendererHasVtxOffset: 8>
    __members__: typing.ClassVar[dict[str, ImGuiBackendFlags_]]  # value = {'ImGuiBackendFlags_None': <ImGuiBackendFlags_.ImGuiBackendFlags_None: 0>, 'ImGuiBackendFlags_HasGamepad': <ImGuiBackendFlags_.ImGuiBackendFlags_HasGamepad: 1>, 'ImGuiBackendFlags_HasMouseCursors': <ImGuiBackendFlags_.ImGuiBackendFlags_HasMouseCursors: 2>, 'ImGuiBackendFlags_HasSetMousePos': <ImGuiBackendFlags_.ImGuiBackendFlags_HasSetMousePos: 4>, 'ImGuiBackendFlags_RendererHasVtxOffset': <ImGuiBackendFlags_.ImGuiBackendFlags_RendererHasVtxOffset: 8>, 'ImGuiBackendFlags_PlatformHasViewports': <ImGuiBackendFlags_.ImGuiBackendFlags_PlatformHasViewports: 1024>, 'ImGuiBackendFlags_HasMouseHoveredViewport': <ImGuiBackendFlags_.ImGuiBackendFlags_HasMouseHoveredViewport: 2048>, 'ImGuiBackendFlags_RendererHasViewports': <ImGuiBackendFlags_.ImGuiBackendFlags_RendererHasViewports: 4096>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiButtonFlagsPrivate_:
    """
    Members:
    
      ImGuiButtonFlags_PressedOnClick
    
      ImGuiButtonFlags_PressedOnClickRelease
    
      ImGuiButtonFlags_PressedOnClickReleaseAnywhere
    
      ImGuiButtonFlags_PressedOnRelease
    
      ImGuiButtonFlags_PressedOnDoubleClick
    
      ImGuiButtonFlags_PressedOnDragDropHold
    
      ImGuiButtonFlags_Repeat
    
      ImGuiButtonFlags_FlattenChildren
    
      ImGuiButtonFlags_AllowOverlap
    
      ImGuiButtonFlags_DontClosePopups
    
      ImGuiButtonFlags_AlignTextBaseLine
    
      ImGuiButtonFlags_NoKeyModifiers
    
      ImGuiButtonFlags_NoHoldingActiveId
    
      ImGuiButtonFlags_NoNavFocus
    
      ImGuiButtonFlags_NoHoveredOnFocus
    
      ImGuiButtonFlags_NoSetKeyOwner
    
      ImGuiButtonFlags_NoTestKeyOwner
    
      ImGuiButtonFlags_PressedOnMask_
    
      ImGuiButtonFlags_PressedOnDefault_
    """
    ImGuiButtonFlags_AlignTextBaseLine: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_AlignTextBaseLine: 32768>
    ImGuiButtonFlags_AllowOverlap: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_AllowOverlap: 4096>
    ImGuiButtonFlags_DontClosePopups: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_DontClosePopups: 8192>
    ImGuiButtonFlags_FlattenChildren: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_FlattenChildren: 2048>
    ImGuiButtonFlags_NoHoldingActiveId: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoHoldingActiveId: 131072>
    ImGuiButtonFlags_NoHoveredOnFocus: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoHoveredOnFocus: 524288>
    ImGuiButtonFlags_NoKeyModifiers: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoKeyModifiers: 65536>
    ImGuiButtonFlags_NoNavFocus: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoNavFocus: 262144>
    ImGuiButtonFlags_NoSetKeyOwner: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoSetKeyOwner: 1048576>
    ImGuiButtonFlags_NoTestKeyOwner: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoTestKeyOwner: 2097152>
    ImGuiButtonFlags_PressedOnClick: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnClick: 16>
    ImGuiButtonFlags_PressedOnClickRelease: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnClickRelease: 32>
    ImGuiButtonFlags_PressedOnClickReleaseAnywhere: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnClickReleaseAnywhere: 64>
    ImGuiButtonFlags_PressedOnDefault_: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnClickRelease: 32>
    ImGuiButtonFlags_PressedOnDoubleClick: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnDoubleClick: 256>
    ImGuiButtonFlags_PressedOnDragDropHold: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnDragDropHold: 512>
    ImGuiButtonFlags_PressedOnMask_: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnMask_: 1008>
    ImGuiButtonFlags_PressedOnRelease: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnRelease: 128>
    ImGuiButtonFlags_Repeat: typing.ClassVar[ImGuiButtonFlagsPrivate_]  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_Repeat: 1024>
    __members__: typing.ClassVar[dict[str, ImGuiButtonFlagsPrivate_]]  # value = {'ImGuiButtonFlags_PressedOnClick': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnClick: 16>, 'ImGuiButtonFlags_PressedOnClickRelease': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnClickRelease: 32>, 'ImGuiButtonFlags_PressedOnClickReleaseAnywhere': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnClickReleaseAnywhere: 64>, 'ImGuiButtonFlags_PressedOnRelease': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnRelease: 128>, 'ImGuiButtonFlags_PressedOnDoubleClick': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnDoubleClick: 256>, 'ImGuiButtonFlags_PressedOnDragDropHold': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnDragDropHold: 512>, 'ImGuiButtonFlags_Repeat': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_Repeat: 1024>, 'ImGuiButtonFlags_FlattenChildren': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_FlattenChildren: 2048>, 'ImGuiButtonFlags_AllowOverlap': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_AllowOverlap: 4096>, 'ImGuiButtonFlags_DontClosePopups': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_DontClosePopups: 8192>, 'ImGuiButtonFlags_AlignTextBaseLine': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_AlignTextBaseLine: 32768>, 'ImGuiButtonFlags_NoKeyModifiers': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoKeyModifiers: 65536>, 'ImGuiButtonFlags_NoHoldingActiveId': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoHoldingActiveId: 131072>, 'ImGuiButtonFlags_NoNavFocus': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoNavFocus: 262144>, 'ImGuiButtonFlags_NoHoveredOnFocus': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoHoveredOnFocus: 524288>, 'ImGuiButtonFlags_NoSetKeyOwner': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoSetKeyOwner: 1048576>, 'ImGuiButtonFlags_NoTestKeyOwner': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoTestKeyOwner: 2097152>, 'ImGuiButtonFlags_PressedOnMask_': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnMask_: 1008>, 'ImGuiButtonFlags_PressedOnDefault_': <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnClickRelease: 32>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiButtonFlags_:
    """
    Members:
    
      ImGuiButtonFlags_None
    
      ImGuiButtonFlags_MouseButtonLeft
    
      ImGuiButtonFlags_MouseButtonRight
    
      ImGuiButtonFlags_MouseButtonMiddle
    
      ImGuiButtonFlags_MouseButtonMask_
    """
    ImGuiButtonFlags_MouseButtonLeft: typing.ClassVar[ImGuiButtonFlags_]  # value = <ImGuiButtonFlags_.ImGuiButtonFlags_MouseButtonLeft: 1>
    ImGuiButtonFlags_MouseButtonMask_: typing.ClassVar[ImGuiButtonFlags_]  # value = <ImGuiButtonFlags_.ImGuiButtonFlags_MouseButtonMask_: 7>
    ImGuiButtonFlags_MouseButtonMiddle: typing.ClassVar[ImGuiButtonFlags_]  # value = <ImGuiButtonFlags_.ImGuiButtonFlags_MouseButtonMiddle: 4>
    ImGuiButtonFlags_MouseButtonRight: typing.ClassVar[ImGuiButtonFlags_]  # value = <ImGuiButtonFlags_.ImGuiButtonFlags_MouseButtonRight: 2>
    ImGuiButtonFlags_None: typing.ClassVar[ImGuiButtonFlags_]  # value = <ImGuiButtonFlags_.ImGuiButtonFlags_None: 0>
    __members__: typing.ClassVar[dict[str, ImGuiButtonFlags_]]  # value = {'ImGuiButtonFlags_None': <ImGuiButtonFlags_.ImGuiButtonFlags_None: 0>, 'ImGuiButtonFlags_MouseButtonLeft': <ImGuiButtonFlags_.ImGuiButtonFlags_MouseButtonLeft: 1>, 'ImGuiButtonFlags_MouseButtonRight': <ImGuiButtonFlags_.ImGuiButtonFlags_MouseButtonRight: 2>, 'ImGuiButtonFlags_MouseButtonMiddle': <ImGuiButtonFlags_.ImGuiButtonFlags_MouseButtonMiddle: 4>, 'ImGuiButtonFlags_MouseButtonMask_': <ImGuiButtonFlags_.ImGuiButtonFlags_MouseButtonMask_: 7>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiChildFlags_:
    """
    Members:
    
      ImGuiChildFlags_None
    
      ImGuiChildFlags_Border
    
      ImGuiChildFlags_AlwaysUseWindowPadding
    
      ImGuiChildFlags_ResizeX
    
      ImGuiChildFlags_ResizeY
    
      ImGuiChildFlags_AutoResizeX
    
      ImGuiChildFlags_AutoResizeY
    
      ImGuiChildFlags_AlwaysAutoResize
    
      ImGuiChildFlags_FrameStyle
    
      ImGuiChildFlags_NavFlattened
    """
    ImGuiChildFlags_AlwaysAutoResize: typing.ClassVar[ImGuiChildFlags_]  # value = <ImGuiChildFlags_.ImGuiChildFlags_AlwaysAutoResize: 64>
    ImGuiChildFlags_AlwaysUseWindowPadding: typing.ClassVar[ImGuiChildFlags_]  # value = <ImGuiChildFlags_.ImGuiChildFlags_AlwaysUseWindowPadding: 2>
    ImGuiChildFlags_AutoResizeX: typing.ClassVar[ImGuiChildFlags_]  # value = <ImGuiChildFlags_.ImGuiChildFlags_AutoResizeX: 16>
    ImGuiChildFlags_AutoResizeY: typing.ClassVar[ImGuiChildFlags_]  # value = <ImGuiChildFlags_.ImGuiChildFlags_AutoResizeY: 32>
    ImGuiChildFlags_Border: typing.ClassVar[ImGuiChildFlags_]  # value = <ImGuiChildFlags_.ImGuiChildFlags_Border: 1>
    ImGuiChildFlags_FrameStyle: typing.ClassVar[ImGuiChildFlags_]  # value = <ImGuiChildFlags_.ImGuiChildFlags_FrameStyle: 128>
    ImGuiChildFlags_NavFlattened: typing.ClassVar[ImGuiChildFlags_]  # value = <ImGuiChildFlags_.ImGuiChildFlags_NavFlattened: 256>
    ImGuiChildFlags_None: typing.ClassVar[ImGuiChildFlags_]  # value = <ImGuiChildFlags_.ImGuiChildFlags_None: 0>
    ImGuiChildFlags_ResizeX: typing.ClassVar[ImGuiChildFlags_]  # value = <ImGuiChildFlags_.ImGuiChildFlags_ResizeX: 4>
    ImGuiChildFlags_ResizeY: typing.ClassVar[ImGuiChildFlags_]  # value = <ImGuiChildFlags_.ImGuiChildFlags_ResizeY: 8>
    __members__: typing.ClassVar[dict[str, ImGuiChildFlags_]]  # value = {'ImGuiChildFlags_None': <ImGuiChildFlags_.ImGuiChildFlags_None: 0>, 'ImGuiChildFlags_Border': <ImGuiChildFlags_.ImGuiChildFlags_Border: 1>, 'ImGuiChildFlags_AlwaysUseWindowPadding': <ImGuiChildFlags_.ImGuiChildFlags_AlwaysUseWindowPadding: 2>, 'ImGuiChildFlags_ResizeX': <ImGuiChildFlags_.ImGuiChildFlags_ResizeX: 4>, 'ImGuiChildFlags_ResizeY': <ImGuiChildFlags_.ImGuiChildFlags_ResizeY: 8>, 'ImGuiChildFlags_AutoResizeX': <ImGuiChildFlags_.ImGuiChildFlags_AutoResizeX: 16>, 'ImGuiChildFlags_AutoResizeY': <ImGuiChildFlags_.ImGuiChildFlags_AutoResizeY: 32>, 'ImGuiChildFlags_AlwaysAutoResize': <ImGuiChildFlags_.ImGuiChildFlags_AlwaysAutoResize: 64>, 'ImGuiChildFlags_FrameStyle': <ImGuiChildFlags_.ImGuiChildFlags_FrameStyle: 128>, 'ImGuiChildFlags_NavFlattened': <ImGuiChildFlags_.ImGuiChildFlags_NavFlattened: 256>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiCol_:
    """
    Members:
    
      ImGuiCol_Text
    
      ImGuiCol_TextDisabled
    
      ImGuiCol_WindowBg
    
      ImGuiCol_ChildBg
    
      ImGuiCol_PopupBg
    
      ImGuiCol_Border
    
      ImGuiCol_BorderShadow
    
      ImGuiCol_FrameBg
    
      ImGuiCol_FrameBgHovered
    
      ImGuiCol_FrameBgActive
    
      ImGuiCol_TitleBg
    
      ImGuiCol_TitleBgActive
    
      ImGuiCol_TitleBgCollapsed
    
      ImGuiCol_MenuBarBg
    
      ImGuiCol_ScrollbarBg
    
      ImGuiCol_ScrollbarGrab
    
      ImGuiCol_ScrollbarGrabHovered
    
      ImGuiCol_ScrollbarGrabActive
    
      ImGuiCol_CheckMark
    
      ImGuiCol_SliderGrab
    
      ImGuiCol_SliderGrabActive
    
      ImGuiCol_Button
    
      ImGuiCol_ButtonHovered
    
      ImGuiCol_ButtonActive
    
      ImGuiCol_Header
    
      ImGuiCol_HeaderHovered
    
      ImGuiCol_HeaderActive
    
      ImGuiCol_Separator
    
      ImGuiCol_SeparatorHovered
    
      ImGuiCol_SeparatorActive
    
      ImGuiCol_ResizeGrip
    
      ImGuiCol_ResizeGripHovered
    
      ImGuiCol_ResizeGripActive
    
      ImGuiCol_TabHovered
    
      ImGuiCol_Tab
    
      ImGuiCol_TabSelected
    
      ImGuiCol_TabSelectedOverline
    
      ImGuiCol_TabDimmed
    
      ImGuiCol_TabDimmedSelected
    
      ImGuiCol_TabDimmedSelectedOverline
    
      ImGuiCol_DockingPreview
    
      ImGuiCol_DockingEmptyBg
    
      ImGuiCol_PlotLines
    
      ImGuiCol_PlotLinesHovered
    
      ImGuiCol_PlotHistogram
    
      ImGuiCol_PlotHistogramHovered
    
      ImGuiCol_TableHeaderBg
    
      ImGuiCol_TableBorderStrong
    
      ImGuiCol_TableBorderLight
    
      ImGuiCol_TableRowBg
    
      ImGuiCol_TableRowBgAlt
    
      ImGuiCol_TextSelectedBg
    
      ImGuiCol_DragDropTarget
    
      ImGuiCol_NavHighlight
    
      ImGuiCol_NavWindowingHighlight
    
      ImGuiCol_NavWindowingDimBg
    
      ImGuiCol_ModalWindowDimBg
    
      ImGuiCol_COUNT
    """
    ImGuiCol_Border: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_Border: 5>
    ImGuiCol_BorderShadow: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_BorderShadow: 6>
    ImGuiCol_Button: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_Button: 21>
    ImGuiCol_ButtonActive: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_ButtonActive: 23>
    ImGuiCol_ButtonHovered: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_ButtonHovered: 22>
    ImGuiCol_COUNT: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_COUNT: 57>
    ImGuiCol_CheckMark: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_CheckMark: 18>
    ImGuiCol_ChildBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_ChildBg: 3>
    ImGuiCol_DockingEmptyBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_DockingEmptyBg: 41>
    ImGuiCol_DockingPreview: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_DockingPreview: 40>
    ImGuiCol_DragDropTarget: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_DragDropTarget: 52>
    ImGuiCol_FrameBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_FrameBg: 7>
    ImGuiCol_FrameBgActive: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_FrameBgActive: 9>
    ImGuiCol_FrameBgHovered: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_FrameBgHovered: 8>
    ImGuiCol_Header: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_Header: 24>
    ImGuiCol_HeaderActive: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_HeaderActive: 26>
    ImGuiCol_HeaderHovered: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_HeaderHovered: 25>
    ImGuiCol_MenuBarBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_MenuBarBg: 13>
    ImGuiCol_ModalWindowDimBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_ModalWindowDimBg: 56>
    ImGuiCol_NavHighlight: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_NavHighlight: 53>
    ImGuiCol_NavWindowingDimBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_NavWindowingDimBg: 55>
    ImGuiCol_NavWindowingHighlight: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_NavWindowingHighlight: 54>
    ImGuiCol_PlotHistogram: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_PlotHistogram: 44>
    ImGuiCol_PlotHistogramHovered: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_PlotHistogramHovered: 45>
    ImGuiCol_PlotLines: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_PlotLines: 42>
    ImGuiCol_PlotLinesHovered: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_PlotLinesHovered: 43>
    ImGuiCol_PopupBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_PopupBg: 4>
    ImGuiCol_ResizeGrip: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_ResizeGrip: 30>
    ImGuiCol_ResizeGripActive: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_ResizeGripActive: 32>
    ImGuiCol_ResizeGripHovered: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_ResizeGripHovered: 31>
    ImGuiCol_ScrollbarBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_ScrollbarBg: 14>
    ImGuiCol_ScrollbarGrab: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_ScrollbarGrab: 15>
    ImGuiCol_ScrollbarGrabActive: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_ScrollbarGrabActive: 17>
    ImGuiCol_ScrollbarGrabHovered: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_ScrollbarGrabHovered: 16>
    ImGuiCol_Separator: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_Separator: 27>
    ImGuiCol_SeparatorActive: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_SeparatorActive: 29>
    ImGuiCol_SeparatorHovered: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_SeparatorHovered: 28>
    ImGuiCol_SliderGrab: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_SliderGrab: 19>
    ImGuiCol_SliderGrabActive: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_SliderGrabActive: 20>
    ImGuiCol_Tab: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_Tab: 34>
    ImGuiCol_TabDimmed: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TabDimmed: 37>
    ImGuiCol_TabDimmedSelected: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TabDimmedSelected: 38>
    ImGuiCol_TabDimmedSelectedOverline: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TabDimmedSelectedOverline: 39>
    ImGuiCol_TabHovered: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TabHovered: 33>
    ImGuiCol_TabSelected: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TabSelected: 35>
    ImGuiCol_TabSelectedOverline: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TabSelectedOverline: 36>
    ImGuiCol_TableBorderLight: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TableBorderLight: 48>
    ImGuiCol_TableBorderStrong: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TableBorderStrong: 47>
    ImGuiCol_TableHeaderBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TableHeaderBg: 46>
    ImGuiCol_TableRowBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TableRowBg: 49>
    ImGuiCol_TableRowBgAlt: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TableRowBgAlt: 50>
    ImGuiCol_Text: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_Text: 0>
    ImGuiCol_TextDisabled: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TextDisabled: 1>
    ImGuiCol_TextSelectedBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TextSelectedBg: 51>
    ImGuiCol_TitleBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TitleBg: 10>
    ImGuiCol_TitleBgActive: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TitleBgActive: 11>
    ImGuiCol_TitleBgCollapsed: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_TitleBgCollapsed: 12>
    ImGuiCol_WindowBg: typing.ClassVar[ImGuiCol_]  # value = <ImGuiCol_.ImGuiCol_WindowBg: 2>
    __members__: typing.ClassVar[dict[str, ImGuiCol_]]  # value = {'ImGuiCol_Text': <ImGuiCol_.ImGuiCol_Text: 0>, 'ImGuiCol_TextDisabled': <ImGuiCol_.ImGuiCol_TextDisabled: 1>, 'ImGuiCol_WindowBg': <ImGuiCol_.ImGuiCol_WindowBg: 2>, 'ImGuiCol_ChildBg': <ImGuiCol_.ImGuiCol_ChildBg: 3>, 'ImGuiCol_PopupBg': <ImGuiCol_.ImGuiCol_PopupBg: 4>, 'ImGuiCol_Border': <ImGuiCol_.ImGuiCol_Border: 5>, 'ImGuiCol_BorderShadow': <ImGuiCol_.ImGuiCol_BorderShadow: 6>, 'ImGuiCol_FrameBg': <ImGuiCol_.ImGuiCol_FrameBg: 7>, 'ImGuiCol_FrameBgHovered': <ImGuiCol_.ImGuiCol_FrameBgHovered: 8>, 'ImGuiCol_FrameBgActive': <ImGuiCol_.ImGuiCol_FrameBgActive: 9>, 'ImGuiCol_TitleBg': <ImGuiCol_.ImGuiCol_TitleBg: 10>, 'ImGuiCol_TitleBgActive': <ImGuiCol_.ImGuiCol_TitleBgActive: 11>, 'ImGuiCol_TitleBgCollapsed': <ImGuiCol_.ImGuiCol_TitleBgCollapsed: 12>, 'ImGuiCol_MenuBarBg': <ImGuiCol_.ImGuiCol_MenuBarBg: 13>, 'ImGuiCol_ScrollbarBg': <ImGuiCol_.ImGuiCol_ScrollbarBg: 14>, 'ImGuiCol_ScrollbarGrab': <ImGuiCol_.ImGuiCol_ScrollbarGrab: 15>, 'ImGuiCol_ScrollbarGrabHovered': <ImGuiCol_.ImGuiCol_ScrollbarGrabHovered: 16>, 'ImGuiCol_ScrollbarGrabActive': <ImGuiCol_.ImGuiCol_ScrollbarGrabActive: 17>, 'ImGuiCol_CheckMark': <ImGuiCol_.ImGuiCol_CheckMark: 18>, 'ImGuiCol_SliderGrab': <ImGuiCol_.ImGuiCol_SliderGrab: 19>, 'ImGuiCol_SliderGrabActive': <ImGuiCol_.ImGuiCol_SliderGrabActive: 20>, 'ImGuiCol_Button': <ImGuiCol_.ImGuiCol_Button: 21>, 'ImGuiCol_ButtonHovered': <ImGuiCol_.ImGuiCol_ButtonHovered: 22>, 'ImGuiCol_ButtonActive': <ImGuiCol_.ImGuiCol_ButtonActive: 23>, 'ImGuiCol_Header': <ImGuiCol_.ImGuiCol_Header: 24>, 'ImGuiCol_HeaderHovered': <ImGuiCol_.ImGuiCol_HeaderHovered: 25>, 'ImGuiCol_HeaderActive': <ImGuiCol_.ImGuiCol_HeaderActive: 26>, 'ImGuiCol_Separator': <ImGuiCol_.ImGuiCol_Separator: 27>, 'ImGuiCol_SeparatorHovered': <ImGuiCol_.ImGuiCol_SeparatorHovered: 28>, 'ImGuiCol_SeparatorActive': <ImGuiCol_.ImGuiCol_SeparatorActive: 29>, 'ImGuiCol_ResizeGrip': <ImGuiCol_.ImGuiCol_ResizeGrip: 30>, 'ImGuiCol_ResizeGripHovered': <ImGuiCol_.ImGuiCol_ResizeGripHovered: 31>, 'ImGuiCol_ResizeGripActive': <ImGuiCol_.ImGuiCol_ResizeGripActive: 32>, 'ImGuiCol_TabHovered': <ImGuiCol_.ImGuiCol_TabHovered: 33>, 'ImGuiCol_Tab': <ImGuiCol_.ImGuiCol_Tab: 34>, 'ImGuiCol_TabSelected': <ImGuiCol_.ImGuiCol_TabSelected: 35>, 'ImGuiCol_TabSelectedOverline': <ImGuiCol_.ImGuiCol_TabSelectedOverline: 36>, 'ImGuiCol_TabDimmed': <ImGuiCol_.ImGuiCol_TabDimmed: 37>, 'ImGuiCol_TabDimmedSelected': <ImGuiCol_.ImGuiCol_TabDimmedSelected: 38>, 'ImGuiCol_TabDimmedSelectedOverline': <ImGuiCol_.ImGuiCol_TabDimmedSelectedOverline: 39>, 'ImGuiCol_DockingPreview': <ImGuiCol_.ImGuiCol_DockingPreview: 40>, 'ImGuiCol_DockingEmptyBg': <ImGuiCol_.ImGuiCol_DockingEmptyBg: 41>, 'ImGuiCol_PlotLines': <ImGuiCol_.ImGuiCol_PlotLines: 42>, 'ImGuiCol_PlotLinesHovered': <ImGuiCol_.ImGuiCol_PlotLinesHovered: 43>, 'ImGuiCol_PlotHistogram': <ImGuiCol_.ImGuiCol_PlotHistogram: 44>, 'ImGuiCol_PlotHistogramHovered': <ImGuiCol_.ImGuiCol_PlotHistogramHovered: 45>, 'ImGuiCol_TableHeaderBg': <ImGuiCol_.ImGuiCol_TableHeaderBg: 46>, 'ImGuiCol_TableBorderStrong': <ImGuiCol_.ImGuiCol_TableBorderStrong: 47>, 'ImGuiCol_TableBorderLight': <ImGuiCol_.ImGuiCol_TableBorderLight: 48>, 'ImGuiCol_TableRowBg': <ImGuiCol_.ImGuiCol_TableRowBg: 49>, 'ImGuiCol_TableRowBgAlt': <ImGuiCol_.ImGuiCol_TableRowBgAlt: 50>, 'ImGuiCol_TextSelectedBg': <ImGuiCol_.ImGuiCol_TextSelectedBg: 51>, 'ImGuiCol_DragDropTarget': <ImGuiCol_.ImGuiCol_DragDropTarget: 52>, 'ImGuiCol_NavHighlight': <ImGuiCol_.ImGuiCol_NavHighlight: 53>, 'ImGuiCol_NavWindowingHighlight': <ImGuiCol_.ImGuiCol_NavWindowingHighlight: 54>, 'ImGuiCol_NavWindowingDimBg': <ImGuiCol_.ImGuiCol_NavWindowingDimBg: 55>, 'ImGuiCol_ModalWindowDimBg': <ImGuiCol_.ImGuiCol_ModalWindowDimBg: 56>, 'ImGuiCol_COUNT': <ImGuiCol_.ImGuiCol_COUNT: 57>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiColorEditFlags_:
    """
    Members:
    
      ImGuiColorEditFlags_None
    
      ImGuiColorEditFlags_NoAlpha
    
      ImGuiColorEditFlags_NoPicker
    
      ImGuiColorEditFlags_NoOptions
    
      ImGuiColorEditFlags_NoSmallPreview
    
      ImGuiColorEditFlags_NoInputs
    
      ImGuiColorEditFlags_NoTooltip
    
      ImGuiColorEditFlags_NoLabel
    
      ImGuiColorEditFlags_NoSidePreview
    
      ImGuiColorEditFlags_NoDragDrop
    
      ImGuiColorEditFlags_NoBorder
    
      ImGuiColorEditFlags_AlphaBar
    
      ImGuiColorEditFlags_AlphaPreview
    
      ImGuiColorEditFlags_AlphaPreviewHalf
    
      ImGuiColorEditFlags_HDR
    
      ImGuiColorEditFlags_DisplayRGB
    
      ImGuiColorEditFlags_DisplayHSV
    
      ImGuiColorEditFlags_DisplayHex
    
      ImGuiColorEditFlags_Uint8
    
      ImGuiColorEditFlags_Float
    
      ImGuiColorEditFlags_PickerHueBar
    
      ImGuiColorEditFlags_PickerHueWheel
    
      ImGuiColorEditFlags_InputRGB
    
      ImGuiColorEditFlags_InputHSV
    
      ImGuiColorEditFlags_DefaultOptions_
    
      ImGuiColorEditFlags_DisplayMask_
    
      ImGuiColorEditFlags_DataTypeMask_
    
      ImGuiColorEditFlags_PickerMask_
    
      ImGuiColorEditFlags_InputMask_
    """
    ImGuiColorEditFlags_AlphaBar: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_AlphaBar: 65536>
    ImGuiColorEditFlags_AlphaPreview: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_AlphaPreview: 131072>
    ImGuiColorEditFlags_AlphaPreviewHalf: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_AlphaPreviewHalf: 262144>
    ImGuiColorEditFlags_DataTypeMask_: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_DataTypeMask_: 25165824>
    ImGuiColorEditFlags_DefaultOptions_: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_DefaultOptions_: 177209344>
    ImGuiColorEditFlags_DisplayHSV: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_DisplayHSV: 2097152>
    ImGuiColorEditFlags_DisplayHex: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_DisplayHex: 4194304>
    ImGuiColorEditFlags_DisplayMask_: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_DisplayMask_: 7340032>
    ImGuiColorEditFlags_DisplayRGB: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_DisplayRGB: 1048576>
    ImGuiColorEditFlags_Float: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_Float: 16777216>
    ImGuiColorEditFlags_HDR: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_HDR: 524288>
    ImGuiColorEditFlags_InputHSV: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_InputHSV: 268435456>
    ImGuiColorEditFlags_InputMask_: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_InputMask_: 402653184>
    ImGuiColorEditFlags_InputRGB: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_InputRGB: 134217728>
    ImGuiColorEditFlags_NoAlpha: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoAlpha: 2>
    ImGuiColorEditFlags_NoBorder: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoBorder: 1024>
    ImGuiColorEditFlags_NoDragDrop: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoDragDrop: 512>
    ImGuiColorEditFlags_NoInputs: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoInputs: 32>
    ImGuiColorEditFlags_NoLabel: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoLabel: 128>
    ImGuiColorEditFlags_NoOptions: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoOptions: 8>
    ImGuiColorEditFlags_NoPicker: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoPicker: 4>
    ImGuiColorEditFlags_NoSidePreview: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoSidePreview: 256>
    ImGuiColorEditFlags_NoSmallPreview: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoSmallPreview: 16>
    ImGuiColorEditFlags_NoTooltip: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoTooltip: 64>
    ImGuiColorEditFlags_None: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_None: 0>
    ImGuiColorEditFlags_PickerHueBar: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_PickerHueBar: 33554432>
    ImGuiColorEditFlags_PickerHueWheel: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_PickerHueWheel: 67108864>
    ImGuiColorEditFlags_PickerMask_: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_PickerMask_: 100663296>
    ImGuiColorEditFlags_Uint8: typing.ClassVar[ImGuiColorEditFlags_]  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_Uint8: 8388608>
    __members__: typing.ClassVar[dict[str, ImGuiColorEditFlags_]]  # value = {'ImGuiColorEditFlags_None': <ImGuiColorEditFlags_.ImGuiColorEditFlags_None: 0>, 'ImGuiColorEditFlags_NoAlpha': <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoAlpha: 2>, 'ImGuiColorEditFlags_NoPicker': <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoPicker: 4>, 'ImGuiColorEditFlags_NoOptions': <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoOptions: 8>, 'ImGuiColorEditFlags_NoSmallPreview': <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoSmallPreview: 16>, 'ImGuiColorEditFlags_NoInputs': <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoInputs: 32>, 'ImGuiColorEditFlags_NoTooltip': <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoTooltip: 64>, 'ImGuiColorEditFlags_NoLabel': <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoLabel: 128>, 'ImGuiColorEditFlags_NoSidePreview': <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoSidePreview: 256>, 'ImGuiColorEditFlags_NoDragDrop': <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoDragDrop: 512>, 'ImGuiColorEditFlags_NoBorder': <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoBorder: 1024>, 'ImGuiColorEditFlags_AlphaBar': <ImGuiColorEditFlags_.ImGuiColorEditFlags_AlphaBar: 65536>, 'ImGuiColorEditFlags_AlphaPreview': <ImGuiColorEditFlags_.ImGuiColorEditFlags_AlphaPreview: 131072>, 'ImGuiColorEditFlags_AlphaPreviewHalf': <ImGuiColorEditFlags_.ImGuiColorEditFlags_AlphaPreviewHalf: 262144>, 'ImGuiColorEditFlags_HDR': <ImGuiColorEditFlags_.ImGuiColorEditFlags_HDR: 524288>, 'ImGuiColorEditFlags_DisplayRGB': <ImGuiColorEditFlags_.ImGuiColorEditFlags_DisplayRGB: 1048576>, 'ImGuiColorEditFlags_DisplayHSV': <ImGuiColorEditFlags_.ImGuiColorEditFlags_DisplayHSV: 2097152>, 'ImGuiColorEditFlags_DisplayHex': <ImGuiColorEditFlags_.ImGuiColorEditFlags_DisplayHex: 4194304>, 'ImGuiColorEditFlags_Uint8': <ImGuiColorEditFlags_.ImGuiColorEditFlags_Uint8: 8388608>, 'ImGuiColorEditFlags_Float': <ImGuiColorEditFlags_.ImGuiColorEditFlags_Float: 16777216>, 'ImGuiColorEditFlags_PickerHueBar': <ImGuiColorEditFlags_.ImGuiColorEditFlags_PickerHueBar: 33554432>, 'ImGuiColorEditFlags_PickerHueWheel': <ImGuiColorEditFlags_.ImGuiColorEditFlags_PickerHueWheel: 67108864>, 'ImGuiColorEditFlags_InputRGB': <ImGuiColorEditFlags_.ImGuiColorEditFlags_InputRGB: 134217728>, 'ImGuiColorEditFlags_InputHSV': <ImGuiColorEditFlags_.ImGuiColorEditFlags_InputHSV: 268435456>, 'ImGuiColorEditFlags_DefaultOptions_': <ImGuiColorEditFlags_.ImGuiColorEditFlags_DefaultOptions_: 177209344>, 'ImGuiColorEditFlags_DisplayMask_': <ImGuiColorEditFlags_.ImGuiColorEditFlags_DisplayMask_: 7340032>, 'ImGuiColorEditFlags_DataTypeMask_': <ImGuiColorEditFlags_.ImGuiColorEditFlags_DataTypeMask_: 25165824>, 'ImGuiColorEditFlags_PickerMask_': <ImGuiColorEditFlags_.ImGuiColorEditFlags_PickerMask_: 100663296>, 'ImGuiColorEditFlags_InputMask_': <ImGuiColorEditFlags_.ImGuiColorEditFlags_InputMask_: 402653184>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiColorMod:
    BackupValue: ImVec4
    Col: int
class ImGuiComboFlagsPrivate_:
    """
    Members:
    
      ImGuiComboFlags_CustomPreview
    """
    ImGuiComboFlags_CustomPreview: typing.ClassVar[ImGuiComboFlagsPrivate_]  # value = <ImGuiComboFlagsPrivate_.ImGuiComboFlags_CustomPreview: 1048576>
    __members__: typing.ClassVar[dict[str, ImGuiComboFlagsPrivate_]]  # value = {'ImGuiComboFlags_CustomPreview': <ImGuiComboFlagsPrivate_.ImGuiComboFlags_CustomPreview: 1048576>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiComboFlags_:
    """
    Members:
    
      ImGuiComboFlags_None
    
      ImGuiComboFlags_PopupAlignLeft
    
      ImGuiComboFlags_HeightSmall
    
      ImGuiComboFlags_HeightRegular
    
      ImGuiComboFlags_HeightLarge
    
      ImGuiComboFlags_HeightLargest
    
      ImGuiComboFlags_NoArrowButton
    
      ImGuiComboFlags_NoPreview
    
      ImGuiComboFlags_WidthFitPreview
    
      ImGuiComboFlags_HeightMask_
    """
    ImGuiComboFlags_HeightLarge: typing.ClassVar[ImGuiComboFlags_]  # value = <ImGuiComboFlags_.ImGuiComboFlags_HeightLarge: 8>
    ImGuiComboFlags_HeightLargest: typing.ClassVar[ImGuiComboFlags_]  # value = <ImGuiComboFlags_.ImGuiComboFlags_HeightLargest: 16>
    ImGuiComboFlags_HeightMask_: typing.ClassVar[ImGuiComboFlags_]  # value = <ImGuiComboFlags_.ImGuiComboFlags_HeightMask_: 30>
    ImGuiComboFlags_HeightRegular: typing.ClassVar[ImGuiComboFlags_]  # value = <ImGuiComboFlags_.ImGuiComboFlags_HeightRegular: 4>
    ImGuiComboFlags_HeightSmall: typing.ClassVar[ImGuiComboFlags_]  # value = <ImGuiComboFlags_.ImGuiComboFlags_HeightSmall: 2>
    ImGuiComboFlags_NoArrowButton: typing.ClassVar[ImGuiComboFlags_]  # value = <ImGuiComboFlags_.ImGuiComboFlags_NoArrowButton: 32>
    ImGuiComboFlags_NoPreview: typing.ClassVar[ImGuiComboFlags_]  # value = <ImGuiComboFlags_.ImGuiComboFlags_NoPreview: 64>
    ImGuiComboFlags_None: typing.ClassVar[ImGuiComboFlags_]  # value = <ImGuiComboFlags_.ImGuiComboFlags_None: 0>
    ImGuiComboFlags_PopupAlignLeft: typing.ClassVar[ImGuiComboFlags_]  # value = <ImGuiComboFlags_.ImGuiComboFlags_PopupAlignLeft: 1>
    ImGuiComboFlags_WidthFitPreview: typing.ClassVar[ImGuiComboFlags_]  # value = <ImGuiComboFlags_.ImGuiComboFlags_WidthFitPreview: 128>
    __members__: typing.ClassVar[dict[str, ImGuiComboFlags_]]  # value = {'ImGuiComboFlags_None': <ImGuiComboFlags_.ImGuiComboFlags_None: 0>, 'ImGuiComboFlags_PopupAlignLeft': <ImGuiComboFlags_.ImGuiComboFlags_PopupAlignLeft: 1>, 'ImGuiComboFlags_HeightSmall': <ImGuiComboFlags_.ImGuiComboFlags_HeightSmall: 2>, 'ImGuiComboFlags_HeightRegular': <ImGuiComboFlags_.ImGuiComboFlags_HeightRegular: 4>, 'ImGuiComboFlags_HeightLarge': <ImGuiComboFlags_.ImGuiComboFlags_HeightLarge: 8>, 'ImGuiComboFlags_HeightLargest': <ImGuiComboFlags_.ImGuiComboFlags_HeightLargest: 16>, 'ImGuiComboFlags_NoArrowButton': <ImGuiComboFlags_.ImGuiComboFlags_NoArrowButton: 32>, 'ImGuiComboFlags_NoPreview': <ImGuiComboFlags_.ImGuiComboFlags_NoPreview: 64>, 'ImGuiComboFlags_WidthFitPreview': <ImGuiComboFlags_.ImGuiComboFlags_WidthFitPreview: 128>, 'ImGuiComboFlags_HeightMask_': <ImGuiComboFlags_.ImGuiComboFlags_HeightMask_: 30>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiComboPreviewData:
    BackupCursorMaxPos: ImVec2
    BackupCursorPos: ImVec2
    BackupCursorPosPrevLine: ImVec2
    BackupLayout: int
    BackupPrevLineTextBaseOffset: float
    PreviewRect: ImRect
    def __init__(self) -> None:
        ...
class ImGuiCond_:
    """
    Members:
    
      ImGuiCond_None
    
      ImGuiCond_Always
    
      ImGuiCond_Once
    
      ImGuiCond_FirstUseEver
    
      ImGuiCond_Appearing
    """
    ImGuiCond_Always: typing.ClassVar[ImGuiCond_]  # value = <ImGuiCond_.ImGuiCond_Always: 1>
    ImGuiCond_Appearing: typing.ClassVar[ImGuiCond_]  # value = <ImGuiCond_.ImGuiCond_Appearing: 8>
    ImGuiCond_FirstUseEver: typing.ClassVar[ImGuiCond_]  # value = <ImGuiCond_.ImGuiCond_FirstUseEver: 4>
    ImGuiCond_None: typing.ClassVar[ImGuiCond_]  # value = <ImGuiCond_.ImGuiCond_None: 0>
    ImGuiCond_Once: typing.ClassVar[ImGuiCond_]  # value = <ImGuiCond_.ImGuiCond_Once: 2>
    __members__: typing.ClassVar[dict[str, ImGuiCond_]]  # value = {'ImGuiCond_None': <ImGuiCond_.ImGuiCond_None: 0>, 'ImGuiCond_Always': <ImGuiCond_.ImGuiCond_Always: 1>, 'ImGuiCond_Once': <ImGuiCond_.ImGuiCond_Once: 2>, 'ImGuiCond_FirstUseEver': <ImGuiCond_.ImGuiCond_FirstUseEver: 4>, 'ImGuiCond_Appearing': <ImGuiCond_.ImGuiCond_Appearing: 8>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiConfigFlags_:
    """
    Members:
    
      ImGuiConfigFlags_None
    
      ImGuiConfigFlags_NavEnableKeyboard
    
      ImGuiConfigFlags_NavEnableGamepad
    
      ImGuiConfigFlags_NavEnableSetMousePos
    
      ImGuiConfigFlags_NavNoCaptureKeyboard
    
      ImGuiConfigFlags_NoMouse
    
      ImGuiConfigFlags_NoMouseCursorChange
    
      ImGuiConfigFlags_NoKeyboard
    
      ImGuiConfigFlags_DockingEnable
    
      ImGuiConfigFlags_ViewportsEnable
    
      ImGuiConfigFlags_DpiEnableScaleViewports
    
      ImGuiConfigFlags_DpiEnableScaleFonts
    
      ImGuiConfigFlags_IsSRGB
    
      ImGuiConfigFlags_IsTouchScreen
    """
    ImGuiConfigFlags_DockingEnable: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_DockingEnable: 128>
    ImGuiConfigFlags_DpiEnableScaleFonts: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_DpiEnableScaleFonts: 32768>
    ImGuiConfigFlags_DpiEnableScaleViewports: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_DpiEnableScaleViewports: 16384>
    ImGuiConfigFlags_IsSRGB: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_IsSRGB: 1048576>
    ImGuiConfigFlags_IsTouchScreen: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_IsTouchScreen: 2097152>
    ImGuiConfigFlags_NavEnableGamepad: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NavEnableGamepad: 2>
    ImGuiConfigFlags_NavEnableKeyboard: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NavEnableKeyboard: 1>
    ImGuiConfigFlags_NavEnableSetMousePos: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NavEnableSetMousePos: 4>
    ImGuiConfigFlags_NavNoCaptureKeyboard: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NavNoCaptureKeyboard: 8>
    ImGuiConfigFlags_NoKeyboard: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NoKeyboard: 64>
    ImGuiConfigFlags_NoMouse: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NoMouse: 16>
    ImGuiConfigFlags_NoMouseCursorChange: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NoMouseCursorChange: 32>
    ImGuiConfigFlags_None: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_None: 0>
    ImGuiConfigFlags_ViewportsEnable: typing.ClassVar[ImGuiConfigFlags_]  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_ViewportsEnable: 1024>
    __members__: typing.ClassVar[dict[str, ImGuiConfigFlags_]]  # value = {'ImGuiConfigFlags_None': <ImGuiConfigFlags_.ImGuiConfigFlags_None: 0>, 'ImGuiConfigFlags_NavEnableKeyboard': <ImGuiConfigFlags_.ImGuiConfigFlags_NavEnableKeyboard: 1>, 'ImGuiConfigFlags_NavEnableGamepad': <ImGuiConfigFlags_.ImGuiConfigFlags_NavEnableGamepad: 2>, 'ImGuiConfigFlags_NavEnableSetMousePos': <ImGuiConfigFlags_.ImGuiConfigFlags_NavEnableSetMousePos: 4>, 'ImGuiConfigFlags_NavNoCaptureKeyboard': <ImGuiConfigFlags_.ImGuiConfigFlags_NavNoCaptureKeyboard: 8>, 'ImGuiConfigFlags_NoMouse': <ImGuiConfigFlags_.ImGuiConfigFlags_NoMouse: 16>, 'ImGuiConfigFlags_NoMouseCursorChange': <ImGuiConfigFlags_.ImGuiConfigFlags_NoMouseCursorChange: 32>, 'ImGuiConfigFlags_NoKeyboard': <ImGuiConfigFlags_.ImGuiConfigFlags_NoKeyboard: 64>, 'ImGuiConfigFlags_DockingEnable': <ImGuiConfigFlags_.ImGuiConfigFlags_DockingEnable: 128>, 'ImGuiConfigFlags_ViewportsEnable': <ImGuiConfigFlags_.ImGuiConfigFlags_ViewportsEnable: 1024>, 'ImGuiConfigFlags_DpiEnableScaleViewports': <ImGuiConfigFlags_.ImGuiConfigFlags_DpiEnableScaleViewports: 16384>, 'ImGuiConfigFlags_DpiEnableScaleFonts': <ImGuiConfigFlags_.ImGuiConfigFlags_DpiEnableScaleFonts: 32768>, 'ImGuiConfigFlags_IsSRGB': <ImGuiConfigFlags_.ImGuiConfigFlags_IsSRGB: 1048576>, 'ImGuiConfigFlags_IsTouchScreen': <ImGuiConfigFlags_.ImGuiConfigFlags_IsTouchScreen: 2097152>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiContext:
    ActiveId: int
    ActiveIdAllowOverlap: bool
    ActiveIdClickOffset: ImVec2
    ActiveIdFromShortcut: bool
    ActiveIdHasBeenEditedBefore: bool
    ActiveIdHasBeenEditedThisFrame: bool
    ActiveIdHasBeenPressedBefore: bool
    ActiveIdIsAlive: int
    ActiveIdIsJustActivated: bool
    ActiveIdMouseButton: int
    ActiveIdNoClearOnFocusLoss: bool
    ActiveIdPreviousFrame: int
    ActiveIdPreviousFrameHasBeenEditedBefore: bool
    ActiveIdPreviousFrameIsAlive: bool
    ActiveIdPreviousFrameWindow: ImGuiWindow
    ActiveIdSource: ImGuiInputSource
    ActiveIdTimer: float
    ActiveIdUsingAllKeyboardKeys: bool
    ActiveIdUsingNavDirMask: int
    ActiveIdWindow: ImGuiWindow
    BeginComboDepth: int
    BeginMenuDepth: int
    BeginPopupStack: ImVector_ImGuiPopupData
    ClipboardHandlerData: ImVector_char
    ClipperTempData: ImVector_ImGuiListClipperData
    ClipperTempDataStacked: int
    ColorEditCurrentID: int
    ColorEditOptions: int
    ColorEditSavedColor: int
    ColorEditSavedHue: float
    ColorEditSavedID: int
    ColorEditSavedSat: float
    ColorPickerRef: ImVec4
    ColorStack: ImVector_ImGuiColorMod
    ComboPreviewData: ImGuiComboPreviewData
    ConfigFlagsCurrFrame: int
    ConfigFlagsLastFrame: int
    ConfigNavWindowingKeyNext: int
    ConfigNavWindowingKeyPrev: int
    CurrentDpiScale: float
    CurrentFocusScopeId: int
    CurrentItemFlags: int
    CurrentTabBar: ImGuiTabBar
    CurrentTabBarStack: ImVector_ImGuiPtrOrIndex
    CurrentTable: ImGuiTable
    CurrentViewport: ImGuiViewportP
    CurrentWindow: ImGuiWindow
    CurrentWindowStack: ImVector_ImGuiWindowStackData
    DataTypeZeroValue: ImGuiDataTypeStorage
    DebugAllocInfo: ImGuiDebugAllocInfo
    DebugBeginReturnValueCullDepth: int
    DebugBreakInLocateId: bool
    DebugBreakInShortcutRouting: int
    DebugBreakInTable: int
    DebugBreakInWindow: int
    DebugBreakKeyChord: int
    DebugFlashStyleColorBackup: ImVec4
    DebugFlashStyleColorIdx: int
    DebugFlashStyleColorTime: float
    DebugHookIdInfo: int
    DebugHoveredDockNode: ImGuiDockNode
    DebugIDStackTool: ImGuiIDStackTool
    DebugItemPickerActive: bool
    DebugItemPickerBreakId: int
    DebugItemPickerMouseButton: int
    DebugLocateFrames: int
    DebugLocateId: int
    DebugLogAutoDisableFlags: int
    DebugLogAutoDisableFrames: int
    DebugLogBuf: ImGuiTextBuffer
    DebugLogFlags: int
    DebugLogIndex: ImGuiTextIndex
    DebugMetricsConfig: ImGuiMetricsConfig
    DebugShowGroupRects: bool
    DimBgRatio: float
    DisabledAlphaBackup: float
    DisabledStackSize: int
    DockContext: ImGuiDockContext
    DragCurrentAccum: float
    DragCurrentAccumDirty: bool
    DragDropAcceptFlags: int
    DragDropAcceptFrameCount: int
    DragDropAcceptIdCurr: int
    DragDropAcceptIdCurrRectSurface: float
    DragDropAcceptIdPrev: int
    DragDropActive: bool
    DragDropHoldJustPressedId: int
    DragDropMouseButton: int
    DragDropPayload: ImGuiPayload
    DragDropPayloadBufHeap: ImVector_unsigned_char
    DragDropSourceFlags: int
    DragDropSourceFrameCount: int
    DragDropTargetClipRect: ImRect
    DragDropTargetId: int
    DragDropTargetRect: ImRect
    DragDropWithinSource: bool
    DragDropWithinTarget: bool
    DragSpeedDefaultRatio: float
    DrawChannelsTempMergeBuffer: ImVector_ImDrawChannel
    DrawListSharedData: ImDrawListSharedData
    FallbackMonitor: ImGuiPlatformMonitor
    FocusScopeStack: ImVector_ImGuiFocusScopeData
    Font: ImFont
    FontAtlasOwnedByContext: bool
    FontBaseSize: float
    FontSize: float
    FontStack: ImVector_ImFontPtr
    FrameCount: int
    FrameCountEnded: int
    FrameCountPlatformEnded: int
    FrameCountRendered: int
    FramerateSecPerFrameAccum: float
    FramerateSecPerFrameCount: int
    FramerateSecPerFrameIdx: int
    GcCompactAll: bool
    GroupStack: ImVector_ImGuiGroupData
    HookIdNext: int
    Hooks: ImVector_ImGuiContextHook
    HoverItemDelayClearTimer: float
    HoverItemDelayId: int
    HoverItemDelayIdPreviousFrame: int
    HoverItemDelayTimer: float
    HoverItemUnlockedStationaryId: int
    HoverWindowUnlockedStationaryId: int
    HoveredId: int
    HoveredIdAllowOverlap: bool
    HoveredIdIsDisabled: bool
    HoveredIdNotActiveTimer: float
    HoveredIdPreviousFrame: int
    HoveredIdTimer: float
    HoveredWindow: ImGuiWindow
    HoveredWindowBeforeClear: ImGuiWindow
    HoveredWindowUnderMovingWindow: ImGuiWindow
    IO: ImGuiIO
    Initialized: bool
    InputEventsNextEventId: int
    InputEventsNextMouseSource: ImGuiMouseSource
    InputEventsQueue: ImVector_ImGuiInputEvent
    InputEventsTrail: ImVector_ImGuiInputEvent
    InputTextDeactivatedState: ImGuiInputTextDeactivatedState
    InputTextPasswordFont: ImFont
    InputTextState: ImGuiInputTextState
    ItemFlagsStack: ImVector_ImGuiItemFlags
    ItemUnclipByLog: bool
    KeysMayBeCharInput: ImBitArray_ImGuiKey_NamedKey_COUNT__lessImGuiKey_NamedKey_BEGIN
    KeysRoutingTable: ImGuiKeyRoutingTable
    LastActiveId: int
    LastActiveIdTimer: float
    LastItemData: ImGuiLastItemData
    LastKeyModsChangeFromNoneTime: float
    LastKeyModsChangeTime: float
    LastKeyboardKeyPressTime: float
    LockMarkEdited: int
    LogBuffer: ImGuiTextBuffer
    LogDepthRef: int
    LogDepthToExpand: int
    LogDepthToExpandDefault: int
    LogEnabled: bool
    LogFile: _iobuf
    LogLineFirstItem: bool
    LogLinePosY: float
    LogNextPrefix: str
    LogNextSuffix: str
    LogType: ImGuiLogType
    MenusIdSubmittedThisFrame: ImVector_ImGuiID
    MouseCursor: int
    MouseLastHoveredViewport: ImGuiViewportP
    MouseLastValidPos: ImVec2
    MouseStationaryTimer: float
    MouseViewport: ImGuiViewportP
    MovingWindow: ImGuiWindow
    NavActivateDownId: int
    NavActivateFlags: int
    NavActivateId: int
    NavActivatePressedId: int
    NavAnyRequest: bool
    NavDisableHighlight: bool
    NavDisableMouseHover: bool
    NavFocusRoute: ImVector_ImGuiFocusScopeData
    NavFocusScopeId: int
    NavHighlightActivatedId: int
    NavHighlightActivatedTimer: float
    NavId: int
    NavIdIsAlive: bool
    NavInitRequest: bool
    NavInitRequestFromMove: bool
    NavInitResult: ImGuiNavItemData
    NavInputSource: ImGuiInputSource
    NavJustMovedFromFocusScopeId: int
    NavJustMovedToFocusScopeId: int
    NavJustMovedToHasSelectionData: bool
    NavJustMovedToId: int
    NavJustMovedToIsTabbing: bool
    NavJustMovedToKeyMods: int
    NavLastValidSelectionUserData: int
    NavLayer: ImGuiNavLayer
    NavMousePosDirty: bool
    NavMoveClipDir: ImGuiDir
    NavMoveDir: ImGuiDir
    NavMoveDirForDebug: ImGuiDir
    NavMoveFlags: int
    NavMoveForwardToNextFrame: bool
    NavMoveKeyMods: int
    NavMoveResultLocal: ImGuiNavItemData
    NavMoveResultLocalVisible: ImGuiNavItemData
    NavMoveResultOther: ImGuiNavItemData
    NavMoveScoringItems: bool
    NavMoveScrollFlags: int
    NavMoveSubmitted: bool
    NavNextActivateFlags: int
    NavNextActivateId: int
    NavScoringDebugCount: int
    NavScoringNoClipRect: ImRect
    NavScoringRect: ImRect
    NavTabbingCounter: int
    NavTabbingDir: int
    NavTabbingResultFirst: ImGuiNavItemData
    NavTreeNodeStack: ImVector_ImGuiNavTreeNodeData
    NavWindow: ImGuiWindow
    NavWindowingAccumDeltaPos: ImVec2
    NavWindowingAccumDeltaSize: ImVec2
    NavWindowingHighlightAlpha: float
    NavWindowingListWindow: ImGuiWindow
    NavWindowingTarget: ImGuiWindow
    NavWindowingTargetAnim: ImGuiWindow
    NavWindowingTimer: float
    NavWindowingToggleKey: ImGuiKey
    NavWindowingToggleLayer: bool
    NextItemData: ImGuiNextItemData
    NextWindowData: ImGuiNextWindowData
    OpenPopupStack: ImVector_ImGuiPopupData
    PlatformIO: ImGuiPlatformIO
    PlatformImeData: ImGuiPlatformImeData
    PlatformImeDataPrev: ImGuiPlatformImeData
    PlatformImeViewport: int
    PlatformLastFocusedViewportId: int
    PlatformMonitorsFullWorkRect: ImRect
    PlatformWindowsCreatedCount: int
    ScrollbarClickDeltaToGrabCenter: float
    ScrollbarSeekMode: int
    SettingsDirtyTimer: float
    SettingsHandlers: ImVector_ImGuiSettingsHandler
    SettingsIniData: ImGuiTextBuffer
    SettingsLoaded: bool
    SettingsTables: ImChunkStream_ImGuiTableSettings
    SettingsWindows: ImChunkStream_ImGuiWindowSettings
    ShrinkWidthBuffer: ImVector_ImGuiShrinkWidthItem
    SliderCurrentAccum: float
    SliderCurrentAccumDirty: bool
    SliderGrabClickOffset: float
    Style: ImGuiStyle
    StyleVarStack: ImVector_ImGuiStyleMod
    TabBars: ImPool_ImGuiTabBar
    Tables: ImPool_ImGuiTable
    TablesLastTimeActive: ImVector_float
    TablesTempData: ImVector_ImGuiTableTempData
    TablesTempDataStacked: int
    TempBuffer: ImVector_char
    TempInputId: int
    TestEngine: capsule
    TestEngineHookItems: bool
    Time: float
    TooltipOverrideCount: int
    TypingSelectState: ImGuiTypingSelectState
    ViewportCreatedCount: int
    ViewportFocusedStampCount: int
    Viewports: ImVector_ImGuiViewportPPtr
    WantCaptureKeyboardNextFrame: int
    WantCaptureMouseNextFrame: int
    WantTextInputNextFrame: int
    WheelingAxisAvg: ImVec2
    WheelingWindow: ImGuiWindow
    WheelingWindowRefMousePos: ImVec2
    WheelingWindowReleaseTimer: float
    WheelingWindowScrolledFrame: int
    WheelingWindowStartFrame: int
    WheelingWindowWheelRemainder: ImVec2
    WindowResizeBorderExpectedRect: ImRect
    WindowResizeRelativeMode: bool
    Windows: ImVector_ImGuiWindowPtr
    WindowsActiveCount: int
    WindowsById: ImGuiStorage
    WindowsFocusOrder: ImVector_ImGuiWindowPtr
    WindowsHoverPadding: ImVec2
    WindowsTempSortBuffer: ImVector_ImGuiWindowPtr
    WithinEndChild: bool
    WithinFrameScope: bool
    WithinFrameScopeWithImplicitWindow: bool
    def __init__(self, shared_font_atlas: ImFontAtlas) -> None:
        ...
    @property
    def ContextName(self) -> Arr_char:
        ...
    @property
    def DragDropPayloadBufLocal(self) -> Arr_unsigned_char:
        ...
    @property
    def FramerateSecPerFrame(self) -> Arr_float:
        ...
    @property
    def KeysOwnerData(self) -> Arr_ImGuiKeyOwnerData:
        ...
    @property
    def LocalizationTable(self) -> Arr_p_const_char:
        ...
    @property
    def TempKeychordName(self) -> Arr_char:
        ...
class ImGuiContextHook:
    HookId: int
    Owner: int
    Type: ImGuiContextHookType
    UserData: capsule
    def __init__(self) -> None:
        ...
    @property
    def Callback(*args, **kwargs):
        """
        (arg0: pyimgui.imgui.ImGuiContextHook) -> void __cdecl(ImGuiContext * __ptr64,ImGuiContextHook * __ptr64)
        """
    @Callback.setter
    def Callback(self, arg1: ...) -> None:
        ...
class ImGuiContextHookType:
    """
    Members:
    
      ImGuiContextHookType_NewFramePre
    
      ImGuiContextHookType_NewFramePost
    
      ImGuiContextHookType_EndFramePre
    
      ImGuiContextHookType_EndFramePost
    
      ImGuiContextHookType_RenderPre
    
      ImGuiContextHookType_RenderPost
    
      ImGuiContextHookType_Shutdown
    
      ImGuiContextHookType_PendingRemoval_
    """
    ImGuiContextHookType_EndFramePost: typing.ClassVar[ImGuiContextHookType]  # value = <ImGuiContextHookType.ImGuiContextHookType_EndFramePost: 3>
    ImGuiContextHookType_EndFramePre: typing.ClassVar[ImGuiContextHookType]  # value = <ImGuiContextHookType.ImGuiContextHookType_EndFramePre: 2>
    ImGuiContextHookType_NewFramePost: typing.ClassVar[ImGuiContextHookType]  # value = <ImGuiContextHookType.ImGuiContextHookType_NewFramePost: 1>
    ImGuiContextHookType_NewFramePre: typing.ClassVar[ImGuiContextHookType]  # value = <ImGuiContextHookType.ImGuiContextHookType_NewFramePre: 0>
    ImGuiContextHookType_PendingRemoval_: typing.ClassVar[ImGuiContextHookType]  # value = <ImGuiContextHookType.ImGuiContextHookType_PendingRemoval_: 7>
    ImGuiContextHookType_RenderPost: typing.ClassVar[ImGuiContextHookType]  # value = <ImGuiContextHookType.ImGuiContextHookType_RenderPost: 5>
    ImGuiContextHookType_RenderPre: typing.ClassVar[ImGuiContextHookType]  # value = <ImGuiContextHookType.ImGuiContextHookType_RenderPre: 4>
    ImGuiContextHookType_Shutdown: typing.ClassVar[ImGuiContextHookType]  # value = <ImGuiContextHookType.ImGuiContextHookType_Shutdown: 6>
    __members__: typing.ClassVar[dict[str, ImGuiContextHookType]]  # value = {'ImGuiContextHookType_NewFramePre': <ImGuiContextHookType.ImGuiContextHookType_NewFramePre: 0>, 'ImGuiContextHookType_NewFramePost': <ImGuiContextHookType.ImGuiContextHookType_NewFramePost: 1>, 'ImGuiContextHookType_EndFramePre': <ImGuiContextHookType.ImGuiContextHookType_EndFramePre: 2>, 'ImGuiContextHookType_EndFramePost': <ImGuiContextHookType.ImGuiContextHookType_EndFramePost: 3>, 'ImGuiContextHookType_RenderPre': <ImGuiContextHookType.ImGuiContextHookType_RenderPre: 4>, 'ImGuiContextHookType_RenderPost': <ImGuiContextHookType.ImGuiContextHookType_RenderPost: 5>, 'ImGuiContextHookType_Shutdown': <ImGuiContextHookType.ImGuiContextHookType_Shutdown: 6>, 'ImGuiContextHookType_PendingRemoval_': <ImGuiContextHookType.ImGuiContextHookType_PendingRemoval_: 7>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiDataAuthority_:
    """
    Members:
    
      ImGuiDataAuthority_Auto
    
      ImGuiDataAuthority_DockNode
    
      ImGuiDataAuthority_Window
    """
    ImGuiDataAuthority_Auto: typing.ClassVar[ImGuiDataAuthority_]  # value = <ImGuiDataAuthority_.ImGuiDataAuthority_Auto: 0>
    ImGuiDataAuthority_DockNode: typing.ClassVar[ImGuiDataAuthority_]  # value = <ImGuiDataAuthority_.ImGuiDataAuthority_DockNode: 1>
    ImGuiDataAuthority_Window: typing.ClassVar[ImGuiDataAuthority_]  # value = <ImGuiDataAuthority_.ImGuiDataAuthority_Window: 2>
    __members__: typing.ClassVar[dict[str, ImGuiDataAuthority_]]  # value = {'ImGuiDataAuthority_Auto': <ImGuiDataAuthority_.ImGuiDataAuthority_Auto: 0>, 'ImGuiDataAuthority_DockNode': <ImGuiDataAuthority_.ImGuiDataAuthority_DockNode: 1>, 'ImGuiDataAuthority_Window': <ImGuiDataAuthority_.ImGuiDataAuthority_Window: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiDataTypeInfo:
    Name: str
    PrintFmt: str
    ScanFmt: str
    Size: int
class ImGuiDataTypePrivate_:
    """
    Members:
    
      ImGuiDataType_String
    
      ImGuiDataType_Pointer
    
      ImGuiDataType_ID
    """
    ImGuiDataType_ID: typing.ClassVar[ImGuiDataTypePrivate_]  # value = <ImGuiDataTypePrivate_.ImGuiDataType_ID: 13>
    ImGuiDataType_Pointer: typing.ClassVar[ImGuiDataTypePrivate_]  # value = <ImGuiDataTypePrivate_.ImGuiDataType_Pointer: 12>
    ImGuiDataType_String: typing.ClassVar[ImGuiDataTypePrivate_]  # value = <ImGuiDataTypePrivate_.ImGuiDataType_String: 11>
    __members__: typing.ClassVar[dict[str, ImGuiDataTypePrivate_]]  # value = {'ImGuiDataType_String': <ImGuiDataTypePrivate_.ImGuiDataType_String: 11>, 'ImGuiDataType_Pointer': <ImGuiDataTypePrivate_.ImGuiDataType_Pointer: 12>, 'ImGuiDataType_ID': <ImGuiDataTypePrivate_.ImGuiDataType_ID: 13>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiDataTypeStorage:
    @property
    def Data(self) -> Arr_unsigned_char:
        ...
class ImGuiDataType_:
    """
    Members:
    
      ImGuiDataType_S8
    
      ImGuiDataType_U8
    
      ImGuiDataType_S16
    
      ImGuiDataType_U16
    
      ImGuiDataType_S32
    
      ImGuiDataType_U32
    
      ImGuiDataType_S64
    
      ImGuiDataType_U64
    
      ImGuiDataType_Float
    
      ImGuiDataType_Double
    
      ImGuiDataType_COUNT
    """
    ImGuiDataType_COUNT: typing.ClassVar[ImGuiDataType_]  # value = <ImGuiDataType_.ImGuiDataType_COUNT: 10>
    ImGuiDataType_Double: typing.ClassVar[ImGuiDataType_]  # value = <ImGuiDataType_.ImGuiDataType_Double: 9>
    ImGuiDataType_Float: typing.ClassVar[ImGuiDataType_]  # value = <ImGuiDataType_.ImGuiDataType_Float: 8>
    ImGuiDataType_S16: typing.ClassVar[ImGuiDataType_]  # value = <ImGuiDataType_.ImGuiDataType_S16: 2>
    ImGuiDataType_S32: typing.ClassVar[ImGuiDataType_]  # value = <ImGuiDataType_.ImGuiDataType_S32: 4>
    ImGuiDataType_S64: typing.ClassVar[ImGuiDataType_]  # value = <ImGuiDataType_.ImGuiDataType_S64: 6>
    ImGuiDataType_S8: typing.ClassVar[ImGuiDataType_]  # value = <ImGuiDataType_.ImGuiDataType_S8: 0>
    ImGuiDataType_U16: typing.ClassVar[ImGuiDataType_]  # value = <ImGuiDataType_.ImGuiDataType_U16: 3>
    ImGuiDataType_U32: typing.ClassVar[ImGuiDataType_]  # value = <ImGuiDataType_.ImGuiDataType_U32: 5>
    ImGuiDataType_U64: typing.ClassVar[ImGuiDataType_]  # value = <ImGuiDataType_.ImGuiDataType_U64: 7>
    ImGuiDataType_U8: typing.ClassVar[ImGuiDataType_]  # value = <ImGuiDataType_.ImGuiDataType_U8: 1>
    __members__: typing.ClassVar[dict[str, ImGuiDataType_]]  # value = {'ImGuiDataType_S8': <ImGuiDataType_.ImGuiDataType_S8: 0>, 'ImGuiDataType_U8': <ImGuiDataType_.ImGuiDataType_U8: 1>, 'ImGuiDataType_S16': <ImGuiDataType_.ImGuiDataType_S16: 2>, 'ImGuiDataType_U16': <ImGuiDataType_.ImGuiDataType_U16: 3>, 'ImGuiDataType_S32': <ImGuiDataType_.ImGuiDataType_S32: 4>, 'ImGuiDataType_U32': <ImGuiDataType_.ImGuiDataType_U32: 5>, 'ImGuiDataType_S64': <ImGuiDataType_.ImGuiDataType_S64: 6>, 'ImGuiDataType_U64': <ImGuiDataType_.ImGuiDataType_U64: 7>, 'ImGuiDataType_Float': <ImGuiDataType_.ImGuiDataType_Float: 8>, 'ImGuiDataType_Double': <ImGuiDataType_.ImGuiDataType_Double: 9>, 'ImGuiDataType_COUNT': <ImGuiDataType_.ImGuiDataType_COUNT: 10>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiDataVarInfo:
    Count: int
    Offset: int
    Type: int
    def GetVarPtr(self, parent: capsule) -> capsule:
        ...
class ImGuiDebugAllocEntry:
    AllocCount: int
    FrameCount: int
    FreeCount: int
class ImGuiDebugAllocInfo:
    LastEntriesIdx: int
    TotalAllocCount: int
    TotalFreeCount: int
    def __init__(self) -> None:
        ...
    @property
    def LastEntriesBuf(self) -> Arr_ImGuiDebugAllocEntry:
        ...
class ImGuiDebugLogFlags_:
    """
    Members:
    
      ImGuiDebugLogFlags_None
    
      ImGuiDebugLogFlags_EventActiveId
    
      ImGuiDebugLogFlags_EventFocus
    
      ImGuiDebugLogFlags_EventPopup
    
      ImGuiDebugLogFlags_EventNav
    
      ImGuiDebugLogFlags_EventClipper
    
      ImGuiDebugLogFlags_EventSelection
    
      ImGuiDebugLogFlags_EventIO
    
      ImGuiDebugLogFlags_EventInputRouting
    
      ImGuiDebugLogFlags_EventDocking
    
      ImGuiDebugLogFlags_EventViewport
    
      ImGuiDebugLogFlags_EventMask_
    
      ImGuiDebugLogFlags_OutputToTTY
    
      ImGuiDebugLogFlags_OutputToTestEngine
    """
    ImGuiDebugLogFlags_EventActiveId: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventActiveId: 1>
    ImGuiDebugLogFlags_EventClipper: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventClipper: 16>
    ImGuiDebugLogFlags_EventDocking: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventDocking: 256>
    ImGuiDebugLogFlags_EventFocus: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventFocus: 2>
    ImGuiDebugLogFlags_EventIO: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventIO: 64>
    ImGuiDebugLogFlags_EventInputRouting: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventInputRouting: 128>
    ImGuiDebugLogFlags_EventMask_: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventMask_: 1023>
    ImGuiDebugLogFlags_EventNav: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventNav: 8>
    ImGuiDebugLogFlags_EventPopup: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventPopup: 4>
    ImGuiDebugLogFlags_EventSelection: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventSelection: 32>
    ImGuiDebugLogFlags_EventViewport: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventViewport: 512>
    ImGuiDebugLogFlags_None: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_None: 0>
    ImGuiDebugLogFlags_OutputToTTY: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_OutputToTTY: 1048576>
    ImGuiDebugLogFlags_OutputToTestEngine: typing.ClassVar[ImGuiDebugLogFlags_]  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_OutputToTestEngine: 2097152>
    __members__: typing.ClassVar[dict[str, ImGuiDebugLogFlags_]]  # value = {'ImGuiDebugLogFlags_None': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_None: 0>, 'ImGuiDebugLogFlags_EventActiveId': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventActiveId: 1>, 'ImGuiDebugLogFlags_EventFocus': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventFocus: 2>, 'ImGuiDebugLogFlags_EventPopup': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventPopup: 4>, 'ImGuiDebugLogFlags_EventNav': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventNav: 8>, 'ImGuiDebugLogFlags_EventClipper': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventClipper: 16>, 'ImGuiDebugLogFlags_EventSelection': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventSelection: 32>, 'ImGuiDebugLogFlags_EventIO': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventIO: 64>, 'ImGuiDebugLogFlags_EventInputRouting': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventInputRouting: 128>, 'ImGuiDebugLogFlags_EventDocking': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventDocking: 256>, 'ImGuiDebugLogFlags_EventViewport': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventViewport: 512>, 'ImGuiDebugLogFlags_EventMask_': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventMask_: 1023>, 'ImGuiDebugLogFlags_OutputToTTY': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_OutputToTTY: 1048576>, 'ImGuiDebugLogFlags_OutputToTestEngine': <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_OutputToTestEngine: 2097152>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiDir:
    """
    Members:
    
      ImGuiDir_None
    
      ImGuiDir_Left
    
      ImGuiDir_Right
    
      ImGuiDir_Up
    
      ImGuiDir_Down
    
      ImGuiDir_COUNT
    """
    ImGuiDir_COUNT: typing.ClassVar[ImGuiDir]  # value = <ImGuiDir.ImGuiDir_COUNT: 4>
    ImGuiDir_Down: typing.ClassVar[ImGuiDir]  # value = <ImGuiDir.ImGuiDir_Down: 3>
    ImGuiDir_Left: typing.ClassVar[ImGuiDir]  # value = <ImGuiDir.ImGuiDir_Left: 0>
    ImGuiDir_None: typing.ClassVar[ImGuiDir]  # value = <ImGuiDir.ImGuiDir_None: -1>
    ImGuiDir_Right: typing.ClassVar[ImGuiDir]  # value = <ImGuiDir.ImGuiDir_Right: 1>
    ImGuiDir_Up: typing.ClassVar[ImGuiDir]  # value = <ImGuiDir.ImGuiDir_Up: 2>
    __members__: typing.ClassVar[dict[str, ImGuiDir]]  # value = {'ImGuiDir_None': <ImGuiDir.ImGuiDir_None: -1>, 'ImGuiDir_Left': <ImGuiDir.ImGuiDir_Left: 0>, 'ImGuiDir_Right': <ImGuiDir.ImGuiDir_Right: 1>, 'ImGuiDir_Up': <ImGuiDir.ImGuiDir_Up: 2>, 'ImGuiDir_Down': <ImGuiDir.ImGuiDir_Down: 3>, 'ImGuiDir_COUNT': <ImGuiDir.ImGuiDir_COUNT: 4>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiDockContext:
    Nodes: ImGuiStorage
    NodesSettings: ImVector_ImGuiDockNodeSettings
    Requests: ImVector_ImGuiDockRequest
    WantFullRebuild: bool
    def __init__(self) -> None:
        ...
class ImGuiDockNode:
    AuthorityForPos: int
    AuthorityForSize: int
    AuthorityForViewport: int
    CentralNode: ImGuiDockNode
    CountNodeWithWindows: int
    HasCentralNodeChild: bool
    HasCloseButton: bool
    HasWindowMenuButton: bool
    HostWindow: ImGuiWindow
    ID: int
    IsBgDrawnThisFrame: bool
    IsFocused: bool
    IsVisible: bool
    LastBgColor: int
    LastFocusedNodeId: int
    LastFrameActive: int
    LastFrameAlive: int
    LastFrameFocused: int
    LocalFlags: int
    LocalFlagsInWindows: int
    MergedFlags: int
    OnlyNodeWithWindows: ImGuiDockNode
    ParentNode: ImGuiDockNode
    Pos: ImVec2
    RefViewportId: int
    SelectedTabId: int
    SharedFlags: int
    Size: ImVec2
    SizeRef: ImVec2
    SplitAxis: ImGuiAxis
    State: ImGuiDockNodeState
    TabBar: ImGuiTabBar
    VisibleWindow: ImGuiWindow
    WantCloseAll: bool
    WantCloseTabId: int
    WantHiddenTabBarToggle: bool
    WantHiddenTabBarUpdate: bool
    WantLockSizeOnce: bool
    WantMouseMove: bool
    WindowClass: ImGuiWindowClass
    Windows: ImVector_ImGuiWindowPtr
    def IsCentralNode(self) -> bool:
        ...
    def IsDockSpace(self) -> bool:
        ...
    def IsEmpty(self) -> bool:
        ...
    def IsFloatingNode(self) -> bool:
        ...
    def IsHiddenTabBar(self) -> bool:
        ...
    def IsLeafNode(self) -> bool:
        ...
    def IsNoTabBar(self) -> bool:
        ...
    def IsRootNode(self) -> bool:
        ...
    def IsSplitNode(self) -> bool:
        ...
    def Rect(self) -> ImRect:
        ...
    def SetLocalFlags(self, flags: int) -> None:
        ...
    def UpdateMergedFlags(self) -> None:
        ...
    def __init__(self, id: int) -> None:
        ...
    @property
    def ChildNodes(self) -> Arr_p_ImGuiDockNode:
        ...
class ImGuiDockNodeFlagsPrivate_:
    """
    Members:
    
      ImGuiDockNodeFlags_DockSpace
    
      ImGuiDockNodeFlags_CentralNode
    
      ImGuiDockNodeFlags_NoTabBar
    
      ImGuiDockNodeFlags_HiddenTabBar
    
      ImGuiDockNodeFlags_NoWindowMenuButton
    
      ImGuiDockNodeFlags_NoCloseButton
    
      ImGuiDockNodeFlags_NoResizeX
    
      ImGuiDockNodeFlags_NoResizeY
    
      ImGuiDockNodeFlags_DockedWindowsInFocusRoute
    
      ImGuiDockNodeFlags_NoDockingSplitOther
    
      ImGuiDockNodeFlags_NoDockingOverMe
    
      ImGuiDockNodeFlags_NoDockingOverOther
    
      ImGuiDockNodeFlags_NoDockingOverEmpty
    
      ImGuiDockNodeFlags_NoDocking
    
      ImGuiDockNodeFlags_SharedFlagsInheritMask_
    
      ImGuiDockNodeFlags_NoResizeFlagsMask_
    
      ImGuiDockNodeFlags_LocalFlagsTransferMask_
    
      ImGuiDockNodeFlags_SavedFlagsMask_
    """
    ImGuiDockNodeFlags_CentralNode: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_CentralNode: 2048>
    ImGuiDockNodeFlags_DockSpace: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_DockSpace: 1024>
    ImGuiDockNodeFlags_DockedWindowsInFocusRoute: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_DockedWindowsInFocusRoute: 262144>
    ImGuiDockNodeFlags_HiddenTabBar: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_HiddenTabBar: 8192>
    ImGuiDockNodeFlags_LocalFlagsTransferMask_: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_LocalFlagsTransferMask_: 260208>
    ImGuiDockNodeFlags_NoCloseButton: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoCloseButton: 32768>
    ImGuiDockNodeFlags_NoDocking: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDocking: 7864336>
    ImGuiDockNodeFlags_NoDockingOverEmpty: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDockingOverEmpty: 4194304>
    ImGuiDockNodeFlags_NoDockingOverMe: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDockingOverMe: 1048576>
    ImGuiDockNodeFlags_NoDockingOverOther: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDockingOverOther: 2097152>
    ImGuiDockNodeFlags_NoDockingSplitOther: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDockingSplitOther: 524288>
    ImGuiDockNodeFlags_NoResizeFlagsMask_: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoResizeFlagsMask_: 196640>
    ImGuiDockNodeFlags_NoResizeX: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoResizeX: 65536>
    ImGuiDockNodeFlags_NoResizeY: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoResizeY: 131072>
    ImGuiDockNodeFlags_NoTabBar: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoTabBar: 4096>
    ImGuiDockNodeFlags_NoWindowMenuButton: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoWindowMenuButton: 16384>
    ImGuiDockNodeFlags_SavedFlagsMask_: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_SavedFlagsMask_: 261152>
    ImGuiDockNodeFlags_SharedFlagsInheritMask_: typing.ClassVar[ImGuiDockNodeFlagsPrivate_]  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_SharedFlagsInheritMask_: -1>
    __members__: typing.ClassVar[dict[str, ImGuiDockNodeFlagsPrivate_]]  # value = {'ImGuiDockNodeFlags_DockSpace': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_DockSpace: 1024>, 'ImGuiDockNodeFlags_CentralNode': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_CentralNode: 2048>, 'ImGuiDockNodeFlags_NoTabBar': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoTabBar: 4096>, 'ImGuiDockNodeFlags_HiddenTabBar': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_HiddenTabBar: 8192>, 'ImGuiDockNodeFlags_NoWindowMenuButton': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoWindowMenuButton: 16384>, 'ImGuiDockNodeFlags_NoCloseButton': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoCloseButton: 32768>, 'ImGuiDockNodeFlags_NoResizeX': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoResizeX: 65536>, 'ImGuiDockNodeFlags_NoResizeY': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoResizeY: 131072>, 'ImGuiDockNodeFlags_DockedWindowsInFocusRoute': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_DockedWindowsInFocusRoute: 262144>, 'ImGuiDockNodeFlags_NoDockingSplitOther': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDockingSplitOther: 524288>, 'ImGuiDockNodeFlags_NoDockingOverMe': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDockingOverMe: 1048576>, 'ImGuiDockNodeFlags_NoDockingOverOther': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDockingOverOther: 2097152>, 'ImGuiDockNodeFlags_NoDockingOverEmpty': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDockingOverEmpty: 4194304>, 'ImGuiDockNodeFlags_NoDocking': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDocking: 7864336>, 'ImGuiDockNodeFlags_SharedFlagsInheritMask_': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_SharedFlagsInheritMask_: -1>, 'ImGuiDockNodeFlags_NoResizeFlagsMask_': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoResizeFlagsMask_: 196640>, 'ImGuiDockNodeFlags_LocalFlagsTransferMask_': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_LocalFlagsTransferMask_: 260208>, 'ImGuiDockNodeFlags_SavedFlagsMask_': <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_SavedFlagsMask_: 261152>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiDockNodeFlags_:
    """
    Members:
    
      ImGuiDockNodeFlags_None
    
      ImGuiDockNodeFlags_KeepAliveOnly
    
      ImGuiDockNodeFlags_NoDockingOverCentralNode
    
      ImGuiDockNodeFlags_PassthruCentralNode
    
      ImGuiDockNodeFlags_NoDockingSplit
    
      ImGuiDockNodeFlags_NoResize
    
      ImGuiDockNodeFlags_AutoHideTabBar
    
      ImGuiDockNodeFlags_NoUndocking
    """
    ImGuiDockNodeFlags_AutoHideTabBar: typing.ClassVar[ImGuiDockNodeFlags_]  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_AutoHideTabBar: 64>
    ImGuiDockNodeFlags_KeepAliveOnly: typing.ClassVar[ImGuiDockNodeFlags_]  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_KeepAliveOnly: 1>
    ImGuiDockNodeFlags_NoDockingOverCentralNode: typing.ClassVar[ImGuiDockNodeFlags_]  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_NoDockingOverCentralNode: 4>
    ImGuiDockNodeFlags_NoDockingSplit: typing.ClassVar[ImGuiDockNodeFlags_]  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_NoDockingSplit: 16>
    ImGuiDockNodeFlags_NoResize: typing.ClassVar[ImGuiDockNodeFlags_]  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_NoResize: 32>
    ImGuiDockNodeFlags_NoUndocking: typing.ClassVar[ImGuiDockNodeFlags_]  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_NoUndocking: 128>
    ImGuiDockNodeFlags_None: typing.ClassVar[ImGuiDockNodeFlags_]  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_None: 0>
    ImGuiDockNodeFlags_PassthruCentralNode: typing.ClassVar[ImGuiDockNodeFlags_]  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_PassthruCentralNode: 8>
    __members__: typing.ClassVar[dict[str, ImGuiDockNodeFlags_]]  # value = {'ImGuiDockNodeFlags_None': <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_None: 0>, 'ImGuiDockNodeFlags_KeepAliveOnly': <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_KeepAliveOnly: 1>, 'ImGuiDockNodeFlags_NoDockingOverCentralNode': <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_NoDockingOverCentralNode: 4>, 'ImGuiDockNodeFlags_PassthruCentralNode': <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_PassthruCentralNode: 8>, 'ImGuiDockNodeFlags_NoDockingSplit': <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_NoDockingSplit: 16>, 'ImGuiDockNodeFlags_NoResize': <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_NoResize: 32>, 'ImGuiDockNodeFlags_AutoHideTabBar': <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_AutoHideTabBar: 64>, 'ImGuiDockNodeFlags_NoUndocking': <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_NoUndocking: 128>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiDockNodeState:
    """
    Members:
    
      ImGuiDockNodeState_Unknown
    
      ImGuiDockNodeState_HostWindowHiddenBecauseSingleWindow
    
      ImGuiDockNodeState_HostWindowHiddenBecauseWindowsAreResizing
    
      ImGuiDockNodeState_HostWindowVisible
    """
    ImGuiDockNodeState_HostWindowHiddenBecauseSingleWindow: typing.ClassVar[ImGuiDockNodeState]  # value = <ImGuiDockNodeState.ImGuiDockNodeState_HostWindowHiddenBecauseSingleWindow: 1>
    ImGuiDockNodeState_HostWindowHiddenBecauseWindowsAreResizing: typing.ClassVar[ImGuiDockNodeState]  # value = <ImGuiDockNodeState.ImGuiDockNodeState_HostWindowHiddenBecauseWindowsAreResizing: 2>
    ImGuiDockNodeState_HostWindowVisible: typing.ClassVar[ImGuiDockNodeState]  # value = <ImGuiDockNodeState.ImGuiDockNodeState_HostWindowVisible: 3>
    ImGuiDockNodeState_Unknown: typing.ClassVar[ImGuiDockNodeState]  # value = <ImGuiDockNodeState.ImGuiDockNodeState_Unknown: 0>
    __members__: typing.ClassVar[dict[str, ImGuiDockNodeState]]  # value = {'ImGuiDockNodeState_Unknown': <ImGuiDockNodeState.ImGuiDockNodeState_Unknown: 0>, 'ImGuiDockNodeState_HostWindowHiddenBecauseSingleWindow': <ImGuiDockNodeState.ImGuiDockNodeState_HostWindowHiddenBecauseSingleWindow: 1>, 'ImGuiDockNodeState_HostWindowHiddenBecauseWindowsAreResizing': <ImGuiDockNodeState.ImGuiDockNodeState_HostWindowHiddenBecauseWindowsAreResizing: 2>, 'ImGuiDockNodeState_HostWindowVisible': <ImGuiDockNodeState.ImGuiDockNodeState_HostWindowVisible: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiDragDropFlags_:
    """
    Members:
    
      ImGuiDragDropFlags_None
    
      ImGuiDragDropFlags_SourceNoPreviewTooltip
    
      ImGuiDragDropFlags_SourceNoDisableHover
    
      ImGuiDragDropFlags_SourceNoHoldToOpenOthers
    
      ImGuiDragDropFlags_SourceAllowNullID
    
      ImGuiDragDropFlags_SourceExtern
    
      ImGuiDragDropFlags_PayloadAutoExpire
    
      ImGuiDragDropFlags_PayloadNoCrossContext
    
      ImGuiDragDropFlags_PayloadNoCrossProcess
    
      ImGuiDragDropFlags_AcceptBeforeDelivery
    
      ImGuiDragDropFlags_AcceptNoDrawDefaultRect
    
      ImGuiDragDropFlags_AcceptNoPreviewTooltip
    
      ImGuiDragDropFlags_AcceptPeekOnly
    """
    ImGuiDragDropFlags_AcceptBeforeDelivery: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_AcceptBeforeDelivery: 1024>
    ImGuiDragDropFlags_AcceptNoDrawDefaultRect: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_AcceptNoDrawDefaultRect: 2048>
    ImGuiDragDropFlags_AcceptNoPreviewTooltip: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_AcceptNoPreviewTooltip: 4096>
    ImGuiDragDropFlags_AcceptPeekOnly: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_AcceptPeekOnly: 3072>
    ImGuiDragDropFlags_None: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_None: 0>
    ImGuiDragDropFlags_PayloadAutoExpire: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_PayloadAutoExpire: 32>
    ImGuiDragDropFlags_PayloadNoCrossContext: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_PayloadNoCrossContext: 64>
    ImGuiDragDropFlags_PayloadNoCrossProcess: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_PayloadNoCrossProcess: 128>
    ImGuiDragDropFlags_SourceAllowNullID: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceAllowNullID: 8>
    ImGuiDragDropFlags_SourceExtern: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceExtern: 16>
    ImGuiDragDropFlags_SourceNoDisableHover: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceNoDisableHover: 2>
    ImGuiDragDropFlags_SourceNoHoldToOpenOthers: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceNoHoldToOpenOthers: 4>
    ImGuiDragDropFlags_SourceNoPreviewTooltip: typing.ClassVar[ImGuiDragDropFlags_]  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceNoPreviewTooltip: 1>
    __members__: typing.ClassVar[dict[str, ImGuiDragDropFlags_]]  # value = {'ImGuiDragDropFlags_None': <ImGuiDragDropFlags_.ImGuiDragDropFlags_None: 0>, 'ImGuiDragDropFlags_SourceNoPreviewTooltip': <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceNoPreviewTooltip: 1>, 'ImGuiDragDropFlags_SourceNoDisableHover': <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceNoDisableHover: 2>, 'ImGuiDragDropFlags_SourceNoHoldToOpenOthers': <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceNoHoldToOpenOthers: 4>, 'ImGuiDragDropFlags_SourceAllowNullID': <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceAllowNullID: 8>, 'ImGuiDragDropFlags_SourceExtern': <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceExtern: 16>, 'ImGuiDragDropFlags_PayloadAutoExpire': <ImGuiDragDropFlags_.ImGuiDragDropFlags_PayloadAutoExpire: 32>, 'ImGuiDragDropFlags_PayloadNoCrossContext': <ImGuiDragDropFlags_.ImGuiDragDropFlags_PayloadNoCrossContext: 64>, 'ImGuiDragDropFlags_PayloadNoCrossProcess': <ImGuiDragDropFlags_.ImGuiDragDropFlags_PayloadNoCrossProcess: 128>, 'ImGuiDragDropFlags_AcceptBeforeDelivery': <ImGuiDragDropFlags_.ImGuiDragDropFlags_AcceptBeforeDelivery: 1024>, 'ImGuiDragDropFlags_AcceptNoDrawDefaultRect': <ImGuiDragDropFlags_.ImGuiDragDropFlags_AcceptNoDrawDefaultRect: 2048>, 'ImGuiDragDropFlags_AcceptNoPreviewTooltip': <ImGuiDragDropFlags_.ImGuiDragDropFlags_AcceptNoPreviewTooltip: 4096>, 'ImGuiDragDropFlags_AcceptPeekOnly': <ImGuiDragDropFlags_.ImGuiDragDropFlags_AcceptPeekOnly: 3072>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiFocusRequestFlags_:
    """
    Members:
    
      ImGuiFocusRequestFlags_None
    
      ImGuiFocusRequestFlags_RestoreFocusedChild
    
      ImGuiFocusRequestFlags_UnlessBelowModal
    """
    ImGuiFocusRequestFlags_None: typing.ClassVar[ImGuiFocusRequestFlags_]  # value = <ImGuiFocusRequestFlags_.ImGuiFocusRequestFlags_None: 0>
    ImGuiFocusRequestFlags_RestoreFocusedChild: typing.ClassVar[ImGuiFocusRequestFlags_]  # value = <ImGuiFocusRequestFlags_.ImGuiFocusRequestFlags_RestoreFocusedChild: 1>
    ImGuiFocusRequestFlags_UnlessBelowModal: typing.ClassVar[ImGuiFocusRequestFlags_]  # value = <ImGuiFocusRequestFlags_.ImGuiFocusRequestFlags_UnlessBelowModal: 2>
    __members__: typing.ClassVar[dict[str, ImGuiFocusRequestFlags_]]  # value = {'ImGuiFocusRequestFlags_None': <ImGuiFocusRequestFlags_.ImGuiFocusRequestFlags_None: 0>, 'ImGuiFocusRequestFlags_RestoreFocusedChild': <ImGuiFocusRequestFlags_.ImGuiFocusRequestFlags_RestoreFocusedChild: 1>, 'ImGuiFocusRequestFlags_UnlessBelowModal': <ImGuiFocusRequestFlags_.ImGuiFocusRequestFlags_UnlessBelowModal: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiFocusScopeData:
    ID: int
    WindowID: int
class ImGuiFocusedFlags_:
    """
    Members:
    
      ImGuiFocusedFlags_None
    
      ImGuiFocusedFlags_ChildWindows
    
      ImGuiFocusedFlags_RootWindow
    
      ImGuiFocusedFlags_AnyWindow
    
      ImGuiFocusedFlags_NoPopupHierarchy
    
      ImGuiFocusedFlags_DockHierarchy
    
      ImGuiFocusedFlags_RootAndChildWindows
    """
    ImGuiFocusedFlags_AnyWindow: typing.ClassVar[ImGuiFocusedFlags_]  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_AnyWindow: 4>
    ImGuiFocusedFlags_ChildWindows: typing.ClassVar[ImGuiFocusedFlags_]  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_ChildWindows: 1>
    ImGuiFocusedFlags_DockHierarchy: typing.ClassVar[ImGuiFocusedFlags_]  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_DockHierarchy: 16>
    ImGuiFocusedFlags_NoPopupHierarchy: typing.ClassVar[ImGuiFocusedFlags_]  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_NoPopupHierarchy: 8>
    ImGuiFocusedFlags_None: typing.ClassVar[ImGuiFocusedFlags_]  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_None: 0>
    ImGuiFocusedFlags_RootAndChildWindows: typing.ClassVar[ImGuiFocusedFlags_]  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_RootAndChildWindows: 3>
    ImGuiFocusedFlags_RootWindow: typing.ClassVar[ImGuiFocusedFlags_]  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_RootWindow: 2>
    __members__: typing.ClassVar[dict[str, ImGuiFocusedFlags_]]  # value = {'ImGuiFocusedFlags_None': <ImGuiFocusedFlags_.ImGuiFocusedFlags_None: 0>, 'ImGuiFocusedFlags_ChildWindows': <ImGuiFocusedFlags_.ImGuiFocusedFlags_ChildWindows: 1>, 'ImGuiFocusedFlags_RootWindow': <ImGuiFocusedFlags_.ImGuiFocusedFlags_RootWindow: 2>, 'ImGuiFocusedFlags_AnyWindow': <ImGuiFocusedFlags_.ImGuiFocusedFlags_AnyWindow: 4>, 'ImGuiFocusedFlags_NoPopupHierarchy': <ImGuiFocusedFlags_.ImGuiFocusedFlags_NoPopupHierarchy: 8>, 'ImGuiFocusedFlags_DockHierarchy': <ImGuiFocusedFlags_.ImGuiFocusedFlags_DockHierarchy: 16>, 'ImGuiFocusedFlags_RootAndChildWindows': <ImGuiFocusedFlags_.ImGuiFocusedFlags_RootAndChildWindows: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiGroupData:
    BackupActiveIdIsAlive: int
    BackupActiveIdPreviousFrameIsAlive: bool
    BackupCurrLineSize: ImVec2
    BackupCurrLineTextBaseOffset: float
    BackupCursorMaxPos: ImVec2
    BackupCursorPos: ImVec2
    BackupCursorPosPrevLine: ImVec2
    BackupGroupOffset: ImVec1
    BackupHoveredIdIsAlive: bool
    BackupIndent: ImVec1
    BackupIsSameLine: bool
    EmitItem: bool
    WindowID: int
class ImGuiHoveredFlagsPrivate_:
    """
    Members:
    
      ImGuiHoveredFlags_DelayMask_
    
      ImGuiHoveredFlags_AllowedMaskForIsWindowHovered
    
      ImGuiHoveredFlags_AllowedMaskForIsItemHovered
    """
    ImGuiHoveredFlags_AllowedMaskForIsItemHovered: typing.ClassVar[ImGuiHoveredFlagsPrivate_]  # value = <ImGuiHoveredFlagsPrivate_.ImGuiHoveredFlags_AllowedMaskForIsItemHovered: 262048>
    ImGuiHoveredFlags_AllowedMaskForIsWindowHovered: typing.ClassVar[ImGuiHoveredFlagsPrivate_]  # value = <ImGuiHoveredFlagsPrivate_.ImGuiHoveredFlags_AllowedMaskForIsWindowHovered: 12479>
    ImGuiHoveredFlags_DelayMask_: typing.ClassVar[ImGuiHoveredFlagsPrivate_]  # value = <ImGuiHoveredFlagsPrivate_.ImGuiHoveredFlags_DelayMask_: 245760>
    __members__: typing.ClassVar[dict[str, ImGuiHoveredFlagsPrivate_]]  # value = {'ImGuiHoveredFlags_DelayMask_': <ImGuiHoveredFlagsPrivate_.ImGuiHoveredFlags_DelayMask_: 245760>, 'ImGuiHoveredFlags_AllowedMaskForIsWindowHovered': <ImGuiHoveredFlagsPrivate_.ImGuiHoveredFlags_AllowedMaskForIsWindowHovered: 12479>, 'ImGuiHoveredFlags_AllowedMaskForIsItemHovered': <ImGuiHoveredFlagsPrivate_.ImGuiHoveredFlags_AllowedMaskForIsItemHovered: 262048>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiHoveredFlags_:
    """
    Members:
    
      ImGuiHoveredFlags_None
    
      ImGuiHoveredFlags_ChildWindows
    
      ImGuiHoveredFlags_RootWindow
    
      ImGuiHoveredFlags_AnyWindow
    
      ImGuiHoveredFlags_NoPopupHierarchy
    
      ImGuiHoveredFlags_DockHierarchy
    
      ImGuiHoveredFlags_AllowWhenBlockedByPopup
    
      ImGuiHoveredFlags_AllowWhenBlockedByActiveItem
    
      ImGuiHoveredFlags_AllowWhenOverlappedByItem
    
      ImGuiHoveredFlags_AllowWhenOverlappedByWindow
    
      ImGuiHoveredFlags_AllowWhenDisabled
    
      ImGuiHoveredFlags_NoNavOverride
    
      ImGuiHoveredFlags_AllowWhenOverlapped
    
      ImGuiHoveredFlags_RectOnly
    
      ImGuiHoveredFlags_RootAndChildWindows
    
      ImGuiHoveredFlags_ForTooltip
    
      ImGuiHoveredFlags_Stationary
    
      ImGuiHoveredFlags_DelayNone
    
      ImGuiHoveredFlags_DelayShort
    
      ImGuiHoveredFlags_DelayNormal
    
      ImGuiHoveredFlags_NoSharedDelay
    """
    ImGuiHoveredFlags_AllowWhenBlockedByActiveItem: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenBlockedByActiveItem: 128>
    ImGuiHoveredFlags_AllowWhenBlockedByPopup: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenBlockedByPopup: 32>
    ImGuiHoveredFlags_AllowWhenDisabled: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenDisabled: 1024>
    ImGuiHoveredFlags_AllowWhenOverlapped: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenOverlapped: 768>
    ImGuiHoveredFlags_AllowWhenOverlappedByItem: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenOverlappedByItem: 256>
    ImGuiHoveredFlags_AllowWhenOverlappedByWindow: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenOverlappedByWindow: 512>
    ImGuiHoveredFlags_AnyWindow: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AnyWindow: 4>
    ImGuiHoveredFlags_ChildWindows: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_ChildWindows: 1>
    ImGuiHoveredFlags_DelayNone: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_DelayNone: 16384>
    ImGuiHoveredFlags_DelayNormal: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_DelayNormal: 65536>
    ImGuiHoveredFlags_DelayShort: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_DelayShort: 32768>
    ImGuiHoveredFlags_DockHierarchy: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_DockHierarchy: 16>
    ImGuiHoveredFlags_ForTooltip: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_ForTooltip: 4096>
    ImGuiHoveredFlags_NoNavOverride: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_NoNavOverride: 2048>
    ImGuiHoveredFlags_NoPopupHierarchy: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_NoPopupHierarchy: 8>
    ImGuiHoveredFlags_NoSharedDelay: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_NoSharedDelay: 131072>
    ImGuiHoveredFlags_None: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_None: 0>
    ImGuiHoveredFlags_RectOnly: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_RectOnly: 928>
    ImGuiHoveredFlags_RootAndChildWindows: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_RootAndChildWindows: 3>
    ImGuiHoveredFlags_RootWindow: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_RootWindow: 2>
    ImGuiHoveredFlags_Stationary: typing.ClassVar[ImGuiHoveredFlags_]  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_Stationary: 8192>
    __members__: typing.ClassVar[dict[str, ImGuiHoveredFlags_]]  # value = {'ImGuiHoveredFlags_None': <ImGuiHoveredFlags_.ImGuiHoveredFlags_None: 0>, 'ImGuiHoveredFlags_ChildWindows': <ImGuiHoveredFlags_.ImGuiHoveredFlags_ChildWindows: 1>, 'ImGuiHoveredFlags_RootWindow': <ImGuiHoveredFlags_.ImGuiHoveredFlags_RootWindow: 2>, 'ImGuiHoveredFlags_AnyWindow': <ImGuiHoveredFlags_.ImGuiHoveredFlags_AnyWindow: 4>, 'ImGuiHoveredFlags_NoPopupHierarchy': <ImGuiHoveredFlags_.ImGuiHoveredFlags_NoPopupHierarchy: 8>, 'ImGuiHoveredFlags_DockHierarchy': <ImGuiHoveredFlags_.ImGuiHoveredFlags_DockHierarchy: 16>, 'ImGuiHoveredFlags_AllowWhenBlockedByPopup': <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenBlockedByPopup: 32>, 'ImGuiHoveredFlags_AllowWhenBlockedByActiveItem': <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenBlockedByActiveItem: 128>, 'ImGuiHoveredFlags_AllowWhenOverlappedByItem': <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenOverlappedByItem: 256>, 'ImGuiHoveredFlags_AllowWhenOverlappedByWindow': <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenOverlappedByWindow: 512>, 'ImGuiHoveredFlags_AllowWhenDisabled': <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenDisabled: 1024>, 'ImGuiHoveredFlags_NoNavOverride': <ImGuiHoveredFlags_.ImGuiHoveredFlags_NoNavOverride: 2048>, 'ImGuiHoveredFlags_AllowWhenOverlapped': <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenOverlapped: 768>, 'ImGuiHoveredFlags_RectOnly': <ImGuiHoveredFlags_.ImGuiHoveredFlags_RectOnly: 928>, 'ImGuiHoveredFlags_RootAndChildWindows': <ImGuiHoveredFlags_.ImGuiHoveredFlags_RootAndChildWindows: 3>, 'ImGuiHoveredFlags_ForTooltip': <ImGuiHoveredFlags_.ImGuiHoveredFlags_ForTooltip: 4096>, 'ImGuiHoveredFlags_Stationary': <ImGuiHoveredFlags_.ImGuiHoveredFlags_Stationary: 8192>, 'ImGuiHoveredFlags_DelayNone': <ImGuiHoveredFlags_.ImGuiHoveredFlags_DelayNone: 16384>, 'ImGuiHoveredFlags_DelayShort': <ImGuiHoveredFlags_.ImGuiHoveredFlags_DelayShort: 32768>, 'ImGuiHoveredFlags_DelayNormal': <ImGuiHoveredFlags_.ImGuiHoveredFlags_DelayNormal: 65536>, 'ImGuiHoveredFlags_NoSharedDelay': <ImGuiHoveredFlags_.ImGuiHoveredFlags_NoSharedDelay: 131072>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiIDStackTool:
    CopyToClipboardLastTime: float
    CopyToClipboardOnCtrlC: bool
    LastActiveFrame: int
    QueryId: int
    Results: ImVector_ImGuiStackLevelInfo
    StackLevel: int
    def __init__(self) -> None:
        ...
class ImGuiIO:
    AppAcceptingEvents: bool
    AppFocusLost: bool
    BackendFlags: int
    BackendLanguageUserData: capsule
    BackendPlatformName: str
    BackendPlatformUserData: capsule
    BackendRendererName: str
    BackendRendererUserData: capsule
    BackendUsingLegacyKeyArrays: int
    BackendUsingLegacyNavInputArray: bool
    ClipboardUserData: capsule
    ConfigDebugBeginReturnValueLoop: bool
    ConfigDebugBeginReturnValueOnce: bool
    ConfigDebugIgnoreFocusLoss: bool
    ConfigDebugIniSettings: bool
    ConfigDebugIsDebuggerPresent: bool
    ConfigDockingAlwaysTabBar: bool
    ConfigDockingNoSplit: bool
    ConfigDockingTransparentPayload: bool
    ConfigDockingWithShift: bool
    ConfigDragClickToInputText: bool
    ConfigFlags: int
    ConfigInputTextCursorBlink: bool
    ConfigInputTextEnterKeepActive: bool
    ConfigInputTrickleEventQueue: bool
    ConfigMacOSXBehaviors: bool
    ConfigMemoryCompactTimer: float
    ConfigViewportsNoAutoMerge: bool
    ConfigViewportsNoDecoration: bool
    ConfigViewportsNoDefaultParent: bool
    ConfigViewportsNoTaskBarIcon: bool
    ConfigWindowsMoveFromTitleBarOnly: bool
    ConfigWindowsResizeFromEdges: bool
    Ctx: ImGuiContext
    DeltaTime: float
    DisplayFramebufferScale: ImVec2
    DisplaySize: ImVec2
    FontAllowUserScaling: bool
    FontDefault: ImFont
    FontGlobalScale: float
    Fonts: ImFontAtlas
    Framerate: float
    IniFilename: str
    IniSavingRate: float
    InputQueueCharacters: ImVector_ImWchar
    InputQueueSurrogate: int
    KeyAlt: bool
    KeyCtrl: bool
    KeyMods: int
    KeyRepeatDelay: float
    KeyRepeatRate: float
    KeyShift: bool
    KeySuper: bool
    LogFilename: str
    MetricsActiveWindows: int
    MetricsRenderIndices: int
    MetricsRenderVertices: int
    MetricsRenderWindows: int
    MouseCtrlLeftAsRightClick: bool
    MouseDelta: ImVec2
    MouseDoubleClickMaxDist: float
    MouseDoubleClickTime: float
    MouseDragThreshold: float
    MouseDrawCursor: bool
    MouseHoveredViewport: int
    MousePos: ImVec2
    MousePosPrev: ImVec2
    MouseSource: ImGuiMouseSource
    MouseWheel: float
    MouseWheelH: float
    MouseWheelRequestAxisSwap: bool
    NavActive: bool
    NavVisible: bool
    PenPressure: float
    PlatformLocaleDecimalPoint: int
    UserData: capsule
    WantCaptureKeyboard: bool
    WantCaptureMouse: bool
    WantCaptureMouseUnlessPopupClose: bool
    WantSaveIniSettings: bool
    WantSetMousePos: bool
    WantTextInput: bool
    def AddFocusEvent(self, focused: bool) -> None:
        ...
    def AddInputCharacter(self, c: int) -> None:
        ...
    def AddInputCharacterUTF16(self, c: int) -> None:
        ...
    def AddInputCharactersUTF8(self, str: str) -> None:
        ...
    def AddKeyAnalogEvent(self, key: ImGuiKey, down: bool, v: float) -> None:
        ...
    def AddKeyEvent(self, key: ImGuiKey, down: bool) -> None:
        ...
    def AddMouseButtonEvent(self, button: int, down: bool) -> None:
        ...
    def AddMousePosEvent(self, x: float, y: float) -> None:
        ...
    def AddMouseSourceEvent(self, source: ImGuiMouseSource) -> None:
        ...
    def AddMouseViewportEvent(self, id: int) -> None:
        ...
    def AddMouseWheelEvent(self, wheel_x: float, wheel_y: float) -> None:
        ...
    def ClearEventsQueue(self) -> None:
        ...
    def ClearInputKeys(self) -> None:
        ...
    def ClearInputMouse(self) -> None:
        ...
    def SetAppAcceptingEvents(self, accepting_events: bool) -> None:
        ...
    def SetKeyEventNativeData(self, key: ImGuiKey, native_keycode: int, native_scancode: int, native_legacy_index: int = -1) -> None:
        ...
    def __init__(self) -> None:
        ...
    @property
    def KeysData(self) -> Arr_ImGuiKeyData:
        ...
    @property
    def MouseClicked(self) -> Arr_bool:
        ...
    @property
    def MouseClickedCount(self) -> Arr_unsigned_short:
        ...
    @property
    def MouseClickedLastCount(self) -> Arr_unsigned_short:
        ...
    @property
    def MouseClickedPos(self) -> Arr_ImVec2:
        ...
    @property
    def MouseClickedTime(self) -> Arr_double:
        ...
    @property
    def MouseDoubleClicked(self) -> Arr_bool:
        ...
    @property
    def MouseDown(self) -> Arr_bool:
        ...
    @property
    def MouseDownDuration(self) -> Arr_float:
        ...
    @property
    def MouseDownDurationPrev(self) -> Arr_float:
        ...
    @property
    def MouseDownOwned(self) -> Arr_bool:
        ...
    @property
    def MouseDownOwnedUnlessPopupClose(self) -> Arr_bool:
        ...
    @property
    def MouseDragMaxDistanceAbs(self) -> Arr_ImVec2:
        ...
    @property
    def MouseDragMaxDistanceSqr(self) -> Arr_float:
        ...
    @property
    def MouseReleased(self) -> Arr_bool:
        ...
class ImGuiInputEvent:
    AddedByTestEngine: bool
    AppFocused: ImGuiInputEventAppFocused
    EventId: int
    Key: ImGuiInputEventKey
    MouseButton: ImGuiInputEventMouseButton
    MousePos: ImGuiInputEventMousePos
    MouseViewport: ImGuiInputEventMouseViewport
    MouseWheel: ImGuiInputEventMouseWheel
    Source: ImGuiInputSource
    Text: ImGuiInputEventText
    Type: ImGuiInputEventType
    def __init__(self) -> None:
        ...
class ImGuiInputEventAppFocused:
    Focused: bool
class ImGuiInputEventKey:
    AnalogValue: float
    Down: bool
    Key: ImGuiKey
class ImGuiInputEventMouseButton:
    Button: int
    Down: bool
    MouseSource: ImGuiMouseSource
class ImGuiInputEventMousePos:
    MouseSource: ImGuiMouseSource
    PosX: float
    PosY: float
class ImGuiInputEventMouseViewport:
    HoveredViewportID: int
class ImGuiInputEventMouseWheel:
    MouseSource: ImGuiMouseSource
    WheelX: float
    WheelY: float
class ImGuiInputEventText:
    Char: int
class ImGuiInputEventType:
    """
    Members:
    
      ImGuiInputEventType_None
    
      ImGuiInputEventType_MousePos
    
      ImGuiInputEventType_MouseWheel
    
      ImGuiInputEventType_MouseButton
    
      ImGuiInputEventType_MouseViewport
    
      ImGuiInputEventType_Key
    
      ImGuiInputEventType_Text
    
      ImGuiInputEventType_Focus
    
      ImGuiInputEventType_COUNT
    """
    ImGuiInputEventType_COUNT: typing.ClassVar[ImGuiInputEventType]  # value = <ImGuiInputEventType.ImGuiInputEventType_COUNT: 8>
    ImGuiInputEventType_Focus: typing.ClassVar[ImGuiInputEventType]  # value = <ImGuiInputEventType.ImGuiInputEventType_Focus: 7>
    ImGuiInputEventType_Key: typing.ClassVar[ImGuiInputEventType]  # value = <ImGuiInputEventType.ImGuiInputEventType_Key: 5>
    ImGuiInputEventType_MouseButton: typing.ClassVar[ImGuiInputEventType]  # value = <ImGuiInputEventType.ImGuiInputEventType_MouseButton: 3>
    ImGuiInputEventType_MousePos: typing.ClassVar[ImGuiInputEventType]  # value = <ImGuiInputEventType.ImGuiInputEventType_MousePos: 1>
    ImGuiInputEventType_MouseViewport: typing.ClassVar[ImGuiInputEventType]  # value = <ImGuiInputEventType.ImGuiInputEventType_MouseViewport: 4>
    ImGuiInputEventType_MouseWheel: typing.ClassVar[ImGuiInputEventType]  # value = <ImGuiInputEventType.ImGuiInputEventType_MouseWheel: 2>
    ImGuiInputEventType_None: typing.ClassVar[ImGuiInputEventType]  # value = <ImGuiInputEventType.ImGuiInputEventType_None: 0>
    ImGuiInputEventType_Text: typing.ClassVar[ImGuiInputEventType]  # value = <ImGuiInputEventType.ImGuiInputEventType_Text: 6>
    __members__: typing.ClassVar[dict[str, ImGuiInputEventType]]  # value = {'ImGuiInputEventType_None': <ImGuiInputEventType.ImGuiInputEventType_None: 0>, 'ImGuiInputEventType_MousePos': <ImGuiInputEventType.ImGuiInputEventType_MousePos: 1>, 'ImGuiInputEventType_MouseWheel': <ImGuiInputEventType.ImGuiInputEventType_MouseWheel: 2>, 'ImGuiInputEventType_MouseButton': <ImGuiInputEventType.ImGuiInputEventType_MouseButton: 3>, 'ImGuiInputEventType_MouseViewport': <ImGuiInputEventType.ImGuiInputEventType_MouseViewport: 4>, 'ImGuiInputEventType_Key': <ImGuiInputEventType.ImGuiInputEventType_Key: 5>, 'ImGuiInputEventType_Text': <ImGuiInputEventType.ImGuiInputEventType_Text: 6>, 'ImGuiInputEventType_Focus': <ImGuiInputEventType.ImGuiInputEventType_Focus: 7>, 'ImGuiInputEventType_COUNT': <ImGuiInputEventType.ImGuiInputEventType_COUNT: 8>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiInputFlagsPrivate_:
    """
    Members:
    
      ImGuiInputFlags_RepeatRateDefault
    
      ImGuiInputFlags_RepeatRateNavMove
    
      ImGuiInputFlags_RepeatRateNavTweak
    
      ImGuiInputFlags_RepeatUntilRelease
    
      ImGuiInputFlags_RepeatUntilKeyModsChange
    
      ImGuiInputFlags_RepeatUntilKeyModsChangeFromNone
    
      ImGuiInputFlags_RepeatUntilOtherKeyPress
    
      ImGuiInputFlags_LockThisFrame
    
      ImGuiInputFlags_LockUntilRelease
    
      ImGuiInputFlags_CondHovered
    
      ImGuiInputFlags_CondActive
    
      ImGuiInputFlags_CondDefault_
    
      ImGuiInputFlags_RepeatRateMask_
    
      ImGuiInputFlags_RepeatUntilMask_
    
      ImGuiInputFlags_RepeatMask_
    
      ImGuiInputFlags_CondMask_
    
      ImGuiInputFlags_RouteTypeMask_
    
      ImGuiInputFlags_RouteOptionsMask_
    
      ImGuiInputFlags_SupportedByIsKeyPressed
    
      ImGuiInputFlags_SupportedByIsMouseClicked
    
      ImGuiInputFlags_SupportedByShortcut
    
      ImGuiInputFlags_SupportedBySetNextItemShortcut
    
      ImGuiInputFlags_SupportedBySetKeyOwner
    
      ImGuiInputFlags_SupportedBySetItemKeyOwner
    """
    ImGuiInputFlags_CondActive: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_CondActive: 8388608>
    ImGuiInputFlags_CondDefault_: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_CondDefault_: 12582912>
    ImGuiInputFlags_CondHovered: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_CondHovered: 4194304>
    ImGuiInputFlags_CondMask_: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_CondDefault_: 12582912>
    ImGuiInputFlags_LockThisFrame: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_LockThisFrame: 1048576>
    ImGuiInputFlags_LockUntilRelease: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_LockUntilRelease: 2097152>
    ImGuiInputFlags_RepeatMask_: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatMask_: 255>
    ImGuiInputFlags_RepeatRateDefault: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatRateDefault: 2>
    ImGuiInputFlags_RepeatRateMask_: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatRateMask_: 14>
    ImGuiInputFlags_RepeatRateNavMove: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatRateNavMove: 4>
    ImGuiInputFlags_RepeatRateNavTweak: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatRateNavTweak: 8>
    ImGuiInputFlags_RepeatUntilKeyModsChange: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilKeyModsChange: 32>
    ImGuiInputFlags_RepeatUntilKeyModsChangeFromNone: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilKeyModsChangeFromNone: 64>
    ImGuiInputFlags_RepeatUntilMask_: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilMask_: 240>
    ImGuiInputFlags_RepeatUntilOtherKeyPress: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilOtherKeyPress: 128>
    ImGuiInputFlags_RepeatUntilRelease: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilRelease: 16>
    ImGuiInputFlags_RouteOptionsMask_: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RouteOptionsMask_: 245760>
    ImGuiInputFlags_RouteTypeMask_: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RouteTypeMask_: 15360>
    ImGuiInputFlags_SupportedByIsKeyPressed: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatMask_: 255>
    ImGuiInputFlags_SupportedByIsMouseClicked: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedByIsMouseClicked: 1>
    ImGuiInputFlags_SupportedBySetItemKeyOwner: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedBySetItemKeyOwner: 15728640>
    ImGuiInputFlags_SupportedBySetKeyOwner: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedBySetKeyOwner: 3145728>
    ImGuiInputFlags_SupportedBySetNextItemShortcut: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedBySetNextItemShortcut: 523519>
    ImGuiInputFlags_SupportedByShortcut: typing.ClassVar[ImGuiInputFlagsPrivate_]  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedByShortcut: 261375>
    __members__: typing.ClassVar[dict[str, ImGuiInputFlagsPrivate_]]  # value = {'ImGuiInputFlags_RepeatRateDefault': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatRateDefault: 2>, 'ImGuiInputFlags_RepeatRateNavMove': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatRateNavMove: 4>, 'ImGuiInputFlags_RepeatRateNavTweak': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatRateNavTweak: 8>, 'ImGuiInputFlags_RepeatUntilRelease': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilRelease: 16>, 'ImGuiInputFlags_RepeatUntilKeyModsChange': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilKeyModsChange: 32>, 'ImGuiInputFlags_RepeatUntilKeyModsChangeFromNone': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilKeyModsChangeFromNone: 64>, 'ImGuiInputFlags_RepeatUntilOtherKeyPress': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilOtherKeyPress: 128>, 'ImGuiInputFlags_LockThisFrame': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_LockThisFrame: 1048576>, 'ImGuiInputFlags_LockUntilRelease': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_LockUntilRelease: 2097152>, 'ImGuiInputFlags_CondHovered': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_CondHovered: 4194304>, 'ImGuiInputFlags_CondActive': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_CondActive: 8388608>, 'ImGuiInputFlags_CondDefault_': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_CondDefault_: 12582912>, 'ImGuiInputFlags_RepeatRateMask_': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatRateMask_: 14>, 'ImGuiInputFlags_RepeatUntilMask_': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilMask_: 240>, 'ImGuiInputFlags_RepeatMask_': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatMask_: 255>, 'ImGuiInputFlags_CondMask_': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_CondDefault_: 12582912>, 'ImGuiInputFlags_RouteTypeMask_': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RouteTypeMask_: 15360>, 'ImGuiInputFlags_RouteOptionsMask_': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RouteOptionsMask_: 245760>, 'ImGuiInputFlags_SupportedByIsKeyPressed': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatMask_: 255>, 'ImGuiInputFlags_SupportedByIsMouseClicked': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedByIsMouseClicked: 1>, 'ImGuiInputFlags_SupportedByShortcut': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedByShortcut: 261375>, 'ImGuiInputFlags_SupportedBySetNextItemShortcut': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedBySetNextItemShortcut: 523519>, 'ImGuiInputFlags_SupportedBySetKeyOwner': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedBySetKeyOwner: 3145728>, 'ImGuiInputFlags_SupportedBySetItemKeyOwner': <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedBySetItemKeyOwner: 15728640>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiInputFlags_:
    """
    Members:
    
      ImGuiInputFlags_None
    
      ImGuiInputFlags_Repeat
    
      ImGuiInputFlags_RouteActive
    
      ImGuiInputFlags_RouteFocused
    
      ImGuiInputFlags_RouteGlobal
    
      ImGuiInputFlags_RouteAlways
    
      ImGuiInputFlags_RouteOverFocused
    
      ImGuiInputFlags_RouteOverActive
    
      ImGuiInputFlags_RouteUnlessBgFocused
    
      ImGuiInputFlags_RouteFromRootWindow
    
      ImGuiInputFlags_Tooltip
    """
    ImGuiInputFlags_None: typing.ClassVar[ImGuiInputFlags_]  # value = <ImGuiInputFlags_.ImGuiInputFlags_None: 0>
    ImGuiInputFlags_Repeat: typing.ClassVar[ImGuiInputFlags_]  # value = <ImGuiInputFlags_.ImGuiInputFlags_Repeat: 1>
    ImGuiInputFlags_RouteActive: typing.ClassVar[ImGuiInputFlags_]  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteActive: 1024>
    ImGuiInputFlags_RouteAlways: typing.ClassVar[ImGuiInputFlags_]  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteAlways: 8192>
    ImGuiInputFlags_RouteFocused: typing.ClassVar[ImGuiInputFlags_]  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteFocused: 2048>
    ImGuiInputFlags_RouteFromRootWindow: typing.ClassVar[ImGuiInputFlags_]  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteFromRootWindow: 131072>
    ImGuiInputFlags_RouteGlobal: typing.ClassVar[ImGuiInputFlags_]  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteGlobal: 4096>
    ImGuiInputFlags_RouteOverActive: typing.ClassVar[ImGuiInputFlags_]  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteOverActive: 32768>
    ImGuiInputFlags_RouteOverFocused: typing.ClassVar[ImGuiInputFlags_]  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteOverFocused: 16384>
    ImGuiInputFlags_RouteUnlessBgFocused: typing.ClassVar[ImGuiInputFlags_]  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteUnlessBgFocused: 65536>
    ImGuiInputFlags_Tooltip: typing.ClassVar[ImGuiInputFlags_]  # value = <ImGuiInputFlags_.ImGuiInputFlags_Tooltip: 262144>
    __members__: typing.ClassVar[dict[str, ImGuiInputFlags_]]  # value = {'ImGuiInputFlags_None': <ImGuiInputFlags_.ImGuiInputFlags_None: 0>, 'ImGuiInputFlags_Repeat': <ImGuiInputFlags_.ImGuiInputFlags_Repeat: 1>, 'ImGuiInputFlags_RouteActive': <ImGuiInputFlags_.ImGuiInputFlags_RouteActive: 1024>, 'ImGuiInputFlags_RouteFocused': <ImGuiInputFlags_.ImGuiInputFlags_RouteFocused: 2048>, 'ImGuiInputFlags_RouteGlobal': <ImGuiInputFlags_.ImGuiInputFlags_RouteGlobal: 4096>, 'ImGuiInputFlags_RouteAlways': <ImGuiInputFlags_.ImGuiInputFlags_RouteAlways: 8192>, 'ImGuiInputFlags_RouteOverFocused': <ImGuiInputFlags_.ImGuiInputFlags_RouteOverFocused: 16384>, 'ImGuiInputFlags_RouteOverActive': <ImGuiInputFlags_.ImGuiInputFlags_RouteOverActive: 32768>, 'ImGuiInputFlags_RouteUnlessBgFocused': <ImGuiInputFlags_.ImGuiInputFlags_RouteUnlessBgFocused: 65536>, 'ImGuiInputFlags_RouteFromRootWindow': <ImGuiInputFlags_.ImGuiInputFlags_RouteFromRootWindow: 131072>, 'ImGuiInputFlags_Tooltip': <ImGuiInputFlags_.ImGuiInputFlags_Tooltip: 262144>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiInputSource:
    """
    Members:
    
      ImGuiInputSource_None
    
      ImGuiInputSource_Mouse
    
      ImGuiInputSource_Keyboard
    
      ImGuiInputSource_Gamepad
    
      ImGuiInputSource_COUNT
    """
    ImGuiInputSource_COUNT: typing.ClassVar[ImGuiInputSource]  # value = <ImGuiInputSource.ImGuiInputSource_COUNT: 4>
    ImGuiInputSource_Gamepad: typing.ClassVar[ImGuiInputSource]  # value = <ImGuiInputSource.ImGuiInputSource_Gamepad: 3>
    ImGuiInputSource_Keyboard: typing.ClassVar[ImGuiInputSource]  # value = <ImGuiInputSource.ImGuiInputSource_Keyboard: 2>
    ImGuiInputSource_Mouse: typing.ClassVar[ImGuiInputSource]  # value = <ImGuiInputSource.ImGuiInputSource_Mouse: 1>
    ImGuiInputSource_None: typing.ClassVar[ImGuiInputSource]  # value = <ImGuiInputSource.ImGuiInputSource_None: 0>
    __members__: typing.ClassVar[dict[str, ImGuiInputSource]]  # value = {'ImGuiInputSource_None': <ImGuiInputSource.ImGuiInputSource_None: 0>, 'ImGuiInputSource_Mouse': <ImGuiInputSource.ImGuiInputSource_Mouse: 1>, 'ImGuiInputSource_Keyboard': <ImGuiInputSource.ImGuiInputSource_Keyboard: 2>, 'ImGuiInputSource_Gamepad': <ImGuiInputSource.ImGuiInputSource_Gamepad: 3>, 'ImGuiInputSource_COUNT': <ImGuiInputSource.ImGuiInputSource_COUNT: 4>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiInputTextCallbackData:
    Buf: str
    BufDirty: bool
    BufSize: int
    BufTextLen: int
    Ctx: ImGuiContext
    CursorPos: int
    EventChar: int
    EventFlag: int
    EventKey: ImGuiKey
    Flags: int
    SelectionEnd: int
    SelectionStart: int
    UserData: capsule
    def ClearSelection(self) -> None:
        ...
    def DeleteChars(self, pos: int, bytes_count: int) -> None:
        ...
    def HasSelection(self) -> bool:
        ...
    def InsertChars(self, pos: int, text: str, text_end: str = 0) -> None:
        ...
    def SelectAll(self) -> None:
        ...
    def __init__(self) -> None:
        ...
class ImGuiInputTextDeactivatedState:
    ID: int
    TextA: ImVector_char
    def ClearFreeMemory(self) -> None:
        ...
    def __init__(self) -> None:
        ...
class ImGuiInputTextFlagsPrivate_:
    """
    Members:
    
      ImGuiInputTextFlags_Multiline
    
      ImGuiInputTextFlags_NoMarkEdited
    
      ImGuiInputTextFlags_MergedItem
    
      ImGuiInputTextFlags_LocalizeDecimalPoint
    """
    ImGuiInputTextFlags_LocalizeDecimalPoint: typing.ClassVar[ImGuiInputTextFlagsPrivate_]  # value = <ImGuiInputTextFlagsPrivate_.ImGuiInputTextFlags_LocalizeDecimalPoint: 536870912>
    ImGuiInputTextFlags_MergedItem: typing.ClassVar[ImGuiInputTextFlagsPrivate_]  # value = <ImGuiInputTextFlagsPrivate_.ImGuiInputTextFlags_MergedItem: 268435456>
    ImGuiInputTextFlags_Multiline: typing.ClassVar[ImGuiInputTextFlagsPrivate_]  # value = <ImGuiInputTextFlagsPrivate_.ImGuiInputTextFlags_Multiline: 67108864>
    ImGuiInputTextFlags_NoMarkEdited: typing.ClassVar[ImGuiInputTextFlagsPrivate_]  # value = <ImGuiInputTextFlagsPrivate_.ImGuiInputTextFlags_NoMarkEdited: 134217728>
    __members__: typing.ClassVar[dict[str, ImGuiInputTextFlagsPrivate_]]  # value = {'ImGuiInputTextFlags_Multiline': <ImGuiInputTextFlagsPrivate_.ImGuiInputTextFlags_Multiline: 67108864>, 'ImGuiInputTextFlags_NoMarkEdited': <ImGuiInputTextFlagsPrivate_.ImGuiInputTextFlags_NoMarkEdited: 134217728>, 'ImGuiInputTextFlags_MergedItem': <ImGuiInputTextFlagsPrivate_.ImGuiInputTextFlags_MergedItem: 268435456>, 'ImGuiInputTextFlags_LocalizeDecimalPoint': <ImGuiInputTextFlagsPrivate_.ImGuiInputTextFlags_LocalizeDecimalPoint: 536870912>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiInputTextFlags_:
    """
    Members:
    
      ImGuiInputTextFlags_None
    
      ImGuiInputTextFlags_CharsDecimal
    
      ImGuiInputTextFlags_CharsHexadecimal
    
      ImGuiInputTextFlags_CharsScientific
    
      ImGuiInputTextFlags_CharsUppercase
    
      ImGuiInputTextFlags_CharsNoBlank
    
      ImGuiInputTextFlags_AllowTabInput
    
      ImGuiInputTextFlags_EnterReturnsTrue
    
      ImGuiInputTextFlags_EscapeClearsAll
    
      ImGuiInputTextFlags_CtrlEnterForNewLine
    
      ImGuiInputTextFlags_ReadOnly
    
      ImGuiInputTextFlags_Password
    
      ImGuiInputTextFlags_AlwaysOverwrite
    
      ImGuiInputTextFlags_AutoSelectAll
    
      ImGuiInputTextFlags_ParseEmptyRefVal
    
      ImGuiInputTextFlags_DisplayEmptyRefVal
    
      ImGuiInputTextFlags_NoHorizontalScroll
    
      ImGuiInputTextFlags_NoUndoRedo
    
      ImGuiInputTextFlags_CallbackCompletion
    
      ImGuiInputTextFlags_CallbackHistory
    
      ImGuiInputTextFlags_CallbackAlways
    
      ImGuiInputTextFlags_CallbackCharFilter
    
      ImGuiInputTextFlags_CallbackResize
    
      ImGuiInputTextFlags_CallbackEdit
    """
    ImGuiInputTextFlags_AllowTabInput: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_AllowTabInput: 32>
    ImGuiInputTextFlags_AlwaysOverwrite: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_AlwaysOverwrite: 2048>
    ImGuiInputTextFlags_AutoSelectAll: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_AutoSelectAll: 4096>
    ImGuiInputTextFlags_CallbackAlways: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackAlways: 524288>
    ImGuiInputTextFlags_CallbackCharFilter: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackCharFilter: 1048576>
    ImGuiInputTextFlags_CallbackCompletion: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackCompletion: 131072>
    ImGuiInputTextFlags_CallbackEdit: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackEdit: 4194304>
    ImGuiInputTextFlags_CallbackHistory: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackHistory: 262144>
    ImGuiInputTextFlags_CallbackResize: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackResize: 2097152>
    ImGuiInputTextFlags_CharsDecimal: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsDecimal: 1>
    ImGuiInputTextFlags_CharsHexadecimal: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsHexadecimal: 2>
    ImGuiInputTextFlags_CharsNoBlank: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsNoBlank: 16>
    ImGuiInputTextFlags_CharsScientific: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsScientific: 4>
    ImGuiInputTextFlags_CharsUppercase: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsUppercase: 8>
    ImGuiInputTextFlags_CtrlEnterForNewLine: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CtrlEnterForNewLine: 256>
    ImGuiInputTextFlags_DisplayEmptyRefVal: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_DisplayEmptyRefVal: 16384>
    ImGuiInputTextFlags_EnterReturnsTrue: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_EnterReturnsTrue: 64>
    ImGuiInputTextFlags_EscapeClearsAll: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_EscapeClearsAll: 128>
    ImGuiInputTextFlags_NoHorizontalScroll: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_NoHorizontalScroll: 32768>
    ImGuiInputTextFlags_NoUndoRedo: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_NoUndoRedo: 65536>
    ImGuiInputTextFlags_None: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_None: 0>
    ImGuiInputTextFlags_ParseEmptyRefVal: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_ParseEmptyRefVal: 8192>
    ImGuiInputTextFlags_Password: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_Password: 1024>
    ImGuiInputTextFlags_ReadOnly: typing.ClassVar[ImGuiInputTextFlags_]  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_ReadOnly: 512>
    __members__: typing.ClassVar[dict[str, ImGuiInputTextFlags_]]  # value = {'ImGuiInputTextFlags_None': <ImGuiInputTextFlags_.ImGuiInputTextFlags_None: 0>, 'ImGuiInputTextFlags_CharsDecimal': <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsDecimal: 1>, 'ImGuiInputTextFlags_CharsHexadecimal': <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsHexadecimal: 2>, 'ImGuiInputTextFlags_CharsScientific': <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsScientific: 4>, 'ImGuiInputTextFlags_CharsUppercase': <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsUppercase: 8>, 'ImGuiInputTextFlags_CharsNoBlank': <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsNoBlank: 16>, 'ImGuiInputTextFlags_AllowTabInput': <ImGuiInputTextFlags_.ImGuiInputTextFlags_AllowTabInput: 32>, 'ImGuiInputTextFlags_EnterReturnsTrue': <ImGuiInputTextFlags_.ImGuiInputTextFlags_EnterReturnsTrue: 64>, 'ImGuiInputTextFlags_EscapeClearsAll': <ImGuiInputTextFlags_.ImGuiInputTextFlags_EscapeClearsAll: 128>, 'ImGuiInputTextFlags_CtrlEnterForNewLine': <ImGuiInputTextFlags_.ImGuiInputTextFlags_CtrlEnterForNewLine: 256>, 'ImGuiInputTextFlags_ReadOnly': <ImGuiInputTextFlags_.ImGuiInputTextFlags_ReadOnly: 512>, 'ImGuiInputTextFlags_Password': <ImGuiInputTextFlags_.ImGuiInputTextFlags_Password: 1024>, 'ImGuiInputTextFlags_AlwaysOverwrite': <ImGuiInputTextFlags_.ImGuiInputTextFlags_AlwaysOverwrite: 2048>, 'ImGuiInputTextFlags_AutoSelectAll': <ImGuiInputTextFlags_.ImGuiInputTextFlags_AutoSelectAll: 4096>, 'ImGuiInputTextFlags_ParseEmptyRefVal': <ImGuiInputTextFlags_.ImGuiInputTextFlags_ParseEmptyRefVal: 8192>, 'ImGuiInputTextFlags_DisplayEmptyRefVal': <ImGuiInputTextFlags_.ImGuiInputTextFlags_DisplayEmptyRefVal: 16384>, 'ImGuiInputTextFlags_NoHorizontalScroll': <ImGuiInputTextFlags_.ImGuiInputTextFlags_NoHorizontalScroll: 32768>, 'ImGuiInputTextFlags_NoUndoRedo': <ImGuiInputTextFlags_.ImGuiInputTextFlags_NoUndoRedo: 65536>, 'ImGuiInputTextFlags_CallbackCompletion': <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackCompletion: 131072>, 'ImGuiInputTextFlags_CallbackHistory': <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackHistory: 262144>, 'ImGuiInputTextFlags_CallbackAlways': <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackAlways: 524288>, 'ImGuiInputTextFlags_CallbackCharFilter': <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackCharFilter: 1048576>, 'ImGuiInputTextFlags_CallbackResize': <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackResize: 2097152>, 'ImGuiInputTextFlags_CallbackEdit': <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackEdit: 4194304>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiInputTextState:
    BufCapacityA: int
    Ctx: ImGuiContext
    CurLenA: int
    CurLenW: int
    CursorAnim: float
    CursorFollow: bool
    Edited: bool
    Flags: int
    ID: int
    InitialTextA: ImVector_char
    ReloadSelectionEnd: int
    ReloadSelectionStart: int
    ReloadUserBuf: bool
    ScrollX: float
    SelectedAllMouseLock: bool
    Stb: STB_TexteditState
    TextA: ImVector_char
    TextAIsValid: bool
    TextW: ImVector_ImWchar
    def ClearFreeMemory(self) -> None:
        ...
    def ClearSelection(self) -> None:
        ...
    def ClearText(self) -> None:
        ...
    def CursorAnimReset(self) -> None:
        ...
    def CursorClamp(self) -> None:
        ...
    def GetCursorPos(self) -> int:
        ...
    def GetRedoAvailCount(self) -> int:
        ...
    def GetSelectionEnd(self) -> int:
        ...
    def GetSelectionStart(self) -> int:
        ...
    def GetUndoAvailCount(self) -> int:
        ...
    def HasSelection(self) -> bool:
        ...
    def OnKeyPressed(self, key: int) -> None:
        ...
    def ReloadUserBufAndKeepSelection(self) -> None:
        ...
    def ReloadUserBufAndMoveToEnd(self) -> None:
        ...
    def ReloadUserBufAndSelectAll(self) -> None:
        ...
    def SelectAll(self) -> None:
        ...
    def __init__(self) -> None:
        ...
class ImGuiItemFlags_:
    """
    Members:
    
      ImGuiItemFlags_None
    
      ImGuiItemFlags_NoTabStop
    
      ImGuiItemFlags_ButtonRepeat
    
      ImGuiItemFlags_Disabled
    
      ImGuiItemFlags_NoNav
    
      ImGuiItemFlags_NoNavDefaultFocus
    
      ImGuiItemFlags_SelectableDontClosePopup
    
      ImGuiItemFlags_MixedValue
    
      ImGuiItemFlags_ReadOnly
    
      ImGuiItemFlags_NoWindowHoverableCheck
    
      ImGuiItemFlags_AllowOverlap
    
      ImGuiItemFlags_Inputable
    
      ImGuiItemFlags_HasSelectionUserData
    """
    ImGuiItemFlags_AllowOverlap: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_AllowOverlap: 512>
    ImGuiItemFlags_ButtonRepeat: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_ButtonRepeat: 2>
    ImGuiItemFlags_Disabled: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_Disabled: 4>
    ImGuiItemFlags_HasSelectionUserData: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_HasSelectionUserData: 2048>
    ImGuiItemFlags_Inputable: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_Inputable: 1024>
    ImGuiItemFlags_MixedValue: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_MixedValue: 64>
    ImGuiItemFlags_NoNav: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_NoNav: 8>
    ImGuiItemFlags_NoNavDefaultFocus: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_NoNavDefaultFocus: 16>
    ImGuiItemFlags_NoTabStop: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_NoTabStop: 1>
    ImGuiItemFlags_NoWindowHoverableCheck: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_NoWindowHoverableCheck: 256>
    ImGuiItemFlags_None: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_None: 0>
    ImGuiItemFlags_ReadOnly: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_ReadOnly: 128>
    ImGuiItemFlags_SelectableDontClosePopup: typing.ClassVar[ImGuiItemFlags_]  # value = <ImGuiItemFlags_.ImGuiItemFlags_SelectableDontClosePopup: 32>
    __members__: typing.ClassVar[dict[str, ImGuiItemFlags_]]  # value = {'ImGuiItemFlags_None': <ImGuiItemFlags_.ImGuiItemFlags_None: 0>, 'ImGuiItemFlags_NoTabStop': <ImGuiItemFlags_.ImGuiItemFlags_NoTabStop: 1>, 'ImGuiItemFlags_ButtonRepeat': <ImGuiItemFlags_.ImGuiItemFlags_ButtonRepeat: 2>, 'ImGuiItemFlags_Disabled': <ImGuiItemFlags_.ImGuiItemFlags_Disabled: 4>, 'ImGuiItemFlags_NoNav': <ImGuiItemFlags_.ImGuiItemFlags_NoNav: 8>, 'ImGuiItemFlags_NoNavDefaultFocus': <ImGuiItemFlags_.ImGuiItemFlags_NoNavDefaultFocus: 16>, 'ImGuiItemFlags_SelectableDontClosePopup': <ImGuiItemFlags_.ImGuiItemFlags_SelectableDontClosePopup: 32>, 'ImGuiItemFlags_MixedValue': <ImGuiItemFlags_.ImGuiItemFlags_MixedValue: 64>, 'ImGuiItemFlags_ReadOnly': <ImGuiItemFlags_.ImGuiItemFlags_ReadOnly: 128>, 'ImGuiItemFlags_NoWindowHoverableCheck': <ImGuiItemFlags_.ImGuiItemFlags_NoWindowHoverableCheck: 256>, 'ImGuiItemFlags_AllowOverlap': <ImGuiItemFlags_.ImGuiItemFlags_AllowOverlap: 512>, 'ImGuiItemFlags_Inputable': <ImGuiItemFlags_.ImGuiItemFlags_Inputable: 1024>, 'ImGuiItemFlags_HasSelectionUserData': <ImGuiItemFlags_.ImGuiItemFlags_HasSelectionUserData: 2048>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiItemStatusFlags_:
    """
    Members:
    
      ImGuiItemStatusFlags_None
    
      ImGuiItemStatusFlags_HoveredRect
    
      ImGuiItemStatusFlags_HasDisplayRect
    
      ImGuiItemStatusFlags_Edited
    
      ImGuiItemStatusFlags_ToggledSelection
    
      ImGuiItemStatusFlags_ToggledOpen
    
      ImGuiItemStatusFlags_HasDeactivated
    
      ImGuiItemStatusFlags_Deactivated
    
      ImGuiItemStatusFlags_HoveredWindow
    
      ImGuiItemStatusFlags_Visible
    
      ImGuiItemStatusFlags_HasClipRect
    
      ImGuiItemStatusFlags_HasShortcut
    """
    ImGuiItemStatusFlags_Deactivated: typing.ClassVar[ImGuiItemStatusFlags_]  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_Deactivated: 64>
    ImGuiItemStatusFlags_Edited: typing.ClassVar[ImGuiItemStatusFlags_]  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_Edited: 4>
    ImGuiItemStatusFlags_HasClipRect: typing.ClassVar[ImGuiItemStatusFlags_]  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HasClipRect: 512>
    ImGuiItemStatusFlags_HasDeactivated: typing.ClassVar[ImGuiItemStatusFlags_]  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HasDeactivated: 32>
    ImGuiItemStatusFlags_HasDisplayRect: typing.ClassVar[ImGuiItemStatusFlags_]  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HasDisplayRect: 2>
    ImGuiItemStatusFlags_HasShortcut: typing.ClassVar[ImGuiItemStatusFlags_]  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HasShortcut: 1024>
    ImGuiItemStatusFlags_HoveredRect: typing.ClassVar[ImGuiItemStatusFlags_]  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HoveredRect: 1>
    ImGuiItemStatusFlags_HoveredWindow: typing.ClassVar[ImGuiItemStatusFlags_]  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HoveredWindow: 128>
    ImGuiItemStatusFlags_None: typing.ClassVar[ImGuiItemStatusFlags_]  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_None: 0>
    ImGuiItemStatusFlags_ToggledOpen: typing.ClassVar[ImGuiItemStatusFlags_]  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_ToggledOpen: 16>
    ImGuiItemStatusFlags_ToggledSelection: typing.ClassVar[ImGuiItemStatusFlags_]  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_ToggledSelection: 8>
    ImGuiItemStatusFlags_Visible: typing.ClassVar[ImGuiItemStatusFlags_]  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_Visible: 256>
    __members__: typing.ClassVar[dict[str, ImGuiItemStatusFlags_]]  # value = {'ImGuiItemStatusFlags_None': <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_None: 0>, 'ImGuiItemStatusFlags_HoveredRect': <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HoveredRect: 1>, 'ImGuiItemStatusFlags_HasDisplayRect': <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HasDisplayRect: 2>, 'ImGuiItemStatusFlags_Edited': <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_Edited: 4>, 'ImGuiItemStatusFlags_ToggledSelection': <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_ToggledSelection: 8>, 'ImGuiItemStatusFlags_ToggledOpen': <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_ToggledOpen: 16>, 'ImGuiItemStatusFlags_HasDeactivated': <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HasDeactivated: 32>, 'ImGuiItemStatusFlags_Deactivated': <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_Deactivated: 64>, 'ImGuiItemStatusFlags_HoveredWindow': <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HoveredWindow: 128>, 'ImGuiItemStatusFlags_Visible': <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_Visible: 256>, 'ImGuiItemStatusFlags_HasClipRect': <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HasClipRect: 512>, 'ImGuiItemStatusFlags_HasShortcut': <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HasShortcut: 1024>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiKey:
    """
    Members:
    
      ImGuiKey_None
    
      ImGuiKey_Tab
    
      ImGuiKey_LeftArrow
    
      ImGuiKey_RightArrow
    
      ImGuiKey_UpArrow
    
      ImGuiKey_DownArrow
    
      ImGuiKey_PageUp
    
      ImGuiKey_PageDown
    
      ImGuiKey_Home
    
      ImGuiKey_End
    
      ImGuiKey_Insert
    
      ImGuiKey_Delete
    
      ImGuiKey_Backspace
    
      ImGuiKey_Space
    
      ImGuiKey_Enter
    
      ImGuiKey_Escape
    
      ImGuiKey_LeftCtrl
    
      ImGuiKey_LeftShift
    
      ImGuiKey_LeftAlt
    
      ImGuiKey_LeftSuper
    
      ImGuiKey_RightCtrl
    
      ImGuiKey_RightShift
    
      ImGuiKey_RightAlt
    
      ImGuiKey_RightSuper
    
      ImGuiKey_Menu
    
      ImGuiKey_0
    
      ImGuiKey_1
    
      ImGuiKey_2
    
      ImGuiKey_3
    
      ImGuiKey_4
    
      ImGuiKey_5
    
      ImGuiKey_6
    
      ImGuiKey_7
    
      ImGuiKey_8
    
      ImGuiKey_9
    
      ImGuiKey_A
    
      ImGuiKey_B
    
      ImGuiKey_C
    
      ImGuiKey_D
    
      ImGuiKey_E
    
      ImGuiKey_F
    
      ImGuiKey_G
    
      ImGuiKey_H
    
      ImGuiKey_I
    
      ImGuiKey_J
    
      ImGuiKey_K
    
      ImGuiKey_L
    
      ImGuiKey_M
    
      ImGuiKey_N
    
      ImGuiKey_O
    
      ImGuiKey_P
    
      ImGuiKey_Q
    
      ImGuiKey_R
    
      ImGuiKey_S
    
      ImGuiKey_T
    
      ImGuiKey_U
    
      ImGuiKey_V
    
      ImGuiKey_W
    
      ImGuiKey_X
    
      ImGuiKey_Y
    
      ImGuiKey_Z
    
      ImGuiKey_F1
    
      ImGuiKey_F2
    
      ImGuiKey_F3
    
      ImGuiKey_F4
    
      ImGuiKey_F5
    
      ImGuiKey_F6
    
      ImGuiKey_F7
    
      ImGuiKey_F8
    
      ImGuiKey_F9
    
      ImGuiKey_F10
    
      ImGuiKey_F11
    
      ImGuiKey_F12
    
      ImGuiKey_F13
    
      ImGuiKey_F14
    
      ImGuiKey_F15
    
      ImGuiKey_F16
    
      ImGuiKey_F17
    
      ImGuiKey_F18
    
      ImGuiKey_F19
    
      ImGuiKey_F20
    
      ImGuiKey_F21
    
      ImGuiKey_F22
    
      ImGuiKey_F23
    
      ImGuiKey_F24
    
      ImGuiKey_Apostrophe
    
      ImGuiKey_Comma
    
      ImGuiKey_Minus
    
      ImGuiKey_Period
    
      ImGuiKey_Slash
    
      ImGuiKey_Semicolon
    
      ImGuiKey_Equal
    
      ImGuiKey_LeftBracket
    
      ImGuiKey_Backslash
    
      ImGuiKey_RightBracket
    
      ImGuiKey_GraveAccent
    
      ImGuiKey_CapsLock
    
      ImGuiKey_ScrollLock
    
      ImGuiKey_NumLock
    
      ImGuiKey_PrintScreen
    
      ImGuiKey_Pause
    
      ImGuiKey_Keypad0
    
      ImGuiKey_Keypad1
    
      ImGuiKey_Keypad2
    
      ImGuiKey_Keypad3
    
      ImGuiKey_Keypad4
    
      ImGuiKey_Keypad5
    
      ImGuiKey_Keypad6
    
      ImGuiKey_Keypad7
    
      ImGuiKey_Keypad8
    
      ImGuiKey_Keypad9
    
      ImGuiKey_KeypadDecimal
    
      ImGuiKey_KeypadDivide
    
      ImGuiKey_KeypadMultiply
    
      ImGuiKey_KeypadSubtract
    
      ImGuiKey_KeypadAdd
    
      ImGuiKey_KeypadEnter
    
      ImGuiKey_KeypadEqual
    
      ImGuiKey_AppBack
    
      ImGuiKey_AppForward
    
      ImGuiKey_GamepadStart
    
      ImGuiKey_GamepadBack
    
      ImGuiKey_GamepadFaceLeft
    
      ImGuiKey_GamepadFaceRight
    
      ImGuiKey_GamepadFaceUp
    
      ImGuiKey_GamepadFaceDown
    
      ImGuiKey_GamepadDpadLeft
    
      ImGuiKey_GamepadDpadRight
    
      ImGuiKey_GamepadDpadUp
    
      ImGuiKey_GamepadDpadDown
    
      ImGuiKey_GamepadL1
    
      ImGuiKey_GamepadR1
    
      ImGuiKey_GamepadL2
    
      ImGuiKey_GamepadR2
    
      ImGuiKey_GamepadL3
    
      ImGuiKey_GamepadR3
    
      ImGuiKey_GamepadLStickLeft
    
      ImGuiKey_GamepadLStickRight
    
      ImGuiKey_GamepadLStickUp
    
      ImGuiKey_GamepadLStickDown
    
      ImGuiKey_GamepadRStickLeft
    
      ImGuiKey_GamepadRStickRight
    
      ImGuiKey_GamepadRStickUp
    
      ImGuiKey_GamepadRStickDown
    
      ImGuiKey_MouseLeft
    
      ImGuiKey_MouseRight
    
      ImGuiKey_MouseMiddle
    
      ImGuiKey_MouseX1
    
      ImGuiKey_MouseX2
    
      ImGuiKey_MouseWheelX
    
      ImGuiKey_MouseWheelY
    
      ImGuiKey_ReservedForModCtrl
    
      ImGuiKey_ReservedForModShift
    
      ImGuiKey_ReservedForModAlt
    
      ImGuiKey_ReservedForModSuper
    
      ImGuiKey_COUNT
    
      ImGuiMod_None
    
      ImGuiMod_Ctrl
    
      ImGuiMod_Shift
    
      ImGuiMod_Alt
    
      ImGuiMod_Super
    
      ImGuiMod_Mask_
    
      ImGuiKey_NamedKey_BEGIN
    
      ImGuiKey_NamedKey_END
    
      ImGuiKey_NamedKey_COUNT
    
      ImGuiKey_KeysData_SIZE
    
      ImGuiKey_KeysData_OFFSET
    """
    ImGuiKey_0: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_0: 536>
    ImGuiKey_1: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_1: 537>
    ImGuiKey_2: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_2: 538>
    ImGuiKey_3: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_3: 539>
    ImGuiKey_4: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_4: 540>
    ImGuiKey_5: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_5: 541>
    ImGuiKey_6: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_6: 542>
    ImGuiKey_7: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_7: 543>
    ImGuiKey_8: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_8: 544>
    ImGuiKey_9: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_9: 545>
    ImGuiKey_A: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_A: 546>
    ImGuiKey_Apostrophe: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Apostrophe: 596>
    ImGuiKey_AppBack: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_AppBack: 629>
    ImGuiKey_AppForward: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_AppForward: 630>
    ImGuiKey_B: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_B: 547>
    ImGuiKey_Backslash: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Backslash: 604>
    ImGuiKey_Backspace: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Backspace: 523>
    ImGuiKey_C: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_C: 548>
    ImGuiKey_COUNT: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_COUNT: 666>
    ImGuiKey_CapsLock: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_CapsLock: 607>
    ImGuiKey_Comma: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Comma: 597>
    ImGuiKey_D: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_D: 549>
    ImGuiKey_Delete: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Delete: 522>
    ImGuiKey_DownArrow: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_DownArrow: 516>
    ImGuiKey_E: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_E: 550>
    ImGuiKey_End: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_End: 520>
    ImGuiKey_Enter: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Enter: 525>
    ImGuiKey_Equal: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Equal: 602>
    ImGuiKey_Escape: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Escape: 526>
    ImGuiKey_F: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F: 551>
    ImGuiKey_F1: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F1: 572>
    ImGuiKey_F10: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F10: 581>
    ImGuiKey_F11: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F11: 582>
    ImGuiKey_F12: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F12: 583>
    ImGuiKey_F13: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F13: 584>
    ImGuiKey_F14: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F14: 585>
    ImGuiKey_F15: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F15: 586>
    ImGuiKey_F16: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F16: 587>
    ImGuiKey_F17: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F17: 588>
    ImGuiKey_F18: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F18: 589>
    ImGuiKey_F19: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F19: 590>
    ImGuiKey_F2: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F2: 573>
    ImGuiKey_F20: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F20: 591>
    ImGuiKey_F21: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F21: 592>
    ImGuiKey_F22: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F22: 593>
    ImGuiKey_F23: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F23: 594>
    ImGuiKey_F24: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F24: 595>
    ImGuiKey_F3: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F3: 574>
    ImGuiKey_F4: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F4: 575>
    ImGuiKey_F5: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F5: 576>
    ImGuiKey_F6: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F6: 577>
    ImGuiKey_F7: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F7: 578>
    ImGuiKey_F8: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F8: 579>
    ImGuiKey_F9: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_F9: 580>
    ImGuiKey_G: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_G: 552>
    ImGuiKey_GamepadBack: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadBack: 632>
    ImGuiKey_GamepadDpadDown: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadDpadDown: 640>
    ImGuiKey_GamepadDpadLeft: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadDpadLeft: 637>
    ImGuiKey_GamepadDpadRight: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadDpadRight: 638>
    ImGuiKey_GamepadDpadUp: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadDpadUp: 639>
    ImGuiKey_GamepadFaceDown: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadFaceDown: 636>
    ImGuiKey_GamepadFaceLeft: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadFaceLeft: 633>
    ImGuiKey_GamepadFaceRight: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadFaceRight: 634>
    ImGuiKey_GamepadFaceUp: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadFaceUp: 635>
    ImGuiKey_GamepadL1: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadL1: 641>
    ImGuiKey_GamepadL2: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadL2: 643>
    ImGuiKey_GamepadL3: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadL3: 645>
    ImGuiKey_GamepadLStickDown: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadLStickDown: 650>
    ImGuiKey_GamepadLStickLeft: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadLStickLeft: 647>
    ImGuiKey_GamepadLStickRight: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadLStickRight: 648>
    ImGuiKey_GamepadLStickUp: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadLStickUp: 649>
    ImGuiKey_GamepadR1: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadR1: 642>
    ImGuiKey_GamepadR2: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadR2: 644>
    ImGuiKey_GamepadR3: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadR3: 646>
    ImGuiKey_GamepadRStickDown: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadRStickDown: 654>
    ImGuiKey_GamepadRStickLeft: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadRStickLeft: 651>
    ImGuiKey_GamepadRStickRight: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadRStickRight: 652>
    ImGuiKey_GamepadRStickUp: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadRStickUp: 653>
    ImGuiKey_GamepadStart: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GamepadStart: 631>
    ImGuiKey_GraveAccent: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_GraveAccent: 606>
    ImGuiKey_H: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_H: 553>
    ImGuiKey_Home: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Home: 519>
    ImGuiKey_I: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_I: 554>
    ImGuiKey_Insert: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Insert: 521>
    ImGuiKey_J: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_J: 555>
    ImGuiKey_K: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_K: 556>
    ImGuiKey_Keypad0: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Keypad0: 612>
    ImGuiKey_Keypad1: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Keypad1: 613>
    ImGuiKey_Keypad2: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Keypad2: 614>
    ImGuiKey_Keypad3: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Keypad3: 615>
    ImGuiKey_Keypad4: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Keypad4: 616>
    ImGuiKey_Keypad5: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Keypad5: 617>
    ImGuiKey_Keypad6: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Keypad6: 618>
    ImGuiKey_Keypad7: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Keypad7: 619>
    ImGuiKey_Keypad8: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Keypad8: 620>
    ImGuiKey_Keypad9: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Keypad9: 621>
    ImGuiKey_KeypadAdd: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_KeypadAdd: 626>
    ImGuiKey_KeypadDecimal: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_KeypadDecimal: 622>
    ImGuiKey_KeypadDivide: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_KeypadDivide: 623>
    ImGuiKey_KeypadEnter: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_KeypadEnter: 627>
    ImGuiKey_KeypadEqual: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_KeypadEqual: 628>
    ImGuiKey_KeypadMultiply: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_KeypadMultiply: 624>
    ImGuiKey_KeypadSubtract: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_KeypadSubtract: 625>
    ImGuiKey_KeysData_OFFSET: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Tab: 512>
    ImGuiKey_KeysData_SIZE: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_NamedKey_COUNT: 154>
    ImGuiKey_L: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_L: 557>
    ImGuiKey_LeftAlt: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_LeftAlt: 529>
    ImGuiKey_LeftArrow: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_LeftArrow: 513>
    ImGuiKey_LeftBracket: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_LeftBracket: 603>
    ImGuiKey_LeftCtrl: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_LeftCtrl: 527>
    ImGuiKey_LeftShift: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_LeftShift: 528>
    ImGuiKey_LeftSuper: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_LeftSuper: 530>
    ImGuiKey_M: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_M: 558>
    ImGuiKey_Menu: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Menu: 535>
    ImGuiKey_Minus: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Minus: 598>
    ImGuiKey_MouseLeft: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_MouseLeft: 655>
    ImGuiKey_MouseMiddle: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_MouseMiddle: 657>
    ImGuiKey_MouseRight: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_MouseRight: 656>
    ImGuiKey_MouseWheelX: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_MouseWheelX: 660>
    ImGuiKey_MouseWheelY: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_MouseWheelY: 661>
    ImGuiKey_MouseX1: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_MouseX1: 658>
    ImGuiKey_MouseX2: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_MouseX2: 659>
    ImGuiKey_N: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_N: 559>
    ImGuiKey_NamedKey_BEGIN: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Tab: 512>
    ImGuiKey_NamedKey_COUNT: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_NamedKey_COUNT: 154>
    ImGuiKey_NamedKey_END: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_COUNT: 666>
    ImGuiKey_None: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_None: 0>
    ImGuiKey_NumLock: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_NumLock: 609>
    ImGuiKey_O: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_O: 560>
    ImGuiKey_P: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_P: 561>
    ImGuiKey_PageDown: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_PageDown: 518>
    ImGuiKey_PageUp: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_PageUp: 517>
    ImGuiKey_Pause: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Pause: 611>
    ImGuiKey_Period: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Period: 599>
    ImGuiKey_PrintScreen: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_PrintScreen: 610>
    ImGuiKey_Q: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Q: 562>
    ImGuiKey_R: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_R: 563>
    ImGuiKey_ReservedForModAlt: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_ReservedForModAlt: 664>
    ImGuiKey_ReservedForModCtrl: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_ReservedForModCtrl: 662>
    ImGuiKey_ReservedForModShift: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_ReservedForModShift: 663>
    ImGuiKey_ReservedForModSuper: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_ReservedForModSuper: 665>
    ImGuiKey_RightAlt: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_RightAlt: 533>
    ImGuiKey_RightArrow: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_RightArrow: 514>
    ImGuiKey_RightBracket: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_RightBracket: 605>
    ImGuiKey_RightCtrl: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_RightCtrl: 531>
    ImGuiKey_RightShift: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_RightShift: 532>
    ImGuiKey_RightSuper: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_RightSuper: 534>
    ImGuiKey_S: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_S: 564>
    ImGuiKey_ScrollLock: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_ScrollLock: 608>
    ImGuiKey_Semicolon: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Semicolon: 601>
    ImGuiKey_Slash: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Slash: 600>
    ImGuiKey_Space: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Space: 524>
    ImGuiKey_T: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_T: 565>
    ImGuiKey_Tab: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Tab: 512>
    ImGuiKey_U: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_U: 566>
    ImGuiKey_UpArrow: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_UpArrow: 515>
    ImGuiKey_V: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_V: 567>
    ImGuiKey_W: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_W: 568>
    ImGuiKey_X: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_X: 569>
    ImGuiKey_Y: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Y: 570>
    ImGuiKey_Z: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_Z: 571>
    ImGuiMod_Alt: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiMod_Alt: 16384>
    ImGuiMod_Ctrl: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiMod_Ctrl: 4096>
    ImGuiMod_Mask_: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiMod_Mask_: 61440>
    ImGuiMod_None: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiKey_None: 0>
    ImGuiMod_Shift: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiMod_Shift: 8192>
    ImGuiMod_Super: typing.ClassVar[ImGuiKey]  # value = <ImGuiKey.ImGuiMod_Super: 32768>
    __members__: typing.ClassVar[dict[str, ImGuiKey]]  # value = {'ImGuiKey_None': <ImGuiKey.ImGuiKey_None: 0>, 'ImGuiKey_Tab': <ImGuiKey.ImGuiKey_Tab: 512>, 'ImGuiKey_LeftArrow': <ImGuiKey.ImGuiKey_LeftArrow: 513>, 'ImGuiKey_RightArrow': <ImGuiKey.ImGuiKey_RightArrow: 514>, 'ImGuiKey_UpArrow': <ImGuiKey.ImGuiKey_UpArrow: 515>, 'ImGuiKey_DownArrow': <ImGuiKey.ImGuiKey_DownArrow: 516>, 'ImGuiKey_PageUp': <ImGuiKey.ImGuiKey_PageUp: 517>, 'ImGuiKey_PageDown': <ImGuiKey.ImGuiKey_PageDown: 518>, 'ImGuiKey_Home': <ImGuiKey.ImGuiKey_Home: 519>, 'ImGuiKey_End': <ImGuiKey.ImGuiKey_End: 520>, 'ImGuiKey_Insert': <ImGuiKey.ImGuiKey_Insert: 521>, 'ImGuiKey_Delete': <ImGuiKey.ImGuiKey_Delete: 522>, 'ImGuiKey_Backspace': <ImGuiKey.ImGuiKey_Backspace: 523>, 'ImGuiKey_Space': <ImGuiKey.ImGuiKey_Space: 524>, 'ImGuiKey_Enter': <ImGuiKey.ImGuiKey_Enter: 525>, 'ImGuiKey_Escape': <ImGuiKey.ImGuiKey_Escape: 526>, 'ImGuiKey_LeftCtrl': <ImGuiKey.ImGuiKey_LeftCtrl: 527>, 'ImGuiKey_LeftShift': <ImGuiKey.ImGuiKey_LeftShift: 528>, 'ImGuiKey_LeftAlt': <ImGuiKey.ImGuiKey_LeftAlt: 529>, 'ImGuiKey_LeftSuper': <ImGuiKey.ImGuiKey_LeftSuper: 530>, 'ImGuiKey_RightCtrl': <ImGuiKey.ImGuiKey_RightCtrl: 531>, 'ImGuiKey_RightShift': <ImGuiKey.ImGuiKey_RightShift: 532>, 'ImGuiKey_RightAlt': <ImGuiKey.ImGuiKey_RightAlt: 533>, 'ImGuiKey_RightSuper': <ImGuiKey.ImGuiKey_RightSuper: 534>, 'ImGuiKey_Menu': <ImGuiKey.ImGuiKey_Menu: 535>, 'ImGuiKey_0': <ImGuiKey.ImGuiKey_0: 536>, 'ImGuiKey_1': <ImGuiKey.ImGuiKey_1: 537>, 'ImGuiKey_2': <ImGuiKey.ImGuiKey_2: 538>, 'ImGuiKey_3': <ImGuiKey.ImGuiKey_3: 539>, 'ImGuiKey_4': <ImGuiKey.ImGuiKey_4: 540>, 'ImGuiKey_5': <ImGuiKey.ImGuiKey_5: 541>, 'ImGuiKey_6': <ImGuiKey.ImGuiKey_6: 542>, 'ImGuiKey_7': <ImGuiKey.ImGuiKey_7: 543>, 'ImGuiKey_8': <ImGuiKey.ImGuiKey_8: 544>, 'ImGuiKey_9': <ImGuiKey.ImGuiKey_9: 545>, 'ImGuiKey_A': <ImGuiKey.ImGuiKey_A: 546>, 'ImGuiKey_B': <ImGuiKey.ImGuiKey_B: 547>, 'ImGuiKey_C': <ImGuiKey.ImGuiKey_C: 548>, 'ImGuiKey_D': <ImGuiKey.ImGuiKey_D: 549>, 'ImGuiKey_E': <ImGuiKey.ImGuiKey_E: 550>, 'ImGuiKey_F': <ImGuiKey.ImGuiKey_F: 551>, 'ImGuiKey_G': <ImGuiKey.ImGuiKey_G: 552>, 'ImGuiKey_H': <ImGuiKey.ImGuiKey_H: 553>, 'ImGuiKey_I': <ImGuiKey.ImGuiKey_I: 554>, 'ImGuiKey_J': <ImGuiKey.ImGuiKey_J: 555>, 'ImGuiKey_K': <ImGuiKey.ImGuiKey_K: 556>, 'ImGuiKey_L': <ImGuiKey.ImGuiKey_L: 557>, 'ImGuiKey_M': <ImGuiKey.ImGuiKey_M: 558>, 'ImGuiKey_N': <ImGuiKey.ImGuiKey_N: 559>, 'ImGuiKey_O': <ImGuiKey.ImGuiKey_O: 560>, 'ImGuiKey_P': <ImGuiKey.ImGuiKey_P: 561>, 'ImGuiKey_Q': <ImGuiKey.ImGuiKey_Q: 562>, 'ImGuiKey_R': <ImGuiKey.ImGuiKey_R: 563>, 'ImGuiKey_S': <ImGuiKey.ImGuiKey_S: 564>, 'ImGuiKey_T': <ImGuiKey.ImGuiKey_T: 565>, 'ImGuiKey_U': <ImGuiKey.ImGuiKey_U: 566>, 'ImGuiKey_V': <ImGuiKey.ImGuiKey_V: 567>, 'ImGuiKey_W': <ImGuiKey.ImGuiKey_W: 568>, 'ImGuiKey_X': <ImGuiKey.ImGuiKey_X: 569>, 'ImGuiKey_Y': <ImGuiKey.ImGuiKey_Y: 570>, 'ImGuiKey_Z': <ImGuiKey.ImGuiKey_Z: 571>, 'ImGuiKey_F1': <ImGuiKey.ImGuiKey_F1: 572>, 'ImGuiKey_F2': <ImGuiKey.ImGuiKey_F2: 573>, 'ImGuiKey_F3': <ImGuiKey.ImGuiKey_F3: 574>, 'ImGuiKey_F4': <ImGuiKey.ImGuiKey_F4: 575>, 'ImGuiKey_F5': <ImGuiKey.ImGuiKey_F5: 576>, 'ImGuiKey_F6': <ImGuiKey.ImGuiKey_F6: 577>, 'ImGuiKey_F7': <ImGuiKey.ImGuiKey_F7: 578>, 'ImGuiKey_F8': <ImGuiKey.ImGuiKey_F8: 579>, 'ImGuiKey_F9': <ImGuiKey.ImGuiKey_F9: 580>, 'ImGuiKey_F10': <ImGuiKey.ImGuiKey_F10: 581>, 'ImGuiKey_F11': <ImGuiKey.ImGuiKey_F11: 582>, 'ImGuiKey_F12': <ImGuiKey.ImGuiKey_F12: 583>, 'ImGuiKey_F13': <ImGuiKey.ImGuiKey_F13: 584>, 'ImGuiKey_F14': <ImGuiKey.ImGuiKey_F14: 585>, 'ImGuiKey_F15': <ImGuiKey.ImGuiKey_F15: 586>, 'ImGuiKey_F16': <ImGuiKey.ImGuiKey_F16: 587>, 'ImGuiKey_F17': <ImGuiKey.ImGuiKey_F17: 588>, 'ImGuiKey_F18': <ImGuiKey.ImGuiKey_F18: 589>, 'ImGuiKey_F19': <ImGuiKey.ImGuiKey_F19: 590>, 'ImGuiKey_F20': <ImGuiKey.ImGuiKey_F20: 591>, 'ImGuiKey_F21': <ImGuiKey.ImGuiKey_F21: 592>, 'ImGuiKey_F22': <ImGuiKey.ImGuiKey_F22: 593>, 'ImGuiKey_F23': <ImGuiKey.ImGuiKey_F23: 594>, 'ImGuiKey_F24': <ImGuiKey.ImGuiKey_F24: 595>, 'ImGuiKey_Apostrophe': <ImGuiKey.ImGuiKey_Apostrophe: 596>, 'ImGuiKey_Comma': <ImGuiKey.ImGuiKey_Comma: 597>, 'ImGuiKey_Minus': <ImGuiKey.ImGuiKey_Minus: 598>, 'ImGuiKey_Period': <ImGuiKey.ImGuiKey_Period: 599>, 'ImGuiKey_Slash': <ImGuiKey.ImGuiKey_Slash: 600>, 'ImGuiKey_Semicolon': <ImGuiKey.ImGuiKey_Semicolon: 601>, 'ImGuiKey_Equal': <ImGuiKey.ImGuiKey_Equal: 602>, 'ImGuiKey_LeftBracket': <ImGuiKey.ImGuiKey_LeftBracket: 603>, 'ImGuiKey_Backslash': <ImGuiKey.ImGuiKey_Backslash: 604>, 'ImGuiKey_RightBracket': <ImGuiKey.ImGuiKey_RightBracket: 605>, 'ImGuiKey_GraveAccent': <ImGuiKey.ImGuiKey_GraveAccent: 606>, 'ImGuiKey_CapsLock': <ImGuiKey.ImGuiKey_CapsLock: 607>, 'ImGuiKey_ScrollLock': <ImGuiKey.ImGuiKey_ScrollLock: 608>, 'ImGuiKey_NumLock': <ImGuiKey.ImGuiKey_NumLock: 609>, 'ImGuiKey_PrintScreen': <ImGuiKey.ImGuiKey_PrintScreen: 610>, 'ImGuiKey_Pause': <ImGuiKey.ImGuiKey_Pause: 611>, 'ImGuiKey_Keypad0': <ImGuiKey.ImGuiKey_Keypad0: 612>, 'ImGuiKey_Keypad1': <ImGuiKey.ImGuiKey_Keypad1: 613>, 'ImGuiKey_Keypad2': <ImGuiKey.ImGuiKey_Keypad2: 614>, 'ImGuiKey_Keypad3': <ImGuiKey.ImGuiKey_Keypad3: 615>, 'ImGuiKey_Keypad4': <ImGuiKey.ImGuiKey_Keypad4: 616>, 'ImGuiKey_Keypad5': <ImGuiKey.ImGuiKey_Keypad5: 617>, 'ImGuiKey_Keypad6': <ImGuiKey.ImGuiKey_Keypad6: 618>, 'ImGuiKey_Keypad7': <ImGuiKey.ImGuiKey_Keypad7: 619>, 'ImGuiKey_Keypad8': <ImGuiKey.ImGuiKey_Keypad8: 620>, 'ImGuiKey_Keypad9': <ImGuiKey.ImGuiKey_Keypad9: 621>, 'ImGuiKey_KeypadDecimal': <ImGuiKey.ImGuiKey_KeypadDecimal: 622>, 'ImGuiKey_KeypadDivide': <ImGuiKey.ImGuiKey_KeypadDivide: 623>, 'ImGuiKey_KeypadMultiply': <ImGuiKey.ImGuiKey_KeypadMultiply: 624>, 'ImGuiKey_KeypadSubtract': <ImGuiKey.ImGuiKey_KeypadSubtract: 625>, 'ImGuiKey_KeypadAdd': <ImGuiKey.ImGuiKey_KeypadAdd: 626>, 'ImGuiKey_KeypadEnter': <ImGuiKey.ImGuiKey_KeypadEnter: 627>, 'ImGuiKey_KeypadEqual': <ImGuiKey.ImGuiKey_KeypadEqual: 628>, 'ImGuiKey_AppBack': <ImGuiKey.ImGuiKey_AppBack: 629>, 'ImGuiKey_AppForward': <ImGuiKey.ImGuiKey_AppForward: 630>, 'ImGuiKey_GamepadStart': <ImGuiKey.ImGuiKey_GamepadStart: 631>, 'ImGuiKey_GamepadBack': <ImGuiKey.ImGuiKey_GamepadBack: 632>, 'ImGuiKey_GamepadFaceLeft': <ImGuiKey.ImGuiKey_GamepadFaceLeft: 633>, 'ImGuiKey_GamepadFaceRight': <ImGuiKey.ImGuiKey_GamepadFaceRight: 634>, 'ImGuiKey_GamepadFaceUp': <ImGuiKey.ImGuiKey_GamepadFaceUp: 635>, 'ImGuiKey_GamepadFaceDown': <ImGuiKey.ImGuiKey_GamepadFaceDown: 636>, 'ImGuiKey_GamepadDpadLeft': <ImGuiKey.ImGuiKey_GamepadDpadLeft: 637>, 'ImGuiKey_GamepadDpadRight': <ImGuiKey.ImGuiKey_GamepadDpadRight: 638>, 'ImGuiKey_GamepadDpadUp': <ImGuiKey.ImGuiKey_GamepadDpadUp: 639>, 'ImGuiKey_GamepadDpadDown': <ImGuiKey.ImGuiKey_GamepadDpadDown: 640>, 'ImGuiKey_GamepadL1': <ImGuiKey.ImGuiKey_GamepadL1: 641>, 'ImGuiKey_GamepadR1': <ImGuiKey.ImGuiKey_GamepadR1: 642>, 'ImGuiKey_GamepadL2': <ImGuiKey.ImGuiKey_GamepadL2: 643>, 'ImGuiKey_GamepadR2': <ImGuiKey.ImGuiKey_GamepadR2: 644>, 'ImGuiKey_GamepadL3': <ImGuiKey.ImGuiKey_GamepadL3: 645>, 'ImGuiKey_GamepadR3': <ImGuiKey.ImGuiKey_GamepadR3: 646>, 'ImGuiKey_GamepadLStickLeft': <ImGuiKey.ImGuiKey_GamepadLStickLeft: 647>, 'ImGuiKey_GamepadLStickRight': <ImGuiKey.ImGuiKey_GamepadLStickRight: 648>, 'ImGuiKey_GamepadLStickUp': <ImGuiKey.ImGuiKey_GamepadLStickUp: 649>, 'ImGuiKey_GamepadLStickDown': <ImGuiKey.ImGuiKey_GamepadLStickDown: 650>, 'ImGuiKey_GamepadRStickLeft': <ImGuiKey.ImGuiKey_GamepadRStickLeft: 651>, 'ImGuiKey_GamepadRStickRight': <ImGuiKey.ImGuiKey_GamepadRStickRight: 652>, 'ImGuiKey_GamepadRStickUp': <ImGuiKey.ImGuiKey_GamepadRStickUp: 653>, 'ImGuiKey_GamepadRStickDown': <ImGuiKey.ImGuiKey_GamepadRStickDown: 654>, 'ImGuiKey_MouseLeft': <ImGuiKey.ImGuiKey_MouseLeft: 655>, 'ImGuiKey_MouseRight': <ImGuiKey.ImGuiKey_MouseRight: 656>, 'ImGuiKey_MouseMiddle': <ImGuiKey.ImGuiKey_MouseMiddle: 657>, 'ImGuiKey_MouseX1': <ImGuiKey.ImGuiKey_MouseX1: 658>, 'ImGuiKey_MouseX2': <ImGuiKey.ImGuiKey_MouseX2: 659>, 'ImGuiKey_MouseWheelX': <ImGuiKey.ImGuiKey_MouseWheelX: 660>, 'ImGuiKey_MouseWheelY': <ImGuiKey.ImGuiKey_MouseWheelY: 661>, 'ImGuiKey_ReservedForModCtrl': <ImGuiKey.ImGuiKey_ReservedForModCtrl: 662>, 'ImGuiKey_ReservedForModShift': <ImGuiKey.ImGuiKey_ReservedForModShift: 663>, 'ImGuiKey_ReservedForModAlt': <ImGuiKey.ImGuiKey_ReservedForModAlt: 664>, 'ImGuiKey_ReservedForModSuper': <ImGuiKey.ImGuiKey_ReservedForModSuper: 665>, 'ImGuiKey_COUNT': <ImGuiKey.ImGuiKey_COUNT: 666>, 'ImGuiMod_None': <ImGuiKey.ImGuiKey_None: 0>, 'ImGuiMod_Ctrl': <ImGuiKey.ImGuiMod_Ctrl: 4096>, 'ImGuiMod_Shift': <ImGuiKey.ImGuiMod_Shift: 8192>, 'ImGuiMod_Alt': <ImGuiKey.ImGuiMod_Alt: 16384>, 'ImGuiMod_Super': <ImGuiKey.ImGuiMod_Super: 32768>, 'ImGuiMod_Mask_': <ImGuiKey.ImGuiMod_Mask_: 61440>, 'ImGuiKey_NamedKey_BEGIN': <ImGuiKey.ImGuiKey_Tab: 512>, 'ImGuiKey_NamedKey_END': <ImGuiKey.ImGuiKey_COUNT: 666>, 'ImGuiKey_NamedKey_COUNT': <ImGuiKey.ImGuiKey_NamedKey_COUNT: 154>, 'ImGuiKey_KeysData_SIZE': <ImGuiKey.ImGuiKey_NamedKey_COUNT: 154>, 'ImGuiKey_KeysData_OFFSET': <ImGuiKey.ImGuiKey_Tab: 512>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiKeyData:
    AnalogValue: float
    Down: bool
    DownDuration: float
    DownDurationPrev: float
class ImGuiKeyOwnerData:
    LockThisFrame: bool
    LockUntilRelease: bool
    OwnerCurr: int
    OwnerNext: int
    def __init__(self) -> None:
        ...
class ImGuiKeyRoutingData:
    Mods: int
    NextEntryIndex: int
    RoutingCurr: int
    RoutingCurrScore: int
    RoutingNext: int
    RoutingNextScore: int
    def __init__(self) -> None:
        ...
class ImGuiKeyRoutingTable:
    Entries: ImVector_ImGuiKeyRoutingData
    EntriesNext: ImVector_ImGuiKeyRoutingData
    def Clear(self) -> None:
        ...
    def __init__(self) -> None:
        ...
    @property
    def Index(self) -> Arr_signed_short:
        ...
class ImGuiLastItemData:
    ClipRect: ImRect
    DisplayRect: ImRect
    ID: int
    InFlags: int
    NavRect: ImRect
    Rect: ImRect
    Shortcut: int
    StatusFlags: int
    def __init__(self) -> None:
        ...
class ImGuiLayoutType_:
    """
    Members:
    
      ImGuiLayoutType_Horizontal
    
      ImGuiLayoutType_Vertical
    """
    ImGuiLayoutType_Horizontal: typing.ClassVar[ImGuiLayoutType_]  # value = <ImGuiLayoutType_.ImGuiLayoutType_Horizontal: 0>
    ImGuiLayoutType_Vertical: typing.ClassVar[ImGuiLayoutType_]  # value = <ImGuiLayoutType_.ImGuiLayoutType_Vertical: 1>
    __members__: typing.ClassVar[dict[str, ImGuiLayoutType_]]  # value = {'ImGuiLayoutType_Horizontal': <ImGuiLayoutType_.ImGuiLayoutType_Horizontal: 0>, 'ImGuiLayoutType_Vertical': <ImGuiLayoutType_.ImGuiLayoutType_Vertical: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiListClipper:
    Ctx: ImGuiContext
    DisplayEnd: int
    DisplayStart: int
    ItemsCount: int
    ItemsHeight: float
    StartPosY: float
    TempData: capsule
    def Begin(self, items_count: int, items_height: float = -1.0) -> None:
        ...
    def End(self) -> None:
        ...
    def IncludeItemByIndex(self, item_index: int) -> None:
        ...
    def IncludeItemsByIndex(self, item_begin: int, item_end: int) -> None:
        ...
    def Step(self) -> bool:
        ...
    def __init__(self) -> None:
        ...
class ImGuiListClipperData:
    ItemsFrozen: int
    ListClipper: ImGuiListClipper
    LossynessOffset: float
    Ranges: ImVector_ImGuiListClipperRange
    StepNo: int
    def Reset(self, clipper: ImGuiListClipper) -> None:
        ...
    def __init__(self) -> None:
        ...
class ImGuiListClipperRange:
    Max: int
    Min: int
    PosToIndexConvert: bool
    PosToIndexOffsetMax: int
    PosToIndexOffsetMin: int
    @staticmethod
    def FromIndices(min: int, max: int) -> ImGuiListClipperRange:
        ...
    @staticmethod
    def FromPositions(y1: float, y2: float, off_min: int, off_max: int) -> ImGuiListClipperRange:
        ...
class ImGuiLocEntry:
    Key: ImGuiLocKey
    Text: str
class ImGuiLocKey:
    """
    Members:
    
      ImGuiLocKey_VersionStr
    
      ImGuiLocKey_TableSizeOne
    
      ImGuiLocKey_TableSizeAllFit
    
      ImGuiLocKey_TableSizeAllDefault
    
      ImGuiLocKey_TableResetOrder
    
      ImGuiLocKey_WindowingMainMenuBar
    
      ImGuiLocKey_WindowingPopup
    
      ImGuiLocKey_WindowingUntitled
    
      ImGuiLocKey_DockingHideTabBar
    
      ImGuiLocKey_DockingHoldShiftToDock
    
      ImGuiLocKey_DockingDragToUndockOrMoveNode
    
      ImGuiLocKey_COUNT
    """
    ImGuiLocKey_COUNT: typing.ClassVar[ImGuiLocKey]  # value = <ImGuiLocKey.ImGuiLocKey_COUNT: 11>
    ImGuiLocKey_DockingDragToUndockOrMoveNode: typing.ClassVar[ImGuiLocKey]  # value = <ImGuiLocKey.ImGuiLocKey_DockingDragToUndockOrMoveNode: 10>
    ImGuiLocKey_DockingHideTabBar: typing.ClassVar[ImGuiLocKey]  # value = <ImGuiLocKey.ImGuiLocKey_DockingHideTabBar: 8>
    ImGuiLocKey_DockingHoldShiftToDock: typing.ClassVar[ImGuiLocKey]  # value = <ImGuiLocKey.ImGuiLocKey_DockingHoldShiftToDock: 9>
    ImGuiLocKey_TableResetOrder: typing.ClassVar[ImGuiLocKey]  # value = <ImGuiLocKey.ImGuiLocKey_TableResetOrder: 4>
    ImGuiLocKey_TableSizeAllDefault: typing.ClassVar[ImGuiLocKey]  # value = <ImGuiLocKey.ImGuiLocKey_TableSizeAllDefault: 3>
    ImGuiLocKey_TableSizeAllFit: typing.ClassVar[ImGuiLocKey]  # value = <ImGuiLocKey.ImGuiLocKey_TableSizeAllFit: 2>
    ImGuiLocKey_TableSizeOne: typing.ClassVar[ImGuiLocKey]  # value = <ImGuiLocKey.ImGuiLocKey_TableSizeOne: 1>
    ImGuiLocKey_VersionStr: typing.ClassVar[ImGuiLocKey]  # value = <ImGuiLocKey.ImGuiLocKey_VersionStr: 0>
    ImGuiLocKey_WindowingMainMenuBar: typing.ClassVar[ImGuiLocKey]  # value = <ImGuiLocKey.ImGuiLocKey_WindowingMainMenuBar: 5>
    ImGuiLocKey_WindowingPopup: typing.ClassVar[ImGuiLocKey]  # value = <ImGuiLocKey.ImGuiLocKey_WindowingPopup: 6>
    ImGuiLocKey_WindowingUntitled: typing.ClassVar[ImGuiLocKey]  # value = <ImGuiLocKey.ImGuiLocKey_WindowingUntitled: 7>
    __members__: typing.ClassVar[dict[str, ImGuiLocKey]]  # value = {'ImGuiLocKey_VersionStr': <ImGuiLocKey.ImGuiLocKey_VersionStr: 0>, 'ImGuiLocKey_TableSizeOne': <ImGuiLocKey.ImGuiLocKey_TableSizeOne: 1>, 'ImGuiLocKey_TableSizeAllFit': <ImGuiLocKey.ImGuiLocKey_TableSizeAllFit: 2>, 'ImGuiLocKey_TableSizeAllDefault': <ImGuiLocKey.ImGuiLocKey_TableSizeAllDefault: 3>, 'ImGuiLocKey_TableResetOrder': <ImGuiLocKey.ImGuiLocKey_TableResetOrder: 4>, 'ImGuiLocKey_WindowingMainMenuBar': <ImGuiLocKey.ImGuiLocKey_WindowingMainMenuBar: 5>, 'ImGuiLocKey_WindowingPopup': <ImGuiLocKey.ImGuiLocKey_WindowingPopup: 6>, 'ImGuiLocKey_WindowingUntitled': <ImGuiLocKey.ImGuiLocKey_WindowingUntitled: 7>, 'ImGuiLocKey_DockingHideTabBar': <ImGuiLocKey.ImGuiLocKey_DockingHideTabBar: 8>, 'ImGuiLocKey_DockingHoldShiftToDock': <ImGuiLocKey.ImGuiLocKey_DockingHoldShiftToDock: 9>, 'ImGuiLocKey_DockingDragToUndockOrMoveNode': <ImGuiLocKey.ImGuiLocKey_DockingDragToUndockOrMoveNode: 10>, 'ImGuiLocKey_COUNT': <ImGuiLocKey.ImGuiLocKey_COUNT: 11>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiLogType:
    """
    Members:
    
      ImGuiLogType_None
    
      ImGuiLogType_TTY
    
      ImGuiLogType_File
    
      ImGuiLogType_Buffer
    
      ImGuiLogType_Clipboard
    """
    ImGuiLogType_Buffer: typing.ClassVar[ImGuiLogType]  # value = <ImGuiLogType.ImGuiLogType_Buffer: 3>
    ImGuiLogType_Clipboard: typing.ClassVar[ImGuiLogType]  # value = <ImGuiLogType.ImGuiLogType_Clipboard: 4>
    ImGuiLogType_File: typing.ClassVar[ImGuiLogType]  # value = <ImGuiLogType.ImGuiLogType_File: 2>
    ImGuiLogType_None: typing.ClassVar[ImGuiLogType]  # value = <ImGuiLogType.ImGuiLogType_None: 0>
    ImGuiLogType_TTY: typing.ClassVar[ImGuiLogType]  # value = <ImGuiLogType.ImGuiLogType_TTY: 1>
    __members__: typing.ClassVar[dict[str, ImGuiLogType]]  # value = {'ImGuiLogType_None': <ImGuiLogType.ImGuiLogType_None: 0>, 'ImGuiLogType_TTY': <ImGuiLogType.ImGuiLogType_TTY: 1>, 'ImGuiLogType_File': <ImGuiLogType.ImGuiLogType_File: 2>, 'ImGuiLogType_Buffer': <ImGuiLogType.ImGuiLogType_Buffer: 3>, 'ImGuiLogType_Clipboard': <ImGuiLogType.ImGuiLogType_Clipboard: 4>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiMenuColumns:
    NextTotalWidth: int
    OffsetIcon: int
    OffsetLabel: int
    OffsetMark: int
    OffsetShortcut: int
    Spacing: int
    TotalWidth: int
    def CalcNextTotalWidth(self, update_offsets: bool) -> None:
        ...
    def DeclColumns(self, w_icon: float, w_label: float, w_shortcut: float, w_mark: float) -> float:
        ...
    def Update(self, spacing: float, window_reappearing: bool) -> None:
        ...
    def __init__(self) -> None:
        ...
    @property
    def Widths(self) -> Arr_unsigned_short:
        ...
class ImGuiMetricsConfig:
    HighlightMonitorIdx: int
    HighlightViewportID: int
    ShowAtlasTintedWithTextColor: bool
    ShowDebugLog: bool
    ShowDockingNodes: bool
    ShowDrawCmdBoundingBoxes: bool
    ShowDrawCmdMesh: bool
    ShowIDStackTool: bool
    ShowTablesRects: bool
    ShowTablesRectsType: int
    ShowTextEncodingViewer: bool
    ShowWindowsBeginOrder: bool
    ShowWindowsRects: bool
    ShowWindowsRectsType: int
class ImGuiMouseButton_:
    """
    Members:
    
      ImGuiMouseButton_Left
    
      ImGuiMouseButton_Right
    
      ImGuiMouseButton_Middle
    
      ImGuiMouseButton_COUNT
    """
    ImGuiMouseButton_COUNT: typing.ClassVar[ImGuiMouseButton_]  # value = <ImGuiMouseButton_.ImGuiMouseButton_COUNT: 5>
    ImGuiMouseButton_Left: typing.ClassVar[ImGuiMouseButton_]  # value = <ImGuiMouseButton_.ImGuiMouseButton_Left: 0>
    ImGuiMouseButton_Middle: typing.ClassVar[ImGuiMouseButton_]  # value = <ImGuiMouseButton_.ImGuiMouseButton_Middle: 2>
    ImGuiMouseButton_Right: typing.ClassVar[ImGuiMouseButton_]  # value = <ImGuiMouseButton_.ImGuiMouseButton_Right: 1>
    __members__: typing.ClassVar[dict[str, ImGuiMouseButton_]]  # value = {'ImGuiMouseButton_Left': <ImGuiMouseButton_.ImGuiMouseButton_Left: 0>, 'ImGuiMouseButton_Right': <ImGuiMouseButton_.ImGuiMouseButton_Right: 1>, 'ImGuiMouseButton_Middle': <ImGuiMouseButton_.ImGuiMouseButton_Middle: 2>, 'ImGuiMouseButton_COUNT': <ImGuiMouseButton_.ImGuiMouseButton_COUNT: 5>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiMouseCursor_:
    """
    Members:
    
      ImGuiMouseCursor_None
    
      ImGuiMouseCursor_Arrow
    
      ImGuiMouseCursor_TextInput
    
      ImGuiMouseCursor_ResizeAll
    
      ImGuiMouseCursor_ResizeNS
    
      ImGuiMouseCursor_ResizeEW
    
      ImGuiMouseCursor_ResizeNESW
    
      ImGuiMouseCursor_ResizeNWSE
    
      ImGuiMouseCursor_Hand
    
      ImGuiMouseCursor_NotAllowed
    
      ImGuiMouseCursor_COUNT
    """
    ImGuiMouseCursor_Arrow: typing.ClassVar[ImGuiMouseCursor_]  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_Arrow: 0>
    ImGuiMouseCursor_COUNT: typing.ClassVar[ImGuiMouseCursor_]  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_COUNT: 9>
    ImGuiMouseCursor_Hand: typing.ClassVar[ImGuiMouseCursor_]  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_Hand: 7>
    ImGuiMouseCursor_None: typing.ClassVar[ImGuiMouseCursor_]  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_None: -1>
    ImGuiMouseCursor_NotAllowed: typing.ClassVar[ImGuiMouseCursor_]  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_NotAllowed: 8>
    ImGuiMouseCursor_ResizeAll: typing.ClassVar[ImGuiMouseCursor_]  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeAll: 2>
    ImGuiMouseCursor_ResizeEW: typing.ClassVar[ImGuiMouseCursor_]  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeEW: 4>
    ImGuiMouseCursor_ResizeNESW: typing.ClassVar[ImGuiMouseCursor_]  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeNESW: 5>
    ImGuiMouseCursor_ResizeNS: typing.ClassVar[ImGuiMouseCursor_]  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeNS: 3>
    ImGuiMouseCursor_ResizeNWSE: typing.ClassVar[ImGuiMouseCursor_]  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeNWSE: 6>
    ImGuiMouseCursor_TextInput: typing.ClassVar[ImGuiMouseCursor_]  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_TextInput: 1>
    __members__: typing.ClassVar[dict[str, ImGuiMouseCursor_]]  # value = {'ImGuiMouseCursor_None': <ImGuiMouseCursor_.ImGuiMouseCursor_None: -1>, 'ImGuiMouseCursor_Arrow': <ImGuiMouseCursor_.ImGuiMouseCursor_Arrow: 0>, 'ImGuiMouseCursor_TextInput': <ImGuiMouseCursor_.ImGuiMouseCursor_TextInput: 1>, 'ImGuiMouseCursor_ResizeAll': <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeAll: 2>, 'ImGuiMouseCursor_ResizeNS': <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeNS: 3>, 'ImGuiMouseCursor_ResizeEW': <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeEW: 4>, 'ImGuiMouseCursor_ResizeNESW': <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeNESW: 5>, 'ImGuiMouseCursor_ResizeNWSE': <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeNWSE: 6>, 'ImGuiMouseCursor_Hand': <ImGuiMouseCursor_.ImGuiMouseCursor_Hand: 7>, 'ImGuiMouseCursor_NotAllowed': <ImGuiMouseCursor_.ImGuiMouseCursor_NotAllowed: 8>, 'ImGuiMouseCursor_COUNT': <ImGuiMouseCursor_.ImGuiMouseCursor_COUNT: 9>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiMouseSource:
    """
    Members:
    
      ImGuiMouseSource_Mouse
    
      ImGuiMouseSource_TouchScreen
    
      ImGuiMouseSource_Pen
    
      ImGuiMouseSource_COUNT
    """
    ImGuiMouseSource_COUNT: typing.ClassVar[ImGuiMouseSource]  # value = <ImGuiMouseSource.ImGuiMouseSource_COUNT: 3>
    ImGuiMouseSource_Mouse: typing.ClassVar[ImGuiMouseSource]  # value = <ImGuiMouseSource.ImGuiMouseSource_Mouse: 0>
    ImGuiMouseSource_Pen: typing.ClassVar[ImGuiMouseSource]  # value = <ImGuiMouseSource.ImGuiMouseSource_Pen: 2>
    ImGuiMouseSource_TouchScreen: typing.ClassVar[ImGuiMouseSource]  # value = <ImGuiMouseSource.ImGuiMouseSource_TouchScreen: 1>
    __members__: typing.ClassVar[dict[str, ImGuiMouseSource]]  # value = {'ImGuiMouseSource_Mouse': <ImGuiMouseSource.ImGuiMouseSource_Mouse: 0>, 'ImGuiMouseSource_TouchScreen': <ImGuiMouseSource.ImGuiMouseSource_TouchScreen: 1>, 'ImGuiMouseSource_Pen': <ImGuiMouseSource.ImGuiMouseSource_Pen: 2>, 'ImGuiMouseSource_COUNT': <ImGuiMouseSource.ImGuiMouseSource_COUNT: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiNavHighlightFlags_:
    """
    Members:
    
      ImGuiNavHighlightFlags_None
    
      ImGuiNavHighlightFlags_Compact
    
      ImGuiNavHighlightFlags_AlwaysDraw
    
      ImGuiNavHighlightFlags_NoRounding
    """
    ImGuiNavHighlightFlags_AlwaysDraw: typing.ClassVar[ImGuiNavHighlightFlags_]  # value = <ImGuiNavHighlightFlags_.ImGuiNavHighlightFlags_AlwaysDraw: 4>
    ImGuiNavHighlightFlags_Compact: typing.ClassVar[ImGuiNavHighlightFlags_]  # value = <ImGuiNavHighlightFlags_.ImGuiNavHighlightFlags_Compact: 2>
    ImGuiNavHighlightFlags_NoRounding: typing.ClassVar[ImGuiNavHighlightFlags_]  # value = <ImGuiNavHighlightFlags_.ImGuiNavHighlightFlags_NoRounding: 8>
    ImGuiNavHighlightFlags_None: typing.ClassVar[ImGuiNavHighlightFlags_]  # value = <ImGuiNavHighlightFlags_.ImGuiNavHighlightFlags_None: 0>
    __members__: typing.ClassVar[dict[str, ImGuiNavHighlightFlags_]]  # value = {'ImGuiNavHighlightFlags_None': <ImGuiNavHighlightFlags_.ImGuiNavHighlightFlags_None: 0>, 'ImGuiNavHighlightFlags_Compact': <ImGuiNavHighlightFlags_.ImGuiNavHighlightFlags_Compact: 2>, 'ImGuiNavHighlightFlags_AlwaysDraw': <ImGuiNavHighlightFlags_.ImGuiNavHighlightFlags_AlwaysDraw: 4>, 'ImGuiNavHighlightFlags_NoRounding': <ImGuiNavHighlightFlags_.ImGuiNavHighlightFlags_NoRounding: 8>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiNavItemData:
    DistAxial: float
    DistBox: float
    DistCenter: float
    FocusScopeId: int
    ID: int
    InFlags: int
    RectRel: ImRect
    SelectionUserData: int
    Window: ImGuiWindow
    def Clear(self) -> None:
        ...
    def __init__(self) -> None:
        ...
class ImGuiNavLayer:
    """
    Members:
    
      ImGuiNavLayer_Main
    
      ImGuiNavLayer_Menu
    
      ImGuiNavLayer_COUNT
    """
    ImGuiNavLayer_COUNT: typing.ClassVar[ImGuiNavLayer]  # value = <ImGuiNavLayer.ImGuiNavLayer_COUNT: 2>
    ImGuiNavLayer_Main: typing.ClassVar[ImGuiNavLayer]  # value = <ImGuiNavLayer.ImGuiNavLayer_Main: 0>
    ImGuiNavLayer_Menu: typing.ClassVar[ImGuiNavLayer]  # value = <ImGuiNavLayer.ImGuiNavLayer_Menu: 1>
    __members__: typing.ClassVar[dict[str, ImGuiNavLayer]]  # value = {'ImGuiNavLayer_Main': <ImGuiNavLayer.ImGuiNavLayer_Main: 0>, 'ImGuiNavLayer_Menu': <ImGuiNavLayer.ImGuiNavLayer_Menu: 1>, 'ImGuiNavLayer_COUNT': <ImGuiNavLayer.ImGuiNavLayer_COUNT: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiNavMoveFlags_:
    """
    Members:
    
      ImGuiNavMoveFlags_None
    
      ImGuiNavMoveFlags_LoopX
    
      ImGuiNavMoveFlags_LoopY
    
      ImGuiNavMoveFlags_WrapX
    
      ImGuiNavMoveFlags_WrapY
    
      ImGuiNavMoveFlags_WrapMask_
    
      ImGuiNavMoveFlags_AllowCurrentNavId
    
      ImGuiNavMoveFlags_AlsoScoreVisibleSet
    
      ImGuiNavMoveFlags_ScrollToEdgeY
    
      ImGuiNavMoveFlags_Forwarded
    
      ImGuiNavMoveFlags_DebugNoResult
    
      ImGuiNavMoveFlags_FocusApi
    
      ImGuiNavMoveFlags_IsTabbing
    
      ImGuiNavMoveFlags_IsPageMove
    
      ImGuiNavMoveFlags_Activate
    
      ImGuiNavMoveFlags_NoSelect
    
      ImGuiNavMoveFlags_NoSetNavHighlight
    
      ImGuiNavMoveFlags_NoClearActiveId
    """
    ImGuiNavMoveFlags_Activate: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_Activate: 4096>
    ImGuiNavMoveFlags_AllowCurrentNavId: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_AllowCurrentNavId: 16>
    ImGuiNavMoveFlags_AlsoScoreVisibleSet: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_AlsoScoreVisibleSet: 32>
    ImGuiNavMoveFlags_DebugNoResult: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_DebugNoResult: 256>
    ImGuiNavMoveFlags_FocusApi: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_FocusApi: 512>
    ImGuiNavMoveFlags_Forwarded: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_Forwarded: 128>
    ImGuiNavMoveFlags_IsPageMove: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_IsPageMove: 2048>
    ImGuiNavMoveFlags_IsTabbing: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_IsTabbing: 1024>
    ImGuiNavMoveFlags_LoopX: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_LoopX: 1>
    ImGuiNavMoveFlags_LoopY: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_LoopY: 2>
    ImGuiNavMoveFlags_NoClearActiveId: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_NoClearActiveId: 32768>
    ImGuiNavMoveFlags_NoSelect: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_NoSelect: 8192>
    ImGuiNavMoveFlags_NoSetNavHighlight: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_NoSetNavHighlight: 16384>
    ImGuiNavMoveFlags_None: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_None: 0>
    ImGuiNavMoveFlags_ScrollToEdgeY: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_ScrollToEdgeY: 64>
    ImGuiNavMoveFlags_WrapMask_: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_WrapMask_: 15>
    ImGuiNavMoveFlags_WrapX: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_WrapX: 4>
    ImGuiNavMoveFlags_WrapY: typing.ClassVar[ImGuiNavMoveFlags_]  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_WrapY: 8>
    __members__: typing.ClassVar[dict[str, ImGuiNavMoveFlags_]]  # value = {'ImGuiNavMoveFlags_None': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_None: 0>, 'ImGuiNavMoveFlags_LoopX': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_LoopX: 1>, 'ImGuiNavMoveFlags_LoopY': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_LoopY: 2>, 'ImGuiNavMoveFlags_WrapX': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_WrapX: 4>, 'ImGuiNavMoveFlags_WrapY': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_WrapY: 8>, 'ImGuiNavMoveFlags_WrapMask_': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_WrapMask_: 15>, 'ImGuiNavMoveFlags_AllowCurrentNavId': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_AllowCurrentNavId: 16>, 'ImGuiNavMoveFlags_AlsoScoreVisibleSet': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_AlsoScoreVisibleSet: 32>, 'ImGuiNavMoveFlags_ScrollToEdgeY': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_ScrollToEdgeY: 64>, 'ImGuiNavMoveFlags_Forwarded': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_Forwarded: 128>, 'ImGuiNavMoveFlags_DebugNoResult': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_DebugNoResult: 256>, 'ImGuiNavMoveFlags_FocusApi': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_FocusApi: 512>, 'ImGuiNavMoveFlags_IsTabbing': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_IsTabbing: 1024>, 'ImGuiNavMoveFlags_IsPageMove': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_IsPageMove: 2048>, 'ImGuiNavMoveFlags_Activate': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_Activate: 4096>, 'ImGuiNavMoveFlags_NoSelect': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_NoSelect: 8192>, 'ImGuiNavMoveFlags_NoSetNavHighlight': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_NoSetNavHighlight: 16384>, 'ImGuiNavMoveFlags_NoClearActiveId': <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_NoClearActiveId: 32768>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiNavTreeNodeData:
    ID: int
    InFlags: int
    NavRect: ImRect
class ImGuiNextItemData:
    Flags: int
    ItemFlags: int
    OpenCond: int
    OpenVal: bool
    RefVal: ImGuiDataTypeStorage
    SelectionUserData: int
    Shortcut: int
    ShortcutFlags: int
    Width: float
    def ClearFlags(self) -> None:
        ...
    def __init__(self) -> None:
        ...
class ImGuiNextItemDataFlags_:
    """
    Members:
    
      ImGuiNextItemDataFlags_None
    
      ImGuiNextItemDataFlags_HasWidth
    
      ImGuiNextItemDataFlags_HasOpen
    
      ImGuiNextItemDataFlags_HasShortcut
    
      ImGuiNextItemDataFlags_HasRefVal
    """
    ImGuiNextItemDataFlags_HasOpen: typing.ClassVar[ImGuiNextItemDataFlags_]  # value = <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_HasOpen: 2>
    ImGuiNextItemDataFlags_HasRefVal: typing.ClassVar[ImGuiNextItemDataFlags_]  # value = <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_HasRefVal: 8>
    ImGuiNextItemDataFlags_HasShortcut: typing.ClassVar[ImGuiNextItemDataFlags_]  # value = <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_HasShortcut: 4>
    ImGuiNextItemDataFlags_HasWidth: typing.ClassVar[ImGuiNextItemDataFlags_]  # value = <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_HasWidth: 1>
    ImGuiNextItemDataFlags_None: typing.ClassVar[ImGuiNextItemDataFlags_]  # value = <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_None: 0>
    __members__: typing.ClassVar[dict[str, ImGuiNextItemDataFlags_]]  # value = {'ImGuiNextItemDataFlags_None': <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_None: 0>, 'ImGuiNextItemDataFlags_HasWidth': <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_HasWidth: 1>, 'ImGuiNextItemDataFlags_HasOpen': <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_HasOpen: 2>, 'ImGuiNextItemDataFlags_HasShortcut': <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_HasShortcut: 4>, 'ImGuiNextItemDataFlags_HasRefVal': <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_HasRefVal: 8>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiNextWindowData:
    BgAlphaVal: float
    ChildFlags: int
    CollapsedCond: int
    CollapsedVal: bool
    ContentSizeVal: ImVec2
    DockCond: int
    DockId: int
    Flags: int
    MenuBarOffsetMinVal: ImVec2
    PosCond: int
    PosPivotVal: ImVec2
    PosUndock: bool
    PosVal: ImVec2
    RefreshFlagsVal: int
    ScrollVal: ImVec2
    SizeCallbackUserData: capsule
    SizeCond: int
    SizeConstraintRect: ImRect
    SizeVal: ImVec2
    ViewportId: int
    WindowClass: ImGuiWindowClass
    def ClearFlags(self) -> None:
        ...
    def __init__(self) -> None:
        ...
    @property
    def SizeCallback(*args, **kwargs):
        """
        (arg0: pyimgui.imgui.ImGuiNextWindowData) -> void __cdecl(ImGuiSizeCallbackData * __ptr64)
        """
    @SizeCallback.setter
    def SizeCallback(self, arg1: ...) -> None:
        ...
class ImGuiNextWindowDataFlags_:
    """
    Members:
    
      ImGuiNextWindowDataFlags_None
    
      ImGuiNextWindowDataFlags_HasPos
    
      ImGuiNextWindowDataFlags_HasSize
    
      ImGuiNextWindowDataFlags_HasContentSize
    
      ImGuiNextWindowDataFlags_HasCollapsed
    
      ImGuiNextWindowDataFlags_HasSizeConstraint
    
      ImGuiNextWindowDataFlags_HasFocus
    
      ImGuiNextWindowDataFlags_HasBgAlpha
    
      ImGuiNextWindowDataFlags_HasScroll
    
      ImGuiNextWindowDataFlags_HasChildFlags
    
      ImGuiNextWindowDataFlags_HasRefreshPolicy
    
      ImGuiNextWindowDataFlags_HasViewport
    
      ImGuiNextWindowDataFlags_HasDock
    
      ImGuiNextWindowDataFlags_HasWindowClass
    """
    ImGuiNextWindowDataFlags_HasBgAlpha: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasBgAlpha: 64>
    ImGuiNextWindowDataFlags_HasChildFlags: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasChildFlags: 256>
    ImGuiNextWindowDataFlags_HasCollapsed: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasCollapsed: 8>
    ImGuiNextWindowDataFlags_HasContentSize: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasContentSize: 4>
    ImGuiNextWindowDataFlags_HasDock: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasDock: 2048>
    ImGuiNextWindowDataFlags_HasFocus: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasFocus: 32>
    ImGuiNextWindowDataFlags_HasPos: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasPos: 1>
    ImGuiNextWindowDataFlags_HasRefreshPolicy: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasRefreshPolicy: 512>
    ImGuiNextWindowDataFlags_HasScroll: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasScroll: 128>
    ImGuiNextWindowDataFlags_HasSize: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasSize: 2>
    ImGuiNextWindowDataFlags_HasSizeConstraint: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasSizeConstraint: 16>
    ImGuiNextWindowDataFlags_HasViewport: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasViewport: 1024>
    ImGuiNextWindowDataFlags_HasWindowClass: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasWindowClass: 4096>
    ImGuiNextWindowDataFlags_None: typing.ClassVar[ImGuiNextWindowDataFlags_]  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_None: 0>
    __members__: typing.ClassVar[dict[str, ImGuiNextWindowDataFlags_]]  # value = {'ImGuiNextWindowDataFlags_None': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_None: 0>, 'ImGuiNextWindowDataFlags_HasPos': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasPos: 1>, 'ImGuiNextWindowDataFlags_HasSize': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasSize: 2>, 'ImGuiNextWindowDataFlags_HasContentSize': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasContentSize: 4>, 'ImGuiNextWindowDataFlags_HasCollapsed': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasCollapsed: 8>, 'ImGuiNextWindowDataFlags_HasSizeConstraint': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasSizeConstraint: 16>, 'ImGuiNextWindowDataFlags_HasFocus': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasFocus: 32>, 'ImGuiNextWindowDataFlags_HasBgAlpha': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasBgAlpha: 64>, 'ImGuiNextWindowDataFlags_HasScroll': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasScroll: 128>, 'ImGuiNextWindowDataFlags_HasChildFlags': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasChildFlags: 256>, 'ImGuiNextWindowDataFlags_HasRefreshPolicy': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasRefreshPolicy: 512>, 'ImGuiNextWindowDataFlags_HasViewport': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasViewport: 1024>, 'ImGuiNextWindowDataFlags_HasDock': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasDock: 2048>, 'ImGuiNextWindowDataFlags_HasWindowClass': <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasWindowClass: 4096>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiOldColumnData:
    ClipRect: ImRect
    Flags: int
    OffsetNorm: float
    OffsetNormBeforeResize: float
    def __init__(self) -> None:
        ...
class ImGuiOldColumnFlags_:
    """
    Members:
    
      ImGuiOldColumnFlags_None
    
      ImGuiOldColumnFlags_NoBorder
    
      ImGuiOldColumnFlags_NoResize
    
      ImGuiOldColumnFlags_NoPreserveWidths
    
      ImGuiOldColumnFlags_NoForceWithinWindow
    
      ImGuiOldColumnFlags_GrowParentContentsSize
    """
    ImGuiOldColumnFlags_GrowParentContentsSize: typing.ClassVar[ImGuiOldColumnFlags_]  # value = <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_GrowParentContentsSize: 16>
    ImGuiOldColumnFlags_NoBorder: typing.ClassVar[ImGuiOldColumnFlags_]  # value = <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_NoBorder: 1>
    ImGuiOldColumnFlags_NoForceWithinWindow: typing.ClassVar[ImGuiOldColumnFlags_]  # value = <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_NoForceWithinWindow: 8>
    ImGuiOldColumnFlags_NoPreserveWidths: typing.ClassVar[ImGuiOldColumnFlags_]  # value = <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_NoPreserveWidths: 4>
    ImGuiOldColumnFlags_NoResize: typing.ClassVar[ImGuiOldColumnFlags_]  # value = <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_NoResize: 2>
    ImGuiOldColumnFlags_None: typing.ClassVar[ImGuiOldColumnFlags_]  # value = <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_None: 0>
    __members__: typing.ClassVar[dict[str, ImGuiOldColumnFlags_]]  # value = {'ImGuiOldColumnFlags_None': <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_None: 0>, 'ImGuiOldColumnFlags_NoBorder': <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_NoBorder: 1>, 'ImGuiOldColumnFlags_NoResize': <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_NoResize: 2>, 'ImGuiOldColumnFlags_NoPreserveWidths': <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_NoPreserveWidths: 4>, 'ImGuiOldColumnFlags_NoForceWithinWindow': <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_NoForceWithinWindow: 8>, 'ImGuiOldColumnFlags_GrowParentContentsSize': <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_GrowParentContentsSize: 16>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiOldColumns:
    Columns: ImVector_ImGuiOldColumnData
    Count: int
    Current: int
    Flags: int
    HostBackupClipRect: ImRect
    HostBackupParentWorkRect: ImRect
    HostCursorMaxPosX: float
    HostCursorPosY: float
    HostInitialClipRect: ImRect
    ID: int
    IsBeingResized: bool
    IsFirstFrame: bool
    LineMaxY: float
    LineMinY: float
    OffMaxX: float
    OffMinX: float
    Splitter: ImDrawListSplitter
    def __init__(self) -> None:
        ...
class ImGuiOnceUponAFrame:
    RefFrame: int
    def __init__(self) -> None:
        ...
class ImGuiPayload:
    Data: capsule
    DataFrameCount: int
    DataSize: int
    Delivery: bool
    Preview: bool
    SourceId: int
    SourceParentId: int
    def Clear(self) -> None:
        ...
    def IsDataType(self, type: str) -> bool:
        ...
    def IsDelivery(self) -> bool:
        ...
    def IsPreview(self) -> bool:
        ...
    def __init__(self) -> None:
        ...
    @property
    def DataType(self) -> Arr_char:
        ...
class ImGuiPlatformIO:
    Monitors: ImVector_ImGuiPlatformMonitor
    Viewports: ImVector_ImGuiViewportPtr
    def __init__(self) -> None:
        ...
class ImGuiPlatformImeData:
    InputLineHeight: float
    InputPos: ImVec2
    WantVisible: bool
    def __init__(self) -> None:
        ...
class ImGuiPlatformMonitor:
    DpiScale: float
    MainPos: ImVec2
    MainSize: ImVec2
    PlatformHandle: capsule
    WorkPos: ImVec2
    WorkSize: ImVec2
    def __init__(self) -> None:
        ...
class ImGuiPlotType:
    """
    Members:
    
      ImGuiPlotType_Lines
    
      ImGuiPlotType_Histogram
    """
    ImGuiPlotType_Histogram: typing.ClassVar[ImGuiPlotType]  # value = <ImGuiPlotType.ImGuiPlotType_Histogram: 1>
    ImGuiPlotType_Lines: typing.ClassVar[ImGuiPlotType]  # value = <ImGuiPlotType.ImGuiPlotType_Lines: 0>
    __members__: typing.ClassVar[dict[str, ImGuiPlotType]]  # value = {'ImGuiPlotType_Lines': <ImGuiPlotType.ImGuiPlotType_Lines: 0>, 'ImGuiPlotType_Histogram': <ImGuiPlotType.ImGuiPlotType_Histogram: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiPopupData:
    OpenFrameCount: int
    OpenMousePos: ImVec2
    OpenParentId: int
    OpenPopupPos: ImVec2
    ParentNavLayer: int
    PopupId: int
    RestoreNavWindow: ImGuiWindow
    Window: ImGuiWindow
    def __init__(self) -> None:
        ...
class ImGuiPopupFlags_:
    """
    Members:
    
      ImGuiPopupFlags_None
    
      ImGuiPopupFlags_MouseButtonLeft
    
      ImGuiPopupFlags_MouseButtonRight
    
      ImGuiPopupFlags_MouseButtonMiddle
    
      ImGuiPopupFlags_MouseButtonMask_
    
      ImGuiPopupFlags_MouseButtonDefault_
    
      ImGuiPopupFlags_NoReopen
    
      ImGuiPopupFlags_NoOpenOverExistingPopup
    
      ImGuiPopupFlags_NoOpenOverItems
    
      ImGuiPopupFlags_AnyPopupId
    
      ImGuiPopupFlags_AnyPopupLevel
    
      ImGuiPopupFlags_AnyPopup
    """
    ImGuiPopupFlags_AnyPopup: typing.ClassVar[ImGuiPopupFlags_]  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_AnyPopup: 3072>
    ImGuiPopupFlags_AnyPopupId: typing.ClassVar[ImGuiPopupFlags_]  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_AnyPopupId: 1024>
    ImGuiPopupFlags_AnyPopupLevel: typing.ClassVar[ImGuiPopupFlags_]  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_AnyPopupLevel: 2048>
    ImGuiPopupFlags_MouseButtonDefault_: typing.ClassVar[ImGuiPopupFlags_]  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonRight: 1>
    ImGuiPopupFlags_MouseButtonLeft: typing.ClassVar[ImGuiPopupFlags_]  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_None: 0>
    ImGuiPopupFlags_MouseButtonMask_: typing.ClassVar[ImGuiPopupFlags_]  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonMask_: 31>
    ImGuiPopupFlags_MouseButtonMiddle: typing.ClassVar[ImGuiPopupFlags_]  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonMiddle: 2>
    ImGuiPopupFlags_MouseButtonRight: typing.ClassVar[ImGuiPopupFlags_]  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonRight: 1>
    ImGuiPopupFlags_NoOpenOverExistingPopup: typing.ClassVar[ImGuiPopupFlags_]  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_NoOpenOverExistingPopup: 128>
    ImGuiPopupFlags_NoOpenOverItems: typing.ClassVar[ImGuiPopupFlags_]  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_NoOpenOverItems: 256>
    ImGuiPopupFlags_NoReopen: typing.ClassVar[ImGuiPopupFlags_]  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_NoReopen: 32>
    ImGuiPopupFlags_None: typing.ClassVar[ImGuiPopupFlags_]  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_None: 0>
    __members__: typing.ClassVar[dict[str, ImGuiPopupFlags_]]  # value = {'ImGuiPopupFlags_None': <ImGuiPopupFlags_.ImGuiPopupFlags_None: 0>, 'ImGuiPopupFlags_MouseButtonLeft': <ImGuiPopupFlags_.ImGuiPopupFlags_None: 0>, 'ImGuiPopupFlags_MouseButtonRight': <ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonRight: 1>, 'ImGuiPopupFlags_MouseButtonMiddle': <ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonMiddle: 2>, 'ImGuiPopupFlags_MouseButtonMask_': <ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonMask_: 31>, 'ImGuiPopupFlags_MouseButtonDefault_': <ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonRight: 1>, 'ImGuiPopupFlags_NoReopen': <ImGuiPopupFlags_.ImGuiPopupFlags_NoReopen: 32>, 'ImGuiPopupFlags_NoOpenOverExistingPopup': <ImGuiPopupFlags_.ImGuiPopupFlags_NoOpenOverExistingPopup: 128>, 'ImGuiPopupFlags_NoOpenOverItems': <ImGuiPopupFlags_.ImGuiPopupFlags_NoOpenOverItems: 256>, 'ImGuiPopupFlags_AnyPopupId': <ImGuiPopupFlags_.ImGuiPopupFlags_AnyPopupId: 1024>, 'ImGuiPopupFlags_AnyPopupLevel': <ImGuiPopupFlags_.ImGuiPopupFlags_AnyPopupLevel: 2048>, 'ImGuiPopupFlags_AnyPopup': <ImGuiPopupFlags_.ImGuiPopupFlags_AnyPopup: 3072>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiPopupPositionPolicy:
    """
    Members:
    
      ImGuiPopupPositionPolicy_Default
    
      ImGuiPopupPositionPolicy_ComboBox
    
      ImGuiPopupPositionPolicy_Tooltip
    """
    ImGuiPopupPositionPolicy_ComboBox: typing.ClassVar[ImGuiPopupPositionPolicy]  # value = <ImGuiPopupPositionPolicy.ImGuiPopupPositionPolicy_ComboBox: 1>
    ImGuiPopupPositionPolicy_Default: typing.ClassVar[ImGuiPopupPositionPolicy]  # value = <ImGuiPopupPositionPolicy.ImGuiPopupPositionPolicy_Default: 0>
    ImGuiPopupPositionPolicy_Tooltip: typing.ClassVar[ImGuiPopupPositionPolicy]  # value = <ImGuiPopupPositionPolicy.ImGuiPopupPositionPolicy_Tooltip: 2>
    __members__: typing.ClassVar[dict[str, ImGuiPopupPositionPolicy]]  # value = {'ImGuiPopupPositionPolicy_Default': <ImGuiPopupPositionPolicy.ImGuiPopupPositionPolicy_Default: 0>, 'ImGuiPopupPositionPolicy_ComboBox': <ImGuiPopupPositionPolicy.ImGuiPopupPositionPolicy_ComboBox: 1>, 'ImGuiPopupPositionPolicy_Tooltip': <ImGuiPopupPositionPolicy.ImGuiPopupPositionPolicy_Tooltip: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiPtrOrIndex:
    Index: int
    Ptr: capsule
    @typing.overload
    def __init__(self, ptr: capsule) -> None:
        ...
    @typing.overload
    def __init__(self, index: int) -> None:
        ...
class ImGuiScrollFlags_:
    """
    Members:
    
      ImGuiScrollFlags_None
    
      ImGuiScrollFlags_KeepVisibleEdgeX
    
      ImGuiScrollFlags_KeepVisibleEdgeY
    
      ImGuiScrollFlags_KeepVisibleCenterX
    
      ImGuiScrollFlags_KeepVisibleCenterY
    
      ImGuiScrollFlags_AlwaysCenterX
    
      ImGuiScrollFlags_AlwaysCenterY
    
      ImGuiScrollFlags_NoScrollParent
    
      ImGuiScrollFlags_MaskX_
    
      ImGuiScrollFlags_MaskY_
    """
    ImGuiScrollFlags_AlwaysCenterX: typing.ClassVar[ImGuiScrollFlags_]  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_AlwaysCenterX: 16>
    ImGuiScrollFlags_AlwaysCenterY: typing.ClassVar[ImGuiScrollFlags_]  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_AlwaysCenterY: 32>
    ImGuiScrollFlags_KeepVisibleCenterX: typing.ClassVar[ImGuiScrollFlags_]  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_KeepVisibleCenterX: 4>
    ImGuiScrollFlags_KeepVisibleCenterY: typing.ClassVar[ImGuiScrollFlags_]  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_KeepVisibleCenterY: 8>
    ImGuiScrollFlags_KeepVisibleEdgeX: typing.ClassVar[ImGuiScrollFlags_]  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_KeepVisibleEdgeX: 1>
    ImGuiScrollFlags_KeepVisibleEdgeY: typing.ClassVar[ImGuiScrollFlags_]  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_KeepVisibleEdgeY: 2>
    ImGuiScrollFlags_MaskX_: typing.ClassVar[ImGuiScrollFlags_]  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_MaskX_: 21>
    ImGuiScrollFlags_MaskY_: typing.ClassVar[ImGuiScrollFlags_]  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_MaskY_: 42>
    ImGuiScrollFlags_NoScrollParent: typing.ClassVar[ImGuiScrollFlags_]  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_NoScrollParent: 64>
    ImGuiScrollFlags_None: typing.ClassVar[ImGuiScrollFlags_]  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_None: 0>
    __members__: typing.ClassVar[dict[str, ImGuiScrollFlags_]]  # value = {'ImGuiScrollFlags_None': <ImGuiScrollFlags_.ImGuiScrollFlags_None: 0>, 'ImGuiScrollFlags_KeepVisibleEdgeX': <ImGuiScrollFlags_.ImGuiScrollFlags_KeepVisibleEdgeX: 1>, 'ImGuiScrollFlags_KeepVisibleEdgeY': <ImGuiScrollFlags_.ImGuiScrollFlags_KeepVisibleEdgeY: 2>, 'ImGuiScrollFlags_KeepVisibleCenterX': <ImGuiScrollFlags_.ImGuiScrollFlags_KeepVisibleCenterX: 4>, 'ImGuiScrollFlags_KeepVisibleCenterY': <ImGuiScrollFlags_.ImGuiScrollFlags_KeepVisibleCenterY: 8>, 'ImGuiScrollFlags_AlwaysCenterX': <ImGuiScrollFlags_.ImGuiScrollFlags_AlwaysCenterX: 16>, 'ImGuiScrollFlags_AlwaysCenterY': <ImGuiScrollFlags_.ImGuiScrollFlags_AlwaysCenterY: 32>, 'ImGuiScrollFlags_NoScrollParent': <ImGuiScrollFlags_.ImGuiScrollFlags_NoScrollParent: 64>, 'ImGuiScrollFlags_MaskX_': <ImGuiScrollFlags_.ImGuiScrollFlags_MaskX_: 21>, 'ImGuiScrollFlags_MaskY_': <ImGuiScrollFlags_.ImGuiScrollFlags_MaskY_: 42>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiSelectableFlagsPrivate_:
    """
    Members:
    
      ImGuiSelectableFlags_NoHoldingActiveID
    
      ImGuiSelectableFlags_SelectOnNav
    
      ImGuiSelectableFlags_SelectOnClick
    
      ImGuiSelectableFlags_SelectOnRelease
    
      ImGuiSelectableFlags_SpanAvailWidth
    
      ImGuiSelectableFlags_SetNavIdOnHover
    
      ImGuiSelectableFlags_NoPadWithHalfSpacing
    
      ImGuiSelectableFlags_NoSetKeyOwner
    """
    ImGuiSelectableFlags_NoHoldingActiveID: typing.ClassVar[ImGuiSelectableFlagsPrivate_]  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_NoHoldingActiveID: 1048576>
    ImGuiSelectableFlags_NoPadWithHalfSpacing: typing.ClassVar[ImGuiSelectableFlagsPrivate_]  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_NoPadWithHalfSpacing: 67108864>
    ImGuiSelectableFlags_NoSetKeyOwner: typing.ClassVar[ImGuiSelectableFlagsPrivate_]  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_NoSetKeyOwner: 134217728>
    ImGuiSelectableFlags_SelectOnClick: typing.ClassVar[ImGuiSelectableFlagsPrivate_]  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SelectOnClick: 4194304>
    ImGuiSelectableFlags_SelectOnNav: typing.ClassVar[ImGuiSelectableFlagsPrivate_]  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SelectOnNav: 2097152>
    ImGuiSelectableFlags_SelectOnRelease: typing.ClassVar[ImGuiSelectableFlagsPrivate_]  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SelectOnRelease: 8388608>
    ImGuiSelectableFlags_SetNavIdOnHover: typing.ClassVar[ImGuiSelectableFlagsPrivate_]  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SetNavIdOnHover: 33554432>
    ImGuiSelectableFlags_SpanAvailWidth: typing.ClassVar[ImGuiSelectableFlagsPrivate_]  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SpanAvailWidth: 16777216>
    __members__: typing.ClassVar[dict[str, ImGuiSelectableFlagsPrivate_]]  # value = {'ImGuiSelectableFlags_NoHoldingActiveID': <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_NoHoldingActiveID: 1048576>, 'ImGuiSelectableFlags_SelectOnNav': <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SelectOnNav: 2097152>, 'ImGuiSelectableFlags_SelectOnClick': <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SelectOnClick: 4194304>, 'ImGuiSelectableFlags_SelectOnRelease': <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SelectOnRelease: 8388608>, 'ImGuiSelectableFlags_SpanAvailWidth': <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SpanAvailWidth: 16777216>, 'ImGuiSelectableFlags_SetNavIdOnHover': <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SetNavIdOnHover: 33554432>, 'ImGuiSelectableFlags_NoPadWithHalfSpacing': <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_NoPadWithHalfSpacing: 67108864>, 'ImGuiSelectableFlags_NoSetKeyOwner': <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_NoSetKeyOwner: 134217728>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiSelectableFlags_:
    """
    Members:
    
      ImGuiSelectableFlags_None
    
      ImGuiSelectableFlags_DontClosePopups
    
      ImGuiSelectableFlags_SpanAllColumns
    
      ImGuiSelectableFlags_AllowDoubleClick
    
      ImGuiSelectableFlags_Disabled
    
      ImGuiSelectableFlags_AllowOverlap
    """
    ImGuiSelectableFlags_AllowDoubleClick: typing.ClassVar[ImGuiSelectableFlags_]  # value = <ImGuiSelectableFlags_.ImGuiSelectableFlags_AllowDoubleClick: 4>
    ImGuiSelectableFlags_AllowOverlap: typing.ClassVar[ImGuiSelectableFlags_]  # value = <ImGuiSelectableFlags_.ImGuiSelectableFlags_AllowOverlap: 16>
    ImGuiSelectableFlags_Disabled: typing.ClassVar[ImGuiSelectableFlags_]  # value = <ImGuiSelectableFlags_.ImGuiSelectableFlags_Disabled: 8>
    ImGuiSelectableFlags_DontClosePopups: typing.ClassVar[ImGuiSelectableFlags_]  # value = <ImGuiSelectableFlags_.ImGuiSelectableFlags_DontClosePopups: 1>
    ImGuiSelectableFlags_None: typing.ClassVar[ImGuiSelectableFlags_]  # value = <ImGuiSelectableFlags_.ImGuiSelectableFlags_None: 0>
    ImGuiSelectableFlags_SpanAllColumns: typing.ClassVar[ImGuiSelectableFlags_]  # value = <ImGuiSelectableFlags_.ImGuiSelectableFlags_SpanAllColumns: 2>
    __members__: typing.ClassVar[dict[str, ImGuiSelectableFlags_]]  # value = {'ImGuiSelectableFlags_None': <ImGuiSelectableFlags_.ImGuiSelectableFlags_None: 0>, 'ImGuiSelectableFlags_DontClosePopups': <ImGuiSelectableFlags_.ImGuiSelectableFlags_DontClosePopups: 1>, 'ImGuiSelectableFlags_SpanAllColumns': <ImGuiSelectableFlags_.ImGuiSelectableFlags_SpanAllColumns: 2>, 'ImGuiSelectableFlags_AllowDoubleClick': <ImGuiSelectableFlags_.ImGuiSelectableFlags_AllowDoubleClick: 4>, 'ImGuiSelectableFlags_Disabled': <ImGuiSelectableFlags_.ImGuiSelectableFlags_Disabled: 8>, 'ImGuiSelectableFlags_AllowOverlap': <ImGuiSelectableFlags_.ImGuiSelectableFlags_AllowOverlap: 16>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiSeparatorFlags_:
    """
    Members:
    
      ImGuiSeparatorFlags_None
    
      ImGuiSeparatorFlags_Horizontal
    
      ImGuiSeparatorFlags_Vertical
    
      ImGuiSeparatorFlags_SpanAllColumns
    """
    ImGuiSeparatorFlags_Horizontal: typing.ClassVar[ImGuiSeparatorFlags_]  # value = <ImGuiSeparatorFlags_.ImGuiSeparatorFlags_Horizontal: 1>
    ImGuiSeparatorFlags_None: typing.ClassVar[ImGuiSeparatorFlags_]  # value = <ImGuiSeparatorFlags_.ImGuiSeparatorFlags_None: 0>
    ImGuiSeparatorFlags_SpanAllColumns: typing.ClassVar[ImGuiSeparatorFlags_]  # value = <ImGuiSeparatorFlags_.ImGuiSeparatorFlags_SpanAllColumns: 4>
    ImGuiSeparatorFlags_Vertical: typing.ClassVar[ImGuiSeparatorFlags_]  # value = <ImGuiSeparatorFlags_.ImGuiSeparatorFlags_Vertical: 2>
    __members__: typing.ClassVar[dict[str, ImGuiSeparatorFlags_]]  # value = {'ImGuiSeparatorFlags_None': <ImGuiSeparatorFlags_.ImGuiSeparatorFlags_None: 0>, 'ImGuiSeparatorFlags_Horizontal': <ImGuiSeparatorFlags_.ImGuiSeparatorFlags_Horizontal: 1>, 'ImGuiSeparatorFlags_Vertical': <ImGuiSeparatorFlags_.ImGuiSeparatorFlags_Vertical: 2>, 'ImGuiSeparatorFlags_SpanAllColumns': <ImGuiSeparatorFlags_.ImGuiSeparatorFlags_SpanAllColumns: 4>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiSettingsHandler:
    TypeHash: int
    TypeName: str
    UserData: capsule
    def __init__(self) -> None:
        ...
class ImGuiShrinkWidthItem:
    Index: int
    InitialWidth: float
    Width: float
class ImGuiSizeCallbackData:
    CurrentSize: ImVec2
    DesiredSize: ImVec2
    Pos: ImVec2
    UserData: capsule
class ImGuiSliderFlagsPrivate_:
    """
    Members:
    
      ImGuiSliderFlags_Vertical
    
      ImGuiSliderFlags_ReadOnly
    """
    ImGuiSliderFlags_ReadOnly: typing.ClassVar[ImGuiSliderFlagsPrivate_]  # value = <ImGuiSliderFlagsPrivate_.ImGuiSliderFlags_ReadOnly: 2097152>
    ImGuiSliderFlags_Vertical: typing.ClassVar[ImGuiSliderFlagsPrivate_]  # value = <ImGuiSliderFlagsPrivate_.ImGuiSliderFlags_Vertical: 1048576>
    __members__: typing.ClassVar[dict[str, ImGuiSliderFlagsPrivate_]]  # value = {'ImGuiSliderFlags_Vertical': <ImGuiSliderFlagsPrivate_.ImGuiSliderFlags_Vertical: 1048576>, 'ImGuiSliderFlags_ReadOnly': <ImGuiSliderFlagsPrivate_.ImGuiSliderFlags_ReadOnly: 2097152>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiSliderFlags_:
    """
    Members:
    
      ImGuiSliderFlags_None
    
      ImGuiSliderFlags_AlwaysClamp
    
      ImGuiSliderFlags_Logarithmic
    
      ImGuiSliderFlags_NoRoundToFormat
    
      ImGuiSliderFlags_NoInput
    
      ImGuiSliderFlags_WrapAround
    
      ImGuiSliderFlags_InvalidMask_
    """
    ImGuiSliderFlags_AlwaysClamp: typing.ClassVar[ImGuiSliderFlags_]  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_AlwaysClamp: 16>
    ImGuiSliderFlags_InvalidMask_: typing.ClassVar[ImGuiSliderFlags_]  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_InvalidMask_: 1879048207>
    ImGuiSliderFlags_Logarithmic: typing.ClassVar[ImGuiSliderFlags_]  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_Logarithmic: 32>
    ImGuiSliderFlags_NoInput: typing.ClassVar[ImGuiSliderFlags_]  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_NoInput: 128>
    ImGuiSliderFlags_NoRoundToFormat: typing.ClassVar[ImGuiSliderFlags_]  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_NoRoundToFormat: 64>
    ImGuiSliderFlags_None: typing.ClassVar[ImGuiSliderFlags_]  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_None: 0>
    ImGuiSliderFlags_WrapAround: typing.ClassVar[ImGuiSliderFlags_]  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_WrapAround: 256>
    __members__: typing.ClassVar[dict[str, ImGuiSliderFlags_]]  # value = {'ImGuiSliderFlags_None': <ImGuiSliderFlags_.ImGuiSliderFlags_None: 0>, 'ImGuiSliderFlags_AlwaysClamp': <ImGuiSliderFlags_.ImGuiSliderFlags_AlwaysClamp: 16>, 'ImGuiSliderFlags_Logarithmic': <ImGuiSliderFlags_.ImGuiSliderFlags_Logarithmic: 32>, 'ImGuiSliderFlags_NoRoundToFormat': <ImGuiSliderFlags_.ImGuiSliderFlags_NoRoundToFormat: 64>, 'ImGuiSliderFlags_NoInput': <ImGuiSliderFlags_.ImGuiSliderFlags_NoInput: 128>, 'ImGuiSliderFlags_WrapAround': <ImGuiSliderFlags_.ImGuiSliderFlags_WrapAround: 256>, 'ImGuiSliderFlags_InvalidMask_': <ImGuiSliderFlags_.ImGuiSliderFlags_InvalidMask_: 1879048207>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiSortDirection:
    """
    Members:
    
      ImGuiSortDirection_None
    
      ImGuiSortDirection_Ascending
    
      ImGuiSortDirection_Descending
    """
    ImGuiSortDirection_Ascending: typing.ClassVar[ImGuiSortDirection]  # value = <ImGuiSortDirection.ImGuiSortDirection_Ascending: 1>
    ImGuiSortDirection_Descending: typing.ClassVar[ImGuiSortDirection]  # value = <ImGuiSortDirection.ImGuiSortDirection_Descending: 2>
    ImGuiSortDirection_None: typing.ClassVar[ImGuiSortDirection]  # value = <ImGuiSortDirection.ImGuiSortDirection_None: 0>
    __members__: typing.ClassVar[dict[str, ImGuiSortDirection]]  # value = {'ImGuiSortDirection_None': <ImGuiSortDirection.ImGuiSortDirection_None: 0>, 'ImGuiSortDirection_Ascending': <ImGuiSortDirection.ImGuiSortDirection_Ascending: 1>, 'ImGuiSortDirection_Descending': <ImGuiSortDirection.ImGuiSortDirection_Descending: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiStackLevelInfo:
    DataType: int
    ID: int
    QueryFrameCount: int
    QuerySuccess: bool
    def __init__(self) -> None:
        ...
    @property
    def Desc(self) -> Arr_char:
        ...
class ImGuiStackSizes:
    SizeOfBeginPopupStack: int
    SizeOfColorStack: int
    SizeOfDisabledStack: int
    SizeOfFocusScopeStack: int
    SizeOfFontStack: int
    SizeOfGroupStack: int
    SizeOfIDStack: int
    SizeOfItemFlagsStack: int
    SizeOfStyleVarStack: int
    def CompareWithContextState(self, ctx: ImGuiContext) -> None:
        ...
    def SetToContextState(self, ctx: ImGuiContext) -> None:
        ...
    def __init__(self) -> None:
        ...
class ImGuiStorage:
    Data: ImVector_ImGuiStoragePair
    def BuildSortByKey(self) -> None:
        ...
    def Clear(self) -> None:
        ...
    def GetBool(self, key: int, default_val: bool = False) -> bool:
        ...
    def GetBoolRef(self, key: int, default_val: bool = False) -> bool:
        ...
    def GetFloat(self, key: int, default_val: float = 0.0) -> float:
        ...
    def GetFloatRef(self, key: int, default_val: float = 0.0) -> float:
        ...
    def GetInt(self, key: int, default_val: int = 0) -> int:
        ...
    def GetIntRef(self, key: int, default_val: int = 0) -> int:
        ...
    def GetVoidPtr(self, key: int) -> capsule:
        ...
    def GetVoidPtrRef(self, key: int, default_val: capsule = 0) -> capsule:
        ...
    def SetAllInt(self, val: int) -> None:
        ...
    def SetBool(self, key: int, val: bool) -> None:
        ...
    def SetFloat(self, key: int, val: float) -> None:
        ...
    def SetInt(self, key: int, val: int) -> None:
        ...
    def SetVoidPtr(self, key: int, val: capsule) -> None:
        ...
class ImGuiStoragePair:
    key: int
    val_f: float
    val_i: int
    val_p: capsule
    @typing.overload
    def __init__(self, _key: int, _val: int) -> None:
        ...
    @typing.overload
    def __init__(self, _key: int, _val: float) -> None:
        ...
    @typing.overload
    def __init__(self, _key: int, _val: capsule) -> None:
        ...
class ImGuiStyle:
    Alpha: float
    AntiAliasedFill: bool
    AntiAliasedLines: bool
    AntiAliasedLinesUseTex: bool
    ButtonTextAlign: ImVec2
    CellPadding: ImVec2
    ChildBorderSize: float
    ChildRounding: float
    CircleTessellationMaxError: float
    ColorButtonPosition: ImGuiDir
    ColumnsMinSpacing: float
    CurveTessellationTol: float
    DisabledAlpha: float
    DisplaySafeAreaPadding: ImVec2
    DisplayWindowPadding: ImVec2
    DockingSeparatorSize: float
    FrameBorderSize: float
    FramePadding: ImVec2
    FrameRounding: float
    GrabMinSize: float
    GrabRounding: float
    HoverDelayNormal: float
    HoverDelayShort: float
    HoverFlagsForTooltipMouse: int
    HoverFlagsForTooltipNav: int
    HoverStationaryDelay: float
    IndentSpacing: float
    ItemInnerSpacing: ImVec2
    ItemSpacing: ImVec2
    LogSliderDeadzone: float
    MouseCursorScale: float
    PopupBorderSize: float
    PopupRounding: float
    ScrollbarRounding: float
    ScrollbarSize: float
    SelectableTextAlign: ImVec2
    SeparatorTextAlign: ImVec2
    SeparatorTextBorderSize: float
    SeparatorTextPadding: ImVec2
    TabBarBorderSize: float
    TabBorderSize: float
    TabMinWidthForCloseButton: float
    TabRounding: float
    TableAngledHeadersAngle: float
    TableAngledHeadersTextAlign: ImVec2
    TouchExtraPadding: ImVec2
    WindowBorderSize: float
    WindowMenuButtonPosition: ImGuiDir
    WindowMinSize: ImVec2
    WindowPadding: ImVec2
    WindowRounding: float
    WindowTitleAlign: ImVec2
    def ScaleAllSizes(self, scale_factor: float) -> None:
        ...
    def __init__(self) -> None:
        ...
    @property
    def Colors(self) -> Arr_ImVec4:
        ...
class ImGuiStyleMod:
    VarIdx: int
    @typing.overload
    def __init__(self, idx: int, v: int) -> None:
        ...
    @typing.overload
    def __init__(self, idx: int, v: float) -> None:
        ...
    @typing.overload
    def __init__(self, idx: int, v: ImVec2) -> None:
        ...
class ImGuiStyleVar_:
    """
    Members:
    
      ImGuiStyleVar_Alpha
    
      ImGuiStyleVar_DisabledAlpha
    
      ImGuiStyleVar_WindowPadding
    
      ImGuiStyleVar_WindowRounding
    
      ImGuiStyleVar_WindowBorderSize
    
      ImGuiStyleVar_WindowMinSize
    
      ImGuiStyleVar_WindowTitleAlign
    
      ImGuiStyleVar_ChildRounding
    
      ImGuiStyleVar_ChildBorderSize
    
      ImGuiStyleVar_PopupRounding
    
      ImGuiStyleVar_PopupBorderSize
    
      ImGuiStyleVar_FramePadding
    
      ImGuiStyleVar_FrameRounding
    
      ImGuiStyleVar_FrameBorderSize
    
      ImGuiStyleVar_ItemSpacing
    
      ImGuiStyleVar_ItemInnerSpacing
    
      ImGuiStyleVar_IndentSpacing
    
      ImGuiStyleVar_CellPadding
    
      ImGuiStyleVar_ScrollbarSize
    
      ImGuiStyleVar_ScrollbarRounding
    
      ImGuiStyleVar_GrabMinSize
    
      ImGuiStyleVar_GrabRounding
    
      ImGuiStyleVar_TabRounding
    
      ImGuiStyleVar_TabBorderSize
    
      ImGuiStyleVar_TabBarBorderSize
    
      ImGuiStyleVar_TableAngledHeadersAngle
    
      ImGuiStyleVar_TableAngledHeadersTextAlign
    
      ImGuiStyleVar_ButtonTextAlign
    
      ImGuiStyleVar_SelectableTextAlign
    
      ImGuiStyleVar_SeparatorTextBorderSize
    
      ImGuiStyleVar_SeparatorTextAlign
    
      ImGuiStyleVar_SeparatorTextPadding
    
      ImGuiStyleVar_DockingSeparatorSize
    
      ImGuiStyleVar_COUNT
    """
    ImGuiStyleVar_Alpha: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_Alpha: 0>
    ImGuiStyleVar_ButtonTextAlign: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_ButtonTextAlign: 27>
    ImGuiStyleVar_COUNT: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_COUNT: 33>
    ImGuiStyleVar_CellPadding: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_CellPadding: 17>
    ImGuiStyleVar_ChildBorderSize: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_ChildBorderSize: 8>
    ImGuiStyleVar_ChildRounding: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_ChildRounding: 7>
    ImGuiStyleVar_DisabledAlpha: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_DisabledAlpha: 1>
    ImGuiStyleVar_DockingSeparatorSize: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_DockingSeparatorSize: 32>
    ImGuiStyleVar_FrameBorderSize: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_FrameBorderSize: 13>
    ImGuiStyleVar_FramePadding: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_FramePadding: 11>
    ImGuiStyleVar_FrameRounding: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_FrameRounding: 12>
    ImGuiStyleVar_GrabMinSize: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_GrabMinSize: 20>
    ImGuiStyleVar_GrabRounding: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_GrabRounding: 21>
    ImGuiStyleVar_IndentSpacing: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_IndentSpacing: 16>
    ImGuiStyleVar_ItemInnerSpacing: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_ItemInnerSpacing: 15>
    ImGuiStyleVar_ItemSpacing: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_ItemSpacing: 14>
    ImGuiStyleVar_PopupBorderSize: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_PopupBorderSize: 10>
    ImGuiStyleVar_PopupRounding: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_PopupRounding: 9>
    ImGuiStyleVar_ScrollbarRounding: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_ScrollbarRounding: 19>
    ImGuiStyleVar_ScrollbarSize: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_ScrollbarSize: 18>
    ImGuiStyleVar_SelectableTextAlign: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_SelectableTextAlign: 28>
    ImGuiStyleVar_SeparatorTextAlign: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_SeparatorTextAlign: 30>
    ImGuiStyleVar_SeparatorTextBorderSize: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_SeparatorTextBorderSize: 29>
    ImGuiStyleVar_SeparatorTextPadding: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_SeparatorTextPadding: 31>
    ImGuiStyleVar_TabBarBorderSize: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_TabBarBorderSize: 24>
    ImGuiStyleVar_TabBorderSize: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_TabBorderSize: 23>
    ImGuiStyleVar_TabRounding: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_TabRounding: 22>
    ImGuiStyleVar_TableAngledHeadersAngle: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_TableAngledHeadersAngle: 25>
    ImGuiStyleVar_TableAngledHeadersTextAlign: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_TableAngledHeadersTextAlign: 26>
    ImGuiStyleVar_WindowBorderSize: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_WindowBorderSize: 4>
    ImGuiStyleVar_WindowMinSize: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_WindowMinSize: 5>
    ImGuiStyleVar_WindowPadding: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_WindowPadding: 2>
    ImGuiStyleVar_WindowRounding: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_WindowRounding: 3>
    ImGuiStyleVar_WindowTitleAlign: typing.ClassVar[ImGuiStyleVar_]  # value = <ImGuiStyleVar_.ImGuiStyleVar_WindowTitleAlign: 6>
    __members__: typing.ClassVar[dict[str, ImGuiStyleVar_]]  # value = {'ImGuiStyleVar_Alpha': <ImGuiStyleVar_.ImGuiStyleVar_Alpha: 0>, 'ImGuiStyleVar_DisabledAlpha': <ImGuiStyleVar_.ImGuiStyleVar_DisabledAlpha: 1>, 'ImGuiStyleVar_WindowPadding': <ImGuiStyleVar_.ImGuiStyleVar_WindowPadding: 2>, 'ImGuiStyleVar_WindowRounding': <ImGuiStyleVar_.ImGuiStyleVar_WindowRounding: 3>, 'ImGuiStyleVar_WindowBorderSize': <ImGuiStyleVar_.ImGuiStyleVar_WindowBorderSize: 4>, 'ImGuiStyleVar_WindowMinSize': <ImGuiStyleVar_.ImGuiStyleVar_WindowMinSize: 5>, 'ImGuiStyleVar_WindowTitleAlign': <ImGuiStyleVar_.ImGuiStyleVar_WindowTitleAlign: 6>, 'ImGuiStyleVar_ChildRounding': <ImGuiStyleVar_.ImGuiStyleVar_ChildRounding: 7>, 'ImGuiStyleVar_ChildBorderSize': <ImGuiStyleVar_.ImGuiStyleVar_ChildBorderSize: 8>, 'ImGuiStyleVar_PopupRounding': <ImGuiStyleVar_.ImGuiStyleVar_PopupRounding: 9>, 'ImGuiStyleVar_PopupBorderSize': <ImGuiStyleVar_.ImGuiStyleVar_PopupBorderSize: 10>, 'ImGuiStyleVar_FramePadding': <ImGuiStyleVar_.ImGuiStyleVar_FramePadding: 11>, 'ImGuiStyleVar_FrameRounding': <ImGuiStyleVar_.ImGuiStyleVar_FrameRounding: 12>, 'ImGuiStyleVar_FrameBorderSize': <ImGuiStyleVar_.ImGuiStyleVar_FrameBorderSize: 13>, 'ImGuiStyleVar_ItemSpacing': <ImGuiStyleVar_.ImGuiStyleVar_ItemSpacing: 14>, 'ImGuiStyleVar_ItemInnerSpacing': <ImGuiStyleVar_.ImGuiStyleVar_ItemInnerSpacing: 15>, 'ImGuiStyleVar_IndentSpacing': <ImGuiStyleVar_.ImGuiStyleVar_IndentSpacing: 16>, 'ImGuiStyleVar_CellPadding': <ImGuiStyleVar_.ImGuiStyleVar_CellPadding: 17>, 'ImGuiStyleVar_ScrollbarSize': <ImGuiStyleVar_.ImGuiStyleVar_ScrollbarSize: 18>, 'ImGuiStyleVar_ScrollbarRounding': <ImGuiStyleVar_.ImGuiStyleVar_ScrollbarRounding: 19>, 'ImGuiStyleVar_GrabMinSize': <ImGuiStyleVar_.ImGuiStyleVar_GrabMinSize: 20>, 'ImGuiStyleVar_GrabRounding': <ImGuiStyleVar_.ImGuiStyleVar_GrabRounding: 21>, 'ImGuiStyleVar_TabRounding': <ImGuiStyleVar_.ImGuiStyleVar_TabRounding: 22>, 'ImGuiStyleVar_TabBorderSize': <ImGuiStyleVar_.ImGuiStyleVar_TabBorderSize: 23>, 'ImGuiStyleVar_TabBarBorderSize': <ImGuiStyleVar_.ImGuiStyleVar_TabBarBorderSize: 24>, 'ImGuiStyleVar_TableAngledHeadersAngle': <ImGuiStyleVar_.ImGuiStyleVar_TableAngledHeadersAngle: 25>, 'ImGuiStyleVar_TableAngledHeadersTextAlign': <ImGuiStyleVar_.ImGuiStyleVar_TableAngledHeadersTextAlign: 26>, 'ImGuiStyleVar_ButtonTextAlign': <ImGuiStyleVar_.ImGuiStyleVar_ButtonTextAlign: 27>, 'ImGuiStyleVar_SelectableTextAlign': <ImGuiStyleVar_.ImGuiStyleVar_SelectableTextAlign: 28>, 'ImGuiStyleVar_SeparatorTextBorderSize': <ImGuiStyleVar_.ImGuiStyleVar_SeparatorTextBorderSize: 29>, 'ImGuiStyleVar_SeparatorTextAlign': <ImGuiStyleVar_.ImGuiStyleVar_SeparatorTextAlign: 30>, 'ImGuiStyleVar_SeparatorTextPadding': <ImGuiStyleVar_.ImGuiStyleVar_SeparatorTextPadding: 31>, 'ImGuiStyleVar_DockingSeparatorSize': <ImGuiStyleVar_.ImGuiStyleVar_DockingSeparatorSize: 32>, 'ImGuiStyleVar_COUNT': <ImGuiStyleVar_.ImGuiStyleVar_COUNT: 33>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTabBar:
    BackupCursorPos: ImVec2
    BarRect: ImRect
    BeginCount: int
    CurrFrameVisible: int
    CurrTabsContentsHeight: float
    Flags: int
    FramePadding: ImVec2
    ID: int
    ItemSpacingY: float
    LastTabItemIdx: int
    NextSelectedTabId: int
    PrevFrameVisible: int
    PrevTabsContentsHeight: float
    ReorderRequestOffset: int
    ReorderRequestTabId: int
    ScrollingAnim: float
    ScrollingRectMaxX: float
    ScrollingRectMinX: float
    ScrollingSpeed: float
    ScrollingTarget: float
    ScrollingTargetDistToVisibility: float
    SelectedTabId: int
    SeparatorMaxX: float
    SeparatorMinX: float
    Tabs: ImVector_ImGuiTabItem
    TabsActiveCount: int
    TabsAddedNew: bool
    TabsNames: ImGuiTextBuffer
    VisibleTabId: int
    VisibleTabWasSubmitted: bool
    WantLayout: bool
    WidthAllTabs: float
    WidthAllTabsIdeal: float
    def __init__(self) -> None:
        ...
class ImGuiTabBarFlagsPrivate_:
    """
    Members:
    
      ImGuiTabBarFlags_DockNode
    
      ImGuiTabBarFlags_IsFocused
    
      ImGuiTabBarFlags_SaveSettings
    """
    ImGuiTabBarFlags_DockNode: typing.ClassVar[ImGuiTabBarFlagsPrivate_]  # value = <ImGuiTabBarFlagsPrivate_.ImGuiTabBarFlags_DockNode: 1048576>
    ImGuiTabBarFlags_IsFocused: typing.ClassVar[ImGuiTabBarFlagsPrivate_]  # value = <ImGuiTabBarFlagsPrivate_.ImGuiTabBarFlags_IsFocused: 2097152>
    ImGuiTabBarFlags_SaveSettings: typing.ClassVar[ImGuiTabBarFlagsPrivate_]  # value = <ImGuiTabBarFlagsPrivate_.ImGuiTabBarFlags_SaveSettings: 4194304>
    __members__: typing.ClassVar[dict[str, ImGuiTabBarFlagsPrivate_]]  # value = {'ImGuiTabBarFlags_DockNode': <ImGuiTabBarFlagsPrivate_.ImGuiTabBarFlags_DockNode: 1048576>, 'ImGuiTabBarFlags_IsFocused': <ImGuiTabBarFlagsPrivate_.ImGuiTabBarFlags_IsFocused: 2097152>, 'ImGuiTabBarFlags_SaveSettings': <ImGuiTabBarFlagsPrivate_.ImGuiTabBarFlags_SaveSettings: 4194304>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTabBarFlags_:
    """
    Members:
    
      ImGuiTabBarFlags_None
    
      ImGuiTabBarFlags_Reorderable
    
      ImGuiTabBarFlags_AutoSelectNewTabs
    
      ImGuiTabBarFlags_TabListPopupButton
    
      ImGuiTabBarFlags_NoCloseWithMiddleMouseButton
    
      ImGuiTabBarFlags_NoTabListScrollingButtons
    
      ImGuiTabBarFlags_NoTooltip
    
      ImGuiTabBarFlags_DrawSelectedOverline
    
      ImGuiTabBarFlags_FittingPolicyResizeDown
    
      ImGuiTabBarFlags_FittingPolicyScroll
    
      ImGuiTabBarFlags_FittingPolicyMask_
    
      ImGuiTabBarFlags_FittingPolicyDefault_
    """
    ImGuiTabBarFlags_AutoSelectNewTabs: typing.ClassVar[ImGuiTabBarFlags_]  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_AutoSelectNewTabs: 2>
    ImGuiTabBarFlags_DrawSelectedOverline: typing.ClassVar[ImGuiTabBarFlags_]  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_DrawSelectedOverline: 64>
    ImGuiTabBarFlags_FittingPolicyDefault_: typing.ClassVar[ImGuiTabBarFlags_]  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_FittingPolicyResizeDown: 128>
    ImGuiTabBarFlags_FittingPolicyMask_: typing.ClassVar[ImGuiTabBarFlags_]  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_FittingPolicyMask_: 384>
    ImGuiTabBarFlags_FittingPolicyResizeDown: typing.ClassVar[ImGuiTabBarFlags_]  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_FittingPolicyResizeDown: 128>
    ImGuiTabBarFlags_FittingPolicyScroll: typing.ClassVar[ImGuiTabBarFlags_]  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_FittingPolicyScroll: 256>
    ImGuiTabBarFlags_NoCloseWithMiddleMouseButton: typing.ClassVar[ImGuiTabBarFlags_]  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_NoCloseWithMiddleMouseButton: 8>
    ImGuiTabBarFlags_NoTabListScrollingButtons: typing.ClassVar[ImGuiTabBarFlags_]  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_NoTabListScrollingButtons: 16>
    ImGuiTabBarFlags_NoTooltip: typing.ClassVar[ImGuiTabBarFlags_]  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_NoTooltip: 32>
    ImGuiTabBarFlags_None: typing.ClassVar[ImGuiTabBarFlags_]  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_None: 0>
    ImGuiTabBarFlags_Reorderable: typing.ClassVar[ImGuiTabBarFlags_]  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_Reorderable: 1>
    ImGuiTabBarFlags_TabListPopupButton: typing.ClassVar[ImGuiTabBarFlags_]  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_TabListPopupButton: 4>
    __members__: typing.ClassVar[dict[str, ImGuiTabBarFlags_]]  # value = {'ImGuiTabBarFlags_None': <ImGuiTabBarFlags_.ImGuiTabBarFlags_None: 0>, 'ImGuiTabBarFlags_Reorderable': <ImGuiTabBarFlags_.ImGuiTabBarFlags_Reorderable: 1>, 'ImGuiTabBarFlags_AutoSelectNewTabs': <ImGuiTabBarFlags_.ImGuiTabBarFlags_AutoSelectNewTabs: 2>, 'ImGuiTabBarFlags_TabListPopupButton': <ImGuiTabBarFlags_.ImGuiTabBarFlags_TabListPopupButton: 4>, 'ImGuiTabBarFlags_NoCloseWithMiddleMouseButton': <ImGuiTabBarFlags_.ImGuiTabBarFlags_NoCloseWithMiddleMouseButton: 8>, 'ImGuiTabBarFlags_NoTabListScrollingButtons': <ImGuiTabBarFlags_.ImGuiTabBarFlags_NoTabListScrollingButtons: 16>, 'ImGuiTabBarFlags_NoTooltip': <ImGuiTabBarFlags_.ImGuiTabBarFlags_NoTooltip: 32>, 'ImGuiTabBarFlags_DrawSelectedOverline': <ImGuiTabBarFlags_.ImGuiTabBarFlags_DrawSelectedOverline: 64>, 'ImGuiTabBarFlags_FittingPolicyResizeDown': <ImGuiTabBarFlags_.ImGuiTabBarFlags_FittingPolicyResizeDown: 128>, 'ImGuiTabBarFlags_FittingPolicyScroll': <ImGuiTabBarFlags_.ImGuiTabBarFlags_FittingPolicyScroll: 256>, 'ImGuiTabBarFlags_FittingPolicyMask_': <ImGuiTabBarFlags_.ImGuiTabBarFlags_FittingPolicyMask_: 384>, 'ImGuiTabBarFlags_FittingPolicyDefault_': <ImGuiTabBarFlags_.ImGuiTabBarFlags_FittingPolicyResizeDown: 128>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTabItem:
    BeginOrder: int
    ContentWidth: float
    Flags: int
    ID: int
    IndexDuringLayout: int
    LastFrameSelected: int
    LastFrameVisible: int
    NameOffset: int
    Offset: float
    RequestedWidth: float
    WantClose: bool
    Width: float
    Window: ImGuiWindow
    def __init__(self) -> None:
        ...
class ImGuiTabItemFlagsPrivate_:
    """
    Members:
    
      ImGuiTabItemFlags_SectionMask_
    
      ImGuiTabItemFlags_NoCloseButton
    
      ImGuiTabItemFlags_Button
    
      ImGuiTabItemFlags_Unsorted
    """
    ImGuiTabItemFlags_Button: typing.ClassVar[ImGuiTabItemFlagsPrivate_]  # value = <ImGuiTabItemFlagsPrivate_.ImGuiTabItemFlags_Button: 2097152>
    ImGuiTabItemFlags_NoCloseButton: typing.ClassVar[ImGuiTabItemFlagsPrivate_]  # value = <ImGuiTabItemFlagsPrivate_.ImGuiTabItemFlags_NoCloseButton: 1048576>
    ImGuiTabItemFlags_SectionMask_: typing.ClassVar[ImGuiTabItemFlagsPrivate_]  # value = <ImGuiTabItemFlagsPrivate_.ImGuiTabItemFlags_SectionMask_: 192>
    ImGuiTabItemFlags_Unsorted: typing.ClassVar[ImGuiTabItemFlagsPrivate_]  # value = <ImGuiTabItemFlagsPrivate_.ImGuiTabItemFlags_Unsorted: 4194304>
    __members__: typing.ClassVar[dict[str, ImGuiTabItemFlagsPrivate_]]  # value = {'ImGuiTabItemFlags_SectionMask_': <ImGuiTabItemFlagsPrivate_.ImGuiTabItemFlags_SectionMask_: 192>, 'ImGuiTabItemFlags_NoCloseButton': <ImGuiTabItemFlagsPrivate_.ImGuiTabItemFlags_NoCloseButton: 1048576>, 'ImGuiTabItemFlags_Button': <ImGuiTabItemFlagsPrivate_.ImGuiTabItemFlags_Button: 2097152>, 'ImGuiTabItemFlags_Unsorted': <ImGuiTabItemFlagsPrivate_.ImGuiTabItemFlags_Unsorted: 4194304>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTabItemFlags_:
    """
    Members:
    
      ImGuiTabItemFlags_None
    
      ImGuiTabItemFlags_UnsavedDocument
    
      ImGuiTabItemFlags_SetSelected
    
      ImGuiTabItemFlags_NoCloseWithMiddleMouseButton
    
      ImGuiTabItemFlags_NoPushId
    
      ImGuiTabItemFlags_NoTooltip
    
      ImGuiTabItemFlags_NoReorder
    
      ImGuiTabItemFlags_Leading
    
      ImGuiTabItemFlags_Trailing
    
      ImGuiTabItemFlags_NoAssumedClosure
    """
    ImGuiTabItemFlags_Leading: typing.ClassVar[ImGuiTabItemFlags_]  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_Leading: 64>
    ImGuiTabItemFlags_NoAssumedClosure: typing.ClassVar[ImGuiTabItemFlags_]  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoAssumedClosure: 256>
    ImGuiTabItemFlags_NoCloseWithMiddleMouseButton: typing.ClassVar[ImGuiTabItemFlags_]  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoCloseWithMiddleMouseButton: 4>
    ImGuiTabItemFlags_NoPushId: typing.ClassVar[ImGuiTabItemFlags_]  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoPushId: 8>
    ImGuiTabItemFlags_NoReorder: typing.ClassVar[ImGuiTabItemFlags_]  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoReorder: 32>
    ImGuiTabItemFlags_NoTooltip: typing.ClassVar[ImGuiTabItemFlags_]  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoTooltip: 16>
    ImGuiTabItemFlags_None: typing.ClassVar[ImGuiTabItemFlags_]  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_None: 0>
    ImGuiTabItemFlags_SetSelected: typing.ClassVar[ImGuiTabItemFlags_]  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_SetSelected: 2>
    ImGuiTabItemFlags_Trailing: typing.ClassVar[ImGuiTabItemFlags_]  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_Trailing: 128>
    ImGuiTabItemFlags_UnsavedDocument: typing.ClassVar[ImGuiTabItemFlags_]  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_UnsavedDocument: 1>
    __members__: typing.ClassVar[dict[str, ImGuiTabItemFlags_]]  # value = {'ImGuiTabItemFlags_None': <ImGuiTabItemFlags_.ImGuiTabItemFlags_None: 0>, 'ImGuiTabItemFlags_UnsavedDocument': <ImGuiTabItemFlags_.ImGuiTabItemFlags_UnsavedDocument: 1>, 'ImGuiTabItemFlags_SetSelected': <ImGuiTabItemFlags_.ImGuiTabItemFlags_SetSelected: 2>, 'ImGuiTabItemFlags_NoCloseWithMiddleMouseButton': <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoCloseWithMiddleMouseButton: 4>, 'ImGuiTabItemFlags_NoPushId': <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoPushId: 8>, 'ImGuiTabItemFlags_NoTooltip': <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoTooltip: 16>, 'ImGuiTabItemFlags_NoReorder': <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoReorder: 32>, 'ImGuiTabItemFlags_Leading': <ImGuiTabItemFlags_.ImGuiTabItemFlags_Leading: 64>, 'ImGuiTabItemFlags_Trailing': <ImGuiTabItemFlags_.ImGuiTabItemFlags_Trailing: 128>, 'ImGuiTabItemFlags_NoAssumedClosure': <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoAssumedClosure: 256>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTable:
    AngledHeadersCount: int
    AngledHeadersHeight: float
    AngledHeadersSlope: float
    AutoFitSingleColumn: int
    Bg0ClipRectForDrawCmd: ImRect
    Bg2ClipRectForDrawCmd: ImRect
    Bg2DrawChannelCurrent: int
    Bg2DrawChannelUnfrozen: int
    BgClipRect: ImRect
    BorderColorLight: int
    BorderColorStrong: int
    BorderX1: float
    BorderX2: float
    CellPaddingX: float
    CellSpacingX1: float
    CellSpacingX2: float
    Columns: ImSpan_ImGuiTableColumn
    ColumnsAutoFitWidth: float
    ColumnsCount: int
    ColumnsEnabledCount: int
    ColumnsEnabledFixedCount: int
    ColumnsGivenWidth: float
    ColumnsNames: ImGuiTextBuffer
    ColumnsStretchSumWeights: float
    ContextPopupColumn: int
    CurrentColumn: int
    CurrentRow: int
    DeclColumnsCount: int
    DisableDefaultContextMenu: bool
    DisplayOrderToIndex: ImSpan_ImGuiTableColumnIdx
    DrawSplitter: ImDrawListSplitter
    DummyDrawChannel: int
    EnabledMaskByDisplayOrder: int
    EnabledMaskByIndex: int
    Flags: int
    FreezeColumnsCount: int
    FreezeColumnsRequest: int
    FreezeRowsCount: int
    FreezeRowsRequest: int
    HasScrollbarYCurr: bool
    HasScrollbarYPrev: bool
    HeldHeaderColumn: int
    HighlightColumnHeader: int
    HostBackupInnerClipRect: ImRect
    HostClipRect: ImRect
    HostIndentX: float
    HostSkipItems: bool
    HoveredColumnBody: int
    HoveredColumnBorder: int
    ID: int
    InnerClipRect: ImRect
    InnerRect: ImRect
    InnerWidth: float
    InnerWindow: ImGuiWindow
    InstanceCurrent: int
    InstanceDataExtra: ImVector_ImGuiTableInstanceData
    InstanceDataFirst: ImGuiTableInstanceData
    InstanceInteracted: int
    IsActiveIdAliveBeforeTable: bool
    IsActiveIdInTable: bool
    IsContextPopupOpen: bool
    IsDefaultDisplayOrder: bool
    IsDefaultSizingPolicy: bool
    IsInitializing: bool
    IsInsideRow: bool
    IsLayoutLocked: bool
    IsResetAllRequest: bool
    IsResetDisplayOrderRequest: bool
    IsSettingsDirty: bool
    IsSettingsRequestLoad: bool
    IsSortSpecsDirty: bool
    IsUnfrozenRows: bool
    IsUsingHeaders: bool
    LastFrameActive: int
    LastResizedColumn: int
    LastRowFlags: int
    LeftMostEnabledColumn: int
    LeftMostStretchedColumn: int
    MemoryCompacted: bool
    MinColumnWidth: float
    OuterPaddingX: float
    OuterRect: ImRect
    OuterWindow: ImGuiWindow
    RawData: capsule
    RefScale: float
    ReorderColumn: int
    ReorderColumnDir: int
    ResizeLockMinContentsX2: float
    ResizedColumn: int
    ResizedColumnNextWidth: float
    RightMostEnabledColumn: int
    RightMostStretchedColumn: int
    RowBgColorCounter: int
    RowCellData: ImSpan_ImGuiTableCellData
    RowCellDataCurrent: int
    RowCellPaddingY: float
    RowFlags: int
    RowIndentOffsetX: float
    RowMinHeight: float
    RowPosY1: float
    RowPosY2: float
    RowTextBaseline: float
    SettingsLoadedFlags: int
    SettingsOffset: int
    SortSpecs: ImGuiTableSortSpecs
    SortSpecsCount: int
    SortSpecsMulti: ImVector_ImGuiTableColumnSortSpecs
    SortSpecsSingle: ImGuiTableColumnSortSpecs
    TempData: ImGuiTableTempData
    VisibleMaskByIndex: int
    WorkRect: ImRect
    def __init__(self) -> None:
        ...
    @property
    def RowBgColor(self) -> Arr_unsigned_int:
        ...
class ImGuiTableBgTarget_:
    """
    Members:
    
      ImGuiTableBgTarget_None
    
      ImGuiTableBgTarget_RowBg0
    
      ImGuiTableBgTarget_RowBg1
    
      ImGuiTableBgTarget_CellBg
    """
    ImGuiTableBgTarget_CellBg: typing.ClassVar[ImGuiTableBgTarget_]  # value = <ImGuiTableBgTarget_.ImGuiTableBgTarget_CellBg: 3>
    ImGuiTableBgTarget_None: typing.ClassVar[ImGuiTableBgTarget_]  # value = <ImGuiTableBgTarget_.ImGuiTableBgTarget_None: 0>
    ImGuiTableBgTarget_RowBg0: typing.ClassVar[ImGuiTableBgTarget_]  # value = <ImGuiTableBgTarget_.ImGuiTableBgTarget_RowBg0: 1>
    ImGuiTableBgTarget_RowBg1: typing.ClassVar[ImGuiTableBgTarget_]  # value = <ImGuiTableBgTarget_.ImGuiTableBgTarget_RowBg1: 2>
    __members__: typing.ClassVar[dict[str, ImGuiTableBgTarget_]]  # value = {'ImGuiTableBgTarget_None': <ImGuiTableBgTarget_.ImGuiTableBgTarget_None: 0>, 'ImGuiTableBgTarget_RowBg0': <ImGuiTableBgTarget_.ImGuiTableBgTarget_RowBg0: 1>, 'ImGuiTableBgTarget_RowBg1': <ImGuiTableBgTarget_.ImGuiTableBgTarget_RowBg1: 2>, 'ImGuiTableBgTarget_CellBg': <ImGuiTableBgTarget_.ImGuiTableBgTarget_CellBg: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTableCellData:
    BgColor: int
    Column: int
class ImGuiTableColumn:
    AutoFitQueue: int
    CannotSkipItemsQueue: int
    ClipRect: ImRect
    ContentMaxXFrozen: float
    ContentMaxXHeadersIdeal: float
    ContentMaxXHeadersUsed: float
    ContentMaxXUnfrozen: float
    DisplayOrder: int
    DrawChannelCurrent: int
    DrawChannelFrozen: int
    DrawChannelUnfrozen: int
    Flags: int
    IndexWithinEnabledSet: int
    InitStretchWeightOrWidth: float
    IsEnabled: bool
    IsPreserveWidthAuto: bool
    IsRequestOutput: bool
    IsSkipItems: bool
    IsUserEnabled: bool
    IsUserEnabledNextFrame: bool
    IsVisibleX: bool
    IsVisibleY: bool
    ItemWidth: float
    MaxX: float
    MinX: float
    NameOffset: int
    NavLayerCurrent: int
    NextEnabledColumn: int
    PrevEnabledColumn: int
    SortDirection: int
    SortDirectionsAvailCount: int
    SortDirectionsAvailList: int
    SortDirectionsAvailMask: int
    SortOrder: int
    StretchWeight: float
    UserID: int
    WidthAuto: float
    WidthGiven: float
    WidthRequest: float
    WorkMaxX: float
    WorkMinX: float
    def __init__(self) -> None:
        ...
class ImGuiTableColumnFlags_:
    """
    Members:
    
      ImGuiTableColumnFlags_None
    
      ImGuiTableColumnFlags_Disabled
    
      ImGuiTableColumnFlags_DefaultHide
    
      ImGuiTableColumnFlags_DefaultSort
    
      ImGuiTableColumnFlags_WidthStretch
    
      ImGuiTableColumnFlags_WidthFixed
    
      ImGuiTableColumnFlags_NoResize
    
      ImGuiTableColumnFlags_NoReorder
    
      ImGuiTableColumnFlags_NoHide
    
      ImGuiTableColumnFlags_NoClip
    
      ImGuiTableColumnFlags_NoSort
    
      ImGuiTableColumnFlags_NoSortAscending
    
      ImGuiTableColumnFlags_NoSortDescending
    
      ImGuiTableColumnFlags_NoHeaderLabel
    
      ImGuiTableColumnFlags_NoHeaderWidth
    
      ImGuiTableColumnFlags_PreferSortAscending
    
      ImGuiTableColumnFlags_PreferSortDescending
    
      ImGuiTableColumnFlags_IndentEnable
    
      ImGuiTableColumnFlags_IndentDisable
    
      ImGuiTableColumnFlags_AngledHeader
    
      ImGuiTableColumnFlags_IsEnabled
    
      ImGuiTableColumnFlags_IsVisible
    
      ImGuiTableColumnFlags_IsSorted
    
      ImGuiTableColumnFlags_IsHovered
    
      ImGuiTableColumnFlags_WidthMask_
    
      ImGuiTableColumnFlags_IndentMask_
    
      ImGuiTableColumnFlags_StatusMask_
    
      ImGuiTableColumnFlags_NoDirectResize_
    """
    ImGuiTableColumnFlags_AngledHeader: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_AngledHeader: 262144>
    ImGuiTableColumnFlags_DefaultHide: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_DefaultHide: 2>
    ImGuiTableColumnFlags_DefaultSort: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_DefaultSort: 4>
    ImGuiTableColumnFlags_Disabled: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_Disabled: 1>
    ImGuiTableColumnFlags_IndentDisable: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IndentDisable: 131072>
    ImGuiTableColumnFlags_IndentEnable: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IndentEnable: 65536>
    ImGuiTableColumnFlags_IndentMask_: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IndentMask_: 196608>
    ImGuiTableColumnFlags_IsEnabled: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IsEnabled: 16777216>
    ImGuiTableColumnFlags_IsHovered: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IsHovered: 134217728>
    ImGuiTableColumnFlags_IsSorted: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IsSorted: 67108864>
    ImGuiTableColumnFlags_IsVisible: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IsVisible: 33554432>
    ImGuiTableColumnFlags_NoClip: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoClip: 256>
    ImGuiTableColumnFlags_NoDirectResize_: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoDirectResize_: 1073741824>
    ImGuiTableColumnFlags_NoHeaderLabel: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoHeaderLabel: 4096>
    ImGuiTableColumnFlags_NoHeaderWidth: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoHeaderWidth: 8192>
    ImGuiTableColumnFlags_NoHide: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoHide: 128>
    ImGuiTableColumnFlags_NoReorder: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoReorder: 64>
    ImGuiTableColumnFlags_NoResize: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoResize: 32>
    ImGuiTableColumnFlags_NoSort: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoSort: 512>
    ImGuiTableColumnFlags_NoSortAscending: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoSortAscending: 1024>
    ImGuiTableColumnFlags_NoSortDescending: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoSortDescending: 2048>
    ImGuiTableColumnFlags_None: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_None: 0>
    ImGuiTableColumnFlags_PreferSortAscending: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_PreferSortAscending: 16384>
    ImGuiTableColumnFlags_PreferSortDescending: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_PreferSortDescending: 32768>
    ImGuiTableColumnFlags_StatusMask_: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_StatusMask_: 251658240>
    ImGuiTableColumnFlags_WidthFixed: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_WidthFixed: 16>
    ImGuiTableColumnFlags_WidthMask_: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_WidthMask_: 24>
    ImGuiTableColumnFlags_WidthStretch: typing.ClassVar[ImGuiTableColumnFlags_]  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_WidthStretch: 8>
    __members__: typing.ClassVar[dict[str, ImGuiTableColumnFlags_]]  # value = {'ImGuiTableColumnFlags_None': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_None: 0>, 'ImGuiTableColumnFlags_Disabled': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_Disabled: 1>, 'ImGuiTableColumnFlags_DefaultHide': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_DefaultHide: 2>, 'ImGuiTableColumnFlags_DefaultSort': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_DefaultSort: 4>, 'ImGuiTableColumnFlags_WidthStretch': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_WidthStretch: 8>, 'ImGuiTableColumnFlags_WidthFixed': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_WidthFixed: 16>, 'ImGuiTableColumnFlags_NoResize': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoResize: 32>, 'ImGuiTableColumnFlags_NoReorder': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoReorder: 64>, 'ImGuiTableColumnFlags_NoHide': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoHide: 128>, 'ImGuiTableColumnFlags_NoClip': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoClip: 256>, 'ImGuiTableColumnFlags_NoSort': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoSort: 512>, 'ImGuiTableColumnFlags_NoSortAscending': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoSortAscending: 1024>, 'ImGuiTableColumnFlags_NoSortDescending': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoSortDescending: 2048>, 'ImGuiTableColumnFlags_NoHeaderLabel': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoHeaderLabel: 4096>, 'ImGuiTableColumnFlags_NoHeaderWidth': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoHeaderWidth: 8192>, 'ImGuiTableColumnFlags_PreferSortAscending': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_PreferSortAscending: 16384>, 'ImGuiTableColumnFlags_PreferSortDescending': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_PreferSortDescending: 32768>, 'ImGuiTableColumnFlags_IndentEnable': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IndentEnable: 65536>, 'ImGuiTableColumnFlags_IndentDisable': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IndentDisable: 131072>, 'ImGuiTableColumnFlags_AngledHeader': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_AngledHeader: 262144>, 'ImGuiTableColumnFlags_IsEnabled': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IsEnabled: 16777216>, 'ImGuiTableColumnFlags_IsVisible': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IsVisible: 33554432>, 'ImGuiTableColumnFlags_IsSorted': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IsSorted: 67108864>, 'ImGuiTableColumnFlags_IsHovered': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IsHovered: 134217728>, 'ImGuiTableColumnFlags_WidthMask_': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_WidthMask_: 24>, 'ImGuiTableColumnFlags_IndentMask_': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IndentMask_: 196608>, 'ImGuiTableColumnFlags_StatusMask_': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_StatusMask_: 251658240>, 'ImGuiTableColumnFlags_NoDirectResize_': <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoDirectResize_: 1073741824>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTableColumnSettings:
    DisplayOrder: int
    Index: int
    IsEnabled: int
    IsStretch: int
    SortDirection: int
    SortOrder: int
    UserID: int
    WidthOrWeight: float
    def __init__(self) -> None:
        ...
class ImGuiTableColumnSortSpecs:
    ColumnIndex: int
    ColumnUserID: int
    SortDirection: ImGuiSortDirection
    SortOrder: int
    def __init__(self) -> None:
        ...
class ImGuiTableFlags_:
    """
    Members:
    
      ImGuiTableFlags_None
    
      ImGuiTableFlags_Resizable
    
      ImGuiTableFlags_Reorderable
    
      ImGuiTableFlags_Hideable
    
      ImGuiTableFlags_Sortable
    
      ImGuiTableFlags_NoSavedSettings
    
      ImGuiTableFlags_ContextMenuInBody
    
      ImGuiTableFlags_RowBg
    
      ImGuiTableFlags_BordersInnerH
    
      ImGuiTableFlags_BordersOuterH
    
      ImGuiTableFlags_BordersInnerV
    
      ImGuiTableFlags_BordersOuterV
    
      ImGuiTableFlags_BordersH
    
      ImGuiTableFlags_BordersV
    
      ImGuiTableFlags_BordersInner
    
      ImGuiTableFlags_BordersOuter
    
      ImGuiTableFlags_Borders
    
      ImGuiTableFlags_NoBordersInBody
    
      ImGuiTableFlags_NoBordersInBodyUntilResize
    
      ImGuiTableFlags_SizingFixedFit
    
      ImGuiTableFlags_SizingFixedSame
    
      ImGuiTableFlags_SizingStretchProp
    
      ImGuiTableFlags_SizingStretchSame
    
      ImGuiTableFlags_NoHostExtendX
    
      ImGuiTableFlags_NoHostExtendY
    
      ImGuiTableFlags_NoKeepColumnsVisible
    
      ImGuiTableFlags_PreciseWidths
    
      ImGuiTableFlags_NoClip
    
      ImGuiTableFlags_PadOuterX
    
      ImGuiTableFlags_NoPadOuterX
    
      ImGuiTableFlags_NoPadInnerX
    
      ImGuiTableFlags_ScrollX
    
      ImGuiTableFlags_ScrollY
    
      ImGuiTableFlags_SortMulti
    
      ImGuiTableFlags_SortTristate
    
      ImGuiTableFlags_HighlightHoveredColumn
    
      ImGuiTableFlags_SizingMask_
    """
    ImGuiTableFlags_Borders: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_Borders: 1920>
    ImGuiTableFlags_BordersH: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersH: 384>
    ImGuiTableFlags_BordersInner: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersInner: 640>
    ImGuiTableFlags_BordersInnerH: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersInnerH: 128>
    ImGuiTableFlags_BordersInnerV: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersInnerV: 512>
    ImGuiTableFlags_BordersOuter: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersOuter: 1280>
    ImGuiTableFlags_BordersOuterH: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersOuterH: 256>
    ImGuiTableFlags_BordersOuterV: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersOuterV: 1024>
    ImGuiTableFlags_BordersV: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersV: 1536>
    ImGuiTableFlags_ContextMenuInBody: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_ContextMenuInBody: 32>
    ImGuiTableFlags_Hideable: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_Hideable: 4>
    ImGuiTableFlags_HighlightHoveredColumn: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_HighlightHoveredColumn: 268435456>
    ImGuiTableFlags_NoBordersInBody: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoBordersInBody: 2048>
    ImGuiTableFlags_NoBordersInBodyUntilResize: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoBordersInBodyUntilResize: 4096>
    ImGuiTableFlags_NoClip: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoClip: 1048576>
    ImGuiTableFlags_NoHostExtendX: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoHostExtendX: 65536>
    ImGuiTableFlags_NoHostExtendY: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoHostExtendY: 131072>
    ImGuiTableFlags_NoKeepColumnsVisible: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoKeepColumnsVisible: 262144>
    ImGuiTableFlags_NoPadInnerX: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoPadInnerX: 8388608>
    ImGuiTableFlags_NoPadOuterX: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoPadOuterX: 4194304>
    ImGuiTableFlags_NoSavedSettings: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoSavedSettings: 16>
    ImGuiTableFlags_None: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_None: 0>
    ImGuiTableFlags_PadOuterX: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_PadOuterX: 2097152>
    ImGuiTableFlags_PreciseWidths: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_PreciseWidths: 524288>
    ImGuiTableFlags_Reorderable: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_Reorderable: 2>
    ImGuiTableFlags_Resizable: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_Resizable: 1>
    ImGuiTableFlags_RowBg: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_RowBg: 64>
    ImGuiTableFlags_ScrollX: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_ScrollX: 16777216>
    ImGuiTableFlags_ScrollY: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_ScrollY: 33554432>
    ImGuiTableFlags_SizingFixedFit: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_SizingFixedFit: 8192>
    ImGuiTableFlags_SizingFixedSame: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_SizingFixedSame: 16384>
    ImGuiTableFlags_SizingMask_: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_SizingMask_: 57344>
    ImGuiTableFlags_SizingStretchProp: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_SizingStretchProp: 24576>
    ImGuiTableFlags_SizingStretchSame: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_SizingStretchSame: 32768>
    ImGuiTableFlags_SortMulti: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_SortMulti: 67108864>
    ImGuiTableFlags_SortTristate: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_SortTristate: 134217728>
    ImGuiTableFlags_Sortable: typing.ClassVar[ImGuiTableFlags_]  # value = <ImGuiTableFlags_.ImGuiTableFlags_Sortable: 8>
    __members__: typing.ClassVar[dict[str, ImGuiTableFlags_]]  # value = {'ImGuiTableFlags_None': <ImGuiTableFlags_.ImGuiTableFlags_None: 0>, 'ImGuiTableFlags_Resizable': <ImGuiTableFlags_.ImGuiTableFlags_Resizable: 1>, 'ImGuiTableFlags_Reorderable': <ImGuiTableFlags_.ImGuiTableFlags_Reorderable: 2>, 'ImGuiTableFlags_Hideable': <ImGuiTableFlags_.ImGuiTableFlags_Hideable: 4>, 'ImGuiTableFlags_Sortable': <ImGuiTableFlags_.ImGuiTableFlags_Sortable: 8>, 'ImGuiTableFlags_NoSavedSettings': <ImGuiTableFlags_.ImGuiTableFlags_NoSavedSettings: 16>, 'ImGuiTableFlags_ContextMenuInBody': <ImGuiTableFlags_.ImGuiTableFlags_ContextMenuInBody: 32>, 'ImGuiTableFlags_RowBg': <ImGuiTableFlags_.ImGuiTableFlags_RowBg: 64>, 'ImGuiTableFlags_BordersInnerH': <ImGuiTableFlags_.ImGuiTableFlags_BordersInnerH: 128>, 'ImGuiTableFlags_BordersOuterH': <ImGuiTableFlags_.ImGuiTableFlags_BordersOuterH: 256>, 'ImGuiTableFlags_BordersInnerV': <ImGuiTableFlags_.ImGuiTableFlags_BordersInnerV: 512>, 'ImGuiTableFlags_BordersOuterV': <ImGuiTableFlags_.ImGuiTableFlags_BordersOuterV: 1024>, 'ImGuiTableFlags_BordersH': <ImGuiTableFlags_.ImGuiTableFlags_BordersH: 384>, 'ImGuiTableFlags_BordersV': <ImGuiTableFlags_.ImGuiTableFlags_BordersV: 1536>, 'ImGuiTableFlags_BordersInner': <ImGuiTableFlags_.ImGuiTableFlags_BordersInner: 640>, 'ImGuiTableFlags_BordersOuter': <ImGuiTableFlags_.ImGuiTableFlags_BordersOuter: 1280>, 'ImGuiTableFlags_Borders': <ImGuiTableFlags_.ImGuiTableFlags_Borders: 1920>, 'ImGuiTableFlags_NoBordersInBody': <ImGuiTableFlags_.ImGuiTableFlags_NoBordersInBody: 2048>, 'ImGuiTableFlags_NoBordersInBodyUntilResize': <ImGuiTableFlags_.ImGuiTableFlags_NoBordersInBodyUntilResize: 4096>, 'ImGuiTableFlags_SizingFixedFit': <ImGuiTableFlags_.ImGuiTableFlags_SizingFixedFit: 8192>, 'ImGuiTableFlags_SizingFixedSame': <ImGuiTableFlags_.ImGuiTableFlags_SizingFixedSame: 16384>, 'ImGuiTableFlags_SizingStretchProp': <ImGuiTableFlags_.ImGuiTableFlags_SizingStretchProp: 24576>, 'ImGuiTableFlags_SizingStretchSame': <ImGuiTableFlags_.ImGuiTableFlags_SizingStretchSame: 32768>, 'ImGuiTableFlags_NoHostExtendX': <ImGuiTableFlags_.ImGuiTableFlags_NoHostExtendX: 65536>, 'ImGuiTableFlags_NoHostExtendY': <ImGuiTableFlags_.ImGuiTableFlags_NoHostExtendY: 131072>, 'ImGuiTableFlags_NoKeepColumnsVisible': <ImGuiTableFlags_.ImGuiTableFlags_NoKeepColumnsVisible: 262144>, 'ImGuiTableFlags_PreciseWidths': <ImGuiTableFlags_.ImGuiTableFlags_PreciseWidths: 524288>, 'ImGuiTableFlags_NoClip': <ImGuiTableFlags_.ImGuiTableFlags_NoClip: 1048576>, 'ImGuiTableFlags_PadOuterX': <ImGuiTableFlags_.ImGuiTableFlags_PadOuterX: 2097152>, 'ImGuiTableFlags_NoPadOuterX': <ImGuiTableFlags_.ImGuiTableFlags_NoPadOuterX: 4194304>, 'ImGuiTableFlags_NoPadInnerX': <ImGuiTableFlags_.ImGuiTableFlags_NoPadInnerX: 8388608>, 'ImGuiTableFlags_ScrollX': <ImGuiTableFlags_.ImGuiTableFlags_ScrollX: 16777216>, 'ImGuiTableFlags_ScrollY': <ImGuiTableFlags_.ImGuiTableFlags_ScrollY: 33554432>, 'ImGuiTableFlags_SortMulti': <ImGuiTableFlags_.ImGuiTableFlags_SortMulti: 67108864>, 'ImGuiTableFlags_SortTristate': <ImGuiTableFlags_.ImGuiTableFlags_SortTristate: 134217728>, 'ImGuiTableFlags_HighlightHoveredColumn': <ImGuiTableFlags_.ImGuiTableFlags_HighlightHoveredColumn: 268435456>, 'ImGuiTableFlags_SizingMask_': <ImGuiTableFlags_.ImGuiTableFlags_SizingMask_: 57344>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTableHeaderData:
    BgColor0: int
    BgColor1: int
    Index: int
    TextColor: int
class ImGuiTableInstanceData:
    HoveredRowLast: int
    HoveredRowNext: int
    LastFrozenHeight: float
    LastOuterHeight: float
    LastTopHeadersRowHeight: float
    TableInstanceID: int
    def __init__(self) -> None:
        ...
class ImGuiTableRowFlags_:
    """
    Members:
    
      ImGuiTableRowFlags_None
    
      ImGuiTableRowFlags_Headers
    """
    ImGuiTableRowFlags_Headers: typing.ClassVar[ImGuiTableRowFlags_]  # value = <ImGuiTableRowFlags_.ImGuiTableRowFlags_Headers: 1>
    ImGuiTableRowFlags_None: typing.ClassVar[ImGuiTableRowFlags_]  # value = <ImGuiTableRowFlags_.ImGuiTableRowFlags_None: 0>
    __members__: typing.ClassVar[dict[str, ImGuiTableRowFlags_]]  # value = {'ImGuiTableRowFlags_None': <ImGuiTableRowFlags_.ImGuiTableRowFlags_None: 0>, 'ImGuiTableRowFlags_Headers': <ImGuiTableRowFlags_.ImGuiTableRowFlags_Headers: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTableSettings:
    ColumnsCount: int
    ColumnsCountMax: int
    ID: int
    RefScale: float
    SaveFlags: int
    WantApply: bool
    def GetColumnSettings(self) -> ImGuiTableColumnSettings:
        ...
    def __init__(self) -> None:
        ...
class ImGuiTableSortSpecs:
    Specs: ImGuiTableColumnSortSpecs
    SpecsCount: int
    SpecsDirty: bool
    def __init__(self) -> None:
        ...
class ImGuiTableTempData:
    AngledHeadersExtraWidth: float
    AngledHeadersRequests: ImVector_ImGuiTableHeaderData
    DrawSplitter: ImDrawListSplitter
    HostBackupColumnsOffset: ImVec1
    HostBackupCurrLineSize: ImVec2
    HostBackupCursorMaxPos: ImVec2
    HostBackupItemWidth: float
    HostBackupItemWidthStackSize: int
    HostBackupParentWorkRect: ImRect
    HostBackupPrevLineSize: ImVec2
    HostBackupWorkRect: ImRect
    LastTimeActive: float
    TableIndex: int
    UserOuterSize: ImVec2
    def __init__(self) -> None:
        ...
class ImGuiTextBuffer:
    Buf: ImVector_char
    def __init__(self) -> None:
        ...
    def append(self, str: str, str_end: str = 0) -> None:
        ...
    def begin(self) -> str:
        ...
    def c_str(self) -> str:
        ...
    def clear(self) -> None:
        ...
    def empty(self) -> bool:
        ...
    def end(self) -> str:
        ...
    def reserve(self, capacity: int) -> None:
        ...
    def size(self) -> int:
        ...
class ImGuiTextFilter:
    CountGrep: int
    Filters: ImVector_ImGuiTextRange
    def Build(self) -> None:
        ...
    def Clear(self) -> None:
        ...
    def Draw(self, label: str = 'Filter(inc,-exc)', width: float = 0.0) -> bool:
        ...
    def IsActive(self) -> bool:
        ...
    def PassFilter(self, text: str, text_end: str = 0) -> bool:
        ...
    def __init__(self, default_filter: str = '') -> None:
        ...
    @property
    def InputBuf(self) -> Arr_char:
        ...
class ImGuiTextFlags_:
    """
    Members:
    
      ImGuiTextFlags_None
    
      ImGuiTextFlags_NoWidthForLargeClippedText
    """
    ImGuiTextFlags_NoWidthForLargeClippedText: typing.ClassVar[ImGuiTextFlags_]  # value = <ImGuiTextFlags_.ImGuiTextFlags_NoWidthForLargeClippedText: 1>
    ImGuiTextFlags_None: typing.ClassVar[ImGuiTextFlags_]  # value = <ImGuiTextFlags_.ImGuiTextFlags_None: 0>
    __members__: typing.ClassVar[dict[str, ImGuiTextFlags_]]  # value = {'ImGuiTextFlags_None': <ImGuiTextFlags_.ImGuiTextFlags_None: 0>, 'ImGuiTextFlags_NoWidthForLargeClippedText': <ImGuiTextFlags_.ImGuiTextFlags_NoWidthForLargeClippedText: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTextIndex:
    EndOffset: int
    LineOffsets: ImVector_int
    def append(self, base: str, old_size: int, new_size: int) -> None:
        ...
    def clear(self) -> None:
        ...
    def get_line_begin(self, base: str, n: int) -> str:
        ...
    def get_line_end(self, base: str, n: int) -> str:
        ...
    def size(self) -> int:
        ...
class ImGuiTextRange:
    b: str
    e: str
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, _b: str, _e: str) -> None:
        ...
    def empty(self) -> bool:
        ...
    def split(self, separator: str, out: ImVector_ImGuiTextRange) -> None:
        ...
class ImGuiTooltipFlags_:
    """
    Members:
    
      ImGuiTooltipFlags_None
    
      ImGuiTooltipFlags_OverridePrevious
    """
    ImGuiTooltipFlags_None: typing.ClassVar[ImGuiTooltipFlags_]  # value = <ImGuiTooltipFlags_.ImGuiTooltipFlags_None: 0>
    ImGuiTooltipFlags_OverridePrevious: typing.ClassVar[ImGuiTooltipFlags_]  # value = <ImGuiTooltipFlags_.ImGuiTooltipFlags_OverridePrevious: 2>
    __members__: typing.ClassVar[dict[str, ImGuiTooltipFlags_]]  # value = {'ImGuiTooltipFlags_None': <ImGuiTooltipFlags_.ImGuiTooltipFlags_None: 0>, 'ImGuiTooltipFlags_OverridePrevious': <ImGuiTooltipFlags_.ImGuiTooltipFlags_OverridePrevious: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTreeNodeFlagsPrivate_:
    """
    Members:
    
      ImGuiTreeNodeFlags_ClipLabelForTrailingButton
    
      ImGuiTreeNodeFlags_UpsideDownArrow
    """
    ImGuiTreeNodeFlags_ClipLabelForTrailingButton: typing.ClassVar[ImGuiTreeNodeFlagsPrivate_]  # value = <ImGuiTreeNodeFlagsPrivate_.ImGuiTreeNodeFlags_ClipLabelForTrailingButton: 1048576>
    ImGuiTreeNodeFlags_UpsideDownArrow: typing.ClassVar[ImGuiTreeNodeFlagsPrivate_]  # value = <ImGuiTreeNodeFlagsPrivate_.ImGuiTreeNodeFlags_UpsideDownArrow: 2097152>
    __members__: typing.ClassVar[dict[str, ImGuiTreeNodeFlagsPrivate_]]  # value = {'ImGuiTreeNodeFlags_ClipLabelForTrailingButton': <ImGuiTreeNodeFlagsPrivate_.ImGuiTreeNodeFlags_ClipLabelForTrailingButton: 1048576>, 'ImGuiTreeNodeFlags_UpsideDownArrow': <ImGuiTreeNodeFlagsPrivate_.ImGuiTreeNodeFlags_UpsideDownArrow: 2097152>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTreeNodeFlags_:
    """
    Members:
    
      ImGuiTreeNodeFlags_None
    
      ImGuiTreeNodeFlags_Selected
    
      ImGuiTreeNodeFlags_Framed
    
      ImGuiTreeNodeFlags_AllowOverlap
    
      ImGuiTreeNodeFlags_NoTreePushOnOpen
    
      ImGuiTreeNodeFlags_NoAutoOpenOnLog
    
      ImGuiTreeNodeFlags_DefaultOpen
    
      ImGuiTreeNodeFlags_OpenOnDoubleClick
    
      ImGuiTreeNodeFlags_OpenOnArrow
    
      ImGuiTreeNodeFlags_Leaf
    
      ImGuiTreeNodeFlags_Bullet
    
      ImGuiTreeNodeFlags_FramePadding
    
      ImGuiTreeNodeFlags_SpanAvailWidth
    
      ImGuiTreeNodeFlags_SpanFullWidth
    
      ImGuiTreeNodeFlags_SpanTextWidth
    
      ImGuiTreeNodeFlags_SpanAllColumns
    
      ImGuiTreeNodeFlags_NavLeftJumpsBackHere
    
      ImGuiTreeNodeFlags_CollapsingHeader
    """
    ImGuiTreeNodeFlags_AllowOverlap: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_AllowOverlap: 4>
    ImGuiTreeNodeFlags_Bullet: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Bullet: 512>
    ImGuiTreeNodeFlags_CollapsingHeader: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_CollapsingHeader: 26>
    ImGuiTreeNodeFlags_DefaultOpen: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_DefaultOpen: 32>
    ImGuiTreeNodeFlags_FramePadding: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_FramePadding: 1024>
    ImGuiTreeNodeFlags_Framed: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Framed: 2>
    ImGuiTreeNodeFlags_Leaf: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Leaf: 256>
    ImGuiTreeNodeFlags_NavLeftJumpsBackHere: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_NavLeftJumpsBackHere: 32768>
    ImGuiTreeNodeFlags_NoAutoOpenOnLog: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_NoAutoOpenOnLog: 16>
    ImGuiTreeNodeFlags_NoTreePushOnOpen: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_NoTreePushOnOpen: 8>
    ImGuiTreeNodeFlags_None: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_None: 0>
    ImGuiTreeNodeFlags_OpenOnArrow: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_OpenOnArrow: 128>
    ImGuiTreeNodeFlags_OpenOnDoubleClick: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_OpenOnDoubleClick: 64>
    ImGuiTreeNodeFlags_Selected: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Selected: 1>
    ImGuiTreeNodeFlags_SpanAllColumns: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_SpanAllColumns: 16384>
    ImGuiTreeNodeFlags_SpanAvailWidth: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_SpanAvailWidth: 2048>
    ImGuiTreeNodeFlags_SpanFullWidth: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_SpanFullWidth: 4096>
    ImGuiTreeNodeFlags_SpanTextWidth: typing.ClassVar[ImGuiTreeNodeFlags_]  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_SpanTextWidth: 8192>
    __members__: typing.ClassVar[dict[str, ImGuiTreeNodeFlags_]]  # value = {'ImGuiTreeNodeFlags_None': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_None: 0>, 'ImGuiTreeNodeFlags_Selected': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Selected: 1>, 'ImGuiTreeNodeFlags_Framed': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Framed: 2>, 'ImGuiTreeNodeFlags_AllowOverlap': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_AllowOverlap: 4>, 'ImGuiTreeNodeFlags_NoTreePushOnOpen': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_NoTreePushOnOpen: 8>, 'ImGuiTreeNodeFlags_NoAutoOpenOnLog': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_NoAutoOpenOnLog: 16>, 'ImGuiTreeNodeFlags_DefaultOpen': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_DefaultOpen: 32>, 'ImGuiTreeNodeFlags_OpenOnDoubleClick': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_OpenOnDoubleClick: 64>, 'ImGuiTreeNodeFlags_OpenOnArrow': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_OpenOnArrow: 128>, 'ImGuiTreeNodeFlags_Leaf': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Leaf: 256>, 'ImGuiTreeNodeFlags_Bullet': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Bullet: 512>, 'ImGuiTreeNodeFlags_FramePadding': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_FramePadding: 1024>, 'ImGuiTreeNodeFlags_SpanAvailWidth': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_SpanAvailWidth: 2048>, 'ImGuiTreeNodeFlags_SpanFullWidth': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_SpanFullWidth: 4096>, 'ImGuiTreeNodeFlags_SpanTextWidth': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_SpanTextWidth: 8192>, 'ImGuiTreeNodeFlags_SpanAllColumns': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_SpanAllColumns: 16384>, 'ImGuiTreeNodeFlags_NavLeftJumpsBackHere': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_NavLeftJumpsBackHere: 32768>, 'ImGuiTreeNodeFlags_CollapsingHeader': <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_CollapsingHeader: 26>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTypingSelectFlags_:
    """
    Members:
    
      ImGuiTypingSelectFlags_None
    
      ImGuiTypingSelectFlags_AllowBackspace
    
      ImGuiTypingSelectFlags_AllowSingleCharMode
    """
    ImGuiTypingSelectFlags_AllowBackspace: typing.ClassVar[ImGuiTypingSelectFlags_]  # value = <ImGuiTypingSelectFlags_.ImGuiTypingSelectFlags_AllowBackspace: 1>
    ImGuiTypingSelectFlags_AllowSingleCharMode: typing.ClassVar[ImGuiTypingSelectFlags_]  # value = <ImGuiTypingSelectFlags_.ImGuiTypingSelectFlags_AllowSingleCharMode: 2>
    ImGuiTypingSelectFlags_None: typing.ClassVar[ImGuiTypingSelectFlags_]  # value = <ImGuiTypingSelectFlags_.ImGuiTypingSelectFlags_None: 0>
    __members__: typing.ClassVar[dict[str, ImGuiTypingSelectFlags_]]  # value = {'ImGuiTypingSelectFlags_None': <ImGuiTypingSelectFlags_.ImGuiTypingSelectFlags_None: 0>, 'ImGuiTypingSelectFlags_AllowBackspace': <ImGuiTypingSelectFlags_.ImGuiTypingSelectFlags_AllowBackspace: 1>, 'ImGuiTypingSelectFlags_AllowSingleCharMode': <ImGuiTypingSelectFlags_.ImGuiTypingSelectFlags_AllowSingleCharMode: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiTypingSelectRequest:
    Flags: int
    SearchBuffer: str
    SearchBufferLen: int
    SelectRequest: bool
    SingleCharMode: bool
    SingleCharSize: int
class ImGuiTypingSelectState:
    FocusScope: int
    LastRequestFrame: int
    LastRequestTime: float
    Request: ImGuiTypingSelectRequest
    SingleCharModeLock: bool
    def Clear(self) -> None:
        ...
    def __init__(self) -> None:
        ...
    @property
    def SearchBuffer(self) -> Arr_char:
        ...
class ImGuiViewport:
    DpiScale: float
    DrawData: ImDrawData
    Flags: int
    ID: int
    ParentViewportId: int
    PlatformHandle: capsule
    PlatformHandleRaw: capsule
    PlatformRequestClose: bool
    PlatformRequestMove: bool
    PlatformRequestResize: bool
    PlatformUserData: capsule
    PlatformWindowCreated: bool
    Pos: ImVec2
    RendererUserData: capsule
    Size: ImVec2
    WorkPos: ImVec2
    WorkSize: ImVec2
    def GetCenter(self) -> ImVec2:
        ...
    def GetWorkCenter(self) -> ImVec2:
        ...
    def __init__(self) -> None:
        ...
class ImGuiViewportFlags_:
    """
    Members:
    
      ImGuiViewportFlags_None
    
      ImGuiViewportFlags_IsPlatformWindow
    
      ImGuiViewportFlags_IsPlatformMonitor
    
      ImGuiViewportFlags_OwnedByApp
    
      ImGuiViewportFlags_NoDecoration
    
      ImGuiViewportFlags_NoTaskBarIcon
    
      ImGuiViewportFlags_NoFocusOnAppearing
    
      ImGuiViewportFlags_NoFocusOnClick
    
      ImGuiViewportFlags_NoInputs
    
      ImGuiViewportFlags_NoRendererClear
    
      ImGuiViewportFlags_NoAutoMerge
    
      ImGuiViewportFlags_TopMost
    
      ImGuiViewportFlags_CanHostOtherWindows
    
      ImGuiViewportFlags_IsMinimized
    
      ImGuiViewportFlags_IsFocused
    """
    ImGuiViewportFlags_CanHostOtherWindows: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_CanHostOtherWindows: 2048>
    ImGuiViewportFlags_IsFocused: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_IsFocused: 8192>
    ImGuiViewportFlags_IsMinimized: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_IsMinimized: 4096>
    ImGuiViewportFlags_IsPlatformMonitor: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_IsPlatformMonitor: 2>
    ImGuiViewportFlags_IsPlatformWindow: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_IsPlatformWindow: 1>
    ImGuiViewportFlags_NoAutoMerge: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoAutoMerge: 512>
    ImGuiViewportFlags_NoDecoration: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoDecoration: 8>
    ImGuiViewportFlags_NoFocusOnAppearing: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoFocusOnAppearing: 32>
    ImGuiViewportFlags_NoFocusOnClick: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoFocusOnClick: 64>
    ImGuiViewportFlags_NoInputs: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoInputs: 128>
    ImGuiViewportFlags_NoRendererClear: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoRendererClear: 256>
    ImGuiViewportFlags_NoTaskBarIcon: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoTaskBarIcon: 16>
    ImGuiViewportFlags_None: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_None: 0>
    ImGuiViewportFlags_OwnedByApp: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_OwnedByApp: 4>
    ImGuiViewportFlags_TopMost: typing.ClassVar[ImGuiViewportFlags_]  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_TopMost: 1024>
    __members__: typing.ClassVar[dict[str, ImGuiViewportFlags_]]  # value = {'ImGuiViewportFlags_None': <ImGuiViewportFlags_.ImGuiViewportFlags_None: 0>, 'ImGuiViewportFlags_IsPlatformWindow': <ImGuiViewportFlags_.ImGuiViewportFlags_IsPlatformWindow: 1>, 'ImGuiViewportFlags_IsPlatformMonitor': <ImGuiViewportFlags_.ImGuiViewportFlags_IsPlatformMonitor: 2>, 'ImGuiViewportFlags_OwnedByApp': <ImGuiViewportFlags_.ImGuiViewportFlags_OwnedByApp: 4>, 'ImGuiViewportFlags_NoDecoration': <ImGuiViewportFlags_.ImGuiViewportFlags_NoDecoration: 8>, 'ImGuiViewportFlags_NoTaskBarIcon': <ImGuiViewportFlags_.ImGuiViewportFlags_NoTaskBarIcon: 16>, 'ImGuiViewportFlags_NoFocusOnAppearing': <ImGuiViewportFlags_.ImGuiViewportFlags_NoFocusOnAppearing: 32>, 'ImGuiViewportFlags_NoFocusOnClick': <ImGuiViewportFlags_.ImGuiViewportFlags_NoFocusOnClick: 64>, 'ImGuiViewportFlags_NoInputs': <ImGuiViewportFlags_.ImGuiViewportFlags_NoInputs: 128>, 'ImGuiViewportFlags_NoRendererClear': <ImGuiViewportFlags_.ImGuiViewportFlags_NoRendererClear: 256>, 'ImGuiViewportFlags_NoAutoMerge': <ImGuiViewportFlags_.ImGuiViewportFlags_NoAutoMerge: 512>, 'ImGuiViewportFlags_TopMost': <ImGuiViewportFlags_.ImGuiViewportFlags_TopMost: 1024>, 'ImGuiViewportFlags_CanHostOtherWindows': <ImGuiViewportFlags_.ImGuiViewportFlags_CanHostOtherWindows: 2048>, 'ImGuiViewportFlags_IsMinimized': <ImGuiViewportFlags_.ImGuiViewportFlags_IsMinimized: 4096>, 'ImGuiViewportFlags_IsFocused': <ImGuiViewportFlags_.ImGuiViewportFlags_IsFocused: 8192>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiViewportP:
    Alpha: float
    BuildWorkOffsetMax: ImVec2
    BuildWorkOffsetMin: ImVec2
    DrawDataBuilder: ImDrawDataBuilder
    DrawDataP: ImDrawData
    Idx: int
    LastAlpha: float
    LastFocusedHadNavWindow: bool
    LastFocusedStampCount: int
    LastFrameActive: int
    LastNameHash: int
    LastPlatformPos: ImVec2
    LastPlatformSize: ImVec2
    LastPos: ImVec2
    LastRendererSize: ImVec2
    PlatformMonitor: int
    Window: ImGuiWindow
    WorkOffsetMax: ImVec2
    WorkOffsetMin: ImVec2
    def CalcWorkRectPos(self, off_min: ImVec2) -> ImVec2:
        ...
    def CalcWorkRectSize(self, off_min: ImVec2, off_max: ImVec2) -> ImVec2:
        ...
    def ClearRequestFlags(self) -> None:
        ...
    def GetBuildWorkRect(self) -> ImRect:
        ...
    def GetMainRect(self) -> ImRect:
        ...
    def GetWorkRect(self) -> ImRect:
        ...
    def UpdateWorkRect(self) -> None:
        ...
    def __init__(self) -> None:
        ...
    @property
    def BgFgDrawLists(self) -> Arr_p_ImDrawList:
        ...
    @property
    def BgFgDrawListsLastFrame(self) -> Arr_int:
        ...
    @property
    def _ImGuiViewport(self) -> ImGuiViewport:
        ...
class ImGuiWindow:
    Active: bool
    Appearing: bool
    AutoFitFramesX: int
    AutoFitFramesY: int
    AutoFitOnlyGrows: bool
    AutoPosLastDirection: ImGuiDir
    BeginCount: int
    BeginCountPreviousFrame: int
    BeginOrderWithinContext: int
    BeginOrderWithinParent: int
    ChildFlags: int
    ChildId: int
    ClipRect: ImRect
    Collapsed: bool
    ColumnsStorage: ImVector_ImGuiOldColumns
    ContentRegionRect: ImRect
    ContentSize: ImVec2
    ContentSizeExplicit: ImVec2
    ContentSizeIdeal: ImVec2
    Ctx: ImGuiContext
    DC: ImGuiWindowTempData
    DecoInnerSizeX1: float
    DecoInnerSizeY1: float
    DecoOuterSizeX1: float
    DecoOuterSizeX2: float
    DecoOuterSizeY1: float
    DecoOuterSizeY2: float
    DisableInputsFrames: int
    DockId: int
    DockIsActive: bool
    DockNode: ImGuiDockNode
    DockNodeAsHost: ImGuiDockNode
    DockNodeIsVisible: bool
    DockOrder: int
    DockStyle: ImGuiWindowDockStyle
    DockTabIsVisible: bool
    DockTabItemRect: ImRect
    DockTabItemStatusFlags: int
    DockTabWantClose: bool
    DrawList: ImDrawList
    DrawListInst: ImDrawList
    Flags: int
    FlagsPreviousFrame: int
    FocusOrder: int
    FontDpiScale: float
    FontWindowScale: float
    HasCloseButton: bool
    Hidden: bool
    HiddenFramesCanSkipItems: int
    HiddenFramesCannotSkipItems: int
    HiddenFramesForRenderOnly: int
    HitTestHoleOffset: ImVec2ih
    HitTestHoleSize: ImVec2ih
    ID: int
    IDStack: ImVector_ImGuiID
    InnerClipRect: ImRect
    InnerRect: ImRect
    IsExplicitChild: bool
    IsFallbackWindow: bool
    ItemWidthDefault: float
    LastFrameActive: int
    LastFrameJustFocused: int
    LastTimeActive: float
    MemoryCompacted: bool
    MemoryDrawListIdxCapacity: int
    MemoryDrawListVtxCapacity: int
    MenuBarHeight: float
    MoveId: int
    Name: str
    NameBufLen: int
    NavLastChildNavWindow: ImGuiWindow
    NavRootFocusScopeId: int
    OuterRectClipped: ImRect
    ParentWindow: ImGuiWindow
    ParentWindowForFocusRoute: ImGuiWindow
    ParentWindowInBeginStack: ImGuiWindow
    ParentWorkRect: ImRect
    PopupId: int
    Pos: ImVec2
    ResizeBorderHeld: int
    ResizeBorderHovered: int
    RootWindow: ImGuiWindow
    RootWindowDockTree: ImGuiWindow
    RootWindowForNav: ImGuiWindow
    RootWindowForTitleBarHighlight: ImGuiWindow
    RootWindowPopupTree: ImGuiWindow
    Scroll: ImVec2
    ScrollMax: ImVec2
    ScrollTarget: ImVec2
    ScrollTargetCenterRatio: ImVec2
    ScrollTargetEdgeSnapDist: ImVec2
    ScrollbarSizes: ImVec2
    ScrollbarX: bool
    ScrollbarY: bool
    SetWindowCollapsedAllowFlags: int
    SetWindowDockAllowFlags: int
    SetWindowPosAllowFlags: int
    SetWindowPosPivot: ImVec2
    SetWindowPosVal: ImVec2
    SetWindowSizeAllowFlags: int
    SettingsOffset: int
    Size: ImVec2
    SizeFull: ImVec2
    SkipItems: bool
    SkipRefresh: bool
    StateStorage: ImGuiStorage
    TabId: int
    TitleBarHeight: float
    Viewport: ImGuiViewportP
    ViewportAllowPlatformMonitorExtend: int
    ViewportId: int
    ViewportOwned: bool
    ViewportPos: ImVec2
    WantCollapseToggle: bool
    WasActive: bool
    WindowBorderSize: float
    WindowClass: ImGuiWindowClass
    WindowPadding: ImVec2
    WindowRounding: float
    WorkRect: ImRect
    WriteAccessed: bool
    def CalcFontSize(self) -> float:
        ...
    @typing.overload
    def GetID(self, str: str, str_end: str = 0) -> int:
        ...
    @typing.overload
    def GetID(self, ptr: capsule) -> int:
        ...
    @typing.overload
    def GetID(self, n: int) -> int:
        ...
    def GetIDFromRectangle(self, r_abs: ImRect) -> int:
        ...
    def MenuBarRect(self) -> ImRect:
        ...
    def Rect(self) -> ImRect:
        ...
    def TitleBarRect(self) -> ImRect:
        ...
    def __init__(self, context: ImGuiContext, name: str) -> None:
        ...
    @property
    def NavLastIds(self) -> Arr_unsigned_int:
        ...
    @property
    def NavPreferredScoringPosRel(self) -> Arr_ImVec2:
        ...
    @property
    def NavRectRel(self) -> Arr_ImRect:
        ...
class ImGuiWindowClass:
    ClassId: int
    DockNodeFlagsOverrideSet: int
    DockingAllowUnclassed: bool
    DockingAlwaysTabBar: bool
    FocusRouteParentWindowId: int
    ParentViewportId: int
    TabItemFlagsOverrideSet: int
    ViewportFlagsOverrideClear: int
    ViewportFlagsOverrideSet: int
    def __init__(self) -> None:
        ...
class ImGuiWindowDockStyle:
    @property
    def Colors(self) -> Arr_unsigned_int:
        ...
class ImGuiWindowDockStyleCol:
    """
    Members:
    
      ImGuiWindowDockStyleCol_Text
    
      ImGuiWindowDockStyleCol_TabHovered
    
      ImGuiWindowDockStyleCol_TabFocused
    
      ImGuiWindowDockStyleCol_TabSelected
    
      ImGuiWindowDockStyleCol_TabSelectedOverline
    
      ImGuiWindowDockStyleCol_TabDimmed
    
      ImGuiWindowDockStyleCol_TabDimmedSelected
    
      ImGuiWindowDockStyleCol_TabDimmedSelectedOverline
    
      ImGuiWindowDockStyleCol_COUNT
    """
    ImGuiWindowDockStyleCol_COUNT: typing.ClassVar[ImGuiWindowDockStyleCol]  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_COUNT: 8>
    ImGuiWindowDockStyleCol_TabDimmed: typing.ClassVar[ImGuiWindowDockStyleCol]  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabDimmed: 5>
    ImGuiWindowDockStyleCol_TabDimmedSelected: typing.ClassVar[ImGuiWindowDockStyleCol]  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabDimmedSelected: 6>
    ImGuiWindowDockStyleCol_TabDimmedSelectedOverline: typing.ClassVar[ImGuiWindowDockStyleCol]  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabDimmedSelectedOverline: 7>
    ImGuiWindowDockStyleCol_TabFocused: typing.ClassVar[ImGuiWindowDockStyleCol]  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabFocused: 2>
    ImGuiWindowDockStyleCol_TabHovered: typing.ClassVar[ImGuiWindowDockStyleCol]  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabHovered: 1>
    ImGuiWindowDockStyleCol_TabSelected: typing.ClassVar[ImGuiWindowDockStyleCol]  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabSelected: 3>
    ImGuiWindowDockStyleCol_TabSelectedOverline: typing.ClassVar[ImGuiWindowDockStyleCol]  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabSelectedOverline: 4>
    ImGuiWindowDockStyleCol_Text: typing.ClassVar[ImGuiWindowDockStyleCol]  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_Text: 0>
    __members__: typing.ClassVar[dict[str, ImGuiWindowDockStyleCol]]  # value = {'ImGuiWindowDockStyleCol_Text': <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_Text: 0>, 'ImGuiWindowDockStyleCol_TabHovered': <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabHovered: 1>, 'ImGuiWindowDockStyleCol_TabFocused': <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabFocused: 2>, 'ImGuiWindowDockStyleCol_TabSelected': <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabSelected: 3>, 'ImGuiWindowDockStyleCol_TabSelectedOverline': <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabSelectedOverline: 4>, 'ImGuiWindowDockStyleCol_TabDimmed': <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabDimmed: 5>, 'ImGuiWindowDockStyleCol_TabDimmedSelected': <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabDimmedSelected: 6>, 'ImGuiWindowDockStyleCol_TabDimmedSelectedOverline': <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabDimmedSelectedOverline: 7>, 'ImGuiWindowDockStyleCol_COUNT': <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_COUNT: 8>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiWindowFlags_:
    """
    Members:
    
      ImGuiWindowFlags_None
    
      ImGuiWindowFlags_NoTitleBar
    
      ImGuiWindowFlags_NoResize
    
      ImGuiWindowFlags_NoMove
    
      ImGuiWindowFlags_NoScrollbar
    
      ImGuiWindowFlags_NoScrollWithMouse
    
      ImGuiWindowFlags_NoCollapse
    
      ImGuiWindowFlags_AlwaysAutoResize
    
      ImGuiWindowFlags_NoBackground
    
      ImGuiWindowFlags_NoSavedSettings
    
      ImGuiWindowFlags_NoMouseInputs
    
      ImGuiWindowFlags_MenuBar
    
      ImGuiWindowFlags_HorizontalScrollbar
    
      ImGuiWindowFlags_NoFocusOnAppearing
    
      ImGuiWindowFlags_NoBringToFrontOnFocus
    
      ImGuiWindowFlags_AlwaysVerticalScrollbar
    
      ImGuiWindowFlags_AlwaysHorizontalScrollbar
    
      ImGuiWindowFlags_NoNavInputs
    
      ImGuiWindowFlags_NoNavFocus
    
      ImGuiWindowFlags_UnsavedDocument
    
      ImGuiWindowFlags_NoDocking
    
      ImGuiWindowFlags_NoNav
    
      ImGuiWindowFlags_NoDecoration
    
      ImGuiWindowFlags_NoInputs
    
      ImGuiWindowFlags_ChildWindow
    
      ImGuiWindowFlags_Tooltip
    
      ImGuiWindowFlags_Popup
    
      ImGuiWindowFlags_Modal
    
      ImGuiWindowFlags_ChildMenu
    
      ImGuiWindowFlags_DockNodeHost
    """
    ImGuiWindowFlags_AlwaysAutoResize: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_AlwaysAutoResize: 64>
    ImGuiWindowFlags_AlwaysHorizontalScrollbar: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_AlwaysHorizontalScrollbar: 32768>
    ImGuiWindowFlags_AlwaysVerticalScrollbar: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_AlwaysVerticalScrollbar: 16384>
    ImGuiWindowFlags_ChildMenu: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_ChildMenu: 268435456>
    ImGuiWindowFlags_ChildWindow: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_ChildWindow: 16777216>
    ImGuiWindowFlags_DockNodeHost: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_DockNodeHost: 536870912>
    ImGuiWindowFlags_HorizontalScrollbar: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_HorizontalScrollbar: 2048>
    ImGuiWindowFlags_MenuBar: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_MenuBar: 1024>
    ImGuiWindowFlags_Modal: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_Modal: 134217728>
    ImGuiWindowFlags_NoBackground: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoBackground: 128>
    ImGuiWindowFlags_NoBringToFrontOnFocus: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoBringToFrontOnFocus: 8192>
    ImGuiWindowFlags_NoCollapse: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoCollapse: 32>
    ImGuiWindowFlags_NoDecoration: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoDecoration: 43>
    ImGuiWindowFlags_NoDocking: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoDocking: 524288>
    ImGuiWindowFlags_NoFocusOnAppearing: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoFocusOnAppearing: 4096>
    ImGuiWindowFlags_NoInputs: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoInputs: 197120>
    ImGuiWindowFlags_NoMouseInputs: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoMouseInputs: 512>
    ImGuiWindowFlags_NoMove: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoMove: 4>
    ImGuiWindowFlags_NoNav: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoNav: 196608>
    ImGuiWindowFlags_NoNavFocus: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoNavFocus: 131072>
    ImGuiWindowFlags_NoNavInputs: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoNavInputs: 65536>
    ImGuiWindowFlags_NoResize: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoResize: 2>
    ImGuiWindowFlags_NoSavedSettings: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoSavedSettings: 256>
    ImGuiWindowFlags_NoScrollWithMouse: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoScrollWithMouse: 16>
    ImGuiWindowFlags_NoScrollbar: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoScrollbar: 8>
    ImGuiWindowFlags_NoTitleBar: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoTitleBar: 1>
    ImGuiWindowFlags_None: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_None: 0>
    ImGuiWindowFlags_Popup: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_Popup: 67108864>
    ImGuiWindowFlags_Tooltip: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_Tooltip: 33554432>
    ImGuiWindowFlags_UnsavedDocument: typing.ClassVar[ImGuiWindowFlags_]  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_UnsavedDocument: 262144>
    __members__: typing.ClassVar[dict[str, ImGuiWindowFlags_]]  # value = {'ImGuiWindowFlags_None': <ImGuiWindowFlags_.ImGuiWindowFlags_None: 0>, 'ImGuiWindowFlags_NoTitleBar': <ImGuiWindowFlags_.ImGuiWindowFlags_NoTitleBar: 1>, 'ImGuiWindowFlags_NoResize': <ImGuiWindowFlags_.ImGuiWindowFlags_NoResize: 2>, 'ImGuiWindowFlags_NoMove': <ImGuiWindowFlags_.ImGuiWindowFlags_NoMove: 4>, 'ImGuiWindowFlags_NoScrollbar': <ImGuiWindowFlags_.ImGuiWindowFlags_NoScrollbar: 8>, 'ImGuiWindowFlags_NoScrollWithMouse': <ImGuiWindowFlags_.ImGuiWindowFlags_NoScrollWithMouse: 16>, 'ImGuiWindowFlags_NoCollapse': <ImGuiWindowFlags_.ImGuiWindowFlags_NoCollapse: 32>, 'ImGuiWindowFlags_AlwaysAutoResize': <ImGuiWindowFlags_.ImGuiWindowFlags_AlwaysAutoResize: 64>, 'ImGuiWindowFlags_NoBackground': <ImGuiWindowFlags_.ImGuiWindowFlags_NoBackground: 128>, 'ImGuiWindowFlags_NoSavedSettings': <ImGuiWindowFlags_.ImGuiWindowFlags_NoSavedSettings: 256>, 'ImGuiWindowFlags_NoMouseInputs': <ImGuiWindowFlags_.ImGuiWindowFlags_NoMouseInputs: 512>, 'ImGuiWindowFlags_MenuBar': <ImGuiWindowFlags_.ImGuiWindowFlags_MenuBar: 1024>, 'ImGuiWindowFlags_HorizontalScrollbar': <ImGuiWindowFlags_.ImGuiWindowFlags_HorizontalScrollbar: 2048>, 'ImGuiWindowFlags_NoFocusOnAppearing': <ImGuiWindowFlags_.ImGuiWindowFlags_NoFocusOnAppearing: 4096>, 'ImGuiWindowFlags_NoBringToFrontOnFocus': <ImGuiWindowFlags_.ImGuiWindowFlags_NoBringToFrontOnFocus: 8192>, 'ImGuiWindowFlags_AlwaysVerticalScrollbar': <ImGuiWindowFlags_.ImGuiWindowFlags_AlwaysVerticalScrollbar: 16384>, 'ImGuiWindowFlags_AlwaysHorizontalScrollbar': <ImGuiWindowFlags_.ImGuiWindowFlags_AlwaysHorizontalScrollbar: 32768>, 'ImGuiWindowFlags_NoNavInputs': <ImGuiWindowFlags_.ImGuiWindowFlags_NoNavInputs: 65536>, 'ImGuiWindowFlags_NoNavFocus': <ImGuiWindowFlags_.ImGuiWindowFlags_NoNavFocus: 131072>, 'ImGuiWindowFlags_UnsavedDocument': <ImGuiWindowFlags_.ImGuiWindowFlags_UnsavedDocument: 262144>, 'ImGuiWindowFlags_NoDocking': <ImGuiWindowFlags_.ImGuiWindowFlags_NoDocking: 524288>, 'ImGuiWindowFlags_NoNav': <ImGuiWindowFlags_.ImGuiWindowFlags_NoNav: 196608>, 'ImGuiWindowFlags_NoDecoration': <ImGuiWindowFlags_.ImGuiWindowFlags_NoDecoration: 43>, 'ImGuiWindowFlags_NoInputs': <ImGuiWindowFlags_.ImGuiWindowFlags_NoInputs: 197120>, 'ImGuiWindowFlags_ChildWindow': <ImGuiWindowFlags_.ImGuiWindowFlags_ChildWindow: 16777216>, 'ImGuiWindowFlags_Tooltip': <ImGuiWindowFlags_.ImGuiWindowFlags_Tooltip: 33554432>, 'ImGuiWindowFlags_Popup': <ImGuiWindowFlags_.ImGuiWindowFlags_Popup: 67108864>, 'ImGuiWindowFlags_Modal': <ImGuiWindowFlags_.ImGuiWindowFlags_Modal: 134217728>, 'ImGuiWindowFlags_ChildMenu': <ImGuiWindowFlags_.ImGuiWindowFlags_ChildMenu: 268435456>, 'ImGuiWindowFlags_DockNodeHost': <ImGuiWindowFlags_.ImGuiWindowFlags_DockNodeHost: 536870912>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiWindowRefreshFlags_:
    """
    Members:
    
      ImGuiWindowRefreshFlags_None
    
      ImGuiWindowRefreshFlags_TryToAvoidRefresh
    
      ImGuiWindowRefreshFlags_RefreshOnHover
    
      ImGuiWindowRefreshFlags_RefreshOnFocus
    """
    ImGuiWindowRefreshFlags_None: typing.ClassVar[ImGuiWindowRefreshFlags_]  # value = <ImGuiWindowRefreshFlags_.ImGuiWindowRefreshFlags_None: 0>
    ImGuiWindowRefreshFlags_RefreshOnFocus: typing.ClassVar[ImGuiWindowRefreshFlags_]  # value = <ImGuiWindowRefreshFlags_.ImGuiWindowRefreshFlags_RefreshOnFocus: 4>
    ImGuiWindowRefreshFlags_RefreshOnHover: typing.ClassVar[ImGuiWindowRefreshFlags_]  # value = <ImGuiWindowRefreshFlags_.ImGuiWindowRefreshFlags_RefreshOnHover: 2>
    ImGuiWindowRefreshFlags_TryToAvoidRefresh: typing.ClassVar[ImGuiWindowRefreshFlags_]  # value = <ImGuiWindowRefreshFlags_.ImGuiWindowRefreshFlags_TryToAvoidRefresh: 1>
    __members__: typing.ClassVar[dict[str, ImGuiWindowRefreshFlags_]]  # value = {'ImGuiWindowRefreshFlags_None': <ImGuiWindowRefreshFlags_.ImGuiWindowRefreshFlags_None: 0>, 'ImGuiWindowRefreshFlags_TryToAvoidRefresh': <ImGuiWindowRefreshFlags_.ImGuiWindowRefreshFlags_TryToAvoidRefresh: 1>, 'ImGuiWindowRefreshFlags_RefreshOnHover': <ImGuiWindowRefreshFlags_.ImGuiWindowRefreshFlags_RefreshOnHover: 2>, 'ImGuiWindowRefreshFlags_RefreshOnFocus': <ImGuiWindowRefreshFlags_.ImGuiWindowRefreshFlags_RefreshOnFocus: 4>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImGuiWindowSettings:
    ClassId: int
    Collapsed: bool
    DockId: int
    DockOrder: int
    ID: int
    IsChild: bool
    Pos: ImVec2ih
    Size: ImVec2ih
    ViewportId: int
    ViewportPos: ImVec2ih
    WantApply: bool
    WantDelete: bool
    def GetName(self) -> str:
        ...
    def __init__(self) -> None:
        ...
class ImGuiWindowStackData:
    DisabledOverrideReenable: bool
    ParentLastItemDataBackup: ImGuiLastItemData
    StackSizesOnBegin: ImGuiStackSizes
    Window: ImGuiWindow
class ImGuiWindowTempData:
    ChildWindows: ImVector_ImGuiWindowPtr
    ColumnsOffset: ImVec1
    CurrLineSize: ImVec2
    CurrLineTextBaseOffset: float
    CurrentColumns: ImGuiOldColumns
    CurrentTableIdx: int
    CursorMaxPos: ImVec2
    CursorPos: ImVec2
    CursorPosPrevLine: ImVec2
    CursorStartPos: ImVec2
    CursorStartPosLossyness: ImVec2
    GroupOffset: ImVec1
    IdealMaxPos: ImVec2
    Indent: ImVec1
    IsSameLine: bool
    IsSetPos: bool
    ItemWidth: float
    ItemWidthStack: ImVector_float
    LayoutType: int
    MenuBarAppending: bool
    MenuBarOffset: ImVec2
    MenuColumns: ImGuiMenuColumns
    ModalDimBgColor: int
    NavHideHighlightOneFrame: bool
    NavIsScrollPushableX: bool
    NavLayerCurrent: ImGuiNavLayer
    NavLayersActiveMask: int
    NavLayersActiveMaskNext: int
    NavWindowHasScrollY: bool
    ParentLayoutType: int
    PrevLineSize: ImVec2
    PrevLineTextBaseOffset: float
    StateStorage: ImGuiStorage
    TextWrapPos: float
    TextWrapPosStack: ImVector_float
    TreeDepth: int
    TreeJumpToParentOnPopMask: int
class ImPool_ImGuiTabBar:
    pass
class ImPool_ImGuiTable:
    pass
class ImRect:
    Max: ImVec2
    Min: ImVec2
    @typing.overload
    def Add(self, p: ImVec2) -> None:
        ...
    @typing.overload
    def Add(self, r: ImRect) -> None:
        ...
    def ClipWith(self, r: ImRect) -> None:
        ...
    def ClipWithFull(self, r: ImRect) -> None:
        ...
    @typing.overload
    def Contains(self, p: ImVec2) -> bool:
        ...
    @typing.overload
    def Contains(self, r: ImRect) -> bool:
        ...
    def ContainsWithPad(self, p: ImVec2, pad: ImVec2) -> bool:
        ...
    @typing.overload
    def Expand(self, amount: float) -> None:
        ...
    @typing.overload
    def Expand(self, amount: ImVec2) -> None:
        ...
    def Floor(self) -> None:
        ...
    def GetArea(self) -> float:
        ...
    def GetBL(self) -> ImVec2:
        ...
    def GetBR(self) -> ImVec2:
        ...
    def GetCenter(self) -> ImVec2:
        ...
    def GetHeight(self) -> float:
        ...
    def GetSize(self) -> ImVec2:
        ...
    def GetTL(self) -> ImVec2:
        ...
    def GetTR(self) -> ImVec2:
        ...
    def GetWidth(self) -> float:
        ...
    def IsInverted(self) -> bool:
        ...
    def Overlaps(self, r: ImRect) -> bool:
        ...
    def ToVec4(self) -> ImVec4:
        ...
    def Translate(self, d: ImVec2) -> None:
        ...
    def TranslateX(self, dx: float) -> None:
        ...
    def TranslateY(self, dy: float) -> None:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, min: ImVec2, max: ImVec2) -> None:
        ...
    @typing.overload
    def __init__(self, v: ImVec4) -> None:
        ...
    @typing.overload
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        ...
class ImSpan_ImGuiTableCellData:
    pass
class ImSpan_ImGuiTableColumn:
    pass
class ImSpan_ImGuiTableColumnIdx:
    pass
class ImVec1:
    x: float
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, _x: float) -> None:
        ...
class ImVec2:
    x: float
    y: float
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, _x: float, _y: float) -> None:
        ...
class ImVec2ih:
    x: int
    y: int
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, _x: int, _y: int) -> None:
        ...
    @typing.overload
    def __init__(self, rhs: ImVec2) -> None:
        ...
class ImVec4:
    w: float
    x: float
    y: float
    z: float
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, _x: float, _y: float, _z: float, _w: float) -> None:
        ...
class ImVector_ImDrawChannel:
    pass
class ImVector_ImDrawCmd:
    pass
class ImVector_ImDrawIdx:
    pass
class ImVector_ImDrawListPtr:
    pass
class ImVector_ImDrawVert:
    pass
class ImVector_ImFontAtlasCustomRect:
    pass
class ImVector_ImFontConfig:
    pass
class ImVector_ImFontGlyph:
    pass
class ImVector_ImFontPtr:
    pass
class ImVector_ImGuiColorMod:
    pass
class ImVector_ImGuiContextHook:
    pass
class ImVector_ImGuiDockNodeSettings:
    pass
class ImVector_ImGuiDockRequest:
    pass
class ImVector_ImGuiFocusScopeData:
    pass
class ImVector_ImGuiGroupData:
    pass
class ImVector_ImGuiID:
    pass
class ImVector_ImGuiInputEvent:
    pass
class ImVector_ImGuiItemFlags:
    pass
class ImVector_ImGuiKeyRoutingData:
    pass
class ImVector_ImGuiListClipperData:
    pass
class ImVector_ImGuiListClipperRange:
    pass
class ImVector_ImGuiNavTreeNodeData:
    pass
class ImVector_ImGuiOldColumnData:
    pass
class ImVector_ImGuiOldColumns:
    pass
class ImVector_ImGuiPlatformMonitor:
    pass
class ImVector_ImGuiPopupData:
    pass
class ImVector_ImGuiPtrOrIndex:
    pass
class ImVector_ImGuiSettingsHandler:
    pass
class ImVector_ImGuiShrinkWidthItem:
    pass
class ImVector_ImGuiStackLevelInfo:
    pass
class ImVector_ImGuiStoragePair:
    pass
class ImVector_ImGuiStyleMod:
    pass
class ImVector_ImGuiTabItem:
    pass
class ImVector_ImGuiTableColumnSortSpecs:
    pass
class ImVector_ImGuiTableHeaderData:
    pass
class ImVector_ImGuiTableInstanceData:
    pass
class ImVector_ImGuiTableTempData:
    pass
class ImVector_ImGuiTextRange:
    pass
class ImVector_ImGuiViewportPPtr:
    pass
class ImVector_ImGuiViewportPtr:
    pass
class ImVector_ImGuiWindowPtr:
    pass
class ImVector_ImGuiWindowStackData:
    pass
class ImVector_ImTextureID:
    pass
class ImVector_ImU32:
    pass
class ImVector_ImVec2:
    pass
class ImVector_ImVec4:
    pass
class ImVector_ImWchar:
    pass
class ImVector_char:
    pass
class ImVector_float:
    pass
class ImVector_int:
    pass
class ImVector_unsigned_char:
    pass
class STB_TexteditState:
    cursor: int
    cursor_at_end_of_line: int
    has_preferred_x: int
    initialized: int
    insert_mode: int
    padding1: int
    padding2: int
    padding3: int
    preferred_x: float
    row_count_per_page: int
    select_end: int
    select_start: int
    single_line: int
    undostate: StbUndoState
class StbTexteditRow:
    baseline_y_delta: float
    num_chars: int
    x0: float
    x1: float
    ymax: float
    ymin: float
class StbUndoRecord:
    char_storage: int
    delete_length: int
    insert_length: int
    where: int
class StbUndoState:
    redo_char_point: int
    redo_point: int
    undo_char_point: int
    undo_point: int
    @property
    def undo_char(self) -> Arr_unsigned_short:
        ...
    @property
    def undo_rec(self) -> Arr_StbUndoRecord:
        ...
def AcceptDragDropPayload(type: str, flags: int = 0) -> ImGuiPayload:
    ...
def ActivateItemByID(id: int) -> None:
    ...
def AddContextHook(context: ImGuiContext, hook: ImGuiContextHook) -> int:
    ...
def AddDrawListToDrawDataEx(draw_data: ImDrawData, out_list: ImVector_ImDrawListPtr, draw_list: ImDrawList) -> None:
    ...
def AddSettingsHandler(handler: ImGuiSettingsHandler) -> None:
    ...
def AlignTextToFramePadding() -> None:
    ...
def ArrowButton(str_id: str, dir: ImGuiDir) -> bool:
    ...
def ArrowButtonEx(str_id: str, dir: ImGuiDir, size_arg: ImVec2, flags: int = 0) -> bool:
    ...
def Begin(name: str = '', open: bool = True, flags: int = 0) -> tuple:
    ...
@typing.overload
def BeginChild(str_id: str, size: ImVec2 = ..., child_flags: int = 0, window_flags: int = 0) -> bool:
    ...
@typing.overload
def BeginChild(id: int, size: ImVec2 = ..., child_flags: int = 0, window_flags: int = 0) -> bool:
    ...
def BeginChildEx(name: str, id: int, size_arg: ImVec2, child_flags: int, window_flags: int) -> bool:
    ...
def BeginColumns(str_id: str, count: int, flags: int = 0) -> None:
    ...
def BeginCombo(label: str, preview_value: str, flags: int = 0) -> bool:
    ...
def BeginComboPopup(popup_id: int, bb: ImRect, flags: int) -> bool:
    ...
def BeginComboPreview() -> bool:
    ...
def BeginDisabled(disabled: bool = True) -> None:
    ...
def BeginDisabledOverrideReenable() -> None:
    ...
def BeginDockableDragDropSource(window: ImGuiWindow) -> None:
    ...
def BeginDockableDragDropTarget(window: ImGuiWindow) -> None:
    ...
def BeginDocked(window: ImGuiWindow, p_open: bool) -> None:
    ...
def BeginDragDropSource(flags: int = 0) -> bool:
    ...
def BeginDragDropTarget() -> bool:
    ...
def BeginDragDropTargetCustom(bb: ImRect, id: int) -> bool:
    ...
def BeginGroup() -> None:
    ...
def BeginItemTooltip() -> bool:
    ...
def BeginListBox(label: str, size: ImVec2 = ...) -> bool:
    ...
def BeginMainMenuBar() -> bool:
    ...
def BeginMenu(label: str, enabled: bool = True) -> bool:
    ...
def BeginMenuBar() -> bool:
    ...
def BeginMenuEx(label: str, icon: str, enabled: bool = True) -> bool:
    ...
def BeginPopup(str_id: str, flags: int = 0) -> bool:
    ...
def BeginPopupContextItem(str_id: str = 0, popup_flags: int = 1) -> bool:
    ...
def BeginPopupContextVoid(str_id: str = 0, popup_flags: int = 1) -> bool:
    ...
def BeginPopupContextWindow(str_id: str = 0, popup_flags: int = 1) -> bool:
    ...
def BeginPopupEx(id: int, extra_window_flags: int) -> bool:
    ...
def BeginPopupModal(name: str, p_open: bool = 0, flags: int = 0) -> bool:
    ...
def BeginTabBar(str_id: str, flags: int = 0) -> bool:
    ...
def BeginTabBarEx(tab_bar: ImGuiTabBar, bb: ImRect, flags: int) -> bool:
    ...
def BeginTabItem(label: str, p_open: bool = 0, flags: int = 0) -> bool:
    ...
def BeginTable(str_id: str, columns: int, flags: int = 0, outer_size: ImVec2 = ..., inner_width: float = 0.0) -> bool:
    ...
def BeginTableEx(name: str, id: int, columns_count: int, flags: int = 0, outer_size: ImVec2 = ..., inner_width: float = 0.0) -> bool:
    ...
def BeginTooltip() -> bool:
    ...
def BeginTooltipEx(tooltip_flags: int, extra_window_flags: int) -> bool:
    ...
def BeginTooltipHidden() -> bool:
    ...
def BeginViewportSideBar(name: str, viewport: ImGuiViewport, dir: ImGuiDir, size: float, window_flags: int) -> bool:
    ...
def BringWindowToDisplayBack(window: ImGuiWindow) -> None:
    ...
def BringWindowToDisplayBehind(window: ImGuiWindow, above_window: ImGuiWindow) -> None:
    ...
def BringWindowToDisplayFront(window: ImGuiWindow) -> None:
    ...
def BringWindowToFocusFront(window: ImGuiWindow) -> None:
    ...
def Bullet() -> None:
    ...
def Button(label: str, size: ImVec2 = ...) -> bool:
    ...
def ButtonBehavior(bb: ImRect, id: int, out_hovered: bool, out_held: bool, flags: int = 0) -> bool:
    ...
def ButtonEx(label: str, size_arg: ImVec2 = ..., flags: int = 0) -> bool:
    ...
def CalcItemSize(size: ImVec2, default_w: float, default_h: float) -> ImVec2:
    ...
def CalcItemWidth() -> float:
    ...
def CalcRoundingFlagsForRectInRect(r_in: ImRect, r_outer: ImRect, threshold: float) -> int:
    ...
def CalcTextSize(text: str, text_end: str = 0, hide_text_after_double_hash: bool = False, wrap_width: float = -1.0) -> ImVec2:
    ...
def CalcTypematicRepeatAmount(t0: float, t1: float, repeat_delay: float, repeat_rate: float) -> int:
    ...
def CalcWindowNextAutoFitSize(window: ImGuiWindow) -> ImVec2:
    ...
def CalcWrapWidthForPos(pos: ImVec2, wrap_pos_x: float) -> float:
    ...
def CallContextHooks(context: ImGuiContext, type: ImGuiContextHookType) -> None:
    ...
def Checkbox(label: str = '', v: bool = False) -> tuple:
    ...
@typing.overload
def CheckboxFlags(label: str, flags: int, flags_value: int) -> bool:
    ...
@typing.overload
def CheckboxFlags(label: str, flags: int, flags_value: int) -> bool:
    ...
@typing.overload
def CheckboxFlags(label: str, flags: int, flags_value: int) -> bool:
    ...
@typing.overload
def CheckboxFlags(label: str, flags: int, flags_value: int) -> bool:
    ...
def ClearActiveID() -> None:
    ...
def ClearDragDrop() -> None:
    ...
def ClearIniSettings() -> None:
    ...
def ClearWindowSettings(name: str) -> None:
    ...
def CloseButton(id: int, pos: ImVec2) -> bool:
    ...
def CloseCurrentPopup() -> None:
    ...
def ClosePopupToLevel(remaining: int, restore_focus_to_window_under_popup: bool) -> None:
    ...
def ClosePopupsExceptModals() -> None:
    ...
def ClosePopupsOverWindow(ref_window: ImGuiWindow, restore_focus_to_window_under_popup: bool) -> None:
    ...
def CollapseButton(id: int, pos: ImVec2, dock_node: ImGuiDockNode) -> bool:
    ...
@typing.overload
def CollapsingHeader(label: str, flags: int = 0) -> bool:
    ...
@typing.overload
def CollapsingHeader(label: str, p_visible: bool, flags: int = 0) -> bool:
    ...
@typing.overload
def ColorButton(desc_id: str, col: ImVec4, flags: int = 0, size: ImVec2 = ...) -> bool:
    ...
@typing.overload
def ColorButton(desc_id: str, col: ImColor, flags: int = 0, size: ImVec2 = ...) -> bool:
    ...
def ColorConvertFloat4ToU32(in: ImVec4) -> int:
    ...
def ColorConvertHSVtoRGB(h: float, s: float, v: float, out_r: float, out_g: float, out_b: float) -> None:
    ...
def ColorConvertRGBtoHSV(r: float, g: float, b: float, out_h: float, out_s: float, out_v: float) -> None:
    ...
def ColorConvertU32ToFloat4(in: int) -> ImVec4:
    ...
@typing.overload
def ColorEdit3(label: str, color: ImVec4, flags: int = 0) -> tuple:
    ...
@typing.overload
def ColorEdit3(label: str, color: ImColor, flags: int = 0) -> tuple:
    ...
@typing.overload
def ColorEdit4(label: str, color: ImVec4, flags: int = 0) -> tuple:
    ...
@typing.overload
def ColorEdit4(label: str, color: ImColor, flags: int = 0) -> tuple:
    ...
def ColorEditOptionsPopup(col: float, flags: int) -> None:
    ...
@typing.overload
def ColorPicker3(label: str, color: ImVec4, flags: int = 0) -> tuple:
    ...
@typing.overload
def ColorPicker3(label: str, color: ImColor, flags: int = 0) -> tuple:
    ...
@typing.overload
def ColorPicker4(label: str, color: ImVec4, flags: int = 0, ref_col: float = None) -> tuple:
    ...
@typing.overload
def ColorPicker4(label: str, color: ImColor, flags: int = 0, ref_col: float = None) -> tuple:
    ...
def ColorPickerOptionsPopup(ref_col: float, flags: int) -> None:
    ...
def ColorTooltip(text: str, col: float, flags: int) -> None:
    ...
def Columns(count: int = 1, id: str | None = None, border: bool = True) -> None:
    ...
def Combo(label: str = '', current_item: int = 0, items_separated_by_zeros: str = None, popup_max_height_in_items: int = 0) -> tuple:
    ...
def ConvertSingleModFlagToKey(key: ImGuiKey) -> ImGuiKey:
    ...
def CreateContext(shared_font_atlas: ImFontAtlas | None = None) -> ImGuiContext:
    ...
def CreateNewWindowSettings(name: str) -> ImGuiWindowSettings:
    ...
def DataTypeApplyFromText(buf: str, data_type: int, p_data: capsule, format: str, p_data_when_empty: capsule = 0) -> bool:
    ...
def DataTypeApplyOp(data_type: int, op: int, output: capsule, arg_1: capsule, arg_2: capsule) -> None:
    ...
def DataTypeClamp(data_type: int, p_data: capsule, p_min: capsule, p_max: capsule) -> bool:
    ...
def DataTypeCompare(data_type: int, arg_1: capsule, arg_2: capsule) -> int:
    ...
def DataTypeFormatString(buf: str, buf_size: int, data_type: int, p_data: capsule, format: str) -> int:
    ...
def DataTypeGetInfo(data_type: int) -> ImGuiDataTypeInfo:
    ...
def DebugAllocHook(info: ImGuiDebugAllocInfo, frame_count: int, ptr: capsule, size: int) -> None:
    ...
def DebugBreakButton(label: str, description_of_location: str) -> bool:
    ...
def DebugBreakButtonTooltip(keyboard_only: bool, description_of_location: str) -> None:
    ...
def DebugBreakClearData() -> None:
    ...
def DebugCheckVersionAndDataLayout(version_str: str, sz_io: int, sz_style: int, sz_vec2: int, sz_vec4: int, sz_drawvert: int, sz_drawidx: int) -> bool:
    ...
def DebugDrawCursorPos(col: int = 4278190335) -> None:
    ...
def DebugDrawItemRect(col: int = 4278190335) -> None:
    ...
def DebugDrawLineExtents(col: int = 4278190335) -> None:
    ...
def DebugFlashStyleColor(idx: int) -> None:
    ...
def DebugHookIdInfo(id: int, data_type: int, data_id: capsule, data_id_end: capsule) -> None:
    ...
def DebugLocateItem(target_id: int) -> None:
    ...
def DebugLocateItemOnHover(target_id: int) -> None:
    ...
def DebugLocateItemResolveWithLastItem() -> None:
    ...
def DebugNodeColumns(columns: ImGuiOldColumns) -> None:
    ...
def DebugNodeDockNode(node: ImGuiDockNode, label: str) -> None:
    ...
def DebugNodeDrawCmdShowMeshAndBoundingBox(out_draw_list: ImDrawList, draw_list: ImDrawList, draw_cmd: ImDrawCmd, show_mesh: bool, show_aabb: bool) -> None:
    ...
def DebugNodeDrawList(window: ImGuiWindow, viewport: ImGuiViewportP, draw_list: ImDrawList, label: str) -> None:
    ...
def DebugNodeFont(font: ImFont) -> None:
    ...
def DebugNodeFontGlyph(font: ImFont, glyph: ImFontGlyph) -> None:
    ...
def DebugNodeInputTextState(state: ImGuiInputTextState) -> None:
    ...
def DebugNodeStorage(storage: ImGuiStorage, label: str) -> None:
    ...
def DebugNodeTabBar(tab_bar: ImGuiTabBar, label: str) -> None:
    ...
def DebugNodeTable(table: ImGuiTable) -> None:
    ...
def DebugNodeTableSettings(settings: ImGuiTableSettings) -> None:
    ...
def DebugNodeTypingSelectState(state: ImGuiTypingSelectState) -> None:
    ...
def DebugNodeViewport(viewport: ImGuiViewportP) -> None:
    ...
def DebugNodeWindow(window: ImGuiWindow, label: str) -> None:
    ...
def DebugNodeWindowSettings(settings: ImGuiWindowSettings) -> None:
    ...
def DebugNodeWindowsList(windows: ImVector_ImGuiWindowPtr, label: str) -> None:
    ...
def DebugRenderKeyboardPreview(draw_list: ImDrawList) -> None:
    ...
def DebugRenderViewportThumbnail(draw_list: ImDrawList, viewport: ImGuiViewportP, bb: ImRect) -> None:
    ...
def DebugStartItemPicker() -> None:
    ...
def DebugTextEncoding(text: str) -> None:
    ...
def DebugTextUnformattedWithLocateItem(line_begin: str, line_end: str) -> None:
    ...
def DestroyContext(ctx: ImGuiContext | None = None) -> None:
    ...
def DestroyPlatformWindow(viewport: ImGuiViewportP) -> None:
    ...
def DestroyPlatformWindows() -> None:
    ...
def DockBuilderAddNode(node_id: int = 0, flags: int = 0) -> int:
    ...
def DockBuilderCopyDockSpace(src_dockspace_id: int, dst_dockspace_id: int, in_window_remap_pairs: ImVector_const_charPtr) -> None:
    ...
def DockBuilderCopyNode(src_node_id: int, dst_node_id: int, out_node_remap_pairs: ImVector_ImGuiID) -> None:
    ...
def DockBuilderCopyWindowSettings(src_name: str, dst_name: str) -> None:
    ...
def DockBuilderDockWindow(window_name: str, node_id: int) -> None:
    ...
def DockBuilderFinish(node_id: int) -> None:
    ...
def DockBuilderGetCentralNode(node_id: int) -> ImGuiDockNode:
    ...
def DockBuilderGetNode(node_id: int) -> ImGuiDockNode:
    ...
def DockBuilderRemoveNode(node_id: int) -> None:
    ...
def DockBuilderRemoveNodeChildNodes(node_id: int) -> None:
    ...
def DockBuilderRemoveNodeDockedWindows(node_id: int, clear_settings_refs: bool = True) -> None:
    ...
def DockBuilderSetNodePos(node_id: int, pos: ImVec2) -> None:
    ...
def DockBuilderSetNodeSize(node_id: int, size: ImVec2) -> None:
    ...
def DockBuilderSplitNode(node_id: int, split_dir: ImGuiDir, size_ratio_for_node_at_dir: float, out_id_at_dir: int, out_id_at_opposite_dir: int) -> int:
    ...
def DockContextCalcDropPosForDocking(target: ImGuiWindow, target_node: ImGuiDockNode, payload_window: ImGuiWindow, payload_node: ImGuiDockNode, split_dir: ImGuiDir, split_outer: bool, out_pos: ImVec2) -> bool:
    ...
def DockContextClearNodes(ctx: ImGuiContext, root_id: int, clear_settings_refs: bool) -> None:
    ...
def DockContextEndFrame(ctx: ImGuiContext) -> None:
    ...
def DockContextFindNodeByID(ctx: ImGuiContext, id: int) -> ImGuiDockNode:
    ...
def DockContextGenNodeID(ctx: ImGuiContext) -> int:
    ...
def DockContextInitialize(ctx: ImGuiContext) -> None:
    ...
def DockContextNewFrameUpdateDocking(ctx: ImGuiContext) -> None:
    ...
def DockContextNewFrameUpdateUndocking(ctx: ImGuiContext) -> None:
    ...
def DockContextProcessUndockNode(ctx: ImGuiContext, node: ImGuiDockNode) -> None:
    ...
def DockContextProcessUndockWindow(ctx: ImGuiContext, window: ImGuiWindow, clear_persistent_docking_ref: bool = True) -> None:
    ...
def DockContextQueueDock(ctx: ImGuiContext, target: ImGuiWindow, target_node: ImGuiDockNode, payload: ImGuiWindow, split_dir: ImGuiDir, split_ratio: float, split_outer: bool) -> None:
    ...
def DockContextQueueUndockNode(ctx: ImGuiContext, node: ImGuiDockNode) -> None:
    ...
def DockContextQueueUndockWindow(ctx: ImGuiContext, window: ImGuiWindow) -> None:
    ...
def DockContextRebuildNodes(ctx: ImGuiContext) -> None:
    ...
def DockContextShutdown(ctx: ImGuiContext) -> None:
    ...
def DockNodeBeginAmendTabBar(node: ImGuiDockNode) -> bool:
    ...
def DockNodeEndAmendTabBar() -> None:
    ...
def DockNodeGetDepth(node: ImGuiDockNode) -> int:
    ...
def DockNodeGetRootNode(node: ImGuiDockNode) -> ImGuiDockNode:
    ...
def DockNodeGetWindowMenuButtonId(node: ImGuiDockNode) -> int:
    ...
def DockNodeIsInHierarchyOf(node: ImGuiDockNode, parent: ImGuiDockNode) -> bool:
    ...
def DockNodeWindowMenuHandler_Default(ctx: ImGuiContext, node: ImGuiDockNode, tab_bar: ImGuiTabBar) -> None:
    ...
def DockSpace(dockspace_id: int, size: ImVec2 = ..., flags: int = 0, window_class: ImGuiWindowClass | None = None) -> int:
    ...
def DockSpaceOverViewport(dockspace_id: int = 0, viewport: ImGuiViewport | None = None, flags: int = 0, window_class: ImGuiWindowClass | None = None) -> int:
    ...
def DragBehavior(id: int, data_type: int, p_v: capsule, v_speed: float, p_min: capsule, p_max: capsule, format: str, flags: int) -> bool:
    ...
def DragFloat(label: str, v: float, v_speed: float = 1.0, v_min: float = 0.0, v_max: float = 0.0, format: str = '%.3f', flags: int = 0) -> bool:
    ...
def DragFloat2(label: str, v: float, v_speed: float = 1.0, v_min: float = 0.0, v_max: float = 0.0, format: str = '%.3f', flags: int = 0) -> bool:
    ...
def DragFloat3(label: str, v: float, v_speed: float = 1.0, v_min: float = 0.0, v_max: float = 0.0, format: str = '%.3f', flags: int = 0) -> bool:
    ...
def DragFloat4(label: str, v: float, v_speed: float = 1.0, v_min: float = 0.0, v_max: float = 0.0, format: str = '%.3f', flags: int = 0) -> bool:
    ...
def DragFloatRange2(label: str, v_current_min: float, v_current_max: float, v_speed: float = 1.0, v_min: float = 0.0, v_max: float = 0.0, format: str = '%.3f', format_max: str = 0, flags: int = 0) -> bool:
    ...
def DragInt(label: str, v: int, v_speed: float = 1.0, v_min: int = 0, v_max: int = 0, format: str = '%d', flags: int = 0) -> bool:
    ...
def DragInt2(label: str, v: int, v_speed: float = 1.0, v_min: int = 0, v_max: int = 0, format: str = '%d', flags: int = 0) -> bool:
    ...
def DragInt3(label: str, v: int, v_speed: float = 1.0, v_min: int = 0, v_max: int = 0, format: str = '%d', flags: int = 0) -> bool:
    ...
def DragInt4(label: str, v: int, v_speed: float = 1.0, v_min: int = 0, v_max: int = 0, format: str = '%d', flags: int = 0) -> bool:
    ...
def DragIntRange2(label: str, v_current_min: int, v_current_max: int, v_speed: float = 1.0, v_min: int = 0, v_max: int = 0, format: str = '%d', format_max: str = 0, flags: int = 0) -> bool:
    ...
def DragScalar(label: str, data_type: int, p_data: capsule, v_speed: float = 1.0, p_min: capsule = 0, p_max: capsule = 0, format: str = 0, flags: int = 0) -> bool:
    ...
def DragScalarN(label: str, data_type: int, p_data: capsule, components: int, v_speed: float = 1.0, p_min: capsule = 0, p_max: capsule = 0, format: str = 0, flags: int = 0) -> bool:
    ...
def Dummy(size: ImVec2) -> None:
    ...
def End() -> None:
    ...
def EndChild() -> None:
    ...
def EndColumns() -> None:
    ...
def EndCombo() -> None:
    ...
def EndComboPreview() -> None:
    ...
def EndDisabled() -> None:
    ...
def EndDisabledOverrideReenable() -> None:
    ...
def EndDragDropSource() -> None:
    ...
def EndDragDropTarget() -> None:
    ...
def EndFrame() -> None:
    ...
def EndGroup() -> None:
    ...
def EndListBox() -> None:
    ...
def EndMainMenuBar() -> None:
    ...
def EndMenu() -> None:
    ...
def EndMenuBar() -> None:
    ...
def EndPopup() -> None:
    ...
def EndTabBar() -> None:
    ...
def EndTabItem() -> None:
    ...
def EndTable() -> None:
    ...
def EndTooltip() -> None:
    ...
def ErrorCheckEndFrameRecover(log_callback: ..., user_data: capsule = 0) -> None:
    ...
def ErrorCheckEndWindowRecover(log_callback: ..., user_data: capsule = 0) -> None:
    ...
def ErrorCheckUsingSetCursorPosToExtendParentBoundaries() -> None:
    ...
def FindBestWindowPosForPopup(window: ImGuiWindow) -> ImVec2:
    ...
def FindBestWindowPosForPopupEx(ref_pos: ImVec2, size: ImVec2, last_dir: ImGuiDir, r_outer: ImRect, r_avoid: ImRect, policy: ImGuiPopupPositionPolicy) -> ImVec2:
    ...
def FindBlockingModal(window: ImGuiWindow) -> ImGuiWindow:
    ...
def FindBottomMostVisibleWindowWithinBeginStack(window: ImGuiWindow) -> ImGuiWindow:
    ...
def FindHoveredViewportFromPlatformWindowStack(mouse_platform_pos: ImVec2) -> ImGuiViewportP:
    ...
def FindOrCreateColumns(window: ImGuiWindow, id: int) -> ImGuiOldColumns:
    ...
def FindRenderedTextEnd(text: str, text_end: str = 0) -> str:
    ...
def FindSettingsHandler(type_name: str) -> ImGuiSettingsHandler:
    ...
def FindViewportByID(id: int) -> ImGuiViewport:
    ...
def FindViewportByPlatformHandle(platform_handle: capsule) -> ImGuiViewport:
    ...
def FindWindowByID(id: int) -> ImGuiWindow:
    ...
def FindWindowByName(name: str) -> ImGuiWindow:
    ...
def FindWindowDisplayIndex(window: ImGuiWindow) -> int:
    ...
def FindWindowSettingsByID(id: int) -> ImGuiWindowSettings:
    ...
def FindWindowSettingsByWindow(window: ImGuiWindow) -> ImGuiWindowSettings:
    ...
def FixupKeyChord(key_chord: int) -> int:
    ...
def FocusItem() -> None:
    ...
def FocusTopMostWindowUnderOne(under_this_window: ImGuiWindow, ignore_window: ImGuiWindow, filter_viewport: ImGuiViewport, flags: int) -> None:
    ...
def FocusWindow(window: ImGuiWindow, flags: int = 0) -> None:
    ...
def GcAwakeTransientWindowBuffers(window: ImGuiWindow) -> None:
    ...
def GcCompactTransientMiscBuffers() -> None:
    ...
def GcCompactTransientWindowBuffers(window: ImGuiWindow) -> None:
    ...
def GetActiveID() -> int:
    ...
def GetBackgroundDrawList(viewport: ImGuiViewport | None = None) -> ImDrawList:
    ...
def GetClipboardText() -> str:
    ...
@typing.overload
def GetColorU32(idx: int, alpha_mul: float = 1.0) -> int:
    ...
@typing.overload
def GetColorU32(col: ImVec4) -> int:
    ...
@typing.overload
def GetColorU32(col: int, alpha_mul: float = 1.0) -> int:
    ...
def GetColumnIndex() -> int:
    ...
def GetColumnNormFromOffset(columns: ImGuiOldColumns, offset: float) -> float:
    ...
def GetColumnOffset(column_index: int = -1) -> float:
    ...
def GetColumnOffsetFromNorm(columns: ImGuiOldColumns, offset_norm: float) -> float:
    ...
def GetColumnWidth(column_index: int = -1) -> float:
    ...
def GetColumnsCount() -> int:
    ...
def GetColumnsID(str_id: str, count: int) -> int:
    ...
def GetContentRegionAvail() -> ImVec2:
    ...
def GetContentRegionMax() -> ImVec2:
    ...
def GetContentRegionMaxAbs() -> ImVec2:
    ...
def GetCurrentContext() -> ImGuiContext:
    ...
def GetCurrentFocusScope() -> int:
    ...
def GetCurrentTabBar() -> ImGuiTabBar:
    ...
def GetCurrentTable() -> ImGuiTable:
    ...
def GetCurrentWindow() -> ImGuiWindow:
    ...
def GetCurrentWindowRead() -> ImGuiWindow:
    ...
def GetCursorPos() -> ImVec2:
    ...
def GetCursorPosX() -> float:
    ...
def GetCursorPosY() -> float:
    ...
def GetCursorScreenPos() -> ImVec2:
    ...
def GetCursorStartPos() -> ImVec2:
    ...
def GetDefaultFont() -> ImFont:
    ...
def GetDragDropPayload() -> ImGuiPayload:
    ...
def GetDrawData() -> ImDrawData:
    ...
def GetDrawListSharedData() -> ImDrawListSharedData:
    ...
def GetFocusID() -> int:
    ...
def GetFont() -> ImFont:
    ...
def GetFontSize() -> float:
    ...
def GetFontTexUvWhitePixel() -> ImVec2:
    ...
@typing.overload
def GetForegroundDrawList(viewport: ImGuiViewport | None = None) -> ImDrawList:
    ...
@typing.overload
def GetForegroundDrawList(window: ImGuiWindow) -> ImDrawList:
    ...
def GetFrameCount() -> int:
    ...
def GetFrameHeight() -> float:
    ...
def GetFrameHeightWithSpacing() -> float:
    ...
def GetHoveredID() -> int:
    ...
@typing.overload
def GetID(str_id: str) -> int:
    ...
@typing.overload
def GetID(str_id_begin: str, str_id_end: str) -> int:
    ...
@typing.overload
def GetID(ptr_id: capsule) -> int:
    ...
@typing.overload
def GetIDWithSeed(str_id_begin: str, str_id_end: str, seed: int) -> int:
    ...
@typing.overload
def GetIDWithSeed(n: int, seed: int) -> int:
    ...
def GetIO() -> ImGuiIO:
    ...
def GetInputTextState(id: int) -> ImGuiInputTextState:
    ...
def GetItemFlags() -> int:
    ...
def GetItemID() -> int:
    ...
def GetItemRectMax() -> ImVec2:
    ...
def GetItemRectMin() -> ImVec2:
    ...
def GetItemRectSize() -> ImVec2:
    ...
def GetItemStatusFlags() -> int:
    ...
def GetKeyChordName(key_chord: int) -> str:
    ...
@typing.overload
def GetKeyData(ctx: ImGuiContext, key: ImGuiKey) -> ImGuiKeyData:
    ...
@typing.overload
def GetKeyData(key: ImGuiKey) -> ImGuiKeyData:
    ...
def GetKeyMagnitude2d(key_left: ImGuiKey, key_right: ImGuiKey, key_up: ImGuiKey, key_down: ImGuiKey) -> ImVec2:
    ...
def GetKeyName(key: ImGuiKey) -> str:
    ...
def GetKeyOwner(key: ImGuiKey) -> int:
    ...
def GetKeyOwnerData(ctx: ImGuiContext, key: ImGuiKey) -> ImGuiKeyOwnerData:
    ...
def GetKeyPressedAmount(key: ImGuiKey, repeat_delay: float, rate: float) -> int:
    ...
def GetMainViewport() -> ImGuiViewport:
    ...
def GetMouseClickedCount(button: int) -> int:
    ...
def GetMouseCursor() -> int:
    ...
def GetMouseDragDelta(button: int = 0, lock_threshold: float = -1.0) -> ImVec2:
    ...
def GetMousePos() -> ImVec2:
    ...
def GetMousePosOnOpeningCurrentPopup() -> ImVec2:
    ...
def GetNavTweakPressedAmount(axis: ImGuiAxis) -> float:
    ...
def GetPlatformIO() -> ImGuiPlatformIO:
    ...
def GetPopupAllowedExtentRect(window: ImGuiWindow) -> ImRect:
    ...
def GetScrollMaxX() -> float:
    ...
def GetScrollMaxY() -> float:
    ...
def GetScrollX() -> float:
    ...
def GetScrollY() -> float:
    ...
def GetShortcutRoutingData(key_chord: int) -> ImGuiKeyRoutingData:
    ...
def GetStateStorage() -> ImGuiStorage:
    ...
def GetStyle() -> ImGuiStyle:
    ...
def GetStyleColorName(idx: int) -> str:
    ...
def GetStyleColorVec4(idx: int) -> ImVec4:
    ...
def GetStyleVarInfo(idx: int) -> ImGuiDataVarInfo:
    ...
def GetTextLineHeight() -> float:
    ...
def GetTextLineHeightWithSpacing() -> float:
    ...
def GetTime() -> float:
    ...
def GetTopMostAndVisiblePopupModal() -> ImGuiWindow:
    ...
def GetTopMostPopupModal() -> ImGuiWindow:
    ...
def GetTreeNodeToLabelSpacing() -> float:
    ...
def GetTypematicRepeatRate(flags: int, repeat_delay: float, repeat_rate: float) -> None:
    ...
def GetTypingSelectRequest(flags: int = ...) -> ImGuiTypingSelectRequest:
    ...
def GetVersion() -> str:
    ...
def GetViewportPlatformMonitor(viewport: ImGuiViewport) -> ImGuiPlatformMonitor:
    ...
def GetWindowAlwaysWantOwnTabBar(window: ImGuiWindow) -> bool:
    ...
def GetWindowContentRegionMax() -> ImVec2:
    ...
def GetWindowContentRegionMin() -> ImVec2:
    ...
def GetWindowDockID() -> int:
    ...
def GetWindowDockNode() -> ImGuiDockNode:
    ...
def GetWindowDpiScale() -> float:
    ...
def GetWindowDrawList() -> ImDrawList:
    ...
def GetWindowHeight() -> float:
    ...
def GetWindowPos() -> ImVec2:
    ...
def GetWindowResizeBorderID(window: ImGuiWindow, dir: ImGuiDir) -> int:
    ...
def GetWindowResizeCornerID(window: ImGuiWindow, n: int) -> int:
    ...
def GetWindowScrollbarID(window: ImGuiWindow, axis: ImGuiAxis) -> int:
    ...
def GetWindowScrollbarRect(window: ImGuiWindow, axis: ImGuiAxis) -> ImRect:
    ...
def GetWindowSize() -> ImVec2:
    ...
def GetWindowViewport() -> ImGuiViewport:
    ...
def GetWindowWidth() -> float:
    ...
@typing.overload
def ImAbs(x: int) -> int:
    ...
@typing.overload
def ImAbs(x: float) -> float:
    ...
@typing.overload
def ImAbs(x: float) -> float:
    ...
def ImAlphaBlendColors(col_a: int, col_b: int) -> int:
    ...
def ImBezierCubicCalc(p1: ImVec2, p2: ImVec2, p3: ImVec2, p4: ImVec2, t: float) -> ImVec2:
    ...
def ImBezierCubicClosestPoint(p1: ImVec2, p2: ImVec2, p3: ImVec2, p4: ImVec2, p: ImVec2, num_segments: int) -> ImVec2:
    ...
def ImBezierCubicClosestPointCasteljau(p1: ImVec2, p2: ImVec2, p3: ImVec2, p4: ImVec2, p: ImVec2, tess_tol: float) -> ImVec2:
    ...
def ImBezierQuadraticCalc(p1: ImVec2, p2: ImVec2, p3: ImVec2, t: float) -> ImVec2:
    ...
def ImBitArrayClearAllBits(arr: int, bitcount: int) -> None:
    ...
def ImBitArrayClearBit(arr: int, n: int) -> None:
    ...
def ImBitArrayGetStorageSizeInBytes(bitcount: int) -> int:
    ...
def ImBitArraySetBit(arr: int, n: int) -> None:
    ...
def ImBitArraySetBitRange(arr: int, n: int, n2: int) -> None:
    ...
def ImBitArrayTestBit(arr: int, n: int) -> bool:
    ...
def ImCharIsBlankA(c: str) -> bool:
    ...
def ImCharIsBlankW(c: int) -> bool:
    ...
def ImClamp(v: ImVec2, mn: ImVec2, mx: ImVec2) -> ImVec2:
    ...
def ImDot(a: ImVec2, b: ImVec2) -> float:
    ...
def ImExponentialMovingAverage(avg: float, sample: float, n: int) -> float:
    ...
def ImFileClose(file: _iobuf) -> bool:
    ...
def ImFileGetSize(file: _iobuf) -> int:
    ...
def ImFileLoadToMemory(filename: str, mode: str, out_file_size: int = 0, padding_bytes: int = 0) -> capsule:
    ...
def ImFileOpen(filename: str, mode: str) -> _iobuf:
    ...
def ImFileRead(data: capsule, size: int, count: int, file: _iobuf) -> int:
    ...
def ImFileWrite(data: capsule, size: int, count: int, file: _iobuf) -> int:
    ...
@typing.overload
def ImFloor(f: float) -> float:
    ...
@typing.overload
def ImFloor(v: ImVec2) -> ImVec2:
    ...
def ImFontAtlasBuildFinish(atlas: ImFontAtlas) -> None:
    ...
def ImFontAtlasBuildInit(atlas: ImFontAtlas) -> None:
    ...
def ImFontAtlasBuildMultiplyCalcLookupTable(out_table: int, in_multiply_factor: float) -> None:
    ...
def ImFontAtlasBuildMultiplyRectAlpha8(table: int, pixels: int, x: int, y: int, w: int, h: int, stride: int) -> None:
    ...
def ImFontAtlasBuildPackCustomRects(atlas: ImFontAtlas, stbrp_context_opaque: capsule) -> None:
    ...
def ImFontAtlasBuildRender32bppRectFromString(atlas: ImFontAtlas, x: int, y: int, w: int, h: int, in_str: str, in_marker_char: str, in_marker_pixel_value: int) -> None:
    ...
def ImFontAtlasBuildRender8bppRectFromString(atlas: ImFontAtlas, x: int, y: int, w: int, h: int, in_str: str, in_marker_char: str, in_marker_pixel_value: int) -> None:
    ...
def ImFontAtlasBuildSetupFont(atlas: ImFontAtlas, font: ImFont, font_config: ImFontConfig, ascent: float, descent: float) -> None:
    ...
def ImFontAtlasGetBuilderForStbTruetype() -> ImFontBuilderIO:
    ...
def ImFontAtlasUpdateConfigDataPointers(atlas: ImFontAtlas) -> None:
    ...
def ImHashData(data: capsule, data_size: int, seed: int = 0) -> int:
    ...
def ImHashStr(data: str, data_size: int = 0, seed: int = 0) -> int:
    ...
def ImInvLength(lhs: ImVec2, fail_value: float) -> float:
    ...
def ImIsFloatAboveGuaranteedIntegerPrecision(f: float) -> bool:
    ...
@typing.overload
def ImIsPowerOfTwo(v: int) -> bool:
    ...
@typing.overload
def ImIsPowerOfTwo(v: int) -> bool:
    ...
@typing.overload
def ImLengthSqr(lhs: ImVec2) -> float:
    ...
@typing.overload
def ImLengthSqr(lhs: ImVec4) -> float:
    ...
@typing.overload
def ImLerp(a: ImVec2, b: ImVec2, t: float) -> ImVec2:
    ...
@typing.overload
def ImLerp(a: ImVec2, b: ImVec2, t: ImVec2) -> ImVec2:
    ...
@typing.overload
def ImLerp(a: ImVec4, b: ImVec4, t: float) -> ImVec4:
    ...
def ImLineClosestPoint(a: ImVec2, b: ImVec2, p: ImVec2) -> ImVec2:
    ...
def ImLinearSweep(current: float, target: float, speed: float) -> float:
    ...
@typing.overload
def ImLog(x: float) -> float:
    ...
@typing.overload
def ImLog(x: float) -> float:
    ...
def ImLowerBound(in_begin: ImGuiStoragePair, in_end: ImGuiStoragePair, key: int) -> ImGuiStoragePair:
    ...
def ImMax(lhs: ImVec2, rhs: ImVec2) -> ImVec2:
    ...
def ImMin(lhs: ImVec2, rhs: ImVec2) -> ImVec2:
    ...
def ImModPositive(a: int, b: int) -> int:
    ...
def ImMul(lhs: ImVec2, rhs: ImVec2) -> ImVec2:
    ...
def ImParseFormatFindEnd(format: str) -> str:
    ...
def ImParseFormatFindStart(format: str) -> str:
    ...
def ImParseFormatPrecision(format: str, default_value: int) -> int:
    ...
def ImParseFormatSanitizeForPrinting(fmt_in: str, fmt_out: str, fmt_out_size: int) -> None:
    ...
def ImParseFormatSanitizeForScanning(fmt_in: str, fmt_out: str, fmt_out_size: int) -> str:
    ...
def ImParseFormatTrimDecorations(format: str, buf: str, buf_size: int) -> str:
    ...
@typing.overload
def ImPow(x: float, y: float) -> float:
    ...
@typing.overload
def ImPow(x: float, y: float) -> float:
    ...
def ImRotate(v: ImVec2, cos_a: float, sin_a: float) -> ImVec2:
    ...
@typing.overload
def ImRsqrt(x: float) -> float:
    ...
@typing.overload
def ImRsqrt(x: float) -> float:
    ...
def ImSaturate(f: float) -> float:
    ...
@typing.overload
def ImSign(x: float) -> float:
    ...
@typing.overload
def ImSign(x: float) -> float:
    ...
def ImStrSkipBlank(str: str) -> str:
    ...
def ImStrTrimBlanks(str: str) -> None:
    ...
def ImStrbolW(buf_mid_line: int, buf_begin: int) -> int:
    ...
def ImStrchrRange(str_begin: str, str_end: str, c: str) -> str:
    ...
def ImStrdup(str: str) -> str:
    ...
def ImStrdupcpy(dst: str, p_dst_size: int, str: str) -> str:
    ...
def ImStreolRange(str: str, str_end: str) -> str:
    ...
def ImStricmp(str1: str, str2: str) -> int:
    ...
def ImStristr(haystack: str, haystack_end: str, needle: str, needle_end: str) -> str:
    ...
def ImStrlenW(str: int) -> int:
    ...
def ImStrncpy(dst: str, src: str, count: int) -> None:
    ...
def ImStrnicmp(str1: str, str2: str, count: int) -> int:
    ...
def ImTextCharFromUtf8(out_char: int, in_text: str, in_text_end: str) -> int:
    ...
def ImTextCharToUtf8(out_buf: str, c: int) -> str:
    ...
def ImTextCountCharsFromUtf8(in_text: str, in_text_end: str) -> int:
    ...
def ImTextCountLines(in_text: str, in_text_end: str) -> int:
    ...
def ImTextCountUtf8BytesFromChar(in_text: str, in_text_end: str) -> int:
    ...
def ImTextCountUtf8BytesFromStr(in_text: int, in_text_end: int) -> int:
    ...
def ImTextFindPreviousUtf8Codepoint(in_text_start: str, in_text_curr: str) -> str:
    ...
def ImTextStrToUtf8(out_buf: str, out_buf_size: int, in_text: int, in_text_end: int) -> int:
    ...
def ImToUpper(c: str) -> str:
    ...
def ImTriangleArea(a: ImVec2, b: ImVec2, c: ImVec2) -> float:
    ...
def ImTriangleBarycentricCoords(a: ImVec2, b: ImVec2, c: ImVec2, p: ImVec2, out_u: float, out_v: float, out_w: float) -> None:
    ...
def ImTriangleClosestPoint(a: ImVec2, b: ImVec2, c: ImVec2, p: ImVec2) -> ImVec2:
    ...
def ImTriangleContainsPoint(a: ImVec2, b: ImVec2, c: ImVec2, p: ImVec2) -> bool:
    ...
def ImTriangleIsClockwise(a: ImVec2, b: ImVec2, c: ImVec2) -> bool:
    ...
@typing.overload
def ImTrunc(f: float) -> float:
    ...
@typing.overload
def ImTrunc(v: ImVec2) -> ImVec2:
    ...
def ImUpperPowerOfTwo(v: int) -> int:
    ...
def Image(user_texture_id: int, image_size: ImVec2, uv0: ImVec2 = ..., uv1: ImVec2 = ..., tint_col: ImVec4 = ..., border_col: ImVec4 = ...) -> None:
    ...
def ImageButton(str_id: str, user_texture_id: int, image_size: ImVec2, uv0: ImVec2 = ..., uv1: ImVec2 = ..., bg_col: ImVec4 = ..., tint_col: ImVec4 = ...) -> bool:
    ...
def ImageButtonEx(id: int, texture_id: int, image_size: ImVec2, uv0: ImVec2, uv1: ImVec2, bg_col: ImVec4, tint_col: ImVec4, flags: int = 0) -> bool:
    ...
def Indent(indent_w: float = 0.0) -> None:
    ...
def Initialize() -> None:
    ...
def InputDouble(label: str, v: float, step: float = 0.0, step_fast: float = 0.0, format: str = '%.6f', flags: int = 0) -> tuple:
    ...
def InputFloat(label: str, v: float, step: float = 0.0, step_fast: float = 0.0, format: str = '%.3f', flags: int = 0) -> tuple:
    ...
def InputFloat2(label: str, v: tuple[float, float], format: str = '%.3f', flags: int = 0) -> tuple:
    ...
def InputFloat3(label: str, v: tuple[float, float, float], format: str = '%.3f', flags: int = 0) -> tuple:
    ...
def InputFloat4(label: str, v: tuple[float, float, float, float], format: str = '%.3f', flags: int = 0) -> tuple:
    ...
def InputInt(label: str, v: int, step: int = 1, step_fast: int = 100, flags: int = 0) -> tuple:
    ...
def InputInt2(label: str, v: tuple[int, int], flags: int = 0) -> tuple:
    ...
def InputInt3(label: str, v: tuple[int, int, int], flags: int = 0) -> tuple:
    ...
def InputInt4(label: str, v: tuple[int, int, int, int], flags: int = 0) -> tuple:
    ...
def InputScalar(label: str, data_type: int, p_data: capsule, p_step: capsule = 0, p_step_fast: capsule = 0, format: str = 0, flags: int = 0) -> bool:
    ...
def InputScalarN(label: str, data_type: int, p_data: capsule, components: int, p_step: capsule = 0, p_step_fast: capsule = 0, format: str = 0, flags: int = 0) -> bool:
    ...
def InputText(label: str, text: str, flags: int = 0) -> tuple:
    ...
def InputTextDeactivateHook(id: int) -> None:
    ...
def InputTextEx(label: str, hint: str, buf: str, buf_size: int, size_arg: ImVec2, flags: int, callback: ... = 0, user_data: capsule = 0) -> bool:
    ...
def InputTextMultiline(label: str, text: str, size: ImVec2 = ..., flags: int = 0) -> tuple:
    ...
def InputTextWithHint(label: str, hint: str, text: str, flags: int = 0) -> tuple:
    ...
def InvisibleButton(str_id: str, size: ImVec2, flags: int = 0) -> bool:
    ...
def IsActiveIdUsingNavDir(dir: ImGuiDir) -> bool:
    ...
def IsAliasKey(key: ImGuiKey) -> bool:
    ...
def IsAnyItemActive() -> bool:
    ...
def IsAnyItemFocused() -> bool:
    ...
def IsAnyItemHovered() -> bool:
    ...
def IsAnyMouseDown() -> bool:
    ...
def IsClippedEx(bb: ImRect, id: int) -> bool:
    ...
def IsDragDropActive() -> bool:
    ...
def IsDragDropPayloadBeingAccepted() -> bool:
    ...
def IsGamepadKey(key: ImGuiKey) -> bool:
    ...
def IsItemActivated() -> bool:
    ...
def IsItemActive() -> bool:
    ...
def IsItemClicked(mouse_button: int = 0) -> bool:
    ...
def IsItemDeactivated() -> bool:
    ...
def IsItemDeactivatedAfterEdit() -> bool:
    ...
def IsItemEdited() -> bool:
    ...
def IsItemFocused() -> bool:
    ...
def IsItemHovered(flags: int = 0) -> bool:
    ...
def IsItemToggledOpen() -> bool:
    ...
def IsItemToggledSelection() -> bool:
    ...
def IsItemVisible() -> bool:
    ...
@typing.overload
def IsKeyChordPressed(key_chord: int) -> bool:
    ...
@typing.overload
def IsKeyChordPressed(key_chord: int, flags: int, owner_id: int = 0) -> bool:
    ...
@typing.overload
def IsKeyDown(key: ImGuiKey) -> bool:
    ...
@typing.overload
def IsKeyDown(key: ImGuiKey, owner_id: int) -> bool:
    ...
@typing.overload
def IsKeyPressed(key: ImGuiKey, repeat: bool = True) -> bool:
    ...
@typing.overload
def IsKeyPressed(key: ImGuiKey, flags: int, owner_id: int = 0) -> bool:
    ...
@typing.overload
def IsKeyReleased(key: ImGuiKey) -> bool:
    ...
@typing.overload
def IsKeyReleased(key: ImGuiKey, owner_id: int) -> bool:
    ...
def IsKeyboardKey(key: ImGuiKey) -> bool:
    ...
def IsLegacyKey(key: ImGuiKey) -> bool:
    ...
def IsModKey(key: ImGuiKey) -> bool:
    ...
@typing.overload
def IsMouseClicked(button: int, repeat: bool = False) -> bool:
    ...
@typing.overload
def IsMouseClicked(button: int, flags: int, owner_id: int = 0) -> bool:
    ...
@typing.overload
def IsMouseDoubleClicked(button: int) -> bool:
    ...
@typing.overload
def IsMouseDoubleClicked(button: int, owner_id: int) -> bool:
    ...
@typing.overload
def IsMouseDown(button: int) -> bool:
    ...
@typing.overload
def IsMouseDown(button: int, owner_id: int) -> bool:
    ...
def IsMouseDragPastThreshold(button: int, lock_threshold: float = -1.0) -> bool:
    ...
def IsMouseDragging(button: int, lock_threshold: float = -1.0) -> bool:
    ...
def IsMouseHoveringRect(r_min: ImVec2, r_max: ImVec2, clip: bool = True) -> bool:
    ...
def IsMouseKey(key: ImGuiKey) -> bool:
    ...
def IsMousePosValid(mouse_pos: ImVec2 | None = None) -> bool:
    ...
@typing.overload
def IsMouseReleased(button: int) -> bool:
    ...
@typing.overload
def IsMouseReleased(button: int, owner_id: int) -> bool:
    ...
def IsNamedKey(key: ImGuiKey) -> bool:
    ...
def IsNamedKeyOrMod(key: ImGuiKey) -> bool:
    ...
@typing.overload
def IsPopupOpen(str_id: str, flags: int = 0) -> bool:
    ...
@typing.overload
def IsPopupOpen(id: int, popup_flags: int) -> bool:
    ...
@typing.overload
def IsRectVisible(size: ImVec2) -> bool:
    ...
@typing.overload
def IsRectVisible(rect_min: ImVec2, rect_max: ImVec2) -> bool:
    ...
def IsWindowAbove(potential_above: ImGuiWindow, potential_below: ImGuiWindow) -> bool:
    ...
def IsWindowAppearing() -> bool:
    ...
def IsWindowChildOf(window: ImGuiWindow, potential_parent: ImGuiWindow, popup_hierarchy: bool, dock_hierarchy: bool) -> bool:
    ...
def IsWindowCollapsed() -> bool:
    ...
def IsWindowContentHoverable(window: ImGuiWindow, flags: int = 0) -> bool:
    ...
def IsWindowDocked() -> bool:
    ...
def IsWindowFocused(flags: int = 0) -> bool:
    ...
def IsWindowHovered(flags: int = 0) -> bool:
    ...
def IsWindowNavFocusable(window: ImGuiWindow) -> bool:
    ...
def IsWindowWithinBeginStackOf(window: ImGuiWindow, potential_parent: ImGuiWindow) -> bool:
    ...
def ItemAdd(bb: ImRect, id: int, nav_bb: ImRect | None = None, extra_flags: int = 0) -> bool:
    ...
def ItemHoverable(bb: ImRect, id: int, item_flags: int) -> bool:
    ...
@typing.overload
def ItemSize(size: ImVec2, text_baseline_y: float = -1.0) -> None:
    ...
@typing.overload
def ItemSize(bb: ImRect, text_baseline_y: float = -1.0) -> None:
    ...
def KeepAliveID(id: int) -> None:
    ...
def LoadIniSettingsFromDisk(ini_filename: str) -> None:
    ...
def LoadIniSettingsFromMemory(ini_data: str, ini_size: int = 0) -> None:
    ...
def LocalizeGetMsg(key: ImGuiLocKey) -> str:
    ...
def LocalizeRegisterEntries(entries: ImGuiLocEntry, count: int) -> None:
    ...
def LogBegin(type: ImGuiLogType, auto_open_depth: int) -> None:
    ...
def LogButtons() -> None:
    ...
def LogFinish() -> None:
    ...
def LogRenderedText(ref_pos: ImVec2, text: str, text_end: str = 0) -> None:
    ...
def LogSetNextTextDecoration(prefix: str, suffix: str) -> None:
    ...
def LogToBuffer(auto_open_depth: int = -1) -> None:
    ...
def LogToClipboard(auto_open_depth: int = -1) -> None:
    ...
def LogToFile(auto_open_depth: int = -1, filename: str = 0) -> None:
    ...
def LogToTTY(auto_open_depth: int = -1) -> None:
    ...
@typing.overload
def MarkIniSettingsDirty() -> None:
    ...
@typing.overload
def MarkIniSettingsDirty(window: ImGuiWindow) -> None:
    ...
def MarkItemEdited(id: int) -> None:
    ...
def MemAlloc(size: int) -> capsule:
    ...
def MemFree(ptr: capsule) -> None:
    ...
@typing.overload
def MenuItem(label: str, shortcut: str = 0, selected: bool = False, enabled: bool = True) -> bool:
    ...
@typing.overload
def MenuItem(label: str, shortcut: str, p_selected: bool, enabled: bool = True) -> bool:
    ...
def MenuItemEx(label: str, icon: str, shortcut: str = 0, selected: bool = False, enabled: bool = True) -> bool:
    ...
def MouseButtonToKey(button: int) -> ImGuiKey:
    ...
def NavClearPreferredPosForAxis(axis: ImGuiAxis) -> None:
    ...
def NavHighlightActivated(id: int) -> None:
    ...
def NavInitRequestApplyResult() -> None:
    ...
def NavInitWindow(window: ImGuiWindow, force_reinit: bool) -> None:
    ...
def NavMoveRequestApplyResult() -> None:
    ...
def NavMoveRequestButNoResultYet() -> bool:
    ...
def NavMoveRequestCancel() -> None:
    ...
def NavMoveRequestForward(move_dir: ImGuiDir, clip_dir: ImGuiDir, move_flags: int, scroll_flags: int) -> None:
    ...
def NavMoveRequestResolveWithLastItem(result: ImGuiNavItemData) -> None:
    ...
def NavMoveRequestResolveWithPastTreeNode(result: ImGuiNavItemData, tree_node_data: ImGuiNavTreeNodeData) -> None:
    ...
def NavMoveRequestSubmit(move_dir: ImGuiDir, clip_dir: ImGuiDir, move_flags: int, scroll_flags: int) -> None:
    ...
def NavMoveRequestTryWrapping(window: ImGuiWindow, move_flags: int) -> None:
    ...
def NavRestoreHighlightAfterMove() -> None:
    ...
def NavUpdateCurrentWindowIsScrollPushableX() -> None:
    ...
def NewFrame() -> None:
    ...
def NewLine() -> None:
    ...
def NextColumn() -> None:
    ...
@typing.overload
def OpenPopup(str_id: str, popup_flags: int = 0) -> None:
    ...
@typing.overload
def OpenPopup(id: int, popup_flags: int = 0) -> None:
    ...
def OpenPopupEx(id: int, popup_flags: int = ...) -> None:
    ...
def OpenPopupOnItemClick(str_id: str = 0, popup_flags: int = 1) -> None:
    ...
def PlotHistogram(label: str, values: float, values_count: int, values_offset: int = 0, overlay_text: str = 0, scale_min: float = 3.4028234663852886e+38, scale_max: float = 3.4028234663852886e+38, graph_size: ImVec2 = ..., stride: int = 4) -> None:
    ...
def PlotLines(label: str, values: float, values_count: int, values_offset: int = 0, overlay_text: str = 0, scale_min: float = 3.4028234663852886e+38, scale_max: float = 3.4028234663852886e+38, graph_size: ImVec2 = ..., stride: int = 4) -> None:
    ...
def PopButtonRepeat() -> None:
    ...
def PopClipRect() -> None:
    ...
def PopColumnsBackground() -> None:
    ...
def PopFocusScope() -> None:
    ...
def PopFont() -> None:
    ...
def PopID() -> None:
    ...
def PopItemFlag() -> None:
    ...
def PopItemWidth() -> None:
    ...
def PopStyleColor(count: int = 1) -> None:
    ...
def PopStyleVar(count: int = 1) -> None:
    ...
def PopTabStop() -> None:
    ...
def PopTextWrapPos() -> None:
    ...
def ProgressBar(fraction: float, size_arg: ImVec2 = ..., overlay: str = 0) -> None:
    ...
def PushButtonRepeat(repeat: bool) -> None:
    ...
def PushClipRect(clip_rect_min: ImVec2, clip_rect_max: ImVec2, intersect_with_current_clip_rect: bool) -> None:
    ...
def PushColumnClipRect(column_index: int) -> None:
    ...
def PushColumnsBackground() -> None:
    ...
def PushFocusScope(id: int) -> None:
    ...
def PushFont(font: ImFont) -> None:
    ...
@typing.overload
def PushID(str_id: str) -> None:
    ...
@typing.overload
def PushID(str_id_begin: str, str_id_end: str) -> None:
    ...
@typing.overload
def PushID(ptr_id: capsule) -> None:
    ...
@typing.overload
def PushID(int_id: int) -> None:
    ...
def PushItemFlag(option: int, enabled: bool) -> None:
    ...
def PushItemWidth(item_width: float) -> None:
    ...
def PushMultiItemsWidths(components: int, width_full: float) -> None:
    ...
def PushOverrideID(id: int) -> None:
    ...
@typing.overload
def PushStyleColor(idx: int, col: int) -> None:
    ...
@typing.overload
def PushStyleColor(idx: int, col: ImVec4) -> None:
    ...
@typing.overload
def PushStyleVar(idx: int, val: float) -> None:
    ...
@typing.overload
def PushStyleVar(idx: int, val: ImVec2) -> None:
    ...
def PushTabStop(tab_stop: bool) -> None:
    ...
def PushTextWrapPos(wrap_local_pos_x: float = 0.0) -> None:
    ...
@typing.overload
def RadioButton(label: str, active: bool) -> bool:
    ...
@typing.overload
def RadioButton(label: str, v: int, v_button: int) -> bool:
    ...
def RemoveContextHook(context: ImGuiContext, hook_to_remove: int) -> None:
    ...
def RemoveSettingsHandler(type_name: str) -> None:
    ...
def Render() -> None:
    ...
def RenderArrow(draw_list: ImDrawList, pos: ImVec2, col: int, dir: ImGuiDir, scale: float = 1.0) -> None:
    ...
def RenderArrowDockMenu(draw_list: ImDrawList, p_min: ImVec2, sz: float, col: int) -> None:
    ...
def RenderArrowPointingAt(draw_list: ImDrawList, pos: ImVec2, half_sz: ImVec2, direction: ImGuiDir, col: int) -> None:
    ...
def RenderBullet(draw_list: ImDrawList, pos: ImVec2, col: int) -> None:
    ...
def RenderCheckMark(draw_list: ImDrawList, pos: ImVec2, col: int, sz: float) -> None:
    ...
def RenderColorRectWithAlphaCheckerboard(draw_list: ImDrawList, p_min: ImVec2, p_max: ImVec2, fill_col: int, grid_step: float, grid_off: ImVec2, rounding: float = 0.0, flags: int = 0) -> None:
    ...
def RenderDragDropTargetRect(bb: ImRect, item_clip_rect: ImRect) -> None:
    ...
def RenderFrame(p_min: ImVec2, p_max: ImVec2, fill_col: int, border: bool = True, rounding: float = 0.0) -> None:
    ...
def RenderFrameBorder(p_min: ImVec2, p_max: ImVec2, rounding: float = 0.0) -> None:
    ...
def RenderMouseCursor(pos: ImVec2, scale: float, mouse_cursor: int, col_fill: int, col_border: int, col_shadow: int) -> None:
    ...
def RenderNavHighlight(bb: ImRect, id: int, flags: int = ...) -> None:
    ...
def RenderPlatformWindowsDefault(platform_render_arg: capsule = 0, renderer_render_arg: capsule = 0) -> None:
    ...
def RenderRectFilledRangeH(draw_list: ImDrawList, rect: ImRect, col: int, x_start_norm: float, x_end_norm: float, rounding: float) -> None:
    ...
def RenderRectFilledWithHole(draw_list: ImDrawList, outer: ImRect, inner: ImRect, col: int, rounding: float) -> None:
    ...
def RenderText(pos: ImVec2, text: str, text_end: str = 0, hide_text_after_hash: bool = True) -> None:
    ...
def RenderTextClipped(pos_min: ImVec2, pos_max: ImVec2, text: str, text_end: str, text_size_if_known: ImVec2, align: ImVec2 = ..., clip_rect: ImRect | None = None) -> None:
    ...
def RenderTextClippedEx(draw_list: ImDrawList, pos_min: ImVec2, pos_max: ImVec2, text: str, text_end: str, text_size_if_known: ImVec2, align: ImVec2 = ..., clip_rect: ImRect | None = None) -> None:
    ...
def RenderTextEllipsis(draw_list: ImDrawList, pos_min: ImVec2, pos_max: ImVec2, clip_max_x: float, ellipsis_max_x: float, text: str, text_end: str, text_size_if_known: ImVec2) -> None:
    ...
def RenderTextWrapped(pos: ImVec2, text: str, text_end: str, wrap_width: float) -> None:
    ...
def ResetMouseDragDelta(button: int = 0) -> None:
    ...
def SameLine(offset_from_start_x: float = 0.0, spacing: float = -1.0) -> None:
    ...
def SaveIniSettingsToDisk(ini_filename: str) -> None:
    ...
def SaveIniSettingsToMemory(out_ini_size: int = 0) -> str:
    ...
def ScaleWindowsInViewport(viewport: ImGuiViewportP, scale: float) -> None:
    ...
def ScrollToBringRectIntoView(window: ImGuiWindow, rect: ImRect) -> None:
    ...
def ScrollToItem(flags: int = 0) -> None:
    ...
def ScrollToRect(window: ImGuiWindow, rect: ImRect, flags: int = 0) -> None:
    ...
def ScrollToRectEx(window: ImGuiWindow, rect: ImRect, flags: int = 0) -> ImVec2:
    ...
def Scrollbar(axis: ImGuiAxis) -> None:
    ...
def ScrollbarEx(bb: ImRect, id: int, axis: ImGuiAxis, p_scroll_v: int, avail_v: int, contents_v: int, flags: int) -> bool:
    ...
@typing.overload
def Selectable(label: str, selected: bool = False, flags: int = 0, size: ImVec2 = ...) -> bool:
    ...
@typing.overload
def Selectable(label: str, p_selected: bool, flags: int = 0, size: ImVec2 = ...) -> bool:
    ...
def Separator() -> None:
    ...
def SeparatorEx(flags: int, thickness: float = 1.0) -> None:
    ...
def SeparatorText(label: str) -> None:
    ...
def SeparatorTextEx(id: int, label: str, label_end: str, extra_width: float) -> None:
    ...
def SetActiveID(id: int, window: ImGuiWindow) -> None:
    ...
def SetActiveIdUsingAllKeyboardKeys() -> None:
    ...
def SetAllocatorFunctions(alloc_func: ..., free_func: ..., user_data: capsule = 0) -> None:
    ...
def SetClipboardText(text: str) -> None:
    ...
def SetColorEditOptions(flags: int) -> None:
    ...
def SetColumnOffset(column_index: int, offset_x: float) -> None:
    ...
def SetColumnWidth(column_index: int, width: float) -> None:
    ...
def SetCurrentContext(ctx: ImGuiContext) -> None:
    ...
def SetCurrentFont(font: ImFont) -> None:
    ...
def SetCurrentViewport(window: ImGuiWindow, viewport: ImGuiViewportP) -> None:
    ...
def SetCursorPos(local_pos: ImVec2) -> None:
    ...
def SetCursorPosX(local_x: float) -> None:
    ...
def SetCursorPosY(local_y: float) -> None:
    ...
def SetCursorScreenPos(pos: ImVec2) -> None:
    ...
def SetDragDropPayload(type: str, data: capsule, sz: int, cond: int = 0) -> bool:
    ...
def SetFocusID(id: int, window: ImGuiWindow) -> None:
    ...
def SetHoveredID(id: int) -> None:
    ...
def SetItemDefaultFocus() -> None:
    ...
def SetItemKeyOwner(key: ImGuiKey, flags: int = 0) -> None:
    ...
def SetKeyOwner(key: ImGuiKey, owner_id: int, flags: int = 0) -> None:
    ...
def SetKeyOwnersForKeyChord(key: int, owner_id: int, flags: int = 0) -> None:
    ...
def SetKeyboardFocusHere(offset: int = 0) -> None:
    ...
def SetLastItemData(item_id: int, in_flags: int, status_flags: int, item_rect: ImRect) -> None:
    ...
def SetMouseCursor(cursor_type: int) -> None:
    ...
def SetNavFocusScope(focus_scope_id: int) -> None:
    ...
def SetNavID(id: int, nav_layer: ImGuiNavLayer, focus_scope_id: int, rect_rel: ImRect) -> None:
    ...
def SetNavWindow(window: ImGuiWindow) -> None:
    ...
def SetNextFrameWantCaptureKeyboard(want_capture_keyboard: bool) -> None:
    ...
def SetNextFrameWantCaptureMouse(want_capture_mouse: bool) -> None:
    ...
def SetNextItemAllowOverlap() -> None:
    ...
def SetNextItemOpen(is_open: bool, cond: int = 0) -> None:
    ...
def SetNextItemRefVal(data_type: int, p_data: capsule) -> None:
    ...
def SetNextItemSelectionUserData(selection_user_data: int) -> None:
    ...
def SetNextItemShortcut(key_chord: int, flags: int = 0) -> None:
    ...
def SetNextItemWidth(item_width: float) -> None:
    ...
def SetNextWindowBgAlpha(alpha: float) -> None:
    ...
def SetNextWindowClass(window_class: ImGuiWindowClass) -> None:
    ...
def SetNextWindowCollapsed(collapsed: bool, cond: int = 0) -> None:
    ...
def SetNextWindowContentSize(size: ImVec2) -> None:
    ...
def SetNextWindowDockID(dock_id: int, cond: int = 0) -> None:
    ...
def SetNextWindowFocus() -> None:
    ...
def SetNextWindowPos(pos: ImVec2, cond: int = 0, pivot: ImVec2 = ...) -> None:
    ...
def SetNextWindowRefreshPolicy(flags: int) -> None:
    ...
def SetNextWindowScroll(scroll: ImVec2) -> None:
    ...
def SetNextWindowSize(size: ImVec2, cond: int = 0) -> None:
    ...
def SetNextWindowSizeConstraints(size_min: ImVec2, size_max: ImVec2, custom_callback: ... = 0, custom_callback_data: capsule = 0) -> None:
    ...
def SetNextWindowViewport(viewport_id: int) -> None:
    ...
@typing.overload
def SetScrollFromPosX(local_x: float, center_x_ratio: float = 0.5) -> None:
    ...
@typing.overload
def SetScrollFromPosX(window: ImGuiWindow, local_x: float, center_x_ratio: float) -> None:
    ...
@typing.overload
def SetScrollFromPosY(local_y: float, center_y_ratio: float = 0.5) -> None:
    ...
@typing.overload
def SetScrollFromPosY(window: ImGuiWindow, local_y: float, center_y_ratio: float) -> None:
    ...
def SetScrollHereX(center_x_ratio: float = 0.5) -> None:
    ...
def SetScrollHereY(center_y_ratio: float = 0.5) -> None:
    ...
@typing.overload
def SetScrollX(scroll_x: float) -> None:
    ...
@typing.overload
def SetScrollX(window: ImGuiWindow, scroll_x: float) -> None:
    ...
@typing.overload
def SetScrollY(scroll_y: float) -> None:
    ...
@typing.overload
def SetScrollY(window: ImGuiWindow, scroll_y: float) -> None:
    ...
def SetShortcutRouting(key_chord: int, flags: int, owner_id: int) -> bool:
    ...
def SetStateStorage(storage: ImGuiStorage) -> None:
    ...
def SetTabItemClosed(tab_or_docked_window_label: str) -> None:
    ...
def SetWindowClipRectBeforeSetChannel(window: ImGuiWindow, clip_rect: ImRect) -> None:
    ...
@typing.overload
def SetWindowCollapsed(collapsed: bool, cond: int = 0) -> None:
    ...
@typing.overload
def SetWindowCollapsed(name: str, collapsed: bool, cond: int = 0) -> None:
    ...
@typing.overload
def SetWindowCollapsed(window: ImGuiWindow, collapsed: bool, cond: int = 0) -> None:
    ...
def SetWindowDock(window: ImGuiWindow, dock_id: int, cond: int) -> None:
    ...
@typing.overload
def SetWindowFocus() -> None:
    ...
@typing.overload
def SetWindowFocus(name: str) -> None:
    ...
def SetWindowFontScale(scale: float) -> None:
    ...
def SetWindowHiddenAndSkipItemsForCurrentFrame(window: ImGuiWindow) -> None:
    ...
def SetWindowHitTestHole(window: ImGuiWindow, pos: ImVec2, size: ImVec2) -> None:
    ...
def SetWindowParentWindowForFocusRoute(window: ImGuiWindow, parent_window: ImGuiWindow) -> None:
    ...
@typing.overload
def SetWindowPos(pos: ImVec2, cond: int = 0) -> None:
    ...
@typing.overload
def SetWindowPos(name: str, pos: ImVec2, cond: int = 0) -> None:
    ...
@typing.overload
def SetWindowPos(window: ImGuiWindow, pos: ImVec2, cond: int = 0) -> None:
    ...
@typing.overload
def SetWindowSize(size: ImVec2, cond: int = 0) -> None:
    ...
@typing.overload
def SetWindowSize(name: str, size: ImVec2, cond: int = 0) -> None:
    ...
@typing.overload
def SetWindowSize(window: ImGuiWindow, size: ImVec2, cond: int = 0) -> None:
    ...
def SetWindowViewport(window: ImGuiWindow, viewport: ImGuiViewportP) -> None:
    ...
def ShadeVertsLinearColorGradientKeepAlpha(draw_list: ImDrawList, vert_start_idx: int, vert_end_idx: int, gradient_p0: ImVec2, gradient_p1: ImVec2, col0: int, col1: int) -> None:
    ...
def ShadeVertsLinearUV(draw_list: ImDrawList, vert_start_idx: int, vert_end_idx: int, a: ImVec2, b: ImVec2, uv_a: ImVec2, uv_b: ImVec2, clamp: bool) -> None:
    ...
def ShadeVertsTransformPos(draw_list: ImDrawList, vert_start_idx: int, vert_end_idx: int, pivot_in: ImVec2, cos_a: float, sin_a: float, pivot_out: ImVec2) -> None:
    ...
@typing.overload
def Shortcut(key_chord: int, flags: int = 0) -> bool:
    ...
@typing.overload
def Shortcut(key_chord: int, flags: int, owner_id: int) -> bool:
    ...
def ShowAboutWindow(is_open: bool = True) -> bool:
    ...
def ShowDebugLogWindow(is_open: bool = True) -> bool:
    ...
def ShowDemoWindow(is_open: bool = True) -> bool:
    ...
def ShowFontAtlas(atlas: ImFontAtlas) -> None:
    ...
def ShowFontSelector(label: str) -> None:
    ...
def ShowIDStackToolWindow(is_open: bool = True) -> bool:
    ...
def ShowMetricsWindow(is_open: bool = True) -> bool:
    ...
def ShowStyleEditor(ref: ImGuiStyle | None = None) -> None:
    ...
def ShowStyleSelector(label: str) -> bool:
    ...
def ShowUserGuide() -> None:
    ...
def ShrinkWidths(items: ImGuiShrinkWidthItem, count: int, width_excess: float) -> None:
    ...
def Shutdown() -> None:
    ...
def SliderAngle(label: str, v_rad: float, v_degrees_min: float = -360.0, v_degrees_max: float = 360.0, format: str = '%.0f deg', flags: int = 0) -> tuple:
    ...
def SliderBehavior(bb: ImRect, id: int, data_type: int, p_v: capsule, p_min: capsule, p_max: capsule, format: str, flags: int, out_grab_bb: ImRect) -> bool:
    ...
def SliderFloat(label: str, v: float, v_min: float, v_max: float, format: str = '%.3f', flags: int = 0) -> tuple:
    ...
def SliderFloat2(label: str, v: tuple[float, float], v_min: float, v_max: float, format: str = '%.3f', flags: int = 0) -> tuple:
    ...
def SliderFloat3(label: str, v: tuple[float, float, float], v_min: float, v_max: float, format: str = '%.3f', flags: int = 0) -> tuple:
    ...
def SliderFloat4(label: str, v: tuple[float, float, float, float], v_min: float, v_max: float, format: str = '%.3f', flags: int = 0) -> tuple:
    ...
def SliderInt(label: str, v: int, v_min: int, v_max: int, format: str = '%d', flags: int = 0) -> tuple:
    ...
def SliderInt2(label: str, v: tuple[int, int], v_min: int, v_max: int, format: str = '%d', flags: int = 0) -> tuple:
    ...
def SliderInt3(label: str, v: tuple[int, int, int], v_min: int, v_max: int, format: str = '%d', flags: int = 0) -> tuple:
    ...
def SliderInt4(label: str, v: tuple[int, int, int, int], v_min: int, v_max: int, format: str = '%d', flags: int = 0) -> tuple:
    ...
def SliderScalar(label: str, data_type: int, p_data: capsule, p_min: capsule, p_max: capsule, format: str = 0, flags: int = 0) -> bool:
    ...
def SliderScalarN(label: str, data_type: int, p_data: capsule, components: int, p_min: capsule, p_max: capsule, format: str = 0, flags: int = 0) -> bool:
    ...
def SmallButton(label: str) -> bool:
    ...
def Spacing() -> None:
    ...
def SplitterBehavior(bb: ImRect, id: int, axis: ImGuiAxis, size1: float, size2: float, min_size1: float, min_size2: float, hover_extend: float = 0.0, hover_visibility_delay: float = 0.0, bg_col: int = 0) -> bool:
    ...
def StartMouseMovingWindow(window: ImGuiWindow) -> None:
    ...
def StartMouseMovingWindowOrNode(window: ImGuiWindow, node: ImGuiDockNode, undock: bool) -> None:
    ...
def StyleColorsClassic(dst: ImGuiStyle | None = None) -> None:
    ...
def StyleColorsDark(dst: ImGuiStyle | None = None) -> None:
    ...
def StyleColorsLight(dst: ImGuiStyle | None = None) -> None:
    ...
def TabBarAddTab(tab_bar: ImGuiTabBar, tab_flags: int, window: ImGuiWindow) -> None:
    ...
def TabBarCloseTab(tab_bar: ImGuiTabBar, tab: ImGuiTabItem) -> None:
    ...
def TabBarFindMostRecentlySelectedTabForActiveWindow(tab_bar: ImGuiTabBar) -> ImGuiTabItem:
    ...
def TabBarFindTabByID(tab_bar: ImGuiTabBar, tab_id: int) -> ImGuiTabItem:
    ...
def TabBarFindTabByOrder(tab_bar: ImGuiTabBar, order: int) -> ImGuiTabItem:
    ...
def TabBarGetCurrentTab(tab_bar: ImGuiTabBar) -> ImGuiTabItem:
    ...
def TabBarGetTabName(tab_bar: ImGuiTabBar, tab: ImGuiTabItem) -> str:
    ...
def TabBarGetTabOrder(tab_bar: ImGuiTabBar, tab: ImGuiTabItem) -> int:
    ...
def TabBarProcessReorder(tab_bar: ImGuiTabBar) -> bool:
    ...
def TabBarQueueFocus(tab_bar: ImGuiTabBar, tab: ImGuiTabItem) -> None:
    ...
def TabBarQueueReorder(tab_bar: ImGuiTabBar, tab: ImGuiTabItem, offset: int) -> None:
    ...
def TabBarQueueReorderFromMousePos(tab_bar: ImGuiTabBar, tab: ImGuiTabItem, mouse_pos: ImVec2) -> None:
    ...
def TabBarRemoveTab(tab_bar: ImGuiTabBar, tab_id: int) -> None:
    ...
def TabItemBackground(draw_list: ImDrawList, bb: ImRect, flags: int, col: int) -> None:
    ...
def TabItemButton(label: str, flags: int = 0) -> bool:
    ...
@typing.overload
def TabItemCalcSize(label: str, has_close_button_or_unsaved_marker: bool) -> ImVec2:
    ...
@typing.overload
def TabItemCalcSize(window: ImGuiWindow) -> ImVec2:
    ...
def TabItemEx(tab_bar: ImGuiTabBar, label: str, p_open: bool, flags: int, docked_window: ImGuiWindow) -> bool:
    ...
def TabItemLabelAndCloseButton(draw_list: ImDrawList, bb: ImRect, flags: int, frame_padding: ImVec2, label: str, tab_id: int, close_button_id: int, is_contents_visible: bool, out_just_closed: bool, out_text_clipped: bool) -> None:
    ...
def TableAngledHeadersRow() -> None:
    ...
def TableAngledHeadersRowEx(row_id: int, angle: float, max_label_width: float, data: ImGuiTableHeaderData, data_count: int) -> None:
    ...
def TableBeginApplyRequests(table: ImGuiTable) -> None:
    ...
def TableBeginCell(table: ImGuiTable, column_n: int) -> None:
    ...
def TableBeginContextMenuPopup(table: ImGuiTable) -> bool:
    ...
def TableBeginInitMemory(table: ImGuiTable, columns_count: int) -> None:
    ...
def TableBeginRow(table: ImGuiTable) -> None:
    ...
def TableDrawBorders(table: ImGuiTable) -> None:
    ...
def TableDrawDefaultContextMenu(table: ImGuiTable, flags_for_section_to_display: int) -> None:
    ...
def TableEndCell(table: ImGuiTable) -> None:
    ...
def TableEndRow(table: ImGuiTable) -> None:
    ...
def TableFindByID(id: int) -> ImGuiTable:
    ...
def TableFixColumnSortDirection(table: ImGuiTable, column: ImGuiTableColumn) -> None:
    ...
def TableGcCompactSettings() -> None:
    ...
@typing.overload
def TableGcCompactTransientBuffers(table: ImGuiTable) -> None:
    ...
@typing.overload
def TableGcCompactTransientBuffers(table: ImGuiTableTempData) -> None:
    ...
def TableGetBoundSettings(table: ImGuiTable) -> ImGuiTableSettings:
    ...
def TableGetCellBgRect(table: ImGuiTable, column_n: int) -> ImRect:
    ...
def TableGetColumnCount() -> int:
    ...
def TableGetColumnFlags(column_n: int = -1) -> int:
    ...
def TableGetColumnIndex() -> int:
    ...
@typing.overload
def TableGetColumnName(column_n: int = -1) -> str:
    ...
@typing.overload
def TableGetColumnName(table: ImGuiTable, column_n: int) -> str:
    ...
def TableGetColumnNextSortDirection(column: ImGuiTableColumn) -> ImGuiSortDirection:
    ...
def TableGetColumnResizeID(table: ImGuiTable, column_n: int, instance_no: int = 0) -> int:
    ...
def TableGetColumnWidthAuto(table: ImGuiTable, column: ImGuiTableColumn) -> float:
    ...
def TableGetHeaderAngledMaxLabelWidth() -> float:
    ...
def TableGetHeaderRowHeight() -> float:
    ...
def TableGetHoveredColumn() -> int:
    ...
def TableGetHoveredRow() -> int:
    ...
def TableGetInstanceData(table: ImGuiTable, instance_no: int) -> ImGuiTableInstanceData:
    ...
def TableGetInstanceID(table: ImGuiTable, instance_no: int) -> int:
    ...
def TableGetMaxColumnWidth(table: ImGuiTable, column_n: int) -> float:
    ...
def TableGetRowIndex() -> int:
    ...
def TableGetSortSpecs() -> ImGuiTableSortSpecs:
    ...
def TableHeader(label: str) -> None:
    ...
def TableHeadersRow() -> None:
    ...
def TableLoadSettings(table: ImGuiTable) -> None:
    ...
def TableMergeDrawChannels(table: ImGuiTable) -> None:
    ...
def TableNextColumn() -> bool:
    ...
def TableNextRow(row_flags: int = 0, min_row_height: float = 0.0) -> None:
    ...
def TableOpenContextMenu(column_n: int = -1) -> None:
    ...
def TablePopBackgroundChannel() -> None:
    ...
def TablePushBackgroundChannel() -> None:
    ...
def TableRemove(table: ImGuiTable) -> None:
    ...
def TableResetSettings(table: ImGuiTable) -> None:
    ...
def TableSaveSettings(table: ImGuiTable) -> None:
    ...
def TableSetBgColor(target: int, color: int, column_n: int = -1) -> None:
    ...
def TableSetColumnEnabled(column_n: int, v: bool) -> None:
    ...
def TableSetColumnIndex(column_n: int) -> bool:
    ...
def TableSetColumnSortDirection(column_n: int, sort_direction: ImGuiSortDirection, append_to_sort_specs: bool) -> None:
    ...
def TableSetColumnWidth(column_n: int, width: float) -> None:
    ...
def TableSetColumnWidthAutoAll(table: ImGuiTable) -> None:
    ...
def TableSetColumnWidthAutoSingle(table: ImGuiTable, column_n: int) -> None:
    ...
def TableSettingsAddSettingsHandler() -> None:
    ...
def TableSettingsCreate(id: int, columns_count: int) -> ImGuiTableSettings:
    ...
def TableSettingsFindByID(id: int) -> ImGuiTableSettings:
    ...
def TableSetupColumn(label: str, flags: int = 0, init_width_or_weight: float = 0.0, user_id: int = 0) -> None:
    ...
def TableSetupDrawChannels(table: ImGuiTable) -> None:
    ...
def TableSetupScrollFreeze(cols: int, rows: int) -> None:
    ...
def TableSortSpecsBuild(table: ImGuiTable) -> None:
    ...
def TableSortSpecsSanitize(table: ImGuiTable) -> None:
    ...
def TableUpdateBorders(table: ImGuiTable) -> None:
    ...
def TableUpdateColumnsWeightFromWidth(table: ImGuiTable) -> None:
    ...
def TableUpdateLayout(table: ImGuiTable) -> None:
    ...
def TeleportMousePos(pos: ImVec2) -> None:
    ...
def TempInputIsActive(id: int) -> bool:
    ...
def TempInputScalar(bb: ImRect, id: int, label: str, data_type: int, p_data: capsule, format: str, p_clamp_min: capsule = 0, p_clamp_max: capsule = 0) -> bool:
    ...
def TempInputText(bb: ImRect, id: int, label: str, buf: str, buf_size: int, flags: int) -> bool:
    ...
def TestKeyOwner(key: ImGuiKey, owner_id: int) -> bool:
    ...
def TestShortcutRouting(key_chord: int, owner_id: int) -> bool:
    ...
def Text(s: str = '') -> None:
    ...
def TextColored(col: ImVec4, s: str = '') -> None:
    ...
def TextDisabled(s: str = '') -> None:
    ...
def TextEx(text: str, text_end: str = 0, flags: int = 0) -> None:
    ...
def TextUnformatted(text: str, text_end: str = 0) -> None:
    ...
def TextWrapped(s: str = '') -> None:
    ...
def TranslateWindowsInViewport(viewport: ImGuiViewportP, old_pos: ImVec2, new_pos: ImVec2) -> None:
    ...
def TreeNode(label: str) -> bool:
    ...
def TreeNodeBehavior(id: int, flags: int, label: str, label_end: str = 0) -> bool:
    ...
def TreeNodeEx(label: str, flags: int = 0) -> bool:
    ...
def TreeNodeSetOpen(id: int, open: bool) -> None:
    ...
def TreeNodeUpdateNextOpen(id: int, flags: int) -> bool:
    ...
def TreePop() -> None:
    ...
@typing.overload
def TreePush(str_id: str) -> None:
    ...
@typing.overload
def TreePush(ptr_id: capsule) -> None:
    ...
def TreePushOverrideID(id: int) -> None:
    ...
def Unindent(indent_w: float = 0.0) -> None:
    ...
def UpdateHoveredWindowAndCaptureFlags() -> None:
    ...
def UpdateInputEvents(trickle_fast_inputs: bool) -> None:
    ...
def UpdateMouseMovingWindowEndFrame() -> None:
    ...
def UpdateMouseMovingWindowNewFrame() -> None:
    ...
def UpdatePlatformWindows() -> None:
    ...
def UpdateWindowParentAndRootLinks(window: ImGuiWindow, flags: int, parent_window: ImGuiWindow) -> None:
    ...
def UpdateWindowSkipRefresh(window: ImGuiWindow) -> None:
    ...
def VSliderFloat(label: str, size: ImVec2, v: float, v_min: float, v_max: float, format: str = '%.3f', flags: int = 0) -> bool:
    ...
def VSliderInt(label: str, size: ImVec2, v: int, v_min: int, v_max: int, format: str = '%d', flags: int = 0) -> bool:
    ...
def VSliderScalar(label: str, size: ImVec2, data_type: int, p_data: capsule, p_min: capsule, p_max: capsule, format: str = 0, flags: int = 0) -> bool:
    ...
@typing.overload
def Value(prefix: str, b: bool) -> None:
    ...
@typing.overload
def Value(prefix: str, v: int) -> None:
    ...
@typing.overload
def Value(prefix: str, v: int) -> None:
    ...
@typing.overload
def Value(prefix: str, v: float, float_format: str = 0) -> None:
    ...
def WindowPosRelToAbs(window: ImGuiWindow, p: ImVec2) -> ImVec2:
    ...
def WindowRectAbsToRel(window: ImGuiWindow, r: ImRect) -> ImRect:
    ...
def WindowRectRelToAbs(window: ImGuiWindow, r: ImRect) -> ImRect:
    ...
ImDrawFlags_Closed: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_Closed: 1>
ImDrawFlags_None: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_None: 0>
ImDrawFlags_RoundCornersAll: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersAll: 240>
ImDrawFlags_RoundCornersBottom: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersBottom: 192>
ImDrawFlags_RoundCornersBottomLeft: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersBottomLeft: 64>
ImDrawFlags_RoundCornersBottomRight: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersBottomRight: 128>
ImDrawFlags_RoundCornersDefault_: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersAll: 240>
ImDrawFlags_RoundCornersLeft: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersLeft: 80>
ImDrawFlags_RoundCornersMask_: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersMask_: 496>
ImDrawFlags_RoundCornersNone: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersNone: 256>
ImDrawFlags_RoundCornersRight: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersRight: 160>
ImDrawFlags_RoundCornersTop: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersTop: 48>
ImDrawFlags_RoundCornersTopLeft: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersTopLeft: 16>
ImDrawFlags_RoundCornersTopRight: ImDrawFlags_  # value = <ImDrawFlags_.ImDrawFlags_RoundCornersTopRight: 32>
ImDrawListFlags_AllowVtxOffset: ImDrawListFlags_  # value = <ImDrawListFlags_.ImDrawListFlags_AllowVtxOffset: 8>
ImDrawListFlags_AntiAliasedFill: ImDrawListFlags_  # value = <ImDrawListFlags_.ImDrawListFlags_AntiAliasedFill: 4>
ImDrawListFlags_AntiAliasedLines: ImDrawListFlags_  # value = <ImDrawListFlags_.ImDrawListFlags_AntiAliasedLines: 1>
ImDrawListFlags_AntiAliasedLinesUseTex: ImDrawListFlags_  # value = <ImDrawListFlags_.ImDrawListFlags_AntiAliasedLinesUseTex: 2>
ImDrawListFlags_None: ImDrawListFlags_  # value = <ImDrawListFlags_.ImDrawListFlags_None: 0>
ImFontAtlasFlags_NoBakedLines: ImFontAtlasFlags_  # value = <ImFontAtlasFlags_.ImFontAtlasFlags_NoBakedLines: 4>
ImFontAtlasFlags_NoMouseCursors: ImFontAtlasFlags_  # value = <ImFontAtlasFlags_.ImFontAtlasFlags_NoMouseCursors: 2>
ImFontAtlasFlags_NoPowerOfTwoHeight: ImFontAtlasFlags_  # value = <ImFontAtlasFlags_.ImFontAtlasFlags_NoPowerOfTwoHeight: 1>
ImFontAtlasFlags_None: ImFontAtlasFlags_  # value = <ImFontAtlasFlags_.ImFontAtlasFlags_None: 0>
ImGuiActivateFlags_FromShortcut: ImGuiActivateFlags_  # value = <ImGuiActivateFlags_.ImGuiActivateFlags_FromShortcut: 16>
ImGuiActivateFlags_FromTabbing: ImGuiActivateFlags_  # value = <ImGuiActivateFlags_.ImGuiActivateFlags_FromTabbing: 8>
ImGuiActivateFlags_None: ImGuiActivateFlags_  # value = <ImGuiActivateFlags_.ImGuiActivateFlags_None: 0>
ImGuiActivateFlags_PreferInput: ImGuiActivateFlags_  # value = <ImGuiActivateFlags_.ImGuiActivateFlags_PreferInput: 1>
ImGuiActivateFlags_PreferTweak: ImGuiActivateFlags_  # value = <ImGuiActivateFlags_.ImGuiActivateFlags_PreferTweak: 2>
ImGuiActivateFlags_TryToPreserveState: ImGuiActivateFlags_  # value = <ImGuiActivateFlags_.ImGuiActivateFlags_TryToPreserveState: 4>
ImGuiAxis_None: ImGuiAxis  # value = <ImGuiAxis.ImGuiAxis_None: -1>
ImGuiAxis_X: ImGuiAxis  # value = <ImGuiAxis.ImGuiAxis_X: 0>
ImGuiAxis_Y: ImGuiAxis  # value = <ImGuiAxis.ImGuiAxis_Y: 1>
ImGuiBackendFlags_HasGamepad: ImGuiBackendFlags_  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_HasGamepad: 1>
ImGuiBackendFlags_HasMouseCursors: ImGuiBackendFlags_  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_HasMouseCursors: 2>
ImGuiBackendFlags_HasMouseHoveredViewport: ImGuiBackendFlags_  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_HasMouseHoveredViewport: 2048>
ImGuiBackendFlags_HasSetMousePos: ImGuiBackendFlags_  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_HasSetMousePos: 4>
ImGuiBackendFlags_None: ImGuiBackendFlags_  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_None: 0>
ImGuiBackendFlags_PlatformHasViewports: ImGuiBackendFlags_  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_PlatformHasViewports: 1024>
ImGuiBackendFlags_RendererHasViewports: ImGuiBackendFlags_  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_RendererHasViewports: 4096>
ImGuiBackendFlags_RendererHasVtxOffset: ImGuiBackendFlags_  # value = <ImGuiBackendFlags_.ImGuiBackendFlags_RendererHasVtxOffset: 8>
ImGuiButtonFlags_AlignTextBaseLine: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_AlignTextBaseLine: 32768>
ImGuiButtonFlags_AllowOverlap: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_AllowOverlap: 4096>
ImGuiButtonFlags_DontClosePopups: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_DontClosePopups: 8192>
ImGuiButtonFlags_FlattenChildren: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_FlattenChildren: 2048>
ImGuiButtonFlags_MouseButtonLeft: ImGuiButtonFlags_  # value = <ImGuiButtonFlags_.ImGuiButtonFlags_MouseButtonLeft: 1>
ImGuiButtonFlags_MouseButtonMask_: ImGuiButtonFlags_  # value = <ImGuiButtonFlags_.ImGuiButtonFlags_MouseButtonMask_: 7>
ImGuiButtonFlags_MouseButtonMiddle: ImGuiButtonFlags_  # value = <ImGuiButtonFlags_.ImGuiButtonFlags_MouseButtonMiddle: 4>
ImGuiButtonFlags_MouseButtonRight: ImGuiButtonFlags_  # value = <ImGuiButtonFlags_.ImGuiButtonFlags_MouseButtonRight: 2>
ImGuiButtonFlags_NoHoldingActiveId: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoHoldingActiveId: 131072>
ImGuiButtonFlags_NoHoveredOnFocus: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoHoveredOnFocus: 524288>
ImGuiButtonFlags_NoKeyModifiers: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoKeyModifiers: 65536>
ImGuiButtonFlags_NoNavFocus: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoNavFocus: 262144>
ImGuiButtonFlags_NoSetKeyOwner: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoSetKeyOwner: 1048576>
ImGuiButtonFlags_NoTestKeyOwner: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_NoTestKeyOwner: 2097152>
ImGuiButtonFlags_None: ImGuiButtonFlags_  # value = <ImGuiButtonFlags_.ImGuiButtonFlags_None: 0>
ImGuiButtonFlags_PressedOnClick: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnClick: 16>
ImGuiButtonFlags_PressedOnClickRelease: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnClickRelease: 32>
ImGuiButtonFlags_PressedOnClickReleaseAnywhere: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnClickReleaseAnywhere: 64>
ImGuiButtonFlags_PressedOnDefault_: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnClickRelease: 32>
ImGuiButtonFlags_PressedOnDoubleClick: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnDoubleClick: 256>
ImGuiButtonFlags_PressedOnDragDropHold: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnDragDropHold: 512>
ImGuiButtonFlags_PressedOnMask_: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnMask_: 1008>
ImGuiButtonFlags_PressedOnRelease: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_PressedOnRelease: 128>
ImGuiButtonFlags_Repeat: ImGuiButtonFlagsPrivate_  # value = <ImGuiButtonFlagsPrivate_.ImGuiButtonFlags_Repeat: 1024>
ImGuiChildFlags_AlwaysAutoResize: ImGuiChildFlags_  # value = <ImGuiChildFlags_.ImGuiChildFlags_AlwaysAutoResize: 64>
ImGuiChildFlags_AlwaysUseWindowPadding: ImGuiChildFlags_  # value = <ImGuiChildFlags_.ImGuiChildFlags_AlwaysUseWindowPadding: 2>
ImGuiChildFlags_AutoResizeX: ImGuiChildFlags_  # value = <ImGuiChildFlags_.ImGuiChildFlags_AutoResizeX: 16>
ImGuiChildFlags_AutoResizeY: ImGuiChildFlags_  # value = <ImGuiChildFlags_.ImGuiChildFlags_AutoResizeY: 32>
ImGuiChildFlags_Border: ImGuiChildFlags_  # value = <ImGuiChildFlags_.ImGuiChildFlags_Border: 1>
ImGuiChildFlags_FrameStyle: ImGuiChildFlags_  # value = <ImGuiChildFlags_.ImGuiChildFlags_FrameStyle: 128>
ImGuiChildFlags_NavFlattened: ImGuiChildFlags_  # value = <ImGuiChildFlags_.ImGuiChildFlags_NavFlattened: 256>
ImGuiChildFlags_None: ImGuiChildFlags_  # value = <ImGuiChildFlags_.ImGuiChildFlags_None: 0>
ImGuiChildFlags_ResizeX: ImGuiChildFlags_  # value = <ImGuiChildFlags_.ImGuiChildFlags_ResizeX: 4>
ImGuiChildFlags_ResizeY: ImGuiChildFlags_  # value = <ImGuiChildFlags_.ImGuiChildFlags_ResizeY: 8>
ImGuiCol_Border: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_Border: 5>
ImGuiCol_BorderShadow: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_BorderShadow: 6>
ImGuiCol_Button: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_Button: 21>
ImGuiCol_ButtonActive: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_ButtonActive: 23>
ImGuiCol_ButtonHovered: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_ButtonHovered: 22>
ImGuiCol_COUNT: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_COUNT: 57>
ImGuiCol_CheckMark: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_CheckMark: 18>
ImGuiCol_ChildBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_ChildBg: 3>
ImGuiCol_DockingEmptyBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_DockingEmptyBg: 41>
ImGuiCol_DockingPreview: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_DockingPreview: 40>
ImGuiCol_DragDropTarget: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_DragDropTarget: 52>
ImGuiCol_FrameBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_FrameBg: 7>
ImGuiCol_FrameBgActive: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_FrameBgActive: 9>
ImGuiCol_FrameBgHovered: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_FrameBgHovered: 8>
ImGuiCol_Header: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_Header: 24>
ImGuiCol_HeaderActive: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_HeaderActive: 26>
ImGuiCol_HeaderHovered: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_HeaderHovered: 25>
ImGuiCol_MenuBarBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_MenuBarBg: 13>
ImGuiCol_ModalWindowDimBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_ModalWindowDimBg: 56>
ImGuiCol_NavHighlight: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_NavHighlight: 53>
ImGuiCol_NavWindowingDimBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_NavWindowingDimBg: 55>
ImGuiCol_NavWindowingHighlight: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_NavWindowingHighlight: 54>
ImGuiCol_PlotHistogram: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_PlotHistogram: 44>
ImGuiCol_PlotHistogramHovered: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_PlotHistogramHovered: 45>
ImGuiCol_PlotLines: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_PlotLines: 42>
ImGuiCol_PlotLinesHovered: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_PlotLinesHovered: 43>
ImGuiCol_PopupBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_PopupBg: 4>
ImGuiCol_ResizeGrip: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_ResizeGrip: 30>
ImGuiCol_ResizeGripActive: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_ResizeGripActive: 32>
ImGuiCol_ResizeGripHovered: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_ResizeGripHovered: 31>
ImGuiCol_ScrollbarBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_ScrollbarBg: 14>
ImGuiCol_ScrollbarGrab: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_ScrollbarGrab: 15>
ImGuiCol_ScrollbarGrabActive: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_ScrollbarGrabActive: 17>
ImGuiCol_ScrollbarGrabHovered: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_ScrollbarGrabHovered: 16>
ImGuiCol_Separator: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_Separator: 27>
ImGuiCol_SeparatorActive: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_SeparatorActive: 29>
ImGuiCol_SeparatorHovered: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_SeparatorHovered: 28>
ImGuiCol_SliderGrab: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_SliderGrab: 19>
ImGuiCol_SliderGrabActive: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_SliderGrabActive: 20>
ImGuiCol_Tab: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_Tab: 34>
ImGuiCol_TabDimmed: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TabDimmed: 37>
ImGuiCol_TabDimmedSelected: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TabDimmedSelected: 38>
ImGuiCol_TabDimmedSelectedOverline: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TabDimmedSelectedOverline: 39>
ImGuiCol_TabHovered: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TabHovered: 33>
ImGuiCol_TabSelected: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TabSelected: 35>
ImGuiCol_TabSelectedOverline: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TabSelectedOverline: 36>
ImGuiCol_TableBorderLight: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TableBorderLight: 48>
ImGuiCol_TableBorderStrong: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TableBorderStrong: 47>
ImGuiCol_TableHeaderBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TableHeaderBg: 46>
ImGuiCol_TableRowBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TableRowBg: 49>
ImGuiCol_TableRowBgAlt: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TableRowBgAlt: 50>
ImGuiCol_Text: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_Text: 0>
ImGuiCol_TextDisabled: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TextDisabled: 1>
ImGuiCol_TextSelectedBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TextSelectedBg: 51>
ImGuiCol_TitleBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TitleBg: 10>
ImGuiCol_TitleBgActive: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TitleBgActive: 11>
ImGuiCol_TitleBgCollapsed: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_TitleBgCollapsed: 12>
ImGuiCol_WindowBg: ImGuiCol_  # value = <ImGuiCol_.ImGuiCol_WindowBg: 2>
ImGuiColorEditFlags_AlphaBar: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_AlphaBar: 65536>
ImGuiColorEditFlags_AlphaPreview: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_AlphaPreview: 131072>
ImGuiColorEditFlags_AlphaPreviewHalf: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_AlphaPreviewHalf: 262144>
ImGuiColorEditFlags_DataTypeMask_: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_DataTypeMask_: 25165824>
ImGuiColorEditFlags_DefaultOptions_: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_DefaultOptions_: 177209344>
ImGuiColorEditFlags_DisplayHSV: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_DisplayHSV: 2097152>
ImGuiColorEditFlags_DisplayHex: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_DisplayHex: 4194304>
ImGuiColorEditFlags_DisplayMask_: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_DisplayMask_: 7340032>
ImGuiColorEditFlags_DisplayRGB: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_DisplayRGB: 1048576>
ImGuiColorEditFlags_Float: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_Float: 16777216>
ImGuiColorEditFlags_HDR: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_HDR: 524288>
ImGuiColorEditFlags_InputHSV: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_InputHSV: 268435456>
ImGuiColorEditFlags_InputMask_: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_InputMask_: 402653184>
ImGuiColorEditFlags_InputRGB: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_InputRGB: 134217728>
ImGuiColorEditFlags_NoAlpha: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoAlpha: 2>
ImGuiColorEditFlags_NoBorder: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoBorder: 1024>
ImGuiColorEditFlags_NoDragDrop: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoDragDrop: 512>
ImGuiColorEditFlags_NoInputs: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoInputs: 32>
ImGuiColorEditFlags_NoLabel: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoLabel: 128>
ImGuiColorEditFlags_NoOptions: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoOptions: 8>
ImGuiColorEditFlags_NoPicker: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoPicker: 4>
ImGuiColorEditFlags_NoSidePreview: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoSidePreview: 256>
ImGuiColorEditFlags_NoSmallPreview: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoSmallPreview: 16>
ImGuiColorEditFlags_NoTooltip: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_NoTooltip: 64>
ImGuiColorEditFlags_None: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_None: 0>
ImGuiColorEditFlags_PickerHueBar: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_PickerHueBar: 33554432>
ImGuiColorEditFlags_PickerHueWheel: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_PickerHueWheel: 67108864>
ImGuiColorEditFlags_PickerMask_: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_PickerMask_: 100663296>
ImGuiColorEditFlags_Uint8: ImGuiColorEditFlags_  # value = <ImGuiColorEditFlags_.ImGuiColorEditFlags_Uint8: 8388608>
ImGuiComboFlags_CustomPreview: ImGuiComboFlagsPrivate_  # value = <ImGuiComboFlagsPrivate_.ImGuiComboFlags_CustomPreview: 1048576>
ImGuiComboFlags_HeightLarge: ImGuiComboFlags_  # value = <ImGuiComboFlags_.ImGuiComboFlags_HeightLarge: 8>
ImGuiComboFlags_HeightLargest: ImGuiComboFlags_  # value = <ImGuiComboFlags_.ImGuiComboFlags_HeightLargest: 16>
ImGuiComboFlags_HeightMask_: ImGuiComboFlags_  # value = <ImGuiComboFlags_.ImGuiComboFlags_HeightMask_: 30>
ImGuiComboFlags_HeightRegular: ImGuiComboFlags_  # value = <ImGuiComboFlags_.ImGuiComboFlags_HeightRegular: 4>
ImGuiComboFlags_HeightSmall: ImGuiComboFlags_  # value = <ImGuiComboFlags_.ImGuiComboFlags_HeightSmall: 2>
ImGuiComboFlags_NoArrowButton: ImGuiComboFlags_  # value = <ImGuiComboFlags_.ImGuiComboFlags_NoArrowButton: 32>
ImGuiComboFlags_NoPreview: ImGuiComboFlags_  # value = <ImGuiComboFlags_.ImGuiComboFlags_NoPreview: 64>
ImGuiComboFlags_None: ImGuiComboFlags_  # value = <ImGuiComboFlags_.ImGuiComboFlags_None: 0>
ImGuiComboFlags_PopupAlignLeft: ImGuiComboFlags_  # value = <ImGuiComboFlags_.ImGuiComboFlags_PopupAlignLeft: 1>
ImGuiComboFlags_WidthFitPreview: ImGuiComboFlags_  # value = <ImGuiComboFlags_.ImGuiComboFlags_WidthFitPreview: 128>
ImGuiCond_Always: ImGuiCond_  # value = <ImGuiCond_.ImGuiCond_Always: 1>
ImGuiCond_Appearing: ImGuiCond_  # value = <ImGuiCond_.ImGuiCond_Appearing: 8>
ImGuiCond_FirstUseEver: ImGuiCond_  # value = <ImGuiCond_.ImGuiCond_FirstUseEver: 4>
ImGuiCond_None: ImGuiCond_  # value = <ImGuiCond_.ImGuiCond_None: 0>
ImGuiCond_Once: ImGuiCond_  # value = <ImGuiCond_.ImGuiCond_Once: 2>
ImGuiConfigFlags_DockingEnable: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_DockingEnable: 128>
ImGuiConfigFlags_DpiEnableScaleFonts: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_DpiEnableScaleFonts: 32768>
ImGuiConfigFlags_DpiEnableScaleViewports: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_DpiEnableScaleViewports: 16384>
ImGuiConfigFlags_IsSRGB: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_IsSRGB: 1048576>
ImGuiConfigFlags_IsTouchScreen: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_IsTouchScreen: 2097152>
ImGuiConfigFlags_NavEnableGamepad: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NavEnableGamepad: 2>
ImGuiConfigFlags_NavEnableKeyboard: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NavEnableKeyboard: 1>
ImGuiConfigFlags_NavEnableSetMousePos: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NavEnableSetMousePos: 4>
ImGuiConfigFlags_NavNoCaptureKeyboard: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NavNoCaptureKeyboard: 8>
ImGuiConfigFlags_NoKeyboard: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NoKeyboard: 64>
ImGuiConfigFlags_NoMouse: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NoMouse: 16>
ImGuiConfigFlags_NoMouseCursorChange: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_NoMouseCursorChange: 32>
ImGuiConfigFlags_None: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_None: 0>
ImGuiConfigFlags_ViewportsEnable: ImGuiConfigFlags_  # value = <ImGuiConfigFlags_.ImGuiConfigFlags_ViewportsEnable: 1024>
ImGuiContextHookType_EndFramePost: ImGuiContextHookType  # value = <ImGuiContextHookType.ImGuiContextHookType_EndFramePost: 3>
ImGuiContextHookType_EndFramePre: ImGuiContextHookType  # value = <ImGuiContextHookType.ImGuiContextHookType_EndFramePre: 2>
ImGuiContextHookType_NewFramePost: ImGuiContextHookType  # value = <ImGuiContextHookType.ImGuiContextHookType_NewFramePost: 1>
ImGuiContextHookType_NewFramePre: ImGuiContextHookType  # value = <ImGuiContextHookType.ImGuiContextHookType_NewFramePre: 0>
ImGuiContextHookType_PendingRemoval_: ImGuiContextHookType  # value = <ImGuiContextHookType.ImGuiContextHookType_PendingRemoval_: 7>
ImGuiContextHookType_RenderPost: ImGuiContextHookType  # value = <ImGuiContextHookType.ImGuiContextHookType_RenderPost: 5>
ImGuiContextHookType_RenderPre: ImGuiContextHookType  # value = <ImGuiContextHookType.ImGuiContextHookType_RenderPre: 4>
ImGuiContextHookType_Shutdown: ImGuiContextHookType  # value = <ImGuiContextHookType.ImGuiContextHookType_Shutdown: 6>
ImGuiDataAuthority_Auto: ImGuiDataAuthority_  # value = <ImGuiDataAuthority_.ImGuiDataAuthority_Auto: 0>
ImGuiDataAuthority_DockNode: ImGuiDataAuthority_  # value = <ImGuiDataAuthority_.ImGuiDataAuthority_DockNode: 1>
ImGuiDataAuthority_Window: ImGuiDataAuthority_  # value = <ImGuiDataAuthority_.ImGuiDataAuthority_Window: 2>
ImGuiDataType_COUNT: ImGuiDataType_  # value = <ImGuiDataType_.ImGuiDataType_COUNT: 10>
ImGuiDataType_Double: ImGuiDataType_  # value = <ImGuiDataType_.ImGuiDataType_Double: 9>
ImGuiDataType_Float: ImGuiDataType_  # value = <ImGuiDataType_.ImGuiDataType_Float: 8>
ImGuiDataType_ID: ImGuiDataTypePrivate_  # value = <ImGuiDataTypePrivate_.ImGuiDataType_ID: 13>
ImGuiDataType_Pointer: ImGuiDataTypePrivate_  # value = <ImGuiDataTypePrivate_.ImGuiDataType_Pointer: 12>
ImGuiDataType_S16: ImGuiDataType_  # value = <ImGuiDataType_.ImGuiDataType_S16: 2>
ImGuiDataType_S32: ImGuiDataType_  # value = <ImGuiDataType_.ImGuiDataType_S32: 4>
ImGuiDataType_S64: ImGuiDataType_  # value = <ImGuiDataType_.ImGuiDataType_S64: 6>
ImGuiDataType_S8: ImGuiDataType_  # value = <ImGuiDataType_.ImGuiDataType_S8: 0>
ImGuiDataType_String: ImGuiDataTypePrivate_  # value = <ImGuiDataTypePrivate_.ImGuiDataType_String: 11>
ImGuiDataType_U16: ImGuiDataType_  # value = <ImGuiDataType_.ImGuiDataType_U16: 3>
ImGuiDataType_U32: ImGuiDataType_  # value = <ImGuiDataType_.ImGuiDataType_U32: 5>
ImGuiDataType_U64: ImGuiDataType_  # value = <ImGuiDataType_.ImGuiDataType_U64: 7>
ImGuiDataType_U8: ImGuiDataType_  # value = <ImGuiDataType_.ImGuiDataType_U8: 1>
ImGuiDebugLogFlags_EventActiveId: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventActiveId: 1>
ImGuiDebugLogFlags_EventClipper: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventClipper: 16>
ImGuiDebugLogFlags_EventDocking: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventDocking: 256>
ImGuiDebugLogFlags_EventFocus: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventFocus: 2>
ImGuiDebugLogFlags_EventIO: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventIO: 64>
ImGuiDebugLogFlags_EventInputRouting: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventInputRouting: 128>
ImGuiDebugLogFlags_EventMask_: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventMask_: 1023>
ImGuiDebugLogFlags_EventNav: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventNav: 8>
ImGuiDebugLogFlags_EventPopup: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventPopup: 4>
ImGuiDebugLogFlags_EventSelection: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventSelection: 32>
ImGuiDebugLogFlags_EventViewport: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_EventViewport: 512>
ImGuiDebugLogFlags_None: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_None: 0>
ImGuiDebugLogFlags_OutputToTTY: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_OutputToTTY: 1048576>
ImGuiDebugLogFlags_OutputToTestEngine: ImGuiDebugLogFlags_  # value = <ImGuiDebugLogFlags_.ImGuiDebugLogFlags_OutputToTestEngine: 2097152>
ImGuiDir_COUNT: ImGuiDir  # value = <ImGuiDir.ImGuiDir_COUNT: 4>
ImGuiDir_Down: ImGuiDir  # value = <ImGuiDir.ImGuiDir_Down: 3>
ImGuiDir_Left: ImGuiDir  # value = <ImGuiDir.ImGuiDir_Left: 0>
ImGuiDir_None: ImGuiDir  # value = <ImGuiDir.ImGuiDir_None: -1>
ImGuiDir_Right: ImGuiDir  # value = <ImGuiDir.ImGuiDir_Right: 1>
ImGuiDir_Up: ImGuiDir  # value = <ImGuiDir.ImGuiDir_Up: 2>
ImGuiDockNodeFlags_AutoHideTabBar: ImGuiDockNodeFlags_  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_AutoHideTabBar: 64>
ImGuiDockNodeFlags_CentralNode: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_CentralNode: 2048>
ImGuiDockNodeFlags_DockSpace: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_DockSpace: 1024>
ImGuiDockNodeFlags_DockedWindowsInFocusRoute: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_DockedWindowsInFocusRoute: 262144>
ImGuiDockNodeFlags_HiddenTabBar: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_HiddenTabBar: 8192>
ImGuiDockNodeFlags_KeepAliveOnly: ImGuiDockNodeFlags_  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_KeepAliveOnly: 1>
ImGuiDockNodeFlags_LocalFlagsTransferMask_: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_LocalFlagsTransferMask_: 260208>
ImGuiDockNodeFlags_NoCloseButton: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoCloseButton: 32768>
ImGuiDockNodeFlags_NoDocking: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDocking: 7864336>
ImGuiDockNodeFlags_NoDockingOverCentralNode: ImGuiDockNodeFlags_  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_NoDockingOverCentralNode: 4>
ImGuiDockNodeFlags_NoDockingOverEmpty: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDockingOverEmpty: 4194304>
ImGuiDockNodeFlags_NoDockingOverMe: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDockingOverMe: 1048576>
ImGuiDockNodeFlags_NoDockingOverOther: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDockingOverOther: 2097152>
ImGuiDockNodeFlags_NoDockingSplit: ImGuiDockNodeFlags_  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_NoDockingSplit: 16>
ImGuiDockNodeFlags_NoDockingSplitOther: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoDockingSplitOther: 524288>
ImGuiDockNodeFlags_NoResize: ImGuiDockNodeFlags_  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_NoResize: 32>
ImGuiDockNodeFlags_NoResizeFlagsMask_: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoResizeFlagsMask_: 196640>
ImGuiDockNodeFlags_NoResizeX: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoResizeX: 65536>
ImGuiDockNodeFlags_NoResizeY: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoResizeY: 131072>
ImGuiDockNodeFlags_NoTabBar: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoTabBar: 4096>
ImGuiDockNodeFlags_NoUndocking: ImGuiDockNodeFlags_  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_NoUndocking: 128>
ImGuiDockNodeFlags_NoWindowMenuButton: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_NoWindowMenuButton: 16384>
ImGuiDockNodeFlags_None: ImGuiDockNodeFlags_  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_None: 0>
ImGuiDockNodeFlags_PassthruCentralNode: ImGuiDockNodeFlags_  # value = <ImGuiDockNodeFlags_.ImGuiDockNodeFlags_PassthruCentralNode: 8>
ImGuiDockNodeFlags_SavedFlagsMask_: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_SavedFlagsMask_: 261152>
ImGuiDockNodeFlags_SharedFlagsInheritMask_: ImGuiDockNodeFlagsPrivate_  # value = <ImGuiDockNodeFlagsPrivate_.ImGuiDockNodeFlags_SharedFlagsInheritMask_: -1>
ImGuiDockNodeState_HostWindowHiddenBecauseSingleWindow: ImGuiDockNodeState  # value = <ImGuiDockNodeState.ImGuiDockNodeState_HostWindowHiddenBecauseSingleWindow: 1>
ImGuiDockNodeState_HostWindowHiddenBecauseWindowsAreResizing: ImGuiDockNodeState  # value = <ImGuiDockNodeState.ImGuiDockNodeState_HostWindowHiddenBecauseWindowsAreResizing: 2>
ImGuiDockNodeState_HostWindowVisible: ImGuiDockNodeState  # value = <ImGuiDockNodeState.ImGuiDockNodeState_HostWindowVisible: 3>
ImGuiDockNodeState_Unknown: ImGuiDockNodeState  # value = <ImGuiDockNodeState.ImGuiDockNodeState_Unknown: 0>
ImGuiDragDropFlags_AcceptBeforeDelivery: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_AcceptBeforeDelivery: 1024>
ImGuiDragDropFlags_AcceptNoDrawDefaultRect: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_AcceptNoDrawDefaultRect: 2048>
ImGuiDragDropFlags_AcceptNoPreviewTooltip: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_AcceptNoPreviewTooltip: 4096>
ImGuiDragDropFlags_AcceptPeekOnly: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_AcceptPeekOnly: 3072>
ImGuiDragDropFlags_None: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_None: 0>
ImGuiDragDropFlags_PayloadAutoExpire: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_PayloadAutoExpire: 32>
ImGuiDragDropFlags_PayloadNoCrossContext: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_PayloadNoCrossContext: 64>
ImGuiDragDropFlags_PayloadNoCrossProcess: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_PayloadNoCrossProcess: 128>
ImGuiDragDropFlags_SourceAllowNullID: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceAllowNullID: 8>
ImGuiDragDropFlags_SourceExtern: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceExtern: 16>
ImGuiDragDropFlags_SourceNoDisableHover: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceNoDisableHover: 2>
ImGuiDragDropFlags_SourceNoHoldToOpenOthers: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceNoHoldToOpenOthers: 4>
ImGuiDragDropFlags_SourceNoPreviewTooltip: ImGuiDragDropFlags_  # value = <ImGuiDragDropFlags_.ImGuiDragDropFlags_SourceNoPreviewTooltip: 1>
ImGuiFocusRequestFlags_None: ImGuiFocusRequestFlags_  # value = <ImGuiFocusRequestFlags_.ImGuiFocusRequestFlags_None: 0>
ImGuiFocusRequestFlags_RestoreFocusedChild: ImGuiFocusRequestFlags_  # value = <ImGuiFocusRequestFlags_.ImGuiFocusRequestFlags_RestoreFocusedChild: 1>
ImGuiFocusRequestFlags_UnlessBelowModal: ImGuiFocusRequestFlags_  # value = <ImGuiFocusRequestFlags_.ImGuiFocusRequestFlags_UnlessBelowModal: 2>
ImGuiFocusedFlags_AnyWindow: ImGuiFocusedFlags_  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_AnyWindow: 4>
ImGuiFocusedFlags_ChildWindows: ImGuiFocusedFlags_  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_ChildWindows: 1>
ImGuiFocusedFlags_DockHierarchy: ImGuiFocusedFlags_  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_DockHierarchy: 16>
ImGuiFocusedFlags_NoPopupHierarchy: ImGuiFocusedFlags_  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_NoPopupHierarchy: 8>
ImGuiFocusedFlags_None: ImGuiFocusedFlags_  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_None: 0>
ImGuiFocusedFlags_RootAndChildWindows: ImGuiFocusedFlags_  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_RootAndChildWindows: 3>
ImGuiFocusedFlags_RootWindow: ImGuiFocusedFlags_  # value = <ImGuiFocusedFlags_.ImGuiFocusedFlags_RootWindow: 2>
ImGuiHoveredFlags_AllowWhenBlockedByActiveItem: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenBlockedByActiveItem: 128>
ImGuiHoveredFlags_AllowWhenBlockedByPopup: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenBlockedByPopup: 32>
ImGuiHoveredFlags_AllowWhenDisabled: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenDisabled: 1024>
ImGuiHoveredFlags_AllowWhenOverlapped: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenOverlapped: 768>
ImGuiHoveredFlags_AllowWhenOverlappedByItem: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenOverlappedByItem: 256>
ImGuiHoveredFlags_AllowWhenOverlappedByWindow: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AllowWhenOverlappedByWindow: 512>
ImGuiHoveredFlags_AllowedMaskForIsItemHovered: ImGuiHoveredFlagsPrivate_  # value = <ImGuiHoveredFlagsPrivate_.ImGuiHoveredFlags_AllowedMaskForIsItemHovered: 262048>
ImGuiHoveredFlags_AllowedMaskForIsWindowHovered: ImGuiHoveredFlagsPrivate_  # value = <ImGuiHoveredFlagsPrivate_.ImGuiHoveredFlags_AllowedMaskForIsWindowHovered: 12479>
ImGuiHoveredFlags_AnyWindow: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_AnyWindow: 4>
ImGuiHoveredFlags_ChildWindows: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_ChildWindows: 1>
ImGuiHoveredFlags_DelayMask_: ImGuiHoveredFlagsPrivate_  # value = <ImGuiHoveredFlagsPrivate_.ImGuiHoveredFlags_DelayMask_: 245760>
ImGuiHoveredFlags_DelayNone: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_DelayNone: 16384>
ImGuiHoveredFlags_DelayNormal: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_DelayNormal: 65536>
ImGuiHoveredFlags_DelayShort: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_DelayShort: 32768>
ImGuiHoveredFlags_DockHierarchy: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_DockHierarchy: 16>
ImGuiHoveredFlags_ForTooltip: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_ForTooltip: 4096>
ImGuiHoveredFlags_NoNavOverride: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_NoNavOverride: 2048>
ImGuiHoveredFlags_NoPopupHierarchy: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_NoPopupHierarchy: 8>
ImGuiHoveredFlags_NoSharedDelay: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_NoSharedDelay: 131072>
ImGuiHoveredFlags_None: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_None: 0>
ImGuiHoveredFlags_RectOnly: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_RectOnly: 928>
ImGuiHoveredFlags_RootAndChildWindows: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_RootAndChildWindows: 3>
ImGuiHoveredFlags_RootWindow: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_RootWindow: 2>
ImGuiHoveredFlags_Stationary: ImGuiHoveredFlags_  # value = <ImGuiHoveredFlags_.ImGuiHoveredFlags_Stationary: 8192>
ImGuiInputEventType_COUNT: ImGuiInputEventType  # value = <ImGuiInputEventType.ImGuiInputEventType_COUNT: 8>
ImGuiInputEventType_Focus: ImGuiInputEventType  # value = <ImGuiInputEventType.ImGuiInputEventType_Focus: 7>
ImGuiInputEventType_Key: ImGuiInputEventType  # value = <ImGuiInputEventType.ImGuiInputEventType_Key: 5>
ImGuiInputEventType_MouseButton: ImGuiInputEventType  # value = <ImGuiInputEventType.ImGuiInputEventType_MouseButton: 3>
ImGuiInputEventType_MousePos: ImGuiInputEventType  # value = <ImGuiInputEventType.ImGuiInputEventType_MousePos: 1>
ImGuiInputEventType_MouseViewport: ImGuiInputEventType  # value = <ImGuiInputEventType.ImGuiInputEventType_MouseViewport: 4>
ImGuiInputEventType_MouseWheel: ImGuiInputEventType  # value = <ImGuiInputEventType.ImGuiInputEventType_MouseWheel: 2>
ImGuiInputEventType_None: ImGuiInputEventType  # value = <ImGuiInputEventType.ImGuiInputEventType_None: 0>
ImGuiInputEventType_Text: ImGuiInputEventType  # value = <ImGuiInputEventType.ImGuiInputEventType_Text: 6>
ImGuiInputFlags_CondActive: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_CondActive: 8388608>
ImGuiInputFlags_CondDefault_: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_CondDefault_: 12582912>
ImGuiInputFlags_CondHovered: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_CondHovered: 4194304>
ImGuiInputFlags_CondMask_: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_CondDefault_: 12582912>
ImGuiInputFlags_LockThisFrame: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_LockThisFrame: 1048576>
ImGuiInputFlags_LockUntilRelease: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_LockUntilRelease: 2097152>
ImGuiInputFlags_None: ImGuiInputFlags_  # value = <ImGuiInputFlags_.ImGuiInputFlags_None: 0>
ImGuiInputFlags_Repeat: ImGuiInputFlags_  # value = <ImGuiInputFlags_.ImGuiInputFlags_Repeat: 1>
ImGuiInputFlags_RepeatMask_: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatMask_: 255>
ImGuiInputFlags_RepeatRateDefault: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatRateDefault: 2>
ImGuiInputFlags_RepeatRateMask_: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatRateMask_: 14>
ImGuiInputFlags_RepeatRateNavMove: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatRateNavMove: 4>
ImGuiInputFlags_RepeatRateNavTweak: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatRateNavTweak: 8>
ImGuiInputFlags_RepeatUntilKeyModsChange: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilKeyModsChange: 32>
ImGuiInputFlags_RepeatUntilKeyModsChangeFromNone: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilKeyModsChangeFromNone: 64>
ImGuiInputFlags_RepeatUntilMask_: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilMask_: 240>
ImGuiInputFlags_RepeatUntilOtherKeyPress: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilOtherKeyPress: 128>
ImGuiInputFlags_RepeatUntilRelease: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatUntilRelease: 16>
ImGuiInputFlags_RouteActive: ImGuiInputFlags_  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteActive: 1024>
ImGuiInputFlags_RouteAlways: ImGuiInputFlags_  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteAlways: 8192>
ImGuiInputFlags_RouteFocused: ImGuiInputFlags_  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteFocused: 2048>
ImGuiInputFlags_RouteFromRootWindow: ImGuiInputFlags_  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteFromRootWindow: 131072>
ImGuiInputFlags_RouteGlobal: ImGuiInputFlags_  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteGlobal: 4096>
ImGuiInputFlags_RouteOptionsMask_: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RouteOptionsMask_: 245760>
ImGuiInputFlags_RouteOverActive: ImGuiInputFlags_  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteOverActive: 32768>
ImGuiInputFlags_RouteOverFocused: ImGuiInputFlags_  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteOverFocused: 16384>
ImGuiInputFlags_RouteTypeMask_: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RouteTypeMask_: 15360>
ImGuiInputFlags_RouteUnlessBgFocused: ImGuiInputFlags_  # value = <ImGuiInputFlags_.ImGuiInputFlags_RouteUnlessBgFocused: 65536>
ImGuiInputFlags_SupportedByIsKeyPressed: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_RepeatMask_: 255>
ImGuiInputFlags_SupportedByIsMouseClicked: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedByIsMouseClicked: 1>
ImGuiInputFlags_SupportedBySetItemKeyOwner: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedBySetItemKeyOwner: 15728640>
ImGuiInputFlags_SupportedBySetKeyOwner: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedBySetKeyOwner: 3145728>
ImGuiInputFlags_SupportedBySetNextItemShortcut: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedBySetNextItemShortcut: 523519>
ImGuiInputFlags_SupportedByShortcut: ImGuiInputFlagsPrivate_  # value = <ImGuiInputFlagsPrivate_.ImGuiInputFlags_SupportedByShortcut: 261375>
ImGuiInputFlags_Tooltip: ImGuiInputFlags_  # value = <ImGuiInputFlags_.ImGuiInputFlags_Tooltip: 262144>
ImGuiInputSource_COUNT: ImGuiInputSource  # value = <ImGuiInputSource.ImGuiInputSource_COUNT: 4>
ImGuiInputSource_Gamepad: ImGuiInputSource  # value = <ImGuiInputSource.ImGuiInputSource_Gamepad: 3>
ImGuiInputSource_Keyboard: ImGuiInputSource  # value = <ImGuiInputSource.ImGuiInputSource_Keyboard: 2>
ImGuiInputSource_Mouse: ImGuiInputSource  # value = <ImGuiInputSource.ImGuiInputSource_Mouse: 1>
ImGuiInputSource_None: ImGuiInputSource  # value = <ImGuiInputSource.ImGuiInputSource_None: 0>
ImGuiInputTextFlags_AllowTabInput: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_AllowTabInput: 32>
ImGuiInputTextFlags_AlwaysOverwrite: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_AlwaysOverwrite: 2048>
ImGuiInputTextFlags_AutoSelectAll: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_AutoSelectAll: 4096>
ImGuiInputTextFlags_CallbackAlways: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackAlways: 524288>
ImGuiInputTextFlags_CallbackCharFilter: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackCharFilter: 1048576>
ImGuiInputTextFlags_CallbackCompletion: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackCompletion: 131072>
ImGuiInputTextFlags_CallbackEdit: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackEdit: 4194304>
ImGuiInputTextFlags_CallbackHistory: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackHistory: 262144>
ImGuiInputTextFlags_CallbackResize: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CallbackResize: 2097152>
ImGuiInputTextFlags_CharsDecimal: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsDecimal: 1>
ImGuiInputTextFlags_CharsHexadecimal: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsHexadecimal: 2>
ImGuiInputTextFlags_CharsNoBlank: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsNoBlank: 16>
ImGuiInputTextFlags_CharsScientific: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsScientific: 4>
ImGuiInputTextFlags_CharsUppercase: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CharsUppercase: 8>
ImGuiInputTextFlags_CtrlEnterForNewLine: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_CtrlEnterForNewLine: 256>
ImGuiInputTextFlags_DisplayEmptyRefVal: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_DisplayEmptyRefVal: 16384>
ImGuiInputTextFlags_EnterReturnsTrue: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_EnterReturnsTrue: 64>
ImGuiInputTextFlags_EscapeClearsAll: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_EscapeClearsAll: 128>
ImGuiInputTextFlags_LocalizeDecimalPoint: ImGuiInputTextFlagsPrivate_  # value = <ImGuiInputTextFlagsPrivate_.ImGuiInputTextFlags_LocalizeDecimalPoint: 536870912>
ImGuiInputTextFlags_MergedItem: ImGuiInputTextFlagsPrivate_  # value = <ImGuiInputTextFlagsPrivate_.ImGuiInputTextFlags_MergedItem: 268435456>
ImGuiInputTextFlags_Multiline: ImGuiInputTextFlagsPrivate_  # value = <ImGuiInputTextFlagsPrivate_.ImGuiInputTextFlags_Multiline: 67108864>
ImGuiInputTextFlags_NoHorizontalScroll: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_NoHorizontalScroll: 32768>
ImGuiInputTextFlags_NoMarkEdited: ImGuiInputTextFlagsPrivate_  # value = <ImGuiInputTextFlagsPrivate_.ImGuiInputTextFlags_NoMarkEdited: 134217728>
ImGuiInputTextFlags_NoUndoRedo: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_NoUndoRedo: 65536>
ImGuiInputTextFlags_None: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_None: 0>
ImGuiInputTextFlags_ParseEmptyRefVal: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_ParseEmptyRefVal: 8192>
ImGuiInputTextFlags_Password: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_Password: 1024>
ImGuiInputTextFlags_ReadOnly: ImGuiInputTextFlags_  # value = <ImGuiInputTextFlags_.ImGuiInputTextFlags_ReadOnly: 512>
ImGuiItemFlags_AllowOverlap: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_AllowOverlap: 512>
ImGuiItemFlags_ButtonRepeat: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_ButtonRepeat: 2>
ImGuiItemFlags_Disabled: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_Disabled: 4>
ImGuiItemFlags_HasSelectionUserData: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_HasSelectionUserData: 2048>
ImGuiItemFlags_Inputable: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_Inputable: 1024>
ImGuiItemFlags_MixedValue: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_MixedValue: 64>
ImGuiItemFlags_NoNav: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_NoNav: 8>
ImGuiItemFlags_NoNavDefaultFocus: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_NoNavDefaultFocus: 16>
ImGuiItemFlags_NoTabStop: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_NoTabStop: 1>
ImGuiItemFlags_NoWindowHoverableCheck: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_NoWindowHoverableCheck: 256>
ImGuiItemFlags_None: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_None: 0>
ImGuiItemFlags_ReadOnly: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_ReadOnly: 128>
ImGuiItemFlags_SelectableDontClosePopup: ImGuiItemFlags_  # value = <ImGuiItemFlags_.ImGuiItemFlags_SelectableDontClosePopup: 32>
ImGuiItemStatusFlags_Deactivated: ImGuiItemStatusFlags_  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_Deactivated: 64>
ImGuiItemStatusFlags_Edited: ImGuiItemStatusFlags_  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_Edited: 4>
ImGuiItemStatusFlags_HasClipRect: ImGuiItemStatusFlags_  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HasClipRect: 512>
ImGuiItemStatusFlags_HasDeactivated: ImGuiItemStatusFlags_  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HasDeactivated: 32>
ImGuiItemStatusFlags_HasDisplayRect: ImGuiItemStatusFlags_  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HasDisplayRect: 2>
ImGuiItemStatusFlags_HasShortcut: ImGuiItemStatusFlags_  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HasShortcut: 1024>
ImGuiItemStatusFlags_HoveredRect: ImGuiItemStatusFlags_  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HoveredRect: 1>
ImGuiItemStatusFlags_HoveredWindow: ImGuiItemStatusFlags_  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_HoveredWindow: 128>
ImGuiItemStatusFlags_None: ImGuiItemStatusFlags_  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_None: 0>
ImGuiItemStatusFlags_ToggledOpen: ImGuiItemStatusFlags_  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_ToggledOpen: 16>
ImGuiItemStatusFlags_ToggledSelection: ImGuiItemStatusFlags_  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_ToggledSelection: 8>
ImGuiItemStatusFlags_Visible: ImGuiItemStatusFlags_  # value = <ImGuiItemStatusFlags_.ImGuiItemStatusFlags_Visible: 256>
ImGuiKey_0: ImGuiKey  # value = <ImGuiKey.ImGuiKey_0: 536>
ImGuiKey_1: ImGuiKey  # value = <ImGuiKey.ImGuiKey_1: 537>
ImGuiKey_2: ImGuiKey  # value = <ImGuiKey.ImGuiKey_2: 538>
ImGuiKey_3: ImGuiKey  # value = <ImGuiKey.ImGuiKey_3: 539>
ImGuiKey_4: ImGuiKey  # value = <ImGuiKey.ImGuiKey_4: 540>
ImGuiKey_5: ImGuiKey  # value = <ImGuiKey.ImGuiKey_5: 541>
ImGuiKey_6: ImGuiKey  # value = <ImGuiKey.ImGuiKey_6: 542>
ImGuiKey_7: ImGuiKey  # value = <ImGuiKey.ImGuiKey_7: 543>
ImGuiKey_8: ImGuiKey  # value = <ImGuiKey.ImGuiKey_8: 544>
ImGuiKey_9: ImGuiKey  # value = <ImGuiKey.ImGuiKey_9: 545>
ImGuiKey_A: ImGuiKey  # value = <ImGuiKey.ImGuiKey_A: 546>
ImGuiKey_Apostrophe: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Apostrophe: 596>
ImGuiKey_AppBack: ImGuiKey  # value = <ImGuiKey.ImGuiKey_AppBack: 629>
ImGuiKey_AppForward: ImGuiKey  # value = <ImGuiKey.ImGuiKey_AppForward: 630>
ImGuiKey_B: ImGuiKey  # value = <ImGuiKey.ImGuiKey_B: 547>
ImGuiKey_Backslash: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Backslash: 604>
ImGuiKey_Backspace: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Backspace: 523>
ImGuiKey_C: ImGuiKey  # value = <ImGuiKey.ImGuiKey_C: 548>
ImGuiKey_COUNT: ImGuiKey  # value = <ImGuiKey.ImGuiKey_COUNT: 666>
ImGuiKey_CapsLock: ImGuiKey  # value = <ImGuiKey.ImGuiKey_CapsLock: 607>
ImGuiKey_Comma: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Comma: 597>
ImGuiKey_D: ImGuiKey  # value = <ImGuiKey.ImGuiKey_D: 549>
ImGuiKey_Delete: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Delete: 522>
ImGuiKey_DownArrow: ImGuiKey  # value = <ImGuiKey.ImGuiKey_DownArrow: 516>
ImGuiKey_E: ImGuiKey  # value = <ImGuiKey.ImGuiKey_E: 550>
ImGuiKey_End: ImGuiKey  # value = <ImGuiKey.ImGuiKey_End: 520>
ImGuiKey_Enter: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Enter: 525>
ImGuiKey_Equal: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Equal: 602>
ImGuiKey_Escape: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Escape: 526>
ImGuiKey_F: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F: 551>
ImGuiKey_F1: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F1: 572>
ImGuiKey_F10: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F10: 581>
ImGuiKey_F11: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F11: 582>
ImGuiKey_F12: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F12: 583>
ImGuiKey_F13: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F13: 584>
ImGuiKey_F14: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F14: 585>
ImGuiKey_F15: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F15: 586>
ImGuiKey_F16: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F16: 587>
ImGuiKey_F17: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F17: 588>
ImGuiKey_F18: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F18: 589>
ImGuiKey_F19: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F19: 590>
ImGuiKey_F2: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F2: 573>
ImGuiKey_F20: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F20: 591>
ImGuiKey_F21: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F21: 592>
ImGuiKey_F22: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F22: 593>
ImGuiKey_F23: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F23: 594>
ImGuiKey_F24: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F24: 595>
ImGuiKey_F3: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F3: 574>
ImGuiKey_F4: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F4: 575>
ImGuiKey_F5: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F5: 576>
ImGuiKey_F6: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F6: 577>
ImGuiKey_F7: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F7: 578>
ImGuiKey_F8: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F8: 579>
ImGuiKey_F9: ImGuiKey  # value = <ImGuiKey.ImGuiKey_F9: 580>
ImGuiKey_G: ImGuiKey  # value = <ImGuiKey.ImGuiKey_G: 552>
ImGuiKey_GamepadBack: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadBack: 632>
ImGuiKey_GamepadDpadDown: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadDpadDown: 640>
ImGuiKey_GamepadDpadLeft: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadDpadLeft: 637>
ImGuiKey_GamepadDpadRight: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadDpadRight: 638>
ImGuiKey_GamepadDpadUp: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadDpadUp: 639>
ImGuiKey_GamepadFaceDown: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadFaceDown: 636>
ImGuiKey_GamepadFaceLeft: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadFaceLeft: 633>
ImGuiKey_GamepadFaceRight: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadFaceRight: 634>
ImGuiKey_GamepadFaceUp: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadFaceUp: 635>
ImGuiKey_GamepadL1: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadL1: 641>
ImGuiKey_GamepadL2: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadL2: 643>
ImGuiKey_GamepadL3: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadL3: 645>
ImGuiKey_GamepadLStickDown: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadLStickDown: 650>
ImGuiKey_GamepadLStickLeft: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadLStickLeft: 647>
ImGuiKey_GamepadLStickRight: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadLStickRight: 648>
ImGuiKey_GamepadLStickUp: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadLStickUp: 649>
ImGuiKey_GamepadR1: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadR1: 642>
ImGuiKey_GamepadR2: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadR2: 644>
ImGuiKey_GamepadR3: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadR3: 646>
ImGuiKey_GamepadRStickDown: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadRStickDown: 654>
ImGuiKey_GamepadRStickLeft: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadRStickLeft: 651>
ImGuiKey_GamepadRStickRight: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadRStickRight: 652>
ImGuiKey_GamepadRStickUp: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadRStickUp: 653>
ImGuiKey_GamepadStart: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GamepadStart: 631>
ImGuiKey_GraveAccent: ImGuiKey  # value = <ImGuiKey.ImGuiKey_GraveAccent: 606>
ImGuiKey_H: ImGuiKey  # value = <ImGuiKey.ImGuiKey_H: 553>
ImGuiKey_Home: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Home: 519>
ImGuiKey_I: ImGuiKey  # value = <ImGuiKey.ImGuiKey_I: 554>
ImGuiKey_Insert: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Insert: 521>
ImGuiKey_J: ImGuiKey  # value = <ImGuiKey.ImGuiKey_J: 555>
ImGuiKey_K: ImGuiKey  # value = <ImGuiKey.ImGuiKey_K: 556>
ImGuiKey_Keypad0: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Keypad0: 612>
ImGuiKey_Keypad1: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Keypad1: 613>
ImGuiKey_Keypad2: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Keypad2: 614>
ImGuiKey_Keypad3: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Keypad3: 615>
ImGuiKey_Keypad4: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Keypad4: 616>
ImGuiKey_Keypad5: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Keypad5: 617>
ImGuiKey_Keypad6: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Keypad6: 618>
ImGuiKey_Keypad7: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Keypad7: 619>
ImGuiKey_Keypad8: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Keypad8: 620>
ImGuiKey_Keypad9: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Keypad9: 621>
ImGuiKey_KeypadAdd: ImGuiKey  # value = <ImGuiKey.ImGuiKey_KeypadAdd: 626>
ImGuiKey_KeypadDecimal: ImGuiKey  # value = <ImGuiKey.ImGuiKey_KeypadDecimal: 622>
ImGuiKey_KeypadDivide: ImGuiKey  # value = <ImGuiKey.ImGuiKey_KeypadDivide: 623>
ImGuiKey_KeypadEnter: ImGuiKey  # value = <ImGuiKey.ImGuiKey_KeypadEnter: 627>
ImGuiKey_KeypadEqual: ImGuiKey  # value = <ImGuiKey.ImGuiKey_KeypadEqual: 628>
ImGuiKey_KeypadMultiply: ImGuiKey  # value = <ImGuiKey.ImGuiKey_KeypadMultiply: 624>
ImGuiKey_KeypadSubtract: ImGuiKey  # value = <ImGuiKey.ImGuiKey_KeypadSubtract: 625>
ImGuiKey_KeysData_OFFSET: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Tab: 512>
ImGuiKey_KeysData_SIZE: ImGuiKey  # value = <ImGuiKey.ImGuiKey_NamedKey_COUNT: 154>
ImGuiKey_L: ImGuiKey  # value = <ImGuiKey.ImGuiKey_L: 557>
ImGuiKey_LeftAlt: ImGuiKey  # value = <ImGuiKey.ImGuiKey_LeftAlt: 529>
ImGuiKey_LeftArrow: ImGuiKey  # value = <ImGuiKey.ImGuiKey_LeftArrow: 513>
ImGuiKey_LeftBracket: ImGuiKey  # value = <ImGuiKey.ImGuiKey_LeftBracket: 603>
ImGuiKey_LeftCtrl: ImGuiKey  # value = <ImGuiKey.ImGuiKey_LeftCtrl: 527>
ImGuiKey_LeftShift: ImGuiKey  # value = <ImGuiKey.ImGuiKey_LeftShift: 528>
ImGuiKey_LeftSuper: ImGuiKey  # value = <ImGuiKey.ImGuiKey_LeftSuper: 530>
ImGuiKey_M: ImGuiKey  # value = <ImGuiKey.ImGuiKey_M: 558>
ImGuiKey_Menu: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Menu: 535>
ImGuiKey_Minus: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Minus: 598>
ImGuiKey_MouseLeft: ImGuiKey  # value = <ImGuiKey.ImGuiKey_MouseLeft: 655>
ImGuiKey_MouseMiddle: ImGuiKey  # value = <ImGuiKey.ImGuiKey_MouseMiddle: 657>
ImGuiKey_MouseRight: ImGuiKey  # value = <ImGuiKey.ImGuiKey_MouseRight: 656>
ImGuiKey_MouseWheelX: ImGuiKey  # value = <ImGuiKey.ImGuiKey_MouseWheelX: 660>
ImGuiKey_MouseWheelY: ImGuiKey  # value = <ImGuiKey.ImGuiKey_MouseWheelY: 661>
ImGuiKey_MouseX1: ImGuiKey  # value = <ImGuiKey.ImGuiKey_MouseX1: 658>
ImGuiKey_MouseX2: ImGuiKey  # value = <ImGuiKey.ImGuiKey_MouseX2: 659>
ImGuiKey_N: ImGuiKey  # value = <ImGuiKey.ImGuiKey_N: 559>
ImGuiKey_NamedKey_BEGIN: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Tab: 512>
ImGuiKey_NamedKey_COUNT: ImGuiKey  # value = <ImGuiKey.ImGuiKey_NamedKey_COUNT: 154>
ImGuiKey_NamedKey_END: ImGuiKey  # value = <ImGuiKey.ImGuiKey_COUNT: 666>
ImGuiKey_None: ImGuiKey  # value = <ImGuiKey.ImGuiKey_None: 0>
ImGuiKey_NumLock: ImGuiKey  # value = <ImGuiKey.ImGuiKey_NumLock: 609>
ImGuiKey_O: ImGuiKey  # value = <ImGuiKey.ImGuiKey_O: 560>
ImGuiKey_P: ImGuiKey  # value = <ImGuiKey.ImGuiKey_P: 561>
ImGuiKey_PageDown: ImGuiKey  # value = <ImGuiKey.ImGuiKey_PageDown: 518>
ImGuiKey_PageUp: ImGuiKey  # value = <ImGuiKey.ImGuiKey_PageUp: 517>
ImGuiKey_Pause: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Pause: 611>
ImGuiKey_Period: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Period: 599>
ImGuiKey_PrintScreen: ImGuiKey  # value = <ImGuiKey.ImGuiKey_PrintScreen: 610>
ImGuiKey_Q: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Q: 562>
ImGuiKey_R: ImGuiKey  # value = <ImGuiKey.ImGuiKey_R: 563>
ImGuiKey_ReservedForModAlt: ImGuiKey  # value = <ImGuiKey.ImGuiKey_ReservedForModAlt: 664>
ImGuiKey_ReservedForModCtrl: ImGuiKey  # value = <ImGuiKey.ImGuiKey_ReservedForModCtrl: 662>
ImGuiKey_ReservedForModShift: ImGuiKey  # value = <ImGuiKey.ImGuiKey_ReservedForModShift: 663>
ImGuiKey_ReservedForModSuper: ImGuiKey  # value = <ImGuiKey.ImGuiKey_ReservedForModSuper: 665>
ImGuiKey_RightAlt: ImGuiKey  # value = <ImGuiKey.ImGuiKey_RightAlt: 533>
ImGuiKey_RightArrow: ImGuiKey  # value = <ImGuiKey.ImGuiKey_RightArrow: 514>
ImGuiKey_RightBracket: ImGuiKey  # value = <ImGuiKey.ImGuiKey_RightBracket: 605>
ImGuiKey_RightCtrl: ImGuiKey  # value = <ImGuiKey.ImGuiKey_RightCtrl: 531>
ImGuiKey_RightShift: ImGuiKey  # value = <ImGuiKey.ImGuiKey_RightShift: 532>
ImGuiKey_RightSuper: ImGuiKey  # value = <ImGuiKey.ImGuiKey_RightSuper: 534>
ImGuiKey_S: ImGuiKey  # value = <ImGuiKey.ImGuiKey_S: 564>
ImGuiKey_ScrollLock: ImGuiKey  # value = <ImGuiKey.ImGuiKey_ScrollLock: 608>
ImGuiKey_Semicolon: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Semicolon: 601>
ImGuiKey_Slash: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Slash: 600>
ImGuiKey_Space: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Space: 524>
ImGuiKey_T: ImGuiKey  # value = <ImGuiKey.ImGuiKey_T: 565>
ImGuiKey_Tab: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Tab: 512>
ImGuiKey_U: ImGuiKey  # value = <ImGuiKey.ImGuiKey_U: 566>
ImGuiKey_UpArrow: ImGuiKey  # value = <ImGuiKey.ImGuiKey_UpArrow: 515>
ImGuiKey_V: ImGuiKey  # value = <ImGuiKey.ImGuiKey_V: 567>
ImGuiKey_W: ImGuiKey  # value = <ImGuiKey.ImGuiKey_W: 568>
ImGuiKey_X: ImGuiKey  # value = <ImGuiKey.ImGuiKey_X: 569>
ImGuiKey_Y: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Y: 570>
ImGuiKey_Z: ImGuiKey  # value = <ImGuiKey.ImGuiKey_Z: 571>
ImGuiLayoutType_Horizontal: ImGuiLayoutType_  # value = <ImGuiLayoutType_.ImGuiLayoutType_Horizontal: 0>
ImGuiLayoutType_Vertical: ImGuiLayoutType_  # value = <ImGuiLayoutType_.ImGuiLayoutType_Vertical: 1>
ImGuiLocKey_COUNT: ImGuiLocKey  # value = <ImGuiLocKey.ImGuiLocKey_COUNT: 11>
ImGuiLocKey_DockingDragToUndockOrMoveNode: ImGuiLocKey  # value = <ImGuiLocKey.ImGuiLocKey_DockingDragToUndockOrMoveNode: 10>
ImGuiLocKey_DockingHideTabBar: ImGuiLocKey  # value = <ImGuiLocKey.ImGuiLocKey_DockingHideTabBar: 8>
ImGuiLocKey_DockingHoldShiftToDock: ImGuiLocKey  # value = <ImGuiLocKey.ImGuiLocKey_DockingHoldShiftToDock: 9>
ImGuiLocKey_TableResetOrder: ImGuiLocKey  # value = <ImGuiLocKey.ImGuiLocKey_TableResetOrder: 4>
ImGuiLocKey_TableSizeAllDefault: ImGuiLocKey  # value = <ImGuiLocKey.ImGuiLocKey_TableSizeAllDefault: 3>
ImGuiLocKey_TableSizeAllFit: ImGuiLocKey  # value = <ImGuiLocKey.ImGuiLocKey_TableSizeAllFit: 2>
ImGuiLocKey_TableSizeOne: ImGuiLocKey  # value = <ImGuiLocKey.ImGuiLocKey_TableSizeOne: 1>
ImGuiLocKey_VersionStr: ImGuiLocKey  # value = <ImGuiLocKey.ImGuiLocKey_VersionStr: 0>
ImGuiLocKey_WindowingMainMenuBar: ImGuiLocKey  # value = <ImGuiLocKey.ImGuiLocKey_WindowingMainMenuBar: 5>
ImGuiLocKey_WindowingPopup: ImGuiLocKey  # value = <ImGuiLocKey.ImGuiLocKey_WindowingPopup: 6>
ImGuiLocKey_WindowingUntitled: ImGuiLocKey  # value = <ImGuiLocKey.ImGuiLocKey_WindowingUntitled: 7>
ImGuiLogType_Buffer: ImGuiLogType  # value = <ImGuiLogType.ImGuiLogType_Buffer: 3>
ImGuiLogType_Clipboard: ImGuiLogType  # value = <ImGuiLogType.ImGuiLogType_Clipboard: 4>
ImGuiLogType_File: ImGuiLogType  # value = <ImGuiLogType.ImGuiLogType_File: 2>
ImGuiLogType_None: ImGuiLogType  # value = <ImGuiLogType.ImGuiLogType_None: 0>
ImGuiLogType_TTY: ImGuiLogType  # value = <ImGuiLogType.ImGuiLogType_TTY: 1>
ImGuiMod_Alt: ImGuiKey  # value = <ImGuiKey.ImGuiMod_Alt: 16384>
ImGuiMod_Ctrl: ImGuiKey  # value = <ImGuiKey.ImGuiMod_Ctrl: 4096>
ImGuiMod_Mask_: ImGuiKey  # value = <ImGuiKey.ImGuiMod_Mask_: 61440>
ImGuiMod_None: ImGuiKey  # value = <ImGuiKey.ImGuiKey_None: 0>
ImGuiMod_Shift: ImGuiKey  # value = <ImGuiKey.ImGuiMod_Shift: 8192>
ImGuiMod_Super: ImGuiKey  # value = <ImGuiKey.ImGuiMod_Super: 32768>
ImGuiMouseButton_COUNT: ImGuiMouseButton_  # value = <ImGuiMouseButton_.ImGuiMouseButton_COUNT: 5>
ImGuiMouseButton_Left: ImGuiMouseButton_  # value = <ImGuiMouseButton_.ImGuiMouseButton_Left: 0>
ImGuiMouseButton_Middle: ImGuiMouseButton_  # value = <ImGuiMouseButton_.ImGuiMouseButton_Middle: 2>
ImGuiMouseButton_Right: ImGuiMouseButton_  # value = <ImGuiMouseButton_.ImGuiMouseButton_Right: 1>
ImGuiMouseCursor_Arrow: ImGuiMouseCursor_  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_Arrow: 0>
ImGuiMouseCursor_COUNT: ImGuiMouseCursor_  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_COUNT: 9>
ImGuiMouseCursor_Hand: ImGuiMouseCursor_  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_Hand: 7>
ImGuiMouseCursor_None: ImGuiMouseCursor_  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_None: -1>
ImGuiMouseCursor_NotAllowed: ImGuiMouseCursor_  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_NotAllowed: 8>
ImGuiMouseCursor_ResizeAll: ImGuiMouseCursor_  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeAll: 2>
ImGuiMouseCursor_ResizeEW: ImGuiMouseCursor_  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeEW: 4>
ImGuiMouseCursor_ResizeNESW: ImGuiMouseCursor_  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeNESW: 5>
ImGuiMouseCursor_ResizeNS: ImGuiMouseCursor_  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeNS: 3>
ImGuiMouseCursor_ResizeNWSE: ImGuiMouseCursor_  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_ResizeNWSE: 6>
ImGuiMouseCursor_TextInput: ImGuiMouseCursor_  # value = <ImGuiMouseCursor_.ImGuiMouseCursor_TextInput: 1>
ImGuiMouseSource_COUNT: ImGuiMouseSource  # value = <ImGuiMouseSource.ImGuiMouseSource_COUNT: 3>
ImGuiMouseSource_Mouse: ImGuiMouseSource  # value = <ImGuiMouseSource.ImGuiMouseSource_Mouse: 0>
ImGuiMouseSource_Pen: ImGuiMouseSource  # value = <ImGuiMouseSource.ImGuiMouseSource_Pen: 2>
ImGuiMouseSource_TouchScreen: ImGuiMouseSource  # value = <ImGuiMouseSource.ImGuiMouseSource_TouchScreen: 1>
ImGuiNavHighlightFlags_AlwaysDraw: ImGuiNavHighlightFlags_  # value = <ImGuiNavHighlightFlags_.ImGuiNavHighlightFlags_AlwaysDraw: 4>
ImGuiNavHighlightFlags_Compact: ImGuiNavHighlightFlags_  # value = <ImGuiNavHighlightFlags_.ImGuiNavHighlightFlags_Compact: 2>
ImGuiNavHighlightFlags_NoRounding: ImGuiNavHighlightFlags_  # value = <ImGuiNavHighlightFlags_.ImGuiNavHighlightFlags_NoRounding: 8>
ImGuiNavHighlightFlags_None: ImGuiNavHighlightFlags_  # value = <ImGuiNavHighlightFlags_.ImGuiNavHighlightFlags_None: 0>
ImGuiNavLayer_COUNT: ImGuiNavLayer  # value = <ImGuiNavLayer.ImGuiNavLayer_COUNT: 2>
ImGuiNavLayer_Main: ImGuiNavLayer  # value = <ImGuiNavLayer.ImGuiNavLayer_Main: 0>
ImGuiNavLayer_Menu: ImGuiNavLayer  # value = <ImGuiNavLayer.ImGuiNavLayer_Menu: 1>
ImGuiNavMoveFlags_Activate: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_Activate: 4096>
ImGuiNavMoveFlags_AllowCurrentNavId: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_AllowCurrentNavId: 16>
ImGuiNavMoveFlags_AlsoScoreVisibleSet: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_AlsoScoreVisibleSet: 32>
ImGuiNavMoveFlags_DebugNoResult: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_DebugNoResult: 256>
ImGuiNavMoveFlags_FocusApi: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_FocusApi: 512>
ImGuiNavMoveFlags_Forwarded: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_Forwarded: 128>
ImGuiNavMoveFlags_IsPageMove: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_IsPageMove: 2048>
ImGuiNavMoveFlags_IsTabbing: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_IsTabbing: 1024>
ImGuiNavMoveFlags_LoopX: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_LoopX: 1>
ImGuiNavMoveFlags_LoopY: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_LoopY: 2>
ImGuiNavMoveFlags_NoClearActiveId: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_NoClearActiveId: 32768>
ImGuiNavMoveFlags_NoSelect: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_NoSelect: 8192>
ImGuiNavMoveFlags_NoSetNavHighlight: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_NoSetNavHighlight: 16384>
ImGuiNavMoveFlags_None: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_None: 0>
ImGuiNavMoveFlags_ScrollToEdgeY: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_ScrollToEdgeY: 64>
ImGuiNavMoveFlags_WrapMask_: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_WrapMask_: 15>
ImGuiNavMoveFlags_WrapX: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_WrapX: 4>
ImGuiNavMoveFlags_WrapY: ImGuiNavMoveFlags_  # value = <ImGuiNavMoveFlags_.ImGuiNavMoveFlags_WrapY: 8>
ImGuiNextItemDataFlags_HasOpen: ImGuiNextItemDataFlags_  # value = <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_HasOpen: 2>
ImGuiNextItemDataFlags_HasRefVal: ImGuiNextItemDataFlags_  # value = <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_HasRefVal: 8>
ImGuiNextItemDataFlags_HasShortcut: ImGuiNextItemDataFlags_  # value = <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_HasShortcut: 4>
ImGuiNextItemDataFlags_HasWidth: ImGuiNextItemDataFlags_  # value = <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_HasWidth: 1>
ImGuiNextItemDataFlags_None: ImGuiNextItemDataFlags_  # value = <ImGuiNextItemDataFlags_.ImGuiNextItemDataFlags_None: 0>
ImGuiNextWindowDataFlags_HasBgAlpha: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasBgAlpha: 64>
ImGuiNextWindowDataFlags_HasChildFlags: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasChildFlags: 256>
ImGuiNextWindowDataFlags_HasCollapsed: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasCollapsed: 8>
ImGuiNextWindowDataFlags_HasContentSize: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasContentSize: 4>
ImGuiNextWindowDataFlags_HasDock: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasDock: 2048>
ImGuiNextWindowDataFlags_HasFocus: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasFocus: 32>
ImGuiNextWindowDataFlags_HasPos: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasPos: 1>
ImGuiNextWindowDataFlags_HasRefreshPolicy: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasRefreshPolicy: 512>
ImGuiNextWindowDataFlags_HasScroll: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasScroll: 128>
ImGuiNextWindowDataFlags_HasSize: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasSize: 2>
ImGuiNextWindowDataFlags_HasSizeConstraint: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasSizeConstraint: 16>
ImGuiNextWindowDataFlags_HasViewport: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasViewport: 1024>
ImGuiNextWindowDataFlags_HasWindowClass: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_HasWindowClass: 4096>
ImGuiNextWindowDataFlags_None: ImGuiNextWindowDataFlags_  # value = <ImGuiNextWindowDataFlags_.ImGuiNextWindowDataFlags_None: 0>
ImGuiOldColumnFlags_GrowParentContentsSize: ImGuiOldColumnFlags_  # value = <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_GrowParentContentsSize: 16>
ImGuiOldColumnFlags_NoBorder: ImGuiOldColumnFlags_  # value = <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_NoBorder: 1>
ImGuiOldColumnFlags_NoForceWithinWindow: ImGuiOldColumnFlags_  # value = <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_NoForceWithinWindow: 8>
ImGuiOldColumnFlags_NoPreserveWidths: ImGuiOldColumnFlags_  # value = <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_NoPreserveWidths: 4>
ImGuiOldColumnFlags_NoResize: ImGuiOldColumnFlags_  # value = <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_NoResize: 2>
ImGuiOldColumnFlags_None: ImGuiOldColumnFlags_  # value = <ImGuiOldColumnFlags_.ImGuiOldColumnFlags_None: 0>
ImGuiPlotType_Histogram: ImGuiPlotType  # value = <ImGuiPlotType.ImGuiPlotType_Histogram: 1>
ImGuiPlotType_Lines: ImGuiPlotType  # value = <ImGuiPlotType.ImGuiPlotType_Lines: 0>
ImGuiPopupFlags_AnyPopup: ImGuiPopupFlags_  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_AnyPopup: 3072>
ImGuiPopupFlags_AnyPopupId: ImGuiPopupFlags_  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_AnyPopupId: 1024>
ImGuiPopupFlags_AnyPopupLevel: ImGuiPopupFlags_  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_AnyPopupLevel: 2048>
ImGuiPopupFlags_MouseButtonDefault_: ImGuiPopupFlags_  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonRight: 1>
ImGuiPopupFlags_MouseButtonLeft: ImGuiPopupFlags_  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_None: 0>
ImGuiPopupFlags_MouseButtonMask_: ImGuiPopupFlags_  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonMask_: 31>
ImGuiPopupFlags_MouseButtonMiddle: ImGuiPopupFlags_  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonMiddle: 2>
ImGuiPopupFlags_MouseButtonRight: ImGuiPopupFlags_  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonRight: 1>
ImGuiPopupFlags_NoOpenOverExistingPopup: ImGuiPopupFlags_  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_NoOpenOverExistingPopup: 128>
ImGuiPopupFlags_NoOpenOverItems: ImGuiPopupFlags_  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_NoOpenOverItems: 256>
ImGuiPopupFlags_NoReopen: ImGuiPopupFlags_  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_NoReopen: 32>
ImGuiPopupFlags_None: ImGuiPopupFlags_  # value = <ImGuiPopupFlags_.ImGuiPopupFlags_None: 0>
ImGuiPopupPositionPolicy_ComboBox: ImGuiPopupPositionPolicy  # value = <ImGuiPopupPositionPolicy.ImGuiPopupPositionPolicy_ComboBox: 1>
ImGuiPopupPositionPolicy_Default: ImGuiPopupPositionPolicy  # value = <ImGuiPopupPositionPolicy.ImGuiPopupPositionPolicy_Default: 0>
ImGuiPopupPositionPolicy_Tooltip: ImGuiPopupPositionPolicy  # value = <ImGuiPopupPositionPolicy.ImGuiPopupPositionPolicy_Tooltip: 2>
ImGuiScrollFlags_AlwaysCenterX: ImGuiScrollFlags_  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_AlwaysCenterX: 16>
ImGuiScrollFlags_AlwaysCenterY: ImGuiScrollFlags_  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_AlwaysCenterY: 32>
ImGuiScrollFlags_KeepVisibleCenterX: ImGuiScrollFlags_  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_KeepVisibleCenterX: 4>
ImGuiScrollFlags_KeepVisibleCenterY: ImGuiScrollFlags_  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_KeepVisibleCenterY: 8>
ImGuiScrollFlags_KeepVisibleEdgeX: ImGuiScrollFlags_  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_KeepVisibleEdgeX: 1>
ImGuiScrollFlags_KeepVisibleEdgeY: ImGuiScrollFlags_  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_KeepVisibleEdgeY: 2>
ImGuiScrollFlags_MaskX_: ImGuiScrollFlags_  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_MaskX_: 21>
ImGuiScrollFlags_MaskY_: ImGuiScrollFlags_  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_MaskY_: 42>
ImGuiScrollFlags_NoScrollParent: ImGuiScrollFlags_  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_NoScrollParent: 64>
ImGuiScrollFlags_None: ImGuiScrollFlags_  # value = <ImGuiScrollFlags_.ImGuiScrollFlags_None: 0>
ImGuiSelectableFlags_AllowDoubleClick: ImGuiSelectableFlags_  # value = <ImGuiSelectableFlags_.ImGuiSelectableFlags_AllowDoubleClick: 4>
ImGuiSelectableFlags_AllowOverlap: ImGuiSelectableFlags_  # value = <ImGuiSelectableFlags_.ImGuiSelectableFlags_AllowOverlap: 16>
ImGuiSelectableFlags_Disabled: ImGuiSelectableFlags_  # value = <ImGuiSelectableFlags_.ImGuiSelectableFlags_Disabled: 8>
ImGuiSelectableFlags_DontClosePopups: ImGuiSelectableFlags_  # value = <ImGuiSelectableFlags_.ImGuiSelectableFlags_DontClosePopups: 1>
ImGuiSelectableFlags_NoHoldingActiveID: ImGuiSelectableFlagsPrivate_  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_NoHoldingActiveID: 1048576>
ImGuiSelectableFlags_NoPadWithHalfSpacing: ImGuiSelectableFlagsPrivate_  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_NoPadWithHalfSpacing: 67108864>
ImGuiSelectableFlags_NoSetKeyOwner: ImGuiSelectableFlagsPrivate_  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_NoSetKeyOwner: 134217728>
ImGuiSelectableFlags_None: ImGuiSelectableFlags_  # value = <ImGuiSelectableFlags_.ImGuiSelectableFlags_None: 0>
ImGuiSelectableFlags_SelectOnClick: ImGuiSelectableFlagsPrivate_  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SelectOnClick: 4194304>
ImGuiSelectableFlags_SelectOnNav: ImGuiSelectableFlagsPrivate_  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SelectOnNav: 2097152>
ImGuiSelectableFlags_SelectOnRelease: ImGuiSelectableFlagsPrivate_  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SelectOnRelease: 8388608>
ImGuiSelectableFlags_SetNavIdOnHover: ImGuiSelectableFlagsPrivate_  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SetNavIdOnHover: 33554432>
ImGuiSelectableFlags_SpanAllColumns: ImGuiSelectableFlags_  # value = <ImGuiSelectableFlags_.ImGuiSelectableFlags_SpanAllColumns: 2>
ImGuiSelectableFlags_SpanAvailWidth: ImGuiSelectableFlagsPrivate_  # value = <ImGuiSelectableFlagsPrivate_.ImGuiSelectableFlags_SpanAvailWidth: 16777216>
ImGuiSeparatorFlags_Horizontal: ImGuiSeparatorFlags_  # value = <ImGuiSeparatorFlags_.ImGuiSeparatorFlags_Horizontal: 1>
ImGuiSeparatorFlags_None: ImGuiSeparatorFlags_  # value = <ImGuiSeparatorFlags_.ImGuiSeparatorFlags_None: 0>
ImGuiSeparatorFlags_SpanAllColumns: ImGuiSeparatorFlags_  # value = <ImGuiSeparatorFlags_.ImGuiSeparatorFlags_SpanAllColumns: 4>
ImGuiSeparatorFlags_Vertical: ImGuiSeparatorFlags_  # value = <ImGuiSeparatorFlags_.ImGuiSeparatorFlags_Vertical: 2>
ImGuiSliderFlags_AlwaysClamp: ImGuiSliderFlags_  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_AlwaysClamp: 16>
ImGuiSliderFlags_InvalidMask_: ImGuiSliderFlags_  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_InvalidMask_: 1879048207>
ImGuiSliderFlags_Logarithmic: ImGuiSliderFlags_  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_Logarithmic: 32>
ImGuiSliderFlags_NoInput: ImGuiSliderFlags_  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_NoInput: 128>
ImGuiSliderFlags_NoRoundToFormat: ImGuiSliderFlags_  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_NoRoundToFormat: 64>
ImGuiSliderFlags_None: ImGuiSliderFlags_  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_None: 0>
ImGuiSliderFlags_ReadOnly: ImGuiSliderFlagsPrivate_  # value = <ImGuiSliderFlagsPrivate_.ImGuiSliderFlags_ReadOnly: 2097152>
ImGuiSliderFlags_Vertical: ImGuiSliderFlagsPrivate_  # value = <ImGuiSliderFlagsPrivate_.ImGuiSliderFlags_Vertical: 1048576>
ImGuiSliderFlags_WrapAround: ImGuiSliderFlags_  # value = <ImGuiSliderFlags_.ImGuiSliderFlags_WrapAround: 256>
ImGuiSortDirection_Ascending: ImGuiSortDirection  # value = <ImGuiSortDirection.ImGuiSortDirection_Ascending: 1>
ImGuiSortDirection_Descending: ImGuiSortDirection  # value = <ImGuiSortDirection.ImGuiSortDirection_Descending: 2>
ImGuiSortDirection_None: ImGuiSortDirection  # value = <ImGuiSortDirection.ImGuiSortDirection_None: 0>
ImGuiStyleVar_Alpha: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_Alpha: 0>
ImGuiStyleVar_ButtonTextAlign: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_ButtonTextAlign: 27>
ImGuiStyleVar_COUNT: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_COUNT: 33>
ImGuiStyleVar_CellPadding: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_CellPadding: 17>
ImGuiStyleVar_ChildBorderSize: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_ChildBorderSize: 8>
ImGuiStyleVar_ChildRounding: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_ChildRounding: 7>
ImGuiStyleVar_DisabledAlpha: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_DisabledAlpha: 1>
ImGuiStyleVar_DockingSeparatorSize: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_DockingSeparatorSize: 32>
ImGuiStyleVar_FrameBorderSize: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_FrameBorderSize: 13>
ImGuiStyleVar_FramePadding: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_FramePadding: 11>
ImGuiStyleVar_FrameRounding: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_FrameRounding: 12>
ImGuiStyleVar_GrabMinSize: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_GrabMinSize: 20>
ImGuiStyleVar_GrabRounding: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_GrabRounding: 21>
ImGuiStyleVar_IndentSpacing: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_IndentSpacing: 16>
ImGuiStyleVar_ItemInnerSpacing: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_ItemInnerSpacing: 15>
ImGuiStyleVar_ItemSpacing: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_ItemSpacing: 14>
ImGuiStyleVar_PopupBorderSize: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_PopupBorderSize: 10>
ImGuiStyleVar_PopupRounding: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_PopupRounding: 9>
ImGuiStyleVar_ScrollbarRounding: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_ScrollbarRounding: 19>
ImGuiStyleVar_ScrollbarSize: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_ScrollbarSize: 18>
ImGuiStyleVar_SelectableTextAlign: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_SelectableTextAlign: 28>
ImGuiStyleVar_SeparatorTextAlign: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_SeparatorTextAlign: 30>
ImGuiStyleVar_SeparatorTextBorderSize: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_SeparatorTextBorderSize: 29>
ImGuiStyleVar_SeparatorTextPadding: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_SeparatorTextPadding: 31>
ImGuiStyleVar_TabBarBorderSize: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_TabBarBorderSize: 24>
ImGuiStyleVar_TabBorderSize: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_TabBorderSize: 23>
ImGuiStyleVar_TabRounding: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_TabRounding: 22>
ImGuiStyleVar_TableAngledHeadersAngle: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_TableAngledHeadersAngle: 25>
ImGuiStyleVar_TableAngledHeadersTextAlign: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_TableAngledHeadersTextAlign: 26>
ImGuiStyleVar_WindowBorderSize: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_WindowBorderSize: 4>
ImGuiStyleVar_WindowMinSize: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_WindowMinSize: 5>
ImGuiStyleVar_WindowPadding: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_WindowPadding: 2>
ImGuiStyleVar_WindowRounding: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_WindowRounding: 3>
ImGuiStyleVar_WindowTitleAlign: ImGuiStyleVar_  # value = <ImGuiStyleVar_.ImGuiStyleVar_WindowTitleAlign: 6>
ImGuiTabBarFlags_AutoSelectNewTabs: ImGuiTabBarFlags_  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_AutoSelectNewTabs: 2>
ImGuiTabBarFlags_DockNode: ImGuiTabBarFlagsPrivate_  # value = <ImGuiTabBarFlagsPrivate_.ImGuiTabBarFlags_DockNode: 1048576>
ImGuiTabBarFlags_DrawSelectedOverline: ImGuiTabBarFlags_  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_DrawSelectedOverline: 64>
ImGuiTabBarFlags_FittingPolicyDefault_: ImGuiTabBarFlags_  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_FittingPolicyResizeDown: 128>
ImGuiTabBarFlags_FittingPolicyMask_: ImGuiTabBarFlags_  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_FittingPolicyMask_: 384>
ImGuiTabBarFlags_FittingPolicyResizeDown: ImGuiTabBarFlags_  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_FittingPolicyResizeDown: 128>
ImGuiTabBarFlags_FittingPolicyScroll: ImGuiTabBarFlags_  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_FittingPolicyScroll: 256>
ImGuiTabBarFlags_IsFocused: ImGuiTabBarFlagsPrivate_  # value = <ImGuiTabBarFlagsPrivate_.ImGuiTabBarFlags_IsFocused: 2097152>
ImGuiTabBarFlags_NoCloseWithMiddleMouseButton: ImGuiTabBarFlags_  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_NoCloseWithMiddleMouseButton: 8>
ImGuiTabBarFlags_NoTabListScrollingButtons: ImGuiTabBarFlags_  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_NoTabListScrollingButtons: 16>
ImGuiTabBarFlags_NoTooltip: ImGuiTabBarFlags_  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_NoTooltip: 32>
ImGuiTabBarFlags_None: ImGuiTabBarFlags_  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_None: 0>
ImGuiTabBarFlags_Reorderable: ImGuiTabBarFlags_  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_Reorderable: 1>
ImGuiTabBarFlags_SaveSettings: ImGuiTabBarFlagsPrivate_  # value = <ImGuiTabBarFlagsPrivate_.ImGuiTabBarFlags_SaveSettings: 4194304>
ImGuiTabBarFlags_TabListPopupButton: ImGuiTabBarFlags_  # value = <ImGuiTabBarFlags_.ImGuiTabBarFlags_TabListPopupButton: 4>
ImGuiTabItemFlags_Button: ImGuiTabItemFlagsPrivate_  # value = <ImGuiTabItemFlagsPrivate_.ImGuiTabItemFlags_Button: 2097152>
ImGuiTabItemFlags_Leading: ImGuiTabItemFlags_  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_Leading: 64>
ImGuiTabItemFlags_NoAssumedClosure: ImGuiTabItemFlags_  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoAssumedClosure: 256>
ImGuiTabItemFlags_NoCloseButton: ImGuiTabItemFlagsPrivate_  # value = <ImGuiTabItemFlagsPrivate_.ImGuiTabItemFlags_NoCloseButton: 1048576>
ImGuiTabItemFlags_NoCloseWithMiddleMouseButton: ImGuiTabItemFlags_  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoCloseWithMiddleMouseButton: 4>
ImGuiTabItemFlags_NoPushId: ImGuiTabItemFlags_  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoPushId: 8>
ImGuiTabItemFlags_NoReorder: ImGuiTabItemFlags_  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoReorder: 32>
ImGuiTabItemFlags_NoTooltip: ImGuiTabItemFlags_  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_NoTooltip: 16>
ImGuiTabItemFlags_None: ImGuiTabItemFlags_  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_None: 0>
ImGuiTabItemFlags_SectionMask_: ImGuiTabItemFlagsPrivate_  # value = <ImGuiTabItemFlagsPrivate_.ImGuiTabItemFlags_SectionMask_: 192>
ImGuiTabItemFlags_SetSelected: ImGuiTabItemFlags_  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_SetSelected: 2>
ImGuiTabItemFlags_Trailing: ImGuiTabItemFlags_  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_Trailing: 128>
ImGuiTabItemFlags_UnsavedDocument: ImGuiTabItemFlags_  # value = <ImGuiTabItemFlags_.ImGuiTabItemFlags_UnsavedDocument: 1>
ImGuiTabItemFlags_Unsorted: ImGuiTabItemFlagsPrivate_  # value = <ImGuiTabItemFlagsPrivate_.ImGuiTabItemFlags_Unsorted: 4194304>
ImGuiTableBgTarget_CellBg: ImGuiTableBgTarget_  # value = <ImGuiTableBgTarget_.ImGuiTableBgTarget_CellBg: 3>
ImGuiTableBgTarget_None: ImGuiTableBgTarget_  # value = <ImGuiTableBgTarget_.ImGuiTableBgTarget_None: 0>
ImGuiTableBgTarget_RowBg0: ImGuiTableBgTarget_  # value = <ImGuiTableBgTarget_.ImGuiTableBgTarget_RowBg0: 1>
ImGuiTableBgTarget_RowBg1: ImGuiTableBgTarget_  # value = <ImGuiTableBgTarget_.ImGuiTableBgTarget_RowBg1: 2>
ImGuiTableColumnFlags_AngledHeader: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_AngledHeader: 262144>
ImGuiTableColumnFlags_DefaultHide: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_DefaultHide: 2>
ImGuiTableColumnFlags_DefaultSort: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_DefaultSort: 4>
ImGuiTableColumnFlags_Disabled: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_Disabled: 1>
ImGuiTableColumnFlags_IndentDisable: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IndentDisable: 131072>
ImGuiTableColumnFlags_IndentEnable: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IndentEnable: 65536>
ImGuiTableColumnFlags_IndentMask_: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IndentMask_: 196608>
ImGuiTableColumnFlags_IsEnabled: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IsEnabled: 16777216>
ImGuiTableColumnFlags_IsHovered: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IsHovered: 134217728>
ImGuiTableColumnFlags_IsSorted: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IsSorted: 67108864>
ImGuiTableColumnFlags_IsVisible: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_IsVisible: 33554432>
ImGuiTableColumnFlags_NoClip: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoClip: 256>
ImGuiTableColumnFlags_NoDirectResize_: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoDirectResize_: 1073741824>
ImGuiTableColumnFlags_NoHeaderLabel: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoHeaderLabel: 4096>
ImGuiTableColumnFlags_NoHeaderWidth: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoHeaderWidth: 8192>
ImGuiTableColumnFlags_NoHide: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoHide: 128>
ImGuiTableColumnFlags_NoReorder: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoReorder: 64>
ImGuiTableColumnFlags_NoResize: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoResize: 32>
ImGuiTableColumnFlags_NoSort: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoSort: 512>
ImGuiTableColumnFlags_NoSortAscending: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoSortAscending: 1024>
ImGuiTableColumnFlags_NoSortDescending: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_NoSortDescending: 2048>
ImGuiTableColumnFlags_None: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_None: 0>
ImGuiTableColumnFlags_PreferSortAscending: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_PreferSortAscending: 16384>
ImGuiTableColumnFlags_PreferSortDescending: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_PreferSortDescending: 32768>
ImGuiTableColumnFlags_StatusMask_: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_StatusMask_: 251658240>
ImGuiTableColumnFlags_WidthFixed: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_WidthFixed: 16>
ImGuiTableColumnFlags_WidthMask_: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_WidthMask_: 24>
ImGuiTableColumnFlags_WidthStretch: ImGuiTableColumnFlags_  # value = <ImGuiTableColumnFlags_.ImGuiTableColumnFlags_WidthStretch: 8>
ImGuiTableFlags_Borders: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_Borders: 1920>
ImGuiTableFlags_BordersH: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersH: 384>
ImGuiTableFlags_BordersInner: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersInner: 640>
ImGuiTableFlags_BordersInnerH: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersInnerH: 128>
ImGuiTableFlags_BordersInnerV: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersInnerV: 512>
ImGuiTableFlags_BordersOuter: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersOuter: 1280>
ImGuiTableFlags_BordersOuterH: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersOuterH: 256>
ImGuiTableFlags_BordersOuterV: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersOuterV: 1024>
ImGuiTableFlags_BordersV: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_BordersV: 1536>
ImGuiTableFlags_ContextMenuInBody: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_ContextMenuInBody: 32>
ImGuiTableFlags_Hideable: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_Hideable: 4>
ImGuiTableFlags_HighlightHoveredColumn: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_HighlightHoveredColumn: 268435456>
ImGuiTableFlags_NoBordersInBody: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoBordersInBody: 2048>
ImGuiTableFlags_NoBordersInBodyUntilResize: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoBordersInBodyUntilResize: 4096>
ImGuiTableFlags_NoClip: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoClip: 1048576>
ImGuiTableFlags_NoHostExtendX: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoHostExtendX: 65536>
ImGuiTableFlags_NoHostExtendY: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoHostExtendY: 131072>
ImGuiTableFlags_NoKeepColumnsVisible: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoKeepColumnsVisible: 262144>
ImGuiTableFlags_NoPadInnerX: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoPadInnerX: 8388608>
ImGuiTableFlags_NoPadOuterX: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoPadOuterX: 4194304>
ImGuiTableFlags_NoSavedSettings: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_NoSavedSettings: 16>
ImGuiTableFlags_None: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_None: 0>
ImGuiTableFlags_PadOuterX: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_PadOuterX: 2097152>
ImGuiTableFlags_PreciseWidths: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_PreciseWidths: 524288>
ImGuiTableFlags_Reorderable: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_Reorderable: 2>
ImGuiTableFlags_Resizable: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_Resizable: 1>
ImGuiTableFlags_RowBg: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_RowBg: 64>
ImGuiTableFlags_ScrollX: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_ScrollX: 16777216>
ImGuiTableFlags_ScrollY: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_ScrollY: 33554432>
ImGuiTableFlags_SizingFixedFit: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_SizingFixedFit: 8192>
ImGuiTableFlags_SizingFixedSame: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_SizingFixedSame: 16384>
ImGuiTableFlags_SizingMask_: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_SizingMask_: 57344>
ImGuiTableFlags_SizingStretchProp: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_SizingStretchProp: 24576>
ImGuiTableFlags_SizingStretchSame: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_SizingStretchSame: 32768>
ImGuiTableFlags_SortMulti: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_SortMulti: 67108864>
ImGuiTableFlags_SortTristate: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_SortTristate: 134217728>
ImGuiTableFlags_Sortable: ImGuiTableFlags_  # value = <ImGuiTableFlags_.ImGuiTableFlags_Sortable: 8>
ImGuiTableRowFlags_Headers: ImGuiTableRowFlags_  # value = <ImGuiTableRowFlags_.ImGuiTableRowFlags_Headers: 1>
ImGuiTableRowFlags_None: ImGuiTableRowFlags_  # value = <ImGuiTableRowFlags_.ImGuiTableRowFlags_None: 0>
ImGuiTextFlags_NoWidthForLargeClippedText: ImGuiTextFlags_  # value = <ImGuiTextFlags_.ImGuiTextFlags_NoWidthForLargeClippedText: 1>
ImGuiTextFlags_None: ImGuiTextFlags_  # value = <ImGuiTextFlags_.ImGuiTextFlags_None: 0>
ImGuiTooltipFlags_None: ImGuiTooltipFlags_  # value = <ImGuiTooltipFlags_.ImGuiTooltipFlags_None: 0>
ImGuiTooltipFlags_OverridePrevious: ImGuiTooltipFlags_  # value = <ImGuiTooltipFlags_.ImGuiTooltipFlags_OverridePrevious: 2>
ImGuiTreeNodeFlags_AllowOverlap: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_AllowOverlap: 4>
ImGuiTreeNodeFlags_Bullet: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Bullet: 512>
ImGuiTreeNodeFlags_ClipLabelForTrailingButton: ImGuiTreeNodeFlagsPrivate_  # value = <ImGuiTreeNodeFlagsPrivate_.ImGuiTreeNodeFlags_ClipLabelForTrailingButton: 1048576>
ImGuiTreeNodeFlags_CollapsingHeader: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_CollapsingHeader: 26>
ImGuiTreeNodeFlags_DefaultOpen: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_DefaultOpen: 32>
ImGuiTreeNodeFlags_FramePadding: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_FramePadding: 1024>
ImGuiTreeNodeFlags_Framed: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Framed: 2>
ImGuiTreeNodeFlags_Leaf: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Leaf: 256>
ImGuiTreeNodeFlags_NavLeftJumpsBackHere: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_NavLeftJumpsBackHere: 32768>
ImGuiTreeNodeFlags_NoAutoOpenOnLog: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_NoAutoOpenOnLog: 16>
ImGuiTreeNodeFlags_NoTreePushOnOpen: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_NoTreePushOnOpen: 8>
ImGuiTreeNodeFlags_None: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_None: 0>
ImGuiTreeNodeFlags_OpenOnArrow: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_OpenOnArrow: 128>
ImGuiTreeNodeFlags_OpenOnDoubleClick: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_OpenOnDoubleClick: 64>
ImGuiTreeNodeFlags_Selected: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Selected: 1>
ImGuiTreeNodeFlags_SpanAllColumns: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_SpanAllColumns: 16384>
ImGuiTreeNodeFlags_SpanAvailWidth: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_SpanAvailWidth: 2048>
ImGuiTreeNodeFlags_SpanFullWidth: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_SpanFullWidth: 4096>
ImGuiTreeNodeFlags_SpanTextWidth: ImGuiTreeNodeFlags_  # value = <ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_SpanTextWidth: 8192>
ImGuiTreeNodeFlags_UpsideDownArrow: ImGuiTreeNodeFlagsPrivate_  # value = <ImGuiTreeNodeFlagsPrivate_.ImGuiTreeNodeFlags_UpsideDownArrow: 2097152>
ImGuiTypingSelectFlags_AllowBackspace: ImGuiTypingSelectFlags_  # value = <ImGuiTypingSelectFlags_.ImGuiTypingSelectFlags_AllowBackspace: 1>
ImGuiTypingSelectFlags_AllowSingleCharMode: ImGuiTypingSelectFlags_  # value = <ImGuiTypingSelectFlags_.ImGuiTypingSelectFlags_AllowSingleCharMode: 2>
ImGuiTypingSelectFlags_None: ImGuiTypingSelectFlags_  # value = <ImGuiTypingSelectFlags_.ImGuiTypingSelectFlags_None: 0>
ImGuiViewportFlags_CanHostOtherWindows: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_CanHostOtherWindows: 2048>
ImGuiViewportFlags_IsFocused: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_IsFocused: 8192>
ImGuiViewportFlags_IsMinimized: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_IsMinimized: 4096>
ImGuiViewportFlags_IsPlatformMonitor: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_IsPlatformMonitor: 2>
ImGuiViewportFlags_IsPlatformWindow: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_IsPlatformWindow: 1>
ImGuiViewportFlags_NoAutoMerge: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoAutoMerge: 512>
ImGuiViewportFlags_NoDecoration: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoDecoration: 8>
ImGuiViewportFlags_NoFocusOnAppearing: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoFocusOnAppearing: 32>
ImGuiViewportFlags_NoFocusOnClick: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoFocusOnClick: 64>
ImGuiViewportFlags_NoInputs: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoInputs: 128>
ImGuiViewportFlags_NoRendererClear: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoRendererClear: 256>
ImGuiViewportFlags_NoTaskBarIcon: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_NoTaskBarIcon: 16>
ImGuiViewportFlags_None: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_None: 0>
ImGuiViewportFlags_OwnedByApp: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_OwnedByApp: 4>
ImGuiViewportFlags_TopMost: ImGuiViewportFlags_  # value = <ImGuiViewportFlags_.ImGuiViewportFlags_TopMost: 1024>
ImGuiWindowDockStyleCol_COUNT: ImGuiWindowDockStyleCol  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_COUNT: 8>
ImGuiWindowDockStyleCol_TabDimmed: ImGuiWindowDockStyleCol  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabDimmed: 5>
ImGuiWindowDockStyleCol_TabDimmedSelected: ImGuiWindowDockStyleCol  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabDimmedSelected: 6>
ImGuiWindowDockStyleCol_TabDimmedSelectedOverline: ImGuiWindowDockStyleCol  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabDimmedSelectedOverline: 7>
ImGuiWindowDockStyleCol_TabFocused: ImGuiWindowDockStyleCol  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabFocused: 2>
ImGuiWindowDockStyleCol_TabHovered: ImGuiWindowDockStyleCol  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabHovered: 1>
ImGuiWindowDockStyleCol_TabSelected: ImGuiWindowDockStyleCol  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabSelected: 3>
ImGuiWindowDockStyleCol_TabSelectedOverline: ImGuiWindowDockStyleCol  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_TabSelectedOverline: 4>
ImGuiWindowDockStyleCol_Text: ImGuiWindowDockStyleCol  # value = <ImGuiWindowDockStyleCol.ImGuiWindowDockStyleCol_Text: 0>
ImGuiWindowFlags_AlwaysAutoResize: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_AlwaysAutoResize: 64>
ImGuiWindowFlags_AlwaysHorizontalScrollbar: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_AlwaysHorizontalScrollbar: 32768>
ImGuiWindowFlags_AlwaysVerticalScrollbar: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_AlwaysVerticalScrollbar: 16384>
ImGuiWindowFlags_ChildMenu: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_ChildMenu: 268435456>
ImGuiWindowFlags_ChildWindow: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_ChildWindow: 16777216>
ImGuiWindowFlags_DockNodeHost: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_DockNodeHost: 536870912>
ImGuiWindowFlags_HorizontalScrollbar: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_HorizontalScrollbar: 2048>
ImGuiWindowFlags_MenuBar: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_MenuBar: 1024>
ImGuiWindowFlags_Modal: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_Modal: 134217728>
ImGuiWindowFlags_NoBackground: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoBackground: 128>
ImGuiWindowFlags_NoBringToFrontOnFocus: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoBringToFrontOnFocus: 8192>
ImGuiWindowFlags_NoCollapse: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoCollapse: 32>
ImGuiWindowFlags_NoDecoration: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoDecoration: 43>
ImGuiWindowFlags_NoDocking: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoDocking: 524288>
ImGuiWindowFlags_NoFocusOnAppearing: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoFocusOnAppearing: 4096>
ImGuiWindowFlags_NoInputs: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoInputs: 197120>
ImGuiWindowFlags_NoMouseInputs: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoMouseInputs: 512>
ImGuiWindowFlags_NoMove: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoMove: 4>
ImGuiWindowFlags_NoNav: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoNav: 196608>
ImGuiWindowFlags_NoNavFocus: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoNavFocus: 131072>
ImGuiWindowFlags_NoNavInputs: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoNavInputs: 65536>
ImGuiWindowFlags_NoResize: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoResize: 2>
ImGuiWindowFlags_NoSavedSettings: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoSavedSettings: 256>
ImGuiWindowFlags_NoScrollWithMouse: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoScrollWithMouse: 16>
ImGuiWindowFlags_NoScrollbar: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoScrollbar: 8>
ImGuiWindowFlags_NoTitleBar: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_NoTitleBar: 1>
ImGuiWindowFlags_None: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_None: 0>
ImGuiWindowFlags_Popup: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_Popup: 67108864>
ImGuiWindowFlags_Tooltip: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_Tooltip: 33554432>
ImGuiWindowFlags_UnsavedDocument: ImGuiWindowFlags_  # value = <ImGuiWindowFlags_.ImGuiWindowFlags_UnsavedDocument: 262144>
ImGuiWindowRefreshFlags_None: ImGuiWindowRefreshFlags_  # value = <ImGuiWindowRefreshFlags_.ImGuiWindowRefreshFlags_None: 0>
ImGuiWindowRefreshFlags_RefreshOnFocus: ImGuiWindowRefreshFlags_  # value = <ImGuiWindowRefreshFlags_.ImGuiWindowRefreshFlags_RefreshOnFocus: 4>
ImGuiWindowRefreshFlags_RefreshOnHover: ImGuiWindowRefreshFlags_  # value = <ImGuiWindowRefreshFlags_.ImGuiWindowRefreshFlags_RefreshOnHover: 2>
ImGuiWindowRefreshFlags_TryToAvoidRefresh: ImGuiWindowRefreshFlags_  # value = <ImGuiWindowRefreshFlags_.ImGuiWindowRefreshFlags_TryToAvoidRefresh: 1>
