"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-framework.jar
Target class : mezo/xiaomi/util/Translator
Source MTCR  : miui-framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-framework.jar"
TARGET_CLASS = "mezo/xiaomi/util/Translator.smali"

PATCHES = [
    {
        "id":          "add_class_mezo_xiaomi_util_Translator",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public final Lmezo/xiaomi/util/Translator;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lmezo/xiaomi/util/Translator$SingletonHolder;,
        Lmezo/xiaomi/util/Translator$State;
    }
.end annotation


# static fields
.field private static final blacklist BUFFER_SIZE:I = 0x1000

.field private static final blacklist CHARSET:Ljava/lang/String; = "UTF-8"

.field private static final blacklist CLIENT_TYPE:Ljava/lang/String; = "at"

.field private static final blacklist CLIENT_VERSION:D = 1.0

.field private static final blacklist CONN_TIMEOUT:I = 0x4e20

.field private static final blacklist LANG_AUTO:Ljava/lang/String; = "auto"

.field private static final blacklist QUERY_MAX_LEN:I = 0x2710

.field private static final blacklist TAG:Ljava/lang/String; = "Translator"

.field private static final blacklist USER_AGENT:Ljava/lang/String;


# direct methods
.method static constructor blacklist <clinit>()V
    .registers 2

    new-instance v0, Ljava/lang/StringBuilder;

    const-string v1, "GoogleTranslate/5.22.0.RC04.206832067 {Linux; U; Android "

    invoke-direct {v0, v1}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    sget-object v1, Landroid/os/Build$VERSION;->RELEASE:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "; "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    sget-object v1, Landroid/os/Build;->MODEL:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, ")"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lmezo/xiaomi/util/Translator;->USER_AGENT:Ljava/lang/String;

    return-void
.end method

.method private constructor blacklist <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method synthetic constructor blacklist <init>(Lmezo/xiaomi/util/Translator-IA;)V
    .registers 2

    invoke-direct {p0}, Lmezo/xiaomi/util/Translator;-><init>()V

    return-void
.end method

.method public static whitelist getInstance()Lmezo/xiaomi/util/Translator;
    .registers 1

    invoke-static {}, Lmezo/xiaomi/util/Translator$SingletonHolder;->-$$Nest$sfgetINSTANCE()Lmezo/xiaomi/util/Translator;

    move-result-object v0

    return-object v0
.end method

.method private static blacklist toProperCase(Ljava/lang/String;)Ljava/lang/String;
    .registers 11

    if-nez p0, :cond_0

    const/4 p0, 0x0

    return-object p0

    :cond_0
    invoke-virtual {p0}, Ljava/lang/String;->length()I

    move-result v0

    if-nez v0, :cond_1

    return-object p0

    :cond_1
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const/4 v2, 0x0

    move v3, v2

    :goto_0
    if-ge v3, v0, :cond_3

    invoke-virtual {p0, v3}, Ljava/lang/String;->charAt(I)C

    move-result v4

    invoke-static {v4}, Ljava/lang/Character;->isAlphabetic(I)Z

    move-result v5

    if-eqz v5, :cond_2

    invoke-static {v4}, Ljava/lang/Character;->toUpperCase(C)C

    move-result v4

    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    add-int/lit8 v3, v3, 0x1

    goto :goto_1

    :cond_2
    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    add-int/lit8 v3, v3, 0x1

    goto :goto_0

    :cond_3
    :goto_1
    const/4 v4, 0x3

    new-array v5, v4, [C

    fill-array-data v5, :array_0

    move v6, v2

    :goto_2
    if-ge v3, v0, :cond_7

    invoke-virtual {p0, v3}, Ljava/lang/String;->charAt(I)C

    move-result v7

    if-eqz v6, :cond_4

    const/16 v8, 0x20

    if-eq v7, v8, :cond_4

    invoke-static {v7}, Ljava/lang/Character;->toUpperCase(C)C

    move-result v6

    invoke-virtual {v1, v6}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    move v6, v2

    goto :goto_3

    :cond_4
    invoke-virtual {v1, v7}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    :goto_3
    move v8, v2

    :goto_4
    if-ge v8, v4, :cond_6

    aget-char v9, v5, v8

    if-ne v7, v9, :cond_5

    const/4 v6, 0x1

    goto :goto_5

    :cond_5
    add-int/lit8 v8, v8, 0x1

    goto :goto_4

    :cond_6
    :goto_5
    add-int/lit8 v3, v3, 0x1

    goto :goto_2

    :cond_7
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    return-object p0

    nop

    :array_0
    .array-data 2
        0x2es
        0x3fs
        0x21s
    .end array-data
.end method


# virtual methods
.method public whitelist translate(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .registers 6

    invoke-static {p3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-eqz v0, :cond_0

    return-object p3

    :cond_0
    const/4 v0, 0x1

    new-array v0, v0, [Ljava/lang/String;

    const/4 v1, 0x0

    aput-object p3, v0, v1

    invoke-virtual {p0, p1, p2, v0}, Lmezo/xiaomi/util/Translator;->translate(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;)V

    aget-object p1, v0, v1

    return-object p1
.end method

.method blacklist translate(Ljava/lang/String;Ljava/lang/String;Lmezo/xiaomi/util/Translator$State;)V
    .registers 20
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/io/IOException;,
            Lorg/json/JSONException;
        }
    .end annotation

    goto :goto_19

    nop

    :goto_0
    new-instance v15, Ljava/io/ByteArrayOutputStream;

    goto :goto_d

    nop

    :goto_1
    move-object v1, v0

    :try_start_0
    invoke-virtual {v15}, Ljava/io/ByteArrayOutputStream;->close()V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_63

    nop

    :goto_2
    invoke-virtual {v12, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v12

    goto :goto_1e

    nop

    :goto_3
    check-cast v12, Ljava/lang/String;

    :goto_4
    goto :goto_4b

    nop

    :goto_5
    move-object v2, v0

    goto :goto_29

    nop

    :goto_6
    check-cast v14, Ljava/lang/String;

    goto :goto_a

    nop

    :goto_7
    invoke-interface {v0, v11}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v14

    goto :goto_6

    nop

    :goto_8
    if-lt v8, v1, :cond_0

    goto :goto_48

    :cond_0
    goto :goto_35

    nop

    :goto_9
    add-int/lit8 v10, v10, 0x1

    goto :goto_68

    nop

    :goto_a
    invoke-static {v14, v10}, Ljava/net/URLEncoder;->encode(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v14

    goto :goto_92

    nop

    :goto_b
    invoke-virtual {v12, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v12

    goto :goto_5a

    nop

    :goto_c
    add-int/lit8 v11, v9, 0x1

    goto :goto_56

    nop

    :goto_d
    invoke-direct {v15}, Ljava/io/ByteArrayOutputStream;-><init>()V

    :try_start_1
    new-instance v2, Ljava/io/BufferedInputStream;

    invoke-virtual {v9}, Ljava/net/HttpURLConnection;->getInputStream()Ljava/io/InputStream;

    move-result-object v9

    invoke-direct {v2, v9, v12}, Ljava/io/BufferedInputStream;-><init>(Ljava/io/InputStream;I)V
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_2

    :goto_e
    :try_start_2
    invoke-virtual {v2, v14}, Ljava/io/BufferedInputStream;->read([B)I

    move-result v9

    const/4 v12, -0x1

    if-eq v9, v12, :cond_1

    invoke-virtual {v15, v14, v7, v9}, Ljava/io/ByteArrayOutputStream;->write([BII)V

    goto :goto_e

    :cond_1
    invoke-virtual {v15, v10}, Ljava/io/ByteArrayOutputStream;->toString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v9
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    :try_start_3
    invoke-virtual {v2}, Ljava/io/BufferedInputStream;->close()V
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_2

    goto :goto_8c

    nop

    :goto_f
    add-int/lit8 v1, v1, 0x1

    :goto_10
    goto :goto_5c

    nop

    :goto_11
    const/16 v12, 0x4e20

    goto :goto_25

    nop

    :goto_12
    invoke-virtual {v12, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v12

    goto :goto_4e

    nop

    :goto_13
    move v10, v7

    :goto_14
    goto :goto_75

    nop

    :goto_15
    new-array v14, v12, [B

    goto :goto_0

    nop

    :goto_16
    add-int/lit8 v13, v9, 0x1

    goto :goto_94

    nop

    :goto_17
    return-void

    :goto_18
    goto :goto_43

    nop

    :goto_19
    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;

    move-result-object v0

    goto :goto_28

    nop

    :goto_1a
    if-eq v1, v2, :cond_2

    goto :goto_10

    :cond_2
    goto :goto_70

    nop

    :goto_1b
    move-object/from16 v4, p2

    :goto_1c
    goto :goto_30

    nop

    :goto_1d
    const-string v12, "User-Agent"

    goto :goto_61

    nop

    :goto_1e
    const-string v14, "&hl="

    goto :goto_95

    nop

    :goto_1f
    invoke-virtual {v6, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_3f

    nop

    :goto_20
    const-string v14, "&ie=UTF-8&oe=UTF-8&client=at&v=1.0"

    goto :goto_6d

    nop

    :goto_21
    invoke-virtual {v12}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v12

    goto :goto_3a

    nop

    :goto_22
    invoke-virtual {v6}, Ljava/lang/StringBuilder;->length()I

    move-result v13

    goto :goto_7

    nop

    :goto_23
    invoke-virtual {v6, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_8d

    nop

    :goto_24
    invoke-interface {v0, v8}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v9

    goto :goto_99

    nop

    :goto_25
    invoke-virtual {v9, v12}, Ljava/net/HttpURLConnection;->setConnectTimeout(I)V

    goto :goto_39

    nop

    :goto_26
    invoke-virtual {v2}, Lorg/json/JSONArray;->length()I

    move-result v9

    goto :goto_46

    nop

    :goto_27
    const-string v4, "auto"

    goto :goto_2d

    nop

    :goto_28
    invoke-virtual {v0}, Landroid/os/Looper;->isCurrentThread()Z

    move-result v0

    goto :goto_81

    nop

    :goto_29
    invoke-virtual {v1, v2}, Ljava/lang/Throwable;->addSuppressed(Ljava/lang/Throwable;)V

    :goto_2a
    goto :goto_47

    nop

    :goto_2b
    if-eqz v1, :cond_3

    goto :goto_59

    :cond_3
    goto :goto_58

    nop

    :goto_2c
    check-cast v12, Lorg/json/JSONArray;

    goto :goto_44

    nop

    :goto_2d
    if-nez v3, :cond_4

    goto :goto_91

    :cond_4
    goto :goto_4a

    nop

    :goto_2e
    invoke-virtual {v9}, Ljava/net/URL;->openConnection()Ljava/net/URLConnection;

    move-result-object v9

    goto :goto_93

    nop

    :goto_2f
    invoke-virtual {v12, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v12

    goto :goto_2

    nop

    :goto_30
    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;

    move-result-object v5

    goto :goto_53

    nop

    :goto_31
    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_4c

    nop

    :goto_32
    move-object/from16 v0, p3

    goto :goto_7f

    nop

    :goto_33
    const/4 v2, 0x1

    goto :goto_74

    nop

    :goto_34
    add-int v13, v8, v10

    goto :goto_87

    nop

    :goto_35
    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->setLength(I)V

    goto :goto_45

    nop

    :goto_36
    move v8, v7

    :goto_37
    goto :goto_8

    nop

    :goto_38
    if-nez v2, :cond_5

    goto :goto_18

    :cond_5
    goto :goto_17

    nop

    :goto_39
    invoke-virtual {v9, v12}, Ljava/net/HttpURLConnection;->setReadTimeout(I)V

    goto :goto_1d

    nop

    :goto_3a
    invoke-direct {v9, v12}, Ljava/net/URL;-><init>(Ljava/lang/String;)V

    goto :goto_2e

    nop

    :goto_3b
    goto :goto_1c

    :goto_3c
    goto :goto_1b

    nop

    :goto_3d
    invoke-virtual {v6, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_78

    nop

    :goto_3e
    const/4 v2, 0x1

    goto :goto_1a

    nop

    :goto_3f
    invoke-virtual {v6, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_89

    nop

    :goto_40
    invoke-static {v0, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_50

    nop

    :goto_41
    return-void

    :goto_42
    goto :goto_13

    nop

    :goto_43
    new-instance v2, Lorg/json/JSONArray;

    goto :goto_65

    nop

    :goto_44
    invoke-virtual {v12, v7}, Lorg/json/JSONArray;->getString(I)Ljava/lang/String;

    move-result-object v12

    goto :goto_97

    nop

    :goto_45
    const-string v9, "q="

    goto :goto_8f

    nop

    :goto_46
    if-ne v9, v13, :cond_6

    goto :goto_42

    :cond_6
    goto :goto_41

    nop

    :goto_47
    throw v1

    :goto_48
    goto :goto_67

    nop

    :goto_49
    add-int/2addr v13, v15

    goto :goto_5e

    nop

    :goto_4a
    move-object v3, v4

    goto :goto_90

    nop

    :goto_4b
    invoke-static {v12}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v13

    goto :goto_5b

    nop

    :goto_4c
    const/4 v7, 0x0

    goto :goto_36

    nop

    :goto_4d
    move v8, v11

    goto :goto_33

    nop

    :goto_4e
    const-string v14, "&sl="

    goto :goto_b

    nop

    :goto_4f
    if-lt v11, v1, :cond_7

    goto :goto_73

    :cond_7
    goto :goto_22

    nop

    :goto_50
    return-void

    :goto_51
    goto :goto_32

    nop

    :goto_52
    new-instance v6, Ljava/lang/StringBuilder;

    goto :goto_31

    nop

    :goto_53
    invoke-virtual {v5}, Ljava/util/Locale;->getLanguage()Ljava/lang/String;

    move-result-object v5

    goto :goto_52

    nop

    :goto_54
    const-string v14, "https://translate.google.com/translate_a/t?"

    goto :goto_86

    nop

    :goto_55
    invoke-virtual {v12, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v12

    goto :goto_20

    nop

    :goto_56
    const-string v12, "&q="

    goto :goto_4f

    nop

    :goto_57
    invoke-static {v9, v10}, Ljava/net/URLEncoder;->encode(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v9

    goto :goto_3d

    nop

    :goto_58
    return-void

    :goto_59
    goto :goto_3e

    nop

    :goto_5a
    invoke-virtual {v12, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v12

    goto :goto_66

    nop

    :goto_5b
    if-eqz v13, :cond_8

    goto :goto_6c

    :cond_8
    goto :goto_34

    nop

    :goto_5c
    invoke-static/range {p1 .. p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    goto :goto_27

    nop

    :goto_5d
    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v1

    goto :goto_2b

    nop

    :goto_5e
    add-int/lit8 v13, v13, 0x3

    goto :goto_83

    nop

    :goto_5f
    invoke-virtual {v2, v10}, Lorg/json/JSONArray;->get(I)Ljava/lang/Object;

    move-result-object v12

    goto :goto_64

    nop

    :goto_60
    invoke-virtual {v9}, Ljava/net/HttpURLConnection;->connect()V

    goto :goto_7d

    nop

    :goto_61
    sget-object v14, Lmezo/xiaomi/util/Translator;->USER_AGENT:Ljava/lang/String;

    goto :goto_6f

    nop

    :goto_62
    new-instance v12, Ljava/lang/StringBuilder;

    goto :goto_54

    nop

    :goto_63
    goto :goto_2a

    :catchall_0
    move-exception v0

    goto :goto_5

    nop

    :goto_64
    instance-of v13, v12, Lorg/json/JSONArray;

    goto :goto_7e

    nop

    :goto_65
    invoke-direct {v2, v9}, Lorg/json/JSONArray;-><init>(Ljava/lang/String;)V

    goto :goto_26

    nop

    :goto_66
    const-string v14, "&tl="

    goto :goto_2f

    nop

    :goto_67
    return-void

    :goto_68
    goto :goto_14

    :goto_69
    goto :goto_4d

    nop

    :goto_6a
    new-instance v9, Ljava/net/URL;

    goto :goto_62

    nop

    :goto_6b
    invoke-interface {v0, v13, v12}, Ljava/util/List;->set(ILjava/lang/Object;)Ljava/lang/Object;

    :goto_6c
    goto :goto_9

    nop

    :goto_6d
    invoke-virtual {v12, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v12

    goto :goto_21

    nop

    :goto_6e
    if-nez v5, :cond_9

    goto :goto_3c

    :cond_9
    goto :goto_3b

    nop

    :goto_6f
    invoke-virtual {v9, v12, v14}, Ljava/net/HttpURLConnection;->setRequestProperty(Ljava/lang/String;Ljava/lang/String;)V

    goto :goto_60

    nop

    :goto_70
    const-string v3, ""

    goto :goto_71

    nop

    :goto_71
    invoke-interface {v0, v3}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_f

    nop

    :goto_72
    goto :goto_79

    :goto_73
    goto :goto_7a

    nop

    :goto_74
    goto :goto_37

    :catchall_1
    move-exception v0

    goto :goto_7c

    nop

    :goto_75
    if-lt v10, v9, :cond_a

    goto :goto_69

    :cond_a
    goto :goto_5f

    nop

    :goto_76
    move-object/from16 v3, p1

    :goto_77
    goto :goto_7b

    nop

    :goto_78
    move v9, v8

    :goto_79
    goto :goto_c

    nop

    :goto_7a
    sub-int/2addr v9, v8

    goto :goto_16

    nop

    :goto_7b
    invoke-static/range {p2 .. p2}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v5

    goto :goto_6e

    nop

    :goto_7c
    move-object v1, v0

    :try_start_4
    invoke-virtual {v2}, Ljava/io/BufferedInputStream;->close()V
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_3

    goto :goto_88

    nop

    :goto_7d
    const/16 v12, 0x1000

    goto :goto_15

    nop

    :goto_7e
    if-nez v13, :cond_b

    goto :goto_98

    :cond_b
    goto :goto_2c

    nop

    :goto_7f
    iget-object v0, v0, Lmezo/xiaomi/util/Translator$State;->textList:Ljava/util/List;

    goto :goto_5d

    nop

    :goto_80
    const-string v10, "UTF-8"

    goto :goto_57

    nop

    :goto_81
    if-nez v0, :cond_c

    goto :goto_51

    :cond_c
    goto :goto_96

    nop

    :goto_82
    if-le v13, v15, :cond_d

    goto :goto_73

    :cond_d
    goto :goto_1f

    nop

    :goto_83
    const/16 v15, 0x2710

    goto :goto_82

    nop

    :goto_84
    move-object v2, v0

    :try_start_5
    invoke-virtual {v1, v2}, Ljava/lang/Throwable;->addSuppressed(Ljava/lang/Throwable;)V

    :goto_85
    throw v1
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_2

    :catchall_2
    move-exception v0

    goto :goto_1

    nop

    :goto_86
    invoke-direct {v12, v14}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    goto :goto_12

    nop

    :goto_87
    invoke-static {v12}, Lmezo/xiaomi/util/Translator;->toProperCase(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v12

    goto :goto_6b

    nop

    :goto_88
    goto :goto_85

    :catchall_3
    move-exception v0

    goto :goto_84

    nop

    :goto_89
    move v9, v11

    goto :goto_72

    nop

    :goto_8a
    invoke-static {v9}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v2

    goto :goto_38

    nop

    :goto_8b
    const-string v1, "Cannot run translator on UI thread."

    goto :goto_40

    nop

    :goto_8c
    invoke-virtual {v15}, Ljava/io/ByteArrayOutputStream;->close()V

    goto :goto_8a

    nop

    :goto_8d
    add-int/lit8 v13, v9, 0x2

    :goto_8e
    goto :goto_6a

    nop

    :goto_8f
    invoke-virtual {v6, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_24

    nop

    :goto_90
    goto :goto_77

    :goto_91
    goto :goto_76

    nop

    :goto_92
    invoke-virtual {v14}, Ljava/lang/String;->length()I

    move-result v15

    goto :goto_49

    nop

    :goto_93
    check-cast v9, Ljava/net/HttpURLConnection;

    goto :goto_11

    nop

    :goto_94
    if-eq v13, v2, :cond_e

    goto :goto_8e

    :cond_e
    goto :goto_23

    nop

    :goto_95
    invoke-virtual {v12, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v12

    goto :goto_55

    nop

    :goto_96
    const-string v0, "Translator"

    goto :goto_8b

    nop

    :goto_97
    goto :goto_4

    :goto_98
    goto :goto_3

    nop

    :goto_99
    check-cast v9, Ljava/lang/String;

    goto :goto_80

    nop
.end method

.method public whitelist translate(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;)V
    .registers 9

    if-eqz p3, :cond_3

    array-length v0, p3

    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    new-instance v0, Lmezo/xiaomi/util/Translator$State;

    invoke-direct {v0}, Lmezo/xiaomi/util/Translator$State;-><init>()V

    const/4 v1, 0x0

    :goto_0
    array-length v2, p3

    if-ge v1, v2, :cond_2

    aget-object v2, p3, v1

    invoke-virtual {v2}, Ljava/lang/String;->trim()Ljava/lang/String;

    move-result-object v2

    iget-object v3, v0, Lmezo/xiaomi/util/Translator$State;->textSet:Ljava/util/Set;

    invoke-interface {v3, v2}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v3

    if-eqz v3, :cond_1

    iget-object v3, v0, Lmezo/xiaomi/util/Translator$State;->textList:Ljava/util/List;

    invoke-interface {v3, v2}, Ljava/util/List;->indexOf(Ljava/lang/Object;)I

    move-result v2

    move v4, v2

    move v2, v1

    move v1, v4

    goto :goto_1

    :cond_1
    iget-object v3, v0, Lmezo/xiaomi/util/Translator$State;->textSet:Ljava/util/Set;

    invoke-interface {v3, v2}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    iget-object v3, v0, Lmezo/xiaomi/util/Translator$State;->textList:Ljava/util/List;

    invoke-interface {v3, v2}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    add-int/lit8 v2, v1, 0x1

    :goto_1
    iget-object v3, v0, Lmezo/xiaomi/util/Translator$State;->indexList:Ljava/util/List;

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-interface {v3, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    add-int/lit8 v1, v2, 0x1

    goto :goto_0

    :cond_2
    :try_start_0
    invoke-virtual {p0, p1, p2, v0}, Lmezo/xiaomi/util/Translator;->translate(Ljava/lang/String;Ljava/lang/String;Lmezo/xiaomi/util/Translator$State;)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_2

    :catch_0
    move-exception p1

    const-string p2, "Translator"

    invoke-virtual {p1}, Ljava/lang/Exception;->getMessage()Ljava/lang/String;

    move-result-object p3

    invoke-static {p2, p3, p1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_3
    :goto_2
    return-void
.end method

.method public whitelist translateAuto(Ljava/lang/String;)Ljava/lang/String;
    .registers 3

    const/4 v0, 0x0

    invoke-virtual {p0, v0, v0, p1}, Lmezo/xiaomi/util/Translator;->translate(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p1

    return-object p1
.end method

.method public whitelist translateAuto([Ljava/lang/String;)V
    .registers 3

    const/4 v0, 0x0

    invoke-virtual {p0, v0, v0, p1}, Lmezo/xiaomi/util/Translator;->translate(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;)V

    return-void
.end method

.method public whitelist translateFrom(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .registers 4

    const/4 v0, 0x0

    invoke-virtual {p0, p1, v0, p2}, Lmezo/xiaomi/util/Translator;->translate(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p1

    return-object p1
.end method

.method public whitelist translateFrom(Ljava/lang/String;[Ljava/lang/String;)V
    .registers 4

    const/4 v0, 0x0

    invoke-virtual {p0, p1, v0, p2}, Lmezo/xiaomi/util/Translator;->translate(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;)V

    return-void
.end method

.method public whitelist translateTo(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .registers 4

    const/4 v0, 0x0

    invoke-virtual {p0, v0, p1, p2}, Lmezo/xiaomi/util/Translator;->translate(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p1

    return-object p1
.end method

.method public whitelist translateTo(Ljava/lang/String;[Ljava/lang/String;)V
    .registers 4

    const/4 v0, 0x0

    invoke-virtual {p0, v0, p1, p2}, Lmezo/xiaomi/util/Translator;->translate(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;)V

    return-void
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from miui-framework_Legend.mtcr",
    },
]
