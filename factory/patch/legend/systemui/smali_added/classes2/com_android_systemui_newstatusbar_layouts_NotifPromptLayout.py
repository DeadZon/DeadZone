"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/layouts/NotifPromptLayout.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/layouts/NotifPromptLayout.smali'
CLASS_FALLBACK_NAMES = ['NotifPromptLayout.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_layouts_NotifPromptLayout',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/layouts/NotifPromptLayout;\n.super Lcom/android/systemui/statusbar/views/LimitedSizeFrameLayout;\n\n\n# instance fields\n.field private final TAG:Ljava/lang/String;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 3\n\n    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/views/LimitedSizeFrameLayout;-><init>(Landroid/content/Context;)V\n\n    const-string v0, "Nastya_s"\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotifPromptLayout;->TAG:Ljava/lang/String;\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 4\n\n    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/views/LimitedSizeFrameLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    const-string v0, "Nastya_s"\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotifPromptLayout;->TAG:Ljava/lang/String;\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 5\n\n    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/LimitedSizeFrameLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    const-string v0, "Nastya_s"\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/NotifPromptLayout;->TAG:Ljava/lang/String;\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onViewAdded(Landroid/view/View;)V\n    .registers 6\n\n    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/LimitedSizeFrameLayout;->onViewAdded(Landroid/view/View;)V\n\n    const-string v0, "Nastya_s"\n\n    const-string v1, "onViewAdded: "\n\n    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I\n\n    invoke-virtual {p1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;\n\n    move-result-object v1\n\n    if-eqz v1, :cond_0\n\n    new-instance v2, Ljava/lang/StringBuilder;\n\n    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V\n\n    const-string v3, "onViewAdded: params width = "\n\n    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v2\n\n    iget v3, v1, Landroid/view/ViewGroup$LayoutParams;->width:I\n\n    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;\n\n    move-result-object v2\n\n    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;\n\n    move-result-object v2\n\n    invoke-static {v0, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I\n\n    iget v0, v1, Landroid/view/ViewGroup$LayoutParams;->width:I\n\n    const/4 v2, -0x1\n\n    if-ne v0, v2, :cond_1\n\n    const/4 v0, -0x2\n\n    iput v0, v1, Landroid/view/ViewGroup$LayoutParams;->width:I\n\n    goto :goto_0\n\n    :cond_0\n    const-string v2, "onViewAdded: params = null"\n\n    invoke-static {v0, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I\n\n    :cond_1\n    :goto_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
