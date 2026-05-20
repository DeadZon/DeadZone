"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/NotificationHeaderDateView$2.smali'
CLASS_FALLBACK_NAMES = ['NotificationHeaderDateView$2.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$2;
.super Ljava/lang/Object;

# interfaces
.implements Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$2;->this$0:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onDataChanged()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$2;->this$0:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->update()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$2;->this$0:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->updateDate()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_NotificationHeaderDateView_2',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
