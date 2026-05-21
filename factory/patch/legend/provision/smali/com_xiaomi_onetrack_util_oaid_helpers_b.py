TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/util/oaid/helpers/b.smali'
CLASS_FALLBACK_NAMES = ['b.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_util_oaid_helpers_b__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/util/oaid/helpers/b;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/xiaomi/onetrack/util/oaid/helpers/b$a;
    }
.end annotation


# static fields
.field static a:Ljava/lang/String; = "b"


# direct methods
.method static constructor <clinit>()V
    .registers 0

    return-void
.end method

.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method private static c()Ljava/lang/String;
    .registers 1

    sget-object v0, Landroid/os/Build;->MANUFACTURER:Ljava/lang/String;

    invoke-virtual {v0}, Ljava/lang/String;->toUpperCase()Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method


# virtual methods
.method public a(Landroid/content/Context;)Ljava/lang/String;
    .registers 3

    :try_start_0
    invoke-static {}, Lcom/xiaomi/onetrack/util/oaid/helpers/b;->c()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p0, p1, v0}, Lcom/xiaomi/onetrack/util/oaid/helpers/b;->a(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return-object p0

    :catch_0
    move-exception p0

    sget-object p1, Lcom/xiaomi/onetrack/util/oaid/helpers/b;->a:Ljava/lang/String;

    invoke-virtual {p0}, Ljava/lang/Exception;->getMessage()Ljava/lang/String;

    move-result-object p0

    invoke-static {p1, p0}, Lcom/xiaomi/onetrack/util/p;->a(Ljava/lang/String;Ljava/lang/String;)V

    const-string p0, ""

    return-object p0
.end method

.method a(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    .registers 5

    invoke-static {p2}, Lcom/xiaomi/onetrack/util/oaid/helpers/b$a;->b(Ljava/lang/String;)Lcom/xiaomi/onetrack/util/oaid/helpers/b$a;

    move-result-object v0

    invoke-virtual {p0}, Lcom/xiaomi/onetrack/util/oaid/helpers/b;->a()Z

    move-result v1

    if-eqz v1, :cond_0

    sget-object v0, Lcom/xiaomi/onetrack/util/oaid/helpers/b$a;->o:Lcom/xiaomi/onetrack/util/oaid/helpers/b$a;

    :cond_0
    invoke-virtual {p0}, Lcom/xiaomi/onetrack/util/oaid/helpers/b;->b()Z

    move-result p0

    if-eqz p0, :cond_1

    sget-object v0, Lcom/xiaomi/onetrack/util/oaid/helpers/b$a;->p:Lcom/xiaomi/onetrack/util/oaid/helpers/b$a;

    :cond_1
    if-eqz v0, :cond_2

    sget-object p0, Lcom/xiaomi/onetrack/util/oaid/helpers/c;->a:[I

    invoke-virtual {v0}, Ljava/lang/Enum;->ordinal()I

    move-result p2

    aget p0, p0, p2

    packed-switch p0, :pswitch_data_0

    const-string p0, ""

    return-object p0

    :pswitch_0  #0xe, 0xf, 0x10
    new-instance p0, Lcom/xiaomi/onetrack/util/oaid/helpers/m;

    invoke-direct {p0}, Lcom/xiaomi/onetrack/util/oaid/helpers/m;-><init>()V

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/util/oaid/helpers/m;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :pswitch_1  #0xd
    new-instance p0, Lcom/xiaomi/onetrack/util/oaid/helpers/i;

    invoke-direct {p0}, Lcom/xiaomi/onetrack/util/oaid/helpers/i;-><init>()V

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/util/oaid/helpers/i;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :pswitch_2  #0xa, 0xb, 0xc
    invoke-static {p1}, Lcom/xiaomi/onetrack/util/n;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :pswitch_3  #0x9
    new-instance p0, Lcom/xiaomi/onetrack/util/oaid/helpers/l;

    invoke-direct {p0}, Lcom/xiaomi/onetrack/util/oaid/helpers/l;-><init>()V

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/util/oaid/helpers/l;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :pswitch_4  #0x8
    new-instance p0, Lcom/xiaomi/onetrack/util/oaid/helpers/h;

    invoke-direct {p0}, Lcom/xiaomi/onetrack/util/oaid/helpers/h;-><init>()V

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/util/oaid/helpers/h;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x7
    new-instance p0, Lcom/xiaomi/onetrack/util/oaid/helpers/k;

    invoke-direct {p0}, Lcom/xiaomi/onetrack/util/oaid/helpers/k;-><init>()V

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/util/oaid/helpers/k;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :pswitch_6  #0x6
    new-instance p0, Lcom/xiaomi/onetrack/util/oaid/helpers/j;

    invoke-direct {p0}, Lcom/xiaomi/onetrack/util/oaid/helpers/j;-><init>()V

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/util/oaid/helpers/j;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :pswitch_7  #0x5
    new-instance p0, Lcom/xiaomi/onetrack/util/oaid/helpers/f;

    invoke-direct {p0}, Lcom/xiaomi/onetrack/util/oaid/helpers/f;-><init>()V

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/util/oaid/helpers/f;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :pswitch_8  #0x3, 0x4
    new-instance p0, Lcom/xiaomi/onetrack/util/oaid/helpers/e;

    invoke-direct {p0}, Lcom/xiaomi/onetrack/util/oaid/helpers/e;-><init>()V

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/util/oaid/helpers/e;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :pswitch_9  #0x2
    new-instance p0, Lcom/xiaomi/onetrack/util/oaid/helpers/d;

    invoke-direct {p0}, Lcom/xiaomi/onetrack/util/oaid/helpers/d;-><init>()V

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/util/oaid/helpers/d;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :pswitch_a  #0x1
    new-instance p0, Lcom/xiaomi/onetrack/util/oaid/helpers/a;

    invoke-direct {p0}, Lcom/xiaomi/onetrack/util/oaid/helpers/a;-><init>()V

    invoke-virtual {p0, p1}, Lcom/xiaomi/onetrack/util/oaid/helpers/a;->a(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :cond_2
    new-instance p0, Ljava/lang/Exception;

    const-string p1, "undefined oaid method of manufacturer %s"

    filled-new-array {p2}, [Ljava/lang/Object;

    move-result-object p2

    invoke-static {p1, p2}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p1

    invoke-direct {p0, p1}, Ljava/lang/Exception;-><init>(Ljava/lang/String;)V

    throw p0

    nop

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_a  #00000001
        :pswitch_9  #00000002
        :pswitch_8  #00000003
        :pswitch_8  #00000004
        :pswitch_7  #00000005
        :pswitch_6  #00000006
        :pswitch_5  #00000007
        :pswitch_4  #00000008
        :pswitch_3  #00000009
        :pswitch_2  #0000000a
        :pswitch_2  #0000000b
        :pswitch_2  #0000000c
        :pswitch_1  #0000000d
        :pswitch_0  #0000000e
        :pswitch_0  #0000000f
        :pswitch_0  #00000010
    .end packed-switch
.end method

.method public a()Z
    .registers 2

    const-string p0, "ro.build.freeme.label"

    invoke-static {p0}, Lcom/xiaomi/onetrack/util/ab;->a(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_0

    const-string v0, "FREEMEOS"

    invoke-virtual {p0, v0}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method

.method public b()Z
    .registers 2

    const-string p0, "ro.ssui.product"

    invoke-static {p0}, Lcom/xiaomi/onetrack/util/ab;->a(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_0

    const-string v0, "unknown"

    invoke-virtual {p0, v0}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result p0

    if-nez p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
