"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/layouts/AnimateElementLayout$2.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/layouts/AnimateElementLayout$2.smali'
CLASS_FALLBACK_NAMES = ['AnimateElementLayout$2.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_layouts_AnimateElementLayo',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$2;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$2;->this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$2;->this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->access$100(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)Z\n\n    move-result v0\n\n    if-eqz v0, :cond_0\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$2;->this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->access$200(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)Landroid/animation/ObjectAnimator;\n\n    move-result-object v0\n\n    if-eqz v0, :cond_0\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$2;->this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->access$200(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)Landroid/animation/ObjectAnimator;\n\n    move-result-object v0\n\n    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->start()V\n\n    :cond_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
