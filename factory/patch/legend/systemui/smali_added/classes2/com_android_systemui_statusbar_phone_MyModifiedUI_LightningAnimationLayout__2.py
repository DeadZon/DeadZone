"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout$2.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout$2.smali'
CLASS_FALLBACK_NAMES = ['LightningAnimationLayout$2.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_statusbar_phone_MyModifiedUI_LightningA',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout$2;\n.super Lcom/android/keyguard/KeyguardUpdateMonitorCallback;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout$2;->this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout;\n\n    invoke-direct {p0}, Lcom/android/keyguard/KeyguardUpdateMonitorCallback;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onRefreshBatteryInfo(Lcom/miui/charge/MiuiBatteryStatus;)V\n    .registers 4\n\n    invoke-super {p0, p1}, Lcom/android/keyguard/KeyguardUpdateMonitorCallback;->onRefreshBatteryInfo(Lcom/miui/charge/MiuiBatteryStatus;)V\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout$2;->this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout;\n\n    invoke-virtual {p1}, Lcom/miui/charge/MiuiBatteryStatus;->isCharging()Z\n\n    move-result v1\n\n    invoke-static {v0, v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout;->access$102(Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout;Z)Z\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout$2;->this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout;\n\n    invoke-static {v0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout;->access$000(Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningAnimationLayout;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
