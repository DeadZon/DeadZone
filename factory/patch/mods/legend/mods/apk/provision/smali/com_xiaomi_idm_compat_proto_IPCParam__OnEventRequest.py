TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/compat/proto/IPCParam$OnEventRequest.smali'
CLASS_FALLBACK_NAMES = ['IPCParam$OnEventRequest.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field private static final DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;', '.field public static final IDMEVENT_FIELD_NUMBER:I = 0x1']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_compat_proto_IPCParam__OnEventRequest__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->PARSER:Lcom/google/protobuf/Parser;'],
        'type': 'method_replace',
        'search': """.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .registers 4

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
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->PARSER:Lcom/google/protobuf/Parser;

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
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;

    return-object p0

    :pswitch_4  #0x3
    const-string p0, "idmEvent_"

    filled-new-array {p0}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\u0001\u0000\u0000\u0001\u0001\u0001\u0000\u0000\u0000\u0001\t"

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;

    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;-><init>()V

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
    .registers 4

    goto :goto_16

    nop

    :goto_0
    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;

    goto :goto_18

    nop

    :goto_1
    return-object p0

    :pswitch_0  #0x2
    goto :goto_d

    nop

    :goto_2
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;

    goto :goto_1b

    nop

    :goto_3
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;

    goto :goto_b

    nop

    :goto_4
    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;

    goto :goto_c

    nop

    :goto_5
    const-string p0, "idmEvent_"

    goto :goto_7

    nop

    :goto_6
    return-object p1

    :pswitch_1  #0x6
    goto :goto_14

    nop

    :goto_7
    filled-new-array {p0}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_12

    nop

    :goto_8
    return-object p0

    :pswitch_2  #0x4
    goto :goto_3

    nop

    :goto_9
    return-object p0

    :pswitch_3  #0x1
    goto :goto_2

    nop

    :goto_a
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_1d

    nop

    :goto_b
    return-object p0

    :pswitch_4  #0x3
    goto :goto_5

    nop

    :goto_c
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_1

    nop

    :goto_d
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest$Builder;

    goto :goto_20

    nop

    :goto_e
    throw p0

    :goto_f
    goto :goto_8

    nop

    :goto_10
    throw p0

    :pswitch_5  #0x7
    goto :goto_6

    nop

    :goto_11
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_1e

    nop

    :goto_12
    const-string p1, "\u0000\u0001\u0000\u0000\u0001\u0001\u0001\u0000\u0000\u0000\u0001\t"

    goto :goto_4

    nop

    :goto_13
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_21

    nop

    :goto_14
    const/4 p0, 0x1

    goto :goto_a

    nop

    :goto_15
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_10

    nop

    :goto_16
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_1f

    nop

    :goto_17
    return-object p0

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_3  #00000001
        :pswitch_0  #00000002
        :pswitch_4  #00000003
        :pswitch_2  #00000004
        :pswitch_6  #00000005
        :pswitch_1  #00000006
        :pswitch_5  #00000007
    .end packed-switch

    :goto_18
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_19

    :catchall_0
    move-exception p0

    goto :goto_1a

    :cond_0
    :goto_19
    monitor-exit p1

    return-object p0

    :goto_1a
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_e

    nop

    :goto_1b
    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest;-><init>()V

    goto :goto_17

    nop

    :goto_1c
    aget p0, p0, p1

    goto :goto_13

    nop

    :goto_1d
    return-object p0

    :pswitch_6  #0x5
    goto :goto_11

    nop

    :goto_1e
    if-eqz p0, :cond_1

    goto :goto_f

    :cond_1
    goto :goto_0

    nop

    :goto_1f
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_1c

    nop

    :goto_20
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$OnEventRequest$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    goto :goto_9

    nop

    :goto_21
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_15

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
