"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/MainLayout.smali'
CLASS_FALLBACK_NAMES = ['MainLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/MainLayout;
.super Lcom/android/systemui/statusbar/AlphaOptimizedFrameLayout;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;
    }
.end annotation


# static fields
.field public static final ALPHA_IN:Landroid/view/animation/Interpolator;

.field public static final ALPHA_OUT:Landroid/view/animation/Interpolator;

.field public static TAG:Ljava/lang/String; = null

.field private static final arrangeByPlaces:I = 0x1f6

.field private static final checkMeasuredWidth:I = 0x1f8

.field private static final findNotificationShade:I = 0x1fe

.field private static final hideElements:I = 0x1f5

.field private static final placeCalculation:I = 0x1f9

.field public static final sElementCount:I = 0xb

.field private static final showElements:I = 0x1f4

.field private static final startMove:I = 0x1ff

.field private static final updateAirMode:I = 0x1fd

.field private static final updateFull:I = 0x1f7

.field private static final updateMobileRotate:I = 0x1fa

.field private static final updateNetworkSpeed:I = 0x1fb

.field private static final updateVisibility:I = 0x1fc


# instance fields
.field private algorithm:Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;

.field private blockCalculate:Z

.field private centerEnable:Z

.field private final defSettings:Ljava/lang/String;

.field private final elementController:Lcom/android/systemui/newstatusbar/controllers/ElementController;

.field public final elements:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">;"
        }
    .end annotation
.end field

.field private final elementsBottom:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">;"
        }
    .end annotation
.end field

.field private final elementsTop:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">;"
        }
    .end annotation
.end field

.field private final handler:Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

.field private postLayout:Z

.field private slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

.field private final visibleController:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;


