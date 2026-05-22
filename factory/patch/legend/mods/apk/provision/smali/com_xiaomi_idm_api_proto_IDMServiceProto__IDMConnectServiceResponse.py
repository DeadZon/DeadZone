TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse.smali'
CLASS_FALLBACK_NAMES = ['IDMServiceProto$IDMConnectServiceResponse.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field public static final CLIENTID_FIELD_NUMBER:I = 0x5', '.field public static final CONNLEVEL_FIELD_NUMBER:I = 0x6', '.field public static final CONNPARAM_FIELD_NUMBER:I = 0x4', '.field private static final DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_api_proto_IDMServiceProto__IDMConnectServiceResponse__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->PARSER:Lcom/google/protobuf/Parser;'],
        'type': 'method_replace',
        'search': """.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .registers 10

    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

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
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_0

    :catchall_0
    move-exception v0

    move-object p0, v0

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
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;

    return-object p0

    :pswitch_4  #0x3
    const-string v0, "status_"

    const-string v1, "serviceId_"

    const-string v2, "endpoint_"

    const-string v3, "connParam_"

    const-string v4, "clientId_"

    const-string v5, "connLevel_"

    filled-new-array/range {v0 .. v5}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\u0006\u0000\u0000\u0001\u0006\u0006\u0000\u0000\u0000\u0001\u0004\u0002Ȉ\u0003\t\u0004\t\u0005Ȉ\u0006\u0004"

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;

    invoke-direct {p0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;-><init>()V

    return-object p0

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
    .registers 10

    goto :goto_1f

    nop

    :goto_0
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    goto :goto_1c

    nop

    :goto_1
    invoke-direct {p0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;-><init>()V

    goto :goto_3

    nop

    :goto_2
    const-string v3, "connParam_"

    goto :goto_7

    nop

    :goto_3
    return-object p0

    nop

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_4  #00000001
        :pswitch_1  #00000002
        :pswitch_3  #00000003
        :pswitch_5  #00000004
        :pswitch_2  #00000005
        :pswitch_0  #00000006
        :pswitch_6  #00000007
    .end packed-switch

    :goto_4
    const-string v0, "status_"

    goto :goto_a

    nop

    :goto_5
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_19

    nop

    :goto_6
    const-string p1, "\u0000\u0006\u0000\u0000\u0001\u0006\u0006\u0000\u0000\u0000\u0001\u0004\u0002Ȉ\u0003\t\u0004\t\u0005Ȉ\u0006\u0004"

    goto :goto_9

    nop

    :goto_7
    const-string v4, "clientId_"

    goto :goto_16

    nop

    :goto_8
    return-object p1

    :pswitch_0  #0x6
    goto :goto_15

    nop

    :goto_9
    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;

    goto :goto_18

    nop

    :goto_a
    const-string v1, "serviceId_"

    goto :goto_13

    nop

    :goto_b
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_22

    nop

    :goto_c
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_b

    nop

    :goto_d
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_11

    nop

    :goto_e
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse$Builder;

    goto :goto_0

    nop

    :goto_f
    return-object p0

    :pswitch_1  #0x2
    goto :goto_e

    nop

    :goto_10
    return-object p0

    :pswitch_2  #0x5
    goto :goto_5

    nop

    :goto_11
    aget p0, p0, p1

    goto :goto_1e

    nop

    :goto_12
    const-class p1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;

    goto :goto_24

    nop

    :goto_13
    const-string v2, "endpoint_"

    goto :goto_2

    nop

    :goto_14
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;

    goto :goto_17

    nop

    :goto_15
    const/4 p0, 0x1

    goto :goto_21

    nop

    :goto_16
    const-string v5, "connLevel_"

    goto :goto_1d

    nop

    :goto_17
    return-object p0

    :pswitch_3  #0x3
    goto :goto_4

    nop

    :goto_18
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_f

    nop

    :goto_19
    if-eqz p0, :cond_0

    goto :goto_1b

    :cond_0
    goto :goto_12

    nop

    :goto_1a
    throw p0

    :goto_1b
    goto :goto_20

    nop

    :goto_1c
    return-object p0

    :pswitch_4  #0x1
    goto :goto_23

    nop

    :goto_1d
    filled-new-array/range {v0 .. v5}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_6

    nop

    :goto_1e
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_c

    nop

    :goto_1f
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_d

    nop

    :goto_20
    return-object p0

    :pswitch_5  #0x4
    goto :goto_14

    nop

    :goto_21
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_10

    nop

    :goto_22
    throw p0

    :pswitch_6  #0x7
    goto :goto_8

    nop

    :goto_23
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;

    goto :goto_1

    nop

    :goto_24
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceResponse;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_25

    :catchall_0
    move-exception v0

    move-object p0, v0

    goto :goto_26

    :cond_1
    :goto_25
    monitor-exit p1

    return-object p0

    :goto_26
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
