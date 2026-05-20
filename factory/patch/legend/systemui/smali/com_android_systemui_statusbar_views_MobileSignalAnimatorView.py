"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/views/MobileSignalAnimatorView.smali
Patches      : 2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/views/MobileSignalAnimatorView.smali'
CLASS_FALLBACK_NAMES = ['MobileSignalAnimatorView.smali']
CLASS_ANCHORS        = ['invoke-direct/range {v0 .. v6}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;IIILkotlin/jvm/internal/DefaultConstructorMarker;)V', 'invoke-direct/range {v0 .. v6}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;IIILkotlin/jvm/internal/DefaultConstructorMarker;)V', 'invoke-direct/range {v0 .. v6}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;IIILkotlin/jvm/internal/DefaultConstructorMarker;)V', 'invoke-direct {p0, p1, p2, p3, p4}, Landroidx/constraintlayout/widget/ConstraintLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V', 'iput p1, p0, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorView;->islandState:I']

PATCHES = [
    {
        'id':             'p0000_copyView',
        'type':           'method_add',
        'method':         '.method public copyView()Landroid/view/View;',
        'method_name':    'copyView',
        'method_anchors': ['invoke-virtual {p0}, Landroid/view/ViewGroup;->getWidth()I', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getHeight()I', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;'],
        'search':         None,
        'replacement':    '.method public copyView()Landroid/view/View;\n    .registers 6\n\n    invoke-virtual {p0}, Landroid/view/ViewGroup;->getWidth()I\n\n    move-result v0\n\n    const/4 v1, 0x0\n\n    if-eqz v0, :cond_0\n\n    invoke-virtual {p0}, Landroid/view/ViewGroup;->getHeight()I\n\n    move-result v0\n\n    if-eqz v0, :cond_0\n\n    const/4 v0, 0x1\n\n    goto :goto_0\n\n    :cond_0\n    move v0, v1\n\n    :goto_0\n    const/4 v2, 0x0\n\n    if-nez v0, :cond_1\n\n    return-object v2\n\n    :cond_1\n    :try_start_0\n    new-instance v0, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorView$MobileStatusBarFakeView;\n\n    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;\n\n    move-result-object v3\n\n    const/16 v4, 0xe\n\n    invoke-direct {v0, v3, v2, v1, v4}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorView$MobileStatusBarFakeView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V\n    :try_end_0\n    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_1\n\n    :try_start_1\n    invoke-virtual {v0, p0}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorView$MobileStatusBarFakeView;->setOriginView(Landroid/view/View;)V\n    :try_end_1\n    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_0\n\n    return-object v0\n\n    :catch_0\n    move-exception v1\n\n    move-object v2, v0\n\n    goto :goto_1\n\n    :catch_1\n    move-exception v1\n\n    :goto_1\n    invoke-virtual {p0}, Landroid/view/ViewGroup;->getWidth()I\n\n    move-result v0\n\n    invoke-virtual {p0}, Landroid/view/ViewGroup;->getHeight()I\n\n    move-result p0\n\n    const-string v3, "copyView: Exception  ,width = "\n\n    const-string v4, " height = "\n\n    invoke-static {v3, v0, p0, v4}, Landroidx/compose/runtime/external/kotlinx/collections/immutable/internal/ListImplementation$$ExternalSyntheticOutline0;->m(Ljava/lang/String;IILjava/lang/String;)Ljava/lang/String;\n\n    move-result-object p0\n\n    const-string v0, "MobileSignalAnimatorView"\n\n    invoke-static {v0, p0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I\n\n    return-object v2\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0001_hasOverlappingRendering',
        'type':           'method_add',
        'method':         '.method public hasOverlappingRendering()Z',
        'method_name':    'hasOverlappingRendering',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.method public hasOverlappingRendering()Z\n    .registers 1\n\n    const/4 p0, 0x0\n\n    return p0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
]
