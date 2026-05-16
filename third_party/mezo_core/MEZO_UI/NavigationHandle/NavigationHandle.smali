.class public Lcom/android/systemui/navigationbar/gestural/NavigationHandle;
.super Landroid/view/View;
.source "NavigationHandle.java"

# interfaces
.implements Lcom/android/systemui/navigationbar/buttons/ButtonInterface;


# instance fields
.field public mBottom:F

.field private final mContentResolver:Landroid/content/ContentResolver;

.field private final mContext:Landroid/content/Context;

.field public mDarkColor:I

.field private mDarkIntensity:F

.field private mIsCustomPillEnabled:Z

.field public mLightColor:I

.field public final mPaint:Landroid/graphics/Paint;

.field public mRadius:F

.field public mRequiresInvalidate:Z

.field private final mSettingsObserver:Landroid/database/ContentObserver;

.field public mWidth:I


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3
    .param p1, "context"  # Landroid/content/Context;

    .line 48
    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    .line 49
    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 5
    .param p1, "context"  # Landroid/content/Context;
    .param p2, "attributeSet"  # Landroid/util/AttributeSet;

    .line 52
    invoke-direct {p0, p1, p2}, Landroid/view/View;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    .line 35
    new-instance v0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle$1;

    new-instance v1, Landroid/os/Handler;

    invoke-direct {v1}, Landroid/os/Handler;-><init>()V

    invoke-direct {v0, p0, v1}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle$1;-><init>(Lcom/android/systemui/navigationbar/gestural/NavigationHandle;Landroid/os/Handler;)V

    iput-object v0, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mSettingsObserver:Landroid/database/ContentObserver;

    .line 53
    iput-object p1, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mContext:Landroid/content/Context;

    .line 54
    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mContentResolver:Landroid/content/ContentResolver;

    .line 55
    new-instance v0, Landroid/graphics/Paint;

    invoke-direct {v0}, Landroid/graphics/Paint;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mPaint:Landroid/graphics/Paint;

    .line 56
    iget-object v0, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mPaint:Landroid/graphics/Paint;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Landroid/graphics/Paint;->setAntiAlias(Z)V

    .line 57
    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->setFocusable(Z)V

    .line 58
    invoke-direct {p0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->updateSettings()V

    .line 59
    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/navigationbar/gestural/NavigationHandle;)V
    .registers 1
    .param p0, "x0"  # Lcom/android/systemui/navigationbar/gestural/NavigationHandle;

    .line 24
    invoke-direct {p0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->updateSettings()V

    return-void
.end method

.method private registerSettingsObserver()V
    .registers 5

    .line 133
    iget-object v0, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mContentResolver:Landroid/content/ContentResolver;

    .line 134
    .local v0, "contentResolver":Landroid/content/ContentResolver;
    iget-object v1, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mSettingsObserver:Landroid/database/ContentObserver;

    .line 135
    .local v1, "contentObserver":Landroid/database/ContentObserver;
    const-string v2, "navigation_handle_custom_pill"

    invoke-static {v2}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v2

    const/4 v3, 0x0

    invoke-virtual {v0, v2, v3, v1}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    .line 136
    const-string v2, "navigation_handle_use_monet"

    invoke-static {v2}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v2

    invoke-virtual {v0, v2, v3, v1}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    .line 137
    const-string v2, "navigation_handle_light_color"

    invoke-static {v2}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v2

    invoke-virtual {v0, v2, v3, v1}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    .line 138
    const-string v2, "navigation_handle_dark_color"

    invoke-static {v2}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v2

    invoke-virtual {v0, v2, v3, v1}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    .line 139
    const-string v2, "navigation_handle_width"

    invoke-static {v2}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v2

    invoke-virtual {v0, v2, v3, v1}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    .line 140
    const-string v2, "navigation_handle_radius"

    invoke-static {v2}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v2

    invoke-virtual {v0, v2, v3, v1}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    .line 141
    const-string v2, "navigation_handle_bottom"

    invoke-static {v2}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v2

    invoke-virtual {v0, v2, v3, v1}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    .line 142
    return-void
.end method

.method private updateSettings()V
    .registers 9

    .line 62
    iget-object v0, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mContext:Landroid/content/Context;

    .line 63
    .local v0, "context":Landroid/content/Context;
    iget-object v1, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mContentResolver:Landroid/content/ContentResolver;

    .line 64
    .local v1, "contentResolver":Landroid/content/ContentResolver;
    const-string v2, "navigation_handle_custom_pill"

    const/4 v3, 0x0

    invoke-static {v1, v2, v3}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v2

    const/4 v4, 0x1

    if-ne v2, v4, :cond_10

    move v2, v4

    goto :goto_11

    :cond_10
    move v2, v3

    :goto_11
    iput-boolean v2, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mIsCustomPillEnabled:Z

    .line 65
    iget-boolean v2, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mIsCustomPillEnabled:Z

    if-nez v2, :cond_6a

    .line 66
    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    .line 67
    .local v2, "resources":Landroid/content/res/Resources;
    const-string v4, "dimen/navigation_handle_radius"

    invoke-static {v0, v4}, Lcom/android/kevin/MyUtils;->getRIdentifier(Landroid/content/Context;Ljava/lang/String;)I

    move-result v4

    invoke-virtual {v2, v4}, Landroid/content/res/Resources;->getDimension(I)F

    move-result v4

    iput v4, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mRadius:F

    .line 68
    const-string v4, "dimen/navigation_handle_bottom"

    invoke-static {v0, v4}, Lcom/android/kevin/MyUtils;->getRIdentifier(Landroid/content/Context;Ljava/lang/String;)I

    move-result v4

    invoke-virtual {v2, v4}, Landroid/content/res/Resources;->getDimension(I)F

    move-result v4

    iput v4, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mBottom:F

    .line 69
    invoke-virtual {p0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->getWidth()I

    move-result v4

    iput v4, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mWidth:I

    .line 70
    new-instance v4, Landroid/view/ContextThemeWrapper;

    const-string v5, "attr/lightIconTheme"

    invoke-static {v0, v5}, Lcom/android/kevin/MyUtils;->getRIdentifier(Landroid/content/Context;Ljava/lang/String;)I

    move-result v5

    invoke-static {v5, v0}, Lcom/android/settingslib/Utils;->getThemeAttr(ILandroid/content/Context;)I

    move-result v5

    invoke-direct {v4, v0, v5}, Landroid/view/ContextThemeWrapper;-><init>(Landroid/content/Context;I)V

    .line 71
    .local v4, "contextThemeWrapper":Landroid/view/ContextThemeWrapper;
    new-instance v5, Landroid/view/ContextThemeWrapper;

    const-string v6, "attr/darkIconTheme"

    invoke-static {v0, v6}, Lcom/android/kevin/MyUtils;->getRIdentifier(Landroid/content/Context;Ljava/lang/String;)I

    move-result v6

    invoke-static {v6, v0}, Lcom/android/settingslib/Utils;->getThemeAttr(ILandroid/content/Context;)I

    move-result v6

    invoke-direct {v5, v0, v6}, Landroid/view/ContextThemeWrapper;-><init>(Landroid/content/Context;I)V

    .line 72
    .local v5, "contextThemeWrapper2":Landroid/view/ContextThemeWrapper;
    const-string v6, "attr/homeHandleColor"

    invoke-static {v0, v6}, Lcom/android/kevin/MyUtils;->getRIdentifier(Landroid/content/Context;Ljava/lang/String;)I

    move-result v6

    .line 73
    .local v6, "homeHandleColor":I
    invoke-static {v4, v6, v3}, Lcom/android/settingslib/Utils;->getColorAttrDefaultColor(Landroid/content/Context;II)I

    move-result v7

    iput v7, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mLightColor:I

    .line 74
    invoke-static {v5, v6, v3}, Lcom/android/settingslib/Utils;->getColorAttrDefaultColor(Landroid/content/Context;II)I

    move-result v3

    iput v3, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mDarkColor:I

    .line 75
    .end local v2  # "resources":Landroid/content/res/Resources;
    .end local v4  # "contextThemeWrapper":Landroid/view/ContextThemeWrapper;
    .end local v5  # "contextThemeWrapper2":Landroid/view/ContextThemeWrapper;
    .end local v6  # "homeHandleColor":I
    goto :goto_ca

    .line 76
    :cond_6a
    const-string v2, "navigation_handle_use_monet"

    invoke-static {v1, v2, v3}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v2

    if-ne v2, v4, :cond_73

    move v3, v4

    :cond_73
    move v2, v3

    .line 77
    .local v2, "useMonet":Z
    if-nez v2, :cond_8a

    .line 78
    const-string v3, "navigation_handle_light_color"

    const/high16 v4, -0x1000000

    invoke-static {v1, v3, v4}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v3

    iput v3, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mLightColor:I

    .line 79
    const-string v3, "navigation_handle_dark_color"

    const/4 v4, -0x1

    invoke-static {v1, v3, v4}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v3

    iput v3, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mDarkColor:I

    goto :goto_aa

    .line 81
    :cond_8a
    invoke-virtual {p0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    const-string v4, "color/system_accent1_200.android"

    invoke-static {v0, v4}, Lcom/android/kevin/MyUtils;->getRIdentifier(Landroid/content/Context;Ljava/lang/String;)I

    move-result v4

    invoke-virtual {v3, v4}, Landroid/content/res/Resources;->getColor(I)I

    move-result v3

    iput v3, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mLightColor:I

    .line 82
    invoke-virtual {p0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    const-string v4, "color/system_accent1_500.android"

    invoke-static {v0, v4}, Lcom/android/kevin/MyUtils;->getRIdentifier(Landroid/content/Context;Ljava/lang/String;)I

    move-result v4

    invoke-virtual {v3, v4}, Landroid/content/res/Resources;->getColor(I)I

    move-result v3

    iput v3, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mDarkColor:I

    .line 84
    :goto_aa
    const-string v3, "navigation_handle_width"

    const/16 v4, 0x54

    invoke-static {v1, v3, v4}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v3

    mul-int/lit8 v3, v3, 0x5

    iput v3, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mWidth:I

    .line 85
    const-string v3, "navigation_handle_radius"

    const/high16 v4, 0x40c00000  # 6.0f

    invoke-static {v1, v3, v4}, Landroid/provider/Settings$System;->getFloat(Landroid/content/ContentResolver;Ljava/lang/String;F)F

    move-result v3

    iput v3, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mRadius:F

    .line 86
    const-string v3, "navigation_handle_bottom"

    const/high16 v4, 0x41700000  # 15.0f

    invoke-static {v1, v3, v4}, Landroid/provider/Settings$System;->getFloat(Landroid/content/ContentResolver;Ljava/lang/String;F)F

    move-result v3

    iput v3, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mBottom:F

    .line 88
    .end local v2  # "useMonet":Z
    :goto_ca
    iget v2, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mDarkIntensity:F

    invoke-virtual {p0, v2}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->setDarkIntensity(F)V

    .line 89
    return-void
.end method


# virtual methods
.method public final abortCurrentGesture()V
    .registers 1

    .line 92
    return-void
.end method

.method protected onAttachedToWindow()V
    .registers 1

    .line 145
    invoke-super {p0}, Landroid/view/View;->onAttachedToWindow()V

    .line 146
    invoke-direct {p0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->registerSettingsObserver()V

    .line 147
    return-void
.end method

.method protected onDetachedFromWindow()V
    .registers 3

    .line 150
    invoke-super {p0}, Landroid/view/View;->onDetachedFromWindow()V

    .line 151
    iget-object v0, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mContentResolver:Landroid/content/ContentResolver;

    iget-object v1, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mSettingsObserver:Landroid/database/ContentObserver;

    invoke-virtual {v0, v1}, Landroid/content/ContentResolver;->unregisterContentObserver(Landroid/database/ContentObserver;)V

    .line 152
    return-void
.end method

.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 16
    .param p1, "canvas"  # Landroid/graphics/Canvas;

    .line 96
    invoke-super {p0, p1}, Landroid/view/View;->onDraw(Landroid/graphics/Canvas;)V

    .line 97
    invoke-virtual {p0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->getHeight()I

    move-result v0

    .line 98
    .local v0, "height":I
    iget v1, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mRadius:F

    const/high16 v2, 0x40000000  # 2.0f

    mul-float/2addr v1, v2

    .line 99
    .local v1, "handleHeight":F
    int-to-float v3, v0

    iget v4, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mBottom:F

    sub-float/2addr v3, v4

    sub-float/2addr v3, v1

    .line 100
    .local v3, "top":F
    iget v12, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mRadius:F

    .line 101
    .local v12, "radius":F
    invoke-virtual {p0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->getWidth()I

    move-result v13

    .line 102
    .local v13, "width":I
    iget-boolean v4, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mIsCustomPillEnabled:Z

    if-eqz v4, :cond_34

    .line 103
    iget v4, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mWidth:I

    sub-int v4, v13, v4

    int-to-float v4, v4

    div-float v2, v4, v2

    .line 104
    .local v2, "left":F
    iget v4, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mWidth:I

    int-to-float v4, v4

    add-float v7, v2, v4

    add-float v8, v3, v1

    iget-object v11, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mPaint:Landroid/graphics/Paint;

    move-object v4, p1

    move v5, v2

    move v6, v3

    move v9, v12

    move v10, v12

    invoke-virtual/range {v4 .. v11}, Landroid/graphics/Canvas;->drawRoundRect(FFFFFFLandroid/graphics/Paint;)V

    .line 105
    .end local v2  # "left":F
    goto :goto_41

    .line 106
    :cond_34
    int-to-float v7, v13

    add-float v8, v3, v1

    iget-object v11, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mPaint:Landroid/graphics/Paint;

    const/4 v5, 0x0

    move-object v4, p1

    move v6, v3

    move v9, v12

    move v10, v12

    invoke-virtual/range {v4 .. v11}, Landroid/graphics/Canvas;->drawRoundRect(FFFFFFLandroid/graphics/Paint;)V

    .line 108
    :goto_41
    return-void
.end method

.method public setAlpha(F)V
    .registers 3
    .param p1, "f"  # F

    .line 112
    invoke-super {p0, p1}, Landroid/view/View;->setAlpha(F)V

    .line 113
    const/4 v0, 0x0

    cmpg-float v0, p1, v0

    if-lez v0, :cond_14

    iget-boolean v0, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mRequiresInvalidate:Z

    if-nez v0, :cond_d

    goto :goto_14

    .line 116
    :cond_d
    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mRequiresInvalidate:Z

    .line 117
    invoke-virtual {p0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->invalidate()V

    .line 118
    return-void

    .line 114
    :cond_14
    :goto_14
    return-void
.end method

.method public setDarkIntensity(F)V
    .registers 5
    .param p1, "f"  # F

    .line 121
    iput p1, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mDarkIntensity:F

    .line 122
    invoke-static {}, Landroid/animation/ArgbEvaluator;->getInstance()Landroid/animation/ArgbEvaluator;

    move-result-object v0

    iget v1, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mLightColor:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    iget v2, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mDarkColor:I

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    invoke-virtual {v0, p1, v1, v2}, Landroid/animation/ArgbEvaluator;->evaluate(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/lang/Integer;

    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result v0

    .line 123
    .local v0, "intValue":I
    iget-object v1, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v1}, Landroid/graphics/Paint;->getColor()I

    move-result v1

    if-eq v1, v0, :cond_40

    .line 124
    iget-object v1, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v1, v0}, Landroid/graphics/Paint;->setColor(I)V

    .line 125
    invoke-virtual {p0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->getVisibility()I

    move-result v1

    if-nez v1, :cond_3d

    invoke-virtual {p0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->getAlpha()F

    move-result v1

    const/4 v2, 0x0

    cmpg-float v1, v1, v2

    if-gtz v1, :cond_39

    goto :goto_3d

    .line 128
    :cond_39
    invoke-virtual {p0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->invalidate()V

    goto :goto_40

    .line 126
    :cond_3d
    :goto_3d
    const/4 v1, 0x1

    iput-boolean v1, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mRequiresInvalidate:Z

    .line 131
    :cond_40
    :goto_40
    return-void
.end method

.method public setDefaultColor(I)V
    .registers 3
    .param p1, "i"  # I

    .line 154
    iget-object v0, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->mPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, p1}, Landroid/graphics/Paint;->setColor(I)V

    .line 155
    return-void
.end method

.method public setDelayTouchFeedback(Z)V
    .registers 2
    .param p1, "z"  # Z

    .line 158
    return-void
.end method

.method public setImageDrawable(Landroid/graphics/drawable/Drawable;)V
    .registers 2
    .param p1, "drawable"  # Landroid/graphics/drawable/Drawable;

    .line 161
    return-void
.end method

.method public setVertical(Z)V
    .registers 2
    .param p1, "z"  # Z

    .line 164
    return-void
.end method
