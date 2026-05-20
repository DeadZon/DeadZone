"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/notification/row/ExpandableView.smali
Patches      : 8
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/notification/row/ExpandableView.smali'
CLASS_FALLBACK_NAMES = ['ExpandableView.smali']
CLASS_ANCHORS        = ['invoke-direct {v1, v2}, Landroid/util/FloatProperty;-><init>(Ljava/lang/String;)V', 'invoke-direct {v0, v2, v1}, Lcom/android/systemui/statusbar/notification/PhysicsProperty;-><init>(ILandroid/util/Property;)V', 'invoke-direct {v0}, Landroid/graphics/Rect;-><init>()V', 'sput-object v0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mClipRect:Landroid/graphics/Rect;', 'invoke-direct {p0, p1, p2}, Lcom/miui/systemui/notification/row/ExpandableViewBase;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V']

PATCHES = [
    {
        'id':             'p0000_animNotifPanel',
        'type':           'method_add',
        'method':         '.method public animNotifPanel()V',
        'method_name':    'animNotifPanel',
        'method_anchors': ['invoke-static {v1, v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I', 'invoke-static {v2, v3}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I', 'invoke-static {v3, v4}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I'],
        'search':         None,
        'replacement':    '.method public animNotifPanel()V\n    .registers 7\n\n    const/4 v5, 0x2\n\n    const/4 v0, 0x0\n\n    check-cast v0, Landroid/animation/ObjectAnimator;\n\n    const-string v1, "anim_expand_style"\n\n    const/4 v2, 0x5\n\n    invoke-static {v1, v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v1\n\n    const-string v2, "anim_expand_duration"\n\n    const/16 v3, 0x3e8\n\n    invoke-static {v2, v3}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v2\n\n    const-string v3, "anim_expand_interpolator"\n\n    const/4 v4, 0x5\n\n    invoke-static {v3, v4}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v3\n\n    packed-switch v1, :pswitch_data_0\n\n    :goto_0\n    packed-switch v3, :pswitch_data_1\n\n    :goto_1\n    int-to-long v2, v2\n\n    invoke-virtual {v0, v2, v3}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;\n\n    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->start()V\n\n    return-void\n\n    :pswitch_0  #0x0\n    const-string v0, "rotationX"\n\n    new-array v1, v5, [F\n\n    fill-array-data v1, :array_0\n\n    invoke-static {p0, v0, v1}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;\n\n    move-result-object v0\n\n    goto :goto_0\n\n    :pswitch_1  #0x1\n    const-string v0, "rotationY"\n\n    new-array v1, v5, [F\n\n    fill-array-data v1, :array_1\n\n    invoke-static {p0, v0, v1}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;\n\n    move-result-object v0\n\n    goto :goto_0\n\n    :pswitch_2  #0x2\n    const-string v0, "rotation"\n\n    new-array v1, v5, [F\n\n    fill-array-data v1, :array_2\n\n    invoke-static {p0, v0, v1}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;\n\n    move-result-object v0\n\n    goto :goto_0\n\n    :pswitch_3  #0x3\n    const-string v0, "rotation"\n\n    new-array v1, v5, [F\n\n    fill-array-data v1, :array_3\n\n    invoke-static {p0, v0, v1}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;\n\n    move-result-object v0\n\n    goto :goto_0\n\n    :pswitch_4  #0x4\n    const-string v0, "scaleX"\n\n    new-array v1, v5, [F\n\n    fill-array-data v1, :array_4\n\n    invoke-static {p0, v0, v1}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;\n\n    move-result-object v0\n\n    goto :goto_0\n\n    :pswitch_5  #0x5\n    const-string v0, "scaleY"\n\n    new-array v1, v5, [F\n\n    fill-array-data v1, :array_5\n\n    invoke-static {p0, v0, v1}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;\n\n    move-result-object v0\n\n    goto :goto_0\n\n    :pswitch_6  #0x6\n    const-string v0, "alpha"\n\n    new-array v1, v5, [F\n\n    fill-array-data v1, :array_6\n\n    invoke-static {p0, v0, v1}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;\n\n    move-result-object v0\n\n    goto :goto_0\n\n    :pswitch_7  #0x7\n    const-string v0, "rotationX"\n\n    new-array v1, v5, [F\n\n    fill-array-data v1, :array_7\n\n    invoke-static {p0, v0, v1}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;\n\n    move-result-object v0\n\n    goto :goto_0\n\n    :pswitch_8  #0x0\n    new-instance v1, Landroid/view/animation/LinearInterpolator;\n\n    invoke-direct {v1}, Landroid/view/animation/LinearInterpolator;-><init>()V\n\n    invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V\n\n    goto :goto_1\n\n    :pswitch_9  #0x1\n    new-instance v1, Landroid/view/animation/AccelerateInterpolator;\n\n    invoke-direct {v1}, Landroid/view/animation/AccelerateInterpolator;-><init>()V\n\n    invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V\n\n    goto :goto_1\n\n    :pswitch_a  #0x2\n    new-instance v1, Landroid/view/animation/DecelerateInterpolator;\n\n    invoke-direct {v1}, Landroid/view/animation/DecelerateInterpolator;-><init>()V\n\n    invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V\n\n    goto :goto_1\n\n    :pswitch_b  #0x3\n    new-instance v1, Landroid/view/animation/AccelerateDecelerateInterpolator;\n\n    invoke-direct {v1}, Landroid/view/animation/AccelerateDecelerateInterpolator;-><init>()V\n\n    invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V\n\n    goto :goto_1\n\n    :pswitch_c  #0x4\n    new-instance v1, Landroid/view/animation/BounceInterpolator;\n\n    invoke-direct {v1}, Landroid/view/animation/BounceInterpolator;-><init>()V\n\n    invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V\n\n    goto :goto_1\n\n    :pswitch_d  #0x5\n    new-instance v1, Landroid/view/animation/OvershootInterpolator;\n\n    invoke-direct {v1}, Landroid/view/animation/OvershootInterpolator;-><init>()V\n\n    invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V\n\n    goto :goto_1\n\n    nop\n\n    :pswitch_data_0\n    .packed-switch 0x0\n        :pswitch_0  #00000000\n        :pswitch_1  #00000001\n        :pswitch_2  #00000002\n        :pswitch_3  #00000003\n        :pswitch_4  #00000004\n        :pswitch_5  #00000005\n        :pswitch_6  #00000006\n        :pswitch_7  #00000007\n    .end packed-switch\n\n    :pswitch_data_1\n    .packed-switch 0x0\n        :pswitch_8  #00000000\n        :pswitch_9  #00000001\n        :pswitch_a  #00000002\n        :pswitch_b  #00000003\n        :pswitch_c  #00000004\n        :pswitch_d  #00000005\n    .end packed-switch\n\n    :array_0\n    .array-data 4\n        0x0\n        0x43b40000\n    .end array-data\n\n    :array_1\n    .array-data 4\n        0x0\n        0x43b40000\n    .end array-data\n\n    :array_2\n    .array-data 4\n        0x0\n        0x43b40000\n    .end array-data\n\n    :array_3\n    .array-data 4\n        0x0\n        -0x3c4c0000\n    .end array-data\n\n    :array_4\n    .array-data 4\n        0x0\n        0x3f800000\n    .end array-data\n\n    :array_5\n    .array-data 4\n        0x0\n        0x3f800000\n    .end array-data\n\n    :array_6\n    .array-data 4\n        0x0\n        0x3f800000\n    .end array-data\n\n    :array_7\n    .array-data 4\n        0x0\n        -0x3c4c0000\n    .end array-data\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0001_enableAnim',
        'type':           'method_add',
        'method':         '.method public enableAnim()Z',
        'method_name':    'enableAnim',
        'method_anchors': ['invoke-static {v2, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I'],
        'search':         None,
        'replacement':    '.method public enableAnim()Z\n    .registers 4\n\n    const/4 v0, 0x1\n\n    const v1, 0x0\n\n    const-string v2, "anim_expand_enable"\n\n    invoke-static {v2, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v2\n\n    if-eqz v2, :cond_0\n\n    return v0\n\n    :cond_0\n    return v1\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0002_setActualHeight',
        'type':           'method_replace',
        'method':         '.method public setActualHeight(IZ)V',
        'method_name':    'setActualHeight',
        'method_anchors': ['invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I', 'invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->setAnimationPanel()V', 'iget v0, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mActualHeight:I'],
        'search':         '.method public setActualHeight(IZ)V\n    .registers 4\n    .annotation runtime Ljava/lang/Deprecated;\n    .end annotation\n\n    iget v0, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mActualHeight:I\n\n    if-eq v0, p1, :cond_0\n\n    iput p1, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mActualHeight:I\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->updateClipping$1()V\n\n    if-eqz p2, :cond_0\n\n    const/4 p1, 0x0\n\n    invoke-virtual {p0, p1}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->notifyHeightChanged(Z)V\n\n    :cond_0\n    return-void\n.end method\n',
        'replacement':    '.method public setActualHeight(IZ)V\n    .registers 5\n    .annotation runtime Ljava/lang/Deprecated;\n    .end annotation\n\n    const-string v0, "loopanim"\n\n    const/4 v1, 0x3\n\n    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v0\n\n    const/4 v1, 0x4\n\n    if-eq v0, v1, :cond_0\n\n    goto :goto_0\n\n    :cond_0\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->setAnimationPanel()V\n\n    :goto_0\n    iget v0, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mActualHeight:I\n\n    if-eq v0, p1, :cond_1\n\n    iput p1, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mActualHeight:I\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->updateClipping$1()V\n\n    if-eqz p2, :cond_1\n\n    const/4 p1, 0x0\n\n    invoke-virtual {p0, p1}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->notifyHeightChanged(Z)V\n\n    :cond_1\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
    {
        'id':             'p0003_setAnimationPanel',
        'type':           'method_add',
        'method':         '.method public setAnimationPanel()V',
        'method_name':    'setAnimationPanel',
        'method_anchors': ['invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->enableAnim()Z', 'invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->animNotifPanel()V'],
        'search':         None,
        'replacement':    '.method public setAnimationPanel()V\n    .registers 2\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->enableAnim()Z\n\n    move-result v0\n\n    if-nez v0, :cond_0\n\n    :goto_0\n    return-void\n\n    :cond_0\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->animNotifPanel()V\n\n    goto :goto_0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0004_setChangingPosition',
        'type':           'method_replace',
        'method':         '.method public setChangingPosition(Z)V',
        'method_name':    'setChangingPosition',
        'method_anchors': ['invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I', 'iput-boolean p1, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mChangingPosition:Z', 'invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->setAnimationPanel()V'],
        'search':         '.method public setChangingPosition(Z)V\n    .registers 2\n\n    iput-boolean p1, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mChangingPosition:Z\n\n    return-void\n.end method\n',
        'replacement':    '.method public setChangingPosition(Z)V\n    .registers 5\n\n    const-string v0, "loopanim"\n\n    const/4 v1, 0x3\n\n    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v0\n\n    const/4 v2, 0x2\n\n    if-eq v0, v1, :cond_0\n\n    if-eq v0, v2, :cond_0\n\n    iput-boolean p1, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mChangingPosition:Z\n\n    goto :goto_0\n\n    :cond_0\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->setAnimationPanel()V\n\n    iput-boolean p1, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mChangingPosition:Z\n\n    goto :goto_0\n\n    :goto_0\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
    {
        'id':             'p0005_setLayerType',
        'type':           'method_replace',
        'method':         '.method public setLayerType(ILandroid/graphics/Paint;)V',
        'method_name':    'setLayerType',
        'method_anchors': ['invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I', 'invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->setAnimationPanel()V', 'invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->hasOverlappingRendering()Z'],
        'search':         '.method public setLayerType(ILandroid/graphics/Paint;)V\n    .registers 3\n\n    if-eqz p1, :cond_0\n\n    return-void\n\n    :cond_0\n    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->setLayerType(ILandroid/graphics/Paint;)V\n\n    return-void\n.end method\n',
        'replacement':    '.method public setLayerType(ILandroid/graphics/Paint;)V\n    .registers 6\n\n    const-string v0, "loopanim"\n\n    const/4 v1, 0x3\n\n    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v0\n\n    const/4 v1, 0x1\n\n    const/4 v2, 0x2\n\n    if-eq v0, v1, :cond_0\n\n    if-eq v0, v2, :cond_0\n\n    goto :goto_0\n\n    :cond_0\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->setAnimationPanel()V\n\n    :goto_0\n    if-eqz p1, :cond_1\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->hasOverlappingRendering()Z\n\n    move-result v0\n\n    if-eqz v0, :cond_2\n\n    :cond_1\n    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->setLayerType(ILandroid/graphics/Paint;)V\n\n    :cond_2\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
    {
        'id':             'p0006_updateClipping',
        'type':           'method_add',
        'method':         '.method public final updateClipping()V',
        'method_name':    'updateClipping',
        'method_anchors': ['iget-boolean v0, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mClipToActualHeight:Z', 'invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->shouldClipToActualHeight()Z', 'invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->getClipTopAmount()I'],
        'search':         None,
        'replacement':    '.method public final updateClipping()V\n    .registers 6\n\n    iget-boolean v0, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mClipToActualHeight:Z\n\n    if-eqz v0, :cond_0\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->shouldClipToActualHeight()Z\n\n    move-result v0\n\n    if-eqz v0, :cond_0\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->getClipTopAmount()I\n\n    move-result v0\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->getActualHeight()I\n\n    move-result v1\n\n    iget v2, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mClipBottomAmount:I\n\n    sub-int/2addr v1, v2\n\n    invoke-static {v1, v0}, Ljava/lang/Math;->max(II)I\n\n    move-result v1\n\n    iget v2, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mMinimumHeightForClipping:I\n\n    invoke-static {v1, v2}, Ljava/lang/Math;->max(II)I\n\n    move-result v1\n\n    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getWidth()I\n\n    move-result v2\n\n    iget v3, p0, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mClipRightAmount:I\n\n    sub-int/2addr v2, v3\n\n    sget-object v3, Lcom/android/systemui/statusbar/notification/row/ExpandableView;->mClipRect:Landroid/graphics/Rect;\n\n    const/4 v4, 0x0\n\n    invoke-virtual {v3, v4, v0, v2, v1}, Landroid/graphics/Rect;->set(IIII)V\n\n    invoke-virtual {p0, v3}, Landroid/widget/FrameLayout;->setClipBounds(Landroid/graphics/Rect;)V\n\n    goto :goto_0\n\n    :cond_0\n    const/4 v0, 0x0\n\n    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->setClipBounds(Landroid/graphics/Rect;)V\n\n    :goto_0\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0007_field__field_public_mClipR',
        'type':           'field_add',
        'method':         '.field public mClipRightAmount:I',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field public mClipRightAmount:I',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added field',
    },
]
