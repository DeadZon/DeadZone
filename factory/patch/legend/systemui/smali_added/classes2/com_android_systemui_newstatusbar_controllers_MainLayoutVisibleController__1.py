"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1.smali'
CLASS_FALLBACK_NAMES = ['MainLayoutVisibleController$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_MainLayoutVisi',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onControlStatusChange(Z)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;\n\n    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setControlShow(Z)V\n\n    return-void\n.end method\n\n.method public onExpandStatusChange(Z)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;\n\n    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setExpandShow(Z)V\n\n    return-void\n.end method\n\n.method public onLockScreenStateChange(Z)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;\n\n    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setInLockScreen(Z)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
