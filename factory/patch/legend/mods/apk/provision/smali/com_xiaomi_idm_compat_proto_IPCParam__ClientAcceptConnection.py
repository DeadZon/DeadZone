TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection.smali'
CLASS_FALLBACK_NAMES = ['IPCParam$ClientAcceptConnection.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field public static final CONNLEVEL_FIELD_NUMBER:I = 0x2', '.field private static final DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;', '.field public static final SERVICEID_FIELD_NUMBER:I = 0x1']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_compat_proto_IPCParam__ClientAcceptConnection__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->PARSER:Lcom/google/protobuf/Parser;'],
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
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->PARSER:Lcom/google/protobuf/Parser;

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
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;

    return-object p0

    :pswitch_4  #0x3
    const-string p0, "serviceId_"

    const-string p1, "connLevel_"

    filled-new-array {p0, p1}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\u0002\u0000\u0000\u0001\u0002\u0002\u0000\u0000\u0000\u0001Ȉ\u0002\u0004"

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;

    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;-><init>()V

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

    goto :goto_a

    nop

    :goto_0
    const-string p1, "\u0000\u0002\u0000\u0000\u0001\u0002\u0002\u0000\u0000\u0000\u0001Ȉ\u0002\u0004"

    goto :goto_c

    nop

    :goto_1
    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;

    goto :goto_5

    nop

    :goto_2
    return-object p0

    :pswitch_0  #0x4
    goto :goto_1f

    nop

    :goto_3
    const-string p1, "connLevel_"

    goto :goto_10

    nop

    :goto_4
    return-object p0

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_2  #00000001
        :pswitch_5  #00000002
        :pswitch_3  #00000003
        :pswitch_0  #00000004
        :pswitch_4  #00000005
        :pswitch_6  #00000006
        :pswitch_1  #00000007
    .end packed-switch

    :goto_5
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_6

    :catchall_0
    move-exception p0

    goto :goto_7

    :cond_0
    :goto_6
    monitor-exit p1

    return-object p0

    :goto_7
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_17

    nop

    :goto_8
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_14

    nop

    :goto_9
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_1e

    nop

    :goto_a
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_1a

    nop

    :goto_b
    throw p0

    :pswitch_1  #0x7
    goto :goto_20

    nop

    :goto_c
    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;

    goto :goto_9

    nop

    :goto_d
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    goto :goto_13

    nop

    :goto_e
    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;-><init>()V

    goto :goto_4

    nop

    :goto_f
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_15

    nop

    :goto_10
    filled-new-array {p0, p1}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_0

    nop

    :goto_11
    const/4 p0, 0x1

    goto :goto_1b

    nop

    :goto_12
    const-string p0, "serviceId_"

    goto :goto_3

    nop

    :goto_13
    return-object p0

    :pswitch_2  #0x1
    goto :goto_21

    nop

    :goto_14
    if-eqz p0, :cond_1

    goto :goto_18

    :cond_1
    goto :goto_1

    nop

    :goto_15
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_1c

    nop

    :goto_16
    return-object p0

    :pswitch_3  #0x3
    goto :goto_12

    nop

    :goto_17
    throw p0

    :goto_18
    goto :goto_2

    nop

    :goto_19
    return-object p0

    :pswitch_4  #0x5
    goto :goto_8

    nop

    :goto_1a
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_1d

    nop

    :goto_1b
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_19

    nop

    :goto_1c
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_b

    nop

    :goto_1d
    aget p0, p0, p1

    goto :goto_f

    nop

    :goto_1e
    return-object p0

    :pswitch_5  #0x2
    goto :goto_22

    nop

    :goto_1f
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;

    goto :goto_16

    nop

    :goto_20
    return-object p1

    :pswitch_6  #0x6
    goto :goto_11

    nop

    :goto_21
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection;

    goto :goto_e

    nop

    :goto_22
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$ClientAcceptConnection$Builder;

    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
