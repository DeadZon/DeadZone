"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/layouts/MainLayout$3.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/layouts/MainLayout$3.smali'
CLASS_FALLBACK_NAMES = ['MainLayout$3.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_layouts_MainLayout$3',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class final Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/layouts/MainLayout;->animateHide(Lcom/android/systemui/newstatusbar/layouts/MainLayout;ZLjava/lang/Runnable;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x8\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic val$runnable:Ljava/lang/Runnable;\n\n.field final synthetic val$view:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;Ljava/lang/Runnable;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;->val$view:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n    iput-object p2, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;->val$runnable:Ljava/lang/Runnable;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;->val$view:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n    const/4 v1, 0x4\n\n    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->superSetVisibility(I)V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;->val$view:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n    const/4 v1, 0x0\n\n    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setTranslationX(F)V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;->val$runnable:Ljava/lang/Runnable;\n\n    if-eqz v0, :cond_0\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;->val$runnable:Ljava/lang/Runnable;\n\n    invoke-interface {v0}, Ljava/lang/Runnable;->run()V\n\n    :cond_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
