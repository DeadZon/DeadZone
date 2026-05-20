"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/phone/KeyguardStatusBarView.smali
Patches      : 9
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/phone/KeyguardStatusBarView.smali'
CLASS_FALLBACK_NAMES = ['KeyguardStatusBarView.smali']
CLASS_ANCHORS        = ['invoke-direct {p0, p1, p2}, Landroid/widget/RelativeLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V', 'invoke-direct {p1}, Ljava/util/ArrayList;-><init>()V', 'invoke-static {p1}, Lkotlinx/coroutines/flow/StateFlowKt;->MutableStateFlow(Ljava/lang/Object;)Lkotlinx/coroutines/flow/StateFlowImpl;', 'iput-object p1, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mDarkChange:Lkotlinx/coroutines/flow/StateFlowImpl;', 'iput p1, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mLayoutState:I']

PATCHES = [
    {
        'id':             'p0000_hasOverlappingRendering',
        'type':           'method_add',
        'method':         '.method public hasOverlappingRendering()Z',
        'method_name':    'hasOverlappingRendering',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.method public hasOverlappingRendering()Z\n    .registers 1\n\n    const/4 p0, 0x0\n\n    return p0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0001_loadDimens',
        'type':           'method_add',
        'method':         '.method public loadDimens()V',
        'method_name':    'loadDimens',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/RelativeLayout;->getResources()Landroid/content/res/Resources;', 'invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I', 'iput v1, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mSystemIconsSwitcherHiddenExpandedMargin:I'],
        'search':         None,
        'replacement':    '.method public loadDimens()V\n    .registers 4\n\n    invoke-virtual {p0}, Landroid/widget/RelativeLayout;->getResources()Landroid/content/res/Resources;\n\n    move-result-object v0\n\n    const v1, 0x7f071a16\n\n    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I\n\n    move-result v1\n\n    iput v1, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mSystemIconsSwitcherHiddenExpandedMargin:I\n\n    const v1, 0x7f0718b2\n\n    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I\n\n    const v1, 0x7f07151c\n\n    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I\n\n    move-result v1\n\n    iput v1, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mMinDotWidth:I\n\n    invoke-virtual {p0}, Landroid/widget/RelativeLayout;->getResources()Landroid/content/res/Resources;\n\n    move-result-object v1\n\n    const v2, 0x7f0703e7\n\n    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I\n\n    move-result v1\n\n    iput v1, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mCutoutSideNudge:I\n\n    invoke-virtual {p0}, Landroid/widget/RelativeLayout;->getContext()Landroid/content/Context;\n\n    move-result-object v1\n\n    invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;\n\n    move-result-object v1\n\n    const v2, 0x1110059\n\n    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getBoolean(I)Z\n\n    iget-object p0, p0, Landroid/widget/RelativeLayout;->mContext:Landroid/content/Context;\n\n    invoke-static {p0}, Lcom/miui/utils/configs/MiuiConfigs;->isFlipTinyScreen(Landroid/content/Context;)Z\n\n    move-result p0\n\n    if-eqz p0, :cond_0\n\n    const p0, 0x7f071779\n\n    goto :goto_0\n\n    :cond_0\n    const p0, 0x7f07173a\n\n    :goto_0\n    invoke-virtual {v0, p0}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0002_onLayout',
        'type':           'method_add',
        'method':         '.method public onLayout(ZIIII)V',
        'method_name':    'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Landroid/widget/RelativeLayout;->onLayout(ZIIII)V', 'iget-object p1, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mClipRect:Landroid/graphics/Rect;', 'iget p2, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mTopClipping:I'],
        'search':         None,
        'replacement':    '.method public onLayout(ZIIII)V\n    .registers 6\n\n    invoke-super/range {p0 .. p5}, Landroid/widget/RelativeLayout;->onLayout(ZIIII)V\n\n    iget-object p1, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mClipRect:Landroid/graphics/Rect;\n\n    iget p2, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mTopClipping:I\n\n    invoke-virtual {p0}, Landroid/widget/RelativeLayout;->getWidth()I\n\n    move-result p3\n\n    invoke-virtual {p0}, Landroid/widget/RelativeLayout;->getHeight()I\n\n    move-result p4\n\n    const/4 p5, 0x0\n\n    invoke-virtual {p1, p5, p2, p3, p4}, Landroid/graphics/Rect;->set(IIII)V\n\n    iget-object p1, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mClipRect:Landroid/graphics/Rect;\n\n    invoke-virtual {p0, p1}, Landroid/widget/RelativeLayout;->setClipBounds(Landroid/graphics/Rect;)V\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0003_onMeasure',
        'type':           'method_add',
        'method':         '.method public onMeasure(II)V',
        'method_name':    'onMeasure',
        'method_anchors': ['invoke-static {v0}, Landroid/os/Trace;->beginSection(Ljava/lang/String;)V', 'invoke-super {p0, p1, p2}, Landroid/widget/RelativeLayout;->onMeasure(II)V', 'invoke-static {}, Landroid/os/Trace;->endSection()V'],
        'search':         None,
        'replacement':    '.method public onMeasure(II)V\n    .registers 4\n\n    const-string v0, "KeyguardStatusBarView#onMeasure"\n\n    invoke-static {v0}, Landroid/os/Trace;->beginSection(Ljava/lang/String;)V\n\n    invoke-super {p0, p1, p2}, Landroid/widget/RelativeLayout;->onMeasure(II)V\n\n    invoke-static {}, Landroid/os/Trace;->endSection()V\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0004_onThemeChanged',
        'type':           'method_add',
        'method':         '.method public onThemeChanged()V',
        'method_name':    'onThemeChanged',
        'method_anchors': ['invoke-virtual {p0}, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->updateIconsAndTextColors()V'],
        'search':         None,
        'replacement':    '.method public onThemeChanged()V\n    .registers 1\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->updateIconsAndTextColors()V\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0005_updateSystemIconsLayoutParams',
        'type':           'method_add',
        'method':         '.method public updateSystemIconsLayoutParams()V',
        'method_name':    'updateSystemIconsLayoutParams',
        'method_anchors': ['iget-object v0, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;', 'invoke-virtual {v0}, Landroid/view/ViewGroup;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'iget-boolean v1, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mKeyguardUserSwitcherEnabled:Z'],
        'search':         None,
        'replacement':    '.method public updateSystemIconsLayoutParams()V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;\n\n    invoke-virtual {v0}, Landroid/view/ViewGroup;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;\n\n    move-result-object v0\n\n    check-cast v0, Landroid/widget/LinearLayout$LayoutParams;\n\n    iget-boolean v1, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mKeyguardUserSwitcherEnabled:Z\n\n    if-eqz v1, :cond_0\n\n    iget v1, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mSystemIconsSwitcherHiddenExpandedMargin:I\n\n    goto :goto_0\n\n    :cond_0\n    const/4 v1, 0x0\n\n    :goto_0\n    invoke-virtual {v0}, Landroid/widget/LinearLayout$LayoutParams;->getMarginEnd()I\n\n    move-result v2\n\n    if-eq v1, v2, :cond_1\n\n    invoke-virtual {v0, v1}, Landroid/widget/LinearLayout$LayoutParams;->setMarginEnd(I)V\n\n    iget-object p0, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;\n\n    invoke-virtual {p0, v0}, Landroid/view/ViewGroup;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V\n\n    :cond_1\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0006_updateWindowInsets',
        'type':           'method_add',
        'method':         '.method public updateWindowInsets(Landroid/view/WindowInsets;Lcom/android/systemui/statusbar/layout/StatusBarContentInsetsProvider;)Landroid/view/WindowInsets;',
        'method_name':    'updateWindowInsets',
        'method_anchors': ['iget-object v0, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mPreviousInsets:Landroid/view/WindowInsets;', 'invoke-static {v0, p1}, Ljava/util/Objects;->equals(Ljava/lang/Object;Ljava/lang/Object;)Z', 'iput v0, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mLayoutState:I'],
        'search':         None,
        'replacement':    '.method public updateWindowInsets(Landroid/view/WindowInsets;Lcom/android/systemui/statusbar/layout/StatusBarContentInsetsProvider;)Landroid/view/WindowInsets;\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mPreviousInsets:Landroid/view/WindowInsets;\n\n    invoke-static {v0, p1}, Ljava/util/Objects;->equals(Ljava/lang/Object;Ljava/lang/Object;)Z\n\n    move-result v0\n\n    if-nez v0, :cond_1\n\n    const/4 v0, 0x0\n\n    iput v0, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mLayoutState:I\n\n    invoke-virtual {p0}, Landroid/widget/RelativeLayout;->getRootWindowInsets()Landroid/view/WindowInsets;\n\n    move-result-object v0\n\n    invoke-virtual {v0}, Landroid/view/WindowInsets;->getDisplayCutout()Landroid/view/DisplayCutout;\n\n    move-result-object v0\n\n    invoke-virtual {p0, v0, p2}, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->setDisplayCutout(Landroid/view/DisplayCutout;Lcom/android/systemui/statusbar/layout/StatusBarContentInsetsProvider;)Z\n\n    move-result p2\n\n    if-eqz p2, :cond_0\n\n    invoke-virtual {p0}, Landroid/widget/RelativeLayout;->requestLayout()V\n\n    :cond_0\n    new-instance p2, Landroid/view/WindowInsets;\n\n    invoke-direct {p2, p1}, Landroid/view/WindowInsets;-><init>(Landroid/view/WindowInsets;)V\n\n    iput-object p2, p0, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;->mPreviousInsets:Landroid/view/WindowInsets;\n\n    :cond_1\n    invoke-super {p0, p1}, Landroid/widget/RelativeLayout;->onApplyWindowInsets(Landroid/view/WindowInsets;)Landroid/view/WindowInsets;\n\n    move-result-object p0\n\n    return-object p0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0007_field__field_public_mClipR',
        'type':           'field_add',
        'method':         '.field public mClipRect:Landroid/graphics/Rect;',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field public mClipRect:Landroid/graphics/Rect;',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added field',
    },
    {
        'id':             'p0008_field__field_public_mDarkC',
        'type':           'field_add',
        'method':         '.field public mDarkChange:Lkotlinx/coroutines/flow/StateFlowImpl;',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field public mDarkChange:Lkotlinx/coroutines/flow/StateFlowImpl;',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added field',
    },
]
