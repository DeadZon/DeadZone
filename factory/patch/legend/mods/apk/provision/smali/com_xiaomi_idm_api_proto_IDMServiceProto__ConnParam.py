TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/api/proto/IDMServiceProto$ConnParam.smali'
CLASS_FALLBACK_NAMES = ['IDMServiceProto$ConnParam.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field public static final ACCOUNTTYPE_FIELD_NUMBER:I = 0x9', '.field public static final CONFIG_FIELD_NUMBER:I = 0xf', '.field public static final CONNLEVEL_FIELD_NUMBER:I = 0x5', '.field public static final CONNTYPE_FIELD_NUMBER:I = 0x1']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_api_proto_IDMServiceProto__ConnParam__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->PARSER:Lcom/google/protobuf/Parser;'],
        'type': 'method_replace',
        'search': """.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .registers 14

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
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->PARSER:Lcom/google/protobuf/Parser;

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
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;

    return-object p0

    :pswitch_4  #0x3
    const-string v0, "connType_"

    const-string v1, "errCode_"

    const-string v2, "errMsg_"

    const-string v3, "idHash_"

    const-string v4, "connLevel_"

    const-string v5, "privateData_"

    const-string v6, "linkRole_"

    const-string v7, "rpcChannel_"

    const-string v8, "accountType_"

    const-string v9, "config_"

    filled-new-array/range {v0 .. v9}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\n\u0000\u0000\u0001\u000f\n\u0000\u0000\u0000\u0001\f\u0002\u0004\u0003Ȉ\u0004Ȉ\u0005\u0004\u0006\n\u0007\u0004\b\u0004\t\u0004\u000f\n"

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;

    invoke-direct {p0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;-><init>()V

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
    .registers 14

    goto :goto_4

    nop

    :goto_0
    const-string v1, "errCode_"

    goto :goto_2a

    nop

    :goto_1
    filled-new-array/range {v0 .. v9}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_5

    nop

    :goto_2
    const-string v6, "linkRole_"

    goto :goto_1d

    nop

    :goto_3
    const-class p1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;

    goto :goto_1f

    nop

    :goto_4
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_16

    nop

    :goto_5
    const-string p1, "\u0000\n\u0000\u0000\u0001\u000f\n\u0000\u0000\u0000\u0001\f\u0002\u0004\u0003Ȉ\u0004Ȉ\u0005\u0004\u0006\n\u0007\u0004\b\u0004\t\u0004\u000f\n"

    goto :goto_e

    nop

    :goto_6
    const-string v5, "privateData_"

    goto :goto_2

    nop

    :goto_7
    invoke-direct {p0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;-><init>()V

    goto :goto_1a

    nop

    :goto_8
    const-string v3, "idHash_"

    goto :goto_f

    nop

    :goto_9
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;

    goto :goto_26

    nop

    :goto_a
    aget p0, p0, p1

    goto :goto_19

    nop

    :goto_b
    return-object p0

    :pswitch_0  #0x4
    goto :goto_9

    nop

    :goto_c
    return-object p1

    :pswitch_1  #0x6
    goto :goto_24

    nop

    :goto_d
    return-object p0

    :pswitch_2  #0x2
    goto :goto_10

    nop

    :goto_e
    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;

    goto :goto_11

    nop

    :goto_f
    const-string v4, "connLevel_"

    goto :goto_6

    nop

    :goto_10
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam$Builder;

    goto :goto_28

    nop

    :goto_11
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_d

    nop

    :goto_12
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_18

    nop

    :goto_13
    return-object p0

    :pswitch_3  #0x1
    goto :goto_25

    nop

    :goto_14
    throw p0

    :pswitch_4  #0x7
    goto :goto_c

    nop

    :goto_15
    const-string v8, "accountType_"

    goto :goto_1c

    nop

    :goto_16
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_a

    nop

    :goto_17
    if-eqz p0, :cond_0

    goto :goto_23

    :cond_0
    goto :goto_3

    nop

    :goto_18
    return-object p0

    :pswitch_5  #0x5
    goto :goto_1e

    nop

    :goto_19
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_1b

    nop

    :goto_1a
    return-object p0

    nop

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_3  #00000001
        :pswitch_2  #00000002
        :pswitch_6  #00000003
        :pswitch_0  #00000004
        :pswitch_5  #00000005
        :pswitch_1  #00000006
        :pswitch_4  #00000007
    .end packed-switch

    :goto_1b
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_27

    nop

    :goto_1c
    const-string v9, "config_"

    goto :goto_1

    nop

    :goto_1d
    const-string v7, "rpcChannel_"

    goto :goto_15

    nop

    :goto_1e
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_17

    nop

    :goto_1f
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_20

    :catchall_0
    move-exception v0

    move-object p0, v0

    goto :goto_21

    :cond_1
    :goto_20
    monitor-exit p1

    return-object p0

    :goto_21
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_22

    nop

    :goto_22
    throw p0

    :goto_23
    goto :goto_b

    nop

    :goto_24
    const/4 p0, 0x1

    goto :goto_12

    nop

    :goto_25
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam;

    goto :goto_7

    nop

    :goto_26
    return-object p0

    :pswitch_6  #0x3
    goto :goto_29

    nop

    :goto_27
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_14

    nop

    :goto_28
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$ConnParam$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    goto :goto_13

    nop

    :goto_29
    const-string v0, "connType_"

    goto :goto_0

    nop

    :goto_2a
    const-string v2, "errMsg_"

    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
