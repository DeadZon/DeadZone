TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/compat/proto/IPCParam$TransHead.smali'
CLASS_FALLBACK_NAMES = ['IPCParam$TransHead.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field public static final ACK_FIELD_NUMBER:I = 0x2', '.field private static final DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;', '.field public static final SEQ_FIELD_NUMBER:I = 0x1']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_compat_proto_IPCParam__TransHead__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->PARSER:Lcom/google/protobuf/Parser;'],
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
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->PARSER:Lcom/google/protobuf/Parser;

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
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;

    return-object p0

    :pswitch_4  #0x3
    const-string p0, "seq_"

    const-string p1, "ack_"

    filled-new-array {p0, p1}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\u0002\u0000\u0000\u0001\u0002\u0002\u0000\u0000\u0000\u0001Ȉ\u0002Ȉ"

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;

    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;-><init>()V

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
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;

    goto :goto_1

    nop

    :goto_1
    invoke-direct {p0}, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;-><init>()V

    goto :goto_1b

    nop

    :goto_2
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_14

    nop

    :goto_3
    return-object p0

    :pswitch_0  #0x2
    goto :goto_e

    nop

    :goto_4
    return-object p0

    :pswitch_1  #0x5
    goto :goto_c

    nop

    :goto_5
    const-string p1, "ack_"

    goto :goto_1d

    nop

    :goto_6
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_7

    :catchall_0
    move-exception p0

    goto :goto_8

    :cond_0
    :goto_7
    monitor-exit p1

    return-object p0

    :goto_8
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_16

    nop

    :goto_9
    sget-object p2, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;

    goto :goto_18

    nop

    :goto_a
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_2

    nop

    :goto_b
    const-string p1, "\u0000\u0002\u0000\u0000\u0001\u0002\u0002\u0000\u0000\u0000\u0001Ȉ\u0002Ȉ"

    goto :goto_9

    nop

    :goto_c
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_20

    nop

    :goto_d
    const-string p0, "seq_"

    goto :goto_5

    nop

    :goto_e
    new-instance p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead$Builder;

    goto :goto_1a

    nop

    :goto_f
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_10

    nop

    :goto_10
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_19

    nop

    :goto_11
    return-object p1

    :pswitch_2  #0x6
    goto :goto_22

    nop

    :goto_12
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_4

    nop

    :goto_13
    return-object p0

    :pswitch_3  #0x3
    goto :goto_d

    nop

    :goto_14
    aget p0, p0, p1

    goto :goto_f

    nop

    :goto_15
    const-class p1, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;

    goto :goto_6

    nop

    :goto_16
    throw p0

    :goto_17
    goto :goto_21

    nop

    :goto_18
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_3

    nop

    :goto_19
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_1e

    nop

    :goto_1a
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead$Builder;-><init>(Lcom/xiaomi/idm/compat/proto/IPCParam$1;)V

    goto :goto_1c

    nop

    :goto_1b
    return-object p0

    nop

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_4  #00000001
        :pswitch_0  #00000002
        :pswitch_3  #00000003
        :pswitch_6  #00000004
        :pswitch_1  #00000005
        :pswitch_2  #00000006
        :pswitch_5  #00000007
    .end packed-switch

    :goto_1c
    return-object p0

    :pswitch_4  #0x1
    goto :goto_0

    nop

    :goto_1d
    filled-new-array {p0, p1}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_b

    nop

    :goto_1e
    throw p0

    :pswitch_5  #0x7
    goto :goto_11

    nop

    :goto_1f
    sget-object p0, Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/compat/proto/IPCParam$TransHead;

    goto :goto_13

    nop

    :goto_20
    if-eqz p0, :cond_1

    goto :goto_17

    :cond_1
    goto :goto_15

    nop

    :goto_21
    return-object p0

    :pswitch_6  #0x4
    goto :goto_1f

    nop

    :goto_22
    const/4 p0, 0x1

    goto :goto_12

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
