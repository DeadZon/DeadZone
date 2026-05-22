"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/sim/SimIcon.smali'
CLASS_FALLBACK_NAMES = ['SimIcon.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/sim/SimIcon;
.super Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# static fields
.field private static final TAG:Ljava/lang/String;


# instance fields
.field private final controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

.field public isFirstSlot:Z

.field private isStatusBar:Z


# direct methods
.method static constructor <clinit>()V
    .registers 2

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "Nastya_"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-class v1, Lcom/android/systemui/newstatusbar/sim/SimIcon;

    invoke-virtual {v1}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/systemui/newstatusbar/sim/SimIcon;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/sim/SimIcon;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIcon;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIcon;->isFirstSlot:Z

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIcon;->isStatusBar:Z

    return-void
.end method


# virtual methods
.method public getData()Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIcon;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->getSimData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/sim/SimIcon;->isFirstSlot:Z

    if-nez v1, :cond_18

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/IconData;->copy()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    iget-object v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->additional:Ljava/lang/Object;

    check-cast v1, Ljava/lang/Integer;

    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    :cond_18
    return-object v0
.end method

.method protected onAttached()V
    .registers 2

    goto/32 :goto_c

    nop

    :goto_4
    return-void

    :goto_5
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_4

    nop

    :goto_c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIcon;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_5

    nop
.end method

.method protected onDetached()V
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIcon;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_b

    nop

    :goto_a
    return-void

    :goto_b
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_a

    nop
.end method

.method public onIconChange()V
    .registers 1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->update()V

    return-void
.end method

.method public setSecondSlot()V
    .registers 2

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIcon;->isFirstSlot:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->update()V

    return-void
.end method

.method public setStatusBar()V
    .registers 2

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIcon;->isStatusBar:Z

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_sim_SimIcon',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
