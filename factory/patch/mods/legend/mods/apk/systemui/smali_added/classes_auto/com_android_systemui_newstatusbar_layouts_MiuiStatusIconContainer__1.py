"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1.smali'
CLASS_FALLBACK_NAMES = ['MiuiStatusIconContainer$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

.field final synthetic val$slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V
    .registers 3

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

    iput-object p2, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;->val$slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->access$000(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;)Ljava/util/ArrayList;

    move-result-object v0

    monitor-enter v0

    :try_start_7
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

    invoke-static {v1}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->access$000(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;)Ljava/util/ArrayList;

    move-result-object v1

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_11
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_23

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/systemui/newstatusbar/policy/ISlots;

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;->val$slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-interface {v2, v3}, Lcom/android/systemui/newstatusbar/policy/ISlots;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    goto :goto_11

    :cond_23
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

    invoke-static {v1}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->access$000(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;)Ljava/util/ArrayList;

    move-result-object v1

    invoke-virtual {v1}, Ljava/util/ArrayList;->clear()V

    monitor-exit v0

    return-void

    :catchall_2e
    move-exception v1

    monitor-exit v0
    :try_end_30
    .catchall {:try_start_7 .. :try_end_30} :catchall_2e

    throw v1
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_MiuiStatusIconContainer_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
