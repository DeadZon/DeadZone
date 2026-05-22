"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/SecondTick$1.smali'
CLASS_FALLBACK_NAMES = ['SecondTick$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/clock/SecondTick$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/clock/SecondTick;->onTimeChanged()V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/clock/SecondTick;

.field final synthetic val$callBack:Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/clock/SecondTick;Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;)V
    .registers 3

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/SecondTick$1;->this$0:Lcom/android/systemui/newstatusbar/clock/SecondTick;

    iput-object p2, p0, Lcom/android/systemui/newstatusbar/clock/SecondTick$1;->val$callBack:Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/SecondTick$1;->val$callBack:Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;

    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;->secondTick()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_SecondTick_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
