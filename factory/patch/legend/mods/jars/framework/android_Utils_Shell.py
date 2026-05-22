"""
Legend MTCR patch - class-level rule.

Target JAR   : framework.jar
Target class : android/Utils/Shell
Source MTCR  : Framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "framework.jar"
TARGET_CLASS = "android/Utils/Shell.smali"
CLASS_FALLBACK_NAMES = ['Shell.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "add_class_android_Utils_Shell",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public Landroid/Utils/Shell;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Landroid/Utils/Shell$CommandResult;
    }
.end annotation


# static fields
.field public static final COMMAND_EXIT:Ljava/lang/String; = "exit\\n"

.field public static final COMMAND_LINE_END:Ljava/lang/String; = "\\n"

.field public static final COMMAND_SH:Ljava/lang/String; = "sh"

.field public static final COMMAND_SU:Ljava/lang/String; = "su"


# direct methods
.method private constructor <init>()V
    .registers 2

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/lang/AssertionError;

    invoke-direct {v0}, Ljava/lang/AssertionError;-><init>()V

    throw v0
.end method

.method public static checkRootPermission()Z
    .registers 3

    const/4 v0, 0x1

    const/4 v1, 0x0

    const-string v2, "echo root"

    invoke-static {v2, v0, v1}, Landroid/Utils/Shell;->execCommand(Ljava/lang/String;ZZ)Landroid/Utils/Shell$CommandResult;

    move-result-object v2

    iget v2, v2, Landroid/Utils/Shell$CommandResult;->result:I

    if-nez v2, :cond_0

    :goto_0
    return v0

    :cond_0
    move v0, v1

    goto :goto_0
.end method

.method public static execCommand(Ljava/lang/String;Z)Landroid/Utils/Shell$CommandResult;
    .registers 5

    const/4 v2, 0x1

    new-array v0, v2, [Ljava/lang/String;

    const/4 v1, 0x0

    aput-object p0, v0, v1

    invoke-static {v0, p1, v2}, Landroid/Utils/Shell;->execCommand([Ljava/lang/String;ZZ)Landroid/Utils/Shell$CommandResult;

    move-result-object v0

    return-object v0
.end method

.method public static execCommand(Ljava/lang/String;ZZ)Landroid/Utils/Shell$CommandResult;
    .registers 5

    const/4 v0, 0x1

    new-array v0, v0, [Ljava/lang/String;

    const/4 v1, 0x0

    aput-object p0, v0, v1

    invoke-static {v0, p1, p2}, Landroid/Utils/Shell;->execCommand([Ljava/lang/String;ZZ)Landroid/Utils/Shell$CommandResult;

    move-result-object v0

    return-object v0
.end method

.method public static execCommand(Ljava/util/List;Z)Landroid/Utils/Shell$CommandResult;
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/List",
            "<",
            "Ljava/lang/String;",
            ">;Z)",
            "Landroid/Utils/Shell$CommandResult;"
        }
    .end annotation

    if-nez p0, :cond_0

    const/4 v0, 0x0

    :goto_0
    const/4 v1, 0x1

    invoke-static {v0, p1, v1}, Landroid/Utils/Shell;->execCommand([Ljava/lang/String;ZZ)Landroid/Utils/Shell$CommandResult;

    move-result-object v0

    return-object v0

    :cond_0
    const/4 v0, 0x0

    new-array v0, v0, [Ljava/lang/String;

    invoke-interface {p0, v0}, Ljava/util/List;->toArray([Ljava/lang/Object;)[Ljava/lang/Object;

    move-result-object v0

    check-cast v0, [Ljava/lang/String;

    goto :goto_0
.end method

.method public static execCommand(Ljava/util/List;ZZ)Landroid/Utils/Shell$CommandResult;
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/List",
            "<",
            "Ljava/lang/String;",
            ">;ZZ)",
            "Landroid/Utils/Shell$CommandResult;"
        }
    .end annotation

    if-nez p0, :cond_0

    const/4 v0, 0x0

    :goto_0
    invoke-static {v0, p1, p2}, Landroid/Utils/Shell;->execCommand([Ljava/lang/String;ZZ)Landroid/Utils/Shell$CommandResult;

    move-result-object v0

    return-object v0

    :cond_0
    const/4 v0, 0x0

    new-array v0, v0, [Ljava/lang/String;

    invoke-interface {p0, v0}, Ljava/util/List;->toArray([Ljava/lang/Object;)[Ljava/lang/Object;

    move-result-object v0

    check-cast v0, [Ljava/lang/String;

    goto :goto_0
.end method

.method public static execCommand([Ljava/lang/String;Z)Landroid/Utils/Shell$CommandResult;
    .registers 3

    const/4 v0, 0x1

    invoke-static {p0, p1, v0}, Landroid/Utils/Shell;->execCommand([Ljava/lang/String;ZZ)Landroid/Utils/Shell$CommandResult;

    move-result-object v0

    return-object v0
.end method

.method public static execCommand([Ljava/lang/String;ZZ)Landroid/Utils/Shell$CommandResult;
    .registers 24

    const/4 v12, -0x1

    if-eqz p0, :cond_0

    move-object/from16 v0, p0

    array-length v0, v0

    move/from16 v18, v0

    if-nez v18, :cond_1

    :cond_0
    new-instance v18, Landroid/Utils/Shell$CommandResult;

    const/16 v19, 0x0

    const/16 v20, 0x0

    move-object/from16 v0, v18

    move-object/from16 v1, v19

    move-object/from16 v2, v20

    invoke-direct {v0, v12, v1, v2}, Landroid/Utils/Shell$CommandResult;-><init>(ILjava/lang/String;Ljava/lang/String;)V

    :goto_0
    return-object v18

    :cond_1
    const/4 v11, 0x0

    const/16 v16, 0x0

    const/4 v7, 0x0

    const/4 v14, 0x0

    const/4 v5, 0x0

    const/4 v9, 0x0

    :try_start_0
    invoke-static {}, Ljava/lang/Runtime;->getRuntime()Ljava/lang/Runtime;

    move-result-object v19

    if-eqz p1, :cond_2

    const-string v18, "su"

    :goto_1
    move-object/from16 v0, v19

    move-object/from16 v1, v18

    invoke-virtual {v0, v1}, Ljava/lang/Runtime;->exec(Ljava/lang/String;)Ljava/lang/Process;

    move-result-object v11

    new-instance v10, Ljava/io/DataOutputStream;

    invoke-virtual {v11}, Ljava/lang/Process;->getOutputStream()Ljava/io/OutputStream;

    move-result-object v18

    move-object/from16 v0, v18

    invoke-direct {v10, v0}, Ljava/io/DataOutputStream;-><init>(Ljava/io/OutputStream;)V
    :try_end_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_c
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_7
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :try_start_1
    move-object/from16 v0, p0

    array-length v0, v0

    move/from16 v19, v0

    const/16 v18, 0x0

    :goto_2
    move/from16 v0, v18

    move/from16 v1, v19

    if-ge v0, v1, :cond_8

    aget-object v3, p0, v18
    :try_end_1
    .catch Ljava/io/IOException; {:try_start_1 .. :try_end_1} :catch_0
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_8
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    if-nez v3, :cond_3

    :goto_3
    add-int/lit8 v18, v18, 0x1

    goto :goto_2

    :cond_2
    :try_start_2
    const-string v18, "sh"
    :try_end_2
    .catch Ljava/io/IOException; {:try_start_2 .. :try_end_2} :catch_c
    .catch Ljava/lang/Exception; {:try_start_2 .. :try_end_2} :catch_7
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_1

    :cond_3
    :try_start_3
    invoke-virtual {v3}, Ljava/lang/String;->getBytes()[B

    move-result-object v20

    move-object/from16 v0, v20

    invoke-virtual {v10, v0}, Ljava/io/DataOutputStream;->write([B)V

    const-string v20, "\\n"

    move-object/from16 v0, v20

    invoke-virtual {v10, v0}, Ljava/io/DataOutputStream;->writeBytes(Ljava/lang/String;)V

    invoke-virtual {v10}, Ljava/io/DataOutputStream;->flush()V
    :try_end_3
    .catch Ljava/io/IOException; {:try_start_3 .. :try_end_3} :catch_0
    .catch Ljava/lang/Exception; {:try_start_3 .. :try_end_3} :catch_8
    .catchall {:try_start_3 .. :try_end_3} :catchall_1

    goto :goto_3

    :catch_0
    move-exception v4

    move-object v9, v10

    :goto_4
    :try_start_4
    invoke-virtual {v4}, Ljava/io/IOException;->printStackTrace()V
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_0

    if-eqz v9, :cond_4

    :try_start_5
    invoke-virtual {v9}, Ljava/io/DataOutputStream;->close()V

    :cond_4
    if-eqz v16, :cond_5

    invoke-virtual/range {v16 .. v16}, Ljava/io/BufferedReader;->close()V

    :cond_5
    if-eqz v7, :cond_6

    invoke-virtual {v7}, Ljava/io/BufferedReader;->close()V
    :try_end_5
    .catch Ljava/io/IOException; {:try_start_5 .. :try_end_5} :catch_4

    :cond_6
    :goto_5
    if-eqz v11, :cond_7

    invoke-virtual {v11}, Ljava/lang/Process;->destroy()V

    :cond_7
    :goto_6
    new-instance v19, Landroid/Utils/Shell$CommandResult;

    if-nez v14, :cond_16

    const/16 v18, 0x0

    move-object/from16 v20, v18

    :goto_7
    if-nez v5, :cond_17

    const/16 v18, 0x0

    :goto_8
    move-object/from16 v0, v19

    move-object/from16 v1, v20

    move-object/from16 v2, v18

    invoke-direct {v0, v12, v1, v2}, Landroid/Utils/Shell$CommandResult;-><init>(ILjava/lang/String;Ljava/lang/String;)V

    move-object/from16 v18, v19

    goto :goto_0

    :cond_8
    :try_start_6
    const-string v18, "exit\\n"

    move-object/from16 v0, v18

    invoke-virtual {v10, v0}, Ljava/io/DataOutputStream;->writeBytes(Ljava/lang/String;)V

    invoke-virtual {v10}, Ljava/io/DataOutputStream;->flush()V

    invoke-virtual {v11}, Ljava/lang/Process;->waitFor()I

    move-result v12

    if-eqz p2, :cond_e

    new-instance v15, Ljava/lang/StringBuilder;

    invoke-direct {v15}, Ljava/lang/StringBuilder;-><init>()V
    :try_end_6
    .catch Ljava/io/IOException; {:try_start_6 .. :try_end_6} :catch_0
    .catch Ljava/lang/Exception; {:try_start_6 .. :try_end_6} :catch_8
    .catchall {:try_start_6 .. :try_end_6} :catchall_1

    :try_start_7
    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V
    :try_end_7
    .catch Ljava/io/IOException; {:try_start_7 .. :try_end_7} :catch_d
    .catch Ljava/lang/Exception; {:try_start_7 .. :try_end_7} :catch_9
    .catchall {:try_start_7 .. :try_end_7} :catchall_2

    :try_start_8
    new-instance v17, Ljava/io/BufferedReader;

    new-instance v18, Ljava/io/InputStreamReader;

    invoke-virtual {v11}, Ljava/lang/Process;->getInputStream()Ljava/io/InputStream;

    move-result-object v19

    invoke-direct/range {v18 .. v19}, Ljava/io/InputStreamReader;-><init>(Ljava/io/InputStream;)V

    invoke-direct/range {v17 .. v18}, Ljava/io/BufferedReader;-><init>(Ljava/io/Reader;)V
    :try_end_8
    .catch Ljava/io/IOException; {:try_start_8 .. :try_end_8} :catch_e
    .catch Ljava/lang/Exception; {:try_start_8 .. :try_end_8} :catch_a
    .catchall {:try_start_8 .. :try_end_8} :catchall_3

    :try_start_9
    new-instance v8, Ljava/io/BufferedReader;

    new-instance v18, Ljava/io/InputStreamReader;

    invoke-virtual {v11}, Ljava/lang/Process;->getErrorStream()Ljava/io/InputStream;

    move-result-object v19

    invoke-direct/range {v18 .. v19}, Ljava/io/InputStreamReader;-><init>(Ljava/io/InputStream;)V

    move-object/from16 v0, v18

    invoke-direct {v8, v0}, Ljava/io/BufferedReader;-><init>(Ljava/io/Reader;)V
    :try_end_9
    .catch Ljava/io/IOException; {:try_start_9 .. :try_end_9} :catch_f
    .catch Ljava/lang/Exception; {:try_start_9 .. :try_end_9} :catch_b
    .catchall {:try_start_9 .. :try_end_9} :catchall_4

    :goto_9
    :try_start_a
    invoke-virtual/range {v17 .. v17}, Ljava/io/BufferedReader;->readLine()Ljava/lang/String;

    move-result-object v13

    if-eqz v13, :cond_9

    invoke-virtual {v15, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_9

    :catch_1
    move-exception v4

    move-object v9, v10

    move-object v5, v6

    move-object v14, v15

    move-object v7, v8

    move-object/from16 v16, v17

    goto :goto_4

    :cond_9
    :goto_a
    invoke-virtual {v8}, Ljava/io/BufferedReader;->readLine()Ljava/lang/String;

    move-result-object v13

    if-eqz v13, :cond_d

    invoke-virtual {v6, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    :try_end_a
    .catch Ljava/io/IOException; {:try_start_a .. :try_end_a} :catch_1
    .catch Ljava/lang/Exception; {:try_start_a .. :try_end_a} :catch_2
    .catchall {:try_start_a .. :try_end_a} :catchall_5

    goto :goto_a

    :catch_2
    move-exception v4

    move-object v9, v10

    move-object v5, v6

    move-object v14, v15

    move-object v7, v8

    move-object/from16 v16, v17

    :goto_b
    :try_start_b
    invoke-virtual {v4}, Ljava/lang/Exception;->printStackTrace()V
    :try_end_b
    .catchall {:try_start_b .. :try_end_b} :catchall_0

    if-eqz v9, :cond_a

    :try_start_c
    invoke-virtual {v9}, Ljava/io/DataOutputStream;->close()V

    :cond_a
    if-eqz v16, :cond_b

    invoke-virtual/range {v16 .. v16}, Ljava/io/BufferedReader;->close()V

    :cond_b
    if-eqz v7, :cond_c

    invoke-virtual {v7}, Ljava/io/BufferedReader;->close()V
    :try_end_c
    .catch Ljava/io/IOException; {:try_start_c .. :try_end_c} :catch_5

    :cond_c
    :goto_c
    if-eqz v11, :cond_7

    invoke-virtual {v11}, Ljava/lang/Process;->destroy()V

    goto :goto_6

    :cond_d
    move-object v5, v6

    move-object v14, v15

    move-object v7, v8

    move-object/from16 v16, v17

    :cond_e
    if-eqz v10, :cond_f

    :try_start_d
    invoke-virtual {v10}, Ljava/io/DataOutputStream;->close()V

    :cond_f
    if-eqz v16, :cond_10

    invoke-virtual/range {v16 .. v16}, Ljava/io/BufferedReader;->close()V

    :cond_10
    if-eqz v7, :cond_11

    invoke-virtual {v7}, Ljava/io/BufferedReader;->close()V
    :try_end_d
    .catch Ljava/io/IOException; {:try_start_d .. :try_end_d} :catch_3

    :cond_11
    :goto_d
    if-eqz v11, :cond_18

    invoke-virtual {v11}, Ljava/lang/Process;->destroy()V

    move-object v9, v10

    goto :goto_6

    :catch_3
    move-exception v4

    invoke-virtual {v4}, Ljava/io/IOException;->printStackTrace()V

    goto :goto_d

    :catch_4
    move-exception v4

    invoke-virtual {v4}, Ljava/io/IOException;->printStackTrace()V

    goto :goto_5

    :catch_5
    move-exception v4

    invoke-virtual {v4}, Ljava/io/IOException;->printStackTrace()V

    goto :goto_c

    :catchall_0
    move-exception v18

    :goto_e
    if-eqz v9, :cond_12

    :try_start_e
    invoke-virtual {v9}, Ljava/io/DataOutputStream;->close()V

    :cond_12
    if-eqz v16, :cond_13

    invoke-virtual/range {v16 .. v16}, Ljava/io/BufferedReader;->close()V

    :cond_13
    if-eqz v7, :cond_14

    invoke-virtual {v7}, Ljava/io/BufferedReader;->close()V
    :try_end_e
    .catch Ljava/io/IOException; {:try_start_e .. :try_end_e} :catch_6

    :cond_14
    :goto_f
    if-eqz v11, :cond_15

    invoke-virtual {v11}, Ljava/lang/Process;->destroy()V

    :cond_15
    throw v18

    :catch_6
    move-exception v4

    invoke-virtual {v4}, Ljava/io/IOException;->printStackTrace()V

    goto :goto_f

    :cond_16
    invoke-virtual {v14}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v18

    move-object/from16 v20, v18

    goto :goto_7

    :cond_17
    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v18

    goto :goto_8

    :catchall_1
    move-exception v18

    move-object v9, v10

    goto :goto_e

    :catchall_2
    move-exception v18

    move-object v9, v10

    move-object v14, v15

    goto :goto_e

    :catchall_3
    move-exception v18

    move-object v9, v10

    move-object v5, v6

    move-object v14, v15

    goto :goto_e

    :catchall_4
    move-exception v18

    move-object v9, v10

    move-object v5, v6

    move-object v14, v15

    move-object/from16 v16, v17

    goto :goto_e

    :catchall_5
    move-exception v18

    move-object v9, v10

    move-object v5, v6

    move-object v14, v15

    move-object v7, v8

    move-object/from16 v16, v17

    goto :goto_e

    :catch_7
    move-exception v4

    goto :goto_b

    :catch_8
    move-exception v4

    move-object v9, v10

    goto :goto_b

    :catch_9
    move-exception v4

    move-object v9, v10

    move-object v14, v15

    goto :goto_b

    :catch_a
    move-exception v4

    move-object v9, v10

    move-object v5, v6

    move-object v14, v15

    goto :goto_b

    :catch_b
    move-exception v4

    move-object v9, v10

    move-object v5, v6

    move-object v14, v15

    move-object/from16 v16, v17

    goto :goto_b

    :catch_c
    move-exception v4

    goto :goto_4

    :catch_d
    move-exception v4

    move-object v9, v10

    move-object v14, v15

    goto :goto_4

    :catch_e
    move-exception v4

    move-object v9, v10

    move-object v5, v6

    move-object v14, v15

    goto :goto_4

    :catch_f
    move-exception v4

    move-object v9, v10

    move-object v5, v6

    move-object v14, v15

    move-object/from16 v16, v17

    goto :goto_4

    :cond_18
    move-object v9, v10

    goto :goto_6
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from Framework_Legend.mtcr",
    },
]
