"""
Legend MTCR patch - class-level rule.

Target JAR   : services.jar
Target class : com/android/server/location/LocationManagerService
Source MTCR  : Service_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "services.jar"
TARGET_CLASS = "com/android/server/location/LocationManagerService.smali"
CLASS_FALLBACK_NAMES = ['LocationManagerService.smali']
CLASS_ANCHORS        = ['Lcom/android/server/location/provider/LocationProviderManager$StateChangedListener;', 'Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;', 'Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;', 'Lcom/android/server/location/provider/proxy/ProxyLocationProvider;', 'Lcom/android/server/location/provider/LocationProviderManager;', 'Lcom/android/server/location/fudger/LocationFudgerCache;']

PATCHES = [
    {
        "id":          "replace_method_addLocationProviderManager_Lcom_android_server_location_prov",
        "method":      ".method addLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;Lcom/android/server/location/provider/AbstractLocationProvider;)V",
        "method_name": 'addLocationProviderManager',
        "type":        "method_replace",
        "search": """\
.method addLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;Lcom/android/server/location/provider/AbstractLocationProvider;)V
    .registers 9

    iget-object v0, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    monitor-enter v0

    :try_start_0
    invoke-virtual {p1}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p0, v1}, Lcom/android/server/location/LocationManagerService;->getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object v1

    const/4 v2, 0x1

    const/4 v3, 0x0

    if-nez v1, :cond_0

    move v1, v2

    goto :goto_0

    :cond_0
    move v1, v3

    :goto_0
    invoke-static {v1}, Lcom/android/internal/util/Preconditions;->checkState(Z)V

    invoke-virtual {p1, p0}, Lcom/android/server/location/provider/LocationProviderManager;->startManager(Lcom/android/server/location/provider/LocationProviderManager$StateChangedListener;)V

    if-eqz p2, :cond_6

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mPassiveManager:Lcom/android/server/location/provider/PassiveLocationProviderManager;

    if-eq p1, v1, :cond_5

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v1

    const-string v4, "android.hardware.type.watch"

    invoke-virtual {v1, v4}, Landroid/content/pm/PackageManager;->hasSystemFeature(Ljava/lang/String;)Z

    move-result v1

    if-eqz v1, :cond_1

    move v1, v3

    goto :goto_1

    :cond_1
    move v1, v2

    :goto_1
    iget-object v4, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v4}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v4

    const-string v5, "location_enable_stationary_throttle"

    invoke-static {v4, v5, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v4

    if-eqz v4, :cond_2

    goto :goto_2

    :cond_2
    move v2, v3

    :goto_2
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->disableStationaryThrottling()Z

    move-result v3

    if-eqz v3, :cond_4

    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->keepGnssStationaryThrottling()Z

    move-result v3

    if-eqz v3, :cond_3

    if-eqz v2, :cond_3

    const-string v3, "gps"

    invoke-virtual {p1}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-nez v3, :cond_4

    :cond_3
    const/4 v2, 0x0

    :cond_4
    if-eqz v2, :cond_5

    new-instance v3, Lcom/android/server/location/provider/StationaryThrottlingLocationProvider;

    invoke-virtual {p1}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;

    move-result-object v4

    iget-object v5, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-direct {v3, v4, v5, p2}, Lcom/android/server/location/provider/StationaryThrottlingLocationProvider;-><init>(Ljava/lang/String;Lcom/android/server/location/injector/Injector;Lcom/android/server/location/provider/AbstractLocationProvider;)V

    move-object p2, v3

    :cond_5
    invoke-virtual {p1, p2}, Lcom/android/server/location/provider/LocationProviderManager;->setRealProvider(Lcom/android/server/location/provider/AbstractLocationProvider;)V

    :cond_6
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {v1, p1}, Ljava/util/concurrent/CopyOnWriteArrayList;->add(Ljava/lang/Object;)Z

    monitor-exit v0

    return-void

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method addLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;Lcom/android/server/location/provider/AbstractLocationProvider;)V
    .registers 9

    goto :goto_5

    nop

    :goto_0
    monitor-enter v0

    :try_start_0
    invoke-virtual {p1}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p0, v1}, Lcom/android/server/location/LocationManagerService;->getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object v1

    const/4 v2, 0x1

    const/4 v3, 0x0

    if-nez v1, :cond_0

    move v1, v2

    goto :goto_1

    :cond_0
    move v1, v3

    :goto_1
    invoke-static {v1}, Lcom/android/internal/util/Preconditions;->checkState(Z)V

    invoke-virtual {p1, p0}, Lcom/android/server/location/provider/LocationProviderManager;->startManager(Lcom/android/server/location/provider/LocationProviderManager$StateChangedListener;)V

    if-eqz p2, :cond_6

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mPassiveManager:Lcom/android/server/location/provider/PassiveLocationProviderManager;

    if-eq p1, v1, :cond_5

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v1

    const-string v4, "android.hardware.type.watch"

    invoke-virtual {v1, v4}, Landroid/content/pm/PackageManager;->hasSystemFeature(Ljava/lang/String;)Z

    move-result v1

    if-eqz v1, :cond_1

    move v1, v3

    goto :goto_2

    :cond_1
    move v1, v2

    :goto_2
    iget-object v4, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v4}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v4

    const-string v5, "location_enable_stationary_throttle"

    invoke-static {v4, v5, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v4

    if-eqz v4, :cond_2

    goto :goto_3

    :cond_2
    move v2, v3

    :goto_3
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->disableStationaryThrottling()Z

    move-result v3

    if-eqz v3, :cond_4

    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->keepGnssStationaryThrottling()Z

    move-result v3

    if-eqz v3, :cond_3

    if-eqz v2, :cond_3

    const-string v3, "gps"

    invoke-virtual {p1}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-nez v3, :cond_4

    :cond_3
    const/4 v2, 0x0

    :cond_4
    if-eqz v2, :cond_5

    new-instance v3, Lcom/android/server/location/provider/StationaryThrottlingLocationProvider;

    invoke-virtual {p1}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;

    move-result-object v4

    iget-object v5, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-direct {v3, v4, v5, p2}, Lcom/android/server/location/provider/StationaryThrottlingLocationProvider;-><init>(Ljava/lang/String;Lcom/android/server/location/injector/Injector;Lcom/android/server/location/provider/AbstractLocationProvider;)V

    move-object p2, v3

    :cond_5
    invoke-virtual {p1, p2}, Lcom/android/server/location/provider/LocationProviderManager;->setRealProvider(Lcom/android/server/location/provider/AbstractLocationProvider;)V

    :cond_6
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {v1, p1}, Ljava/util/concurrent/CopyOnWriteArrayList;->add(Ljava/lang/Object;)Z

    monitor-exit v0

    return-void

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_4

    nop

    :goto_4
    throw v1

    :goto_5
    iget-object v0, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;', 'invoke-virtual {p1}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;', 'move-result-object v1', 'invoke-virtual {p0, v1}, Lcom/android/server/location/LocationManagerService;->getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;', 'move-result-object v1', 'if-nez v1, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_addTestProvider_Ljava_lang_String_Landroid_location_provider",
        "method":      ".method public addTestProvider(Ljava/lang/String;Landroid/location/provider/ProviderProperties;Ljava/util/List;Ljava/lang/String;Ljava/lang/String;)V",
        "method_name": 'addTestProvider',
        "type":        "method_replace",
        "search": """\
.method public addTestProvider(Ljava/lang/String;Landroid/location/provider/ProviderProperties;Ljava/util/List;Ljava/lang/String;Ljava/lang/String;)V
    .registers 15
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/lang/String;",
            "Landroid/location/provider/ProviderProperties;",
            "Ljava/util/List<",
            "Ljava/lang/String;",
            ">;",
            "Ljava/lang/String;",
            "Ljava/lang/String;",
            ")V"
        }
    .end annotation

    invoke-static {p4, p5}, Landroid/location/util/identity/CallerIdentity;->fromBinderUnsafe(Ljava/lang/String;Ljava/lang/String;)Landroid/location/util/identity/CallerIdentity;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getAppOpsHelper()Lcom/android/server/location/injector/AppOpsHelper;

    move-result-object v1

    const/16 v2, 0x3a

    invoke-virtual {v1, v2, v0}, Lcom/android/server/location/injector/AppOpsHelper;->noteOp(ILandroid/location/util/identity/CallerIdentity;)Z

    move-result v1

    if-nez v1, :cond_0

    return-void

    :cond_0
    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v2

    iget-object v5, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    move-object v3, p1

    move-object v4, p2

    move-object v7, p3

    move-object v6, p4

    move-object v8, p5

    invoke-interface/range {v2 .. v8}, Lcom/android/server/location/LocationManagerServiceStub;->addTestProvider(Ljava/lang/String;Landroid/location/provider/ProviderProperties;Landroid/content/Context;Ljava/lang/String;Ljava/util/List;Ljava/lang/String;)Z

    move-result p1

    if-nez p1, :cond_1

    return-void

    :cond_1
    invoke-direct {p0, v3}, Lcom/android/server/location/LocationManagerService;->getOrAddLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object p1

    new-instance p2, Lcom/android/server/location/provider/MockLocationProvider;

    new-instance p3, Landroid/util/ArraySet;

    invoke-direct {p3, v7}, Landroid/util/ArraySet;-><init>(Ljava/util/Collection;)V

    invoke-direct {p2, v4, v0, p3}, Lcom/android/server/location/provider/MockLocationProvider;-><init>(Landroid/location/provider/ProviderProperties;Landroid/location/util/identity/CallerIdentity;Ljava/util/Set;)V

    invoke-virtual {p1, p2}, Lcom/android/server/location/provider/LocationProviderManager;->setMockProvider(Lcom/android/server/location/provider/MockLocationProvider;)V

    return-void
.end method
""",
        "replacement": """\
.method public addTestProvider(Ljava/lang/String;Landroid/location/provider/ProviderProperties;Ljava/util/List;Ljava/lang/String;Ljava/lang/String;)V
    .registers 15
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/lang/String;",
            "Landroid/location/provider/ProviderProperties;",
            "Ljava/util/List<",
            "Ljava/lang/String;",
            ">;",
            "Ljava/lang/String;",
            "Ljava/lang/String;",
            ")V"
        }
    .end annotation

    invoke-static {p4, p5}, Landroid/location/util/identity/CallerIdentity;->fromBinderUnsafe(Ljava/lang/String;Ljava/lang/String;)Landroid/location/util/identity/CallerIdentity;

    move-result-object v0

    const/4 v1, 0x1

    const-string v2, "enable_mezo_mock_locations"

    invoke-static {v2, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v2

    if-eqz v2, :cond_0

    if-nez v0, :cond_1

    return-void

    :cond_0
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getAppOpsHelper()Lcom/android/server/location/injector/AppOpsHelper;

    move-result-object v1

    const/16 v2, 0x3a

    invoke-virtual {v1, v2, v0}, Lcom/android/server/location/injector/AppOpsHelper;->noteOp(ILandroid/location/util/identity/CallerIdentity;)Z

    move-result v1

    if-nez v1, :cond_1

    return-void

    :cond_1
    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v2

    iget-object v5, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    move-object v3, p1

    move-object v4, p2

    move-object v7, p3

    move-object v6, p4

    move-object v8, p5

    invoke-interface/range {v2 .. v8}, Lcom/android/server/location/LocationManagerServiceStub;->addTestProvider(Ljava/lang/String;Landroid/location/provider/ProviderProperties;Landroid/content/Context;Ljava/lang/String;Ljava/util/List;Ljava/lang/String;)Z

    move-result p1

    if-nez p1, :cond_2

    return-void

    :cond_2
    invoke-direct {p0, v3}, Lcom/android/server/location/LocationManagerService;->getOrAddLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object p1

    new-instance p2, Lcom/android/server/location/provider/MockLocationProvider;

    new-instance p3, Landroid/util/ArraySet;

    invoke-direct {p3, v7}, Landroid/util/ArraySet;-><init>(Ljava/util/Collection;)V

    invoke-direct {p2, v4, v0, p3}, Lcom/android/server/location/provider/MockLocationProvider;-><init>(Landroid/location/provider/ProviderProperties;Landroid/location/util/identity/CallerIdentity;Ljava/util/Set;)V

    invoke-virtual {p1, p2}, Lcom/android/server/location/provider/LocationProviderManager;->setMockProvider(Lcom/android/server/location/provider/MockLocationProvider;)V

    return-void
.end method
""",
        "method_anchors": ['invoke-static {p4, p5}, Landroid/location/util/identity/CallerIdentity;->fromBinderUnsafe(Ljava/lang/String;Ljava/lang/String;)Landroid/location/util/identity/CallerIdentity;', 'move-result-object v0', 'iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;', 'invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getAppOpsHelper()Lcom/android/server/location/injector/AppOpsHelper;', 'move-result-object v1', 'invoke-virtual {v1, v2, v0}, Lcom/android/server/location/injector/AppOpsHelper;->noteOp(ILandroid/location/util/identity/CallerIdentity;)Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_calculateAppOpsLocationSourceTags_I_Landroid_os_PackageTagsL",
        "method":      ".method calculateAppOpsLocationSourceTags(I)Landroid/os/PackageTagsList;",
        "method_name": 'calculateAppOpsLocationSourceTags',
        "type":        "method_replace",
        "search": """\
.method calculateAppOpsLocationSourceTags(I)Landroid/os/PackageTagsList;
    .registers 8

    new-instance v0, Landroid/os/PackageTagsList$Builder;

    invoke-direct {v0}, Landroid/os/PackageTagsList$Builder;-><init>()V

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {v1}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_0
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_4

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/server/location/provider/LocationProviderManager;

    invoke-virtual {v2}, Lcom/android/server/location/provider/LocationProviderManager;->getState()Lcom/android/server/location/provider/AbstractLocationProvider$State;

    move-result-object v3

    iget-object v4, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->identity:Landroid/location/util/identity/CallerIdentity;

    if-nez v4, :cond_0

    goto :goto_0

    :cond_0
    iget-object v4, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->identity:Landroid/location/util/identity/CallerIdentity;

    invoke-virtual {v4}, Landroid/location/util/identity/CallerIdentity;->getUid()I

    move-result v4

    if-eq v4, p1, :cond_1

    goto :goto_0

    :cond_1
    iget-object v4, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->identity:Landroid/location/util/identity/CallerIdentity;

    invoke-virtual {v4}, Landroid/location/util/identity/CallerIdentity;->getPackageName()Ljava/lang/String;

    move-result-object v4

    iget-object v5, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->extraAttributionTags:Ljava/util/Set;

    invoke-virtual {v0, v4, v5}, Landroid/os/PackageTagsList$Builder;->add(Ljava/lang/String;Ljava/util/Collection;)Landroid/os/PackageTagsList$Builder;

    iget-object v4, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->extraAttributionTags:Ljava/util/Set;

    invoke-interface {v4}, Ljava/util/Set;->isEmpty()Z

    move-result v4

    if-nez v4, :cond_3

    iget-object v4, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->identity:Landroid/location/util/identity/CallerIdentity;

    invoke-virtual {v4}, Landroid/location/util/identity/CallerIdentity;->getAttributionTag()Ljava/lang/String;

    move-result-object v4

    if-eqz v4, :cond_2

    goto :goto_1

    :cond_2
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v5, " provider has specified a null attribution tag and a non-empty set of extra attribution tags - dropping the null attribution tag"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    const-string v5, "LocationManagerService"

    invoke-static {v5, v4}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_2

    :cond_3
    :goto_1
    iget-object v4, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->identity:Landroid/location/util/identity/CallerIdentity;

    invoke-virtual {v4}, Landroid/location/util/identity/CallerIdentity;->getPackageName()Ljava/lang/String;

    move-result-object v4

    iget-object v5, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->identity:Landroid/location/util/identity/CallerIdentity;

    invoke-virtual {v5}, Landroid/location/util/identity/CallerIdentity;->getAttributionTag()Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v0, v4, v5}, Landroid/os/PackageTagsList$Builder;->add(Ljava/lang/String;Ljava/lang/String;)Landroid/os/PackageTagsList$Builder;

    :goto_2
    goto :goto_0

    :cond_4
    invoke-virtual {v0}, Landroid/os/PackageTagsList$Builder;->build()Landroid/os/PackageTagsList;

    move-result-object v1

    return-object v1
.end method
""",
        "replacement": """\
.method calculateAppOpsLocationSourceTags(I)Landroid/os/PackageTagsList;
    .registers 8

    goto :goto_32

    nop

    :goto_0
    iget-object v4, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->identity:Landroid/location/util/identity/CallerIdentity;

    goto :goto_1f

    nop

    :goto_1
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    goto :goto_11

    nop

    :goto_2
    invoke-virtual {v0}, Landroid/os/PackageTagsList$Builder;->build()Landroid/os/PackageTagsList;

    move-result-object v1

    goto :goto_6

    nop

    :goto_3
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    goto :goto_2c

    nop

    :goto_4
    check-cast v2, Lcom/android/server/location/provider/LocationProviderManager;

    goto :goto_31

    nop

    :goto_5
    invoke-virtual {v4}, Landroid/location/util/identity/CallerIdentity;->getUid()I

    move-result v4

    goto :goto_1e

    nop

    :goto_6
    return-object v1

    :goto_7
    invoke-virtual {v2}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;

    move-result-object v5

    goto :goto_20

    nop

    :goto_8
    const-string v5, "LocationManagerService"

    goto :goto_e

    nop

    :goto_9
    if-nez v4, :cond_0

    goto :goto_30

    :cond_0
    goto :goto_2f

    nop

    :goto_a
    new-instance v4, Ljava/lang/StringBuilder;

    goto :goto_12

    nop

    :goto_b
    iget-object v4, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->identity:Landroid/location/util/identity/CallerIdentity;

    goto :goto_5

    nop

    :goto_c
    goto :goto_1c

    :goto_d
    goto :goto_b

    nop

    :goto_e
    invoke-static {v5, v4}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_29

    nop

    :goto_f
    goto :goto_1c

    :goto_10
    goto :goto_2

    nop

    :goto_11
    if-nez v2, :cond_1

    goto :goto_10

    :cond_1
    goto :goto_17

    nop

    :goto_12
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_7

    nop

    :goto_13
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    goto :goto_1b

    nop

    :goto_14
    invoke-virtual {v5}, Landroid/location/util/identity/CallerIdentity;->getAttributionTag()Ljava/lang/String;

    move-result-object v5

    goto :goto_21

    nop

    :goto_15
    invoke-interface {v4}, Ljava/util/Set;->isEmpty()Z

    move-result v4

    goto :goto_26

    nop

    :goto_16
    invoke-virtual {v4}, Landroid/location/util/identity/CallerIdentity;->getPackageName()Ljava/lang/String;

    move-result-object v4

    goto :goto_2e

    nop

    :goto_17
    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    goto :goto_4

    nop

    :goto_18
    const-string v5, " provider has specified a null attribution tag and a non-empty set of extra attribution tags - dropping the null attribution tag"

    goto :goto_3

    nop

    :goto_19
    invoke-direct {v0}, Landroid/os/PackageTagsList$Builder;-><init>()V

    goto :goto_13

    nop

    :goto_1a
    iget-object v5, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->extraAttributionTags:Ljava/util/Set;

    goto :goto_25

    nop

    :goto_1b
    invoke-virtual {v1}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_1c
    goto :goto_1

    nop

    :goto_1d
    iget-object v4, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->identity:Landroid/location/util/identity/CallerIdentity;

    goto :goto_33

    nop

    :goto_1e
    if-ne v4, p1, :cond_2

    goto :goto_28

    :cond_2
    goto :goto_27

    nop

    :goto_1f
    if-eqz v4, :cond_3

    goto :goto_d

    :cond_3
    goto :goto_c

    nop

    :goto_20
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    goto :goto_18

    nop

    :goto_21
    invoke-virtual {v0, v4, v5}, Landroid/os/PackageTagsList$Builder;->add(Ljava/lang/String;Ljava/lang/String;)Landroid/os/PackageTagsList$Builder;

    :goto_22
    goto :goto_f

    nop

    :goto_23
    iget-object v4, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->identity:Landroid/location/util/identity/CallerIdentity;

    goto :goto_2d

    nop

    :goto_24
    iget-object v4, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->extraAttributionTags:Ljava/util/Set;

    goto :goto_15

    nop

    :goto_25
    invoke-virtual {v0, v4, v5}, Landroid/os/PackageTagsList$Builder;->add(Ljava/lang/String;Ljava/util/Collection;)Landroid/os/PackageTagsList$Builder;

    goto :goto_24

    nop

    :goto_26
    if-eqz v4, :cond_4

    goto :goto_2a

    :cond_4
    goto :goto_1d

    nop

    :goto_27
    goto :goto_1c

    :goto_28
    goto :goto_23

    nop

    :goto_29
    goto :goto_22

    :goto_2a
    goto :goto_2b

    nop

    :goto_2b
    iget-object v4, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->identity:Landroid/location/util/identity/CallerIdentity;

    goto :goto_16

    nop

    :goto_2c
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    goto :goto_8

    nop

    :goto_2d
    invoke-virtual {v4}, Landroid/location/util/identity/CallerIdentity;->getPackageName()Ljava/lang/String;

    move-result-object v4

    goto :goto_1a

    nop

    :goto_2e
    iget-object v5, v3, Lcom/android/server/location/provider/AbstractLocationProvider$State;->identity:Landroid/location/util/identity/CallerIdentity;

    goto :goto_14

    nop

    :goto_2f
    goto :goto_2a

    :goto_30
    goto :goto_a

    nop

    :goto_31
    invoke-virtual {v2}, Lcom/android/server/location/provider/LocationProviderManager;->getState()Lcom/android/server/location/provider/AbstractLocationProvider$State;

    move-result-object v3

    goto :goto_0

    nop

    :goto_32
    new-instance v0, Landroid/os/PackageTagsList$Builder;

    goto :goto_19

    nop

    :goto_33
    invoke-virtual {v4}, Landroid/location/util/identity/CallerIdentity;->getAttributionTag()Ljava/lang/String;

    move-result-object v4

    goto :goto_9

    nop
.end method
""",
        "method_anchors": ['new-instance v0, Landroid/os/PackageTagsList$Builder;', 'invoke-direct {v0}, Landroid/os/PackageTagsList$Builder;-><init>()V', 'iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;', 'invoke-virtual {v1}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;', 'move-result-object v1', 'invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_dump_Ljava_io_FileDescriptor_Ljava_io_PrintWriter__Ljava_lan",
        "method":      ".method protected dump(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V",
        "method_name": 'dump',
        "type":        "method_replace",
        "search": """\
.method protected dump(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V
    .registers 10

    iget-object v0, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    const-string v1, "LocationManagerService"

    invoke-static {v0, v1, p2}, Lcom/android/internal/util/DumpUtils;->checkDumpPermission(Landroid/content/Context;Ljava/lang/String;Ljava/io/PrintWriter;)Z

    move-result v0

    if-nez v0, :cond_0

    return-void

    :cond_0
    new-instance v0, Landroid/util/IndentingPrintWriter;

    const-string v1, "  "

    invoke-direct {v0, p2, v1}, Landroid/util/IndentingPrintWriter;-><init>(Ljava/io/Writer;Ljava/lang/String;)V

    array-length v1, p3

    if-lez v1, :cond_3

    const/4 v1, 0x0

    aget-object v2, p3, v1

    invoke-virtual {p0, v2}, Lcom/android/server/location/LocationManagerService;->getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object v2

    if-eqz v2, :cond_1

    const-string v1, "Provider:"

    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    invoke-virtual {v2, p1, v0, p3}, Lcom/android/server/location/provider/LocationProviderManager;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    const-string v1, "Event Log:"

    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    sget-object v1, Lcom/android/server/location/eventlog/LocationEventLog;->EVENT_LOG:Lcom/android/server/location/eventlog/LocationEventLog;

    invoke-static {v0}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    new-instance v3, Lcom/android/server/location/LocationManagerService$$ExternalSyntheticLambda1;

    invoke-direct {v3, v0}, Lcom/android/server/location/LocationManagerService$$ExternalSyntheticLambda1;-><init>(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v2}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v1, v3, v4}, Lcom/android/server/location/eventlog/LocationEventLog;->iterate(Ljava/util/function/Consumer;Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    return-void

    :cond_1
    const-string v3, "--gnssmetrics"

    aget-object v1, p3, v1

    invoke-virtual {v3, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_3

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    if-eqz v1, :cond_2

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    invoke-virtual {v1, p1, v0, p3}, Lcom/android/server/location/gnss/GnssManagerService;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    :cond_2
    return-void

    :cond_3
    const-string v1, "Location Manager State:"

    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    const-string v1, "User Info:"

    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getUserInfoHelper()Lcom/android/server/location/injector/UserInfoHelper;

    move-result-object v1

    invoke-virtual {v1, p1, v0, p3}, Lcom/android/server/location/injector/UserInfoHelper;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    const-string v1, "Location Settings:"

    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getSettingsHelper()Lcom/android/server/location/injector/SettingsHelper;

    move-result-object v1

    invoke-virtual {v1, p1, v0, p3}, Lcom/android/server/location/injector/SettingsHelper;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getLocationSettings()Lcom/android/server/location/settings/LocationSettings;

    move-result-object v1

    invoke-virtual {v1, p1, v0, p3}, Lcom/android/server/location/settings/LocationSettings;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mLock:Ljava/lang/Object;

    monitor-enter v1

    :try_start_0
    iget-object v2, p0, Lcom/android/server/location/LocationManagerService;->mExtraLocationControllerPackage:Ljava/lang/String;

    if-eqz v2, :cond_5

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Location Controller Extra Package: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/location/LocationManagerService;->mExtraLocationControllerPackage:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget-boolean v3, p0, Lcom/android/server/location/LocationManagerService;->mExtraLocationControllerPackageEnabled:Z

    if-eqz v3, :cond_4

    const-string v3, " [enabled]"

    goto :goto_0

    :cond_4
    const-string v3, " [disabled]"

    :goto_0
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    :cond_5
    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    const-string v1, "Location Providers:"

    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {v1}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_1
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_6

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/server/location/provider/LocationProviderManager;

    invoke-virtual {v2, p1, v0, p3}, Lcom/android/server/location/provider/LocationProviderManager;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    goto :goto_1

    :cond_6
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    const-string v1, "Historical Aggregate Location Provider Data:"

    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    sget-object v1, Lcom/android/server/location/eventlog/LocationEventLog;->EVENT_LOG:Lcom/android/server/location/eventlog/LocationEventLog;

    invoke-virtual {v1}, Lcom/android/server/location/eventlog/LocationEventLog;->copyAggregateStats()Landroid/util/ArrayMap;

    move-result-object v1

    const/4 v2, 0x0

    :goto_2
    invoke-virtual {v1}, Landroid/util/ArrayMap;->size()I

    move-result v3

    if-ge v2, v3, :cond_8

    invoke-virtual {v1, v2}, Landroid/util/ArrayMap;->keyAt(I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Ljava/lang/String;

    invoke-virtual {v0, v3}, Landroid/util/IndentingPrintWriter;->print(Ljava/lang/String;)V

    const-string v3, ":"

    invoke-virtual {v0, v3}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    nop

    invoke-virtual {v1, v2}, Landroid/util/ArrayMap;->valueAt(I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Landroid/util/ArrayMap;

    const/4 v4, 0x0

    :goto_3
    invoke-virtual {v3}, Landroid/util/ArrayMap;->size()I

    move-result v5

    if-ge v4, v5, :cond_7

    invoke-virtual {v3, v4}, Landroid/util/ArrayMap;->keyAt(I)Ljava/lang/Object;

    move-result-object v5

    invoke-virtual {v0, v5}, Landroid/util/IndentingPrintWriter;->print(Ljava/lang/Object;)V

    const-string v5, ": "

    invoke-virtual {v0, v5}, Landroid/util/IndentingPrintWriter;->print(Ljava/lang/String;)V

    invoke-virtual {v3, v4}, Landroid/util/ArrayMap;->valueAt(I)Ljava/lang/Object;

    move-result-object v5

    check-cast v5, Lcom/android/server/location/eventlog/LocationEventLog$AggregateStats;

    invoke-virtual {v5}, Lcom/android/server/location/eventlog/LocationEventLog$AggregateStats;->updateTotals()V

    invoke-virtual {v3, v4}, Landroid/util/ArrayMap;->valueAt(I)Ljava/lang/Object;

    move-result-object v5

    invoke-virtual {v0, v5}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/Object;)V

    add-int/lit8 v4, v4, 0x1

    goto :goto_3

    :cond_7
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    add-int/lit8 v2, v2, 0x1

    goto :goto_2

    :cond_8
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    const-string v2, "Historical Aggregate Gnss Measurement Provider Data:"

    invoke-virtual {v0, v2}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    sget-object v2, Lcom/android/server/location/eventlog/LocationEventLog;->EVENT_LOG:Lcom/android/server/location/eventlog/LocationEventLog;

    invoke-virtual {v2}, Lcom/android/server/location/eventlog/LocationEventLog;->copyGnssMeasurementAggregateStats()Landroid/util/ArrayMap;

    move-result-object v2

    const/4 v3, 0x0

    :goto_4
    invoke-virtual {v2}, Landroid/util/ArrayMap;->size()I

    move-result v4

    if-ge v3, v4, :cond_9

    invoke-virtual {v2, v3}, Landroid/util/ArrayMap;->keyAt(I)Ljava/lang/Object;

    move-result-object v4

    invoke-virtual {v0, v4}, Landroid/util/IndentingPrintWriter;->print(Ljava/lang/Object;)V

    const-string v4, ": "

    invoke-virtual {v0, v4}, Landroid/util/IndentingPrintWriter;->print(Ljava/lang/String;)V

    invoke-virtual {v2, v3}, Landroid/util/ArrayMap;->valueAt(I)Ljava/lang/Object;

    move-result-object v4

    check-cast v4, Lcom/android/server/location/eventlog/LocationEventLog$GnssMeasurementAggregateStats;

    invoke-virtual {v4}, Lcom/android/server/location/eventlog/LocationEventLog$GnssMeasurementAggregateStats;->updateTotals()V

    invoke-virtual {v2, v3}, Landroid/util/ArrayMap;->valueAt(I)Ljava/lang/Object;

    move-result-object v4

    invoke-virtual {v0, v4}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/Object;)V

    add-int/lit8 v3, v3, 0x1

    goto :goto_4

    :cond_9
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    iget-object v3, p0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    if-eqz v3, :cond_a

    const-string v3, "GNSS Manager:"

    invoke-virtual {v0, v3}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    iget-object v3, p0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    invoke-virtual {v3, p1, v0, p3}, Lcom/android/server/location/gnss/GnssManagerService;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    :cond_a
    const-string v3, "Geofence Manager:"

    invoke-virtual {v0, v3}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    iget-object v3, p0, Lcom/android/server/location/LocationManagerService;->mGeofenceManager:Lcom/android/server/location/geofence/GeofenceManager;

    invoke-virtual {v3, p1, v0, p3}, Lcom/android/server/location/geofence/GeofenceManager;->dump(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    const-string v3, "Event Log:"

    invoke-virtual {v0, v3}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    sget-object v3, Lcom/android/server/location/eventlog/LocationEventLog;->EVENT_LOG:Lcom/android/server/location/eventlog/LocationEventLog;

    invoke-static {v0}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    new-instance v4, Lcom/android/server/location/LocationManagerService$$ExternalSyntheticLambda1;

    invoke-direct {v4, v0}, Lcom/android/server/location/LocationManagerService$$ExternalSyntheticLambda1;-><init>(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v3, v4}, Lcom/android/server/location/eventlog/LocationEventLog;->iterate(Ljava/util/function/Consumer;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v3

    invoke-interface {v3, v0}, Lcom/android/server/location/LocationManagerServiceStub;->dump(Landroid/util/IndentingPrintWriter;)V

    return-void

    :catchall_0
    move-exception v2

    :try_start_1
    monitor-exit v1
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw v2
.end method
""",
        "replacement": """\
.method protected dump(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V
    .registers 10

    goto :goto_40

    nop

    :goto_0
    const-string v3, ":"

    goto :goto_2

    nop

    :goto_1
    invoke-virtual {v2, v3}, Landroid/util/ArrayMap;->keyAt(I)Ljava/lang/Object;

    move-result-object v4

    goto :goto_78

    nop

    :goto_2
    invoke-virtual {v0, v3}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_3b

    nop

    :goto_3
    const-string v1, "Location Manager State:"

    goto :goto_34

    nop

    :goto_4
    invoke-direct {v4, v0}, Lcom/android/server/location/LocationManagerService$$ExternalSyntheticLambda1;-><init>(Landroid/util/IndentingPrintWriter;)V

    goto :goto_65

    nop

    :goto_5
    invoke-virtual {v1}, Landroid/util/ArrayMap;->size()I

    move-result v3

    goto :goto_83

    nop

    :goto_6
    monitor-enter v1

    :try_start_0
    iget-object v2, p0, Lcom/android/server/location/LocationManagerService;->mExtraLocationControllerPackage:Ljava/lang/String;

    if-eqz v2, :cond_1

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Location Controller Extra Package: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/location/LocationManagerService;->mExtraLocationControllerPackage:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget-boolean v3, p0, Lcom/android/server/location/LocationManagerService;->mExtraLocationControllerPackageEnabled:Z

    if-eqz v3, :cond_0

    const-string v3, " [enabled]"

    goto :goto_7

    :cond_0
    const-string v3, " [disabled]"

    :goto_7
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    :cond_1
    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_88

    nop

    :goto_8
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_33

    nop

    :goto_9
    invoke-virtual {v3, p1, v0, p3}, Lcom/android/server/location/geofence/GeofenceManager;->dump(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V

    goto :goto_86

    nop

    :goto_a
    invoke-virtual {v1, v3, v4}, Lcom/android/server/location/eventlog/LocationEventLog;->iterate(Ljava/util/function/Consumer;Ljava/lang/String;)V

    goto :goto_4e

    nop

    :goto_b
    invoke-virtual {v0, v3}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_4b

    nop

    :goto_c
    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v3

    goto :goto_96

    nop

    :goto_d
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    goto :goto_1a

    nop

    :goto_e
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    goto :goto_2c

    nop

    :goto_f
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_81

    nop

    :goto_10
    invoke-virtual {v0, v4}, Landroid/util/IndentingPrintWriter;->print(Ljava/lang/String;)V

    goto :goto_80

    nop

    :goto_11
    if-nez v1, :cond_2

    goto :goto_2f

    :cond_2
    goto :goto_15

    nop

    :goto_12
    invoke-virtual {v1, p1, v0, p3}, Lcom/android/server/location/gnss/GnssManagerService;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    :goto_13
    goto :goto_2e

    nop

    :goto_14
    invoke-virtual {v2}, Lcom/android/server/location/eventlog/LocationEventLog;->copyGnssMeasurementAggregateStats()Landroid/util/ArrayMap;

    move-result-object v2

    goto :goto_39

    nop

    :goto_15
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    goto :goto_50

    nop

    :goto_16
    invoke-virtual {v1, v2}, Landroid/util/ArrayMap;->valueAt(I)Ljava/lang/Object;

    move-result-object v3

    goto :goto_31

    nop

    :goto_17
    if-eqz v0, :cond_3

    goto :goto_47

    :cond_3
    goto :goto_46

    nop

    :goto_18
    invoke-virtual {v0, v5}, Landroid/util/IndentingPrintWriter;->print(Ljava/lang/Object;)V

    goto :goto_8e

    nop

    :goto_19
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_d

    nop

    :goto_1a
    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getUserInfoHelper()Lcom/android/server/location/injector/UserInfoHelper;

    move-result-object v1

    goto :goto_74

    nop

    :goto_1b
    invoke-virtual {v0, v3}, Landroid/util/IndentingPrintWriter;->print(Ljava/lang/String;)V

    goto :goto_0

    nop

    :goto_1c
    goto :goto_a1

    :goto_1d
    goto :goto_5f

    nop

    :goto_1e
    const-string v1, "LocationManagerService"

    goto :goto_21

    nop

    :goto_1f
    sget-object v3, Lcom/android/server/location/eventlog/LocationEventLog;->EVENT_LOG:Lcom/android/server/location/eventlog/LocationEventLog;

    goto :goto_72

    nop

    :goto_20
    const-string v4, ": "

    goto :goto_10

    nop

    :goto_21
    invoke-static {v0, v1, p2}, Lcom/android/internal/util/DumpUtils;->checkDumpPermission(Landroid/content/Context;Ljava/lang/String;Ljava/io/PrintWriter;)Z

    move-result v0

    goto :goto_17

    nop

    :goto_22
    invoke-virtual {v0, v3}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_62

    nop

    :goto_23
    goto :goto_3a

    :goto_24
    goto :goto_8c

    nop

    :goto_25
    invoke-virtual {v0, v5}, Landroid/util/IndentingPrintWriter;->print(Ljava/lang/String;)V

    goto :goto_a7

    nop

    :goto_26
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    goto :goto_28

    nop

    :goto_27
    invoke-virtual {v0, v2}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_f

    nop

    :goto_28
    invoke-virtual {v1}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_29
    goto :goto_a5

    nop

    :goto_2a
    const-string v1, "User Info:"

    goto :goto_7e

    nop

    :goto_2b
    new-instance v4, Lcom/android/server/location/LocationManagerService$$ExternalSyntheticLambda1;

    goto :goto_4

    nop

    :goto_2c
    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getSettingsHelper()Lcom/android/server/location/injector/SettingsHelper;

    move-result-object v1

    goto :goto_51

    nop

    :goto_2d
    check-cast v4, Lcom/android/server/location/eventlog/LocationEventLog$GnssMeasurementAggregateStats;

    goto :goto_92

    nop

    :goto_2e
    return-void

    :goto_2f
    goto :goto_3

    nop

    :goto_30
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_56

    nop

    :goto_31
    check-cast v3, Landroid/util/ArrayMap;

    goto :goto_9e

    nop

    :goto_32
    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_42

    nop

    :goto_33
    sget-object v1, Lcom/android/server/location/eventlog/LocationEventLog;->EVENT_LOG:Lcom/android/server/location/eventlog/LocationEventLog;

    goto :goto_71

    nop

    :goto_34
    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_6b

    nop

    :goto_35
    return-void

    :goto_36
    goto :goto_8b

    nop

    :goto_37
    add-int/lit8 v4, v4, 0x1

    goto :goto_98

    nop

    :goto_38
    if-nez v2, :cond_4

    goto :goto_36

    :cond_4
    goto :goto_60

    nop

    :goto_39
    const/4 v3, 0x0

    :goto_3a
    goto :goto_79

    nop

    :goto_3b
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    nop

    goto :goto_16

    nop

    :goto_3c
    const-string v2, "Historical Aggregate Gnss Measurement Provider Data:"

    goto :goto_27

    nop

    :goto_3d
    sget-object v1, Lcom/android/server/location/eventlog/LocationEventLog;->EVENT_LOG:Lcom/android/server/location/eventlog/LocationEventLog;

    goto :goto_49

    nop

    :goto_3e
    invoke-virtual {v3, v4}, Landroid/util/ArrayMap;->valueAt(I)Ljava/lang/Object;

    move-result-object v5

    goto :goto_7b

    nop

    :goto_3f
    iget-object v3, p0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    goto :goto_55

    nop

    :goto_40
    iget-object v0, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_1e

    nop

    :goto_41
    iget-object v3, p0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    goto :goto_4c

    nop

    :goto_42
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_e

    nop

    :goto_43
    const/4 v1, 0x0

    goto :goto_73

    nop

    :goto_44
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    :goto_45
    goto :goto_5c

    nop

    :goto_46
    return-void

    :goto_47
    goto :goto_93

    nop

    :goto_48
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_57

    nop

    :goto_49
    invoke-virtual {v1}, Lcom/android/server/location/eventlog/LocationEventLog;->copyAggregateStats()Landroid/util/ArrayMap;

    move-result-object v1

    goto :goto_a0

    nop

    :goto_4a
    invoke-virtual {v5}, Lcom/android/server/location/eventlog/LocationEventLog$AggregateStats;->updateTotals()V

    goto :goto_3e

    nop

    :goto_4b
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_41

    nop

    :goto_4c
    invoke-virtual {v3, p1, v0, p3}, Lcom/android/server/location/gnss/GnssManagerService;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    goto :goto_44

    nop

    :goto_4d
    invoke-virtual {v2}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;

    move-result-object v4

    goto :goto_a

    nop

    :goto_4e
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_35

    nop

    :goto_4f
    array-length v1, p3

    goto :goto_66

    nop

    :goto_50
    if-nez v1, :cond_5

    goto :goto_13

    :cond_5
    goto :goto_67

    nop

    :goto_51
    invoke-virtual {v1, p1, v0, p3}, Lcom/android/server/location/injector/SettingsHelper;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    goto :goto_9c

    nop

    :goto_52
    return-void

    :catchall_0
    move-exception v2

    :try_start_1
    monitor-exit v1
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_63

    nop

    :goto_53
    invoke-virtual {v1, v2}, Landroid/util/ArrayMap;->keyAt(I)Ljava/lang/Object;

    move-result-object v3

    goto :goto_8d

    nop

    :goto_54
    invoke-virtual {v1, p1, v0, p3}, Lcom/android/server/location/settings/LocationSettings;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    goto :goto_9b

    nop

    :goto_55
    if-nez v3, :cond_6

    goto :goto_45

    :cond_6
    goto :goto_a2

    nop

    :goto_56
    invoke-virtual {v2, p1, v0, p3}, Lcom/android/server/location/provider/LocationProviderManager;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    goto :goto_64

    nop

    :goto_57
    const-string v1, "Location Settings:"

    goto :goto_32

    nop

    :goto_58
    invoke-virtual {p0, v2}, Lcom/android/server/location/LocationManagerService;->getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object v2

    goto :goto_38

    nop

    :goto_59
    if-lt v3, v4, :cond_7

    goto :goto_24

    :cond_7
    goto :goto_1

    nop

    :goto_5a
    goto :goto_29

    :goto_5b
    goto :goto_a4

    nop

    :goto_5c
    const-string v3, "Geofence Manager:"

    goto :goto_84

    nop

    :goto_5d
    invoke-virtual {v3, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    goto :goto_11

    nop

    :goto_5e
    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getLocationSettings()Lcom/android/server/location/settings/LocationSettings;

    move-result-object v1

    goto :goto_54

    nop

    :goto_5f
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_3c

    nop

    :goto_60
    const-string v1, "Provider:"

    goto :goto_94

    nop

    :goto_61
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_70

    nop

    :goto_62
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_1f

    nop

    :goto_63
    throw v2

    :goto_64
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_a6

    nop

    :goto_65
    invoke-virtual {v3, v4}, Lcom/android/server/location/eventlog/LocationEventLog;->iterate(Ljava/util/function/Consumer;)V

    goto :goto_95

    nop

    :goto_66
    if-gtz v1, :cond_8

    goto :goto_2f

    :cond_8
    goto :goto_43

    nop

    :goto_67
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    goto :goto_12

    nop

    :goto_68
    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_6e

    nop

    :goto_69
    const-string v1, "Historical Aggregate Location Provider Data:"

    goto :goto_68

    nop

    :goto_6a
    invoke-direct {v3, v0}, Lcom/android/server/location/LocationManagerService$$ExternalSyntheticLambda1;-><init>(Landroid/util/IndentingPrintWriter;)V

    goto :goto_4d

    nop

    :goto_6b
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_2a

    nop

    :goto_6c
    add-int/lit8 v3, v3, 0x1

    goto :goto_23

    nop

    :goto_6d
    invoke-virtual {v2, v3}, Landroid/util/ArrayMap;->valueAt(I)Ljava/lang/Object;

    move-result-object v4

    goto :goto_77

    nop

    :goto_6e
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_3d

    nop

    :goto_6f
    add-int/lit8 v2, v2, 0x1

    goto :goto_1c

    nop

    :goto_70
    iget-object v3, p0, Lcom/android/server/location/LocationManagerService;->mGeofenceManager:Lcom/android/server/location/geofence/GeofenceManager;

    goto :goto_9

    nop

    :goto_71
    invoke-static {v0}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_97

    nop

    :goto_72
    invoke-static {v0}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_2b

    nop

    :goto_73
    aget-object v2, p3, v1

    goto :goto_58

    nop

    :goto_74
    invoke-virtual {v1, p1, v0, p3}, Lcom/android/server/location/injector/UserInfoHelper;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    goto :goto_48

    nop

    :goto_75
    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_9a

    nop

    :goto_76
    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_8

    nop

    :goto_77
    invoke-virtual {v0, v4}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/Object;)V

    goto :goto_6c

    nop

    :goto_78
    invoke-virtual {v0, v4}, Landroid/util/IndentingPrintWriter;->print(Ljava/lang/Object;)V

    goto :goto_20

    nop

    :goto_79
    invoke-virtual {v2}, Landroid/util/ArrayMap;->size()I

    move-result v4

    goto :goto_59

    nop

    :goto_7a
    invoke-virtual {v3}, Landroid/util/ArrayMap;->size()I

    move-result v5

    goto :goto_91

    nop

    :goto_7b
    invoke-virtual {v0, v5}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/Object;)V

    goto :goto_37

    nop

    :goto_7c
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_6f

    nop

    :goto_7d
    check-cast v5, Lcom/android/server/location/eventlog/LocationEventLog$AggregateStats;

    goto :goto_4a

    nop

    :goto_7e
    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_19

    nop

    :goto_7f
    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    goto :goto_8f

    nop

    :goto_80
    invoke-virtual {v2, v3}, Landroid/util/ArrayMap;->valueAt(I)Ljava/lang/Object;

    move-result-object v4

    goto :goto_2d

    nop

    :goto_81
    sget-object v2, Lcom/android/server/location/eventlog/LocationEventLog;->EVENT_LOG:Lcom/android/server/location/eventlog/LocationEventLog;

    goto :goto_14

    nop

    :goto_82
    invoke-direct {v0, p2, v1}, Landroid/util/IndentingPrintWriter;-><init>(Ljava/io/Writer;Ljava/lang/String;)V

    goto :goto_4f

    nop

    :goto_83
    if-lt v2, v3, :cond_9

    goto :goto_1d

    :cond_9
    goto :goto_53

    nop

    :goto_84
    invoke-virtual {v0, v3}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_61

    nop

    :goto_85
    invoke-virtual {v3, v4}, Landroid/util/ArrayMap;->keyAt(I)Ljava/lang/Object;

    move-result-object v5

    goto :goto_18

    nop

    :goto_86
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_9d

    nop

    :goto_87
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mLock:Ljava/lang/Object;

    goto :goto_6

    nop

    :goto_88
    const-string v1, "Location Providers:"

    goto :goto_75

    nop

    :goto_89
    aget-object v1, p3, v1

    goto :goto_5d

    nop

    :goto_8a
    if-nez v2, :cond_a

    goto :goto_5b

    :cond_a
    goto :goto_7f

    nop

    :goto_8b
    const-string v3, "--gnssmetrics"

    goto :goto_89

    nop

    :goto_8c
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_3f

    nop

    :goto_8d
    check-cast v3, Ljava/lang/String;

    goto :goto_1b

    nop

    :goto_8e
    const-string v5, ": "

    goto :goto_25

    nop

    :goto_8f
    check-cast v2, Lcom/android/server/location/provider/LocationProviderManager;

    goto :goto_90

    nop

    :goto_90
    invoke-virtual {v2, p1, v0, p3}, Lcom/android/server/location/provider/LocationProviderManager;->dump(Ljava/io/FileDescriptor;Landroid/util/IndentingPrintWriter;[Ljava/lang/String;)V

    goto :goto_5a

    nop

    :goto_91
    if-lt v4, v5, :cond_b

    goto :goto_99

    :cond_b
    goto :goto_85

    nop

    :goto_92
    invoke-virtual {v4}, Lcom/android/server/location/eventlog/LocationEventLog$GnssMeasurementAggregateStats;->updateTotals()V

    goto :goto_6d

    nop

    :goto_93
    new-instance v0, Landroid/util/IndentingPrintWriter;

    goto :goto_a3

    nop

    :goto_94
    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_30

    nop

    :goto_95
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_c

    nop

    :goto_96
    invoke-interface {v3, v0}, Lcom/android/server/location/LocationManagerServiceStub;->dump(Landroid/util/IndentingPrintWriter;)V

    goto :goto_52

    nop

    :goto_97
    new-instance v3, Lcom/android/server/location/LocationManagerService$$ExternalSyntheticLambda1;

    goto :goto_6a

    nop

    :goto_98
    goto :goto_9f

    :goto_99
    goto :goto_7c

    nop

    :goto_9a
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_26

    nop

    :goto_9b
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_87

    nop

    :goto_9c
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    goto :goto_5e

    nop

    :goto_9d
    const-string v3, "Event Log:"

    goto :goto_22

    nop

    :goto_9e
    const/4 v4, 0x0

    :goto_9f
    goto :goto_7a

    nop

    :goto_a0
    const/4 v2, 0x0

    :goto_a1
    goto :goto_5

    nop

    :goto_a2
    const-string v3, "GNSS Manager:"

    goto :goto_b

    nop

    :goto_a3
    const-string v1, "  "

    goto :goto_82

    nop

    :goto_a4
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->decreaseIndent()Landroid/util/IndentingPrintWriter;

    goto :goto_69

    nop

    :goto_a5
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    goto :goto_8a

    nop

    :goto_a6
    const-string v1, "Event Log:"

    goto :goto_76

    nop

    :goto_a7
    invoke-virtual {v3, v4}, Landroid/util/ArrayMap;->valueAt(I)Ljava/lang/Object;

    move-result-object v5

    goto :goto_7d

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;', 'const-string v1, "LocationManagerService"', 'invoke-static {v0, v1, p2}, Lcom/android/internal/util/DumpUtils;->checkDumpPermission(Landroid/content/Context;Ljava/lang/String;Ljava/io/PrintWriter;)Z', 'move-result v0', 'if-nez v0, :cond_0', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getLocationProviderManager_Ljava_lang_String__Lcom_android_s",
        "method":      ".method getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;",
        "method_name": 'getLocationProviderManager',
        "type":        "method_replace",
        "search": """\
.method getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;
    .registers 6

    const/4 v0, 0x0

    if-nez p1, :cond_0

    return-object v0

    :cond_0
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {v1}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_0
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_3

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/server/location/provider/LocationProviderManager;

    invoke-virtual {v2}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {p1, v3}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-eqz v3, :cond_2

    invoke-virtual {v2}, Lcom/android/server/location/provider/LocationProviderManager;->isVisibleToCaller()Z

    move-result v1

    if-nez v1, :cond_1

    return-object v0

    :cond_1
    return-object v2

    :cond_2
    goto :goto_0

    :cond_3
    return-object v0
.end method
""",
        "replacement": """\
.method getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;
    .registers 6

    goto :goto_7

    nop

    :goto_0
    if-eqz v1, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_13

    nop

    :goto_1
    check-cast v2, Lcom/android/server/location/provider/LocationProviderManager;

    goto :goto_a

    nop

    :goto_2
    invoke-virtual {p1, v3}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v3

    goto :goto_12

    nop

    :goto_3
    goto :goto_10

    :goto_4
    goto :goto_8

    nop

    :goto_5
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    goto :goto_9

    nop

    :goto_6
    invoke-virtual {v2}, Lcom/android/server/location/provider/LocationProviderManager;->isVisibleToCaller()Z

    move-result v1

    goto :goto_0

    nop

    :goto_7
    const/4 v0, 0x0

    goto :goto_11

    nop

    :goto_8
    return-object v0

    :goto_9
    if-nez v2, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_d

    nop

    :goto_a
    invoke-virtual {v2}, Lcom/android/server/location/provider/LocationProviderManager;->getName()Ljava/lang/String;

    move-result-object v3

    goto :goto_2

    nop

    :goto_b
    return-object v0

    :goto_c
    goto :goto_e

    nop

    :goto_d
    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    goto :goto_1

    nop

    :goto_e
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    goto :goto_f

    nop

    :goto_f
    invoke-virtual {v1}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_10
    goto :goto_5

    nop

    :goto_11
    if-eqz p1, :cond_2

    goto :goto_c

    :cond_2
    goto :goto_b

    nop

    :goto_12
    if-nez v3, :cond_3

    goto :goto_16

    :cond_3
    goto :goto_6

    nop

    :goto_13
    return-object v0

    :goto_14
    goto :goto_15

    nop

    :goto_15
    return-object v2

    :goto_16
    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['if-nez p1, :cond_0', 'return-object v0', 'iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;', 'invoke-virtual {v1}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;', 'move-result-object v1', 'invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_onSystemReady__V",
        "method":      ".method onSystemReady()V",
        "method_name": 'onSystemReady',
        "type":        "method_replace",
        "search": """\
.method onSystemReady()V
    .registers 4

    sget-boolean v0, Landroid/os/Build;->IS_DEBUGGABLE:Z

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    const-class v1, Landroid/app/AppOpsManager;

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/app/AppOpsManager;

    invoke-static {v0}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/app/AppOpsManager;

    const/4 v1, 0x1

    const/4 v2, 0x0

    filled-new-array {v1, v2}, [I

    move-result-object v1

    new-instance v2, Lcom/android/server/location/LocationManagerService$$ExternalSyntheticLambda2;

    invoke-direct {v2, p0}, Lcom/android/server/location/LocationManagerService$$ExternalSyntheticLambda2;-><init>(Lcom/android/server/location/LocationManagerService;)V

    invoke-virtual {v0, v1, v2}, Landroid/app/AppOpsManager;->startWatchingNoted([ILandroid/app/AppOpsManager$OnOpNotedListener;)V

    :cond_0
    return-void
.end method
""",
        "replacement": """\
.method onSystemReady()V
    .registers 4

    goto :goto_4

    nop

    :goto_0
    check-cast v0, Landroid/app/AppOpsManager;

    goto :goto_2

    nop

    :goto_1
    iget-object v0, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_5

    nop

    :goto_2
    invoke-static {v0}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_7

    nop

    :goto_3
    return-void

    :goto_4
    sget-boolean v0, Landroid/os/Build;->IS_DEBUGGABLE:Z

    goto :goto_a

    nop

    :goto_5
    const-class v1, Landroid/app/AppOpsManager;

    goto :goto_9

    nop

    :goto_6
    const/4 v1, 0x1

    goto :goto_b

    nop

    :goto_7
    check-cast v0, Landroid/app/AppOpsManager;

    goto :goto_6

    nop

    :goto_8
    invoke-direct {v2, p0}, Lcom/android/server/location/LocationManagerService$$ExternalSyntheticLambda2;-><init>(Lcom/android/server/location/LocationManagerService;)V

    goto :goto_d

    nop

    :goto_9
    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_0

    nop

    :goto_a
    if-nez v0, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_1

    nop

    :goto_b
    const/4 v2, 0x0

    goto :goto_c

    nop

    :goto_c
    filled-new-array {v1, v2}, [I

    move-result-object v1

    goto :goto_f

    nop

    :goto_d
    invoke-virtual {v0, v1, v2}, Landroid/app/AppOpsManager;->startWatchingNoted([ILandroid/app/AppOpsManager$OnOpNotedListener;)V

    :goto_e
    goto :goto_3

    nop

    :goto_f
    new-instance v2, Lcom/android/server/location/LocationManagerService$$ExternalSyntheticLambda2;

    goto :goto_8

    nop
.end method
""",
        "method_anchors": ['sget-boolean v0, Landroid/os/Build;->IS_DEBUGGABLE:Z', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;', 'const-class v1, Landroid/app/AppOpsManager;', 'invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;', 'move-result-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_onSystemThirdPartyAppsCanStart__V",
        "method":      ".method onSystemThirdPartyAppsCanStart()V",
        "method_name": 'onSystemThirdPartyAppsCanStart',
        "type":        "method_replace",
        "search": """\
.method onSystemThirdPartyAppsCanStart()V
    .registers 18

    move-object/from16 v0, p0

    iget-object v1, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    const v2, 0x1110184

    const v3, 0x10402fc

    const-string v4, "network"

    const-string v5, "com.android.location.service.v3.NetworkLocationProvider"

    invoke-static {v1, v4, v5, v2, v3}, Lcom/android/server/location/provider/proxy/ProxyLocationProvider;->create(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;II)Lcom/android/server/location/provider/proxy/ProxyLocationProvider;

    move-result-object v1

    const-string v2, "LocationManagerService"

    if-eqz v1, :cond_0

    new-instance v3, Lcom/android/server/location/provider/LocationProviderManager;

    iget-object v5, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    iget-object v6, v0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mPassiveManager:Lcom/android/server/location/provider/PassiveLocationProviderManager;

    invoke-direct {v3, v5, v6, v4, v7}, Lcom/android/server/location/provider/LocationProviderManager;-><init>(Landroid/content/Context;Lcom/android/server/location/injector/Injector;Ljava/lang/String;Lcom/android/server/location/provider/PassiveLocationProviderManager;)V

    invoke-virtual {v0, v3, v1}, Lcom/android/server/location/LocationManagerService;->addLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;Lcom/android/server/location/provider/AbstractLocationProvider;)V

    goto :goto_0

    :cond_0
    const-string v3, "no network location provider found"

    invoke-static {v2, v3}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    :goto_0
    iget-object v3, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v3}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v3

    new-instance v4, Landroid/content/Intent;

    const-string v5, "com.android.location.service.FusedLocationProvider"

    invoke-direct {v4, v5}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const/high16 v5, 0x180000

    const/4 v6, 0x0

    invoke-virtual {v3, v4, v5, v6}, Landroid/content/pm/PackageManager;->queryIntentServicesAsUser(Landroid/content/Intent;II)Ljava/util/List;

    move-result-object v3

    invoke-interface {v3}, Ljava/util/List;->isEmpty()Z

    move-result v3

    const/4 v4, 0x1

    xor-int/2addr v3, v4

    const-string v5, "Unable to find a direct boot aware fused location provider"

    invoke-static {v3, v5}, Lcom/android/internal/util/Preconditions;->checkState(ZLjava/lang/String;)V

    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    const v11, 0x10402da

    const v12, 0x11101b8

    const-string v8, "fused"

    const-string v9, "com.android.location.service.FusedLocationProvider"

    const v10, 0x1110175

    invoke-static/range {v7 .. v12}, Lcom/android/server/location/provider/proxy/ProxyLocationProvider;->create(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;III)Lcom/android/server/location/provider/proxy/ProxyLocationProvider;

    move-result-object v3

    if-eqz v3, :cond_1

    new-instance v5, Lcom/android/server/location/provider/LocationProviderManager;

    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    const-string v9, "fused"

    iget-object v10, v0, Lcom/android/server/location/LocationManagerService;->mPassiveManager:Lcom/android/server/location/provider/PassiveLocationProviderManager;

    invoke-direct {v5, v7, v8, v9, v10}, Lcom/android/server/location/provider/LocationProviderManager;-><init>(Landroid/content/Context;Lcom/android/server/location/injector/Injector;Ljava/lang/String;Lcom/android/server/location/provider/PassiveLocationProviderManager;)V

    invoke-virtual {v0, v5, v3}, Lcom/android/server/location/LocationManagerService;->addLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;Lcom/android/server/location/provider/AbstractLocationProvider;)V

    goto :goto_1

    :cond_1
    const-string v5, "no fused location provider found"

    invoke-static {v2, v5}, Landroid/util/Log;->wtf(Ljava/lang/String;Ljava/lang/String;)I

    :goto_1
    iget-object v5, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v5}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v5

    const-string v7, "android.hardware.location"

    invoke-virtual {v5, v7}, Landroid/content/pm/PackageManager;->hasSystemFeature(Ljava/lang/String;)Z

    move-result v5

    if-eqz v5, :cond_4

    invoke-static {}, Lcom/android/server/location/gnss/hal/GnssNative;->isSupported()Z

    move-result v7

    if-eqz v7, :cond_4

    new-instance v7, Lcom/android/server/location/gnss/GnssConfiguration;

    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-direct {v7, v8}, Lcom/android/server/location/gnss/GnssConfiguration;-><init>(Landroid/content/Context;)V

    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-static {v8, v7}, Lcom/android/server/location/gnss/hal/GnssNative;->create(Lcom/android/server/location/injector/Injector;Lcom/android/server/location/gnss/GnssConfiguration;)Lcom/android/server/location/gnss/hal/GnssNative;

    move-result-object v8

    new-instance v9, Lcom/android/server/location/gnss/GnssManagerService;

    iget-object v10, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    iget-object v11, v0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-direct {v9, v10, v11, v8}, Lcom/android/server/location/gnss/GnssManagerService;-><init>(Landroid/content/Context;Lcom/android/server/location/injector/Injector;Lcom/android/server/location/gnss/hal/GnssNative;)V

    iput-object v9, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    iget-object v9, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    invoke-virtual {v9}, Lcom/android/server/location/gnss/GnssManagerService;->onSystemReady()V

    iget-object v9, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v9}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v9

    const v10, 0x1110299

    invoke-virtual {v9, v10}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v9

    const/4 v10, 0x0

    if-nez v9, :cond_2

    iget-object v11, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    const v15, 0x10402df

    const v16, 0x11101ba

    const-string v12, "gps"

    const-string v13, "android.location.provider.action.GNSS_PROVIDER"

    const v14, 0x111017b

    invoke-static/range {v11 .. v16}, Lcom/android/server/location/provider/proxy/ProxyLocationProvider;->create(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;III)Lcom/android/server/location/provider/proxy/ProxyLocationProvider;

    move-result-object v10

    :cond_2
    if-nez v10, :cond_3

    iget-object v11, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    invoke-virtual {v11}, Lcom/android/server/location/gnss/GnssManagerService;->getGnssLocationProvider()Lcom/android/server/location/gnss/GnssLocationProvider;

    move-result-object v10

    goto :goto_2

    :cond_3
    new-instance v11, Lcom/android/server/location/provider/LocationProviderManager;

    iget-object v12, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    iget-object v13, v0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    const-string v14, "android.permission.LOCATION_HARDWARE"

    invoke-static {v14}, Ljava/util/Collections;->singletonList(Ljava/lang/Object;)Ljava/util/List;

    move-result-object v16

    const-string v14, "gps_hardware"

    const/4 v15, 0x0

    invoke-direct/range {v11 .. v16}, Lcom/android/server/location/provider/LocationProviderManager;-><init>(Landroid/content/Context;Lcom/android/server/location/injector/Injector;Ljava/lang/String;Lcom/android/server/location/provider/PassiveLocationProviderManager;Ljava/util/Collection;)V

    iget-object v12, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    invoke-virtual {v12}, Lcom/android/server/location/gnss/GnssManagerService;->getGnssLocationProvider()Lcom/android/server/location/gnss/GnssLocationProvider;

    move-result-object v12

    invoke-virtual {v0, v11, v12}, Lcom/android/server/location/LocationManagerService;->addLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;Lcom/android/server/location/provider/AbstractLocationProvider;)V

    :goto_2
    new-instance v11, Lcom/android/server/location/provider/LocationProviderManager;

    iget-object v12, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    iget-object v13, v0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    const-string v14, "gps"

    iget-object v15, v0, Lcom/android/server/location/LocationManagerService;->mPassiveManager:Lcom/android/server/location/provider/PassiveLocationProviderManager;

    invoke-direct {v11, v12, v13, v14, v15}, Lcom/android/server/location/provider/LocationProviderManager;-><init>(Landroid/content/Context;Lcom/android/server/location/injector/Injector;Ljava/lang/String;Lcom/android/server/location/provider/PassiveLocationProviderManager;)V

    invoke-virtual {v0, v11, v10}, Lcom/android/server/location/LocationManagerService;->addLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;Lcom/android/server/location/provider/AbstractLocationProvider;)V

    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v12

    iget-object v13, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-interface {v12, v13}, Lcom/android/server/location/LocationManagerServiceStub;->startPowerSaveListener(Landroid/content/Context;)V

    :cond_4
    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v7

    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    iget-object v9, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    invoke-interface {v7, v8, v9}, Lcom/android/server/location/LocationManagerServiceStub;->onSystemThirdPartyAppsCanStart(Ljava/util/concurrent/CopyOnWriteArrayList;Lcom/android/server/location/gnss/GnssManagerService;)V

    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-static {v7}, Lcom/android/server/location/provider/proxy/ProxyGeocodeProvider;->createAndRegister(Landroid/content/Context;)Lcom/android/server/location/provider/proxy/ProxyGeocodeProvider;

    move-result-object v7

    iput-object v7, v0, Lcom/android/server/location/LocationManagerService;->mGeocodeProvider:Lcom/android/server/location/provider/proxy/ProxyGeocodeProvider;

    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mGeocodeProvider:Lcom/android/server/location/provider/proxy/ProxyGeocodeProvider;

    if-nez v7, :cond_5

    const-string v7, "no geocoder provider found"

    invoke-static {v2, v7}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :cond_5
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->populationDensityProvider()Z

    move-result v7

    if-eqz v7, :cond_8

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v7

    iget-object v9, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-static {v9}, Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;->createAndRegister(Landroid/content/Context;)Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;

    move-result-object v9

    invoke-virtual {v0, v9}, Lcom/android/server/location/LocationManagerService;->setProxyPopulationDensityProvider(Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;)V

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v9

    sub-long/2addr v9, v7

    long-to-int v9, v9

    iget-object v10, v0, Lcom/android/server/location/LocationManagerService;->mPopulationDensityProvider:Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;

    if-nez v10, :cond_6

    const-string v10, "no population density provider found"

    invoke-static {v2, v10}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :cond_6
    iget-object v10, v0, Lcom/android/server/location/LocationManagerService;->mPopulationDensityProvider:Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;

    if-nez v10, :cond_7

    move v10, v4

    goto :goto_3

    :cond_7
    move v10, v6

    :goto_3
    const/16 v11, 0x3ea

    invoke-static {v11, v10, v9}, Lcom/android/internal/util/FrameworkStatsLog;->write(IZI)V

    :cond_8
    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mPopulationDensityProvider:Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;

    if-eqz v7, :cond_9

    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->densityBasedCoarseLocations()Z

    move-result v7

    if-eqz v7, :cond_9

    new-instance v7, Lcom/android/server/location/fudger/LocationFudgerCache;

    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mPopulationDensityProvider:Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;

    invoke-direct {v7, v8}, Lcom/android/server/location/fudger/LocationFudgerCache;-><init>(Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;)V

    invoke-virtual {v0, v7}, Lcom/android/server/location/LocationManagerService;->setLocationFudgerCache(Lcom/android/server/location/fudger/LocationFudgerCache;)V

    :cond_9
    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-static {v7}, Lcom/android/server/location/HardwareActivityRecognitionProxy;->createAndRegister(Landroid/content/Context;)Lcom/android/server/location/HardwareActivityRecognitionProxy;

    move-result-object v7

    if-nez v7, :cond_a

    const-string v8, "unable to bind ActivityRecognitionProxy"

    invoke-static {v2, v8}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :cond_a
    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    if-eqz v8, :cond_b

    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    iget-object v9, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    invoke-virtual {v9}, Lcom/android/server/location/gnss/GnssManagerService;->getGnssGeofenceProxy()Landroid/location/IGpsGeofenceHardware;

    move-result-object v9

    invoke-static {v8, v9}, Lcom/android/server/location/geofence/GeofenceProxy;->createAndBind(Landroid/content/Context;Landroid/location/IGpsGeofenceHardware;)Lcom/android/server/location/geofence/GeofenceProxy;

    move-result-object v8

    if-nez v8, :cond_b

    const-string v9, "unable to bind to GeofenceProxy"

    invoke-static {v2, v9}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :cond_b
    iget-object v2, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    const v8, 0x10700e1

    invoke-virtual {v2, v8}, Landroid/content/res/Resources;->getStringArray(I)[Ljava/lang/String;

    move-result-object v2

    array-length v8, v2

    move v9, v6

    :goto_4
    if-ge v9, v8, :cond_c

    aget-object v10, v2, v9

    const-string v11, ","

    invoke-virtual {v10, v11}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v11

    aget-object v12, v11, v6

    invoke-virtual {v12}, Ljava/lang/String;->trim()Ljava/lang/String;

    move-result-object v12

    new-instance v13, Landroid/location/provider/ProviderProperties$Builder;

    invoke-direct {v13}, Landroid/location/provider/ProviderProperties$Builder;-><init>()V

    aget-object v14, v11, v4

    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasNetworkRequirement(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    const/4 v14, 0x2

    aget-object v14, v11, v14

    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasSatelliteRequirement(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    const/4 v14, 0x3

    aget-object v14, v11, v14

    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasCellRequirement(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    const/4 v14, 0x4

    aget-object v14, v11, v14

    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasMonetaryCost(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    const/4 v14, 0x5

    aget-object v14, v11, v14

    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasAltitudeSupport(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    const/4 v14, 0x6

    aget-object v14, v11, v14

    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasSpeedSupport(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    const/4 v14, 0x7

    aget-object v14, v11, v14

    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasBearingSupport(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    const/16 v14, 0x8

    aget-object v14, v11, v14

    invoke-static {v14}, Ljava/lang/Integer;->parseInt(Ljava/lang/String;)I

    move-result v14

    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setPowerUsage(I)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    const/16 v14, 0x9

    aget-object v14, v11, v14

    invoke-static {v14}, Ljava/lang/Integer;->parseInt(Ljava/lang/String;)I

    move-result v14

    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setAccuracy(I)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    invoke-virtual {v13}, Landroid/location/provider/ProviderProperties$Builder;->build()Landroid/location/provider/ProviderProperties;

    move-result-object v13

    invoke-direct {v0, v12}, Lcom/android/server/location/LocationManagerService;->getOrAddLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object v14

    new-instance v15, Lcom/android/server/location/provider/MockLocationProvider;

    iget-object v4, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-static {v4}, Landroid/location/util/identity/CallerIdentity;->fromContext(Landroid/content/Context;)Landroid/location/util/identity/CallerIdentity;

    move-result-object v4

    invoke-static {}, Ljava/util/Collections;->emptySet()Ljava/util/Set;

    move-result-object v6

    invoke-direct {v15, v13, v4, v6}, Lcom/android/server/location/provider/MockLocationProvider;-><init>(Landroid/location/provider/ProviderProperties;Landroid/location/util/identity/CallerIdentity;Ljava/util/Set;)V

    invoke-virtual {v14, v15}, Lcom/android/server/location/provider/LocationProviderManager;->setMockProvider(Lcom/android/server/location/provider/MockLocationProvider;)V

    add-int/lit8 v9, v9, 0x1

    const/4 v4, 0x1

    const/4 v6, 0x0

    goto :goto_4

    :cond_c
    return-void
.end method
""",
        "replacement": """\
.method onSystemThirdPartyAppsCanStart()V
    .registers 18

    goto :goto_31

    nop

    :goto_0
    invoke-static {v14}, Ljava/lang/Integer;->parseInt(Ljava/lang/String;)I

    move-result v14

    goto :goto_8b

    nop

    :goto_1
    iget-object v9, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    goto :goto_7a

    nop

    :goto_2
    iget-object v12, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    goto :goto_2c

    nop

    :goto_3
    invoke-static {v3, v5}, Lcom/android/internal/util/Preconditions;->checkState(ZLjava/lang/String;)V

    goto :goto_93

    nop

    :goto_4
    const/4 v14, 0x3

    goto :goto_39

    nop

    :goto_5
    const v8, 0x10700e1

    goto :goto_bc

    nop

    :goto_6
    return-void

    :goto_7
    const/16 v11, 0x3ea

    goto :goto_56

    nop

    :goto_8
    invoke-virtual {v3}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v3

    goto :goto_18

    nop

    :goto_9
    if-nez v1, :cond_0

    goto :goto_c7

    :cond_0
    goto :goto_5a

    nop

    :goto_a
    const-string v14, "gps_hardware"

    goto :goto_61

    nop

    :goto_b
    const v10, 0x1110175

    goto :goto_db

    nop

    :goto_c
    const v10, 0x1110299

    goto :goto_90

    nop

    :goto_d
    aget-object v14, v11, v14

    goto :goto_aa

    nop

    :goto_e
    new-instance v5, Lcom/android/server/location/provider/LocationProviderManager;

    goto :goto_70

    nop

    :goto_f
    const/4 v14, 0x7

    goto :goto_86

    nop

    :goto_10
    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mPopulationDensityProvider:Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;

    goto :goto_62

    nop

    :goto_11
    invoke-interface {v7, v8, v9}, Lcom/android/server/location/LocationManagerServiceStub;->onSystemThirdPartyAppsCanStart(Ljava/util/concurrent/CopyOnWriteArrayList;Lcom/android/server/location/gnss/GnssManagerService;)V

    goto :goto_cd

    nop

    :goto_12
    invoke-direct {v9, v10, v11, v8}, Lcom/android/server/location/gnss/GnssManagerService;-><init>(Landroid/content/Context;Lcom/android/server/location/injector/Injector;Lcom/android/server/location/gnss/hal/GnssNative;)V

    goto :goto_79

    nop

    :goto_13
    new-instance v13, Landroid/location/provider/ProviderProperties$Builder;

    goto :goto_74

    nop

    :goto_14
    const-string v8, "unable to bind ActivityRecognitionProxy"

    goto :goto_3f

    nop

    :goto_15
    if-eqz v9, :cond_1

    goto :goto_1e

    :cond_1
    goto :goto_8c

    nop

    :goto_16
    goto :goto_b9

    :goto_17
    goto :goto_b1

    nop

    :goto_18
    new-instance v4, Landroid/content/Intent;

    goto :goto_7f

    nop

    :goto_19
    invoke-virtual {v5, v7}, Landroid/content/pm/PackageManager;->hasSystemFeature(Ljava/lang/String;)Z

    move-result v5

    goto :goto_cf

    nop

    :goto_1a
    const v16, 0x11101ba

    goto :goto_e7

    nop

    :goto_1b
    invoke-static {v2, v9}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :goto_1c
    goto :goto_8a

    nop

    :goto_1d
    invoke-static/range {v11 .. v16}, Lcom/android/server/location/provider/proxy/ProxyLocationProvider;->create(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;III)Lcom/android/server/location/provider/proxy/ProxyLocationProvider;

    move-result-object v10

    :goto_1e
    goto :goto_89

    nop

    :goto_1f
    aget-object v14, v11, v14

    goto :goto_e0

    nop

    :goto_20
    invoke-interface {v12, v13}, Lcom/android/server/location/LocationManagerServiceStub;->startPowerSaveListener(Landroid/content/Context;)V

    :goto_21
    goto :goto_9b

    nop

    :goto_22
    if-eqz v8, :cond_2

    goto :goto_1c

    :cond_2
    goto :goto_a5

    nop

    :goto_23
    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasSpeedSupport(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    goto :goto_f

    nop

    :goto_24
    invoke-static {v7}, Lcom/android/server/location/HardwareActivityRecognitionProxy;->createAndRegister(Landroid/content/Context;)Lcom/android/server/location/HardwareActivityRecognitionProxy;

    move-result-object v7

    goto :goto_72

    nop

    :goto_25
    iget-object v3, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_8

    nop

    :goto_26
    const-string v14, "android.permission.LOCATION_HARDWARE"

    goto :goto_7e

    nop

    :goto_27
    move v10, v6

    :goto_28
    goto :goto_7

    nop

    :goto_29
    invoke-virtual {v9}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v9

    goto :goto_c

    nop

    :goto_2a
    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasMonetaryCost(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    goto :goto_b3

    nop

    :goto_2b
    invoke-virtual {v0, v5, v3}, Lcom/android/server/location/LocationManagerService;->addLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;Lcom/android/server/location/provider/AbstractLocationProvider;)V

    goto :goto_16

    nop

    :goto_2c
    invoke-virtual {v12}, Lcom/android/server/location/gnss/GnssManagerService;->getGnssLocationProvider()Lcom/android/server/location/gnss/GnssLocationProvider;

    move-result-object v12

    goto :goto_2e

    nop

    :goto_2d
    if-nez v3, :cond_3

    goto :goto_17

    :cond_3
    goto :goto_e

    nop

    :goto_2e
    invoke-virtual {v0, v11, v12}, Lcom/android/server/location/LocationManagerService;->addLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;Lcom/android/server/location/provider/AbstractLocationProvider;)V

    :goto_2f
    goto :goto_91

    nop

    :goto_30
    invoke-virtual {v14, v15}, Lcom/android/server/location/provider/LocationProviderManager;->setMockProvider(Lcom/android/server/location/provider/MockLocationProvider;)V

    goto :goto_e8

    nop

    :goto_31
    move-object/from16 v0, p0

    goto :goto_a0

    nop

    :goto_32
    invoke-static {v4}, Landroid/location/util/identity/CallerIdentity;->fromContext(Landroid/content/Context;)Landroid/location/util/identity/CallerIdentity;

    move-result-object v4

    goto :goto_58

    nop

    :goto_33
    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasBearingSupport(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    goto :goto_e5

    nop

    :goto_34
    const-string v14, "gps"

    goto :goto_c2

    nop

    :goto_35
    const-string v4, "network"

    goto :goto_d9

    nop

    :goto_36
    invoke-virtual {v11}, Lcom/android/server/location/gnss/GnssManagerService;->getGnssLocationProvider()Lcom/android/server/location/gnss/GnssLocationProvider;

    move-result-object v10

    goto :goto_95

    nop

    :goto_37
    iget-object v10, v0, Lcom/android/server/location/LocationManagerService;->mPopulationDensityProvider:Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;

    goto :goto_44

    nop

    :goto_38
    iget-object v9, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    goto :goto_a2

    nop

    :goto_39
    aget-object v14, v11, v14

    goto :goto_d7

    nop

    :goto_3a
    move v10, v4

    goto :goto_4d

    nop

    :goto_3b
    goto :goto_6f

    :goto_3c
    goto :goto_6

    nop

    :goto_3d
    new-instance v11, Lcom/android/server/location/provider/LocationProviderManager;

    goto :goto_66

    nop

    :goto_3e
    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    goto :goto_23

    nop

    :goto_3f
    invoke-static {v2, v8}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :goto_40
    goto :goto_bf

    nop

    :goto_41
    invoke-static {}, Lcom/android/server/location/gnss/hal/GnssNative;->isSupported()Z

    move-result v7

    goto :goto_50

    nop

    :goto_42
    if-lt v9, v8, :cond_4

    goto :goto_3c

    :cond_4
    goto :goto_c4

    nop

    :goto_43
    const v2, 0x1110184

    goto :goto_9a

    nop

    :goto_44
    if-eqz v10, :cond_5

    goto :goto_65

    :cond_5
    goto :goto_be

    nop

    :goto_45
    iget-object v10, v0, Lcom/android/server/location/LocationManagerService;->mPassiveManager:Lcom/android/server/location/provider/PassiveLocationProviderManager;

    goto :goto_ca

    nop

    :goto_46
    const/4 v6, 0x0

    goto :goto_8d

    nop

    :goto_47
    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_24

    nop

    :goto_48
    const-string v2, "LocationManagerService"

    goto :goto_9

    nop

    :goto_49
    if-eqz v10, :cond_6

    goto :goto_4e

    :cond_6
    goto :goto_3a

    nop

    :goto_4a
    const/4 v14, 0x2

    goto :goto_77

    nop

    :goto_4b
    iget-object v9, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_da

    nop

    :goto_4c
    invoke-virtual {v5}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v5

    goto :goto_99

    nop

    :goto_4d
    goto :goto_28

    :goto_4e
    goto :goto_27

    nop

    :goto_4f
    iget-object v9, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    goto :goto_11

    nop

    :goto_50
    if-nez v7, :cond_7

    goto :goto_21

    :cond_7
    goto :goto_d2

    nop

    :goto_51
    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    goto :goto_4f

    nop

    :goto_52
    iget-object v13, v0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    goto :goto_34

    nop

    :goto_53
    aget-object v12, v11, v6

    goto :goto_6c

    nop

    :goto_54
    const-string v5, "Unable to find a direct boot aware fused location provider"

    goto :goto_3

    nop

    :goto_55
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->densityBasedCoarseLocations()Z

    move-result v7

    goto :goto_ec

    nop

    :goto_56
    invoke-static {v11, v10, v9}, Lcom/android/internal/util/FrameworkStatsLog;->write(IZI)V

    :goto_57
    goto :goto_10

    nop

    :goto_58
    invoke-static {}, Ljava/util/Collections;->emptySet()Ljava/util/Set;

    move-result-object v6

    goto :goto_7c

    nop

    :goto_59
    new-instance v15, Lcom/android/server/location/provider/MockLocationProvider;

    goto :goto_5e

    nop

    :goto_5a
    new-instance v3, Lcom/android/server/location/provider/LocationProviderManager;

    goto :goto_ea

    nop

    :goto_5b
    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mPassiveManager:Lcom/android/server/location/provider/PassiveLocationProviderManager;

    goto :goto_84

    nop

    :goto_5c
    const-string v7, "no geocoder provider found"

    goto :goto_a7

    nop

    :goto_5d
    if-eqz v7, :cond_8

    goto :goto_a8

    :cond_8
    goto :goto_5c

    nop

    :goto_5e
    iget-object v4, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_32

    nop

    :goto_5f
    iget-object v11, v0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    goto :goto_12

    nop

    :goto_60
    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    goto :goto_33

    nop

    :goto_61
    const/4 v15, 0x0

    goto :goto_b0

    nop

    :goto_62
    if-nez v7, :cond_9

    goto :goto_cc

    :cond_9
    goto :goto_55

    nop

    :goto_63
    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v12

    goto :goto_c8

    nop

    :goto_64
    invoke-static {v2, v10}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :goto_65
    goto :goto_df

    nop

    :goto_66
    iget-object v12, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_ce

    nop

    :goto_67
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v7

    goto :goto_4b

    nop

    :goto_68
    invoke-direct {v4, v5}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    goto :goto_c0

    nop

    :goto_69
    aget-object v14, v11, v14

    goto :goto_3e

    nop

    :goto_6a
    const/4 v14, 0x6

    goto :goto_69

    nop

    :goto_6b
    invoke-virtual {v0, v3, v1}, Lcom/android/server/location/LocationManagerService;->addLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;Lcom/android/server/location/provider/AbstractLocationProvider;)V

    goto :goto_c6

    nop

    :goto_6c
    invoke-virtual {v12}, Ljava/lang/String;->trim()Ljava/lang/String;

    move-result-object v12

    goto :goto_13

    nop

    :goto_6d
    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mGeocodeProvider:Lcom/android/server/location/provider/proxy/ProxyGeocodeProvider;

    goto :goto_5d

    nop

    :goto_6e
    move v9, v6

    :goto_6f
    goto :goto_42

    nop

    :goto_70
    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_d5

    nop

    :goto_71
    invoke-virtual {v13}, Landroid/location/provider/ProviderProperties$Builder;->build()Landroid/location/provider/ProviderProperties;

    move-result-object v13

    goto :goto_98

    nop

    :goto_72
    if-eqz v7, :cond_a

    goto :goto_40

    :cond_a
    goto :goto_14

    nop

    :goto_73
    const/4 v4, 0x1

    goto :goto_a3

    nop

    :goto_74
    invoke-direct {v13}, Landroid/location/provider/ProviderProperties$Builder;-><init>()V

    goto :goto_dd

    nop

    :goto_75
    sub-long/2addr v9, v7

    goto :goto_9f

    nop

    :goto_76
    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mPopulationDensityProvider:Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;

    goto :goto_9c

    nop

    :goto_77
    aget-object v14, v11, v14

    goto :goto_d0

    nop

    :goto_78
    const v14, 0x111017b

    goto :goto_1d

    nop

    :goto_79
    iput-object v9, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    goto :goto_1

    nop

    :goto_7a
    invoke-virtual {v9}, Lcom/android/server/location/gnss/GnssManagerService;->onSystemReady()V

    goto :goto_d1

    nop

    :goto_7b
    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    goto :goto_8e

    nop

    :goto_7c
    invoke-direct {v15, v13, v4, v6}, Lcom/android/server/location/provider/MockLocationProvider;-><init>(Landroid/location/provider/ProviderProperties;Landroid/location/util/identity/CallerIdentity;Ljava/util/Set;)V

    goto :goto_30

    nop

    :goto_7d
    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasNetworkRequirement(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    goto :goto_4a

    nop

    :goto_7e
    invoke-static {v14}, Ljava/util/Collections;->singletonList(Ljava/lang/Object;)Ljava/util/List;

    move-result-object v16

    goto :goto_a

    nop

    :goto_7f
    const-string v5, "com.android.location.service.FusedLocationProvider"

    goto :goto_68

    nop

    :goto_80
    iget-object v12, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_52

    nop

    :goto_81
    const-string v3, "no network location provider found"

    goto :goto_ba

    nop

    :goto_82
    iget-object v6, v0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    goto :goto_5b

    nop

    :goto_83
    invoke-direct {v7, v8}, Lcom/android/server/location/gnss/GnssConfiguration;-><init>(Landroid/content/Context;)V

    goto :goto_7b

    nop

    :goto_84
    invoke-direct {v3, v5, v6, v4, v7}, Lcom/android/server/location/provider/LocationProviderManager;-><init>(Landroid/content/Context;Lcom/android/server/location/injector/Injector;Ljava/lang/String;Lcom/android/server/location/provider/PassiveLocationProviderManager;)V

    goto :goto_6b

    nop

    :goto_85
    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasSatelliteRequirement(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    goto :goto_4

    nop

    :goto_86
    aget-object v14, v11, v14

    goto :goto_60

    nop

    :goto_87
    const/16 v14, 0x9

    goto :goto_b7

    nop

    :goto_88
    invoke-virtual {v10, v11}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v11

    goto :goto_53

    nop

    :goto_89
    if-eqz v10, :cond_b

    goto :goto_96

    :cond_b
    goto :goto_c3

    nop

    :goto_8a
    iget-object v2, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_b6

    nop

    :goto_8b
    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setAccuracy(I)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    goto :goto_71

    nop

    :goto_8c
    iget-object v11, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_ad

    nop

    :goto_8d
    invoke-virtual {v3, v4, v5, v6}, Landroid/content/pm/PackageManager;->queryIntentServicesAsUser(Landroid/content/Intent;II)Ljava/util/List;

    move-result-object v3

    goto :goto_ac

    nop

    :goto_8e
    invoke-static {v8, v7}, Lcom/android/server/location/gnss/hal/GnssNative;->create(Lcom/android/server/location/injector/Injector;Lcom/android/server/location/gnss/GnssConfiguration;)Lcom/android/server/location/gnss/hal/GnssNative;

    move-result-object v8

    goto :goto_e2

    nop

    :goto_8f
    invoke-virtual {v0, v9}, Lcom/android/server/location/LocationManagerService;->setProxyPopulationDensityProvider(Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;)V

    goto :goto_ae

    nop

    :goto_90
    invoke-virtual {v9, v10}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v9

    goto :goto_e3

    nop

    :goto_91
    new-instance v11, Lcom/android/server/location/provider/LocationProviderManager;

    goto :goto_80

    nop

    :goto_92
    const-string v11, ","

    goto :goto_88

    nop

    :goto_93
    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_eb

    nop

    :goto_94
    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    goto :goto_d6

    nop

    :goto_95
    goto :goto_2f

    :goto_96
    goto :goto_3d

    nop

    :goto_97
    if-nez v7, :cond_c

    goto :goto_57

    :cond_c
    goto :goto_67

    nop

    :goto_98
    invoke-direct {v0, v12}, Lcom/android/server/location/LocationManagerService;->getOrAddLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object v14

    goto :goto_59

    nop

    :goto_99
    const-string v7, "android.hardware.location"

    goto :goto_19

    nop

    :goto_9a
    const v3, 0x10402fc

    goto :goto_35

    nop

    :goto_9b
    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v7

    goto :goto_51

    nop

    :goto_9c
    invoke-direct {v7, v8}, Lcom/android/server/location/fudger/LocationFudgerCache;-><init>(Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;)V

    goto :goto_cb

    nop

    :goto_9d
    const-string v8, "fused"

    goto :goto_d3

    nop

    :goto_9e
    iget-object v10, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_5f

    nop

    :goto_9f
    long-to-int v9, v9

    goto :goto_37

    nop

    :goto_a0
    iget-object v1, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_43

    nop

    :goto_a1
    invoke-static {v7}, Lcom/android/server/location/provider/proxy/ProxyGeocodeProvider;->createAndRegister(Landroid/content/Context;)Lcom/android/server/location/provider/proxy/ProxyGeocodeProvider;

    move-result-object v7

    goto :goto_b4

    nop

    :goto_a2
    invoke-virtual {v9}, Lcom/android/server/location/gnss/GnssManagerService;->getGnssGeofenceProxy()Landroid/location/IGpsGeofenceHardware;

    move-result-object v9

    goto :goto_ee

    nop

    :goto_a3
    const/4 v6, 0x0

    goto :goto_3b

    nop

    :goto_a4
    invoke-direct {v11, v12, v13, v14, v15}, Lcom/android/server/location/provider/LocationProviderManager;-><init>(Landroid/content/Context;Lcom/android/server/location/injector/Injector;Ljava/lang/String;Lcom/android/server/location/provider/PassiveLocationProviderManager;)V

    goto :goto_e6

    nop

    :goto_a5
    const-string v9, "unable to bind to GeofenceProxy"

    goto :goto_1b

    nop

    :goto_a6
    invoke-static {v1, v4, v5, v2, v3}, Lcom/android/server/location/provider/proxy/ProxyLocationProvider;->create(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;II)Lcom/android/server/location/provider/proxy/ProxyLocationProvider;

    move-result-object v1

    goto :goto_48

    nop

    :goto_a7
    invoke-static {v2, v7}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :goto_a8
    goto :goto_bd

    nop

    :goto_a9
    const/4 v4, 0x1

    goto :goto_ab

    nop

    :goto_aa
    invoke-static {v14}, Ljava/lang/Integer;->parseInt(Ljava/lang/String;)I

    move-result v14

    goto :goto_d4

    nop

    :goto_ab
    xor-int/2addr v3, v4

    goto :goto_54

    nop

    :goto_ac
    invoke-interface {v3}, Ljava/util/List;->isEmpty()Z

    move-result v3

    goto :goto_a9

    nop

    :goto_ad
    const v15, 0x10402df

    goto :goto_1a

    nop

    :goto_ae
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v9

    goto :goto_75

    nop

    :goto_af
    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    goto :goto_7d

    nop

    :goto_b0
    invoke-direct/range {v11 .. v16}, Lcom/android/server/location/provider/LocationProviderManager;-><init>(Landroid/content/Context;Lcom/android/server/location/injector/Injector;Ljava/lang/String;Lcom/android/server/location/provider/PassiveLocationProviderManager;Ljava/util/Collection;)V

    goto :goto_2

    nop

    :goto_b1
    const-string v5, "no fused location provider found"

    goto :goto_b8

    nop

    :goto_b2
    array-length v8, v2

    goto :goto_6e

    nop

    :goto_b3
    const/4 v14, 0x5

    goto :goto_c5

    nop

    :goto_b4
    iput-object v7, v0, Lcom/android/server/location/LocationManagerService;->mGeocodeProvider:Lcom/android/server/location/provider/proxy/ProxyGeocodeProvider;

    goto :goto_6d

    nop

    :goto_b5
    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_83

    nop

    :goto_b6
    invoke-virtual {v2}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    goto :goto_5

    nop

    :goto_b7
    aget-object v14, v11, v14

    goto :goto_0

    nop

    :goto_b8
    invoke-static {v2, v5}, Landroid/util/Log;->wtf(Ljava/lang/String;Ljava/lang/String;)I

    :goto_b9
    goto :goto_ed

    nop

    :goto_ba
    invoke-static {v2, v3}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    :goto_bb
    goto :goto_25

    nop

    :goto_bc
    invoke-virtual {v2, v8}, Landroid/content/res/Resources;->getStringArray(I)[Ljava/lang/String;

    move-result-object v2

    goto :goto_b2

    nop

    :goto_bd
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->populationDensityProvider()Z

    move-result v7

    goto :goto_97

    nop

    :goto_be
    const-string v10, "no population density provider found"

    goto :goto_64

    nop

    :goto_bf
    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    goto :goto_c9

    nop

    :goto_c0
    const/high16 v5, 0x180000

    goto :goto_46

    nop

    :goto_c1
    const-string v13, "android.location.provider.action.GNSS_PROVIDER"

    goto :goto_78

    nop

    :goto_c2
    iget-object v15, v0, Lcom/android/server/location/LocationManagerService;->mPassiveManager:Lcom/android/server/location/provider/PassiveLocationProviderManager;

    goto :goto_a4

    nop

    :goto_c3
    iget-object v11, v0, Lcom/android/server/location/LocationManagerService;->mGnssManagerService:Lcom/android/server/location/gnss/GnssManagerService;

    goto :goto_36

    nop

    :goto_c4
    aget-object v10, v2, v9

    goto :goto_92

    nop

    :goto_c5
    aget-object v14, v11, v14

    goto :goto_94

    nop

    :goto_c6
    goto :goto_bb

    :goto_c7
    goto :goto_81

    nop

    :goto_c8
    iget-object v13, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_20

    nop

    :goto_c9
    if-nez v8, :cond_d

    goto :goto_1c

    :cond_d
    goto :goto_e9

    nop

    :goto_ca
    invoke-direct {v5, v7, v8, v9, v10}, Lcom/android/server/location/provider/LocationProviderManager;-><init>(Landroid/content/Context;Lcom/android/server/location/injector/Injector;Ljava/lang/String;Lcom/android/server/location/provider/PassiveLocationProviderManager;)V

    goto :goto_2b

    nop

    :goto_cb
    invoke-virtual {v0, v7}, Lcom/android/server/location/LocationManagerService;->setLocationFudgerCache(Lcom/android/server/location/fudger/LocationFudgerCache;)V

    :goto_cc
    goto :goto_47

    nop

    :goto_cd
    iget-object v7, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_a1

    nop

    :goto_ce
    iget-object v13, v0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    goto :goto_26

    nop

    :goto_cf
    if-nez v5, :cond_e

    goto :goto_21

    :cond_e
    goto :goto_41

    nop

    :goto_d0
    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    goto :goto_85

    nop

    :goto_d1
    iget-object v9, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_29

    nop

    :goto_d2
    new-instance v7, Lcom/android/server/location/gnss/GnssConfiguration;

    goto :goto_b5

    nop

    :goto_d3
    const-string v9, "com.android.location.service.FusedLocationProvider"

    goto :goto_b

    nop

    :goto_d4
    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setPowerUsage(I)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    goto :goto_87

    nop

    :goto_d5
    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    goto :goto_d8

    nop

    :goto_d6
    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasAltitudeSupport(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    goto :goto_6a

    nop

    :goto_d7
    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    goto :goto_de

    nop

    :goto_d8
    const-string v9, "fused"

    goto :goto_45

    nop

    :goto_d9
    const-string v5, "com.android.location.service.v3.NetworkLocationProvider"

    goto :goto_a6

    nop

    :goto_da
    invoke-static {v9}, Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;->createAndRegister(Landroid/content/Context;)Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;

    move-result-object v9

    goto :goto_8f

    nop

    :goto_db
    invoke-static/range {v7 .. v12}, Lcom/android/server/location/provider/proxy/ProxyLocationProvider;->create(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;III)Lcom/android/server/location/provider/proxy/ProxyLocationProvider;

    move-result-object v3

    goto :goto_2d

    nop

    :goto_dc
    new-instance v7, Lcom/android/server/location/fudger/LocationFudgerCache;

    goto :goto_76

    nop

    :goto_dd
    aget-object v14, v11, v4

    goto :goto_af

    nop

    :goto_de
    invoke-virtual {v13, v14}, Landroid/location/provider/ProviderProperties$Builder;->setHasCellRequirement(Z)Landroid/location/provider/ProviderProperties$Builder;

    move-result-object v13

    goto :goto_e4

    nop

    :goto_df
    iget-object v10, v0, Lcom/android/server/location/LocationManagerService;->mPopulationDensityProvider:Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;

    goto :goto_49

    nop

    :goto_e0
    invoke-static {v14}, Ljava/lang/Boolean;->parseBoolean(Ljava/lang/String;)Z

    move-result v14

    goto :goto_2a

    nop

    :goto_e1
    const v12, 0x11101b8

    goto :goto_9d

    nop

    :goto_e2
    new-instance v9, Lcom/android/server/location/gnss/GnssManagerService;

    goto :goto_9e

    nop

    :goto_e3
    const/4 v10, 0x0

    goto :goto_15

    nop

    :goto_e4
    const/4 v14, 0x4

    goto :goto_1f

    nop

    :goto_e5
    const/16 v14, 0x8

    goto :goto_d

    nop

    :goto_e6
    invoke-virtual {v0, v11, v10}, Lcom/android/server/location/LocationManagerService;->addLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;Lcom/android/server/location/provider/AbstractLocationProvider;)V

    goto :goto_63

    nop

    :goto_e7
    const-string v12, "gps"

    goto :goto_c1

    nop

    :goto_e8
    add-int/lit8 v9, v9, 0x1

    goto :goto_73

    nop

    :goto_e9
    iget-object v8, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_38

    nop

    :goto_ea
    iget-object v5, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_82

    nop

    :goto_eb
    const v11, 0x10402da

    goto :goto_e1

    nop

    :goto_ec
    if-nez v7, :cond_f

    goto :goto_cc

    :cond_f
    goto :goto_dc

    nop

    :goto_ed
    iget-object v5, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    goto :goto_4c

    nop

    :goto_ee
    invoke-static {v8, v9}, Lcom/android/server/location/geofence/GeofenceProxy;->createAndBind(Landroid/content/Context;Landroid/location/IGpsGeofenceHardware;)Lcom/android/server/location/geofence/GeofenceProxy;

    move-result-object v8

    goto :goto_22

    nop
.end method
""",
        "method_anchors": ['iget-object v1, v0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;', 'const-string v4, "network"', 'const-string v5, "com.android.location.service.v3.NetworkLocationProvider"', 'invoke-static {v1, v4, v5, v2, v3}, Lcom/android/server/location/provider/proxy/ProxyLocationProvider;->create(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;II)Lcom/android/server/location/provider/proxy/ProxyLocationProvider;', 'move-result-object v1', 'const-string v2, "LocationManagerService"'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_removeTestProvider_Ljava_lang_String_Ljava_lang_String_Ljava",
        "method":      ".method public removeTestProvider(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V",
        "method_name": 'removeTestProvider',
        "type":        "method_replace",
        "search": """\
.method public removeTestProvider(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
    .registers 9

    invoke-static {p2, p3}, Landroid/location/util/identity/CallerIdentity;->fromBinderUnsafe(Ljava/lang/String;Ljava/lang/String;)Landroid/location/util/identity/CallerIdentity;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getAppOpsHelper()Lcom/android/server/location/injector/AppOpsHelper;

    move-result-object v1

    const/16 v2, 0x3a

    invoke-virtual {v1, v2, v0}, Lcom/android/server/location/injector/AppOpsHelper;->noteOp(ILandroid/location/util/identity/CallerIdentity;)Z

    move-result v1

    if-nez v1, :cond_0

    return-void

    :cond_0
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mLock:Ljava/lang/Object;

    monitor-enter v1

    :try_start_0
    invoke-virtual {p0, p1}, Lcom/android/server/location/LocationManagerService;->getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object v2

    if-nez v2, :cond_1

    monitor-exit v1

    return-void

    :cond_1
    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v3

    iget-object v4, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-interface {v3, v4, p1, p2, p3}, Lcom/android/server/location/LocationManagerServiceStub;->removeTestProvider(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Z

    move-result v3

    if-nez v3, :cond_2

    monitor-exit v1

    return-void

    :cond_2
    const/4 v3, 0x0

    invoke-virtual {v2, v3}, Lcom/android/server/location/provider/LocationProviderManager;->setMockProvider(Lcom/android/server/location/provider/MockLocationProvider;)V

    invoke-virtual {v2}, Lcom/android/server/location/provider/LocationProviderManager;->hasProvider()Z

    move-result v3

    if-nez v3, :cond_3

    invoke-direct {p0, v2}, Lcom/android/server/location/LocationManagerService;->removeLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;)V

    :cond_3
    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v1

    iget-object v2, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-interface {v1, v2, p1, p2, p3}, Lcom/android/server/location/LocationManagerServiceStub;->removeTestProvider(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Z

    return-void

    :catchall_0
    move-exception v2

    :try_start_1
    monitor-exit v1
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw v2
.end method
""",
        "replacement": """\
.method public removeTestProvider(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
    .registers 9

    invoke-static {p2, p3}, Landroid/location/util/identity/CallerIdentity;->fromBinderUnsafe(Ljava/lang/String;Ljava/lang/String;)Landroid/location/util/identity/CallerIdentity;

    move-result-object v0

    const/4 v1, 0x1

    const-string v2, "enable_mezo_mock_locations"

    invoke-static {v2, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v2

    if-eqz v2, :cond_0

    if-nez v0, :cond_1

    return-void

    :cond_0
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getAppOpsHelper()Lcom/android/server/location/injector/AppOpsHelper;

    move-result-object v1

    const/16 v2, 0x3a

    invoke-virtual {v1, v2, v0}, Lcom/android/server/location/injector/AppOpsHelper;->noteOp(ILandroid/location/util/identity/CallerIdentity;)Z

    move-result v1

    if-nez v1, :cond_1

    return-void

    :cond_1
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mLock:Ljava/lang/Object;

    monitor-enter v1

    :try_start_0
    invoke-virtual {p0, p1}, Lcom/android/server/location/LocationManagerService;->getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object v2

    if-nez v2, :cond_2

    monitor-exit v1

    return-void

    :cond_2
    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v3

    iget-object v4, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-interface {v3, v4, p1, p2, p3}, Lcom/android/server/location/LocationManagerServiceStub;->removeTestProvider(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Z

    move-result v3

    if-nez v3, :cond_3

    monitor-exit v1

    return-void

    :cond_3
    const/4 v3, 0x0

    invoke-virtual {v2, v3}, Lcom/android/server/location/provider/LocationProviderManager;->setMockProvider(Lcom/android/server/location/provider/MockLocationProvider;)V

    invoke-virtual {v2}, Lcom/android/server/location/provider/LocationProviderManager;->hasProvider()Z

    move-result v3

    if-nez v3, :cond_4

    invoke-direct {p0, v2}, Lcom/android/server/location/LocationManagerService;->removeLocationProviderManager(Lcom/android/server/location/provider/LocationProviderManager;)V

    :cond_4
    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v1

    iget-object v2, p0, Lcom/android/server/location/LocationManagerService;->mContext:Landroid/content/Context;

    invoke-interface {v1, v2, p1, p2, p3}, Lcom/android/server/location/LocationManagerServiceStub;->removeTestProvider(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Z

    return-void

    :catchall_0
    move-exception v2

    :try_start_1
    monitor-exit v1
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw v2
.end method
""",
        "method_anchors": ['invoke-static {p2, p3}, Landroid/location/util/identity/CallerIdentity;->fromBinderUnsafe(Ljava/lang/String;Ljava/lang/String;)Landroid/location/util/identity/CallerIdentity;', 'move-result-object v0', 'iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;', 'invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getAppOpsHelper()Lcom/android/server/location/injector/AppOpsHelper;', 'move-result-object v1', 'invoke-virtual {v1, v2, v0}, Lcom/android/server/location/injector/AppOpsHelper;->noteOp(ILandroid/location/util/identity/CallerIdentity;)Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setLocationFudgerCache_Lcom_android_server_location_fudger_L",
        "method":      ".method protected setLocationFudgerCache(Lcom/android/server/location/fudger/LocationFudgerCache;)V",
        "method_name": 'setLocationFudgerCache',
        "type":        "method_replace",
        "search": """\
.method protected setLocationFudgerCache(Lcom/android/server/location/fudger/LocationFudgerCache;)V
    .registers 4

    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->densityBasedCoarseLocations()Z

    move-result v0

    if-nez v0, :cond_0

    return-void

    :cond_0
    iput-object p1, p0, Lcom/android/server/location/LocationManagerService;->mLocationFudgerCache:Lcom/android/server/location/fudger/LocationFudgerCache;

    iget-object v0, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_1

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/location/provider/LocationProviderManager;

    invoke-virtual {v1, p1}, Lcom/android/server/location/provider/LocationProviderManager;->setLocationFudgerCache(Lcom/android/server/location/fudger/LocationFudgerCache;)V

    goto :goto_0

    :cond_1
    return-void
.end method
""",
        "replacement": """\
.method protected setLocationFudgerCache(Lcom/android/server/location/fudger/LocationFudgerCache;)V
    .registers 4

    goto :goto_a

    nop

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_1

    nop

    :goto_1
    if-nez v1, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_f

    nop

    :goto_2
    return-void

    :goto_3
    iget-object v0, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;

    goto :goto_c

    nop

    :goto_4
    if-eqz v0, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_5

    nop

    :goto_5
    return-void

    :goto_6
    goto :goto_b

    nop

    :goto_7
    check-cast v1, Lcom/android/server/location/provider/LocationProviderManager;

    goto :goto_e

    nop

    :goto_8
    goto :goto_d

    :goto_9
    goto :goto_2

    nop

    :goto_a
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->densityBasedCoarseLocations()Z

    move-result v0

    goto :goto_4

    nop

    :goto_b
    iput-object p1, p0, Lcom/android/server/location/LocationManagerService;->mLocationFudgerCache:Lcom/android/server/location/fudger/LocationFudgerCache;

    goto :goto_3

    nop

    :goto_c
    invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_d
    goto :goto_0

    nop

    :goto_e
    invoke-virtual {v1, p1}, Lcom/android/server/location/provider/LocationProviderManager;->setLocationFudgerCache(Lcom/android/server/location/fudger/LocationFudgerCache;)V

    goto :goto_8

    nop

    :goto_f
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_7

    nop
.end method
""",
        "method_anchors": ['invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->densityBasedCoarseLocations()Z', 'move-result v0', 'if-nez v0, :cond_0', 'return-void', 'iput-object p1, p0, Lcom/android/server/location/LocationManagerService;->mLocationFudgerCache:Lcom/android/server/location/fudger/LocationFudgerCache;', 'iget-object v0, p0, Lcom/android/server/location/LocationManagerService;->mProviderManagers:Ljava/util/concurrent/CopyOnWriteArrayList;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setProxyPopulationDensityProvider_Lcom_android_server_locati",
        "method":      ".method protected setProxyPopulationDensityProvider(Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;)V",
        "method_name": 'setProxyPopulationDensityProvider',
        "type":        "method_replace",
        "search": """\
.method protected setProxyPopulationDensityProvider(Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;)V
    .registers 3

    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->populationDensityProvider()Z

    move-result v0

    if-eqz v0, :cond_0

    iput-object p1, p0, Lcom/android/server/location/LocationManagerService;->mPopulationDensityProvider:Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;

    :cond_0
    return-void
.end method
""",
        "replacement": """\
.method protected setProxyPopulationDensityProvider(Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_3

    nop

    :goto_2
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->populationDensityProvider()Z

    move-result v0

    goto :goto_1

    nop

    :goto_3
    iput-object p1, p0, Lcom/android/server/location/LocationManagerService;->mPopulationDensityProvider:Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;

    :goto_4
    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/location/flags/Flags;->populationDensityProvider()Z', 'move-result v0', 'if-eqz v0, :cond_0', 'iput-object p1, p0, Lcom/android/server/location/LocationManagerService;->mPopulationDensityProvider:Lcom/android/server/location/provider/proxy/ProxyPopulationDensityProvider;', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setTestProviderEnabled_Ljava_lang_String_ZLjava_lang_String_",
        "method":      ".method public setTestProviderEnabled(Ljava/lang/String;ZLjava/lang/String;Ljava/lang/String;)V",
        "method_name": 'setTestProviderEnabled',
        "type":        "method_replace",
        "search": """\
.method public setTestProviderEnabled(Ljava/lang/String;ZLjava/lang/String;Ljava/lang/String;)V
    .registers 10

    invoke-static {p3, p4}, Landroid/location/util/identity/CallerIdentity;->fromBinderUnsafe(Ljava/lang/String;Ljava/lang/String;)Landroid/location/util/identity/CallerIdentity;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getAppOpsHelper()Lcom/android/server/location/injector/AppOpsHelper;

    move-result-object v1

    const/16 v2, 0x3a

    invoke-virtual {v1, v2, v0}, Lcom/android/server/location/injector/AppOpsHelper;->noteOp(ILandroid/location/util/identity/CallerIdentity;)Z

    move-result v1

    if-nez v1, :cond_0

    return-void

    :cond_0
    invoke-virtual {p0, p1}, Lcom/android/server/location/LocationManagerService;->getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object v1

    if-eqz v1, :cond_1

    invoke-virtual {v1, p2}, Lcom/android/server/location/provider/LocationProviderManager;->setMockProviderAllowed(Z)V

    return-void

    :cond_1
    new-instance v2, Ljava/lang/IllegalArgumentException;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "provider doesn\\'t exist: "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    throw v2
.end method
""",
        "replacement": """\
.method public setTestProviderEnabled(Ljava/lang/String;ZLjava/lang/String;Ljava/lang/String;)V
    .registers 10

    invoke-static {p3, p4}, Landroid/location/util/identity/CallerIdentity;->fromBinderUnsafe(Ljava/lang/String;Ljava/lang/String;)Landroid/location/util/identity/CallerIdentity;

    move-result-object v0

    const/4 v1, 0x1

    const-string v2, "enable_mezo_mock_locations"

    invoke-static {v2, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v2

    if-eqz v2, :cond_0

    if-nez v0, :cond_1

    return-void

    :cond_0
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getAppOpsHelper()Lcom/android/server/location/injector/AppOpsHelper;

    move-result-object v1

    const/16 v2, 0x3a

    invoke-virtual {v1, v2, v0}, Lcom/android/server/location/injector/AppOpsHelper;->noteOp(ILandroid/location/util/identity/CallerIdentity;)Z

    move-result v1

    if-nez v1, :cond_1

    return-void

    :cond_1
    invoke-virtual {p0, p1}, Lcom/android/server/location/LocationManagerService;->getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object v1

    if-eqz v1, :cond_2

    invoke-virtual {v1, p2}, Lcom/android/server/location/provider/LocationProviderManager;->setMockProviderAllowed(Z)V

    return-void

    :cond_2
    new-instance v2, Ljava/lang/IllegalArgumentException;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "provider doesn\\'t exist: "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    throw v2
.end method
""",
        "method_anchors": ['invoke-static {p3, p4}, Landroid/location/util/identity/CallerIdentity;->fromBinderUnsafe(Ljava/lang/String;Ljava/lang/String;)Landroid/location/util/identity/CallerIdentity;', 'move-result-object v0', 'iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;', 'invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getAppOpsHelper()Lcom/android/server/location/injector/AppOpsHelper;', 'move-result-object v1', 'invoke-virtual {v1, v2, v0}, Lcom/android/server/location/injector/AppOpsHelper;->noteOp(ILandroid/location/util/identity/CallerIdentity;)Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setTestProviderLocation_Ljava_lang_String_Landroid_location_",
        "method":      ".method public setTestProviderLocation(Ljava/lang/String;Landroid/location/Location;Ljava/lang/String;Ljava/lang/String;)V",
        "method_name": 'setTestProviderLocation',
        "type":        "method_replace",
        "search": """\
.method public setTestProviderLocation(Ljava/lang/String;Landroid/location/Location;Ljava/lang/String;Ljava/lang/String;)V
    .registers 10

    invoke-static {p3, p4}, Landroid/location/util/identity/CallerIdentity;->fromBinderUnsafe(Ljava/lang/String;Ljava/lang/String;)Landroid/location/util/identity/CallerIdentity;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getAppOpsHelper()Lcom/android/server/location/injector/AppOpsHelper;

    move-result-object v1

    const/16 v2, 0x3a

    invoke-virtual {v1, v2, v0}, Lcom/android/server/location/injector/AppOpsHelper;->noteOp(ILandroid/location/util/identity/CallerIdentity;)Z

    move-result v1

    if-nez v1, :cond_0

    return-void

    :cond_0
    invoke-virtual {p2}, Landroid/location/Location;->isComplete()Z

    move-result v1

    const-string v2, "incomplete location object, missing timestamp or accuracy?"

    invoke-static {v1, v2}, Lcom/android/internal/util/Preconditions;->checkArgument(ZLjava/lang/Object;)V

    invoke-virtual {p0, p1}, Lcom/android/server/location/LocationManagerService;->getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object v1

    if-eqz v1, :cond_2

    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v2

    invoke-interface {v2, p1, p2}, Lcom/android/server/location/LocationManagerServiceStub;->setTestProviderLocation(Ljava/lang/String;Landroid/location/Location;)Z

    move-result v2

    if-nez v2, :cond_1

    return-void

    :cond_1
    invoke-virtual {v1, p2}, Lcom/android/server/location/provider/LocationProviderManager;->setMockProviderLocation(Landroid/location/Location;)V

    return-void

    :cond_2
    new-instance v2, Ljava/lang/IllegalArgumentException;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "provider doesn\\'t exist: "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    throw v2
.end method
""",
        "replacement": """\
.method public setTestProviderLocation(Ljava/lang/String;Landroid/location/Location;Ljava/lang/String;Ljava/lang/String;)V
    .registers 10

    invoke-static {p3, p4}, Landroid/location/util/identity/CallerIdentity;->fromBinderUnsafe(Ljava/lang/String;Ljava/lang/String;)Landroid/location/util/identity/CallerIdentity;

    move-result-object v0

    const/4 v1, 0x1

    const-string v2, "enable_mezo_mock_locations"

    invoke-static {v2, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v2

    if-eqz v2, :cond_0

    if-nez v0, :cond_1

    return-void

    :cond_0
    iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;

    invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getAppOpsHelper()Lcom/android/server/location/injector/AppOpsHelper;

    move-result-object v1

    const/16 v2, 0x3a

    invoke-virtual {v1, v2, v0}, Lcom/android/server/location/injector/AppOpsHelper;->noteOp(ILandroid/location/util/identity/CallerIdentity;)Z

    move-result v1

    if-nez v1, :cond_1

    return-void

    :cond_1
    invoke-virtual {p2}, Landroid/location/Location;->isComplete()Z

    move-result v1

    const-string v2, "incomplete location object, missing timestamp or accuracy?"

    invoke-static {v1, v2}, Lcom/android/internal/util/Preconditions;->checkArgument(ZLjava/lang/Object;)V

    invoke-virtual {p0, p1}, Lcom/android/server/location/LocationManagerService;->getLocationProviderManager(Ljava/lang/String;)Lcom/android/server/location/provider/LocationProviderManager;

    move-result-object v1

    if-eqz v1, :cond_3

    invoke-static {}, Lcom/android/server/location/LocationManagerServiceStub;->getInstance()Lcom/android/server/location/LocationManagerServiceStub;

    move-result-object v2

    invoke-interface {v2, p1, p2}, Lcom/android/server/location/LocationManagerServiceStub;->setTestProviderLocation(Ljava/lang/String;Landroid/location/Location;)Z

    move-result v2

    if-nez v2, :cond_2

    return-void

    :cond_2
    invoke-virtual {v1, p2}, Lcom/android/server/location/provider/LocationProviderManager;->setMockProviderLocation(Landroid/location/Location;)V

    return-void

    :cond_3
    new-instance v2, Ljava/lang/IllegalArgumentException;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "provider doesn\\'t exist: "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    throw v2
.end method
""",
        "method_anchors": ['invoke-static {p3, p4}, Landroid/location/util/identity/CallerIdentity;->fromBinderUnsafe(Ljava/lang/String;Ljava/lang/String;)Landroid/location/util/identity/CallerIdentity;', 'move-result-object v0', 'iget-object v1, p0, Lcom/android/server/location/LocationManagerService;->mInjector:Lcom/android/server/location/injector/Injector;', 'invoke-interface {v1}, Lcom/android/server/location/injector/Injector;->getAppOpsHelper()Lcom/android/server/location/injector/AppOpsHelper;', 'move-result-object v1', 'invoke-virtual {v1, v2, v0}, Lcom/android/server/location/injector/AppOpsHelper;->noteOp(ILandroid/location/util/identity/CallerIdentity;)Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
]
