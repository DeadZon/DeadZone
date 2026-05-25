"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/ColorTextView.smali'
CLASS_FALLBACK_NAMES = ['ColorTextView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/views/ColorTextView;
.super Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;


# instance fields
.field textData:Lcom/android/systemui/newstatusbar/data/TextData;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/views/ColorTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/views/ColorTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, p3, v0}, Lcom/android/systemui/newstatusbar/views/ColorTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 8

    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    const/4 v0, 0x0

    const-string v1, "settingsKey"

    invoke-interface {p2, v0, v1}, Landroid/util/AttributeSet;->getAttributeValue(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    if-nez v0, :cond_e

    const-string v0, ""

    :cond_e
    new-instance v1, Lcom/android/systemui/newstatusbar/data/TextData;

    invoke-direct {v1, p1, v0}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    const/4 v2, 0x0

    new-array v2, v2, [Ljava/lang/String;

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/data/TextData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v1

    new-instance v2, Lcom/android/systemui/newstatusbar/views/ColorTextView$1;

    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/views/ColorTextView$1;-><init>(Lcom/android/systemui/newstatusbar/views/ColorTextView;)V

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/data/TextData;

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/views/ColorTextView;->textData:Lcom/android/systemui/newstatusbar/data/TextData;

    return-void
.end method


# virtual methods
.method protected getData()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/ColorTextView;->textData:Lcom/android/systemui/newstatusbar/data/TextData;

    goto/32 :goto_a

    nop

    :goto_a
    return-object v0
.end method

.method protected onAttached()V
    .registers 1

    goto/32 :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ColorTextView;->update()V

    goto/32 :goto_4

    nop
.end method

.method protected onDetached()V
    .registers 1

    goto/32 :goto_4

    nop

    :goto_4
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_ColorTextView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
