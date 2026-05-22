TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse.smali'
CLASS_FALLBACK_NAMES = ['IDMServiceProto$IDMResponse.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field public static final CLIENTID_FIELD_NUMBER:I = 0x5', '.field public static final CODE_FIELD_NUMBER:I = 0x1', '.field private static final DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;', '.field public static final MSG_FIELD_NUMBER:I = 0x2']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_api_proto_IDMServiceProto__IDMResponse__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->PARSER:Lcom/google/protobuf/Parser;'],
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
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->PARSER:Lcom/google/protobuf/Parser;

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
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;

    return-object p0

    :pswitch_4  #0x3
    const-string v0, "code_"

    const-string v1, "msg_"

    const-string v2, "requestId_"

    const-string v3, "serviceId_"

    const-string v4, "clientId_"

    const-string v5, "response_"

    filled-new-array/range {v0 .. v5}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\u0006\u0000\u0000\u0001\u000f\u0006\u0000\u0000\u0000\u0001\u0004\u0002Ȉ\u0003Ȉ\u0004Ȉ\u0005Ȉ\u000f\n"

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;

    invoke-direct {p0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;-><init>()V

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

    goto :goto_8

    nop

    :goto_0
    return-object p0

    nop

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_1  #00000001
        :pswitch_6  #00000002
        :pswitch_5  #00000003
        :pswitch_4  #00000004
        :pswitch_3  #00000005
        :pswitch_2  #00000006
        :pswitch_0  #00000007
    .end packed-switch

    :goto_1
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_c

    nop

    :goto_2
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_1b

    nop

    :goto_3
    const-string v0, "code_"

    goto :goto_20

    nop

    :goto_4
    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;

    goto :goto_10

    nop

    :goto_5
    throw p0

    :goto_6
    goto :goto_21

    nop

    :goto_7
    throw p0

    :pswitch_0  #0x7
    goto :goto_16

    nop

    :goto_8
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_2

    nop

    :goto_9
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;

    goto :goto_23

    nop

    :goto_a
    invoke-direct {p0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;-><init>()V

    goto :goto_0

    nop

    :goto_b
    const-string v2, "requestId_"

    goto :goto_17

    nop

    :goto_c
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_18

    nop

    :goto_d
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    goto :goto_11

    nop

    :goto_e
    const/4 p0, 0x1

    goto :goto_24

    nop

    :goto_f
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_1a

    nop

    :goto_10
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_26

    nop

    :goto_11
    return-object p0

    :pswitch_1  #0x1
    goto :goto_1f

    nop

    :goto_12
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_13

    :catchall_0
    move-exception v0

    move-object p0, v0

    goto :goto_14

    :cond_0
    :goto_13
    monitor-exit p1

    return-object p0

    :goto_14
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_5

    nop

    :goto_15
    filled-new-array/range {v0 .. v5}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_1d

    nop

    :goto_16
    return-object p1

    :pswitch_2  #0x6
    goto :goto_e

    nop

    :goto_17
    const-string v3, "serviceId_"

    goto :goto_22

    nop

    :goto_18
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_7

    nop

    :goto_19
    const-class p1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;

    goto :goto_12

    nop

    :goto_1a
    if-eqz p0, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_19

    nop

    :goto_1b
    aget p0, p0, p1

    goto :goto_1

    nop

    :goto_1c
    return-object p0

    :pswitch_3  #0x5
    goto :goto_f

    nop

    :goto_1d
    const-string p1, "\u0000\u0006\u0000\u0000\u0001\u000f\u0006\u0000\u0000\u0000\u0001\u0004\u0002Ȉ\u0003Ȉ\u0004Ȉ\u0005Ȉ\u000f\n"

    goto :goto_4

    nop

    :goto_1e
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse$Builder;

    goto :goto_d

    nop

    :goto_1f
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMResponse;

    goto :goto_a

    nop

    :goto_20
    const-string v1, "msg_"

    goto :goto_b

    nop

    :goto_21
    return-object p0

    :pswitch_4  #0x4
    goto :goto_9

    nop

    :goto_22
    const-string v4, "clientId_"

    goto :goto_25

    nop

    :goto_23
    return-object p0

    :pswitch_5  #0x3
    goto :goto_3

    nop

    :goto_24
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_1c

    nop

    :goto_25
    const-string v5, "response_"

    goto :goto_15

    nop

    :goto_26
    return-object p0

    :pswitch_6  #0x2
    goto :goto_1e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
