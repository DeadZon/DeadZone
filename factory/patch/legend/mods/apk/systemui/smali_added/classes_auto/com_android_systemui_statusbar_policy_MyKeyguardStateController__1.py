"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/policy/MyKeyguardStateController$1.smali'
CLASS_FALLBACK_NAMES = ['MyKeyguardStateController$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$1;
.super Landroid/os/Handler;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;


# direct methods
.method constructor <init>(Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$1;->this$0:Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;

    invoke-direct {p0}, Landroid/os/Handler;-><init>()V

    return-void
.end method


# virtual methods
.method public handleMessage(Landroid/os/Message;)V
    .registers 5
    .param p1  # Landroid/os/Message;
        .annotation build Landroidx/annotation/NonNull;
        .end annotation
    .end param

    const/4 v0, 0x1

    iget v1, p1, Landroid/os/Message;->what:I

    const/16 v2, 0x65

    if-ne v1, v2, :cond_10

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$1;->this$0:Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;

    iget v2, p1, Landroid/os/Message;->arg1:I

    if-ne v2, v0, :cond_11

    :goto_d
    invoke-static {v1, v0}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->access$000(Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;Z)V

    :cond_10
    return-void

    :cond_11
    const/4 v0, 0x0

    goto :goto_d
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_policy_MyKeyguardStateController_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
