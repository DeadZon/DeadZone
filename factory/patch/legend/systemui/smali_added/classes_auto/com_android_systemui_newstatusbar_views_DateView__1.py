"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/DateView$1.smali'
CLASS_FALLBACK_NAMES = ['DateView$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/views/DateView$1;
.super Landroid/content/BroadcastReceiver;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/views/DateView;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/views/DateView;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/views/DateView;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/DateView$1;->this$0:Lcom/android/systemui/newstatusbar/views/DateView;

    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V

    return-void
.end method


# virtual methods
.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    .registers 8

    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    move-result-object v0

    const-string v1, "android.intent.action.TIME_TICK"

    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    const-string v2, "android.intent.action.TIMEZONE_CHANGED"

    const-string v3, "my.settings.intent.DATE_FORMAT_CHANGED"

    const-string v4, "android.intent.action.LOCALE_CHANGED"

    if-nez v1, :cond_2c

    invoke-virtual {v3, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_2c

    const-string v1, "android.intent.action.TIME_SET"

    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_2c

    invoke-virtual {v2, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_2c

    invoke-virtual {v4, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_52

    :cond_2c
    invoke-virtual {v4, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_3e

    invoke-virtual {v2, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_3e

    invoke-virtual {v3, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_48

    :cond_3e
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/DateView$1;->this$0:Lcom/android/systemui/newstatusbar/views/DateView;

    new-instance v2, Lcom/android/systemui/newstatusbar/views/DateView$1$1;

    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/views/DateView$1$1;-><init>(Lcom/android/systemui/newstatusbar/views/DateView$1;)V

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/views/DateView;->post(Ljava/lang/Runnable;)Z

    :cond_48
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/DateView$1;->this$0:Lcom/android/systemui/newstatusbar/views/DateView;

    new-instance v2, Lcom/android/systemui/newstatusbar/views/DateView$1$2;

    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/views/DateView$1$2;-><init>(Lcom/android/systemui/newstatusbar/views/DateView$1;)V

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/views/DateView;->post(Ljava/lang/Runnable;)Z

    :cond_52
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_DateView_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
