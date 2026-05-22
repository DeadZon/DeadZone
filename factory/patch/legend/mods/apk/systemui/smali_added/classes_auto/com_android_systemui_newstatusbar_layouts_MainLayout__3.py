"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/MainLayout$3.smali'
CLASS_FALLBACK_NAMES = ['MainLayout$3.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class final Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/layouts/MainLayout;->animateHide(Lcom/android/systemui/newstatusbar/layouts/MainLayout;ZLjava/lang/Runnable;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x8
    name = null
.end annotation


# instance fields
.field final synthetic val$runnable:Ljava/lang/Runnable;

.field final synthetic val$view:Lcom/android/systemui/newstatusbar/layouts/MainLayout;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;Ljava/lang/Runnable;)V
    .registers 3

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;->val$view:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    iput-object p2, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;->val$runnable:Ljava/lang/Runnable;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;->val$view:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    const/4 v1, 0x4

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->superSetVisibility(I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;->val$view:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setTranslationX(F)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;->val$runnable:Ljava/lang/Runnable;

    if-eqz v0, :cond_15

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;->val$runnable:Ljava/lang/Runnable;

    invoke-interface {v0}, Ljava/lang/Runnable;->run()V

    :cond_15
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_MainLayout_3',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
