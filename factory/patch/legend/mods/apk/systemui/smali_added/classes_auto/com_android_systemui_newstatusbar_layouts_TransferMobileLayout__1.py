"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/TransferMobileLayout$1.smali'
CLASS_FALLBACK_NAMES = ['TransferMobileLayout$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout$1;
.super Landroid/database/ContentObserver;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->onFinishInflate()V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;Landroid/os/Handler;)V
    .registers 3

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;

    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V

    return-void
.end method


# virtual methods
.method public onChange(Z)V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->getElementName()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, "_rotate"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings(Ljava/lang/String;)Z

    move-result v1

    invoke-static {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->access$002(Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;Z)Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->updateRotate()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_TransferMobileLayout_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
