TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/compat/proto/IPCParam$RegisterService.smali'
CLASS_FALLBACK_NAMES = ['IPCParam$RegisterService.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field public static final APPPARAM_FIELD_NUMBER:I = 0x8', '.field public static final COMMTYPE_FIELD_NUMBER:I = 0x5', '.field private static final DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;', '.field public static final DISCTYPE_FIELD_NUMBER:I = 0x4']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_compat_proto_IPCParam__RegisterService__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->PARSER:Lcom/google/protobuf/Parser;'],
        'type': 'method_replace',
        'search': """.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .registers 12

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
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->PARSER:Lcom/google/protobuf/Parser;

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
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;

    return-object p0

    :pswitch_4  #0x3
    const-string v0, "serviceProto_"

    const-string v1, "intentStr_"

    const-string v2, "intentType_"

    const-string v3, "discType_"

    const-string v4, "commType_"

    const-string v5, "serviceSecurityType_"

    const-string v6, "privateData_"

    const-string v7, "appParam_"

    filled-new-array/range {v0 .. v7}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\b\u0000\u0000\u0001\b\b\u0000\u0000\u0000\u0001\t\u0002Ȉ\u0003Ȉ\u0004\u0004\u0005\u0004\u0006\u0004\u0007\n\b\t"

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;

    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;-><init>()V

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
    .registers 12

    goto :goto_2

    nop

    :goto_0
    const-string v0, "serviceProto_"

    goto :goto_19

    nop

    :goto_1
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService$Builder;

    goto :goto_1a

    nop

    :goto_2
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_1b

    nop

    :goto_3
    const/4 p0, 0x1

    goto :goto_28

    nop

    :goto_4
    const-string v2, "intentType_"

    goto :goto_1d

    nop

    :goto_5
    return-object p0

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_2  #00000001
        :pswitch_3  #00000002
        :pswitch_5  #00000003
        :pswitch_1  #00000004
        :pswitch_6  #00000005
        :pswitch_0  #00000006
        :pswitch_4  #00000007
    .end packed-switch

    :goto_6
    filled-new-array/range {v0 .. v7}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_b

    nop

    :goto_7
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;

    goto :goto_23

    nop

    :goto_8
    const-string v6, "privateData_"

    goto :goto_16

    nop

    :goto_9
    return-object p1

    :pswitch_0  #0x6
    goto :goto_3

    nop

    :goto_a
    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;

    goto :goto_20

    nop

    :goto_b
    const-string p1, "\u0000\b\u0000\u0000\u0001\b\b\u0000\u0000\u0000\u0001\t\u0002Ȉ\u0003Ȉ\u0004\u0004\u0005\u0004\u0006\u0004\u0007\n\b\t"

    goto :goto_11

    nop

    :goto_c
    return-object p0

    :pswitch_1  #0x4
    goto :goto_12

    nop

    :goto_d
    const-string v4, "commType_"

    goto :goto_17

    nop

    :goto_e
    throw p0

    :goto_f
    goto :goto_c

    nop

    :goto_10
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_1e

    nop

    :goto_11
    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;

    goto :goto_14

    nop

    :goto_12
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;

    goto :goto_24

    nop

    :goto_13
    return-object p0

    :pswitch_2  #0x1
    goto :goto_7

    nop

    :goto_14
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_18

    nop

    :goto_15
    aget p0, p0, p1

    goto :goto_10

    nop

    :goto_16
    const-string v7, "appParam_"

    goto :goto_6

    nop

    :goto_17
    const-string v5, "serviceSecurityType_"

    goto :goto_8

    nop

    :goto_18
    return-object p0

    :pswitch_3  #0x2
    goto :goto_1

    nop

    :goto_19
    const-string v1, "intentStr_"

    goto :goto_4

    nop

    :goto_1a
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    goto :goto_13

    nop

    :goto_1b
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_15

    nop

    :goto_1c
    throw p0

    :pswitch_4  #0x7
    goto :goto_9

    nop

    :goto_1d
    const-string v3, "discType_"

    goto :goto_d

    nop

    :goto_1e
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_1f

    nop

    :goto_1f
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_1c

    nop

    :goto_20
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_21

    :catchall_0
    move-exception v0

    move-object p0, v0

    goto :goto_22

    :cond_0
    :goto_21
    monitor-exit p1

    return-object p0

    :goto_22
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_e

    nop

    :goto_23
    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;-><init>()V

    goto :goto_5

    nop

    :goto_24
    return-object p0

    :pswitch_5  #0x3
    goto :goto_0

    nop

    :goto_25
    if-eqz p0, :cond_1

    goto :goto_f

    :cond_1
    goto :goto_a

    nop

    :goto_26
    return-object p0

    :pswitch_6  #0x5
    goto :goto_27

    nop

    :goto_27
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$RegisterService;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_25

    nop

    :goto_28
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_26

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
