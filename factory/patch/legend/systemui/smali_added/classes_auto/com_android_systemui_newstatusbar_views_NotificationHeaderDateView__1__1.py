"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$1.smali'
CLASS_FALLBACK_NAMES = ['NotificationHeaderDateView$1$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;->onReceive(Landroid/content/Context;Landroid/content/Intent;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$1:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$1;->this$1:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$1;->this$1:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;->this$0:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->access$000(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_NotificationHeaderDateView_1_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
