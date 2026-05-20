"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/MiuiKeyguardStatusBarView.smali'
CLASS_FALLBACK_NAMES = ['MiuiKeyguardStatusBarView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;
.super Lcom/android/systemui/statusbar/phone/MiuiKeyguardStatusBarView;


# instance fields
.field TAG:Ljava/lang/String;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/phone/MiuiKeyguardStatusBarView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-string v0, "MezologsMiuiKeyguard"

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->TAG:Ljava/lang/String;

    return-void
.end method


# virtual methods
.method public updateKeyguardStatusBarHeight()V
    .registers 5

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-static {v1}, Lcom/android/systemui/util/Utils;->getStatusBarHeaderHeightKeyguard(Landroid/content/Context;)I

    move-result v1

    iput v1, v0, Landroid/view/ViewGroup$LayoutParams;->height:I

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->TAG:Ljava/lang/String;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "updateKeyguardStatusBarHeight: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget v3, v0, Landroid/view/ViewGroup$LayoutParams;->height:I

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    return-void
.end method

.method public updateSystemIconsLayoutParams()V
    .registers 6

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;

    invoke-virtual {v0}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    check-cast v0, Landroid/widget/LinearLayout$LayoutParams;

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->mKeyguardUserSwitcherEnabled:Z

    if-eqz v1, :cond_f

    iget v1, p0, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->mSystemIconsSwitcherHiddenExpandedMargin:I

    goto :goto_10

    :cond_f
    const/4 v1, 0x0

    :goto_10
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;

    instance-of v2, v2, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;

    if-eqz v2, :cond_38

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->getWidth()I

    move-result v2

    div-int/lit8 v2, v2, 0x2

    add-int/lit8 v2, v2, -0x2d

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;

    invoke-virtual {v3}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;->getPaddingEnd()I

    move-result v3

    sub-int/2addr v2, v3

    sub-int/2addr v2, v1

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;

    check-cast v3, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;

    invoke-virtual {v3, v2}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->setMaxWidth(I)V

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;

    const/4 v4, 0x1

    invoke-virtual {v3, v4}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;->setClipChildren(Z)V

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;

    invoke-virtual {v3, v4}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;->setClipToPadding(Z)V

    :cond_38
    invoke-virtual {v0}, Landroid/widget/LinearLayout$LayoutParams;->getMarginEnd()I

    move-result v2

    if-eq v1, v2, :cond_46

    invoke-virtual {v0, v1}, Landroid/widget/LinearLayout$LayoutParams;->setMarginEnd(I)V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/MiuiKeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;

    invoke-virtual {v2, v0}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    :cond_46
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_MiuiKeyguardStatusBarView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
