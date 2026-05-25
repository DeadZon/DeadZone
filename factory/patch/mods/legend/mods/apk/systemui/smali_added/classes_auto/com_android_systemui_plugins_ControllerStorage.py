"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/plugins/ControllerStorage.smali'
CLASS_FALLBACK_NAMES = ['ControllerStorage.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/plugins/ControllerStorage;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/plugins/ControllerStorage$ControllerStorageKey;
    }
.end annotation


# static fields
.field public static sControllerStorage:Lcom/android/systemui/plugins/ControllerStorage;
    .annotation build Landroid/annotation/SuppressLint;
        value = {
            "StaticFieldLeak"
        }
    .end annotation
.end field


# instance fields
.field private final context:Landroid/content/Context;

.field public final mControllers:Landroid/util/ArrayMap;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Landroid/util/ArrayMap",
            "<",
            "Ljava/lang/Object;",
            "Ljava/lang/Object;",
            ">;"
        }
    .end annotation
.end field


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Landroid/util/ArrayMap;

    invoke-direct {v0}, Landroid/util/ArrayMap;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/plugins/ControllerStorage;->mControllers:Landroid/util/ArrayMap;

    iput-object p1, p0, Lcom/android/systemui/plugins/ControllerStorage;->context:Landroid/content/Context;

    invoke-static {p0}, Lcom/android/systemui/plugins/ControllerStorage;->setInstance(Lcom/android/systemui/plugins/ControllerStorage;)V

    invoke-virtual {p0}, Lcom/android/systemui/plugins/ControllerStorage;->start()V

    return-void
.end method

.method public static destroy(Ljava/lang/Class;Ljava/util/function/Consumer;)V
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Ljava/lang/Object;",
            ">(",
            "Ljava/lang/Class",
            "<TT;>;",
            "Ljava/util/function/Consumer",
            "<TT;>;)V"
        }
    .end annotation

    sget-object v0, Lcom/android/systemui/plugins/ControllerStorage;->sControllerStorage:Lcom/android/systemui/plugins/ControllerStorage;

    invoke-virtual {v0, p0, p1}, Lcom/android/systemui/plugins/ControllerStorage;->destroyControllerStorage(Ljava/lang/Class;Ljava/util/function/Consumer;)V

    return-void
.end method

.method public static get(Lcom/android/systemui/plugins/ControllerStorage$ControllerStorageKey;)Ljava/lang/Object;
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Ljava/lang/Object;",
            ">(",
            "Lcom/android/systemui/plugins/ControllerStorage$ControllerStorageKey",
            "<TT;>;)TT;"
        }
    .end annotation

    sget-object v0, Lcom/android/systemui/plugins/ControllerStorage;->sControllerStorage:Lcom/android/systemui/plugins/ControllerStorage;

    if-nez v0, :cond_13

    new-instance v1, Lcom/android/systemui/plugins/ControllerStorage;

    const-class v0, Lcom/miui/systemui/SettingsManager;

    invoke-static {v0}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/miui/systemui/SettingsManager;

    iget-object v0, v0, Lcom/miui/systemui/SettingsManager;->context:Landroid/content/Context;

    invoke-direct {v1, v0}, Lcom/android/systemui/plugins/ControllerStorage;-><init>(Landroid/content/Context;)V

    :cond_13
    sget-object v0, Lcom/android/systemui/plugins/ControllerStorage;->sControllerStorage:Lcom/android/systemui/plugins/ControllerStorage;

    invoke-virtual {v0, p0}, Lcom/android/systemui/plugins/ControllerStorage;->getControllerStorage(Lcom/android/systemui/plugins/ControllerStorage$ControllerStorageKey;)Ljava/lang/Object;

    move-result-object v0

    return-object v0
.end method

