"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/TransferMobileLayout.smali'
CLASS_FALLBACK_NAMES = ['TransferMobileLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;
.super Lcom/android/systemui/newstatusbar/layouts/SingleLayout;


# instance fields
.field private mEnableRotation:Z

.field private mPosition:I

.field private observer:Landroid/database/ContentObserver;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method static synthetic access$002(Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;Z)Z
    .registers 2

    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->mEnableRotation:Z

    return p1
.end method

.method private setRotate()V
    .registers 7

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->mEnableRotation:Z

    if-eqz v0, :cond_7

    const/16 v0, 0xb4

    goto :goto_8

    :cond_7
    const/4 v0, 0x0

    :goto_8
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "mobile_group"

    invoke-static {v1, v2}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v2

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->findViewById(I)Landroid/view/View;

    move-result-object v2

    if-eqz v2, :cond_1c

    int-to-float v3, v0

    invoke-virtual {v2, v3}, Landroid/view/View;->setRotationY(F)V

    :cond_1c
    const-string v3, "mobile_container_left"

    invoke-static {v1, v3}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v3

    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->findViewById(I)Landroid/view/View;

    move-result-object v2

    if-eqz v2, :cond_48

    const-string v3, "mobile_type"

    invoke-static {v1, v3}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v3

    invoke-virtual {v2, v3}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v3

    const-string v4, "mobile_left_mobile_inout"

    invoke-static {v1, v4}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v4

    invoke-virtual {v2, v4}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v4

    if-eqz v3, :cond_42

    int-to-float v5, v0

    invoke-virtual {v3, v5}, Landroid/view/View;->setRotationY(F)V

    :cond_42
    if-eqz v4, :cond_48

    int-to-float v5, v0

    invoke-virtual {v4, v5}, Landroid/view/View;->setRotationY(F)V

    :cond_48
    const-string v3, "mobile_container_left_vertical"

    invoke-static {v1, v3}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v3

    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->findViewById(I)Landroid/view/View;

    move-result-object v2

    if-eqz v2, :cond_58

    int-to-float v3, v0

    invoke-virtual {v2, v3}, Landroid/view/View;->setRotationY(F)V

    :cond_58
    const-string v3, "mobile_volte"

    invoke-static {v1, v3}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v3

    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->findViewById(I)Landroid/view/View;

    move-result-object v2

    if-eqz v2, :cond_68

    int-to-float v3, v0

    invoke-virtual {v2, v3}, Landroid/view/View;->setRotationY(F)V

    :cond_68
    const-string v3, "mobile_vowifi"

    invoke-static {v1, v3}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v3

    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->findViewById(I)Landroid/view/View;

    move-result-object v2

    if-eqz v2, :cond_78

    int-to-float v3, v0

    invoke-virtual {v2, v3}, Landroid/view/View;->setRotationY(F)V

    :cond_78
    return-void
.end method


# virtual methods
.method public getRealMeasuredWidth()I
    .registers 5

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->getChildCount()I

    move-result v0

    const/4 v1, 0x0

    if-lez v0, :cond_27

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    if-eqz v0, :cond_27

    invoke-virtual {v0}, Landroid/view/View;->getVisibility()I

    move-result v2

    if-nez v2, :cond_27

    invoke-virtual {v0}, Landroid/view/View;->getWidth()I

    move-result v2

    if-lez v2, :cond_27

    invoke-virtual {v0}, Landroid/view/View;->getAlpha()F

    move-result v2

    const/4 v3, 0x0

    cmpl-float v2, v2, v3

    if-lez v2, :cond_27

    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v1

    return v1

    :cond_27
    return v1
.end method

.method protected onDetachedFromWindow()V
    .registers 3

    goto/32 :goto_23

    nop

    :goto_4
    invoke-virtual {v0, v1}, Landroid/content/ContentResolver;->unregisterContentObserver(Landroid/database/ContentObserver;)V

    :goto_7
    goto/32 :goto_30

    nop

    :goto_b
    if-nez v0, :cond_10

    goto/32 :goto_7

    :cond_10
    goto/32 :goto_1b

    nop

    :goto_14
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->observer:Landroid/database/ContentObserver;

    goto/32 :goto_b

    nop

    :goto_1a
    return-void

    :goto_1b
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto/32 :goto_3b

    nop

    :goto_23
    invoke-super {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->onDetachedFromWindow()V

    goto/32 :goto_14

    nop

    :goto_2a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->observer:Landroid/database/ContentObserver;

    goto/32 :goto_4

    nop

    :goto_30
    const/4 v0, 0x0

    goto/32 :goto_35

    nop

    :goto_35
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->observer:Landroid/database/ContentObserver;

    goto/32 :goto_1a

    nop

    :goto_3b
    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    goto/32 :goto_2a

    nop
.end method

.method protected onFinishInflate()V
    .registers 6

    goto/32 :goto_19

    nop

    :goto_4
    invoke-virtual {v1, v4}, Landroid/database/ContentObserver;->onChange(Z)V

    :goto_7
    goto/32 :goto_4f

    nop

    :goto_b
    new-instance v2, Landroid/os/Handler;

    goto/32 :goto_58

    nop

    :goto_11
    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    goto/32 :goto_2d

    nop

    :goto_19
    invoke-super {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->onFinishInflate()V

    goto/32 :goto_97

    nop

    :goto_20
    const/4 v4, 0x0

    goto/32 :goto_b1

    nop

    :goto_25
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    goto/32 :goto_79

    nop

    :goto_2d
    new-instance v2, Ljava/lang/StringBuilder;

    goto/32 :goto_82

    nop

    :goto_33
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto/32 :goto_3b

    nop

    :goto_3b
    invoke-static {v2}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v2

    goto/32 :goto_43

    nop

    :goto_43
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->observer:Landroid/database/ContentObserver;

    goto/32 :goto_20

    nop

    :goto_49
    const-string v1, "elem_net1"

    goto/32 :goto_be

    nop

    :goto_4f
    return-void

    :goto_50
    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto/32 :goto_b8

    nop

    :goto_58
    invoke-static {}, Landroid/os/Looper;->myLooper()Landroid/os/Looper;

    move-result-object v3

    goto/32 :goto_89

    nop

    :goto_60
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto/32 :goto_33

    nop

    :goto_68
    if-eqz v1, :cond_6d

    goto/32 :goto_7e

    :cond_6d
    goto/32 :goto_a5

    nop

    :goto_71
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_11

    nop

    :goto_79
    if-nez v1, :cond_7e

    goto/32 :goto_7

    :cond_7e
    :goto_7e
    goto/32 :goto_9f

    nop

    :goto_82
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto/32 :goto_50

    nop

    :goto_89
    invoke-direct {v2, v3}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V

    goto/32 :goto_90

    nop

    :goto_90
    invoke-direct {v1, p0, v2}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout$1;-><init>(Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;Landroid/os/Handler;)V

    goto/32 :goto_c6

    nop

    :goto_97
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->getElementName()Ljava/lang/String;

    move-result-object v0

    goto/32 :goto_49

    nop

    :goto_9f
    new-instance v1, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout$1;

    goto/32 :goto_b

    nop

    :goto_a5
    const-string v1, "elem_net2"

    goto/32 :goto_25

    nop

    :goto_ab
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->observer:Landroid/database/ContentObserver;

    goto/32 :goto_4

    nop

    :goto_b1
    invoke-virtual {v1, v2, v4, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_ab

    nop

    :goto_b8
    const-string v3, "_rotate"

    goto/32 :goto_60

    nop

    :goto_be
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    goto/32 :goto_68

    nop

    :goto_c6
    iput-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->observer:Landroid/database/ContentObserver;

    goto/32 :goto_71

    nop
.end method

.method public onViewAdded(Landroid/view/View;)V
    .registers 2

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->onViewAdded(Landroid/view/View;)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->updateRotate()V

    return-void
.end method

.method public onViewRemoved(Landroid/view/View;)V
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->updateRotate()V

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->onViewRemoved(Landroid/view/View;)V

    return-void
.end method

.method public removeAllViews()V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->setRotate()V

    invoke-super {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->removeAllViews()V

    return-void
.end method

.method public setPosition(I)V
    .registers 4

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->getElementName()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "_rotate"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings(Ljava/lang/String;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->mEnableRotation:Z

    iput p1, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->mPosition:I

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->setPosition(I)V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->setRotate()V

    return-void
.end method

.method public updateDrawable()V
    .registers 1

    return-void
.end method

.method public updateRotate()V
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->mPosition:I

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->setPosition(I)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_TransferMobileLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
