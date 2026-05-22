"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/ext/ExtTextView$1.smali'
CLASS_FALLBACK_NAMES = ['ExtTextView$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/views/ext/ExtTextView$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->onAttachedToWindow()V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView$1;->this$0:Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView$1;->this$0:Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    if-eqz v0, :cond_d

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView$1;->this$0:Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;->update()V

    :cond_d
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_ext_ExtTextView_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
