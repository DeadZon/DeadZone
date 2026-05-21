TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/CrashAnalysis.smali'
CLASS_FALLBACK_NAMES = ['CrashAnalysis.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_CrashAnalysis__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/CrashAnalysis;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;
    }
.end annotation


# static fields
.field private static volatile s:Lcom/xiaomi/onetrack/CrashAnalysis;


# instance fields
.field private final q:[Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;

.field private final r:Lcom/xiaomi/onetrack/api/m;

.field private t:Z


# direct methods
.method private constructor <init>(Landroid/content/Context;Lcom/xiaomi/onetrack/api/m;)V
    .registers 11

    const-string v0, "CrashAnalysis"

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    :try_start_0
    const-string v1, "xcrash.XCrash$InitParameters"

    invoke-static {v1}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v1

    const/4 v2, 0x0

    new-array v3, v2, [Ljava/lang/Class;

    const/4 v3, 0x0

    invoke-virtual {v1, v3}, Ljava/lang/Class;->getConstructor([Ljava/lang/Class;)Ljava/lang/reflect/Constructor;

    move-result-object v1

    invoke-virtual {v1, v3}, Ljava/lang/reflect/Constructor;->newInstance([Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    const-string v4, "setNativeDumpAllThreads"

    sget-object v5, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;

    invoke-direct {p0, v1, v4, v5}, Lcom/xiaomi/onetrack/CrashAnalysis;->a(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/Object;)V

    const-string v4, "setLogDir"

    invoke-static {}, Lcom/xiaomi/onetrack/CrashAnalysis;->getCrashPath()Ljava/lang/String;

    move-result-object v6

    invoke-direct {p0, v1, v4, v6}, Lcom/xiaomi/onetrack/CrashAnalysis;->a(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/Object;)V

    const-string v4, "setNativeDumpMap"

    invoke-direct {p0, v1, v4, v5}, Lcom/xiaomi/onetrack/CrashAnalysis;->a(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/Object;)V

    const-string v4, "setNativeDumpFds"

    invoke-direct {p0, v1, v4, v5}, Lcom/xiaomi/onetrack/CrashAnalysis;->a(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/Object;)V

    const-string v4, "setJavaDumpAllThreads"

    invoke-direct {p0, v1, v4, v5}, Lcom/xiaomi/onetrack/CrashAnalysis;->a(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/Object;)V

    const-string v4, "xcrash.XCrash"

    invoke-static {v4}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v4

    const-string v5, "init"

    const/4 v6, 0x2

    new-array v6, v6, [Ljava/lang/Class;

    const-class v7, Landroid/content/Context;

    aput-object v7, v6, v2

    invoke-virtual {v1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v2

    const/4 v7, 0x1

    aput-object v2, v6, v7

    invoke-virtual {v4, v5, v6}, Ljava/lang/Class;->getDeclaredMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v2

    invoke-virtual {p1}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;

    move-result-object p1

    filled-new-array {p1, v1}, [Ljava/lang/Object;

    move-result-object p1

    invoke-virtual {v2, v3, p1}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    const-string p1, "XCrash init success"

    invoke-static {v0, p1}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    iput-boolean v7, p0, Lcom/xiaomi/onetrack/CrashAnalysis;->t:Z
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_0

    :catchall_0
    move-exception p1

    const-string v1, "XCrash init failed: "

    invoke-static {v0, v1, p1}, Lcom/xiaomi/onetrack/util/p;->c(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V

    :goto_0
    iput-object p2, p0, Lcom/xiaomi/onetrack/CrashAnalysis;->r:Lcom/xiaomi/onetrack/api/m;

    new-instance p1, Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;

    const-string p2, "java"

    invoke-direct {p1, p0, p2}, Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;-><init>(Lcom/xiaomi/onetrack/CrashAnalysis;Ljava/lang/String;)V

    new-instance p2, Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;

    const-string v0, "anr"

    invoke-direct {p2, p0, v0}, Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;-><init>(Lcom/xiaomi/onetrack/CrashAnalysis;Ljava/lang/String;)V

    new-instance v0, Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;

    const-string v1, "native"

    invoke-direct {v0, p0, v1}, Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;-><init>(Lcom/xiaomi/onetrack/CrashAnalysis;Ljava/lang/String;)V

    filled-new-array {p1, p2, v0}, [Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;

    move-result-object p1

    iput-object p1, p0, Lcom/xiaomi/onetrack/CrashAnalysis;->q:[Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;

    return-void
.end method

.method private a()J
    .registers 12

    invoke-static {}, Lcom/xiaomi/onetrack/util/aa;->c()J

    move-result-wide v0

    const-wide/16 v2, 0x0

    cmp-long p0, v0, v2

    const-wide/16 v2, 0xa

    const-string v4, "CrashAnalysis"

    if-nez p0, :cond_0

    const-string p0, "no ticket data found, return max count"

    invoke-static {v4, p0}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    return-wide v2

    :cond_0
    invoke-static {}, Lcom/xiaomi/onetrack/util/ac;->b()J

    move-result-wide v5

    const-wide/16 v7, 0x64

    div-long v9, v0, v7

    cmp-long p0, v9, v5

    if-eqz p0, :cond_1

    const-string p0, "no today\'s ticket, return max count"

    invoke-static {v4, p0}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    return-wide v2

    :cond_1
    mul-long/2addr v5, v7

    sub-long/2addr v0, v5

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "today\'s remain ticket is "

    invoke-virtual {p0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0, v0, v1}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-static {v4, p0}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    return-wide v0
.end method

.method static synthetic a(Ljava/lang/String;)J
    .registers 3

    invoke-static {p0}, Lcom/xiaomi/onetrack/CrashAnalysis;->d(Ljava/lang/String;)J

    move-result-wide v0

    return-wide v0
.end method

.method static synthetic a(Lcom/xiaomi/onetrack/CrashAnalysis;)Lcom/xiaomi/onetrack/api/m;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/CrashAnalysis;->r:Lcom/xiaomi/onetrack/api/m;

    return-object p0
.end method

.method static synthetic a(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .registers 2

    invoke-static {p0, p1}, Lcom/xiaomi/onetrack/CrashAnalysis;->d(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method

.method private a(J)V
    .registers 7

    invoke-static {}, Lcom/xiaomi/onetrack/util/ac;->b()J

    move-result-wide v0

    const-wide/16 v2, 0x64

    mul-long/2addr v0, v2

    add-long/2addr v0, p1

    invoke-static {v0, v1}, Lcom/xiaomi/onetrack/util/aa;->d(J)V

    return-void
.end method

.method private a(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/Object;)V
    .registers 7

    invoke-virtual {p3}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p0

    const-class v0, Ljava/lang/Boolean;

    if-ne p0, v0, :cond_0

    sget-object p0, Ljava/lang/Boolean;->TYPE:Ljava/lang/Class;

    goto :goto_0

    :cond_0
    invoke-virtual {p3}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p0

    :goto_0
    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    const/4 v1, 0x1

    new-array v1, v1, [Ljava/lang/Class;

    const/4 v2, 0x0

    aput-object p0, v1, v2

    invoke-virtual {v0, p2, v1}, Ljava/lang/Class;->getDeclaredMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object p0

    filled-new-array {p3}, [Ljava/lang/Object;

    move-result-object p2

    invoke-virtual {p0, p1, p2}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    return-void
.end method

.method static synthetic b(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .registers 2

    invoke-static {p0, p1}, Lcom/xiaomi/onetrack/CrashAnalysis;->c(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method

.method private b()Ljava/util/List;
    .registers 5

    new-instance v0, Ljava/io/File;

    invoke-static {}, Lcom/xiaomi/onetrack/CrashAnalysis;->getCrashPath()Ljava/lang/String;

    move-result-object v1

    invoke-direct {v0, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    invoke-virtual {v0}, Ljava/io/File;->listFiles()[Ljava/io/File;

    move-result-object v0

    if-nez v0, :cond_0

    const-string p0, "CrashAnalysis"

    const-string v0, "this path does not denote a directory, or if an I/O error occurs."

    invoke-static {p0, v0}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    const/4 p0, 0x0

    return-object p0

    :cond_0
    invoke-static {v0}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v0

    new-instance v1, Lcom/xiaomi/onetrack/CrashAnalysis$1;

    invoke-direct {v1, p0}, Lcom/xiaomi/onetrack/CrashAnalysis$1;-><init>(Lcom/xiaomi/onetrack/CrashAnalysis;)V

    invoke-static {v0, v1}, Ljava/util/Collections;->sort(Ljava/util/List;Ljava/util/Comparator;)V

    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result p0

    const/16 v1, 0x14

    if-le p0, v1, :cond_2

    add-int/lit8 v1, p0, -0x14

    const/4 v2, 0x0

    :goto_0
    if-ge v2, v1, :cond_1

    invoke-interface {v0, v2}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Ljava/io/File;

    invoke-static {v3}, Lcom/xiaomi/onetrack/util/k;->a(Ljava/io/File;)V

    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :cond_1
    invoke-interface {v0, v1, p0}, Ljava/util/List;->subList(II)Ljava/util/List;

    move-result-object p0

    return-object p0

    :cond_2
    return-object v0
.end method

.method static synthetic b(Ljava/lang/String;)Ljava/util/Map;
    .registers 1

    invoke-static {p0}, Lcom/xiaomi/onetrack/CrashAnalysis;->c(Ljava/lang/String;)Ljava/util/Map;

    move-result-object p0

    return-object p0
.end method

.method private static c(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .registers 5

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_2

    :try_start_0
    const-string v0, "anr"

    invoke-virtual {p1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    const/4 v1, -0x1

    if-eqz v0, :cond_0

    const-string p1, " tid=1 "

    invoke-virtual {p0, p1}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result p1

    if-eq p1, v1, :cond_2

    const-string v0, "\n  at "

    invoke-virtual {p0, v0, p1}, Ljava/lang/String;->indexOf(Ljava/lang/String;I)I

    move-result p1

    if-eq p1, v1, :cond_2

    add-int/lit8 v0, p1, 0x6

    const/16 v2, 0xa

    invoke-virtual {p0, v2, v0}, Ljava/lang/String;->indexOf(II)I

    move-result v0

    if-eq v0, v1, :cond_2

    add-int/lit8 p1, p1, 0x2

    invoke-virtual {p0, p1, v0}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :cond_0
    const-string v0, "error reason:\n\t"

    invoke-virtual {p0, v0}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v0

    if-eq v0, v1, :cond_1

    add-int/lit8 v0, v0, 0xf

    const-string p1, "\n\n"

    invoke-virtual {p0, p1, v0}, Ljava/lang/String;->indexOf(Ljava/lang/String;I)I

    move-result p1

    if-eq p1, v1, :cond_2

    invoke-virtual {p0, v0, p1}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :cond_1
    const-string v0, "native"

    invoke-virtual {p1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_2

    invoke-static {p0}, Lcom/xiaomi/onetrack/util/b;->b(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    if-nez p1, :cond_2

    return-object p0

    :catch_0
    move-exception p0

    new-instance p1, Ljava/lang/StringBuilder;

    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "getErrorReasonString error: "

    invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/Exception;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string p1, "CrashAnalysis"

    invoke-static {p1, p0}, Lcom/xiaomi/onetrack/util/p;->b(Ljava/lang/String;Ljava/lang/String;)V

    :cond_2
    const-string p0, "uncategoried"

    return-object p0
.end method

.method private static c(Ljava/lang/String;)Ljava/util/Map;
    .registers 5

    new-instance v0, Ljava/util/HashMap;

    invoke-direct {v0}, Ljava/util/HashMap;-><init>()V

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_0

    :try_start_0
    new-instance v1, Lorg/json/JSONObject;

    const/4 v2, 0x1

    invoke-virtual {p0, v2}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object p0

    invoke-direct {v1, p0}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V

    invoke-virtual {v1}, Lorg/json/JSONObject;->keys()Ljava/util/Iterator;

    move-result-object p0

    :goto_0
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_0

    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Ljava/lang/String;

    invoke-virtual {v1, v2}, Lorg/json/JSONObject;->opt(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v3

    invoke-interface {v0, v2, v3}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception p0

    const-string v1, "CrashAnalysis"

    const-string v2, "getDynamicCommonProperty error："

    invoke-static {v1, v2, p0}, Lcom/xiaomi/onetrack/util/p;->b(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V

    :cond_0
    return-object v0
.end method

.method private c()Z
    .registers 26

    move-object/from16 v0, p0

    invoke-direct {v0}, Lcom/xiaomi/onetrack/CrashAnalysis;->b()Ljava/util/List;

    move-result-object v1

    invoke-direct {v0}, Lcom/xiaomi/onetrack/CrashAnalysis;->a()J

    move-result-wide v2

    if-eqz v1, :cond_9

    invoke-interface {v1}, Ljava/util/List;->size()I

    move-result v5

    if-lez v5, :cond_9

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v5

    invoke-static {}, Lcom/xiaomi/onetrack/util/aa;->b()J

    move-result-wide v7

    cmp-long v9, v7, v5

    const-wide/32 v10, 0x240c8400

    if-lez v9, :cond_0

    sub-long v7, v5, v10

    :cond_0
    invoke-interface {v1}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object v1

    const-wide/16 v12, 0x0

    move-wide v14, v12

    const/4 v9, 0x0

    :goto_0
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v16

    if-eqz v16, :cond_7

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v16

    move-object/from16 v4, v16

    check-cast v4, Ljava/io/File;

    invoke-virtual {v4}, Ljava/io/File;->lastModified()J

    move-result-wide v17

    sub-long v19, v5, v10

    cmp-long v16, v17, v19

    const-string v10, "CrashAnalysis"

    if-ltz v16, :cond_1

    cmp-long v11, v17, v5

    if-lez v11, :cond_2

    :cond_1
    move-object/from16 v16, v1

    move-wide/from16 v21, v12

    goto :goto_3

    :cond_2
    cmp-long v11, v17, v7

    if-gtz v11, :cond_3

    const-string v4, "found already reported crash file, ignore"

    invoke-static {v10, v4}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    move-object/from16 v16, v1

    move-wide/from16 v21, v12

    goto :goto_2

    :cond_3
    cmp-long v11, v2, v12

    if-lez v11, :cond_5

    iget-object v11, v0, Lcom/xiaomi/onetrack/CrashAnalysis;->q:[Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;

    move-wide/from16 v21, v12

    array-length v12, v11

    const/4 v13, 0x0

    :goto_1
    move-object/from16 v16, v1

    if-ge v13, v12, :cond_6

    aget-object v1, v11, v13

    invoke-virtual {v1, v4}, Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;->a(Ljava/io/File;)Z

    move-result v1

    if-eqz v1, :cond_4

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v9, "find crash file:"

    invoke-virtual {v1, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/io/File;->getName()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v1, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v10, v1}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    const-wide/16 v23, 0x1

    sub-long v2, v2, v23

    cmp-long v1, v14, v17

    const/4 v9, 0x1

    if-gez v1, :cond_4

    move-wide/from16 v14, v17

    :cond_4
    add-int/lit8 v13, v13, 0x1

    move-object/from16 v1, v16

    goto :goto_1

    :cond_5
    move-wide/from16 v21, v12

    move-object/from16 v16, v1

    :cond_6
    :goto_2
    move-object/from16 v1, v16

    move-wide/from16 v12, v21

    const-wide/32 v10, 0x240c8400

    goto :goto_0

    :goto_3
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v11, "remove obsolete crash files: "

    invoke-virtual {v1, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/io/File;->getName()Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v1, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v10, v1}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    invoke-static {v4}, Lcom/xiaomi/onetrack/util/k;->a(Ljava/io/File;)V

    goto :goto_2

    :cond_7
    move-wide/from16 v21, v12

    cmp-long v1, v14, v21

    if-lez v1, :cond_8

    invoke-static {v14, v15}, Lcom/xiaomi/onetrack/util/aa;->c(J)V

    :cond_8
    move v4, v9

    goto :goto_4

    :cond_9
    const/4 v4, 0x0

    :goto_4
    if-eqz v4, :cond_a

    invoke-direct {v0, v2, v3}, Lcom/xiaomi/onetrack/CrashAnalysis;->a(J)V

    :cond_a
    return v4
.end method

.method public static calculateJavaDigest(Ljava/lang/String;)Ljava/lang/String;
    .registers 9

    const-string v0, "\\t"

    const-string v1, ""

    invoke-virtual {p0, v0, v1}, Ljava/lang/String;->replaceAll(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    const-string v0, "\\n"

    invoke-virtual {p0, v0}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object p0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    array-length v2, p0

    const/16 v3, 0x14

    invoke-static {v2, v3}, Ljava/lang/Math;->min(II)I

    move-result v2

    const/4 v3, 0x0

    move v4, v3

    :goto_0
    if-ge v4, v2, :cond_0

    aget-object v5, p0, v4

    const-string v6, "((java:)|(length=)|(index=)|(Index:)|(Size:))\\d+"

    const-string v7, "$1XX"

    invoke-virtual {v5, v6, v7}, Ljava/lang/String;->replaceAll(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v5

    const-string v6, "\\$[0-9a-fA-F]{1,10}@[0-9a-fA-F]{1,10}|@[0-9a-fA-F]{1,10}|0x[0-9a-fA-F]{1,10}"

    const-string v7, "XX"

    invoke-virtual {v5, v6, v7}, Ljava/lang/String;->replaceAll(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v5

    const-string v6, "\\d+[B,KB,MB]*"

    invoke-virtual {v5, v6, v1}, Ljava/lang/String;->replaceAll(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v5

    aput-object v5, p0, v4

    add-int/lit8 v4, v4, 0x1

    goto :goto_0

    :cond_0
    :goto_1
    if-ge v3, v2, :cond_2

    aget-object v1, p0, v3

    const-string v4, "..."

    invoke-virtual {v1, v4}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_1

    aget-object v1, p0, v3

    const-string v4, "more"

    invoke-virtual {v1, v4}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_1

    goto :goto_2

    :cond_1
    aget-object v1, p0, v3

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/16 v1, 0xa

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    add-int/lit8 v3, v3, 0x1

    goto :goto_1

    :cond_2
    :goto_2
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Lcom/xiaomi/onetrack/d/d;->h(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method

.method private static d(Ljava/lang/String;)J
    .registers 4

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_0

    :try_start_0
    const-string v0, "Crash time: \'"

    invoke-virtual {p0, v0}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v0

    const/4 v1, -0x1

    if-eq v0, v1, :cond_0

    add-int/lit8 v0, v0, 0xd

    const-string v2, "\'\n"

    invoke-virtual {p0, v2, v0}, Ljava/lang/String;->indexOf(Ljava/lang/String;I)I

    move-result v2

    if-eq v2, v1, :cond_0

    invoke-virtual {p0, v0, v2}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Lcom/xiaomi/onetrack/util/b;->a(Ljava/lang/String;)J

    move-result-wide v0
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return-wide v0

    :catch_0
    move-exception p0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "getCrashTimeStamp error: "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/Exception;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string v0, "CrashAnalysis"

    invoke-static {v0, p0}, Lcom/xiaomi/onetrack/util/p;->b(Ljava/lang/String;Ljava/lang/String;)V

    :cond_0
    const-wide/16 v0, 0x0

    return-wide v0
.end method

.method private static d(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .registers 4

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_1

    :try_start_0
    const-string v0, "anr"

    invoke-virtual {p1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result p1
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    const-string v0, "\n\n"

    const/4 v1, -0x1

    if-eqz p1, :cond_0

    :try_start_1
    const-string p1, " tid=1 "

    invoke-virtual {p0, p1}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result p1

    if-eq p1, v1, :cond_1

    invoke-virtual {p0, v0, p1}, Ljava/lang/String;->indexOf(Ljava/lang/String;I)I

    move-result v0

    if-eq v0, v1, :cond_1

    invoke-virtual {p0, p1, v0}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Lcom/xiaomi/onetrack/CrashAnalysis;->calculateJavaDigest(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :cond_0
    const-string p1, "backtrace feature id:\n\t"

    invoke-virtual {p0, p1}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result p1

    if-eq p1, v1, :cond_1

    add-int/lit8 p1, p1, 0x17

    invoke-virtual {p0, v0, p1}, Ljava/lang/String;->indexOf(Ljava/lang/String;I)I

    move-result v0

    if-eq v0, v1, :cond_1

    invoke-virtual {p0, p1, v0}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object p0
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_0

    return-object p0

    :catch_0
    move-exception p0

    new-instance p1, Ljava/lang/StringBuilder;

    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "calculateFeatureId error: "

    invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/Exception;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string p1, "CrashAnalysis"

    invoke-static {p1, p0}, Lcom/xiaomi/onetrack/util/p;->b(Ljava/lang/String;Ljava/lang/String;)V

    :cond_1
    const-string p0, ""

    return-object p0
.end method

.method private d()V
    .registers 4

    iget-object p0, p0, Lcom/xiaomi/onetrack/CrashAnalysis;->q:[Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;

    array-length v0, p0

    const/4 v1, 0x0

    :goto_0
    if-ge v1, v0, :cond_0

    aget-object v2, p0, v1

    invoke-virtual {v2}, Lcom/xiaomi/onetrack/CrashAnalysis$FileProcessor;->a()V

    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    :cond_0
    return-void
.end method

.method public static getCrashPath()Ljava/lang/String;
    .registers 1

    invoke-static {}, Lcom/xiaomi/onetrack/util/k;->a()Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method

.method public static getInstance()Lcom/xiaomi/onetrack/CrashAnalysis;
    .registers 2

    sget-object v0, Lcom/xiaomi/onetrack/CrashAnalysis;->s:Lcom/xiaomi/onetrack/CrashAnalysis;

    if-nez v0, :cond_0

    const-string v0, "CrashAnalysis"

    const-string v1, "CrashAnalysis.init should be called before"

    invoke-static {v0, v1}, Lcom/xiaomi/onetrack/util/p;->b(Ljava/lang/String;Ljava/lang/String;)V

    :cond_0
    sget-object v0, Lcom/xiaomi/onetrack/CrashAnalysis;->s:Lcom/xiaomi/onetrack/CrashAnalysis;

    return-object v0
.end method

.method public static init(Landroid/content/Context;Lcom/xiaomi/onetrack/api/m;)Lcom/xiaomi/onetrack/CrashAnalysis;
    .registers 4

    sget-object v0, Lcom/xiaomi/onetrack/CrashAnalysis;->s:Lcom/xiaomi/onetrack/CrashAnalysis;

    if-nez v0, :cond_1

    const-class v0, Lcom/xiaomi/onetrack/CrashAnalysis;

    monitor-enter v0

    :try_start_0
    sget-object v1, Lcom/xiaomi/onetrack/CrashAnalysis;->s:Lcom/xiaomi/onetrack/CrashAnalysis;

    if-nez v1, :cond_0

    new-instance v1, Lcom/xiaomi/onetrack/CrashAnalysis;

    invoke-direct {v1, p0, p1}, Lcom/xiaomi/onetrack/CrashAnalysis;-><init>(Landroid/content/Context;Lcom/xiaomi/onetrack/api/m;)V

    sput-object v1, Lcom/xiaomi/onetrack/CrashAnalysis;->s:Lcom/xiaomi/onetrack/CrashAnalysis;

    goto :goto_0

    :catchall_0
    move-exception p0

    goto :goto_1

    :cond_0
    :goto_0
    monitor-exit v0

    goto :goto_2

    :goto_1
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw p0

    :cond_1
    :goto_2
    sget-object p0, Lcom/xiaomi/onetrack/CrashAnalysis;->s:Lcom/xiaomi/onetrack/CrashAnalysis;

    return-object p0
.end method


# virtual methods
.method public isSupport()Z
    .registers 1

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/CrashAnalysis;->t:Z

    return p0
.end method

.method public start()V
    .registers 3

    const-string v0, "CrashAnalysis"

    :try_start_0
    invoke-direct {p0}, Lcom/xiaomi/onetrack/CrashAnalysis;->c()Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-direct {p0}, Lcom/xiaomi/onetrack/CrashAnalysis;->d()V

    return-void

    :catchall_0
    move-exception p0

    goto :goto_0

    :cond_0
    const-string p0, "no crash file found"

    invoke-static {v0, p0}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-void

    :goto_0
    const-string v1, "processCrash error: "

    invoke-static {v0, v1, p0}, Lcom/xiaomi/onetrack/util/p;->b(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
