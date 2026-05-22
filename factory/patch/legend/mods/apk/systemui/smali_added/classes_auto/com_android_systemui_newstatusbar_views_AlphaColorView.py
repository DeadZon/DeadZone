"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/AlphaColorView.smali'
CLASS_FALLBACK_NAMES = ['AlphaColorView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/views/AlphaColorView;
.super Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;


# instance fields
.field iconData:Lcom/android/systemui/newstatusbar/data/IconData;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 7

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const/4 v0, 0x0

    const-string v1, "settingsKey"

    invoke-interface {p2, v0, v1}, Landroid/util/AttributeSet;->getAttributeValue(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    if-nez v0, :cond_e

    const-string v0, ""

    :cond_e
    new-instance v1, Lcom/android/systemui/newstatusbar/data/IconData;

    invoke-direct {v1, p1, v0}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    const/4 v2, 0x0

    new-array v2, v2, [Ljava/lang/String;

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v1

    new-instance v2, Lcom/android/systemui/newstatusbar/views/AlphaColorView$1;

    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView$1;-><init>(Lcom/android/systemui/newstatusbar/views/AlphaColorView;)V

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/data/IconData;

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->iconData:Lcom/android/systemui/newstatusbar/data/IconData;

    return-void
.end method

.method private checkDrawable()V
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    if-eqz v0, :cond_9

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    :cond_9
    return-void
.end method


# virtual methods
.method public getData()Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->iconData:Lcom/android/systemui/newstatusbar/data/IconData;

    return-object v0
.end method

.method protected onAttached()V
    .registers 1

    goto/32 :goto_4

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->update()V

    goto/32 :goto_c

    nop

    :goto_b
    return-void

    :goto_c
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->checkDrawable()V

    goto/32 :goto_b

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
        "id": 'class_add_com_android_systemui_newstatusbar_views_AlphaColorView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
