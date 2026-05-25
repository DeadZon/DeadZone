"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/ModernStatusBarWifiView.smali'
CLASS_FALLBACK_NAMES = ['ModernStatusBarWifiView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;
.super Lcom/android/systemui/statusbar/pipeline/wifi/ui/view/ModernStatusBarWifiView;

# interfaces
.implements Lcom/android/systemui/newstatusbar/policy/ISlots;


# instance fields
.field private isMove:Z

.field private slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

.field public wifiGroup:Landroid/view/ViewGroup;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/pipeline/wifi/ui/view/ModernStatusBarWifiView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->isMove:Z

    return-void
.end method

.method private moveWifi()V
    .registers 7

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->isMove:Z

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getWiFiGroup(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;

    move-result-object v1

    if-eqz v1, :cond_3b

    invoke-virtual {v1}, Landroid/view/ViewGroup;->removeAllViews()V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->wifiGroup:Landroid/view/ViewGroup;

    invoke-virtual {v2}, Landroid/view/ViewGroup;->getParent()Landroid/view/ViewParent;

    move-result-object v2

    check-cast v2, Landroid/view/ViewGroup;

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->wifiGroup:Landroid/view/ViewGroup;

    invoke-virtual {v2, v3}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    new-instance v3, Landroid/widget/LinearLayout$LayoutParams;

    const/4 v4, -0x2

    invoke-direct {v3, v4, v4}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    const/16 v4, 0x11

    iput v4, v3, Landroid/widget/LinearLayout$LayoutParams;->gravity:I

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->wifiGroup:Landroid/view/ViewGroup;

    invoke-virtual {v1, v4, v3}, Landroid/view/ViewGroup;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->wifiGroup:Landroid/view/ViewGroup;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->getVisibility()I

    move-result v5

    invoke-virtual {v4, v5}, Landroid/view/ViewGroup;->setVisibility(I)V

    :cond_3b
    return-void
.end method


# virtual methods
.method public onDetachedFromWindow()V
    .registers 3

    invoke-super {p0}, Lcom/android/systemui/statusbar/pipeline/wifi/ui/view/ModernStatusBarWifiView;->onDetachedFromWindow()V

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->isMove:Z

    if-eqz v0, :cond_24

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    if-eqz v0, :cond_24

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getWiFiGroup(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;

    move-result-object v0

    if-eqz v0, :cond_1e

    invoke-virtual {v0}, Landroid/view/ViewGroup;->removeAllViews()V

    :cond_1e
    const/4 v1, 0x0

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->isMove:Z

    const/4 v1, 0x0

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    :cond_24
    return-void
.end method

.method public onFinishInflate()V
    .registers 3

    invoke-super {p0}, Lcom/android/systemui/statusbar/pipeline/wifi/ui/view/ModernStatusBarWifiView;->onFinishInflate()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "wifi_group"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->wifiGroup:Landroid/view/ViewGroup;

    return-void
.end method

.method public setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->moveWifi()V

    return-void
.end method

.method public setVisibility(I)V
    .registers 4

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/pipeline/wifi/ui/view/ModernStatusBarWifiView;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarWifiView;->wifiGroup:Landroid/view/ViewGroup;

    if-eqz v0, :cond_11

    const/4 v1, 0x4

    if-ne p1, v1, :cond_d

    const/16 v1, 0x8

    goto :goto_e

    :cond_d
    move v1, p1

    :goto_e
    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->setVisibility(I)V

    :cond_11
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_ModernStatusBarWifiView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
