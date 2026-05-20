"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/netspeed/NetworkSpeedSingle.smali'
CLASS_FALLBACK_NAMES = ['NetworkSpeedSingle.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/netspeed/NetworkSpeedSingle;
.super Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# instance fields
.field private final controller:Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/netspeed/NetworkSpeedSingle;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/netspeed/NetworkSpeedSingle;->controller:Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;

    return-void
.end method


# virtual methods
.method protected getData()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 2

    goto/32 :goto_5

    nop

    :goto_4
    return-object v0

    :goto_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/netspeed/NetworkSpeedSingle;->controller:Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;

    goto/32 :goto_b

    nop

    :goto_b
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->getCurrData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    goto/32 :goto_4

    nop
.end method

.method protected onAttached()V
    .registers 2

    goto/32 :goto_13

    nop

    :goto_4
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_c

    nop

    :goto_b
    return-void

    :goto_c
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/netspeed/NetworkSpeedSingle;->update()V

    goto/32 :goto_b

    nop

    :goto_13
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/netspeed/NetworkSpeedSingle;->controller:Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;

    goto/32 :goto_4

    nop
.end method

.method protected onDetached()V
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/netspeed/NetworkSpeedSingle;->controller:Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;

    goto/32 :goto_a

    nop

    :goto_a
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/NetSpeedColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_11

    nop

    :goto_11
    return-void
.end method

.method public onIconChange()V
    .registers 1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/netspeed/NetworkSpeedSingle;->update()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_netspeed_NetworkSpeedSingle',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
