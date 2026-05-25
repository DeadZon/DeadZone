"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout$CenterTextView$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setText(Ljava/lang/String;Z)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

.field final synthetic val$animate:Z

.field final synthetic val$text:Ljava/lang/String;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;Ljava/lang/String;Z)V
    .registers 4

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    iput-object p2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;->val$text:Ljava/lang/String;

    iput-boolean p3, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;->val$animate:Z

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;->this$1:Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;->val$text:Ljava/lang/String;

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView$1;->val$animate:Z

    invoke-virtual {v0, v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockLayout$CenterTextView;->setText(Ljava/lang/String;Z)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_ClockLayout_CenterTextView_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
