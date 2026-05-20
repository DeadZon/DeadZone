"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1.smali'
CLASS_FALLBACK_NAMES = ['EdgeWindowManager$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_statusbar_phone_MyModifiedUI_EdgeWindow',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1;\n.super Lcom/android/keyguard/KeyguardUpdateMonitorCallback;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;-><init>(Landroid/content/Context;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1;->this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;\n\n    invoke-direct {p0}, Lcom/android/keyguard/KeyguardUpdateMonitorCallback;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onRefreshBatteryInfo(Lcom/miui/charge/MiuiBatteryStatus;)V\n    .registers 4\n\n    invoke-super {p0, p1}, Lcom/android/keyguard/KeyguardUpdateMonitorCallback;->onRefreshBatteryInfo(Lcom/miui/charge/MiuiBatteryStatus;)V\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1;->this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;\n\n    invoke-virtual {p1}, Lcom/miui/charge/MiuiBatteryStatus;->isCharging()Z\n\n    move-result v1\n\n    invoke-static {v0, v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->access$002(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;Z)Z\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1;->this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;\n\n    invoke-static {v0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->access$100(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
