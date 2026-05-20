"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/OverflowLayout.smali'
CLASS_FALLBACK_NAMES = ['OverflowLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;
.super Lcom/android/keyguard/AlphaOptimizedLinearLayout;

# interfaces
.implements Landroid/view/animation/Animation$AnimationListener;


# static fields
.field private static final LeftAnim:I = -0x1

.field private static final RightAnim:I = 0x1

.field private static final StopAnim:I


# instance fields
.field private directionAnim:I

.field private layoutWidth:I

.field private needAnimation:Z

.field private realWidth:I


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0, p1}, Lcom/android/keyguard/AlphaOptimizedLinearLayout;-><init>(Landroid/content/Context;)V

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->directionAnim:I

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, p3, v0}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 6

    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/keyguard/AlphaOptimizedLinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->directionAnim:I

    return-void
.end method

.method private animToLeft()V
    .registers 6

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->needAnimation:Z

    if-eqz v0, :cond_3b

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->directionAnim:I

    if-nez v0, :cond_3b

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->getRealMeasuredWidth()I

    move-result v0

    new-instance v1, Landroid/view/animation/TranslateAnimation;

    iget v2, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->layoutWidth:I

    sub-int/2addr v2, v0

    int-to-float v2, v2

    const/4 v3, 0x0

    invoke-direct {v1, v3, v2, v3, v3}, Landroid/view/animation/TranslateAnimation;-><init>(FFFF)V

    iget v2, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->layoutWidth:I

    sub-int v2, v0, v2

    mul-int/lit8 v2, v2, 0x1e

    const/16 v3, 0x12c

    if-ge v2, v3, :cond_23

    const-wide/16 v3, 0x2bc

    goto :goto_24

    :cond_23
    int-to-long v3, v2

    :goto_24
    invoke-virtual {v1, v3, v4}, Landroid/view/animation/TranslateAnimation;->setDuration(J)V

    const/4 v3, 0x1

    invoke-virtual {v1, v3}, Landroid/view/animation/TranslateAnimation;->setRepeatCount(I)V

    const/4 v3, 0x2

    invoke-virtual {v1, v3}, Landroid/view/animation/TranslateAnimation;->setRepeatMode(I)V

    invoke-virtual {v1, p0}, Landroid/view/animation/TranslateAnimation;->setAnimationListener(Landroid/view/animation/Animation$AnimationListener;)V

    const/4 v3, -0x1

    iput v3, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->directionAnim:I

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->setAnimation(Landroid/view/animation/Animation;)V

    invoke-virtual {v1}, Landroid/view/animation/TranslateAnimation;->start()V

    :cond_3b
    return-void
.end method

.method private isNotif()Z
    .registers 2

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    instance-of v0, v0, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;

    return v0
.end method


# virtual methods
.method public getRealMeasuredWidth()I
    .registers 7

    const/4 v0, 0x0

    const/4 v1, 0x0

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    move-object v2, v1

    instance-of v1, v1, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;

    if-eqz v1, :cond_13

    move-object v1, v2

    check-cast v1, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/layouts/NotificationIconContainer;->getActualWidth()I

    move-result v1

    return v1

    :cond_13
    const/4 v1, 0x0

    :goto_14
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->getChildCount()I

    move-result v3

    if-ge v1, v3, :cond_39

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v3

    invoke-virtual {v3}, Landroid/view/View;->getVisibility()I

    move-result v4

    const/16 v5, 0x8

    if-eq v4, v5, :cond_36

    nop

    invoke-virtual {v3}, Landroid/view/View;->getMeasuredWidth()I

    move-result v4

    invoke-virtual {v3}, Landroid/view/View;->getPaddingLeft()I

    move-result v5

    add-int/2addr v4, v5

    invoke-virtual {v3}, Landroid/view/View;->getPaddingRight()I

    move-result v5

    add-int/2addr v4, v5

    add-int/2addr v0, v4

    :cond_36
    add-int/lit8 v1, v1, 0x1

    goto :goto_14

    :cond_39
    return v0
.end method

.method public onAnimationEnd(Landroid/view/animation/Animation;)V
    .registers 4

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->directionAnim:I

    const/4 v1, 0x1

    if-ne v0, v1, :cond_b

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->directionAnim:I

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->animToLeft()V

    :cond_b
    return-void
.end method

.method public onAnimationRepeat(Landroid/view/animation/Animation;)V
    .registers 3

    const/4 v0, 0x1

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->directionAnim:I

    return-void
.end method

.method public onAnimationStart(Landroid/view/animation/Animation;)V
    .registers 2

    return-void
.end method

.method public setWidth(I)V
    .registers 5

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->getRealMeasuredWidth()I

    move-result v0

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->isNotif()Z

    move-result v1

    if-eqz v1, :cond_38

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "setWidth: parentW = "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, "  realW = "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, " oldParentW = "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    iget v2, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->layoutWidth:I

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v2, "Alicia_elem"

    invoke-static {v2, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_38
    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->layoutWidth:I

    if-ne p1, v1, :cond_40

    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->realWidth:I

    if-eq v1, v0, :cond_44

    :cond_40
    iput p1, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->layoutWidth:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->realWidth:I

    :cond_44
    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->layoutWidth:I

    const/4 v2, 0x1

    if-ge v1, v0, :cond_4c

    if-eq p1, v2, :cond_4c

    goto :goto_4d

    :cond_4c
    const/4 v2, 0x0

    :goto_4d
    iput-boolean v2, p0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->needAnimation:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->animToLeft()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_OverflowLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
