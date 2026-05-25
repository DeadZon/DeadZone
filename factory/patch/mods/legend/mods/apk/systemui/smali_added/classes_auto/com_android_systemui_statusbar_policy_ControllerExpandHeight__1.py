"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/policy/ControllerExpandHeight$1.smali'
CLASS_FALLBACK_NAMES = ['ControllerExpandHeight$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;


# direct methods
.method constructor <init>(Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$1;->this$0:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$1;->this$0:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

    const/4 v1, 0x1

    invoke-static {v0, v1}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->access$000(Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;Z)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_policy_ControllerExpandHeight_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
