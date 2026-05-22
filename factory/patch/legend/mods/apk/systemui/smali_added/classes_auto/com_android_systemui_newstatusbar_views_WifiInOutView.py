"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/WifiInOutView.smali'
CLASS_FALLBACK_NAMES = ['WifiInOutView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/views/WifiInOutView;
.super Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# instance fields
.field protected controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/views/WifiInOutView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/WifiInOutView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    return-void
.end method


# virtual methods
.method public getData()Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/WifiInOutView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    if-nez v0, :cond_e

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/WifiInOutView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    :cond_e
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/WifiInOutView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->getWifiInOutData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    return-object v0
.end method

.method protected onAttached()V
    .registers 2

    goto/32 :goto_c

    nop

    :goto_4
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_b

    nop

    :goto_b
    return-void

    :goto_c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/WifiInOutView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_4

    nop
.end method

.method protected onDetached()V
    .registers 2

    goto/32 :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/WifiInOutView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_b

    nop

    :goto_b
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_4

    nop
.end method

.method public onIconChange()V
    .registers 1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/WifiInOutView;->update()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_WifiInOutView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
