"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/AnimatedImageView.smali
Patches      : 5
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/AnimatedImageView.smali'
CLASS_FALLBACK_NAMES = ['AnimatedImageView.smali']
CLASS_ANCHORS        = ['invoke-direct {p0, p1, v0}, Lcom/android/systemui/statusbar/AnimatedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V', 'invoke-direct {p0, p1, p2}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V', 'iput-boolean v0, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAllowAnimation:Z', 'invoke-virtual {p1}, Landroid/content/Context;->getTheme()Landroid/content/res/Resources$Theme;', 'invoke-virtual {p1, p2, v1, v2, v2}, Landroid/content/res/Resources$Theme;->obtainStyledAttributes(Landroid/util/AttributeSet;[III)Landroid/content/res/TypedArray;']

PATCHES = [
    {
        'id':             'p0000_onAttachedToWindow',
        'type':           'method_add',
        'method':         '.method public onAttachedToWindow()V',
        'method_name':    'onAttachedToWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/ImageView;->onAttachedToWindow()V', 'iput-boolean v0, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAttached:Z', 'invoke-virtual {p0}, Lcom/android/systemui/statusbar/AnimatedImageView;->updateAnim()V'],
        'search':         None,
        'replacement':    '.method public onAttachedToWindow()V\n    .registers 2\n\n    invoke-super {p0}, Landroid/widget/ImageView;->onAttachedToWindow()V\n\n    const/4 v0, 0x1\n\n    iput-boolean v0, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAttached:Z\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/AnimatedImageView;->updateAnim()V\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0001_onDetachedFromWindow',
        'type':           'method_add',
        'method':         '.method public onDetachedFromWindow()V',
        'method_name':    'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/ImageView;->onDetachedFromWindow()V', 'iget-object v0, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAnim:Landroid/graphics/drawable/AnimationDrawable;', 'invoke-virtual {v0}, Landroid/graphics/drawable/AnimationDrawable;->stop()V'],
        'search':         None,
        'replacement':    '.method public onDetachedFromWindow()V\n    .registers 2\n\n    invoke-super {p0}, Landroid/widget/ImageView;->onDetachedFromWindow()V\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAnim:Landroid/graphics/drawable/AnimationDrawable;\n\n    if-eqz v0, :cond_0\n\n    invoke-virtual {v0}, Landroid/graphics/drawable/AnimationDrawable;->stop()V\n\n    :cond_0\n    const/4 v0, 0x0\n\n    iput-boolean v0, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAttached:Z\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0002_onVisibilityChanged',
        'type':           'method_add',
        'method':         '.method public onVisibilityChanged(Landroid/view/View;I)V',
        'method_name':    'onVisibilityChanged',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroid/widget/ImageView;->onVisibilityChanged(Landroid/view/View;I)V', 'iget-object p1, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAnim:Landroid/graphics/drawable/AnimationDrawable;', 'invoke-virtual {p0}, Landroid/widget/ImageView;->isShown()Z'],
        'search':         None,
        'replacement':    '.method public onVisibilityChanged(Landroid/view/View;I)V\n    .registers 3\n\n    invoke-super {p0, p1, p2}, Landroid/widget/ImageView;->onVisibilityChanged(Landroid/view/View;I)V\n\n    iget-object p1, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAnim:Landroid/graphics/drawable/AnimationDrawable;\n\n    if-eqz p1, :cond_1\n\n    invoke-virtual {p0}, Landroid/widget/ImageView;->isShown()Z\n\n    move-result p1\n\n    if-eqz p1, :cond_0\n\n    iget-boolean p1, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAllowAnimation:Z\n\n    if-eqz p1, :cond_0\n\n    iget-object p0, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAnim:Landroid/graphics/drawable/AnimationDrawable;\n\n    invoke-virtual {p0}, Landroid/graphics/drawable/AnimationDrawable;->start()V\n\n    return-void\n\n    :cond_0\n    iget-object p0, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAnim:Landroid/graphics/drawable/AnimationDrawable;\n\n    invoke-virtual {p0}, Landroid/graphics/drawable/AnimationDrawable;->stop()V\n\n    :cond_1\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0003_updateAnim',
        'type':           'method_add',
        'method':         '.method public updateAnim()V',
        'method_name':    'updateAnim',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;', 'iget-boolean v1, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAttached:Z', 'iget-object v1, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAnim:Landroid/graphics/drawable/AnimationDrawable;'],
        'search':         None,
        'replacement':    '.method public updateAnim()V\n    .registers 3\n\n    invoke-virtual {p0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;\n\n    move-result-object v0\n\n    iget-boolean v1, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAttached:Z\n\n    if-eqz v1, :cond_0\n\n    iget-object v1, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAnim:Landroid/graphics/drawable/AnimationDrawable;\n\n    if-eqz v1, :cond_0\n\n    invoke-virtual {v1}, Landroid/graphics/drawable/AnimationDrawable;->stop()V\n\n    :cond_0\n    instance-of v1, v0, Landroid/graphics/drawable/AnimationDrawable;\n\n    if-eqz v1, :cond_2\n\n    check-cast v0, Landroid/graphics/drawable/AnimationDrawable;\n\n    iput-object v0, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAnim:Landroid/graphics/drawable/AnimationDrawable;\n\n    invoke-virtual {p0}, Landroid/widget/ImageView;->isShown()Z\n\n    move-result v0\n\n    if-eqz v0, :cond_1\n\n    iget-boolean v0, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAllowAnimation:Z\n\n    if-eqz v0, :cond_1\n\n    iget-object p0, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAnim:Landroid/graphics/drawable/AnimationDrawable;\n\n    invoke-virtual {p0}, Landroid/graphics/drawable/AnimationDrawable;->start()V\n\n    :cond_1\n    return-void\n\n    :cond_2\n    const/4 v0, 0x0\n\n    iput-object v0, p0, Lcom/android/systemui/statusbar/AnimatedImageView;->mAnim:Landroid/graphics/drawable/AnimationDrawable;\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0004_field__field_public_mHasOv',
        'type':           'field_add',
        'method':         '.field public mHasOverlappingRendering:Z',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field public mHasOverlappingRendering:Z',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added field',
    },
]
