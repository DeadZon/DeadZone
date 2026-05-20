"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/layouts/TransferMobileLayout$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/layouts/TransferMobileLayout$1.smali'
CLASS_FALLBACK_NAMES = ['TransferMobileLayout$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_layouts_TransferMobileLayo',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout$1;\n.super Landroid/database/ContentObserver;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->onFinishInflate()V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;Landroid/os/Handler;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;\n\n    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onChange(Z)V\n    .registers 5\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;\n\n    new-instance v1, Ljava/lang/StringBuilder;\n\n    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V\n\n    iget-object v2, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;\n\n    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->getElementName()Ljava/lang/String;\n\n    move-result-object v2\n\n    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v1\n\n    const-string v2, "_rotate"\n\n    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v1\n\n    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;\n\n    move-result-object v1\n\n    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings(Ljava/lang/String;)Z\n\n    move-result v1\n\n    invoke-static {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->access$002(Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;Z)Z\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->updateRotate()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
