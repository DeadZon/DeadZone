"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/VoWiFiView.smali'
CLASS_FALLBACK_NAMES = ['VoWiFiView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/views/VoWiFiView;
.super Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/CustomIconController$CallBack;


# instance fields
.field private iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

.field private mIds:I


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;-><init>(Landroid/content/Context;)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/VoWiFiView;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/VoWiFiView;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/VoWiFiView;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    return-void
.end method


# virtual methods
.method protected onAttached()V
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    invoke-super {p0}, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->onAttached()V

    goto/32 :goto_b

    nop

    :goto_b
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/VoWiFiView;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    goto/32 :goto_11

    nop

    :goto_11
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V

    goto/32 :goto_18

    nop

    :goto_18
    return-void
.end method

.method protected onDetached()V
    .registers 2

    goto/32 :goto_12

    nop

    :goto_4
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V

    goto/32 :goto_b

    nop

    :goto_b
    return-void

    :goto_c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/VoWiFiView;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    goto/32 :goto_4

    nop

    :goto_12
    invoke-super {p0}, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->onDetached()V

    goto/32 :goto_c

    nop
.end method

.method public onIconStyleChange()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/VoWiFiView;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    iget v1, p0, Lcom/android/systemui/newstatusbar/views/VoWiFiView;->mIds:I

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->getVoWifiIds(I)I

    move-result v0

    invoke-super {p0, v0}, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->setImageResource(I)V

    return-void
.end method

.method public setImageResource(I)V
    .registers 3

    iput p1, p0, Lcom/android/systemui/newstatusbar/views/VoWiFiView;->mIds:I

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/VoWiFiView;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    if-nez v0, :cond_10

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/VoWiFiView;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    :cond_10
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/VoWiFiView;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->getVoWifiIds(I)I

    move-result v0

    invoke-super {p0, v0}, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->setImageResource(I)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_VoWiFiView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
