"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/battery/BatteryMeterIconView.smali'
CLASS_FALLBACK_NAMES = ['BatteryMeterIconView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;
.super Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# instance fields
.field protected batteryHeight:I

.field protected batteryWidth:I

.field private bitmap:Landroid/graphics/Bitmap;

.field private final controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

.field protected curHeight:I

.field protected curWidth:I

.field private isIconAdded:Z

.field protected naturalHeight:I

.field protected naturalWidth:I

.field paint:Landroid/graphics/Paint;

.field private final tmpCanvas:Landroid/graphics/Canvas;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 7

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->isIconAdded:Z

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    new-instance v0, Landroid/graphics/Paint;

    const/4 v1, 0x1

    invoke-direct {v0, v1}, Landroid/graphics/Paint;-><init>(I)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->paint:Landroid/graphics/Paint;

    new-instance v0, Landroid/graphics/Canvas;

    invoke-direct {v0}, Landroid/graphics/Canvas;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->tmpCanvas:Landroid/graphics/Canvas;

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const-string v2, "status_bar_icon_height"

    invoke-static {p1, v2}, Landroid/Utils/Utils;->DimenToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v2

    invoke-virtual {v0, v2}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->batteryHeight:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v2, "battery_meter_width"

    invoke-static {v0, v2}, Landroid/Utils/Utils;->getDimen(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->batteryWidth:I

    iget v2, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->batteryHeight:I

    iput v2, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->naturalHeight:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->naturalWidth:I

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->isIconAdded:Z

    return-void
.end method

.method private drawInternal(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V
    .registers 7

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->paint:Landroid/graphics/Paint;

    invoke-virtual {v0}, Landroid/graphics/Paint;->reset()V

    iget v0, p2, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    if-nez v0, :cond_10

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->paint:Landroid/graphics/Paint;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/graphics/Paint;->setColorFilter(Landroid/graphics/ColorFilter;)Landroid/graphics/ColorFilter;

    goto :goto_1e

    :cond_10
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->paint:Landroid/graphics/Paint;

    new-instance v1, Landroid/graphics/PorterDuffColorFilter;

    iget v2, p2, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    sget-object v3, Landroid/graphics/PorterDuff$Mode;->SRC_IN:Landroid/graphics/PorterDuff$Mode;

    invoke-direct {v1, v2, v3}, Landroid/graphics/PorterDuffColorFilter;-><init>(ILandroid/graphics/PorterDuff$Mode;)V

    invoke-virtual {v0, v1}, Landroid/graphics/Paint;->setColorFilter(Landroid/graphics/ColorFilter;)Landroid/graphics/ColorFilter;

    :goto_1e
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->bitmap:Landroid/graphics/Bitmap;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->paint:Landroid/graphics/Paint;

    const/4 v2, 0x0

    invoke-virtual {p1, v0, v2, v2, v1}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;FFLandroid/graphics/Paint;)V

    return-void
.end method

.method private drawShadow(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V
    .registers 8

    iget-boolean v0, p2, Lcom/android/systemui/newstatusbar/data/IconData;->shadow_enable:Z

    if-eqz v0, :cond_27

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->paint:Landroid/graphics/Paint;

    sget v1, Lcom/android/systemui/newstatusbar/data/Data;->ShadowRadius:F

    sget v2, Lcom/android/systemui/newstatusbar/data/Data;->ShadowToX:F

    sget v3, Lcom/android/systemui/newstatusbar/data/Data;->ShadowToY:F

    iget v4, p2, Lcom/android/systemui/newstatusbar/data/IconData;->shadow_color:I

    invoke-virtual {v0, v1, v2, v3, v4}, Landroid/graphics/Paint;->setShadowLayer(FFFI)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->paint:Landroid/graphics/Paint;

    new-instance v1, Landroid/graphics/PorterDuffColorFilter;

    iget v2, p2, Lcom/android/systemui/newstatusbar/data/IconData;->shadow_color:I

    sget-object v3, Landroid/graphics/PorterDuff$Mode;->SRC_IN:Landroid/graphics/PorterDuff$Mode;

    invoke-direct {v1, v2, v3}, Landroid/graphics/PorterDuffColorFilter;-><init>(ILandroid/graphics/PorterDuff$Mode;)V

    invoke-virtual {v0, v1}, Landroid/graphics/Paint;->setColorFilter(Landroid/graphics/ColorFilter;)Landroid/graphics/ColorFilter;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->bitmap:Landroid/graphics/Bitmap;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->paint:Landroid/graphics/Paint;

    const/4 v2, 0x0

    invoke-virtual {p1, v0, v2, v2, v1}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;FFLandroid/graphics/Paint;)V

    :cond_27
    return-void
.end method

.method private getData()Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getIconData(Z)Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    return-object v0
.end method

.method private isZero()Z
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->naturalHeight:I

    if-eqz v0, :cond_b

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->naturalWidth:I

    if-nez v0, :cond_9

    goto :goto_b

    :cond_9
    const/4 v0, 0x0

    goto :goto_c

    :cond_b
    :goto_b
    const/4 v0, 0x1

    :goto_c
    return v0
.end method

.method private update()V
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->isIconAdded:Z

    if-eqz v0, :cond_a

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->updateZoom()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->invalidate()V

    :cond_a
    return-void
.end method

.method private updateBitmapIfNeeded(II)V
    .registers 4

    if-lez p1, :cond_1e

    if-lez p2, :cond_1e

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->curWidth:I

    if-ne p1, v0, :cond_c

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->curHeight:I

    if-eq p2, v0, :cond_1e

    :cond_c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->bitmap:Landroid/graphics/Bitmap;

    if-eqz v0, :cond_16

    invoke-virtual {v0}, Landroid/graphics/Bitmap;->recycle()V

    const/4 v0, 0x0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->bitmap:Landroid/graphics/Bitmap;

    :cond_16
    sget-object v0, Landroid/graphics/Bitmap$Config;->ARGB_8888:Landroid/graphics/Bitmap$Config;

    invoke-static {p1, p2, v0}, Landroid/graphics/Bitmap;->createBitmap(IILandroid/graphics/Bitmap$Config;)Landroid/graphics/Bitmap;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->bitmap:Landroid/graphics/Bitmap;

    :cond_1e
    return-void
.end method

.method private updateScale(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V
    .registers 9

    iget v0, p2, Lcom/android/systemui/newstatusbar/data/IconData;->zoom:I

    int-to-float v0, v0

    const/high16 v1, 0x42c80000  # 100.0f

    div-float v0, v1, v0

    const/high16 v2, 0x3f800000  # 1.0f

    sub-float/2addr v0, v2

    const/high16 v2, 0x40800000  # 4.0f

    mul-float/2addr v0, v2

    iget v2, p2, Lcom/android/systemui/newstatusbar/data/IconData;->division:I

    int-to-float v2, v2

    add-float/2addr v2, v0

    const/4 v3, 0x0

    invoke-virtual {p1, v3, v2}, Landroid/graphics/Canvas;->translate(FF)V

    iget v2, p2, Lcom/android/systemui/newstatusbar/data/IconData;->scale:I

    int-to-float v2, v2

    div-float/2addr v2, v1

    iget v3, p2, Lcom/android/systemui/newstatusbar/data/IconData;->scale:I

    int-to-float v3, v3

    div-float/2addr v3, v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->getWidth()I

    move-result v1

    int-to-float v1, v1

    const/high16 v4, 0x40000000  # 2.0f

    div-float/2addr v1, v4

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->getHeight()I

    move-result v5

    int-to-float v5, v5

    div-float/2addr v5, v4

    invoke-virtual {p1, v2, v3, v1, v5}, Landroid/graphics/Canvas;->scale(FFFF)V

    return-void
.end method

.method private updateZoom()V
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    if-eqz v0, :cond_9

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    :cond_9
    return-void
.end method


# virtual methods
.method public onAttachedToWindow()V
    .registers 2

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;->onAttachedToWindow()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;->onDetachedFromWindow()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public onDraw(Landroid/graphics/Canvas;)V
    .registers 6

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->getData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->isIconAdded:Z

    if-eqz v1, :cond_27

    if-eqz v0, :cond_27

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->updateScale(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->bitmap:Landroid/graphics/Bitmap;

    if-eqz v1, :cond_27

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->tmpCanvas:Landroid/graphics/Canvas;

    invoke-virtual {v2, v1}, Landroid/graphics/Canvas;->setBitmap(Landroid/graphics/Bitmap;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->tmpCanvas:Landroid/graphics/Canvas;

    const/4 v2, 0x0

    sget-object v3, Landroid/graphics/PorterDuff$Mode;->CLEAR:Landroid/graphics/PorterDuff$Mode;

    invoke-virtual {v1, v2, v3}, Landroid/graphics/Canvas;->drawColor(ILandroid/graphics/PorterDuff$Mode;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->tmpCanvas:Landroid/graphics/Canvas;

    invoke-super {p0, v1}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;->onDraw(Landroid/graphics/Canvas;)V

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->drawInternal(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V

    return-void

    :cond_27
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;->onDraw(Landroid/graphics/Canvas;)V

    return-void
.end method

.method public onIconChange()V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->update()V

    return-void
.end method

.method public onMeasure(II)V
    .registers 5

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->curHeight:I

    if-lez v0, :cond_c

    iget v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->curWidth:I

    if-lez v1, :cond_c

    invoke-virtual {p0, v1, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->setMeasuredDimension(II)V

    goto :goto_f

    :cond_c
    invoke-super {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;->onMeasure(II)V

    :goto_f
    return-void
.end method

.method public setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V
    .registers 8

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->getData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->isIconAdded:Z

    if-eqz v1, :cond_30

    if-eqz v0, :cond_30

    if-eqz p1, :cond_30

    iget v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->zoom:I

    iget v2, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->naturalWidth:I

    if-lez v2, :cond_30

    iget v3, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->naturalHeight:I

    if-lez v3, :cond_30

    int-to-float v4, v1

    iget v5, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->batteryHeight:I

    int-to-float v5, v5

    mul-float/2addr v4, v5

    const/high16 v5, 0x42c80000  # 100.0f

    div-float/2addr v4, v5

    float-to-int v4, v4

    int-to-float v5, v4

    int-to-float v2, v2

    mul-float/2addr v5, v2

    int-to-float v2, v3

    div-float/2addr v5, v2

    float-to-int v2, v5

    invoke-direct {p0, v2, v4}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->updateBitmapIfNeeded(II)V

    iput v4, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->curHeight:I

    iput v2, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->curWidth:I

    iput v2, p1, Landroid/view/ViewGroup$LayoutParams;->width:I

    iput v4, p1, Landroid/view/ViewGroup$LayoutParams;->height:I

    :cond_30
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiBatteryMeterIconView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    return-void
.end method

.method public setScaleType(Landroid/widget/ImageView$ScaleType;)V
    .registers 2

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_battery_BatteryMeterIconView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
