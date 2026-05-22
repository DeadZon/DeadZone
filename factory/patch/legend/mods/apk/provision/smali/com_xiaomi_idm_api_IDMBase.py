TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/api/IDMBase.smali'
CLASS_FALLBACK_NAMES = ['IDMBase.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final Companion:Lcom/xiaomi/idm/api/IDMBase$Companion;', '.method public static final synthetic access$getProcessCallback$p(Lcom/xiaomi/idm/api/IDMBase;)Lcom/xiaomi/idm/api/IDMProcessCallback;', '.method public static final synthetic access$setServiceApiVersion$p(Lcom/xiaomi/idm/api/IDMBase;I)V', '.method public static final synthetic access$set_iMiConnect$p(Lcom/xiaomi/idm/api/IDMBase;Lcom/xiaomi/mi_connect_service/IMiConnect;)V', '.method public static final synthetic access$unbindService(Lcom/xiaomi/idm/api/IDMBase;)V']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_api_IDMBase__doDestroy',
        'method': '.method protected doDestroy()V',
        'method_name': 'doDestroy',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected doDestroy()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected doDestroy()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_xiaomi_idm_api_IDMBase__getIMiConnect',
        'method': '.method protected final getIMiConnect()Lcom/xiaomi/mi_connect_service/IMiConnect;',
        'method_name': 'getIMiConnect',
        'method_anchors': ['iget-object p0, p0, Lcom/xiaomi/idm/api/IDMBase;->_iMiConnect:Lcom/xiaomi/mi_connect_service/IMiConnect;', 'if-nez p0, :cond_0', 'const-string v0, "IDMBase"', 'const-string v1, "IMiConnect null calling"', 'invoke-static {v0, v1, p0}, Lcom/xiaomi/idm/util/LogUtil;->e(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V', 'new-instance p0, Lcom/xiaomi/mi_connect_service/IMiConnect$Default;', 'invoke-direct {p0}, Lcom/xiaomi/mi_connect_service/IMiConnect$Default;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected final getIMiConnect()Lcom/xiaomi/mi_connect_service/IMiConnect;
    .registers 3

    iget-object p0, p0, Lcom/xiaomi/idm/api/IDMBase;->_iMiConnect:Lcom/xiaomi/mi_connect_service/IMiConnect;

    if-nez p0, :cond_0

    const/4 p0, 0x0

    new-array p0, p0, [Ljava/lang/Object;

    const-string v0, "IDMBase"

    const-string v1, "IMiConnect null calling"

    invoke-static {v0, v1, p0}, Lcom/xiaomi/idm/util/LogUtil;->e(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    new-instance p0, Lcom/xiaomi/mi_connect_service/IMiConnect$Default;

    invoke-direct {p0}, Lcom/xiaomi/mi_connect_service/IMiConnect$Default;-><init>()V

    return-object p0

    :cond_0
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    return-object p0
.end method""",
        'replacement': """.method protected final getIMiConnect()Lcom/xiaomi/mi_connect_service/IMiConnect;
    .registers 3

    goto :goto_9

    nop

    :goto_0
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    goto :goto_2

    nop

    :goto_1
    const-string v1, "IMiConnect null calling"

    goto :goto_b

    nop

    :goto_2
    return-object p0

    :goto_3
    if-eqz p0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_c

    nop

    :goto_4
    const-string v0, "IDMBase"

    goto :goto_1

    nop

    :goto_5
    new-instance p0, Lcom/xiaomi/mi_connect_service/IMiConnect$Default;

    goto :goto_6

    nop

    :goto_6
    invoke-direct {p0}, Lcom/xiaomi/mi_connect_service/IMiConnect$Default;-><init>()V

    goto :goto_7

    nop

    :goto_7
    return-object p0

    :goto_8
    goto :goto_0

    nop

    :goto_9
    iget-object p0, p0, Lcom/xiaomi/idm/api/IDMBase;->_iMiConnect:Lcom/xiaomi/mi_connect_service/IMiConnect;

    goto :goto_3

    nop

    :goto_a
    new-array p0, p0, [Ljava/lang/Object;

    goto :goto_4

    nop

    :goto_b
    invoke-static {v0, v1, p0}, Lcom/xiaomi/idm/util/LogUtil;->e(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_5

    nop

    :goto_c
    const/4 p0, 0x0

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_xiaomi_idm_api_IDMBase__getNextRequestId',
        'method': '.method protected final getNextRequestId()Ljava/lang/String;',
        'method_name': 'getNextRequestId',
        'method_anchors': ['iget-object p0, p0, Lcom/xiaomi/idm/api/IDMBase;->atomicLong:Ljava/util/concurrent/atomic/AtomicLong;', 'invoke-virtual {p0}, Ljava/util/concurrent/atomic/AtomicLong;->incrementAndGet()J', 'invoke-static {v0, v1}, Ljava/lang/String;->valueOf(J)Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected final getNextRequestId()Ljava/lang/String;
    .registers 3

    iget-object p0, p0, Lcom/xiaomi/idm/api/IDMBase;->atomicLong:Ljava/util/concurrent/atomic/AtomicLong;

    invoke-virtual {p0}, Ljava/util/concurrent/atomic/AtomicLong;->incrementAndGet()J

    move-result-wide v0

    invoke-static {v0, v1}, Ljava/lang/String;->valueOf(J)Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected final getNextRequestId()Ljava/lang/String;
    .registers 3

    goto :goto_3

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0}, Ljava/util/concurrent/atomic/AtomicLong;->incrementAndGet()J

    move-result-wide v0

    goto :goto_2

    nop

    :goto_2
    invoke-static {v0, v1}, Ljava/lang/String;->valueOf(J)Ljava/lang/String;

    move-result-object p0

    goto :goto_0

    nop

    :goto_3
    iget-object p0, p0, Lcom/xiaomi/idm/api/IDMBase;->atomicLong:Ljava/util/concurrent/atomic/AtomicLong;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
