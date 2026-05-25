"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/data/TextData.smali'
CLASS_FALLBACK_NAMES = ['TextData.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/data/TextData;
.super Lcom/android/systemui/newstatusbar/data/Data;


# static fields
.field public static final SettingsKeyTypeFase:Ljava/lang/String; = "_typefase"

.field public static final SettingsKeyTypeFaseStyle:Ljava/lang/String; = "_typefasestyle"


# instance fields
.field public defColor:I

.field public defSize:F

.field public defTypefase:Landroid/graphics/Typeface;

.field public typeFase:Ljava/lang/String;

.field public typeFaseStyle:I


# direct methods
.method public constructor <init>(Landroid/content/Context;Ljava/lang/String;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/data/Data;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    const-string v0, ""

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFase:Ljava/lang/String;

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    return-void
.end method

.method public static get11InverseColor(I)I
    .registers 6

    not-int v0, p0

    invoke-static {p0}, Landroid/graphics/Color;->alpha(I)I

    move-result v1

    invoke-static {v0}, Landroid/graphics/Color;->red(I)I

    move-result v2

    invoke-static {v0}, Landroid/graphics/Color;->green(I)I

    move-result v3

    invoke-static {v0}, Landroid/graphics/Color;->blue(I)I

    move-result v4

    invoke-static {v1, v2, v3, v4}, Landroid/graphics/Color;->argb(IIII)I

    move-result v1

    return v1
.end method


# virtual methods
.method public copy()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 4

    new-instance v0, Lcom/android/systemui/newstatusbar/data/TextData;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->context:Landroid/content/Context;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/data/TextData;->key:Ljava/lang/String;

    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    iget v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->color:I

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->color:I

    iget v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->division:I

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->division:I

    iget v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->zoom:I

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->zoom:I

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFase:Ljava/lang/String;

    iput-object v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFase:Ljava/lang/String;

    iget v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    iget v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->shadow_color:I

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->shadow_color:I

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->shadow_enable:Z

    iput-boolean v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->shadow_enable:Z

    iget v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->defColor:I

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->defColor:I

    iget v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->defSize:F

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->defSize:F

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->defTypefase:Landroid/graphics/Typeface;

    iput-object v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->defTypefase:Landroid/graphics/Typeface;

    return-object v0
.end method

.method public getColor()I
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/data/TextData;->color:I

    if-nez v0, :cond_7

    iget v0, p0, Lcom/android/systemui/newstatusbar/data/TextData;->defColor:I

    goto :goto_9

    :cond_7
    iget v0, p0, Lcom/android/systemui/newstatusbar/data/TextData;->color:I

    :goto_9
    return v0
.end method

.method public getKeys()[Ljava/lang/String;
    .registers 4

    const/4 v0, 0x5

    new-array v0, v0, [Ljava/lang/String;

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/data/TextData;->key:Ljava/lang/String;

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, "_typefase"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x0

    aput-object v1, v0, v2

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/data/TextData;->key:Ljava/lang/String;

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, "_typefasestyle"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x1

    aput-object v1, v0, v2

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/data/TextData;->key:Ljava/lang/String;

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, "_color"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x2

    aput-object v1, v0, v2

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/data/TextData;->key:Ljava/lang/String;

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, "_division"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x3

    aput-object v1, v0, v2

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/data/TextData;->key:Ljava/lang/String;

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, "_zoom"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x4

    aput-object v1, v0, v2

    return-object v0
.end method

.method public getSize()F
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/data/TextData;->zoom:I

    if-nez v0, :cond_7

    iget v0, p0, Lcom/android/systemui/newstatusbar/data/TextData;->defSize:F

    goto :goto_a

    :cond_7
    iget v0, p0, Lcom/android/systemui/newstatusbar/data/TextData;->zoom:I

    int-to-float v0, v0

    :goto_a
    return v0
.end method

.method public getTypeFace()Landroid/graphics/Typeface;
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/data/TextData;->defTypefase:Landroid/graphics/Typeface;

    :try_start_2
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFase:Ljava/lang/String;

    invoke-static {v1}, Landroid/graphics/Typeface;->createFromFile(Ljava/lang/String;)Landroid/graphics/Typeface;

    move-result-object v1
    :try_end_8
    .catch Ljava/lang/RuntimeException; {:try_start_2 .. :try_end_8} :catch_a

    move-object v0, v1

    goto :goto_18

    :catch_a
    move-exception v1

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v2

    const-string v3, "getTypeFase : fonts not found"

    invoke-static {v2, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_18
    return-object v0
.end method

.method public update()Lcom/android/systemui/newstatusbar/data/Data;
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Lcom/android/systemui/newstatusbar/data/Data;",
            ">()TT;"
        }
    .end annotation

    invoke-super {p0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->key:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "_typefasestyle"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/data/TextData;->key:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "_typefase"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "Default"

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getStringofSettings(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFase:Ljava/lang/String;

    return-object p0
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_data_TextData',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
