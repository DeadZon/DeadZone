TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'com/miui/powerkeeper/customerpower/CustomerPowerCheck.smali'
CLASS_FALLBACK_NAMES = ['CustomerPowerCheck.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final TAG:Ljava/lang/String;', '.field private static final WHICH:I']

PATCHES = [
    {
        'id': 'com_miui_powerkeeper_customerpower_CustomerPowerCheck__outputResultPassAndNone',
        'method': '.method private outputResultPassAndNone(Ljava/io/PrintWriter;I)V',
        'method_name': 'outputResultPassAndNone',
        'method_anchors': ['iget-object v3, v0, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->mContext:Landroid/content/Context;', 'invoke-static {v3}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;->getInstance(Landroid/content/Context;)Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;', 'const-string v4, "CustomerPowerRecordTable"', 'invoke-virtual {v3, v4, v2}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;->query(Ljava/lang/String;I)Ljava/util/ArrayList;', 'invoke-virtual {v3}, Ljava/util/ArrayList;->size()I', 'iget-object v6, v0, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->mContext:Landroid/content/Context;', 'invoke-static {v6}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;->getInstance(Landroid/content/Context;)Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;', 'invoke-static {}, Ljava/lang/System;->currentTimeMillis()J'],
        'type': 'method_replace',
        'search': """.method private outputResultPassAndNone(Ljava/io/PrintWriter;I)V
    .registers 25

    move-object/from16 v0, p0

    move-object/from16 v1, p1

    move/from16 v2, p2

    iget-object v3, v0, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->mContext:Landroid/content/Context;

    invoke-static {v3}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;->getInstance(Landroid/content/Context;)Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;

    move-result-object v3

    const-string v4, "CustomerPowerRecordTable"

    invoke-virtual {v3, v4, v2}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;->query(Ljava/lang/String;I)Ljava/util/ArrayList;

    move-result-object v3

    invoke-virtual {v3}, Ljava/util/ArrayList;->size()I

    move-result v5

    iget-object v6, v0, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->mContext:Landroid/content/Context;

    invoke-static {v6}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;->getInstance(Landroid/content/Context;)Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;

    move-result-object v6

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v7

    invoke-virtual {v6, v4, v7, v8}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;->queryAllByWeek(Ljava/lang/String;J)Ljava/util/ArrayList;

    move-result-object v4

    invoke-virtual {v4}, Ljava/util/ArrayList;->size()I

    move-result v6

    const/4 v10, 0x2

    const/16 v11, 0xc

    const-string v12, ","

    const/16 v13, 0xb

    const/4 v14, 0x1

    const/4 v15, 0x0

    if-nez v1, :cond_16

    :try_start_0
    invoke-static {}, Lcom/miui/powerkeeper/customerpower/CustomerPowerUtil;->isMaintenanceModeEnable()Z

    move-result v4

    invoke-direct {v0, v4}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->targetFilePath(Z)Ljava/lang/String;

    move-result-object v6

    if-eqz v6, :cond_0

    new-instance v7, Ljava/io/File;

    invoke-direct {v7, v6}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    goto :goto_0

    :catchall_0
    move-exception v0

    move-object v4, v1

    goto :goto_9

    :catch_0
    move-object v4, v1

    goto :goto_8

    :cond_0
    const/4 v7, 0x0

    :goto_0
    invoke-virtual {v7}, Ljava/io/File;->exists()Z

    move-result v6

    if-nez v6, :cond_1

    invoke-virtual {v7}, Ljava/io/File;->createNewFile()Z

    :cond_1
    if-eqz v4, :cond_2

    invoke-virtual {v7, v14, v15}, Ljava/io/File;->setWritable(ZZ)Z

    invoke-virtual {v7, v14, v15}, Ljava/io/File;->setReadable(ZZ)Z

    :cond_2
    new-instance v4, Ljava/io/PrintWriter;

    new-instance v6, Ljava/io/FileOutputStream;

    invoke-direct {v6, v7}, Ljava/io/FileOutputStream;-><init>(Ljava/io/File;)V

    invoke-direct {v4, v6}, Ljava/io/PrintWriter;-><init>(Ljava/io/OutputStream;)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    if-nez v2, :cond_3

    :try_start_1
    const-string v1, "TEST_CUSTOMER_POWER"

    invoke-virtual {v4, v1}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_1

    :catchall_1
    move-exception v0

    goto :goto_9

    :cond_3
    if-ne v2, v14, :cond_4

    const-string v1, "TEST_FACTORY_CUSTOMER_POWER"

    invoke-virtual {v4, v1}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_4
    :goto_1
    if-lez v5, :cond_f

    move v1, v15

    move v6, v1

    move v7, v6

    move/from16 v16, v7

    move/from16 v17, v16

    move/from16 v18, v17

    move/from16 v19, v18

    :goto_2
    if-ge v15, v5, :cond_e

    invoke-virtual {v3, v15}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v20

    check-cast v20, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;

    invoke-virtual/range {v20 .. v20}, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;->getType()I

    move-result v14

    if-ne v14, v13, :cond_5

    if-nez v17, :cond_5

    sget-boolean v21, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v21, :cond_5

    add-int/lit8 v17, v17, 0x1

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v9, "App bg cpu: "

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual/range {v20 .. v20}, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;->getDetailName()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v9, v12}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v0, v9}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->getLabelByPackageNames([Ljava/lang/String;)Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_3

    :cond_5
    if-ne v14, v13, :cond_6

    if-nez v17, :cond_6

    sget-boolean v8, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v8, :cond_6

    add-int/lit8 v17, v17, 0x1

    const-string v8, "App bg cpu"

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_6
    :goto_3
    if-ne v14, v11, :cond_7

    if-nez v18, :cond_7

    sget-boolean v8, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v8, :cond_7

    add-int/lit8 v18, v18, 0x1

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v9, "App partial wakelock: "

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual/range {v20 .. v20}, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;->getDetailName()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v9, v12}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v0, v9}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->getLabelByPackageNames([Ljava/lang/String;)Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_4

    :cond_7
    if-ne v14, v11, :cond_8

    if-nez v18, :cond_8

    sget-boolean v8, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v8, :cond_8

    add-int/lit8 v18, v18, 0x1

    const-string v8, "App partial wakelock"

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_8
    :goto_4
    if-ne v14, v10, :cond_9

    if-nez v1, :cond_9

    add-int/lit8 v1, v1, 0x1

    const-string v8, "High brightness"

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_9
    const/4 v8, 0x5

    if-ne v14, v8, :cond_a

    if-nez v7, :cond_a

    add-int/lit8 v7, v7, 0x1

    const-string v8, "Kernel wakelock"

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_a
    const/4 v8, 0x6

    if-ne v14, v8, :cond_b

    if-nez v16, :cond_b

    add-int/lit8 v16, v16, 0x1

    const-string v8, "Kernel wakeup"

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_b
    const/4 v8, 0x1

    if-ne v14, v8, :cond_c

    if-nez v6, :cond_c

    add-int/lit8 v6, v6, 0x1

    const-string v8, "Bad signal"

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_c
    const/16 v8, 0x64

    if-ne v14, v8, :cond_d

    if-nez v19, :cond_d

    add-int/lit8 v19, v19, 0x1

    :cond_d
    add-int/lit8 v15, v15, 0x1

    const/4 v14, 0x1

    goto :goto_2

    :cond_e
    move v15, v1

    goto :goto_5

    :cond_f
    sget-object v0, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->TAG:Ljava/lang/String;

    const-string v1, "customer power info power is not checked"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    move v6, v15

    move v7, v6

    move/from16 v16, v7

    move/from16 v17, v16

    move/from16 v18, v17

    const/16 v19, 0x1

    :goto_5
    if-nez v15, :cond_12

    if-nez v6, :cond_12

    if-nez v7, :cond_12

    if-nez v16, :cond_12

    if-nez v17, :cond_12

    if-eqz v18, :cond_10

    goto :goto_6

    :cond_10
    if-eqz v19, :cond_14

    if-nez v2, :cond_11

    const-string v0, "TEST_CUSTOMER_POWER:NONE"

    invoke-virtual {v4, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_7

    :cond_11
    const/4 v8, 0x1

    if-ne v2, v8, :cond_14

    const-string v0, "TEST_FACTORY_CUSTOMER_POWER:NONE"

    invoke-virtual {v4, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_7

    :cond_12
    :goto_6
    if-nez v2, :cond_13

    const-string v0, "TEST_CUSTOMER_POWER:PASS"

    invoke-virtual {v4, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_7

    :cond_13
    const/4 v8, 0x1

    if-ne v2, v8, :cond_14

    const-string v0, "TEST_FACTORY_CUSTOMER_POWER:PASS"

    invoke-virtual {v4, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    :cond_14
    :goto_7
    invoke-virtual {v4}, Ljava/io/PrintWriter;->close()V

    goto :goto_11

    :catch_1
    :goto_8
    :try_start_2
    sget-object v0, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->TAG:Ljava/lang/String;

    const-string v1, "customer power info create autotestfile or write file failed"

    invoke-static {v0, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    if-eqz v4, :cond_29

    goto :goto_7

    :goto_9
    if-eqz v4, :cond_15

    invoke-virtual {v4}, Ljava/io/PrintWriter;->close()V

    :cond_15
    throw v0

    :cond_16
    if-nez v2, :cond_17

    const-string v3, "  TEST_CUSTOMER_POWER"

    invoke-virtual {v1, v3}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_a

    :cond_17
    const/4 v8, 0x1

    if-ne v2, v8, :cond_18

    const-string v3, "  TEST_FACTORY_CUSTOMER_POWER"

    invoke-virtual {v1, v3}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_18
    :goto_a
    if-lez v6, :cond_24

    move v3, v15

    move v5, v3

    move v7, v5

    move v8, v7

    move v9, v8

    move v14, v9

    move/from16 v16, v14

    :goto_b
    if-ge v15, v6, :cond_23

    invoke-virtual {v4, v15}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v17

    check-cast v17, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;

    invoke-virtual/range {v17 .. v17}, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;->getType()I

    move-result v10

    if-ne v10, v13, :cond_1a

    sget-boolean v19, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v19, :cond_1a

    add-int/lit8 v9, v9, 0x1

    new-instance v11, Ljava/lang/StringBuilder;

    invoke-direct {v11}, Ljava/lang/StringBuilder;-><init>()V

    const-string v13, "  App bg cpu: "

    invoke-virtual {v11, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual/range {v17 .. v17}, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;->getDetailName()Ljava/lang/String;

    move-result-object v13

    invoke-virtual {v13, v12}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v13

    invoke-virtual {v0, v13}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->getLabelByPackageNames([Ljava/lang/String;)Ljava/lang/String;

    move-result-object v13

    invoke-virtual {v11, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v11}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    const/16 v11, 0xb

    :cond_19
    :goto_c
    const/16 v13, 0xc

    goto :goto_d

    :cond_1a
    move v11, v13

    if-ne v10, v11, :cond_19

    sget-boolean v13, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v13, :cond_19

    add-int/lit8 v9, v9, 0x1

    const-string v13, "  App bg cpu"

    invoke-virtual {v1, v13}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_c

    :goto_d
    if-ne v10, v13, :cond_1c

    sget-boolean v13, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v13, :cond_1b

    add-int/lit8 v14, v14, 0x1

    new-instance v13, Ljava/lang/StringBuilder;

    invoke-direct {v13}, Ljava/lang/StringBuilder;-><init>()V

    const-string v11, "  App partial wakelock: "

    invoke-virtual {v13, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual/range {v17 .. v17}, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;->getDetailName()Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v11, v12}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v0, v11}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->getLabelByPackageNames([Ljava/lang/String;)Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v13, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v13}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    const/4 v11, 0x2

    const/16 v13, 0xc

    goto :goto_e

    :cond_1b
    const/16 v13, 0xc

    :cond_1c
    if-ne v10, v13, :cond_1d

    sget-boolean v11, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v11, :cond_1d

    add-int/lit8 v14, v14, 0x1

    const-string v11, "  App partial wakelock"

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_1d
    const/4 v11, 0x2

    :goto_e
    if-ne v10, v11, :cond_1e

    add-int/lit8 v3, v3, 0x1

    const-string v11, "  High brightness"

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_1e
    const/4 v11, 0x5

    if-ne v10, v11, :cond_1f

    add-int/lit8 v7, v7, 0x1

    const-string v11, "  Kernel wakelock"

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_1f
    const/4 v11, 0x6

    if-ne v10, v11, :cond_20

    add-int/lit8 v8, v8, 0x1

    const-string v11, "  Kernel wakeup"

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_20
    const/4 v11, 0x1

    if-ne v10, v11, :cond_21

    add-int/lit8 v5, v5, 0x1

    const-string v11, "  Bad signal"

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_21
    const/16 v11, 0x64

    if-ne v10, v11, :cond_22

    if-nez v16, :cond_22

    add-int/lit8 v16, v16, 0x1

    :cond_22
    add-int/lit8 v15, v15, 0x1

    move v11, v13

    const/4 v10, 0x2

    const/16 v13, 0xb

    goto :goto_b

    :cond_23
    move v15, v3

    goto :goto_f

    :cond_24
    sget-object v0, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->TAG:Ljava/lang/String;

    const-string v3, "dump customer power info power is not checked"

    invoke-static {v0, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    move v5, v15

    move v7, v5

    move v8, v7

    move v9, v8

    move v14, v9

    const/16 v16, 0x1

    :goto_f
    if-nez v15, :cond_27

    if-nez v5, :cond_27

    if-nez v7, :cond_27

    if-nez v8, :cond_27

    if-nez v9, :cond_27

    if-eqz v14, :cond_25

    goto :goto_10

    :cond_25
    if-eqz v16, :cond_29

    if-nez v2, :cond_26

    const-string v0, "  TEST_CUSTOMER_POWER:NONE"

    invoke-virtual {v1, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    return-void

    :cond_26
    const/4 v8, 0x1

    if-ne v2, v8, :cond_29

    const-string v0, "  TEST_FACTORY_CUSTOMER_POWER:NONE"

    invoke-virtual {v1, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    return-void

    :cond_27
    :goto_10
    if-nez v2, :cond_28

    const-string v0, "  TEST_CUSTOMER_POWER:PASS"

    invoke-virtual {v1, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    return-void

    :cond_28
    const/4 v8, 0x1

    if-ne v2, v8, :cond_29

    const-string v0, "  TEST_FACTORY_CUSTOMER_POWER:PASS"

    invoke-virtual {v1, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_29
    :goto_11
    return-void
.end method""",
        'replacement': """.method private outputResultPassAndNone(Ljava/io/PrintWriter;I)V
    .registers 25

    move-object/from16 v0, p0

    move-object/from16 v1, p1

    move/from16 v2, p2

    iget-object v3, v0, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->mContext:Landroid/content/Context;

    invoke-static {v3}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;->getInstance(Landroid/content/Context;)Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;

    move-result-object v3

    const-string v4, "CustomerPowerRecordTable"

    invoke-virtual {v3, v4, v2}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;->query(Ljava/lang/String;I)Ljava/util/ArrayList;

    move-result-object v3

    invoke-virtual {v3}, Ljava/util/ArrayList;->size()I

    move-result v5

    iget-object v6, v0, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->mContext:Landroid/content/Context;

    invoke-static {v6}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;->getInstance(Landroid/content/Context;)Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;

    move-result-object v6

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v7

    invoke-virtual {v6, v4, v7, v8}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheckerDatabaseCrud;->queryAllByWeek(Ljava/lang/String;J)Ljava/util/ArrayList;

    move-result-object v4

    invoke-virtual {v4}, Ljava/util/ArrayList;->size()I

    move-result v6

    const/4 v10, 0x2

    const/16 v11, 0xc

    const-string v12, ","

    const/16 v13, 0xb

    const/4 v14, 0x1

    const/4 v15, 0x0

    if-nez v1, :cond_16

    :try_start_0
    invoke-static {}, Lcom/miui/powerkeeper/customerpower/CustomerPowerUtil;->isMaintenanceModeEnable()Z

    move-result v4

    invoke-direct {v0, v4}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->targetFilePath(Z)Ljava/lang/String;

    move-result-object v6

    if-eqz v6, :cond_0

    new-instance v7, Ljava/io/File;

    invoke-direct {v7, v6}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    goto :goto_0

    :catchall_0
    move-exception v0

    move-object v4, v1

    goto :goto_9

    :catch_0
    move-object v4, v1

    goto :goto_8

    :cond_0
    const/4 v7, 0x0

    :goto_0
    invoke-virtual {v7}, Ljava/io/File;->exists()Z

    move-result v6

    if-nez v6, :cond_1

    invoke-virtual {v7}, Ljava/io/File;->createNewFile()Z

    :cond_1
    if-eqz v4, :cond_2

    invoke-virtual {v7, v14, v15}, Ljava/io/File;->setWritable(ZZ)Z

    invoke-virtual {v7, v14, v15}, Ljava/io/File;->setReadable(ZZ)Z

    :cond_2
    new-instance v4, Ljava/io/PrintWriter;

    new-instance v6, Ljava/io/FileOutputStream;

    invoke-direct {v6, v7}, Ljava/io/FileOutputStream;-><init>(Ljava/io/File;)V

    invoke-direct {v4, v6}, Ljava/io/PrintWriter;-><init>(Ljava/io/OutputStream;)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    if-nez v2, :cond_3

    :try_start_1
    const-string v1, "TEST_CUSTOMER_POWER"

    invoke-virtual {v4, v1}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_1

    :catchall_1
    move-exception v0

    goto :goto_9

    :cond_3
    if-ne v2, v14, :cond_4

    const-string v1, "TEST_FACTORY_CUSTOMER_POWER"

    invoke-virtual {v4, v1}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_4
    :goto_1
    if-lez v5, :cond_f

    move v1, v15

    move v6, v1

    move v7, v6

    move/from16 v16, v7

    move/from16 v17, v16

    move/from16 v18, v17

    move/from16 v19, v18

    :goto_2
    if-ge v15, v5, :cond_e

    invoke-virtual {v3, v15}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v20

    check-cast v20, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;

    invoke-virtual/range {v20 .. v20}, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;->getType()I

    move-result v14

    if-ne v14, v13, :cond_5

    if-nez v17, :cond_5

    sget-boolean v21, Lmiui/os/Build;->IS_MIUI:Z

    if-nez v21, :cond_5

    add-int/lit8 v17, v17, 0x1

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v9, "App bg cpu: "

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual/range {v20 .. v20}, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;->getDetailName()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v9, v12}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v0, v9}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->getLabelByPackageNames([Ljava/lang/String;)Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_3

    :cond_5
    if-ne v14, v13, :cond_6

    if-nez v17, :cond_6

    sget-boolean v8, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz v8, :cond_6

    add-int/lit8 v17, v17, 0x1

    const-string v8, "App bg cpu"

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_6
    :goto_3
    if-ne v14, v11, :cond_7

    if-nez v18, :cond_7

    sget-boolean v8, Lmiui/os/Build;->IS_MIUI:Z

    if-nez v8, :cond_7

    add-int/lit8 v18, v18, 0x1

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v9, "App partial wakelock: "

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual/range {v20 .. v20}, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;->getDetailName()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v9, v12}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v0, v9}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->getLabelByPackageNames([Ljava/lang/String;)Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_4

    :cond_7
    if-ne v14, v11, :cond_8

    if-nez v18, :cond_8

    sget-boolean v8, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz v8, :cond_8

    add-int/lit8 v18, v18, 0x1

    const-string v8, "App partial wakelock"

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_8
    :goto_4
    if-ne v14, v10, :cond_9

    if-nez v1, :cond_9

    add-int/lit8 v1, v1, 0x1

    const-string v8, "High brightness"

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_9
    const/4 v8, 0x5

    if-ne v14, v8, :cond_a

    if-nez v7, :cond_a

    add-int/lit8 v7, v7, 0x1

    const-string v8, "Kernel wakelock"

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_a
    const/4 v8, 0x6

    if-ne v14, v8, :cond_b

    if-nez v16, :cond_b

    add-int/lit8 v16, v16, 0x1

    const-string v8, "Kernel wakeup"

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_b
    const/4 v8, 0x1

    if-ne v14, v8, :cond_c

    if-nez v6, :cond_c

    add-int/lit8 v6, v6, 0x1

    const-string v8, "Bad signal"

    invoke-virtual {v4, v8}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_c
    const/16 v8, 0x64

    if-ne v14, v8, :cond_d

    if-nez v19, :cond_d

    add-int/lit8 v19, v19, 0x1

    :cond_d
    add-int/lit8 v15, v15, 0x1

    const/4 v14, 0x1

    goto :goto_2

    :cond_e
    move v15, v1

    goto :goto_5

    :cond_f
    sget-object v0, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->TAG:Ljava/lang/String;

    const-string v1, "customer power info power is not checked"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    move v6, v15

    move v7, v6

    move/from16 v16, v7

    move/from16 v17, v16

    move/from16 v18, v17

    const/16 v19, 0x1

    :goto_5
    if-nez v15, :cond_12

    if-nez v6, :cond_12

    if-nez v7, :cond_12

    if-nez v16, :cond_12

    if-nez v17, :cond_12

    if-eqz v18, :cond_10

    goto :goto_6

    :cond_10
    if-eqz v19, :cond_14

    if-nez v2, :cond_11

    const-string v0, "TEST_CUSTOMER_POWER:NONE"

    invoke-virtual {v4, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_7

    :cond_11
    const/4 v8, 0x1

    if-ne v2, v8, :cond_14

    const-string v0, "TEST_FACTORY_CUSTOMER_POWER:NONE"

    invoke-virtual {v4, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_7

    :cond_12
    :goto_6
    if-nez v2, :cond_13

    const-string v0, "TEST_CUSTOMER_POWER:PASS"

    invoke-virtual {v4, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_7

    :cond_13
    const/4 v8, 0x1

    if-ne v2, v8, :cond_14

    const-string v0, "TEST_FACTORY_CUSTOMER_POWER:PASS"

    invoke-virtual {v4, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    :cond_14
    :goto_7
    invoke-virtual {v4}, Ljava/io/PrintWriter;->close()V

    goto :goto_11

    :catch_1
    :goto_8
    :try_start_2
    sget-object v0, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->TAG:Ljava/lang/String;

    const-string v1, "customer power info create autotestfile or write file failed"

    invoke-static {v0, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    if-eqz v4, :cond_29

    goto :goto_7

    :goto_9
    if-eqz v4, :cond_15

    invoke-virtual {v4}, Ljava/io/PrintWriter;->close()V

    :cond_15
    throw v0

    :cond_16
    if-nez v2, :cond_17

    const-string v3, "  TEST_CUSTOMER_POWER"

    invoke-virtual {v1, v3}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_a

    :cond_17
    const/4 v8, 0x1

    if-ne v2, v8, :cond_18

    const-string v3, "  TEST_FACTORY_CUSTOMER_POWER"

    invoke-virtual {v1, v3}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_18
    :goto_a
    if-lez v6, :cond_24

    move v3, v15

    move v5, v3

    move v7, v5

    move v8, v7

    move v9, v8

    move v14, v9

    move/from16 v16, v14

    :goto_b
    if-ge v15, v6, :cond_23

    invoke-virtual {v4, v15}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v17

    check-cast v17, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;

    invoke-virtual/range {v17 .. v17}, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;->getType()I

    move-result v10

    if-ne v10, v13, :cond_1a

    sget-boolean v19, Lmiui/os/Build;->IS_MIUI:Z

    if-nez v19, :cond_1a

    add-int/lit8 v9, v9, 0x1

    new-instance v11, Ljava/lang/StringBuilder;

    invoke-direct {v11}, Ljava/lang/StringBuilder;-><init>()V

    const-string v13, "  App bg cpu: "

    invoke-virtual {v11, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual/range {v17 .. v17}, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;->getDetailName()Ljava/lang/String;

    move-result-object v13

    invoke-virtual {v13, v12}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v13

    invoke-virtual {v0, v13}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->getLabelByPackageNames([Ljava/lang/String;)Ljava/lang/String;

    move-result-object v13

    invoke-virtual {v11, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v11}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    const/16 v11, 0xb

    :cond_19
    :goto_c
    const/16 v13, 0xc

    goto :goto_d

    :cond_1a
    move v11, v13

    if-ne v10, v11, :cond_19

    sget-boolean v13, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz v13, :cond_19

    add-int/lit8 v9, v9, 0x1

    const-string v13, "  App bg cpu"

    invoke-virtual {v1, v13}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    goto :goto_c

    :goto_d
    if-ne v10, v13, :cond_1c

    sget-boolean v13, Lmiui/os/Build;->IS_MIUI:Z

    if-nez v13, :cond_1b

    add-int/lit8 v14, v14, 0x1

    new-instance v13, Ljava/lang/StringBuilder;

    invoke-direct {v13}, Ljava/lang/StringBuilder;-><init>()V

    const-string v11, "  App partial wakelock: "

    invoke-virtual {v13, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual/range {v17 .. v17}, Lcom/miui/powerkeeper/customerpower/CustomerPowerResultBean;->getDetailName()Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v11, v12}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v0, v11}, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->getLabelByPackageNames([Ljava/lang/String;)Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v13, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v13}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    const/4 v11, 0x2

    const/16 v13, 0xc

    goto :goto_e

    :cond_1b
    const/16 v13, 0xc

    :cond_1c
    if-ne v10, v13, :cond_1d

    sget-boolean v11, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz v11, :cond_1d

    add-int/lit8 v14, v14, 0x1

    const-string v11, "  App partial wakelock"

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_1d
    const/4 v11, 0x2

    :goto_e
    if-ne v10, v11, :cond_1e

    add-int/lit8 v3, v3, 0x1

    const-string v11, "  High brightness"

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_1e
    const/4 v11, 0x5

    if-ne v10, v11, :cond_1f

    add-int/lit8 v7, v7, 0x1

    const-string v11, "  Kernel wakelock"

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_1f
    const/4 v11, 0x6

    if-ne v10, v11, :cond_20

    add-int/lit8 v8, v8, 0x1

    const-string v11, "  Kernel wakeup"

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_20
    const/4 v11, 0x1

    if-ne v10, v11, :cond_21

    add-int/lit8 v5, v5, 0x1

    const-string v11, "  Bad signal"

    invoke-virtual {v1, v11}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_21
    const/16 v11, 0x64

    if-ne v10, v11, :cond_22

    if-nez v16, :cond_22

    add-int/lit8 v16, v16, 0x1

    :cond_22
    add-int/lit8 v15, v15, 0x1

    move v11, v13

    const/4 v10, 0x2

    const/16 v13, 0xb

    goto :goto_b

    :cond_23
    move v15, v3

    goto :goto_f

    :cond_24
    sget-object v0, Lcom/miui/powerkeeper/customerpower/CustomerPowerCheck;->TAG:Ljava/lang/String;

    const-string v3, "dump customer power info power is not checked"

    invoke-static {v0, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    move v5, v15

    move v7, v5

    move v8, v7

    move v9, v8

    move v14, v9

    const/16 v16, 0x1

    :goto_f
    if-nez v15, :cond_27

    if-nez v5, :cond_27

    if-nez v7, :cond_27

    if-nez v8, :cond_27

    if-nez v9, :cond_27

    if-eqz v14, :cond_25

    goto :goto_10

    :cond_25
    if-eqz v16, :cond_29

    if-nez v2, :cond_26

    const-string v0, "  TEST_CUSTOMER_POWER:NONE"

    invoke-virtual {v1, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    return-void

    :cond_26
    const/4 v8, 0x1

    if-ne v2, v8, :cond_29

    const-string v0, "  TEST_FACTORY_CUSTOMER_POWER:NONE"

    invoke-virtual {v1, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    return-void

    :cond_27
    :goto_10
    if-nez v2, :cond_28

    const-string v0, "  TEST_CUSTOMER_POWER:PASS"

    invoke-virtual {v1, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    return-void

    :cond_28
    const/4 v8, 0x1

    if-ne v2, v8, :cond_29

    const-string v0, "  TEST_FACTORY_CUSTOMER_POWER:PASS"

    invoke-virtual {v1, v0}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_29
    :goto_11
    return-void
.end method""",
        'required': True,
        'flag_rewrite_count': 8,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
