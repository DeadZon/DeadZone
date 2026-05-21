TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/compat/proto/IPCParam$EventResponse.smali'
CLASS_FALLBACK_NAMES = ['IPCParam$EventResponse.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field private static final DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;', '.field public static final EVENTRESPONSE_FIELD_NUMBER:I = 0x1']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_compat_proto_IPCParam__EventResponse__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->PARSER:Lcom/google/protobuf/Parser;'],
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
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->PARSER:Lcom/google/protobuf/Parser;

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
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;

    return-object p0

    :pswitch_4  #0x3
    const-string p0, "eventResponse_"

    filled-new-array {p0}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\u0001\u0000\u0000\u0001\u0001\u0001\u0000\u0000\u0000\u0001\t"

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;

    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;-><init>()V

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

    goto :goto_18

    nop

    :goto_0
    return-object p0

    :pswitch_0  #0x4
    goto :goto_1

    nop

    :goto_1
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;

    goto :goto_17

    nop

    :goto_2
    throw p0

    :pswitch_1  #0x7
    goto :goto_1a

    nop

    :goto_3
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;

    goto :goto_21

    nop

    :goto_4
    const/4 p0, 0x1

    goto :goto_f

    nop

    :goto_5
    return-object p0

    :pswitch_2  #0x5
    goto :goto_14

    nop

    :goto_6
    return-object p0

    nop

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_3  #00000001
        :pswitch_5  #00000002
        :pswitch_4  #00000003
        :pswitch_0  #00000004
        :pswitch_2  #00000005
        :pswitch_6  #00000006
        :pswitch_1  #00000007
    .end packed-switch

    :goto_7
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_e

    nop

    :goto_8
    if-eqz p0, :cond_0

    goto :goto_13

    :cond_0
    goto :goto_1d

    nop

    :goto_9
    const-string p0, "eventResponse_"

    goto :goto_1b

    nop

    :goto_a
    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;

    goto :goto_10

    nop

    :goto_b
    const-string p1, "\u0000\u0001\u0000\u0000\u0001\u0001\u0001\u0000\u0000\u0000\u0001\t"

    goto :goto_a

    nop

    :goto_c
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    goto :goto_11

    nop

    :goto_d
    aget p0, p0, p1

    goto :goto_15

    nop

    :goto_e
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_2

    nop

    :goto_f
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_5

    nop

    :goto_10
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_19

    nop

    :goto_11
    return-object p0

    :pswitch_3  #0x1
    goto :goto_3

    nop

    :goto_12
    throw p0

    :goto_13
    goto :goto_0

    nop

    :goto_14
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_8

    nop

    :goto_15
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_7

    nop

    :goto_16
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_d

    nop

    :goto_17
    return-object p0

    :pswitch_4  #0x3
    goto :goto_9

    nop

    :goto_18
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_16

    nop

    :goto_19
    return-object p0

    :pswitch_5  #0x2
    goto :goto_1c

    nop

    :goto_1a
    return-object p1

    :pswitch_6  #0x6
    goto :goto_4

    nop

    :goto_1b
    filled-new-array {p0}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_b

    nop

    :goto_1c
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse$Builder;

    goto :goto_c

    nop

    :goto_1d
    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;

    goto :goto_1e

    nop

    :goto_1e
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_1f

    :catchall_0
    move-exception p0

    goto :goto_20

    :cond_1
    :goto_1f
    monitor-exit p1

    return-object p0

    :goto_20
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_12

    nop

    :goto_21
    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$EventResponse;-><init>()V

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
