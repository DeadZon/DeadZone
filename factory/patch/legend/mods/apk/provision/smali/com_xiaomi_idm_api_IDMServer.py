TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/api/IDMServer.smali'
CLASS_FALLBACK_NAMES = ['IDMServer.smali']
CLASS_ANCHORS = ['.super Lcom/xiaomi/idm/api/IDMBase;']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_api_IDMServer__doDestroy',
        'method': '.method protected doDestroy()V',
        'method_name': 'doDestroy',
        'method_anchors': ['new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v1, "Id["', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getClientId()Ljava/lang/String;', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'const-string v1, "]: doDestroy"', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method protected doDestroy()V
    .registers 4

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "Id["

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getClientId()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v1, "]: doDestroy"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const/4 v1, 0x0

    new-array v1, v1, [Ljava/lang/Object;

    const-string v2, "IDMServer"

    invoke-static {v2, v0, v1}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->serviceAvailable()Z

    move-result v0

    if-eqz v0, :cond_0

    :try_start_0
    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getIMiConnect()Lcom/xiaomi/mi_connect_service/IMiConnect;

    move-result-object v0

    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getClientId()Ljava/lang/String;

    move-result-object v1

    invoke-interface {v0, v1}, Lcom/xiaomi/mi_connect_service/IMiConnect;->unregisterProc(Ljava/lang/String;)I
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception v0

    invoke-virtual {v0}, Landroid/os/RemoteException;->getMessage()Ljava/lang/String;

    move-result-object v1

    invoke-static {v2, v1, v0}, Lcom/xiaomi/idm/util/LogUtil;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V

    :cond_0
    :goto_0
    iget-object v0, p0, Lcom/xiaomi/idm/api/IDMServer;->mRegisteredServices:Ljava/util/Map;

    invoke-interface {v0}, Ljava/util/Map;->clear()V

    iget-object v0, p0, Lcom/xiaomi/idm/api/IDMServer;->mEventCalls:Ljava/util/concurrent/ConcurrentHashMap;

    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentHashMap;->clear()V

    invoke-super {p0}, Lcom/xiaomi/idm/api/IDMBase;->doDestroy()V

    return-void
.end method""",
        'replacement': """.method protected doDestroy()V
    .registers 4

    goto :goto_c

    nop

    :goto_0
    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getClientId()Ljava/lang/String;

    move-result-object v1

    goto :goto_7

    nop

    :goto_1
    const/4 v1, 0x0

    goto :goto_17

    nop

    :goto_2
    const-string v2, "IDMServer"

    goto :goto_3

    nop

    :goto_3
    invoke-static {v2, v0, v1}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_e

    nop

    :goto_4
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_1

    nop

    :goto_5
    const-string v1, "]: doDestroy"

    goto :goto_6

    nop

    :goto_6
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_4

    nop

    :goto_7
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_5

    nop

    :goto_8
    goto :goto_13

    :catch_0
    move-exception v0

    goto :goto_10

    nop

    :goto_9
    invoke-interface {v0}, Ljava/util/Map;->clear()V

    goto :goto_14

    nop

    :goto_a
    iget-object v0, p0, Lcom/xiaomi/idm/api/IDMServer;->mRegisteredServices:Ljava/util/Map;

    goto :goto_9

    nop

    :goto_b
    if-nez v0, :cond_0

    goto :goto_13

    :cond_0
    :try_start_0
    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getIMiConnect()Lcom/xiaomi/mi_connect_service/IMiConnect;

    move-result-object v0

    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getClientId()Ljava/lang/String;

    move-result-object v1

    invoke-interface {v0, v1}, Lcom/xiaomi/mi_connect_service/IMiConnect;->unregisterProc(Ljava/lang/String;)I
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_8

    nop

    :goto_c
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_f

    nop

    :goto_d
    const-string v1, "Id["

    goto :goto_15

    nop

    :goto_e
    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->serviceAvailable()Z

    move-result v0

    goto :goto_b

    nop

    :goto_f
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_d

    nop

    :goto_10
    invoke-virtual {v0}, Landroid/os/RemoteException;->getMessage()Ljava/lang/String;

    move-result-object v1

    goto :goto_12

    nop

    :goto_11
    invoke-super {p0}, Lcom/xiaomi/idm/api/IDMBase;->doDestroy()V

    goto :goto_16

    nop

    :goto_12
    invoke-static {v2, v1, v0}, Lcom/xiaomi/idm/util/LogUtil;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V

    :goto_13
    goto :goto_a

    nop

    :goto_14
    iget-object v0, p0, Lcom/xiaomi/idm/api/IDMServer;->mEventCalls:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_18

    nop

    :goto_15
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    nop

    :goto_16
    return-void

    :goto_17
    new-array v1, v1, [Ljava/lang/Object;

    goto :goto_2

    nop

    :goto_18
    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentHashMap;->clear()V

    goto :goto_11

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
