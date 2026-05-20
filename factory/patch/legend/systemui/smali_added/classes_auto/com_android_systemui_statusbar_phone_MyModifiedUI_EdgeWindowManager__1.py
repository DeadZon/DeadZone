"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1.smali'
CLASS_FALLBACK_NAMES = ['EdgeWindowManager$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1;
.super Lcom/android/keyguard/KeyguardUpdateMonitorCallback;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;-><init>(Landroid/content/Context;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;


# direct methods
.method constructor <init>(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1;->this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;

    invoke-direct {p0}, Lcom/android/keyguard/KeyguardUpdateMonitorCallback;-><init>()V

    return-void
.end method


# virtual methods
.method public onRefreshBatteryInfo(Lcom/miui/charge/MiuiBatteryStatus;)V
    .registers 4

    invoke-super {p0, p1}, Lcom/android/keyguard/KeyguardUpdateMonitorCallback;->onRefreshBatteryInfo(Lcom/miui/charge/MiuiBatteryStatus;)V

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1;->this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;

    invoke-virtual {p1}, Lcom/miui/charge/MiuiBatteryStatus;->isCharging()Z

    move-result v1

    invoke-static {v0, v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->access$002(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;Z)Z

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager$1;->this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;

    invoke-static {v0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->access$100(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_phone_MyModifiedUI_EdgeWindowManager_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
