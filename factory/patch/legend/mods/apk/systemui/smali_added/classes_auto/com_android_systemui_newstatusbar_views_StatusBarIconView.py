"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/StatusBarIconView.smali'
CLASS_FALLBACK_NAMES = ['StatusBarIconView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/views/StatusBarIconView;
.super Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# instance fields
.field private final controller:Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

.field private isStatusIcon:Z


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAnimated;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->isStatusIcon:Z

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    return-void
.end method


# virtual methods
.method public getActualHeight()I
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->isCustColor:Z

    if-eqz v0, :cond_7

    iget v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->curHeight:I

    goto :goto_b

    :cond_7
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->getMeasuredHeight()I

    move-result v0

    :goto_b
    return v0
.end method

.method public getActualWidth()I
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->isCustColor:Z

    if-eqz v0, :cond_7

    iget v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->curWidth:I

    goto :goto_b

    :cond_7
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->getMeasuredWidth()I

    move-result v0

    :goto_b
    return v0
.end method

.method public getData()Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    if-eqz v0, :cond_b

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->isStatusIcon:Z

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->getCurrData(Z)Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    return-object v0

    :cond_b
    const/4 v0, 0x0

    return-object v0
.end method

.method protected onAttached()V
    .registers 3

    goto/32 :goto_4

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    goto/32 :goto_a

    nop

    :goto_a
    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->isStatusIcon:Z

    goto/32 :goto_10

    nop

    :goto_10
    invoke-virtual {v0, p0, v1}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;Z)V

    goto/32 :goto_18

    nop

    :goto_17
    return-void

    :goto_18
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->update()V

    goto/32 :goto_17

    nop
.end method

.method protected onDetached()V
    .registers 3

    goto/32 :goto_12

    nop

    :goto_4
    return-void

    :goto_5
    invoke-virtual {v0, p0, v1}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;Z)V

    goto/32 :goto_4

    nop

    :goto_c
    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->isStatusIcon:Z

    goto/32 :goto_5

    nop

    :goto_12
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    goto/32 :goto_c

    nop
.end method

.method public onIconChange()V
    .registers 1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->update()V

    return-void
.end method

.method public setNotificationIcon()V
    .registers 3

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->isStatusIcon:Z

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->isNeedZoom:Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->isStatusIcon(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)Z

    move-result v0

    if-eqz v0, :cond_13

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/StatusBarIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;

    const/4 v1, 0x1

    invoke-virtual {v0, p0, v1}, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;Z)V

    :cond_13
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_StatusBarIconView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
