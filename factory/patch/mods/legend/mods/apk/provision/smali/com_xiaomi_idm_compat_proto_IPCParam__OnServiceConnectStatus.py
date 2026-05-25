TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus.smali'
CLASS_FALLBACK_NAMES = ['IPCParam$OnServiceConnectStatus.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field public static final CONNPARAM_FIELD_NUMBER:I = 0x4', '.field private static final DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;', '.field public static final ENDPOINT_FIELD_NUMBER:I = 0x3', '.field public static final SERVICEID_FIELD_NUMBER:I = 0x2']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_compat_proto_IPCParam__OnServiceConnectStatus__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->PARSER:Lcom/google/protobuf/Parser;'],
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
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->PARSER:Lcom/google/protobuf/Parser;

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
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;

    return-object p0

    :pswitch_4  #0x3
    const-string p0, "status_"

    const-string p1, "serviceId_"

    const-string p2, "endpoint_"

    const-string p3, "connParam_"

    filled-new-array {p0, p1, p2, p3}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\u0004\u0000\u0000\u0001\u0004\u0004\u0000\u0000\u0000\u0001\u0004\u0002Ȉ\u0003\t\u0004\t"

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;

    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;-><init>()V

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

    :pswitch_0  #0x2
    goto :goto_5

    nop

    :goto_1
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_2

    nop

    :goto_2
    if-eqz p0, :cond_0

    goto :goto_13

    :cond_0
    goto :goto_21

    nop

    :goto_3
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_15

    nop

    :goto_4
    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;

    goto :goto_14

    nop

    :goto_5
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus$Builder;

    goto :goto_17

    nop

    :goto_6
    const/4 p0, 0x1

    goto :goto_1b

    nop

    :goto_7
    return-object p0

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_3  #00000001
        :pswitch_0  #00000002
        :pswitch_1  #00000003
        :pswitch_4  #00000004
        :pswitch_5  #00000005
        :pswitch_6  #00000006
        :pswitch_2  #00000007
    .end packed-switch

    :goto_8
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_9

    :catchall_0
    move-exception p0

    goto :goto_a

    :cond_1
    :goto_9
    monitor-exit p1

    return-object p0

    :goto_a
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_12

    nop

    :goto_b
    const-string p0, "status_"

    goto :goto_d

    nop

    :goto_c
    return-object p0

    :pswitch_1  #0x3
    goto :goto_b

    nop

    :goto_d
    const-string p1, "serviceId_"

    goto :goto_20

    nop

    :goto_e
    throw p0

    :pswitch_2  #0x7
    goto :goto_23

    nop

    :goto_f
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_3

    nop

    :goto_10
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;

    goto :goto_c

    nop

    :goto_11
    return-object p0

    :pswitch_3  #0x1
    goto :goto_1e

    nop

    :goto_12
    throw p0

    :goto_13
    goto :goto_1f

    nop

    :goto_14
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_0

    nop

    :goto_15
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_e

    nop

    :goto_16
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_1c

    nop

    :goto_17
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    goto :goto_11

    nop

    :goto_18
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_16

    nop

    :goto_19
    filled-new-array {p0, p1, p2, p3}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_24

    nop

    :goto_1a
    const-string p3, "connParam_"

    goto :goto_19

    nop

    :goto_1b
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_22

    nop

    :goto_1c
    aget p0, p0, p1

    goto :goto_f

    nop

    :goto_1d
    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;-><init>()V

    goto :goto_7

    nop

    :goto_1e
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;

    goto :goto_1d

    nop

    :goto_1f
    return-object p0

    :pswitch_4  #0x4
    goto :goto_10

    nop

    :goto_20
    const-string p2, "endpoint_"

    goto :goto_1a

    nop

    :goto_21
    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$OnServiceConnectStatus;

    goto :goto_8

    nop

    :goto_22
    return-object p0

    :pswitch_5  #0x5
    goto :goto_1

    nop

    :goto_23
    return-object p1

    :pswitch_6  #0x6
    goto :goto_6

    nop

    :goto_24
    const-string p1, "\u0000\u0004\u0000\u0000\u0001\u0004\u0004\u0000\u0000\u0000\u0001\u0004\u0002Ȉ\u0003\t\u0004\t"

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
