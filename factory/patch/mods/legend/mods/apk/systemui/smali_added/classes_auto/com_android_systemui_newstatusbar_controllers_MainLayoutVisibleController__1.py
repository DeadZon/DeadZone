"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1.smali'
CLASS_FALLBACK_NAMES = ['MainLayoutVisibleController$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onControlStatusChange(Z)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setControlShow(Z)V

    return-void
.end method

.method public onExpandStatusChange(Z)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setExpandShow(Z)V

    return-void
.end method

.method public onLockScreenStateChange(Z)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setInLockScreen(Z)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_MainLayoutVisibleController_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
