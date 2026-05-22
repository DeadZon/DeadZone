"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/NotificationLayout.smali'
CLASS_FALLBACK_NAMES = ['NotificationLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/NotificationLayout;
.super Lcom/android/systemui/newstatusbar/layouts/SingleLayout;


# instance fields
.field private layoutListener:Landroid/view/View$OnLayoutChangeListener;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method


# virtual methods
.method public setLayoutListener(Landroid/view/View$OnLayoutChangeListener;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/NotificationLayout;->layoutListener:Landroid/view/View$OnLayoutChangeListener;

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_NotificationLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
