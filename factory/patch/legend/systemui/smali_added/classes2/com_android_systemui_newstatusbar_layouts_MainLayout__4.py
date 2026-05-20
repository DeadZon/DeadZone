"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/layouts/MainLayout$4.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/layouts/MainLayout$4.smali'
CLASS_FALLBACK_NAMES = ['MainLayout$4.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_layouts_MainLayout$4',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class final Lcom/android/systemui/newstatusbar/layouts/MainLayout$4;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/layouts/MainLayout;->animateShow(Lcom/android/systemui/newstatusbar/layouts/MainLayout;Z)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x8\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic val$view:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$4;->val$view:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$4;->val$view:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n    const/4 v1, 0x0\n\n    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setTranslationX(F)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
