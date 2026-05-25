"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/data/Data.smali'
CLASS_FALLBACK_NAMES = ['Data.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/data/Data;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt<",
        "Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;",
        ">;"
    }
.end annotation


# static fields
.field public static final SettingsKeyColor:Ljava/lang/String; = "_color"

.field public static final SettingsKeyDivision:Ljava/lang/String; = "_division"

.field public static final SettingsKeyShadowColor:Ljava/lang/String; = "_shadowcolor"

.field public static final SettingsKeyShadowEnable:Ljava/lang/String; = "_shadowenable"

.field public static final SettingsKeyZoom:Ljava/lang/String; = "_zoom"

.field public static ShadowRadius:F

.field public static ShadowToX:F

.field public static ShadowToY:F


# instance fields
.field public color:I

.field public division:I

.field public key:Ljava/lang/String;

.field private final listeners:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;",
            ">;"
        }
    .end annotation
.end field

.field private settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver<",
            "*>;"
        }
    .end annotation
.end field

.field public shadow_color:I

.field public shadow_enable:Z

.field public zoom:I


# direct methods
.method static constructor <clinit>()V
    .registers 1

    const/high16 v0, 0x40400000  # 3.0f

    sput v0, Lcom/android/systemui/newstatusbar/data/Data;->ShadowRadius:F

    sput v0, Lcom/android/systemui/newstatusbar/data/Data;->ShadowToX:F

    sput v0, Lcom/android/systemui/newstatusbar/data/Data;->ShadowToY:F

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Ljava/lang/String;)V
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    const-string v0, ""

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->key:Ljava/lang/String;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->listeners:Ljava/util/ArrayList;

    iput-object p2, p0, Lcom/android/systemui/newstatusbar/data/Data;->key:Ljava/lang/String;

    return-void
.end method

.method public static getAlphaShadow(I)I
    .registers 5

    invoke-static {p0}, Landroid/graphics/Color;->alpha(I)I

    move-result v0

    div-int/lit8 v0, v0, 0x2

    invoke-static {p0}, Landroid/graphics/Color;->red(I)I

    move-result v1

    invoke-static {p0}, Landroid/graphics/Color;->green(I)I

    move-result v2

    invoke-static {p0}, Landroid/graphics/Color;->blue(I)I

    move-result v3

    invoke-static {v0, v1, v2, v3}, Landroid/graphics/Color;->argb(IIII)I

    move-result v0

    return v0
.end method


# virtual methods
.method public varargs addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Lcom/android/systemui/newstatusbar/data/Data;",
            ">([",
            "Ljava/lang/String;",
            ")TT;"
        }
    .end annotation

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    if-nez v0, :cond_b

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-direct {v0, p0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    :cond_b
    array-length v0, p1

    if-nez v0, :cond_12

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/data/Data;->getKeys()[Ljava/lang/String;

    move-result-object p1

    :cond_12
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-virtual {v0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->addKeys([Ljava/lang/String;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    return-object p0
.end method

.method public addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Lcom/android/systemui/newstatusbar/data/Data;",
            ">(",
            "Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;",
            ")TT;"
        }
    .end annotation

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->listeners:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    return-object p0
.end method

.method public addUri(Landroid/net/Uri;)Lcom/android/systemui/newstatusbar/data/Data;
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Lcom/android/systemui/newstatusbar/data/Data;",
            ">(",
            "Landroid/net/Uri;",
            ")TT;"
        }
    .end annotation

    if-eqz p1, :cond_12

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    if-nez v0, :cond_d

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-direct {v0, p0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    :cond_d
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-virtual {v0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->addUri(Landroid/net/Uri;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    :cond_12
    return-object p0
.end method

.method public getKeys()[Ljava/lang/String;
    .registers 2

    const/4 v0, 0x0

    new-array v0, v0, [Ljava/lang/String;

    return-object v0
.end method

.method public onSettingsChange(Ljava/lang/String;)V
    .registers 5

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->listeners:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_9
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_1b

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/data/Data;->key:Ljava/lang/String;

    invoke-interface {v1, v2, p1}, Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;->onDataChanged(Ljava/lang/String;Ljava/lang/String;)V

    goto :goto_9

    :cond_1b
    return-void
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

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/data/Data;->key:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "_color"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->color:I

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/data/Data;->key:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "_zoom"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const/16 v1, 0x64

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->zoom:I

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/data/Data;->key:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "_division"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const/16 v1, 0x0

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->division:I

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/data/Data;->key:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "_shadowenable"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings(Ljava/lang/String;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->shadow_enable:Z

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/data/Data;->key:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "_shadowcolor"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->shadow_color:I

    if-nez v0, :cond_97

    iget v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->color:I

    if-eqz v0, :cond_97

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/data/Data;->getAlphaShadow(I)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/data/Data;->shadow_color:I

    :cond_97
    return-object p0
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_data_Data',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
