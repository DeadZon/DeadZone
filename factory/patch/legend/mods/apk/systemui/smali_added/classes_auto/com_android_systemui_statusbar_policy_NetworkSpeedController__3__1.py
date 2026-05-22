"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/policy/NetworkSpeedController$3$1.smali'
CLASS_FALLBACK_NAMES = ['NetworkSpeedController$3$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;->onUserChanged(ILandroid/content/Context;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$1:Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;


# direct methods
.method constructor <init>(Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3$1;->this$1:Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public final run()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3$1;->this$1:Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;

    iget-object v0, v0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;

    invoke-static {v0}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->access$800(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_policy_NetworkSpeedController_3_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
