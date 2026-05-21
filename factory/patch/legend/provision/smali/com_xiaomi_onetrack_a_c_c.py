TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/a/c/c.smali'
CLASS_FALLBACK_NAMES = ['c.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_a_c_c__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/a/c/c;
.super Ljava/lang/Object;


# direct methods
.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static a()V
    .registers 11

    const-string v0, "AdMonitorUploader"

    :try_start_0
    invoke-static {}, Lcom/xiaomi/onetrack/a/c/c;->b()Z

    move-result v1

    if-nez v1, :cond_0

    goto :goto_3

    :cond_0
    const-string v1, "即将读取数据库并上传数据"

    invoke-static {v0, v1}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    const/4 v1, 0x0

    move v2, v1

    :cond_1
    const/16 v3, 0x14

    if-le v2, v3, :cond_2

    goto :goto_3

    :cond_2
    invoke-static {}, Lcom/xiaomi/onetrack/a/a;->a()Lcom/xiaomi/onetrack/a/a;

    move-result-object v3

    invoke-virtual {v3}, Lcom/xiaomi/onetrack/a/a;->d()V

    invoke-static {}, Lcom/xiaomi/onetrack/a/a;->a()Lcom/xiaomi/onetrack/a/a;

    move-result-object v3

    invoke-virtual {v3}, Lcom/xiaomi/onetrack/a/a;->b()Lcom/xiaomi/onetrack/a/c/a;

    move-result-object v3

    if-eqz v3, :cond_8

    iget-object v4, v3, Lcom/xiaomi/onetrack/a/c/a;->b:Ljava/util/ArrayList;

    if-eqz v4, :cond_8

    invoke-virtual {v4}, Ljava/util/ArrayList;->size()I

    move-result v4

    if-gtz v4, :cond_3

    goto :goto_1

    :cond_3
    new-instance v4, Ljava/util/ArrayList;

    invoke-direct {v4}, Ljava/util/ArrayList;-><init>()V

    new-instance v5, Ljava/util/ArrayList;

    invoke-direct {v5}, Ljava/util/ArrayList;-><init>()V

    iget-object v6, v3, Lcom/xiaomi/onetrack/a/c/a;->b:Ljava/util/ArrayList;

    invoke-virtual {v6}, Ljava/util/ArrayList;->size()I

    move-result v7

    move v8, v1

    :goto_0
    if-ge v8, v7, :cond_5

    invoke-virtual {v6, v8}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v9

    add-int/lit8 v8, v8, 0x1

    check-cast v9, Lcom/xiaomi/onetrack/a/b/a;

    invoke-virtual {v9}, Lcom/xiaomi/onetrack/a/b/a;->c()Ljava/lang/String;

    move-result-object v10

    invoke-static {v10}, Lcom/xiaomi/onetrack/g/b;->b(Ljava/lang/String;)Z

    move-result v10

    invoke-virtual {v9}, Lcom/xiaomi/onetrack/a/b/a;->b()I

    move-result v9

    if-eqz v10, :cond_4

    invoke-static {v9}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v9

    invoke-virtual {v4, v9}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_0

    :catchall_0
    move-exception v1

    goto :goto_2

    :cond_4
    invoke-static {v9}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v9

    invoke-virtual {v5, v9}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_0

    :cond_5
    invoke-virtual {v4}, Ljava/util/ArrayList;->size()I

    move-result v6

    if-lez v6, :cond_6

    invoke-static {}, Lcom/xiaomi/onetrack/a/a;->a()Lcom/xiaomi/onetrack/a/a;

    move-result-object v6

    invoke-virtual {v6, v4}, Lcom/xiaomi/onetrack/a/a;->a(Ljava/util/ArrayList;)I

    :cond_6
    invoke-virtual {v5}, Ljava/util/ArrayList;->size()I

    move-result v4

    if-lez v4, :cond_7

    invoke-static {}, Lcom/xiaomi/onetrack/a/a;->a()Lcom/xiaomi/onetrack/a/a;

    move-result-object v4

    invoke-virtual {v4, v5}, Lcom/xiaomi/onetrack/a/a;->b(Ljava/util/ArrayList;)V

    :cond_7
    add-int/lit8 v2, v2, 0x1

    iget-boolean v3, v3, Lcom/xiaomi/onetrack/a/c/a;->c:Z

    if-eqz v3, :cond_1

    const-string v1, "No more ad monitor records"

    invoke-static {v0, v1}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    return-void

    :cond_8
    :goto_1
    const-string v1, "满足条件的adMonitor记录为空，即将返回"

    invoke-static {v0, v1}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-void

    :goto_2
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "uploadData Throwable:"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/Throwable;->getMessage()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    :goto_3
    return-void
.end method

.method private static b()Z
    .registers 7

    const-string v0, "AdMonitorUploader"

    invoke-static {v0}, Lcom/xiaomi/onetrack/util/q;->a(Ljava/lang/String;)Z

    move-result v1

    const/4 v2, 0x0

    if-eqz v1, :cond_0

    const-string v1, "the device is not provisioned, stop poll!"

    invoke-static {v0, v1}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    return v2

    :cond_0
    invoke-static {}, Lcom/xiaomi/onetrack/g/c;->a()Z

    move-result v1

    if-nez v1, :cond_1

    const-string v1, "network is unconnected, stop poll!"

    invoke-static {v0, v1}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    return v2

    :cond_1
    invoke-static {}, Lcom/xiaomi/onetrack/a/a;->a()Lcom/xiaomi/onetrack/a/a;

    move-result-object v1

    invoke-virtual {v1}, Lcom/xiaomi/onetrack/a/a;->e()J

    move-result-wide v3

    const-wide/16 v5, 0x0

    cmp-long v1, v3, v5

    if-nez v1, :cond_2

    const-string v1, "no data remain in db, stop poll!"

    invoke-static {v0, v1}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    return v2

    :cond_2
    const/4 v0, 0x1

    return v0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
