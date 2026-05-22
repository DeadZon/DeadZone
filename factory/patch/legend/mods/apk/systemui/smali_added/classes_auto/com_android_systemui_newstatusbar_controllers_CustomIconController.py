"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/CustomIconController.smali'
CLASS_FALLBACK_NAMES = ['CustomIconController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/CustomIconController;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/controllers/CustomIconController$CallBack;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt<",
        "Lcom/android/systemui/newstatusbar/controllers/CustomIconController$CallBack;",
        ">;"
    }
.end annotation


# static fields
.field public static final SIM_KEY:Ljava/lang/String; = "sim_icon_style"

.field public static final VOLTE_KEY:Ljava/lang/String; = "volte_icon_style"

.field public static final VOWIFI_KEY:Ljava/lang/String; = "vowifi_icon_style"

.field public static final WIFI_KEY:Ljava/lang/String; = "wifi_icon_style"


# instance fields
.field private final simIds:Landroid/util/SparseIntArray;

.field private final stokSimIds:[I

.field private final stokWiFiIds:[I

.field private volteIds:I

.field private vowifiIds:I

.field private final wifiIds:Landroid/util/SparseIntArray;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 14

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    new-instance v0, Landroid/util/SparseIntArray;

    invoke-direct {v0}, Landroid/util/SparseIntArray;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->wifiIds:Landroid/util/SparseIntArray;

    new-instance v0, Landroid/util/SparseIntArray;

    invoke-direct {v0}, Landroid/util/SparseIntArray;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->simIds:Landroid/util/SparseIntArray;

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-direct {v0, p0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;)V

    const-string v1, "wifi_icon_style"

    const-string v2, "sim_icon_style"

    const-string v3, "volte_icon_style"

    const-string v4, "vowifi_icon_style"

    filled-new-array {v1, v2, v3, v4}, [Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->addKeys([Ljava/lang/String;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    const/4 v0, 0x0

    new-array v1, v0, [I

    const/4 v2, 0x0

    const/4 v3, 0x0

    :goto_2a
    const-string v4, "_darkmode"

    const-string v5, "_tint"

    const-string v6, ""

    const/4 v7, 0x3

    const/4 v8, 0x1

    if-ge v3, v7, :cond_7d

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v9

    new-instance v10, Ljava/lang/StringBuilder;

    invoke-direct {v10}, Ljava/lang/StringBuilder;-><init>()V

    const-string v11, "stat_sys_signal_0"

    invoke-virtual {v10, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v10

    if-nez v3, :cond_47

    move-object v4, v6

    goto :goto_4b

    :cond_47
    if-ne v3, v8, :cond_4a

    goto :goto_4b

    :cond_4a
    move-object v4, v5

    :goto_4b
    invoke-virtual {v10, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-direct {p0, v4}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->getArrayId(Ljava/lang/String;)I

    move-result v4

    invoke-virtual {v9, v4}, Landroid/content/res/Resources;->obtainTypedArray(I)Landroid/content/res/TypedArray;

    move-result-object v4

    array-length v5, v1

    if-nez v5, :cond_65

    invoke-virtual {v4}, Landroid/content/res/TypedArray;->length()I

    move-result v5

    mul-int/2addr v5, v7

    new-array v1, v5, [I

    :cond_65
    const/4 v5, 0x0

    :goto_66
    invoke-virtual {v4}, Landroid/content/res/TypedArray;->length()I

    move-result v6

    if-ge v5, v6, :cond_77

    invoke-virtual {v4, v5, v0}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v6

    aput v6, v1, v2

    add-int/lit8 v5, v5, 0x1

    add-int/lit8 v2, v2, 0x1

    goto :goto_66

    :cond_77
    invoke-virtual {v4}, Landroid/content/res/TypedArray;->recycle()V

    add-int/lit8 v3, v3, 0x1

    goto :goto_2a

    :cond_7d
    iput-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->stokSimIds:[I

    new-array v1, v0, [I

    const/4 v2, 0x0

    const/4 v3, 0x0

    :goto_83
    if-ge v3, v7, :cond_cf

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v9

    new-instance v10, Ljava/lang/StringBuilder;

    invoke-direct {v10}, Ljava/lang/StringBuilder;-><init>()V

    const-string v11, "stat_sys_wifi_signal_0"

    invoke-virtual {v10, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v10

    if-nez v3, :cond_98

    move-object v11, v6

    goto :goto_9d

    :cond_98
    if-ne v3, v8, :cond_9c

    move-object v11, v4

    goto :goto_9d

    :cond_9c
    move-object v11, v5

    :goto_9d
    invoke-virtual {v10, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v10

    invoke-virtual {v10}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v10

    invoke-direct {p0, v10}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->getArrayId(Ljava/lang/String;)I

    move-result v10

    invoke-virtual {v9, v10}, Landroid/content/res/Resources;->obtainTypedArray(I)Landroid/content/res/TypedArray;

    move-result-object v9

    array-length v10, v1

    if-nez v10, :cond_b7

    invoke-virtual {v9}, Landroid/content/res/TypedArray;->length()I

    move-result v10

    mul-int/2addr v10, v7

    new-array v1, v10, [I

    :cond_b7
    const/4 v10, 0x0

    :goto_b8
    invoke-virtual {v9}, Landroid/content/res/TypedArray;->length()I

    move-result v11

    if-ge v10, v11, :cond_c9

    invoke-virtual {v9, v10, v0}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v11

    aput v11, v1, v2

    add-int/lit8 v10, v10, 0x1

    add-int/lit8 v2, v2, 0x1

    goto :goto_b8

    :cond_c9
    invoke-virtual {v9}, Landroid/content/res/TypedArray;->recycle()V

    add-int/lit8 v3, v3, 0x1

    goto :goto_83

    :cond_cf
    iput-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->stokWiFiIds:[I

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->initReplacement()V

    return-void
.end method

.method private getArrayId(Ljava/lang/String;)I
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->context:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->context:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v1

    const-string v2, "array"

    invoke-virtual {v0, p1, v2, v1}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v0

    return v0
.end method

.method private initReplacement()V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->initReplacementSim()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->initReplacementWiFi()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->initReplacementVoLte()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->initReplacementVoWifi()V

    return-void
.end method

.method private initReplacementSim()V
    .registers 14

    const-string v0, "sim_icon_style"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    const/4 v1, 0x0

    const/4 v2, 0x1

    if-eqz v0, :cond_c

    move v3, v2

    goto :goto_d

    :cond_c
    move v3, v1

    :goto_d
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->simIds:Landroid/util/SparseIntArray;

    invoke-virtual {v4}, Landroid/util/SparseIntArray;->clear()V

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "stat_sys_signal_"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-direct {p0, v4}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->getArrayId(Ljava/lang/String;)I

    move-result v4

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v6, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v7, "_darkmode"

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-direct {p0, v6}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->getArrayId(Ljava/lang/String;)I

    move-result v6

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v7, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v5

    const-string v7, "_tint"

    invoke-virtual {v5, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-direct {p0, v5}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->getArrayId(Ljava/lang/String;)I

    move-result v5

    if-eqz v3, :cond_b0

    if-lez v4, :cond_b0

    if-nez v6, :cond_66

    move v6, v4

    :cond_66
    if-nez v5, :cond_69

    move v5, v4

    :cond_69
    const/4 v7, 0x0

    iget-object v8, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->stokSimIds:[I

    array-length v8, v8

    new-array v8, v8, [I

    const/4 v9, 0x0

    :goto_70
    const/4 v10, 0x3

    if-ge v9, v10, :cond_9e

    iget-object v10, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->context:Landroid/content/Context;

    invoke-virtual {v10}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v10

    if-nez v9, :cond_7d

    move v11, v4

    goto :goto_82

    :cond_7d
    if-ne v9, v2, :cond_81

    move v11, v6

    goto :goto_82

    :cond_81
    move v11, v5

    :goto_82
    invoke-virtual {v10, v11}, Landroid/content/res/Resources;->obtainTypedArray(I)Landroid/content/res/TypedArray;

    move-result-object v10

    const/4 v11, 0x0

    :goto_87
    invoke-virtual {v10}, Landroid/content/res/TypedArray;->length()I

    move-result v12

    if-ge v11, v12, :cond_98

    invoke-virtual {v10, v11, v1}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v12

    aput v12, v8, v7

    add-int/lit8 v11, v11, 0x1

    add-int/lit8 v7, v7, 0x1

    goto :goto_87

    :cond_98
    invoke-virtual {v10}, Landroid/content/res/TypedArray;->recycle()V

    add-int/lit8 v9, v9, 0x1

    goto :goto_70

    :cond_9e
    const/4 v1, 0x0

    :goto_9f
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->stokSimIds:[I

    array-length v9, v2

    if-ge v1, v9, :cond_b0

    iget-object v9, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->simIds:Landroid/util/SparseIntArray;

    aget v2, v2, v1

    aget v10, v8, v1

    invoke-virtual {v9, v2, v10}, Landroid/util/SparseIntArray;->put(II)V

    add-int/lit8 v1, v1, 0x1

    goto :goto_9f

    :cond_b0
    return-void
.end method

.method private initReplacementVoLte()V
    .registers 5

    const-string v0, "volte_icon_style"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    if-nez v0, :cond_c

    const/4 v1, 0x0

    iput v1, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->volteIds:I

    return-void

    :cond_c
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->context:Landroid/content/Context;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "volte_style_"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/Utils/Utils;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->volteIds:I

    return-void
.end method

.method private initReplacementVoWifi()V
    .registers 5

    const-string v0, "vowifi_icon_style"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    if-nez v0, :cond_c

    const/4 v1, 0x0

    iput v1, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->vowifiIds:I

    return-void

    :cond_c
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->context:Landroid/content/Context;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "vowifi_style_"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/Utils/Utils;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->vowifiIds:I

    return-void
.end method

.method private initReplacementWiFi()V
    .registers 14

    const-string v0, "wifi_icon_style"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    const/4 v1, 0x0

    const/4 v2, 0x1

    if-eqz v0, :cond_c

    move v3, v2

    goto :goto_d

    :cond_c
    move v3, v1

    :goto_d
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->wifiIds:Landroid/util/SparseIntArray;

    invoke-virtual {v4}, Landroid/util/SparseIntArray;->clear()V

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "stat_sys_wifi_signal_"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-direct {p0, v4}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->getArrayId(Ljava/lang/String;)I

    move-result v4

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v6, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v7, "_darkmode"

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-direct {p0, v6}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->getArrayId(Ljava/lang/String;)I

    move-result v6

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v7, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v5

    const-string v7, "_tint"

    invoke-virtual {v5, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-direct {p0, v5}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->getArrayId(Ljava/lang/String;)I

    move-result v5

    if-nez v6, :cond_62

    move v6, v4

    :cond_62
    if-nez v5, :cond_65

    move v5, v4

    :cond_65
    if-eqz v3, :cond_b0

    if-lez v4, :cond_b0

    const/4 v7, 0x0

    iget-object v8, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->stokWiFiIds:[I

    array-length v8, v8

    new-array v8, v8, [I

    const/4 v9, 0x0

    :goto_70
    const/4 v10, 0x3

    if-ge v9, v10, :cond_9e

    iget-object v10, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->context:Landroid/content/Context;

    invoke-virtual {v10}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v10

    if-nez v9, :cond_7d

    move v11, v4

    goto :goto_82

    :cond_7d
    if-ne v9, v2, :cond_81

    move v11, v6

    goto :goto_82

    :cond_81
    move v11, v5

    :goto_82
    invoke-virtual {v10, v11}, Landroid/content/res/Resources;->obtainTypedArray(I)Landroid/content/res/TypedArray;

    move-result-object v10

    const/4 v11, 0x0

    :goto_87
    invoke-virtual {v10}, Landroid/content/res/TypedArray;->length()I

    move-result v12

    if-ge v11, v12, :cond_98

    invoke-virtual {v10, v11, v1}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v12

    aput v12, v8, v7

    add-int/lit8 v11, v11, 0x1

    add-int/lit8 v7, v7, 0x1

    goto :goto_87

    :cond_98
    invoke-virtual {v10}, Landroid/content/res/TypedArray;->recycle()V

    add-int/lit8 v9, v9, 0x1

    goto :goto_70

    :cond_9e
    const/4 v1, 0x0

    :goto_9f
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->stokWiFiIds:[I

    array-length v9, v2

    if-ge v1, v9, :cond_b0

    iget-object v9, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->wifiIds:Landroid/util/SparseIntArray;

    aget v2, v2, v1

    aget v10, v8, v1

    invoke-virtual {v9, v2, v10}, Landroid/util/SparseIntArray;->put(II)V

    add-int/lit8 v1, v1, 0x1

    goto :goto_9f

    :cond_b0
    return-void
.end method

.method private onChange()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->callBacks:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_6
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_18

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/controllers/CustomIconController$CallBack;

    if-eqz v1, :cond_17

    invoke-interface {v1}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController$CallBack;->onIconStyleChange()V

    :cond_17
    goto :goto_6

    :cond_18
    return-void
.end method


# virtual methods
.method public getSimIds(I)I
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->simIds:Landroid/util/SparseIntArray;

    invoke-virtual {v0, p1, p1}, Landroid/util/SparseIntArray;->get(II)I

    move-result v0

    return v0
.end method

.method public getVoLteIds(I)I
    .registers 3

    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->volteIds:I

    if-lez v0, :cond_5

    goto :goto_6

    :cond_5
    move v0, p1

    :goto_6
    return v0
.end method

.method public getVoWifiIds(I)I
    .registers 3

    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->vowifiIds:I

    if-lez v0, :cond_5

    goto :goto_6

    :cond_5
    move v0, p1

    :goto_6
    return v0
.end method

.method public getWiFiIds(I)I
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->wifiIds:Landroid/util/SparseIntArray;

    invoke-virtual {v0, p1, p1}, Landroid/util/SparseIntArray;->get(II)I

    move-result v0

    return v0
.end method

.method public onSettingsChange()V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->initReplacement()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->onChange()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_CustomIconController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
