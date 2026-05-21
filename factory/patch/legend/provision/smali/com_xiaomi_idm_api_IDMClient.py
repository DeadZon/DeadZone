TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/api/IDMClient.smali'
CLASS_FALLBACK_NAMES = ['IDMClient.smali']
CLASS_ANCHORS = ['.super Lcom/xiaomi/idm/api/IDMBase;']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_api_IDMClient__doDestroy',
        'method': '.method protected doDestroy()V',
        'method_name': 'doDestroy',
        'method_anchors': ['new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v1, "Id["', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getClientId()Ljava/lang/String;', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'const-string v1, "]: doDestroy"', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method protected doDestroy()V
    .registers 5

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

    const-string v2, "IDMClient"

    invoke-static {v2, v0, v1}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->serviceAvailable()Z

    move-result v0

    if-eqz v0, :cond_0

    :try_start_0
    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getIMiConnect()Lcom/xiaomi/mi_connect_service/IMiConnect;

    move-result-object v0

    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getClientId()Ljava/lang/String;

    move-result-object v1

    invoke-interface {v0, v1}, Lcom/xiaomi/mi_connect_service/IMiConnect;->unregisterIDMClient(Ljava/lang/String;)I
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception v0

    invoke-virtual {v0}, Landroid/os/RemoteException;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v2, v1, v0}, Lcom/xiaomi/idm/util/LogUtil;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V

    :cond_0
    :goto_0
    iget-object v0, p0, Lcom/xiaomi/idm/api/IDMClient;->mRmiCalls:Ljava/util/concurrent/ConcurrentHashMap;

    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;

    move-result-object v0

    invoke-interface {v0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_1
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_1

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/xiaomi/idm/api/IDMClient$RmiCall;

    iget-object v1, v1, Lcom/xiaomi/idm/api/IDMClient$RmiCall;->future:Lcom/xiaomi/idm/task/CallFuture;

    new-instance v2, Lcom/xiaomi/idm/exception/RequestException;

    sget-object v3, Lcom/xiaomi/idm/constant/ResponseCode$RequestCode;->ERR_CLIENT_DESTROYED:Lcom/xiaomi/idm/constant/ResponseCode$RequestCode;

    invoke-direct {v2, v3}, Lcom/xiaomi/idm/exception/RequestException;-><init>(Lcom/xiaomi/idm/constant/ResponseCode$RequestCode;)V

    invoke-virtual {v1, v2}, Lcom/xiaomi/idm/task/CallFuture;->setFailed(Ljava/lang/Throwable;)Lcom/xiaomi/idm/task/CallFuture;

    goto :goto_1

    :cond_1
    iget-object v0, p0, Lcom/xiaomi/idm/api/IDMClient;->mSubsEventCalls:Ljava/util/concurrent/ConcurrentHashMap;

    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;

    move-result-object v0

    invoke-interface {v0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_2
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_2

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/xiaomi/idm/api/IDMClient$SubsEventCall;

    iget-object v1, v1, Lcom/xiaomi/idm/api/IDMClient$SubsEventCall;->future:Lcom/xiaomi/idm/task/CallFuture;

    new-instance v2, Lcom/xiaomi/idm/exception/SubsEventException;

    sget-object v3, Lcom/xiaomi/idm/constant/ResponseCode$SubsEventCode;->SUBS_EVENT_ERR_CLIENT_DESTROYED:Lcom/xiaomi/idm/constant/ResponseCode$SubsEventCode;

    invoke-direct {v2, v3}, Lcom/xiaomi/idm/exception/SubsEventException;-><init>(Lcom/xiaomi/idm/constant/ResponseCode$SubsEventCode;)V

    invoke-virtual {v1, v2}, Lcom/xiaomi/idm/task/CallFuture;->setFailed(Ljava/lang/Throwable;)Lcom/xiaomi/idm/task/CallFuture;

    goto :goto_2

    :cond_2
    invoke-super {p0}, Lcom/xiaomi/idm/api/IDMBase;->doDestroy()V

    return-void
.end method""",
        'replacement': """.method protected doDestroy()V
    .registers 5

    goto :goto_1e

    nop

    :goto_0
    goto :goto_27

    :goto_1
    goto :goto_f

    nop

    :goto_2
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_1c

    nop

    :goto_3
    new-instance v2, Lcom/xiaomi/idm/exception/RequestException;

    goto :goto_18

    nop

    :goto_4
    invoke-direct {v2, v3}, Lcom/xiaomi/idm/exception/RequestException;-><init>(Lcom/xiaomi/idm/constant/ResponseCode$RequestCode;)V

    goto :goto_29

    nop

    :goto_5
    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->serviceAvailable()Z

    move-result v0

    goto :goto_20

    nop

    :goto_6
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1b

    nop

    :goto_7
    invoke-static {v2, v1, v0}, Lcom/xiaomi/idm/util/LogUtil;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V

    :goto_8
    goto :goto_30

    nop

    :goto_9
    invoke-virtual {v0}, Landroid/os/RemoteException;->toString()Ljava/lang/String;

    move-result-object v1

    goto :goto_7

    nop

    :goto_a
    goto :goto_8

    :catch_0
    move-exception v0

    goto :goto_9

    nop

    :goto_b
    invoke-direct {v2, v3}, Lcom/xiaomi/idm/exception/SubsEventException;-><init>(Lcom/xiaomi/idm/constant/ResponseCode$SubsEventCode;)V

    goto :goto_25

    nop

    :goto_c
    invoke-super {p0}, Lcom/xiaomi/idm/api/IDMBase;->doDestroy()V

    goto :goto_17

    nop

    :goto_d
    new-array v1, v1, [Ljava/lang/Object;

    goto :goto_14

    nop

    :goto_e
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_15

    nop

    :goto_f
    iget-object v0, p0, Lcom/xiaomi/idm/api/IDMClient;->mSubsEventCalls:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_10

    nop

    :goto_10
    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;

    move-result-object v0

    goto :goto_31

    nop

    :goto_11
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2b

    nop

    :goto_12
    invoke-static {v2, v0, v1}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_5

    nop

    :goto_13
    const-string v1, "]: doDestroy"

    goto :goto_6

    nop

    :goto_14
    const-string v2, "IDMClient"

    goto :goto_12

    nop

    :goto_15
    const-string v1, "Id["

    goto :goto_11

    nop

    :goto_16
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_19

    nop

    :goto_17
    return-void

    :goto_18
    sget-object v3, Lcom/xiaomi/idm/constant/ResponseCode$RequestCode;->ERR_CLIENT_DESTROYED:Lcom/xiaomi/idm/constant/ResponseCode$RequestCode;

    goto :goto_4

    nop

    :goto_19
    if-nez v1, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_24

    nop

    :goto_1a
    check-cast v1, Lcom/xiaomi/idm/api/IDMClient$SubsEventCall;

    goto :goto_23

    nop

    :goto_1b
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_1d

    nop

    :goto_1c
    if-nez v1, :cond_1

    goto :goto_2e

    :cond_1
    goto :goto_28

    nop

    :goto_1d
    const/4 v1, 0x0

    goto :goto_d

    nop

    :goto_1e
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_e

    nop

    :goto_1f
    check-cast v1, Lcom/xiaomi/idm/api/IDMClient$RmiCall;

    goto :goto_2c

    nop

    :goto_20
    if-nez v0, :cond_2

    goto :goto_8

    :cond_2
    :try_start_0
    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getIMiConnect()Lcom/xiaomi/mi_connect_service/IMiConnect;

    move-result-object v0

    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getClientId()Ljava/lang/String;

    move-result-object v1

    invoke-interface {v0, v1}, Lcom/xiaomi/mi_connect_service/IMiConnect;->unregisterIDMClient(Ljava/lang/String;)I
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_a

    nop

    :goto_21
    new-instance v2, Lcom/xiaomi/idm/exception/SubsEventException;

    goto :goto_22

    nop

    :goto_22
    sget-object v3, Lcom/xiaomi/idm/constant/ResponseCode$SubsEventCode;->SUBS_EVENT_ERR_CLIENT_DESTROYED:Lcom/xiaomi/idm/constant/ResponseCode$SubsEventCode;

    goto :goto_b

    nop

    :goto_23
    iget-object v1, v1, Lcom/xiaomi/idm/api/IDMClient$SubsEventCall;->future:Lcom/xiaomi/idm/task/CallFuture;

    goto :goto_21

    nop

    :goto_24
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_1f

    nop

    :goto_25
    invoke-virtual {v1, v2}, Lcom/xiaomi/idm/task/CallFuture;->setFailed(Ljava/lang/Throwable;)Lcom/xiaomi/idm/task/CallFuture;

    goto :goto_2d

    nop

    :goto_26
    invoke-interface {v0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_27
    goto :goto_16

    nop

    :goto_28
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_1a

    nop

    :goto_29
    invoke-virtual {v1, v2}, Lcom/xiaomi/idm/task/CallFuture;->setFailed(Ljava/lang/Throwable;)Lcom/xiaomi/idm/task/CallFuture;

    goto :goto_0

    nop

    :goto_2a
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_13

    nop

    :goto_2b
    invoke-virtual {p0}, Lcom/xiaomi/idm/api/IDMBase;->getClientId()Ljava/lang/String;

    move-result-object v1

    goto :goto_2a

    nop

    :goto_2c
    iget-object v1, v1, Lcom/xiaomi/idm/api/IDMClient$RmiCall;->future:Lcom/xiaomi/idm/task/CallFuture;

    goto :goto_3

    nop

    :goto_2d
    goto :goto_32

    :goto_2e
    goto :goto_c

    nop

    :goto_2f
    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;

    move-result-object v0

    goto :goto_26

    nop

    :goto_30
    iget-object v0, p0, Lcom/xiaomi/idm/api/IDMClient;->mRmiCalls:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_2f

    nop

    :goto_31
    invoke-interface {v0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_32
    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
