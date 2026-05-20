"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/StatusBarWifiView.smali'
CLASS_FALLBACK_NAMES = ['StatusBarWifiView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/StatusBarWifiView;
.super Lcom/android/systemui/statusbar/StatusBarWifiView;


# instance fields
.field private isStatusBar:Z


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/StatusBarWifiView;-><init>(Landroid/content/Context;)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->isStatusBar:Z

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/StatusBarWifiView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->isStatusBar:Z

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/StatusBarWifiView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->isStatusBar:Z

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 6

    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/statusbar/StatusBarWifiView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->isStatusBar:Z

    return-void
.end method

.method private isStatusbarIcon()Z
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    invoke-interface {v0}, Landroid/view/ViewParent;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    instance-of v0, v0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->isStatusBar:Z

    return v0
.end method

.method private moveWiFi()V
    .registers 1

    return-void
.end method


# virtual methods
.method protected onAttachedToWindow()V
    .registers 2

    goto/32 :goto_d

    nop

    :goto_4
    if-nez v0, :cond_9

    goto/32 :goto_1f

    :cond_9
    goto/32 :goto_1c

    nop

    :goto_d
    invoke-super {p0}, Lcom/android/systemui/statusbar/StatusBarWifiView;->onAttachedToWindow()V

    goto/32 :goto_14

    nop

    :goto_14
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->isStatusbarIcon()Z

    move-result v0

    goto/32 :goto_4

    nop

    :goto_1c
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->moveWiFi()V

    :goto_1f
    goto/32 :goto_23

    nop

    :goto_23
    return-void
.end method

.method public setVisibility(I)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/StatusBarWifiView;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->mWifiGroup:Landroid/widget/FrameLayout;

    invoke-virtual {v0, p1}, Landroid/widget/FrameLayout;->setVisibility(I)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_StatusBarWifiView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
