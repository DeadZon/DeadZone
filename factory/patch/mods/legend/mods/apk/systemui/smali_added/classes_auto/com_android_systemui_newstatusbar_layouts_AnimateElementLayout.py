"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/AnimateElementLayout.smali'
CLASS_FALLBACK_NAMES = ['AnimateElementLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;
.super Lcom/android/keyguard/AlphaOptimizedLinearLayout;


# instance fields
.field private animator:Landroid/animation/ObjectAnimator;

.field private isOn:Z

.field private mAnimType:I

.field private mDuration:I

.field private mStartDelay:I

.field private mTypeAnim:I

.field private mTypeInterpolator:Landroid/animation/TimeInterpolator;

.field private final startRunable:Ljava/lang/Runnable;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/keyguard/AlphaOptimizedLinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    new-instance v0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$2;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$2;-><init>(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->startRunable:Ljava/lang/Runnable;

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)Ljava/lang/Runnable;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->startRunable:Ljava/lang/Runnable;

    return-object v0
.end method

.method static synthetic access$100(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)Z
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->isOn:Z

    return v0
.end method

.method static synthetic access$200(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)Landroid/animation/ObjectAnimator;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->animator:Landroid/animation/ObjectAnimator;

    return-object v0
.end method

.method static synthetic access$300(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)I
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->mAnimType:I

    return v0
.end method

.method static synthetic access$400(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)I
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->mStartDelay:I

    return v0
.end method

.method static synthetic access$500(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->resetView()V

    return-void
.end method

.method private getAllAnim()Landroid/animation/ObjectAnimator;
    .registers 11

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->getHeight()I

    move-result v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->getWidth()I

    move-result v2

    int-to-float v3, v2

    const/high16 v4, 0x40000000  # 2.0f

    div-float/2addr v3, v4

    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setPivotX(F)V

    int-to-float v3, v1

    div-float/2addr v3, v4

    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setPivotY(F)V

    iget v3, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->mTypeAnim:I

    const/4 v4, 0x0

    const/4 v5, 0x1

    const/4 v6, 0x4

    const/4 v7, 0x2

    const/4 v8, 0x0

    const/4 v9, 0x3

    packed-switch v3, :pswitch_data_1a2

    sget-object v3, Landroid/view/View;->ALPHA:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_1be

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto/16 :goto_16a

    :pswitch_34  #0xc
    int-to-float v3, v1

    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setPivotX(F)V

    sget-object v3, Landroid/view/View;->ROTATION:Landroid/util/Property;

    const/16 v4, 0xc

    new-array v4, v4, [F

    fill-array-data v4, :array_1c8

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto/16 :goto_16a

    :pswitch_4a  #0xb
    sget-object v3, Landroid/view/View;->ROTATION:Landroid/util/Property;

    new-array v4, v7, [F

    fill-array-data v4, :array_1e4

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto/16 :goto_16a

    :pswitch_5a  #0xa
    sget-object v3, Landroid/view/View;->SCALE_X:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_1ec

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v3, Landroid/view/View;->SCALE_Y:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_1f6

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v3, Landroid/view/View;->ROTATION:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_200

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto/16 :goto_16a

    :pswitch_86  #0x9
    sget-object v3, Landroid/view/View;->ROTATION:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_20a

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v3, Landroid/view/View;->SCALE_X:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_214

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v3, Landroid/view/View;->SCALE_Y:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_21e

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto/16 :goto_16a

    :pswitch_b2  #0x8
    sget-object v3, Landroid/view/View;->SCALE_X:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_228

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v3, Landroid/view/View;->SCALE_Y:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_232

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto/16 :goto_16a

    :pswitch_d0  #0x7
    sget-object v3, Landroid/view/View;->SCALE_X:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_23c

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v3, Landroid/view/View;->SCALE_Y:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_246

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto/16 :goto_16a

    :pswitch_ee  #0x6
    invoke-virtual {p0, v8}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setPivotX(F)V

    invoke-virtual {p0, v8}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setPivotY(F)V

    sget-object v3, Landroid/view/View;->ROTATION_X:Landroid/util/Property;

    new-array v4, v6, [F

    fill-array-data v4, :array_250

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_16a

    :pswitch_103  #0x5
    invoke-virtual {p0, v8}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setPivotX(F)V

    invoke-virtual {p0, v8}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setPivotY(F)V

    sget-object v3, Landroid/view/View;->ROTATION_Y:Landroid/util/Property;

    new-array v4, v6, [F

    fill-array-data v4, :array_25c

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_16a

    :pswitch_118  #0x4
    sget-object v3, Landroid/view/View;->ROTATION_Y:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_268

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_16a

    :pswitch_127  #0x3
    sget-object v3, Landroid/view/View;->ROTATION_X:Landroid/util/Property;

    new-array v4, v9, [F

    fill-array-data v4, :array_272

    invoke-static {v3, v4}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_16a

    :pswitch_136  #0x2
    sget-object v3, Landroid/view/View;->TRANSLATION_Y:Landroid/util/Property;

    new-array v6, v6, [F

    aput v8, v6, v4

    div-int/lit8 v4, v1, 0x2

    int-to-float v4, v4

    aput v4, v6, v5

    neg-int v4, v1

    div-int/2addr v4, v7

    int-to-float v4, v4

    aput v4, v6, v7

    aput v8, v6, v9

    invoke-static {v3, v6}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_16a

    :pswitch_150  #0x1
    sget-object v3, Landroid/view/View;->TRANSLATION_X:Landroid/util/Property;

    new-array v6, v6, [F

    aput v8, v6, v4

    div-int/lit8 v4, v2, 0x2

    int-to-float v4, v4

    aput v4, v6, v5

    neg-int v4, v2

    div-int/2addr v4, v7

    int-to-float v4, v4

    aput v4, v6, v7

    aput v8, v6, v9

    invoke-static {v3, v6}, Landroid/animation/PropertyValuesHolder;->ofFloat(Landroid/util/Property;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    nop

    :goto_16a
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v3

    new-array v3, v3, [Landroid/animation/PropertyValuesHolder;

    const/4 v4, 0x0

    :goto_171
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v5

    if-ge v4, v5, :cond_182

    invoke-virtual {v0, v4}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v5

    check-cast v5, Landroid/animation/PropertyValuesHolder;

    aput-object v5, v3, v4

    add-int/lit8 v4, v4, 0x1

    goto :goto_171

    :cond_182
    new-instance v4, Landroid/animation/ObjectAnimator;

    invoke-direct {v4}, Landroid/animation/ObjectAnimator;-><init>()V

    invoke-virtual {v4, p0}, Landroid/animation/ObjectAnimator;->setTarget(Ljava/lang/Object;)V

    invoke-virtual {v4, v3}, Landroid/animation/ObjectAnimator;->setValues([Landroid/animation/PropertyValuesHolder;)V

    iget v5, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->mDuration:I

    int-to-long v5, v5

    invoke-virtual {v4, v5, v6}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    iget-object v5, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->mTypeInterpolator:Landroid/animation/TimeInterpolator;

    invoke-virtual {v4, v5}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V

    new-instance v5, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$1;

    invoke-direct {v5, p0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$1;-><init>(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)V

    invoke-virtual {v4, v5}, Landroid/animation/ObjectAnimator;->addListener(Landroid/animation/Animator$AnimatorListener;)V

    return-object v4

    nop

    :pswitch_data_1a2
    .packed-switch 0x1
        :pswitch_150  #00000001
        :pswitch_136  #00000002
        :pswitch_127  #00000003
        :pswitch_118  #00000004
        :pswitch_103  #00000005
        :pswitch_ee  #00000006
        :pswitch_d0  #00000007
        :pswitch_b2  #00000008
        :pswitch_86  #00000009
        :pswitch_5a  #0000000a
        :pswitch_4a  #0000000b
        :pswitch_34  #0000000c
    .end packed-switch

    :array_1be
    .array-data 4
        0x3f800000  # 1.0f
        0x0
        0x3f800000  # 1.0f
    .end array-data

    :array_1c8
    .array-data 4
        0x0
        0x41200000  # 10.0f
        -0x3ee00000  # -10.0f
        0x41f00000  # 30.0f
        -0x3e100000  # -30.0f
        0x42340000  # 45.0f
        -0x3dcc0000  # -45.0f
        0x41f00000  # 30.0f
        -0x3e100000  # -30.0f
        0x41200000  # 10.0f
        -0x3ee00000  # -10.0f
        0x0
    .end array-data

    :array_1e4
    .array-data 4
        0x0
        0x43b40000  # 360.0f
    .end array-data

    :array_1ec
    .array-data 4
        0x3f800000  # 1.0f
        0x40000000  # 2.0f
        0x3f800000  # 1.0f
    .end array-data

    :array_1f6
    .array-data 4
        0x3f800000  # 1.0f
        0x40000000  # 2.0f
        0x3f800000  # 1.0f
    .end array-data

    :array_200
    .array-data 4
        0x0
        0x43b40000  # 360.0f
        0x0
    .end array-data

    :array_20a
    .array-data 4
        0x0
        0x43b40000  # 360.0f
        0x0
    .end array-data

    :array_214
    .array-data 4
        0x3f800000  # 1.0f
        0x0
        0x3f800000  # 1.0f
    .end array-data

    :array_21e
    .array-data 4
        0x3f800000  # 1.0f
        0x0
        0x3f800000  # 1.0f
    .end array-data

    :array_228
    .array-data 4
        0x3f800000  # 1.0f
        0x3dcccccd  # 0.1f
        0x3f800000  # 1.0f
    .end array-data

    :array_232
    .array-data 4
        0x3f800000  # 1.0f
        0x3dcccccd  # 0.1f
        0x3f800000  # 1.0f
    .end array-data

    :array_23c
    .array-data 4
        0x3f800000  # 1.0f
        0x40000000  # 2.0f
        0x3f800000  # 1.0f
    .end array-data

    :array_246
    .array-data 4
        0x3f800000  # 1.0f
        0x40000000  # 2.0f
        0x3f800000  # 1.0f
    .end array-data

    :array_250
    .array-data 4
        0x0
        0x42960000  # 75.0f
        -0x3d6a0000  # -75.0f
        0x0
    .end array-data

    :array_25c
    .array-data 4
        0x0
        0x42960000  # 75.0f
        -0x3d6a0000  # -75.0f
        0x0
    .end array-data

    :array_268
    .array-data 4
        0x0
        0x43340000  # 180.0f
        0x0
    .end array-data

    :array_272
    .array-data 4
        0x0
        0x43340000  # 180.0f
        0x0
    .end array-data
.end method

.method private getInterpolator(I)Landroid/animation/TimeInterpolator;
    .registers 4

    const/4 v0, 0x1

    if-eq p1, v0, :cond_2f

    const/4 v0, 0x2

    if-eq p1, v0, :cond_29

    const/4 v0, 0x3

    if-eq p1, v0, :cond_23

    const/4 v0, 0x4

    if-eq p1, v0, :cond_1d

    const/4 v0, 0x5

    if-eq p1, v0, :cond_15

    new-instance v0, Landroid/view/animation/AccelerateInterpolator;

    invoke-direct {v0}, Landroid/view/animation/AccelerateInterpolator;-><init>()V

    goto :goto_35

    :cond_15
    new-instance v0, Landroid/view/animation/CycleInterpolator;

    const/high16 v1, 0x3f800000  # 1.0f

    invoke-direct {v0, v1}, Landroid/view/animation/CycleInterpolator;-><init>(F)V

    goto :goto_35

    :cond_1d
    new-instance v0, Landroid/view/animation/OvershootInterpolator;

    invoke-direct {v0}, Landroid/view/animation/OvershootInterpolator;-><init>()V

    goto :goto_35

    :cond_23
    new-instance v0, Landroid/view/animation/BounceInterpolator;

    invoke-direct {v0}, Landroid/view/animation/BounceInterpolator;-><init>()V

    goto :goto_35

    :cond_29
    new-instance v0, Landroid/view/animation/AccelerateDecelerateInterpolator;

    invoke-direct {v0}, Landroid/view/animation/AccelerateDecelerateInterpolator;-><init>()V

    goto :goto_35

    :cond_2f
    new-instance v0, Landroid/view/animation/DecelerateInterpolator;

    invoke-direct {v0}, Landroid/view/animation/DecelerateInterpolator;-><init>()V

    nop

    :goto_35
    return-object v0
.end method

.method private resetView()V
    .registers 3

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setRotationX(F)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setRotationY(F)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setRotation(F)V

    const/high16 v1, 0x3f800000  # 1.0f

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setScaleX(F)V

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setScaleY(F)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setTranslationX(F)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setTranslationY(F)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setTranslationZ(F)V

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->setAlpha(F)V

    return-void
.end method

.method private updateSettings()V
    .registers 2

    const-string v0, "element_anim_duration"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->mDuration:I

    const-string v0, "element_anim_style"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->mTypeAnim:I

    const-string v0, "element_anim_start_delay"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->mStartDelay:I

    const-string v0, "element_anim_interpolator"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->getInterpolator(I)Landroid/animation/TimeInterpolator;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->mTypeInterpolator:Landroid/animation/TimeInterpolator;

    const-string v0, "element_anim_enable"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->mAnimType:I

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->isOn:Z

    return-void
.end method


# virtual methods
.method protected onAttachedToWindow()V
    .registers 1

    goto/32 :goto_c

    nop

    :goto_4
    return-void

    :goto_5
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->updateSettings()V

    goto/32 :goto_4

    nop

    :goto_c
    invoke-super {p0}, Lcom/android/keyguard/AlphaOptimizedLinearLayout;->onAttachedToWindow()V

    goto/32 :goto_5

    nop
.end method

.method protected onDetachedFromWindow()V
    .registers 1

    goto/32 :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    invoke-super {p0}, Lcom/android/keyguard/AlphaOptimizedLinearLayout;->onDetachedFromWindow()V

    goto/32 :goto_4

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_AnimateElementLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
