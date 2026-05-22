"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/ModernStatusBarMobileView.smali'
CLASS_FALLBACK_NAMES = ['ModernStatusBarMobileView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;
.super Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;

# interfaces
.implements Lcom/android/systemui/newstatusbar/policy/ISlots;


# static fields
.field private static final TAG:Ljava/lang/String;


# instance fields
.field private isMove:Z

.field private leftContainer:Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;

.field private mobileGroup:Landroid/view/ViewGroup;

.field private mobileTypeImageView:Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;

.field private simIcon:Lcom/android/systemui/newstatusbar/sim/SimIcon;

.field private slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

.field private slotSim:I


# direct methods
.method static constructor <clinit>()V
    .registers 2

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "Nastya_"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-class v1, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;

    invoke-virtual {v1}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->isMove:Z

    const/4 v0, -0x1

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->slotSim:I

    return-void
.end method

.method private moveSim()V
    .registers 8

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->isMove:Z

    iget v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->slotSim:I

    const/4 v2, -0x1

    if-ne v1, v2, :cond_1a

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-static {v1}, Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;->getInstance(Landroid/content/Context;)Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;

    move-result-object v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->getSubId()I

    move-result v2

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;->getSlot(I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->slotSim:I

    :cond_1a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->simIcon:Lcom/android/systemui/newstatusbar/sim/SimIcon;

    if-eqz v1, :cond_21

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->setStatusBar()V

    :cond_21
    iget v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->slotSim:I

    if-nez v1, :cond_26

    goto :goto_27

    :cond_26
    const/4 v0, 0x0

    :goto_27
    const-class v1, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v1}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    if-eqz v0, :cond_38

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getSim1Group(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;

    move-result-object v2

    goto :goto_3c

    :cond_38
    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getSim2Group(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;

    move-result-object v2

    :goto_3c
    if-eqz v2, :cond_6d

    invoke-virtual {v2}, Landroid/view/ViewGroup;->removeAllViews()V

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->mobileGroup:Landroid/view/ViewGroup;

    invoke-virtual {v3}, Landroid/view/ViewGroup;->getParent()Landroid/view/ViewParent;

    move-result-object v3

    check-cast v3, Landroid/view/ViewGroup;

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->mobileGroup:Landroid/view/ViewGroup;

    invoke-virtual {v3, v4}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    new-instance v4, Landroid/widget/LinearLayout$LayoutParams;

    const/4 v5, -0x2

    invoke-direct {v4, v5, v5}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    const/16 v5, 0x11

    iput v5, v4, Landroid/widget/LinearLayout$LayoutParams;->gravity:I

    iget-object v5, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->mobileGroup:Landroid/view/ViewGroup;

    invoke-virtual {v2, v5, v4}, Landroid/view/ViewGroup;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    iget-object v5, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->mobileGroup:Landroid/view/ViewGroup;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->getVisibility()I

    move-result v6

    invoke-virtual {v5, v6}, Landroid/view/ViewGroup;->setVisibility(I)V

    iget-object v5, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->leftContainer:Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;

    if-eqz v5, :cond_6d

    invoke-virtual {v5}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->setIsStatusBar()V

    :cond_6d
    return-void
.end method


# virtual methods
.method public getTextInPaint()F
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->mobileTypeImageView:Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;

    if-eqz v0, :cond_f

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;->drawable:Lcom/miui/systemui/statusbar/views/MobileTypeDrawable;

    iget-object v0, v0, Lcom/miui/systemui/statusbar/views/MobileTypeDrawable;->mMobileTypeTextPaint:Landroid/graphics/Paint;

    const-string v1, "4G+"

    invoke-virtual {v0, v1}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F

    move-result v0

    return v0

    :cond_f
    const/4 v0, 0x0

    return v0
.end method

.method public onDetachedFromWindow()V
    .registers 6

    invoke-super {p0}, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->onDetachedFromWindow()V

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->isMove:Z

    if-eqz v0, :cond_34

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    if-eqz v0, :cond_34

    iget v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->slotSim:I

    const/4 v1, 0x0

    if-nez v0, :cond_12

    const/4 v0, 0x1

    goto :goto_13

    :cond_12
    move v0, v1

    :goto_13
    const-class v2, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v2}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    if-eqz v0, :cond_24

    invoke-virtual {v2, v3}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getSim1Group(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;

    move-result-object v3

    goto :goto_28

    :cond_24
    invoke-virtual {v2, v3}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getSim2Group(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)Landroid/view/ViewGroup;

    move-result-object v3

    :goto_28
    if-eqz v3, :cond_34

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->mobileGroup:Landroid/view/ViewGroup;

    invoke-virtual {v3, v4}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    const/4 v4, 0x0

    iput-object v4, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->isMove:Z

    :cond_34
    return-void
.end method

.method public onFinishInflate()V
    .registers 5

    invoke-super {p0}, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->onFinishInflate()V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->setClipChildren(Z)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->setClipToPadding(Z)V

    const/4 v1, 0x0

    :goto_b
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->getChildCount()I

    move-result v2

    if-ge v1, v2, :cond_28

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    instance-of v3, v2, Landroid/view/ViewGroup;

    if-eqz v3, :cond_25

    move-object v3, v2

    check-cast v3, Landroid/view/ViewGroup;

    invoke-virtual {v3, v0}, Landroid/view/ViewGroup;->setClipChildren(Z)V

    move-object v3, v2

    check-cast v3, Landroid/view/ViewGroup;

    invoke-virtual {v3, v0}, Landroid/view/ViewGroup;->setClipToPadding(Z)V

    :cond_25
    add-int/lit8 v1, v1, 0x1

    goto :goto_b

    :cond_28
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "mobile_group"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/view/ViewGroup;

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->mobileGroup:Landroid/view/ViewGroup;

    const-string v1, "mobile_signal"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/sim/SimIcon;

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->simIcon:Lcom/android/systemui/newstatusbar/sim/SimIcon;

    const-string v1, "mobile_type"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->mobileTypeImageView:Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;

    const-string v1, "mobile_container_left"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->leftContainer:Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;

    invoke-virtual {v1, p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->setMobileView(Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;)V

    const-string v1, "mobile_left_mobile_inout"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/ImageView;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->mobileTypeImageView:Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->leftContainer:Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;

    invoke-virtual {v2, v3, v1}, Lcom/android/systemui/newstatusbar/sim/MobileTypeImageView;->setLeftContainerAndInOut(Landroid/view/ViewGroup;Landroid/widget/ImageView;)V

    return-void
.end method

.method public setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->moveSim()V

    return-void
.end method

.method public setSubId(I)V
    .registers 4

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->setSubId(I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;->getInstance(Landroid/content/Context;)Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->getSubId()I

    move-result v1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;->getSlot(I)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->slotSim:I

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->simIcon:Lcom/android/systemui/newstatusbar/sim/SimIcon;

    if-eqz v1, :cond_1e

    if-lez v0, :cond_1e

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->setSecondSlot()V

    :cond_1e
    return-void
.end method

.method public setVisibility(I)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/ModernStatusBarMobileView;->mobileGroup:Landroid/view/ViewGroup;

    if-eqz v0, :cond_a

    invoke-virtual {v0, p1}, Landroid/view/ViewGroup;->setVisibility(I)V

    :cond_a
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_ModernStatusBarMobileView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
