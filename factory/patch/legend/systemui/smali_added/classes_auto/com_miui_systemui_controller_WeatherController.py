"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/miui/systemui/controller/WeatherController.smali'
CLASS_FALLBACK_NAMES = ['WeatherController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public final Lcom/miui/systemui/controller/WeatherController;
.super Ljava/lang/Object;


# static fields
.field public static final sProjection:[Ljava/lang/String;


# instance fields
.field public final mContext:Landroid/content/Context;

.field public mEnabled:Z

.field public final mEnabledObserver:Landroid/database/ContentObserver;

.field public final mHandler:Landroid/os/Handler;

.field public final mListeners:Ljava/util/List;

.field public final mPackageChangeReceiver:Landroid/content/BroadcastReceiver;

.field public mQueryHandler:Lcom/miui/systemui/controller/WeatherController$QueryHandler;

.field public mWeatherInfo:Lcom/miui/systemui/controller/WeatherController$WeatherInfo;

.field public final mWeatherObserver:Landroid/database/ContentObserver;


# direct methods
.method public static constructor <clinit>()V
    .registers 4

    const-string v0, "city_name"

    const-string v1, "description"

    const-string/jumbo v2, "temperature"

    const-string/jumbo v3, "temperature_unit"

    filled-new-array {v0, v1, v2, v3}, [Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/miui/systemui/controller/WeatherController;->sProjection:[Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/miui/systemui/controller/WeatherController;->mContext:Landroid/content/Context;

    new-instance p1, Landroid/os/Handler;

    invoke-direct {p1}, Landroid/os/Handler;-><init>()V

    iput-object p1, p0, Lcom/miui/systemui/controller/WeatherController;->mHandler:Landroid/os/Handler;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mListeners:Ljava/util/List;

    new-instance v0, Lcom/miui/systemui/controller/WeatherController$1;

    invoke-direct {v0, p0, p1}, Lcom/miui/systemui/controller/WeatherController$1;-><init>(Lcom/miui/systemui/controller/WeatherController;Landroid/os/Handler;)V

    iput-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mEnabledObserver:Landroid/database/ContentObserver;

    new-instance v0, Lcom/miui/systemui/controller/WeatherController$2;

    invoke-direct {v0, p0}, Lcom/miui/systemui/controller/WeatherController$2;-><init>(Lcom/miui/systemui/controller/WeatherController;)V

    iput-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mPackageChangeReceiver:Landroid/content/BroadcastReceiver;

    new-instance v0, Lcom/miui/systemui/controller/WeatherController$3;

    invoke-direct {v0, p0, p1}, Lcom/miui/systemui/controller/WeatherController$3;-><init>(Lcom/miui/systemui/controller/WeatherController;Landroid/os/Handler;)V

    iput-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mWeatherObserver:Landroid/database/ContentObserver;

    return-void
.end method


# virtual methods
.method public final addCallback(Lcom/miui/systemui/controller/WeatherController$WeatherChangeListener;)V
    .registers 3

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mListeners:Ljava/util/List;

    invoke-interface {v0}, Ljava/util/List;->isEmpty()Z

    move-result v0

    if-eqz v0, :cond_b

    invoke-virtual {p0}, Lcom/miui/systemui/controller/WeatherController;->register()V

    :cond_b
    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mListeners:Ljava/util/List;

    invoke-interface {v0, p1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mWeatherInfo:Lcom/miui/systemui/controller/WeatherController$WeatherInfo;

    invoke-interface {p1, v0}, Lcom/miui/systemui/controller/WeatherController$WeatherChangeListener;->onWeatherChange(Lcom/miui/systemui/controller/WeatherController$WeatherInfo;)V

    return-void
.end method

.method public final getWeatherInfo()Lcom/miui/systemui/controller/WeatherController$WeatherInfo;
    .registers 1

    iget-object p0, p0, Lcom/miui/systemui/controller/WeatherController;->mWeatherInfo:Lcom/miui/systemui/controller/WeatherController$WeatherInfo;

    return-object p0
.end method

.method public final maybeAddUserId(Landroid/net/Uri;I)Landroid/net/Uri;
    .registers 5

    if-eqz p1, :cond_3f

    const/4 v0, -0x2

    if-eq p2, v0, :cond_3f

    const-string v0, "content"

    invoke-virtual {p1}, Landroid/net/Uri;->getScheme()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_3f

    invoke-virtual {p0, p1}, Lcom/miui/systemui/controller/WeatherController;->uriHasUserId(Landroid/net/Uri;)Z

    move-result p0

    if-nez p0, :cond_3f

    invoke-virtual {p1}, Landroid/net/Uri;->buildUpon()Landroid/net/Uri$Builder;

    move-result-object p0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, ""

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v1, "@"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Landroid/net/Uri;->getEncodedAuthority()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p0, v0}, Landroid/net/Uri$Builder;->encodedAuthority(Ljava/lang/String;)Landroid/net/Uri$Builder;

    invoke-virtual {p0}, Landroid/net/Uri$Builder;->build()Landroid/net/Uri;

    move-result-object p1

    :cond_3f
    return-object p1
.end method

.method public final notifyListeners()V
    .registers 4

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mListeners:Ljava/util/List;

    invoke-interface {v0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_6
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_18

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/miui/systemui/controller/WeatherController$WeatherChangeListener;

    iget-object v2, p0, Lcom/miui/systemui/controller/WeatherController;->mWeatherInfo:Lcom/miui/systemui/controller/WeatherController$WeatherInfo;

    invoke-interface {v1, v2}, Lcom/miui/systemui/controller/WeatherController$WeatherChangeListener;->onWeatherChange(Lcom/miui/systemui/controller/WeatherController$WeatherInfo;)V

    goto :goto_6

    :cond_18
    return-void
.end method

.method public final register()V
    .registers 7

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string/jumbo v1, "status_bar_show_weather"

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    const/4 v2, 0x0

    iget-object v3, p0, Lcom/miui/systemui/controller/WeatherController;->mEnabledObserver:Landroid/database/ContentObserver;

    invoke-static {}, Landroid/app/ActivityManager;->getCurrentUser()I

    move-result v4

    invoke-virtual {v0, v1, v2, v3, v4}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-virtual {v3, v2}, Landroid/database/ContentObserver;->onChange(Z)V

    new-instance v3, Landroid/content/IntentFilter;

    invoke-direct {v3}, Landroid/content/IntentFilter;-><init>()V

    const-string v0, "android.intent.action.PACKAGE_ADDED"

    invoke-virtual {v3, v0}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v0, "android.intent.action.PACKAGE_CHANGED"

    invoke-virtual {v3, v0}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v0, "android.intent.action.PACKAGE_REMOVED"

    invoke-virtual {v3, v0}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v0, "android.intent.action.PACKAGE_REPLACED"

    invoke-virtual {v3, v0}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v0, "package"

    invoke-virtual {v3, v0}, Landroid/content/IntentFilter;->addDataScheme(Ljava/lang/String;)V

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mContext:Landroid/content/Context;

    iget-object v1, p0, Lcom/miui/systemui/controller/WeatherController;->mPackageChangeReceiver:Landroid/content/BroadcastReceiver;

    sget-object v2, Landroid/os/UserHandle;->ALL:Landroid/os/UserHandle;

    const/4 v4, 0x0

    const/4 v5, 0x0

    invoke-virtual/range {v0 .. v5}, Landroid/content/Context;->registerReceiverAsUser(Landroid/content/BroadcastReceiver;Landroid/os/UserHandle;Landroid/content/IntentFilter;Ljava/lang/String;Landroid/os/Handler;)Landroid/content/Intent;

    return-void
.end method

.method public final registerObserver()V
    .registers 6

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mQueryHandler:Lcom/miui/systemui/controller/WeatherController$QueryHandler;

    if-nez v0, :cond_1c

    new-instance v0, Lcom/miui/systemui/controller/WeatherController$QueryHandler;

    iget-object v1, p0, Lcom/miui/systemui/controller/WeatherController;->mContext:Landroid/content/Context;

    invoke-direct {v0, p0, v1}, Lcom/miui/systemui/controller/WeatherController$QueryHandler;-><init>(Lcom/miui/systemui/controller/WeatherController;Landroid/content/Context;)V

    iput-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mQueryHandler:Lcom/miui/systemui/controller/WeatherController$QueryHandler;

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    sget-object v1, Lmiui/provider/Weather$LocalWeather;->CONTENT_URI:Landroid/net/Uri;

    const/4 v2, 0x1

    iget-object v3, p0, Lcom/miui/systemui/controller/WeatherController;->mWeatherObserver:Landroid/database/ContentObserver;

    const/4 v4, -0x2

    invoke-virtual {v0, v1, v2, v3, v4}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    :cond_1c
    return-void
.end method

.method public final removeCallback(Lcom/miui/systemui/controller/WeatherController$WeatherChangeListener;)V
    .registers 3

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mListeners:Ljava/util/List;

    invoke-interface {v0, p1}, Ljava/util/List;->remove(Ljava/lang/Object;)Z

    iget-object p1, p0, Lcom/miui/systemui/controller/WeatherController;->mListeners:Ljava/util/List;

    invoke-interface {p1}, Ljava/util/List;->isEmpty()Z

    move-result p1

    if-eqz p1, :cond_10

    invoke-virtual {p0}, Lcom/miui/systemui/controller/WeatherController;->unregister()V

    :cond_10
    return-void
.end method

.method public final startQuery()V
    .registers 9

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mQueryHandler:Lcom/miui/systemui/controller/WeatherController$QueryHandler;

    if-eqz v0, :cond_1c

    const/16 v1, 0x64

    invoke-virtual {v0, v1}, Lcom/miui/systemui/controller/WeatherController$QueryHandler;->cancelOperation(I)V

    const/4 v2, 0x0

    sget-object v3, Lmiui/provider/Weather$LocalWeather;->CONTENT_URI:Landroid/net/Uri;

    invoke-static {}, Landroid/app/ActivityManager;->getCurrentUser()I

    move-result v4

    invoke-virtual {p0, v3, v4}, Lcom/miui/systemui/controller/WeatherController;->maybeAddUserId(Landroid/net/Uri;I)Landroid/net/Uri;

    move-result-object v3

    sget-object v4, Lcom/miui/systemui/controller/WeatherController;->sProjection:[Ljava/lang/String;

    move-object v5, v2

    move-object v6, v2

    move-object v7, v2

    invoke-virtual/range {v0 .. v7}, Lcom/miui/systemui/controller/WeatherController$QueryHandler;->startQuery(ILjava/lang/Object;Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)V

    :cond_1c
    return-void
.end method

.method public final unregister()V
    .registers 3

    invoke-virtual {p0}, Lcom/miui/systemui/controller/WeatherController;->unregisterObserver()V

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mContext:Landroid/content/Context;

    iget-object v1, p0, Lcom/miui/systemui/controller/WeatherController;->mPackageChangeReceiver:Landroid/content/BroadcastReceiver;

    invoke-virtual {v0, v1}, Landroid/content/Context;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object p0, p0, Lcom/miui/systemui/controller/WeatherController;->mEnabledObserver:Landroid/database/ContentObserver;

    invoke-virtual {v0, p0}, Landroid/content/ContentResolver;->unregisterContentObserver(Landroid/database/ContentObserver;)V

    return-void
.end method

.method public final unregisterObserver()V
    .registers 4

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mQueryHandler:Lcom/miui/systemui/controller/WeatherController$QueryHandler;

    const/4 v2, 0x0

    if-eqz v0, :cond_12

    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/miui/systemui/controller/WeatherController;->mWeatherObserver:Landroid/database/ContentObserver;

    invoke-virtual {v0, v1}, Landroid/content/ContentResolver;->unregisterContentObserver(Landroid/database/ContentObserver;)V

    iput-object v2, p0, Lcom/miui/systemui/controller/WeatherController;->mQueryHandler:Lcom/miui/systemui/controller/WeatherController$QueryHandler;

    :cond_12
    iput-object v2, p0, Lcom/miui/systemui/controller/WeatherController;->mWeatherInfo:Lcom/miui/systemui/controller/WeatherController$WeatherInfo;

    invoke-virtual {p0}, Lcom/miui/systemui/controller/WeatherController;->notifyListeners()V

    return-void
.end method

.method public final updateState()V
    .registers 4

    iget-boolean v0, p0, Lcom/miui/systemui/controller/WeatherController;->mEnabled:Z

    if-eqz v0, :cond_28

    :try_start_4
    iget-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v0

    const-string v1, "com.miui.weather2"

    const/4 v2, 0x0

    invoke-virtual {v0, v1, v2}, Landroid/content/pm/PackageManager;->getApplicationInfo(Ljava/lang/String;I)Landroid/content/pm/ApplicationInfo;

    move-result-object v1

    iget-boolean v1, v1, Landroid/content/pm/ApplicationInfo;->enabled:Z

    if-eqz v1, :cond_28

    const-string/jumbo v1, "weather"

    const v2, 0xc0e00

    invoke-virtual {v0, v1, v2}, Landroid/content/pm/PackageManager;->resolveContentProvider(Ljava/lang/String;I)Landroid/content/pm/ProviderInfo;
    :try_end_1e
    .catch Ljava/lang/Exception; {:try_start_4 .. :try_end_1e} :catch_2c

    move-result-object v0

    if-eqz v0, :cond_28

    invoke-virtual {p0}, Lcom/miui/systemui/controller/WeatherController;->registerObserver()V

    invoke-virtual {p0}, Lcom/miui/systemui/controller/WeatherController;->startQuery()V

    return-void

    :cond_28
    :goto_28
    invoke-virtual {p0}, Lcom/miui/systemui/controller/WeatherController;->unregisterObserver()V

    return-void

    :catch_2c
    move-exception v0

    goto :goto_28
.end method

.method public final updateWeather(Landroid/database/Cursor;)V
    .registers 5

    if-nez p1, :cond_b

    const-string v0, "WeatherController"

    const-string/jumbo v1, "updateWeather cursor is null!"

    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_b
    :try_start_b
    invoke-interface {p1}, Landroid/database/Cursor;->moveToFirst()Z

    move-result v0

    if-nez v0, :cond_15

    const/4 v0, 0x0

    iput-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mWeatherInfo:Lcom/miui/systemui/controller/WeatherController$WeatherInfo;

    goto :goto_4e

    :cond_15
    new-instance v0, Lcom/miui/systemui/controller/WeatherController$WeatherInfo;

    invoke-direct {v0}, Lcom/miui/systemui/controller/WeatherController$WeatherInfo;-><init>()V

    const-string v1, "city_name"

    invoke-interface {p1, v1}, Landroid/database/Cursor;->getColumnIndex(Ljava/lang/String;)I

    move-result v1

    invoke-interface {p1, v1}, Landroid/database/Cursor;->getString(I)Ljava/lang/String;

    move-result-object v1

    iput-object v1, v0, Lcom/miui/systemui/controller/WeatherController$WeatherInfo;->cityName:Ljava/lang/String;

    const-string v1, "description"

    invoke-interface {p1, v1}, Landroid/database/Cursor;->getColumnIndex(Ljava/lang/String;)I

    move-result v1

    invoke-interface {p1, v1}, Landroid/database/Cursor;->getString(I)Ljava/lang/String;

    move-result-object v1

    iput-object v1, v0, Lcom/miui/systemui/controller/WeatherController$WeatherInfo;->description:Ljava/lang/String;

    const-string/jumbo v1, "temperature"

    invoke-interface {p1, v1}, Landroid/database/Cursor;->getColumnIndex(Ljava/lang/String;)I

    move-result v1

    invoke-interface {p1, v1}, Landroid/database/Cursor;->getInt(I)I

    move-result v1

    iput v1, v0, Lcom/miui/systemui/controller/WeatherController$WeatherInfo;->temperature:I

    const-string/jumbo v1, "temperature_unit"

    invoke-interface {p1, v1}, Landroid/database/Cursor;->getColumnIndex(Ljava/lang/String;)I

    move-result v1

    invoke-interface {p1, v1}, Landroid/database/Cursor;->getInt(I)I

    move-result v1

    iput v1, v0, Lcom/miui/systemui/controller/WeatherController$WeatherInfo;->temperatureUnit:I

    iput-object v0, p0, Lcom/miui/systemui/controller/WeatherController;->mWeatherInfo:Lcom/miui/systemui/controller/WeatherController$WeatherInfo;
    :try_end_4e
    .catch Ljava/lang/Exception; {:try_start_b .. :try_end_4e} :catch_55

    :goto_4e
    invoke-static {p1}, Llibcore/io/IoUtils;->closeQuietly(Ljava/lang/AutoCloseable;)V

    invoke-virtual {p0}, Lcom/miui/systemui/controller/WeatherController;->notifyListeners()V

    return-void

    :catch_55
    move-exception v2

    const-string v0, "WeatherController"

    const-string/jumbo v1, "updateWeather failed!"

    invoke-static {v0, v1, v2}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    goto :goto_4e
.end method

.method public final uriHasUserId(Landroid/net/Uri;)Z
    .registers 2

    if-eqz p1, :cond_e

    invoke-virtual {p1}, Landroid/net/Uri;->getUserInfo()Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p0

    if-nez p0, :cond_e

    const/4 p0, 0x1

    return p0

    :cond_e
    const/4 p0, 0x0

    return p0
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_miui_systemui_controller_WeatherController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
