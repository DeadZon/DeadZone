TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/api/proto/IDMServiceProto$IDMService.smali'
CLASS_FALLBACK_NAMES = ['IDMServiceProto$IDMService.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field public static final APPDATA_FIELD_NUMBER:I = 0x7', '.field private static final DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;', '.field public static final ENDPOINT_FIELD_NUMBER:I = 0x4', '.field public static final NAME_FIELD_NUMBER:I = 0x3']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_api_proto_IDMServiceProto__IDMService__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->PARSER:Lcom/google/protobuf/Parser;'],
        'type': 'method_replace',
        'search': """.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .registers 11

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
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->PARSER:Lcom/google/protobuf/Parser;

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
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;

    return-object p0

    :pswitch_4  #0x3
    const-string v0, "serviceId_"

    const-string v1, "type_"

    const-string v2, "name_"

    const-string v3, "endpoint_"

    const-string v4, "originalServiceId_"

    const-string v5, "superType_"

    const-string v6, "appData_"

    filled-new-array/range {v0 .. v6}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\u0007\u0000\u0000\u0001\u0007\u0007\u0000\u0000\u0000\u0001Ȉ\u0002Ȉ\u0003Ȉ\u0004\t\u0005Ȉ\u0006Ȉ\u0007\n"

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;

    invoke-direct {p0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;-><init>()V

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
    .registers 11

    goto :goto_21

    nop

    :goto_0
    const-string v1, "type_"

    goto :goto_b

    nop

    :goto_1
    const-string v6, "appData_"

    goto :goto_9

    nop

    :goto_2
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;

    goto :goto_26

    nop

    :goto_3
    throw p0

    :pswitch_0  #0x7
    goto :goto_c

    nop

    :goto_4
    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;

    goto :goto_17

    nop

    :goto_5
    return-object p0

    :pswitch_1  #0x5
    goto :goto_15

    nop

    :goto_6
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_5

    nop

    :goto_7
    aget p0, p0, p1

    goto :goto_11

    nop

    :goto_8
    const-string v0, "serviceId_"

    goto :goto_0

    nop

    :goto_9
    filled-new-array/range {v0 .. v6}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_27

    nop

    :goto_a
    return-object p0

    :pswitch_2  #0x4
    goto :goto_2

    nop

    :goto_b
    const-string v2, "name_"

    goto :goto_12

    nop

    :goto_c
    return-object p1

    :pswitch_3  #0x6
    goto :goto_1a

    nop

    :goto_d
    throw p0

    :goto_e
    goto :goto_a

    nop

    :goto_f
    const-string v5, "superType_"

    goto :goto_1

    nop

    :goto_10
    invoke-direct {p0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;-><init>()V

    goto :goto_1b

    nop

    :goto_11
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_13

    nop

    :goto_12
    const-string v3, "endpoint_"

    goto :goto_20

    nop

    :goto_13
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_14

    nop

    :goto_14
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_3

    nop

    :goto_15
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_19

    nop

    :goto_16
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_7

    nop

    :goto_17
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_23

    nop

    :goto_18
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService$Builder;

    goto :goto_24

    nop

    :goto_19
    if-eqz p0, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_25

    nop

    :goto_1a
    const/4 p0, 0x1

    goto :goto_6

    nop

    :goto_1b
    return-object p0

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_4  #00000001
        :pswitch_5  #00000002
        :pswitch_6  #00000003
        :pswitch_2  #00000004
        :pswitch_1  #00000005
        :pswitch_3  #00000006
        :pswitch_0  #00000007
    .end packed-switch

    :goto_1c
    return-object p0

    :pswitch_4  #0x1
    goto :goto_22

    nop

    :goto_1d
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_1e

    :catchall_0
    move-exception v0

    move-object p0, v0

    goto :goto_1f

    :cond_1
    :goto_1e
    monitor-exit p1

    return-object p0

    :goto_1f
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_d

    nop

    :goto_20
    const-string v4, "originalServiceId_"

    goto :goto_f

    nop

    :goto_21
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_16

    nop

    :goto_22
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;

    goto :goto_10

    nop

    :goto_23
    return-object p0

    :pswitch_5  #0x2
    goto :goto_18

    nop

    :goto_24
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    goto :goto_1c

    nop

    :goto_25
    const-class p1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$IDMService;

    goto :goto_1d

    nop

    :goto_26
    return-object p0

    :pswitch_6  #0x3
    goto :goto_8

    nop

    :goto_27
    const-string p1, "\u0000\u0007\u0000\u0000\u0001\u0007\u0007\u0000\u0000\u0000\u0001Ȉ\u0002Ȉ\u0003Ȉ\u0004\t\u0005Ȉ\u0006Ȉ\u0007\n"

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