.method public static get(Ljava/lang/Class;)Ljava/lang/Object;
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Ljava/lang/Object;",
            ">(",
            "Ljava/lang/Class",
            "<TT;>;)TT;"
        }
    .end annotation

    sget-object v0, Lcom/android/systemui/plugins/ControllerStorage;->sControllerStorage:Lcom/android/systemui/plugins/ControllerStorage;

    if-nez v0, :cond_13

    new-instance v1, Lcom/android/systemui/plugins/ControllerStorage;

    const-class v0, Lcom/miui/systemui/SettingsManager;

    invoke-static {v0}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/miui/systemui/SettingsManager;

    iget-object v0, v0, Lcom/miui/systemui/SettingsManager;->context:Landroid/content/Context;

    invoke-direct {v1, v0}, Lcom/android/systemui/plugins/ControllerStorage;-><init>(Landroid/content/Context;)V

    :cond_13
    sget-object v0, Lcom/android/systemui/plugins/ControllerStorage;->sControllerStorage:Lcom/android/systemui/plugins/ControllerStorage;

    invoke-virtual {v0, p0}, Lcom/android/systemui/plugins/ControllerStorage;->getControllerStorage(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    return-object v0
.end method

.method public static setClassInStorage(Landroid/content/Context;Ljava/lang/Object;)V
    .registers 4

    sget-object v0, Lcom/android/systemui/plugins/ControllerStorage;->sControllerStorage:Lcom/android/systemui/plugins/ControllerStorage;

    if-nez v0, :cond_9

    new-instance v0, Lcom/android/systemui/plugins/ControllerStorage;

    invoke-direct {v0, p0}, Lcom/android/systemui/plugins/ControllerStorage;-><init>(Landroid/content/Context;)V

    :cond_9
    sget-object v0, Lcom/android/systemui/plugins/ControllerStorage;->sControllerStorage:Lcom/android/systemui/plugins/ControllerStorage;

    iget-object v0, v0, Lcom/android/systemui/plugins/ControllerStorage;->mControllers:Landroid/util/ArrayMap;

    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v1

    invoke-virtual {v0, v1, p1}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    return-void
.end method

.method public static setClassInStorage(Ljava/lang/Object;)V
    .registers 2

    const-class v0, Lcom/miui/systemui/SettingsManager;

    invoke-static {v0}, Lcom/miui/systemui/MiuiDependency;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/miui/systemui/SettingsManager;

    check-cast v0, Lcom/miui/systemui/SettingsManager;

    iget-object v0, v0, Lcom/miui/systemui/SettingsManager;->context:Landroid/content/Context;

    invoke-static {v0, p0}, Lcom/android/systemui/plugins/ControllerStorage;->setClassInStorage(Landroid/content/Context;Ljava/lang/Object;)V

    return-void
.end method

.method public static setInstance(Lcom/android/systemui/plugins/ControllerStorage;)V
    .registers 1

    sput-object p0, Lcom/android/systemui/plugins/ControllerStorage;->sControllerStorage:Lcom/android/systemui/plugins/ControllerStorage;

    return-void
.end method


# virtual methods
.method public createControllerStorage(Ljava/lang/Object;)Ljava/lang/Object;
    .registers 8
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Ljava/lang/Object;",
            ">(",
            "Ljava/lang/Object;",
            ")TT;"
        }
    .end annotation

    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/NoSuchMethodException;,
            Ljava/lang/IllegalAccessException;,
            Ljava/lang/reflect/InvocationTargetException;,
            Ljava/lang/InstantiationException;
        }
    .end annotation

    const/4 v5, 0x1

    const/4 v4, 0x0

    instance-of v2, p1, Ljava/lang/Class;

    if-eqz v2, :cond_1e

    move-object v0, p1

    check-cast v0, Ljava/lang/Class;

    new-array v2, v5, [Ljava/lang/Class;

    const-class v3, Landroid/content/Context;

    aput-object v3, v2, v4

    invoke-virtual {v0, v2}, Ljava/lang/Class;->getConstructor([Ljava/lang/Class;)Ljava/lang/reflect/Constructor;

    move-result-object v1

    new-array v2, v5, [Ljava/lang/Object;

    iget-object v3, p0, Lcom/android/systemui/plugins/ControllerStorage;->context:Landroid/content/Context;

    aput-object v3, v2, v4

    invoke-virtual {v1, v2}, Ljava/lang/reflect/Constructor;->newInstance([Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v2

    return-object v2

    :cond_1e
    new-instance v2, Ljava/lang/IllegalArgumentException;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "Unsupported ControllerStorage "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    throw v2
.end method

.method public final destroyControllerStorage(Ljava/lang/Class;Ljava/util/function/Consumer;)V
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Ljava/lang/Object;",
            ">(",
            "Ljava/lang/Class",
            "<TT;>;",
            "Ljava/util/function/Consumer",
            "<TT;>;)V"
        }
    .end annotation

    iget-object v1, p0, Lcom/android/systemui/plugins/ControllerStorage;->mControllers:Landroid/util/ArrayMap;

    invoke-virtual {v1, p1}, Landroid/util/ArrayMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    if-eqz v0, :cond_d

    if-eqz p2, :cond_d

    invoke-interface {p2, v0}, Ljava/util/function/Consumer;->accept(Ljava/lang/Object;)V

    :cond_d
    return-void
.end method

.method public final getControllerStorage(Lcom/android/systemui/plugins/ControllerStorage$ControllerStorageKey;)Ljava/lang/Object;
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Ljava/lang/Object;",
            ">(",
            "Lcom/android/systemui/plugins/ControllerStorage$ControllerStorageKey",
            "<TT;>;)TT;"
        }
    .end annotation

    invoke-virtual {p0, p1}, Lcom/android/systemui/plugins/ControllerStorage;->getControllerStorageInner(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    return-object v0
.end method

.method public final getControllerStorage(Ljava/lang/Class;)Ljava/lang/Object;
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Ljava/lang/Object;",
            ">(",
            "Ljava/lang/Class",
            "<TT;>;)TT;"
        }
    .end annotation

    invoke-virtual {p0, p1}, Lcom/android/systemui/plugins/ControllerStorage;->getControllerStorageInner(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    return-object v0
.end method

.method public final declared-synchronized getControllerStorageInner(Ljava/lang/Object;)Ljava/lang/Object;
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Ljava/lang/Object;",
            ">(",
            "Ljava/lang/Object;",
            ")TT;"
        }
    .end annotation

    monitor-enter p0

    :try_start_1
    iget-object v1, p0, Lcom/android/systemui/plugins/ControllerStorage;->mControllers:Landroid/util/ArrayMap;

    invoke-virtual {v1, p1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;
    :try_end_6
    .catchall {:try_start_1 .. :try_end_6} :catchall_14

    move-result-object v0

    if-nez v0, :cond_12

    :try_start_9
    invoke-virtual {p0, p1}, Lcom/android/systemui/plugins/ControllerStorage;->createControllerStorage(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/plugins/ControllerStorage;->mControllers:Landroid/util/ArrayMap;

    invoke-virtual {v1, p1, v0}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    :try_end_12
    .catch Ljava/lang/Exception; {:try_start_9 .. :try_end_12} :catch_17
    .catchall {:try_start_9 .. :try_end_12} :catchall_14

    :cond_12
    :goto_12
    monitor-exit p0

    return-object v0

    :catchall_14
    move-exception v1

    monitor-exit p0

    throw v1

    :catch_17
    move-exception v1

    goto :goto_12
.end method

.method public start()V
    .registers 2

    const-class v0, Lcom/android/systemui/statusbar/policy/DefaultFirstSettings;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_plugins_ControllerStorage',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
