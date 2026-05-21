TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/e/a.smali'
CLASS_FALLBACK_NAMES = ['a.smali']
CLASS_ANCHORS = ['.super Lcom/xiaomi/onetrack/f/b;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_e_a__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/e/a;
.super Lcom/xiaomi/onetrack/f/b;


# direct methods
.method public constructor <init>(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
    .registers 7

    invoke-direct {p0}, Lcom/xiaomi/onetrack/f/b;-><init>()V

    :try_start_0
    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/f/b;->a(Ljava/lang/String;)V

    invoke-virtual {p0, p3}, Lcom/xiaomi/onetrack/f/b;->c(Ljava/lang/String;)V

    invoke-virtual {p0, p2}, Lcom/xiaomi/onetrack/f/b;->b(Ljava/lang/String;)V

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v0

    invoke-virtual {p0, v0, v1}, Lcom/xiaomi/onetrack/f/b;->b(J)V

    new-instance p2, Lorg/json/JSONObject;

    invoke-direct {p2, p4}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V

    invoke-virtual {p0, p2}, Lcom/xiaomi/onetrack/f/b;->b(Lorg/json/JSONObject;)V

    invoke-static {}, Lcom/xiaomi/onetrack/b/h;->a()Lcom/xiaomi/onetrack/b/h;

    move-result-object p2

    const-string p4, "level"

    const/4 v0, 0x1

    invoke-virtual {p2, p1, p3, p4, v0}, Lcom/xiaomi/onetrack/b/h;->a(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;I)I

    move-result p1

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/f/b;->a(I)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return-void

    :catch_0
    move-exception p0

    new-instance p1, Ljava/lang/StringBuilder;

    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    const-string p2, "CustomEvent error:"

    invoke-virtual {p1, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/Exception;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string p1, "CustomEvent"

    invoke-static {p1, p0}, Lcom/xiaomi/onetrack/util/p;->b(Ljava/lang/String;Ljava/lang/String;)V

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
