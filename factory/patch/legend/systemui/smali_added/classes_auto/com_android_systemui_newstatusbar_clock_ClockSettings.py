"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/ClockSettings.smali'
CLASS_FALLBACK_NAMES = ['ClockSettings.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/clock/ClockSettings;
.super Landroid/database/ContentObserver;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;
    }
.end annotation


# instance fields
.field private clockData:Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

.field private final key:Ljava/lang/String;

.field private final layout:Lcom/android/systemui/newstatusbar/clock/IClock;


# direct methods
.method public constructor <init>(Lcom/android/systemui/newstatusbar/clock/IClock;Ljava/lang/String;)V
    .registers 5

    new-instance v0, Landroid/os/Handler;

    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;

    move-result-object v1

    invoke-direct {v0, v1}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V

    invoke-direct {p0, v0}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->layout:Lcom/android/systemui/newstatusbar/clock/IClock;

    iput-object p2, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->key:Ljava/lang/String;

    return-void
.end method

.method private getUri(Ljava/lang/String;)Landroid/net/Uri;
    .registers 4

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->key:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    return-object v0
.end method


# virtual methods
.method public equals(Ljava/lang/Object;)Z
    .registers 5

    if-ne p0, p1, :cond_4

    const/4 v0, 0x1

    return v0

    :cond_4
    if-eqz p1, :cond_1d

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v1

    if-eq v0, v1, :cond_11

    goto :goto_1d

    :cond_11
    move-object v0, p1

    check-cast v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->key:Ljava/lang/String;

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->key:Ljava/lang/String;

    invoke-static {v1, v2}, Ljava/util/Objects;->equals(Ljava/lang/Object;Ljava/lang/Object;)Z

    move-result v1

    return v1

    :cond_1d
    :goto_1d
    const/4 v0, 0x0

    return v0
.end method

.method public getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->clockData:Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    return-object v0
.end method

.method public hashCode()I
    .registers 4

    const/4 v0, 0x1

    new-array v0, v0, [Ljava/lang/Object;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->key:Ljava/lang/String;

    const/4 v2, 0x0

    aput-object v1, v0, v2

    invoke-static {v0}, Ljava/util/Objects;->hash([Ljava/lang/Object;)I

    move-result v0

    return v0
.end method

.method public onChange(Z)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->clockData:Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    if-eqz v0, :cond_7

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->update()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    :cond_7
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->layout:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->updateSettings()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->layout:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->fullInvalidate()V

    return-void
.end method

.method public register()V
    .registers 4

    new-instance v0, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->layout:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v1}, Lcom/android/systemui/newstatusbar/clock/IClock;->getContext()Landroid/content/Context;

    move-result-object v1

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->key:Ljava/lang/String;

    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->clockData:Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->update()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->layout:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    sget-object v1, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->SettingsKeyAnim:Ljava/lang/String;

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getUri(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    const/4 v2, 0x0

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    sget-object v1, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->SettingsKeyDots:Ljava/lang/String;

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getUri(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    sget-object v1, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->SettingsKeySecond:Ljava/lang/String;

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getUri(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    const-string v1, "status_clock_typefase"

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    const-string v1, "status_clock_typefasestyle"

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    const-string v1, "_division"

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getUri(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    const-string v1, "_color"

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getUri(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    const-string v1, "_zoom"

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getUri(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    const-string v1, "statusbar_clock_style"

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    return-void
.end method

.method public unRegister()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->layout:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    invoke-virtual {v0, p0}, Landroid/content/ContentResolver;->unregisterContentObserver(Landroid/database/ContentObserver;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_ClockSettings',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
