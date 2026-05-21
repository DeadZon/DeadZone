TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration.smali'
CLASS_FALLBACK_NAMES = ['IPCParam$SendBlockConfiguration.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field public static final CLIENTID_FIELD_NUMBER:I = 0x1', '.field private static final DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;', '.field public static final MAXPARALLELTASK_FIELD_NUMBER:I = 0x4', '.field public static final SERVICEID_FIELD_NUMBER:I = 0x2']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_compat_proto_IPCParam__SendBlockConfiguration__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->PARSER:Lcom/google/protobuf/Parser;'],
        'type': 'method_replace',
        'search': """.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .registers 5

    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    aget p0, p0, p1

    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    new-instance p0, Ljava/lang/UnsupportedOperationException;

    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    throw p0

    :pswitch_0  #0x7
    return-object p1

    :pswitch_1  #0x6
    const/4 p0, 0x1

    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    return-object p0

    :pswitch_2  #0x5
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_0

    :catchall_0
    move-exception p0

    goto :goto_1

    :cond_0
    :goto_0
    monitor-exit p1

    return-object p0

    :goto_1
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw p0

    :cond_1
    return-object p0

    :pswitch_3  #0x4
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;

    return-object p0

    :pswitch_4  #0x3
    const-string p0, "clientId_"

    const-string p1, "serviceId_"

    const-string p2, "sizePerPacket_"

    const-string p3, "maxParallelTask_"

    const-string v0, "timeout_"

    filled-new-array {p0, p1, p2, p3, v0}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\u0005\u0000\u0000\u0001\u0005\u0005\u0000\u0000\u0000\u0001Ȉ\u0002Ȉ\u0003\u0004\u0004\u0004\u0005\u0002"

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;

    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;-><init>()V

    return-object p0

    nop

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_6  #00000001
        :pswitch_5  #00000002
        :pswitch_4  #00000003
        :pswitch_3  #00000004
        :pswitch_2  #00000005
        :pswitch_1  #00000006
        :pswitch_0  #00000007
    .end packed-switch
.end method""",
        'replacement': """.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .registers 5

    goto :goto_1e

    nop

    :goto_0
    filled-new-array {p0, p1, p2, p3, v0}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_20

    nop

    :goto_1
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_9

    nop

    :goto_2
    if-eqz p0, :cond_0

    goto :goto_1c

    :cond_0
    goto :goto_5

    nop

    :goto_3
    const-string v0, "timeout_"

    goto :goto_0

    nop

    :goto_4
    const-string p3, "maxParallelTask_"

    goto :goto_3

    nop

    :goto_5
    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;

    goto :goto_21

    nop

    :goto_6
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    goto :goto_17

    nop

    :goto_7
    return-object p0

    nop

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_4  #00000001
        :pswitch_1  #00000002
        :pswitch_3  #00000003
        :pswitch_6  #00000004
        :pswitch_2  #00000005
        :pswitch_0  #00000006
        :pswitch_5  #00000007
    .end packed-switch

    :goto_8
    const-string p1, "serviceId_"

    goto :goto_c

    nop

    :goto_9
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_18

    nop

    :goto_a
    return-object p1

    :pswitch_0  #0x6
    goto :goto_11

    nop

    :goto_b
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_2

    nop

    :goto_c
    const-string p2, "sizePerPacket_"

    goto :goto_4

    nop

    :goto_d
    return-object p0

    :pswitch_1  #0x2
    goto :goto_13

    nop

    :goto_e
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_1

    nop

    :goto_f
    return-object p0

    :pswitch_2  #0x5
    goto :goto_b

    nop

    :goto_10
    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;-><init>()V

    goto :goto_7

    nop

    :goto_11
    const/4 p0, 0x1

    goto :goto_25

    nop

    :goto_12
    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;

    goto :goto_14

    nop

    :goto_13
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration$Builder;

    goto :goto_6

    nop

    :goto_14
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_d

    nop

    :goto_15
    return-object p0

    :pswitch_3  #0x3
    goto :goto_24

    nop

    :goto_16
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;

    goto :goto_10

    nop

    :goto_17
    return-object p0

    :pswitch_4  #0x1
    goto :goto_16

    nop

    :goto_18
    throw p0

    :pswitch_5  #0x7
    goto :goto_a

    nop

    :goto_19
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;

    goto :goto_15

    nop

    :goto_1a
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_1d

    nop

    :goto_1b
    throw p0

    :goto_1c
    goto :goto_1f

    nop

    :goto_1d
    aget p0, p0, p1

    goto :goto_e

    nop

    :goto_1e
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_1a

    nop

    :goto_1f
    return-object p0

    :pswitch_6  #0x4
    goto :goto_19

    nop

    :goto_20
    const-string p1, "\u0000\u0005\u0000\u0000\u0001\u0005\u0005\u0000\u0000\u0000\u0001Ȉ\u0002Ȉ\u0003\u0004\u0004\u0004\u0005\u0002"

    goto :goto_12

    nop

    :goto_21
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$SendBlockConfiguration;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_22

    :catchall_0
    move-exception p0

    goto :goto_23

    :cond_1
    :goto_22
    monitor-exit p1

    return-object p0

    :goto_23
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1b

    nop

    :goto_24
    const-string p0, "clientId_"

    goto :goto_8

    nop

    :goto_25
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_f

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
