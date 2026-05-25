"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/ElementBgLayout.smali'
CLASS_FALLBACK_NAMES = ['ElementBgLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public abstract Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;
.super Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;
    }
.end annotation


# instance fields
.field private background:Landroid/graphics/drawable/GradientDrawable;

.field public bottomMargin:I

.field public leftMargin:I

.field public leftPadd:I

.field private observer:Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;

.field public rightMargin:I

.field public rightPadd:I

.field public topMargin:I


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->leftMargin:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->rightMargin:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->topMargin:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->bottomMargin:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->leftPadd:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->rightPadd:I

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->setClipChildren(Z)V

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;)Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->observer:Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;

    return-object v0
.end method

.method static synthetic access$002(Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;)Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->observer:Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;

    return-object p1
.end method

.method static synthetic access$100(Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->makeBackground()V

    return-void
.end method

.method static synthetic access$200(Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->updateMargins()V

    return-void
.end method

.method private makeBackground()V
    .registers 11

    new-instance v0, Landroid/graphics/drawable/GradientDrawable;

    invoke-direct {v0}, Landroid/graphics/drawable/GradientDrawable;-><init>()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getElementName()Ljava/lang/String;

    move-result-object v1

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    sget-object v3, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->strokeWidthKey:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v2

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    sget-object v4, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->strokeColorKey:Ljava/lang/String;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v3}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v3

    invoke-virtual {v0, v2, v3}, Landroid/graphics/drawable/GradientDrawable;->setStroke(II)V

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    sget-object v3, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->leftPaddKey:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v2

    iput v2, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->leftPadd:I

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    sget-object v3, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->rightPaddKey:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v2

    iput v2, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->rightPadd:I

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    sget-object v3, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->firstColorKey:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v2

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    sget-object v4, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->secondColorKey:Ljava/lang/String;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v3}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v3

    const/4 v4, 0x1

    const/4 v5, 0x0

    const/4 v6, 0x2

    if-eqz v3, :cond_a9

    new-array v7, v6, [I

    aput v2, v7, v5

    aput v3, v7, v4

    invoke-virtual {v0, v7}, Landroid/graphics/drawable/GradientDrawable;->setColors([I)V

    goto :goto_ac

    :cond_a9
    invoke-virtual {v0, v2}, Landroid/graphics/drawable/GradientDrawable;->setColor(I)V

    :goto_ac
    sget-object v7, Landroid/graphics/drawable/GradientDrawable$Orientation;->TL_BR:Landroid/graphics/drawable/GradientDrawable$Orientation;

    invoke-virtual {v0, v7}, Landroid/graphics/drawable/GradientDrawable;->setOrientation(Landroid/graphics/drawable/GradientDrawable$Orientation;)V

    const/16 v7, 0x8

    new-array v7, v7, [F

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v8, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v8

    sget-object v9, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->LT_cornerKey:Ljava/lang/String;

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v8

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-static {v8}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v8

    int-to-float v8, v8

    aput v8, v7, v5

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    sget-object v8, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->LT_cornerKey:Ljava/lang/String;

    invoke-virtual {v5, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v5}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v5

    int-to-float v5, v5

    aput v5, v7, v4

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    sget-object v5, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->RT_cornerKey:Ljava/lang/String;

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v4}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v4

    int-to-float v4, v4

    aput v4, v7, v6

    const/4 v4, 0x3

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    sget-object v6, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->RT_cornerKey:Ljava/lang/String;

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v5}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v5

    int-to-float v5, v5

    aput v5, v7, v4

    const/4 v4, 0x4

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    sget-object v6, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->RB_cornerKey:Ljava/lang/String;

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v5}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v5

    int-to-float v5, v5

    aput v5, v7, v4

    const/4 v4, 0x5

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    sget-object v6, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->RB_cornerKey:Ljava/lang/String;

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v5}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v5

    int-to-float v5, v5

    aput v5, v7, v4

    const/4 v4, 0x6

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    sget-object v6, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->LB_cornerKey:Ljava/lang/String;

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v5}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v5

    int-to-float v5, v5

    aput v5, v7, v4

    const/4 v4, 0x7

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    sget-object v6, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->LB_cornerKey:Ljava/lang/String;

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v5}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v5

    int-to-float v5, v5

    aput v5, v7, v4

    invoke-virtual {v0, v7}, Landroid/graphics/drawable/GradientDrawable;->setCornerRadii([F)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->background:Landroid/graphics/drawable/GradientDrawable;

    return-void
.end method

.method private updateMargins()V
    .registers 4

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getElementName()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    sget-object v1, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->leftMarginKey:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->leftMargin:I

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getElementName()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    sget-object v1, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->rightMarginKey:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->rightMargin:I

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getElementName()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    sget-object v1, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->topMarginKey:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->topMargin:I

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getElementName()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    sget-object v1, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->bottomMarginKey:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->bottomMargin:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getChild()Landroid/view/View;

    move-result-object v0

    if-eqz v0, :cond_98

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getChild()Landroid/view/View;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    instance-of v1, v0, Landroid/view/ViewGroup$MarginLayoutParams;

    if-eqz v1, :cond_98

    move-object v1, v0

    check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;

    iget v2, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->leftMargin:I

    iput v2, v1, Landroid/view/ViewGroup$MarginLayoutParams;->leftMargin:I

    iget v2, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->rightMargin:I

    iput v2, v1, Landroid/view/ViewGroup$MarginLayoutParams;->rightMargin:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getChild()Landroid/view/View;

    move-result-object v2

    invoke-virtual {v2, v1}, Landroid/view/View;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    :cond_98
    return-void
.end method


# virtual methods
.method public addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V
    .registers 7

    invoke-super {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V

    new-instance v0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$2;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$2;-><init>(Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;)V

    const-wide/16 v1, 0x12c

    invoke-virtual {p0, v0, v1, v2}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void
.end method

.method protected dispatchDraw(Landroid/graphics/Canvas;)V
    .registers 9

    goto/32 :goto_9

    nop

    :goto_4
    sub-int/2addr v5, v6

    goto/32 :goto_72

    nop

    :goto_9
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->background:Landroid/graphics/drawable/GradientDrawable;

    goto/32 :goto_8d

    nop

    :goto_f
    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    goto/32 :goto_dd

    nop

    :goto_16
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->background:Landroid/graphics/drawable/GradientDrawable;

    goto/32 :goto_1c

    nop

    :goto_1c
    invoke-virtual {v2, v1}, Landroid/graphics/drawable/GradientDrawable;->setBounds(Landroid/graphics/Rect;)V

    goto/32 :goto_32

    nop

    :goto_23
    iget v3, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->rightMargin:I

    goto/32 :goto_d8

    nop

    :goto_29
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getWidth()I

    move-result v2

    goto/32 :goto_23

    nop

    :goto_31
    return-void

    :goto_32
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->background:Landroid/graphics/drawable/GradientDrawable;

    goto/32 :goto_7f

    nop

    :goto_38
    iget v5, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->rightPadd:I

    goto/32 :goto_53

    nop

    :goto_3e
    new-instance v1, Landroid/graphics/Rect;

    goto/32 :goto_c7

    nop

    :goto_44
    if-gt v0, v1, :cond_49

    goto/32 :goto_82

    :cond_49
    goto/32 :goto_3e

    nop

    :goto_4d
    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->rightMargin:I

    goto/32 :goto_9e

    nop

    :goto_53
    sub-int/2addr v4, v5

    goto/32 :goto_a3

    nop

    :goto_58
    add-int/lit8 v3, v3, 0x32

    goto/32 :goto_b3

    nop

    :goto_5e
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getWidth()I

    move-result v0

    goto/32 :goto_6c

    nop

    :goto_66
    iget v6, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->bottomMargin:I

    goto/32 :goto_4

    nop

    :goto_6c
    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->leftMargin:I

    goto/32 :goto_cd

    nop

    :goto_72
    invoke-direct {v1, v2, v3, v4, v5}, Landroid/graphics/Rect;-><init>(IIII)V

    goto/32 :goto_16

    nop

    :goto_79
    const/16 v1, -0x32

    goto/32 :goto_29

    nop

    :goto_7f
    invoke-virtual {v2, p1}, Landroid/graphics/drawable/GradientDrawable;->draw(Landroid/graphics/Canvas;)V

    :goto_82
    goto/32 :goto_f

    nop

    :goto_86
    invoke-virtual {p1}, Landroid/graphics/Canvas;->restore()V

    goto/32 :goto_31

    nop

    :goto_8d
    if-nez v0, :cond_92

    goto/32 :goto_82

    :cond_92
    goto/32 :goto_5e

    nop

    :goto_96
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getWidth()I

    move-result v4

    goto/32 :goto_38

    nop

    :goto_9e
    sub-int/2addr v0, v1

    goto/32 :goto_d2

    nop

    :goto_a3
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getHeight()I

    move-result v5

    goto/32 :goto_66

    nop

    :goto_ab
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getHeight()I

    move-result v3

    goto/32 :goto_58

    nop

    :goto_b3
    invoke-virtual {p1, v0, v1, v2, v3}, Landroid/graphics/Canvas;->clipRect(IIII)Z

    goto/32 :goto_c0

    nop

    :goto_ba
    iget v3, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->topMargin:I

    goto/32 :goto_96

    nop

    :goto_c0
    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    goto/32 :goto_86

    nop

    :goto_c7
    iget v2, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->leftPadd:I

    goto/32 :goto_ba

    nop

    :goto_cd
    sub-int/2addr v0, v1

    goto/32 :goto_4d

    nop

    :goto_d2
    const/16 v1, 0x14

    goto/32 :goto_44

    nop

    :goto_d8
    sub-int/2addr v2, v3

    goto/32 :goto_ab

    nop

    :goto_dd
    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->leftMargin:I

    goto/32 :goto_79

    nop
.end method

.method public getChild()Landroid/view/View;
    .registers 2

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    return-object v0
.end method

.method public abstract getElementName()Ljava/lang/String;
.end method

.method protected onDetachedFromWindow()V
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    invoke-super {p0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->onDetachedFromWindow()V

    goto/32 :goto_15

    nop

    :goto_b
    if-nez v0, :cond_10

    goto/32 :goto_1e

    :cond_10
    goto/32 :goto_1b

    nop

    :goto_14
    return-void

    :goto_15
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->observer:Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;

    goto/32 :goto_b

    nop

    :goto_1b
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$SettingsObserver;->unregister()V

    :goto_1e
    goto/32 :goto_14

    nop
.end method

.method protected onFinishInflate()V
    .registers 4

    goto/32 :goto_11

    nop

    :goto_4
    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$1;-><init>(Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;)V

    goto/32 :goto_20

    nop

    :goto_b
    new-instance v0, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout$1;

    goto/32 :goto_4

    nop

    :goto_11
    invoke-super {p0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->onFinishInflate()V

    goto/32 :goto_b

    nop

    :goto_18
    invoke-virtual {p0, v0, v1, v2}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->postDelayed(Ljava/lang/Runnable;J)Z

    goto/32 :goto_1f

    nop

    :goto_1f
    return-void

    :goto_20
    const-wide/16 v1, 0xc8

    goto/32 :goto_18

    nop
.end method

.method update()V
    .registers 1

    goto/32 :goto_13

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->invalidate()V

    goto/32 :goto_b

    nop

    :goto_b
    return-void

    :goto_c
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->makeBackground()V

    goto/32 :goto_4

    nop

    :goto_13
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->updateMargins()V

    goto/32 :goto_c

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_ElementBgLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