# direct methods
.method static constructor <clinit>()V
    .registers 4

    const/high16 v3, 0x3f800000  # 1.0f

    const/4 v2, 0x0

    const-string v0, "Nastya_element"

    sput-object v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->TAG:Ljava/lang/String;

    new-instance v0, Landroid/view/animation/PathInterpolator;

    const v1, 0x3ecccccd  # 0.4f

    invoke-direct {v0, v1, v2, v3, v3}, Landroid/view/animation/PathInterpolator;-><init>(FFFF)V

    sput-object v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->ALPHA_IN:Landroid/view/animation/Interpolator;

    new-instance v0, Landroid/view/animation/PathInterpolator;

    const v1, 0x3f4ccccd  # 0.8f

    invoke-direct {v0, v2, v2, v1, v3}, Landroid/view/animation/PathInterpolator;-><init>(FFFF)V

    sput-object v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->ALPHA_OUT:Landroid/view/animation/Interpolator;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 8

    const/4 v4, 0x0

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/AlphaOptimizedFrameLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    new-instance v1, Ljava/util/ArrayList;

    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    new-instance v1, Ljava/util/ArrayList;

    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsTop:Ljava/util/ArrayList;

    new-instance v1, Ljava/util/ArrayList;

    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsBottom:Ljava/util/ArrayList;

    new-instance v1, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->handler:Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->visibleController:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;

    iput-boolean v4, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->postLayout:Z

    const-class v1, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v1}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementController:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    const-string v1, "elem_status.2;elem_clock.1;elem_bat.31;elem_net1.12;elem_net2.11;elem_wifi.13;elem_notif.21;elem_speed.32;elem_weather.15;elem_date.14;"

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->defSettings:Ljava/lang/String;

    iput-boolean v4, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->blockCalculate:Z

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementController:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-virtual {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->setMainLayout(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementController:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {p1}, Lcom/android/internal/policy/SystemBarUtils;->getStatusBarHeight(Landroid/content/Context;)I

    move-result v2

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->updateHeight(I)V

    invoke-virtual {p0, v4, v4, v4, v4}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setPadding(IIII)V

    invoke-virtual {p0, v4, v4, v4, v4}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setPaddingRelative(IIII)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementController:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->updateCutoutType()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->updateAlgoritm()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getLayoutTransition()Landroid/animation/LayoutTransition;

    move-result-object v0

    const/4 v1, 0x4

    invoke-virtual {v0, v1}, Landroid/animation/LayoutTransition;->enableTransitionType(I)V

    const-wide/16 v2, 0x1f4

    invoke-virtual {v0, v2, v3}, Landroid/animation/LayoutTransition;->setDuration(J)V

    invoke-virtual {p0, v4}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setClipChildren(Z)V

    invoke-virtual {p0, v4}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setClipToPadding(Z)V

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->showElements()V

    return-void
.end method

.method static synthetic access$100(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->hideElements()V

    return-void
.end method

.method static synthetic access$200(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->checkMeasuredWidth()V

    return-void
.end method

.method static synthetic access$300(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->placeCalculation()V

    return-void
.end method

.method static synthetic access$400(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->updateAirModeInternal()V

    return-void
.end method

.method static synthetic access$500(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->updateElementVisibilityInternal()V

    return-void
.end method

.method public static animateHide(Lcom/android/systemui/newstatusbar/layouts/MainLayout;Z)V
    .registers 3

    const/4 v0, 0x0

    invoke-static {p0, p1, v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->animateHide(Lcom/android/systemui/newstatusbar/layouts/MainLayout;ZLjava/lang/Runnable;)V

    return-void
.end method

.method public static animateHide(Lcom/android/systemui/newstatusbar/layouts/MainLayout;ZLjava/lang/Runnable;)V
    .registers 10

    const/4 v1, 0x0

    if-nez p0, :cond_4

    :goto_3
    return-void

    :cond_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->cancel()V

    if-eqz p1, :cond_1c

    const-wide/16 v2, 0x3c

    sget-object v4, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->ALPHA_OUT:Landroid/view/animation/Interpolator;

    new-instance v5, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;

    invoke-direct {v5, p0, p2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$3;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;Ljava/lang/Runnable;)V

    const/4 v6, 0x0

    move-object v0, p0

    invoke-static/range {v0 .. v6}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->startAnimation(Landroid/view/View;FJLandroid/animation/TimeInterpolator;Ljava/lang/Runnable;Z)V

    goto :goto_3

    :cond_1c
    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setAlpha(F)V

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setTranslationX(F)V

    const/4 v0, 0x4

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->superSetVisibility(I)V

    goto :goto_3
.end method

.method public static animateShow(Lcom/android/systemui/newstatusbar/layouts/MainLayout;Z)V
    .registers 9

    const/4 v6, 0x0

    const/high16 v1, 0x3f800000  # 1.0f

    if-nez p0, :cond_6

    :goto_5
    return-void

    :cond_6
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->cancel()V

    invoke-virtual {p0, v6}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->superSetVisibility(I)V

    if-eqz p1, :cond_20

    const-wide/16 v2, 0x50

    sget-object v4, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->ALPHA_IN:Landroid/view/animation/Interpolator;

    new-instance v5, Lcom/android/systemui/newstatusbar/layouts/MainLayout$4;

    invoke-direct {v5, p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$4;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    move-object v0, p0

    invoke-static/range {v0 .. v6}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->startAnimation(Landroid/view/View;FJLandroid/animation/TimeInterpolator;Ljava/lang/Runnable;Z)V

    goto :goto_5

    :cond_20
    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setAlpha(F)V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setTranslationX(F)V

    goto :goto_5
.end method

.method private checkMeasuredWidth()V
    .registers 4

    const/4 v2, 0x1

    iput-boolean v2, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->blockCalculate:Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->algorithm:Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsTop:Ljava/util/ArrayList;

    invoke-virtual {v0, v1, v2}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->checkMeasuredWidth(Ljava/util/ArrayList;Z)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->algorithm:Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsBottom:Ljava/util/ArrayList;

    const/4 v2, 0x0

    invoke-virtual {v0, v1, v2}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->checkMeasuredWidth(Ljava/util/ArrayList;Z)V

    return-void
.end method

.method private hideElements()V
    .registers 1

    return-void
.end method

.method private placeCalculation()V
    .registers 5

    const/4 v3, 0x0

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->algorithm:Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsTop:Ljava/util/ArrayList;

    const/4 v2, 0x1

    invoke-virtual {v0, v1, v2}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->placeCalculation(Ljava/util/ArrayList;Z)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->algorithm:Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsBottom:Ljava/util/ArrayList;

    invoke-virtual {v0, v1, v3}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->placeCalculation(Ljava/util/ArrayList;Z)V

    iput-boolean v3, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->blockCalculate:Z

    return-void
.end method

.method private sendMaxWidthAfterChange()V
    .registers 4

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_18

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    const/16 v2, 0x7d0

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->setMaxMeasureWidth(I)V

    goto :goto_6

    :cond_18
    return-void
.end method

.method private showElements()V
    .registers 1

    return-void
.end method

.method public static startAnimation(Landroid/view/View;FJLandroid/animation/TimeInterpolator;Ljava/lang/Runnable;Z)V
    .registers 17

    const/high16 v6, 0x41c80000  # 25.0f

    const/4 v1, 0x0

    if-nez p0, :cond_6

    :goto_5
    return-void

    :cond_6
    invoke-virtual {p0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v7

    invoke-virtual {v7, p1}, Landroid/view/ViewPropertyAnimator;->alpha(F)Landroid/view/ViewPropertyAnimator;

    move-result-object v7

    invoke-virtual {v7, p2, p3}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    move-result-object v7

    invoke-virtual {v7, p4}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    move-result-object v7

    invoke-virtual {v7, p5}, Landroid/view/ViewPropertyAnimator;->withEndAction(Ljava/lang/Runnable;)Landroid/view/ViewPropertyAnimator;

    move-result-object v7

    const/4 v8, 0x0

    invoke-virtual {v7, v8}, Landroid/view/ViewPropertyAnimator;->setListener(Landroid/animation/Animator$AnimatorListener;)Landroid/view/ViewPropertyAnimator;

    move-result-object v3

    if-eqz p6, :cond_46

    const/high16 v7, 0x3f800000  # 1.0f

    invoke-static {p1, v7}, Ljava/lang/Float;->compare(FF)I

    move-result v2

    if-nez v2, :cond_4a

    move v0, v6

    :goto_2a
    if-nez v2, :cond_4c

    :goto_2c
    if-nez v2, :cond_4e

    const-wide/16 v4, 0x12c

    :goto_30
    invoke-virtual {p0, v0}, Landroid/view/View;->setTranslationX(F)V

    new-instance v6, Landroid/view/animation/AccelerateDecelerateInterpolator;

    invoke-direct {v6}, Landroid/view/animation/AccelerateDecelerateInterpolator;-><init>()V

    invoke-virtual {v3, v6}, Landroid/view/ViewPropertyAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)Landroid/view/ViewPropertyAnimator;

    const-wide/16 v6, 0x64

    invoke-virtual {v3, v6, v7}, Landroid/view/ViewPropertyAnimator;->setDuration(J)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {v3, v4, v5}, Landroid/view/ViewPropertyAnimator;->setStartDelay(J)Landroid/view/ViewPropertyAnimator;

    invoke-virtual {v3, v1}, Landroid/view/ViewPropertyAnimator;->translationX(F)Landroid/view/ViewPropertyAnimator;

    :cond_46
    invoke-virtual {v3}, Landroid/view/ViewPropertyAnimator;->start()V

    goto :goto_5

    :cond_4a
    move v0, v1

    goto :goto_2a

    :cond_4c
    move v1, v6

    goto :goto_2c

    :cond_4e
    const-wide/16 v4, 0x0

    goto :goto_30
.end method

.method private updateAirModeInternal()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    if-lez v0, :cond_1e

    const-string v0, "elem_net1"

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getElementForName(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->updateDrawable()V

    const-string v0, "elem_net2"

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getElementForName(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;->updateDrawable()V

    :cond_1e
    return-void
.end method

.method private updateElementVisibilityInternal()V
    .registers 4

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_16

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->updateVisibility()V

    goto :goto_6

    :cond_16
    return-void
.end method


# virtual methods
.method public arrangeByPlaces()V
    .registers 13

    const/4 v11, 0x1

    const/4 v10, 0x0

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->handler:Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

    const/16 v8, 0x1f6

    invoke-virtual {v7, v8}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->removeMessages(I)V

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsTop:Ljava/util/ArrayList;

    invoke-virtual {v7}, Ljava/util/ArrayList;->clear()V

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsBottom:Ljava/util/ArrayList;

    invoke-virtual {v7}, Ljava/util/ArrayList;->clear()V

    iput-boolean v10, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->centerEnable:Z

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    invoke-virtual {v7}, Ljava/util/ArrayList;->size()I

    move-result v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getContext()Landroid/content/Context;

    move-result-object v7

    invoke-virtual {v7}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v7

    const-string v8, "status_bar_elem_position"

    invoke-static {v7, v8}, Landroid/provider/Settings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v6

    if-nez v6, :cond_2d

    const-string v6, "elem_status.2;elem_clock.1;elem_bat.31;elem_net1.12;elem_net2.11;elem_wifi.13;elem_notif.21;elem_speed.32;elem_weather.15;elem_date.14;"

    :cond_2d
    const/4 v2, 0x0

    :goto_2e
    if-ge v2, v1, :cond_76

    :try_start_30
    const-string v7, "."

    invoke-virtual {v6, v7}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v7

    add-int/lit8 v7, v7, 0x1

    const-string v8, ";"

    invoke-virtual {v6, v8}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v8

    invoke-virtual {v6, v7, v8}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v7

    invoke-static {v7}, Ljava/lang/Integer;->parseInt(Ljava/lang/String;)I
    :try_end_45
    .catch Ljava/lang/Exception; {:try_start_30 .. :try_end_45} :catch_74

    move-result v5

    if-nez v5, :cond_4a

    iput-boolean v11, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->centerEnable:Z

    :cond_4a
    const-string v7, "."

    invoke-virtual {v6, v7}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v7

    invoke-virtual {v6, v10, v7}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v4

    const-string v7, "elem_notif"

    invoke-virtual {v4, v7}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v7

    if-eqz v7, :cond_5e

    const-string v4, "fullscreen_notification_icon_area"

    :cond_5e
    invoke-virtual {p0, v4}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getElementForName(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-result-object v7

    invoke-virtual {v7, v5}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->setPosition(I)V

    const-string v7, ";"

    invoke-virtual {v6, v7}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v7

    add-int/lit8 v7, v7, 0x1

    invoke-virtual {v6, v7}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v6

    add-int/lit8 v2, v2, 0x1

    goto :goto_2e

    :catch_74
    move-exception v0

    :goto_75
    return-void

    :cond_76
    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    invoke-virtual {v7}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v7

    :goto_7c
    invoke-interface {v7}, Ljava/util/Iterator;->hasNext()Z

    move-result v8

    if-eqz v8, :cond_9c

    invoke-interface {v7}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    invoke-virtual {v3}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I

    move-result v8

    const/16 v9, 0x14

    if-ge v8, v9, :cond_96

    iget-object v8, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsTop:Ljava/util/ArrayList;

    invoke-virtual {v8, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_7c

    :cond_96
    iget-object v8, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsBottom:Ljava/util/ArrayList;

    invoke-virtual {v8, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_7c

    :cond_9c
    iget-boolean v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->centerEnable:Z

    if-eqz v7, :cond_c8

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->isDoubleStatusBar()Z

    move-result v7

    if-eqz v7, :cond_c8

    invoke-virtual {p0, v10}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getElementForPosition(I)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-result-object v3

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementController:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-object v7, v7, Lcom/android/systemui/newstatusbar/controllers/ElementController;->centerElementPosition:Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;

    invoke-virtual {v7}, Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;->ordinal()I

    move-result v7

    if-lez v7, :cond_b9

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsBottom:Ljava/util/ArrayList;

    invoke-virtual {v7, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :cond_b9
    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementController:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-object v7, v7, Lcom/android/systemui/newstatusbar/controllers/ElementController;->centerElementPosition:Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;

    invoke-virtual {v7}, Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;->ordinal()I

    move-result v7

    if-le v7, v11, :cond_c8

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsTop:Ljava/util/ArrayList;

    invoke-virtual {v7, v3}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    :cond_c8
    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsTop:Ljava/util/ArrayList;

    new-instance v8, Lcom/android/systemui/newstatusbar/layouts/MainLayout$1;

    invoke-direct {v8, p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$1;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    invoke-virtual {v7, v8}, Ljava/util/ArrayList;->sort(Ljava/util/Comparator;)V

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsBottom:Ljava/util/ArrayList;

    new-instance v8, Lcom/android/systemui/newstatusbar/layouts/MainLayout$2;

    invoke-direct {v8, p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$2;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    invoke-virtual {v7, v8}, Ljava/util/ArrayList;->sort(Ljava/util/Comparator;)V

    iget-object v7, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementController:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getContext()Landroid/content/Context;

    move-result-object v8

    invoke-static {v8}, Lcom/android/internal/policy/SystemBarUtils;->getStatusBarHeight(Landroid/content/Context;)I

    move-result v8

    invoke-virtual {v7, v8}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->updateHeight(I)V

    iput-boolean v11, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->postLayout:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->sendMaxWidthAfterChange()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->requestLayout()V

    goto :goto_75
.end method

.method public findNotificationShade()V
    .registers 1

    return-void
.end method

.method public fullUpdate()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->handler:Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

    const/16 v1, 0x1f6

    const-wide/16 v2, 0xc8

    invoke-virtual {v0, v1, v2, v3}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->sendEmptyMessageDelayed(IJ)Z

    return-void
.end method

.method public getElementForName(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;
    .registers 5

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->size()I

    move-result v1

    if-nez v1, :cond_a

    const/4 v0, 0x0

    :goto_9
    return-object v0

    :cond_a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :cond_10
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_27

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getElementName()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v2, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_10

    goto :goto_9

    :cond_27
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    const/4 v2, 0x0

    invoke-virtual {v1, v2}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-object v0, v1

    goto :goto_9
.end method

.method public getElementForPosition(I)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;
    .registers 5

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :cond_6
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_19

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I

    move-result v2

    if-ne v2, p1, :cond_6

    :goto_18
    return-object v0

    :cond_19
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    const/4 v2, 0x0

    invoke-virtual {v1, v2}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-object v0, v1

    goto :goto_18
.end method

.method public getMobileGroup()[Landroid/widget/LinearLayout;
    .registers 4

    const/4 v1, 0x2

    new-array v0, v1, [Landroid/widget/LinearLayout;

    const/4 v1, 0x0

    const-string v2, "elem_net1"

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getElementForName(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-result-object v2

    aput-object v2, v0, v1

    const/4 v1, 0x1

    const-string v2, "elem_net2"

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getElementForName(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-result-object v2

    aput-object v2, v0, v1

    return-object v0
.end method

.method public getSim1Layout()Landroid/view/ViewGroup;
    .registers 2

    const-string v0, "elem_net1"

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getElementForName(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-result-object v0

    return-object v0
.end method

.method public getSim2Layout()Landroid/view/ViewGroup;
    .registers 2

    const-string v0, "elem_net2"

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getElementForName(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-result-object v0

    return-object v0
.end method

.method public getSlot()Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    return-object v0
.end method

.method public getSpeedLayout()Landroid/view/ViewGroup;
    .registers 2

    const-string v0, "elem_speed"

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getElementForName(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-result-object v0

    return-object v0
.end method

.method public getWiFiLayout()Landroid/view/ViewGroup;
    .registers 2

    const-string v0, "elem_wifi"

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getElementForName(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-result-object v0

    return-object v0
.end method

.method public isCenterEnable()Z
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->centerEnable:Z

    return v0
.end method

.method public isDoubleStatusBar()Z
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->isOneLineBar()Z

    move-result v0

    if-nez v0, :cond_8

    const/4 v0, 0x1

    :goto_7
    return v0

    :cond_8
    const/4 v0, 0x0

    goto :goto_7
.end method

.method public isOneLineBar()Z
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsTop:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v0

    if-nez v0, :cond_10

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementsBottom:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v0

    if-eqz v0, :cond_12

    :cond_10
    const/4 v0, 0x1

    :goto_11
    return v0

    :cond_12
    const/4 v0, 0x0

    goto :goto_11
.end method

.method protected onAttachedToWindow()V
    .registers 1

    goto/32 :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    invoke-super {p0}, Lcom/android/systemui/statusbar/AlphaOptimizedFrameLayout;->onAttachedToWindow()V

    goto/32 :goto_4

    nop
.end method

.method protected onDetachedFromWindow()V
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    goto/32 :goto_b

    nop

    :goto_a
    return-void

    :goto_b
    invoke-virtual {v0}, Ljava/util/ArrayList;->clear()V

    goto/32 :goto_12

    nop

    :goto_12
    invoke-super {p0}, Lcom/android/systemui/statusbar/AlphaOptimizedFrameLayout;->onDetachedFromWindow()V

    goto/32 :goto_a

    nop
.end method

.method protected onFinishInflate()V
    .registers 9

    goto/32 :goto_56

    nop

    :goto_4
    const/16 v4, 0x1f6

    goto/32 :goto_b2

    nop

    :goto_a
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    goto/32 :goto_d8

    nop

    :goto_10
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    goto/32 :goto_5d

    nop

    :goto_18
    const-wide/16 v6, 0x64

    goto/32 :goto_85

    nop

    :goto_1e
    move-object v3, v1

    goto/32 :goto_a1

    nop

    :goto_23
    invoke-virtual {v3, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :goto_26
    goto/32 :goto_df

    nop

    :goto_2a
    if-eqz v3, :cond_2f

    goto/32 :goto_26

    :cond_2f
    goto/32 :goto_7f

    nop

    :goto_33
    invoke-virtual {v3}, Lcom/android/systemui/newstatusbar/layouts/StatusLayout;->getChild()Landroid/view/View;

    move-result-object v2

    :goto_37
    goto/32 :goto_be

    nop

    :goto_3b
    goto :goto_37

    :goto_3c
    goto/32 :goto_40

    nop

    :goto_40
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->handler:Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

    goto/32 :goto_4

    nop

    :goto_46
    return-void

    :goto_47
    check-cast v3, Lcom/android/systemui/newstatusbar/policy/ISlots;

    goto/32 :goto_a

    nop

    :goto_4d
    if-nez v3, :cond_52

    goto/32 :goto_d4

    :cond_52
    goto/32 :goto_1e

    nop

    :goto_56
    invoke-super {p0}, Lcom/android/systemui/statusbar/AlphaOptimizedFrameLayout;->onFinishInflate()V

    goto/32 :goto_a7

    nop

    :goto_5d
    check-cast v1, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    goto/32 :goto_6b

    nop

    :goto_63
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getChildCount()I

    move-result v3

    goto/32 :goto_c4

    nop

    :goto_6b
    instance-of v3, v1, Lcom/android/systemui/newstatusbar/layouts/StatusLayout;

    goto/32 :goto_4d

    nop

    :goto_71
    invoke-virtual {v4, v5, v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->obtainMessage(ILjava/lang/Object;)Landroid/os/Message;

    move-result-object v4

    goto/32 :goto_18

    nop

    :goto_79
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->handler:Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

    goto/32 :goto_cd

    nop

    :goto_7f
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elements:Ljava/util/ArrayList;

    goto/32 :goto_23

    nop

    :goto_85
    invoke-virtual {v3, v4, v6, v7}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->sendMessageDelayed(Landroid/os/Message;J)Z

    goto/32 :goto_46

    nop

    :goto_8c
    const/4 v0, 0x0

    :goto_8d
    goto/32 :goto_63

    nop

    :goto_91
    if-nez v3, :cond_96

    goto/32 :goto_37

    :cond_96
    goto/32 :goto_e5

    nop

    :goto_9a
    invoke-virtual {v3, v4, v6, v7}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->sendEmptyMessageDelayed(IJ)Z

    goto/32 :goto_79

    nop

    :goto_a1
    check-cast v3, Lcom/android/systemui/newstatusbar/layouts/StatusLayout;

    goto/32 :goto_33

    nop

    :goto_a7
    const/4 v2, 0x0

    goto/32 :goto_8c

    nop

    :goto_ac
    instance-of v3, v1, Lcom/android/systemui/newstatusbar/policy/ISlots;

    goto/32 :goto_91

    nop

    :goto_b2
    const-wide/16 v6, 0x1f4

    goto/32 :goto_9a

    nop

    :goto_b8
    const/16 v5, 0x1ff

    goto/32 :goto_71

    nop

    :goto_be
    instance-of v3, v1, Lcom/android/systemui/newstatusbar/layouts/PromptLayout;

    goto/32 :goto_2a

    nop

    :goto_c4
    if-lt v0, v3, :cond_c9

    goto/32 :goto_3c

    :cond_c9
    goto/32 :goto_10

    nop

    :goto_cd
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->handler:Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

    goto/32 :goto_b8

    nop

    :goto_d3
    goto :goto_8d

    :goto_d4
    goto/32 :goto_ac

    nop

    :goto_d8
    invoke-interface {v3, v4}, Lcom/android/systemui/newstatusbar/policy/ISlots;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    goto/32 :goto_3b

    nop

    :goto_df
    add-int/lit8 v0, v0, 0x1

    goto/32 :goto_d3

    nop

    :goto_e5
    move-object v3, v1

    goto/32 :goto_47

    nop
.end method

.method protected onLayout(ZIIII)V
    .registers 7

    goto/32 :goto_13

    nop

    :goto_4
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->blockCalculate:Z

    goto/32 :goto_a

    nop

    :goto_a
    if-eqz v0, :cond_f

    goto/32 :goto_26

    :cond_f
    goto/32 :goto_2a

    nop

    :goto_13
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->postLayout:Z

    goto/32 :goto_19

    nop

    :goto_19
    if-nez v0, :cond_1e

    goto/32 :goto_26

    :cond_1e
    goto/32 :goto_4

    nop

    :goto_22
    return-void

    :goto_23
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->placeCalculation()V

    :goto_26
    goto/32 :goto_22

    nop

    :goto_2a
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->checkMeasuredWidth()V

    goto/32 :goto_23

    nop
.end method

.method public postUpdateStatusIcons()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->handler:Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

    const/16 v1, 0x1fb

    const-wide/16 v2, 0x7d0

    invoke-virtual {v0, v1, v2, v3}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->sendEmptyMessageDelayed(IJ)Z

    return-void
.end method

.method public resetLongClick()V
    .registers 3

    const/4 v0, 0x0

    :goto_1
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getChildCount()I

    move-result v1

    if-ge v0, v1, :cond_13

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->resetLongClick()V

    add-int/lit8 v0, v0, 0x1

    goto :goto_1

    :cond_13
    return-void
.end method

.method public setPadding(IIII)V
    .registers 6

    const/4 v0, 0x0

    invoke-super {p0, v0, v0, v0, v0}, Lcom/android/systemui/statusbar/AlphaOptimizedFrameLayout;->setPadding(IIII)V

    return-void
.end method

.method public setPaddingRelative(IIII)V
    .registers 6

    const/4 v0, 0x0

    invoke-super {p0, v0, v0, v0, v0}, Lcom/android/systemui/statusbar/AlphaOptimizedFrameLayout;->setPaddingRelative(IIII)V

    return-void
.end method

.method public setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    return-void
.end method

.method public setVisibility(I)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->visibleController:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;

    if-eqz v0, :cond_a

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->visibleController:Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/MainLayoutVisibleController;->setVisibility(I)V

    :goto_9
    return-void

    :cond_a
    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->superSetVisibility(I)V

    goto :goto_9
.end method

.method startMove(Landroid/view/View;)V
    .registers 5

    goto/32 :goto_4

    nop

    :goto_4
    if-nez p1, :cond_9

    goto/32 :goto_3d

    :cond_9
    goto/32 :goto_1b

    nop

    :goto_d
    invoke-static {v1, v2}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    goto/32 :goto_32

    nop

    :goto_15
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    goto/32 :goto_3a

    nop

    :goto_1b
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_42

    nop

    :goto_23
    check-cast v0, Lcom/android/systemui/newstatusbar/policy/ISlots;

    goto/32 :goto_29

    nop

    :goto_29
    if-nez v0, :cond_2e

    goto/32 :goto_3d

    :cond_2e
    goto/32 :goto_15

    nop

    :goto_32
    invoke-virtual {p1, v1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_23

    nop

    :goto_3a
    invoke-interface {v0, v1}, Lcom/android/systemui/newstatusbar/policy/ISlots;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    :goto_3d
    goto/32 :goto_41

    nop

    :goto_41
    return-void

    :goto_42
    const-string v2, "statusIcons"

    goto/32 :goto_d

    nop
.end method

.method public superSetVisibility(I)V
    .registers 2

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AlphaOptimizedFrameLayout;->setVisibility(I)V

    return-void
.end method

.method public updateAirMode()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->handler:Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

    const/16 v1, 0x1fd

    const-wide/16 v2, 0x12c

    invoke-virtual {v0, v1, v2, v3}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->sendEmptyMessageDelayed(IJ)Z

    return-void
.end method

.method public updateAlgoritm()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->algorithm:Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;

    if-eqz v0, :cond_9

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->algorithm:Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->clearCallBackIslandController()V

    :cond_9
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->elementController:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-boolean v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->isHole:Z

    if-eqz v0, :cond_17

    new-instance v0, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    :goto_14
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->algorithm:Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;

    return-void

    :cond_17
    new-instance v0, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    goto :goto_14
.end method

.method public updateElementVisibility()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->handler:Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

    const/16 v1, 0x1fc

    const-wide/16 v2, 0x12c

    invoke-virtual {v0, v1, v2, v3}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->sendEmptyMessageDelayed(IJ)Z

    return-void
.end method

.method public updateMainLayout()V
    .registers 5

    const-wide/16 v2, 0x64

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->handler:Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

    const/16 v1, 0x1f8

    invoke-virtual {v0, v1, v2, v3}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->sendEmptyMessageDelayed(IJ)Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->handler:Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;

    const/16 v1, 0x1f9

    invoke-virtual {v0, v1, v2, v3}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->sendEmptyMessageDelayed(IJ)Z

    return-void
.end method

.method updateStatusIcons()V
    .registers 5

    goto/32 :goto_1d

    nop

    :goto_4
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->requestLayout()V

    :goto_7
    goto/32 :goto_1c

    nop

    :goto_b
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getContext()Landroid/content/Context;

    move-result-object v2

    goto/32 :goto_23

    nop

    :goto_13
    if-nez v0, :cond_18

    goto/32 :goto_7

    :cond_18
    goto/32 :goto_4

    nop

    :goto_1c
    return-void

    :goto_1d
    const-string v2, "elem_status"

    goto/32 :goto_3f

    nop

    :goto_23
    const-string v3, "statusIcons"

    goto/32 :goto_2f

    nop

    :goto_29
    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;

    goto/32 :goto_13

    nop

    :goto_2f
    invoke-static {v2, v3}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v2

    goto/32 :goto_37

    nop

    :goto_37
    invoke-virtual {v1, v2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_29

    nop

    :goto_3f
    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getElementForName(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-result-object v1

    goto/32 :goto_47

    nop

    :goto_47
    if-nez v1, :cond_4c

    goto/32 :goto_7

    :cond_4c
    goto/32 :goto_b

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_MainLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
