"""
Legend MTCR patch - class-level rule.

Target JAR   : framework.jar
Target class : android/preference/MiuiCoreSettingsPreference
Source MTCR  : Framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "framework.jar"
TARGET_CLASS = "android/preference/MiuiCoreSettingsPreference.smali"

PATCHES = [
    {
        "id":          "add_class_android_preference_MiuiCoreSettingsPreference",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public Landroid/preference/MiuiCoreSettingsPreference;
.super Ljava/lang/Object;


# instance fields
.field private attrs:Landroid/util/AttributeSet;

.field private mContext:Landroid/content/Context;

.field private mIntent:Ljava/lang/String;

.field private mKey:Ljava/lang/String;

.field public mStorageType:I


# direct methods
.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static LaunchCustomApplication(Landroid/content/Context;Ljava/lang/String;)V
    .registers 5

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    invoke-static {v2, p1}, Landroid/provider/Settings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v2

    invoke-virtual {v2, v1}, Landroid/content/pm/PackageManager;->getLaunchIntentForPackage(Ljava/lang/String;)Landroid/content/Intent;

    move-result-object v0

    if-eqz v0, :cond_0

    const/high16 v2, 0x10000000

    invoke-virtual {v0, v2}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    invoke-virtual {p0, v0}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V

    :cond_0
    return-void
.end method

.method private SelectStorage(Ljava/lang/String;)I
    .registers 5

    const/4 v0, 0x0

    if-eqz p1, :cond_3

    const-string v2, "global"

    invoke-virtual {p1, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-nez v2, :cond_0

    const-string v2, "Global"

    invoke-virtual {p1, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_1

    :cond_0
    const/4 v0, 0x1

    move v1, v0

    :goto_0
    return v1

    :cond_1
    const-string v2, "secure"

    invoke-virtual {p1, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-nez v2, :cond_2

    const-string v2, "Secure"

    invoke-virtual {p1, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_3

    :cond_2
    const/4 v0, 0x2

    move v1, v0

    goto :goto_0

    :cond_3
    move v1, v0

    goto :goto_0
.end method

.method public static gKP(Ljava/lang/String;Landroid/content/Context;)I
    .registers 6

    const/4 v1, 0x0

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    invoke-static {v2, p0, v1}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    return v1
.end method

.method public static gKS(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;
    .registers 6

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    invoke-static {v2, p0}, Landroid/provider/Settings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    return-object v1
.end method

.method public static gKT(Ljava/lang/String;Landroid/content/Context;)J
    .registers 8

    const-wide/16 v2, 0x1f4

    const/4 v5, 0x0

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    invoke-static {v1, p0, v2, v3}, Landroid/provider/Settings$System;->getLong(Landroid/content/ContentResolver;Ljava/lang/String;J)J

    move-result-wide v2

    return-wide v2
.end method

.method public static getKeyAktif(Landroid/content/Context;Ljava/lang/String;)I
    .registers 4

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const/4 v1, 0x1

    invoke-static {v0, p1, v1}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    return v0
.end method

.method public static getKeyParam(Landroid/content/Context;Ljava/lang/String;)I
    .registers 4

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const/4 v1, 0x0

    invoke-static {v0, p1, v1}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    return v0
.end method

.method public static getKeyTime(Landroid/content/Context;Ljava/lang/String;)J
    .registers 6

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-wide/16 v2, 0x1f4

    invoke-static {v0, p1, v2, v3}, Landroid/provider/Settings$System;->getLong(Landroid/content/ContentResolver;Ljava/lang/String;J)J

    move-result-wide v0

    return-wide v0
.end method

.method public static lCA(Ljava/lang/String;Landroid/content/Context;)V
    .registers 8

    const/4 v5, 0x0

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v3

    invoke-static {v3, p0}, Landroid/provider/Settings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p1}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v3

    invoke-virtual {v3, v1}, Landroid/content/pm/PackageManager;->getLaunchIntentForPackage(Ljava/lang/String;)Landroid/content/Intent;

    move-result-object v0

    if-eqz v0, :cond_0

    const/high16 v3, 0x10000000

    invoke-virtual {v0, v3}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    invoke-virtual {p1, v0}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V

    :cond_0
    return-void
.end method


# virtual methods
.method public DrawableToID(Ljava/lang/String;)I
    .registers 5

    iget-object v0, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const-string v1, "drawable"

    const-string v2, "android"

    invoke-virtual {v0, p1, v1, v2}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v0

    return v0
.end method

.method public IDtoID(Ljava/lang/String;)I
    .registers 5

    iget-object v0, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const-string v1, "id"

    const-string v2, "android"

    invoke-virtual {v0, p1, v1, v2}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v0

    return v0
.end method

.method public LayoutToID(Ljava/lang/String;)I
    .registers 5

    iget-object v0, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const-string v1, "layout"

    const-string v2, "android"

    invoke-virtual {v0, p1, v1, v2}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v0

    return v0
.end method

.method public StyleToID(Ljava/lang/String;)I
    .registers 5

    iget-object v0, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const-string v1, "style"

    const-string v2, "android"

    invoke-virtual {v0, p1, v1, v2}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v0

    return v0
.end method

.method public getAttributeInt(Ljava/lang/String;I)I
    .registers 5

    iget-object v0, p0, Landroid/preference/MiuiCoreSettingsPreference;->attrs:Landroid/util/AttributeSet;

    const/4 v1, 0x0

    invoke-interface {v0, v1, p1, p2}, Landroid/util/AttributeSet;->getAttributeIntValue(Ljava/lang/String;Ljava/lang/String;I)I

    move-result v0

    return v0
.end method

.method public getAttributeValue(Ljava/lang/String;)Ljava/lang/String;
    .registers 4

    iget-object v0, p0, Landroid/preference/MiuiCoreSettingsPreference;->attrs:Landroid/util/AttributeSet;

    const/4 v1, 0x0

    invoke-interface {v0, v1, p1}, Landroid/util/AttributeSet;->getAttributeValue(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method

.method public getIntegerValue(I)Ljava/lang/Integer;
    .registers 7

    :try_start_0
    iget v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mStorageType:I
    :try_end_0
    .catch Landroid/provider/Settings$SettingNotFoundException; {:try_start_0 .. :try_end_0} :catch_0

    packed-switch v2, :pswitch_data_0

    :goto_0
    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    :goto_1
    return-object v2

    :pswitch_0  #0x0
    :try_start_1
    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v2, v3}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;)I

    move-result v2

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    goto :goto_1

    :pswitch_1  #0x1
    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v2, v3}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;)I

    move-result v2

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    goto :goto_1

    :pswitch_2  #0x2
    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v2, v3}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;)I

    move-result v2

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;
    :try_end_1
    .catch Landroid/provider/Settings$SettingNotFoundException; {:try_start_1 .. :try_end_1} :catch_0

    move-result-object v2

    goto :goto_1

    :catch_0
    move-exception v0

    invoke-virtual {p0, p1}, Landroid/preference/MiuiCoreSettingsPreference;->setIntegerValue(I)V

    goto :goto_0

    :pswitch_data_0
    .packed-switch 0x0
        :pswitch_0  #00000000
        :pswitch_1  #00000001
        :pswitch_2  #00000002
    .end packed-switch
.end method

.method public getStringValue()Ljava/lang/String;
    .registers 5

    const/4 v3, 0x0

    iget v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mStorageType:I

    packed-switch v1, :pswitch_data_0

    const/4 v1, 0x0

    :goto_0
    return-object v1

    :pswitch_0  #0x0
    iget-object v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v1, v2}, Landroid/provider/Settings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    goto :goto_0

    :pswitch_1  #0x1
    iget-object v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v1, v2}, Landroid/provider/Settings$Global;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    goto :goto_0

    :pswitch_2  #0x2
    iget-object v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v1, v2}, Landroid/provider/Settings$Secure;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    goto :goto_0

    nop

    :pswitch_data_0
    .packed-switch 0x0
        :pswitch_0  #00000000
        :pswitch_1  #00000001
        :pswitch_2  #00000002
    .end packed-switch
.end method

.method public getStringValue(Ljava/lang/String;)Ljava/lang/String;
    .registers 7

    const/4 v4, 0x0

    const/4 v1, 0x0

    iget v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mStorageType:I

    packed-switch v2, :pswitch_data_0

    :goto_0
    if-eqz v1, :cond_0

    :goto_1
    return-object v1

    :pswitch_0  #0x0
    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v2, v3}, Landroid/provider/Settings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    goto :goto_0

    :pswitch_1  #0x1
    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v2, v3}, Landroid/provider/Settings$Global;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    goto :goto_0

    :pswitch_2  #0x2
    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v2, v3}, Landroid/provider/Settings$Secure;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    goto :goto_0

    :cond_0
    move-object v1, p1

    goto :goto_1

    nop

    :pswitch_data_0
    .packed-switch 0x0
        :pswitch_0  #00000000
        :pswitch_1  #00000001
        :pswitch_2  #00000002
    .end packed-switch
.end method

.method public initSummary(Ljava/lang/CharSequence;)[Ljava/lang/String;
    .registers 6

    const/4 v3, 0x0

    const/4 v2, 0x2

    new-array v0, v2, [Ljava/lang/String;

    invoke-interface {p1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v2, "%s"

    invoke-virtual {v1, v2}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v2

    invoke-virtual {v1, v3, v2}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v2

    aput-object v2, v0, v3

    const/4 v2, 0x1

    const-string v3, "%s"

    invoke-virtual {v1, v3}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v3

    add-int/lit8 v3, v3, 0x2

    invoke-virtual {v1, v3}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v3

    aput-object v3, v0, v2

    return-object v0
.end method

.method public initialization(Landroid/content/Context;Landroid/util/AttributeSet;Ljava/lang/String;)V
    .registers 5

    iput-object p1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    iput-object p2, p0, Landroid/preference/MiuiCoreSettingsPreference;->attrs:Landroid/util/AttributeSet;

    iput-object p3, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    const-string v0, "intent"

    invoke-virtual {p0, v0}, Landroid/preference/MiuiCoreSettingsPreference;->getAttributeValue(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Landroid/preference/MiuiCoreSettingsPreference;->mIntent:Ljava/lang/String;

    const-string v0, "storage"

    invoke-virtual {p0, v0}, Landroid/preference/MiuiCoreSettingsPreference;->getAttributeValue(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    invoke-direct {p0, v0}, Landroid/preference/MiuiCoreSettingsPreference;->SelectStorage(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Landroid/preference/MiuiCoreSettingsPreference;->mStorageType:I

    return-void
.end method

.method public sendIntent()V
    .registers 5

    const/4 v3, 0x0

    iget-object v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mIntent:Ljava/lang/String;

    if-eqz v1, :cond_0

    iget-object v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    new-instance v2, Landroid/content/Intent;

    iget-object v3, p0, Landroid/preference/MiuiCoreSettingsPreference;->mIntent:Ljava/lang/String;

    invoke-direct {v2, v3}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    invoke-virtual {v1, v2}, Landroid/content/Context;->sendBroadcast(Landroid/content/Intent;)V

    :cond_0
    return-void
.end method

.method public setBridge(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    if-eqz p1, :cond_0

    iput-object p1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    :cond_0
    if-eqz p2, :cond_1

    iput-object p2, p0, Landroid/preference/MiuiCoreSettingsPreference;->attrs:Landroid/util/AttributeSet;

    :cond_1
    return-void
.end method

.method public setIntegerValue(I)V
    .registers 6

    const/4 v3, 0x0

    iget v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mStorageType:I

    packed-switch v1, :pswitch_data_0

    :goto_0
    return-void

    :pswitch_0  #0x0
    iget-object v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v1, v2, p1}, Landroid/provider/Settings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    goto :goto_0

    :pswitch_1  #0x1
    iget-object v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v1, v2, p1}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    goto :goto_0

    :pswitch_2  #0x2
    iget-object v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v1, v2, p1}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    goto :goto_0

    nop

    :pswitch_data_0
    .packed-switch 0x0
        :pswitch_0  #00000000
        :pswitch_1  #00000001
        :pswitch_2  #00000002
    .end packed-switch
.end method

.method public setStringValue(Ljava/lang/String;)V
    .registers 6

    const/4 v3, 0x0

    iget v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mStorageType:I

    packed-switch v1, :pswitch_data_0

    :goto_0
    return-void

    :pswitch_0  #0x0
    iget-object v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v1, v2, p1}, Landroid/provider/Settings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    goto :goto_0

    :pswitch_1  #0x1
    iget-object v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v1, v2, p1}, Landroid/provider/Settings$Global;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    goto :goto_0

    :pswitch_2  #0x2
    iget-object v1, p0, Landroid/preference/MiuiCoreSettingsPreference;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Landroid/preference/MiuiCoreSettingsPreference;->mKey:Ljava/lang/String;

    invoke-static {v1, v2, p1}, Landroid/provider/Settings$Secure;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    goto :goto_0

    nop

    :pswitch_data_0
    .packed-switch 0x0
        :pswitch_0  #00000000
        :pswitch_1  #00000001
        :pswitch_2  #00000002
    .end packed-switch
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from Framework_Legend.mtcr",
    },
]
