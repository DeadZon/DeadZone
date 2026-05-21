TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest.smali'
CLASS_FALLBACK_NAMES = ['IDMServiceProto$IDMConnectServiceRequest.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field public static final CLIENTID_FIELD_NUMBER:I = 0x5', '.field public static final CONNPARAM_FIELD_NUMBER:I = 0x4', '.field private static final DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;', '.field public static final ENDPOINT_FIELD_NUMBER:I = 0x3']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_api_proto_IDMServiceProto__IDMConnectServiceRequest__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->PARSER:Lcom/google/protobuf/Parser;'],
        'type': 'method_replace',
        'search': """.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .registers 5

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
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->PARSER:Lcom/google/protobuf/Parser;

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
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;

    return-object p0

    :pswitch_4  #0x3
    const-string p0, "status_"

    const-string p1, "serviceId_"

    const-string p2, "endpoint_"

    const-string p3, "connParam_"

    const-string v0, "clientId_"

    filled-new-array {p0, p1, p2, p3, v0}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\u0005\u0000\u0000\u0001\u0005\u0005\u0000\u0000\u0000\u0001\u0004\u0002Ȉ\u0003\t\u0004\t\u0005Ȉ"

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;

    invoke-direct {p0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;-><init>()V

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

    goto :goto_18

    nop

    :goto_0
    return-object p0

    :pswitch_0  #0x1
    goto :goto_17

    nop

    :goto_1
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_24

    nop

    :goto_2
    const-string v0, "clientId_"

    goto :goto_6

    nop

    :goto_3
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    goto :goto_0

    nop

    :goto_4
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_11

    nop

    :goto_5
    invoke-direct {p0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;-><init>()V

    goto :goto_1b

    nop

    :goto_6
    filled-new-array {p0, p1, p2, p3, v0}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_25

    nop

    :goto_7
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_8

    :catchall_0
    move-exception p0

    goto :goto_9

    :cond_0
    :goto_8
    monitor-exit p1

    return-object p0

    :goto_9
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1d

    nop

    :goto_a
    return-object p0

    :pswitch_1  #0x3
    goto :goto_1c

    nop

    :goto_b
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_14

    nop

    :goto_c
    return-object p0

    :pswitch_2  #0x2
    goto :goto_15

    nop

    :goto_d
    const-class p1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;

    goto :goto_7

    nop

    :goto_e
    const-string p3, "connParam_"

    goto :goto_2

    nop

    :goto_f
    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;

    goto :goto_22

    nop

    :goto_10
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_1

    nop

    :goto_11
    aget p0, p0, p1

    goto :goto_10

    nop

    :goto_12
    const-string p2, "endpoint_"

    goto :goto_e

    nop

    :goto_13
    return-object p1

    :pswitch_3  #0x6
    goto :goto_16

    nop

    :goto_14
    if-eqz p0, :cond_1

    goto :goto_1e

    :cond_1
    goto :goto_d

    nop

    :goto_15
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest$Builder;

    goto :goto_3

    nop

    :goto_16
    const/4 p0, 0x1

    goto :goto_19

    nop

    :goto_17
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;

    goto :goto_5

    nop

    :goto_18
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_4

    nop

    :goto_19
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_21

    nop

    :goto_1a
    throw p0

    :pswitch_4  #0x7
    goto :goto_13

    nop

    :goto_1b
    return-object p0

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_0  #00000001
        :pswitch_2  #00000002
        :pswitch_1  #00000003
        :pswitch_5  #00000004
        :pswitch_6  #00000005
        :pswitch_3  #00000006
        :pswitch_4  #00000007
    .end packed-switch

    :goto_1c
    const-string p0, "status_"

    goto :goto_23

    nop

    :goto_1d
    throw p0

    :goto_1e
    goto :goto_1f

    nop

    :goto_1f
    return-object p0

    :pswitch_5  #0x4
    goto :goto_20

    nop

    :goto_20
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMConnectServiceRequest;

    goto :goto_a

    nop

    :goto_21
    return-object p0

    :pswitch_6  #0x5
    goto :goto_b

    nop

    :goto_22
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_c

    nop

    :goto_23
    const-string p1, "serviceId_"

    goto :goto_12

    nop

    :goto_24
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_1a

    nop

    :goto_25
    const-string p1, "\u0000\u0005\u0000\u0000\u0001\u0005\u0005\u0000\u0000\u0000\u0001\u0004\u0002Ȉ\u0003\t\u0004\t\u0005Ȉ"

    goto :goto_f

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
