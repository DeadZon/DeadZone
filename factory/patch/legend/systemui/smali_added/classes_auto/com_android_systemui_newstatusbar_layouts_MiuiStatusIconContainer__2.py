"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$2.smali'
CLASS_FALLBACK_NAMES = ['MiuiStatusIconContainer$2.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$2;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->onViewAdded(Landroid/view/View;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

.field final synthetic val$view:Landroid/view/View;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;Landroid/view/View;)V
    .registers 3

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$2;->this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

    iput-object p2, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$2;->val$view:Landroid/view/View;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$2;->val$view:Landroid/view/View;

    instance-of v0, v0, Lcom/android/systemui/newstatusbar/policy/ISlots;

    if-eqz v0, :cond_29

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$2;->this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->access$100(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;)Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    move-result-object v0

    if-nez v0, :cond_1c

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$2;->this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->access$000(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;)Ljava/util/ArrayList;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$2;->val$view:Landroid/view/View;

    check-cast v1, Lcom/android/systemui/newstatusbar/policy/ISlots;

    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_29

    :cond_1c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$2;->val$view:Landroid/view/View;

    check-cast v0, Lcom/android/systemui/newstatusbar/policy/ISlots;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$2;->this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

    invoke-static {v1}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->access$100(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;)Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    move-result-object v1

    invoke-interface {v0, v1}, Lcom/android/systemui/newstatusbar/policy/ISlots;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    :cond_29
    :goto_29
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_MiuiStatusIconContainer_2',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
