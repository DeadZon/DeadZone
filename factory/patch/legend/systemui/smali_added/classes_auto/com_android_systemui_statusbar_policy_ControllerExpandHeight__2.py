"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/policy/ControllerExpandHeight$2.smali'
CLASS_FALLBACK_NAMES = ['ControllerExpandHeight$2.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$2;
.super Ljava/lang/Object;

# interfaces
.implements Lcom/android/systemui/statusbar/policy/ConfigurationController$ConfigurationListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;-><init>()V
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

    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$2;->this$0:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onConfigChanged(Landroid/content/res/Configuration;)V
    .registers 5

    const/4 v0, 0x1

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$2;->this$0:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

    iget v2, p1, Landroid/content/res/Configuration;->orientation:I

    if-ne v2, v0, :cond_10

    :goto_7
    invoke-static {v1, v0}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->access$102(Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;Z)Z

    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$2;->this$0:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;

    invoke-static {v0}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->access$200(Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;)V

    return-void

    :cond_10
    const/4 v0, 0x0

    goto :goto_7
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_policy_ControllerExpandHeight_2',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
