"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/SecondTick$SecondTimerTask.smali'
CLASS_FALLBACK_NAMES = ['SecondTick$SecondTimerTask.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/clock/SecondTick$SecondTimerTask;
.super Ljava/util/TimerTask;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/clock/SecondTick;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = "SecondTimerTask"
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/clock/SecondTick;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/clock/SecondTick;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/SecondTick$SecondTimerTask;->this$0:Lcom/android/systemui/newstatusbar/clock/SecondTick;

    invoke-direct {p0}, Ljava/util/TimerTask;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/SecondTick$SecondTimerTask;->this$0:Lcom/android/systemui/newstatusbar/clock/SecondTick;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/clock/SecondTick;->access$000(Lcom/android/systemui/newstatusbar/clock/SecondTick;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_SecondTick_SecondTimerTask',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
