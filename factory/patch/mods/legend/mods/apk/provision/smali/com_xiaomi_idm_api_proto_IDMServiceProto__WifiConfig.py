TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig.smali'
CLASS_FALLBACK_NAMES = ['IDMServiceProto$WifiConfig.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field public static final CHANNEL_FIELD_NUMBER:I = 0x4', '.field private static final DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;', '.field public static final LOCALIP_FIELD_NUMBER:I = 0x7', '.field public static final LOCALMCC_FIELD_NUMBER:I = 0x8']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_api_proto_IDMServiceProto__WifiConfig__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance p0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object p1', 'invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object p0', 'sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->PARSER:Lcom/google/protobuf/Parser;'],
        'type': 'method_replace',
        'search': """.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .registers 13

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
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_1

    const-class p1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;

    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->PARSER:Lcom/google/protobuf/Parser;

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
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;

    return-object p0

    :pswitch_4  #0x3
    const-string v0, "ssid_"

    const-string v1, "pwd_"

    const-string v2, "use5GBand_"

    const-string v3, "channel_"

    const-string v4, "macAddr_"

    const-string v5, "remoteIp_"

    const-string v6, "localIp_"

    const-string v7, "localMcc_"

    const-string v8, "remoteMcc_"

    filled-new-array/range {v0 .. v8}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "\u0000\t\u0000\u0000\u0001\t\t\u0000\u0000\u0000\u0001Ȉ\u0002Ȉ\u0003\u0007\u0004\u0004\u0005Ȉ\u0006Ȉ\u0007Ȉ\b\u0004\t\u0004"

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;

    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :pswitch_5  #0x2
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig$Builder;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    return-object p0

    :pswitch_6  #0x1
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;

    invoke-direct {p0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;-><init>()V

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
    .registers 13

    goto :goto_19

    nop

    :goto_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_27

    nop

    :goto_1
    const-class p1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;

    goto :goto_1a

    nop

    :goto_2
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig$Builder;

    goto :goto_5

    nop

    :goto_3
    new-instance p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;

    goto :goto_16

    nop

    :goto_4
    filled-new-array/range {v0 .. v8}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_b

    nop

    :goto_5
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    goto :goto_10

    nop

    :goto_6
    return-object p0

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_1  #00000001
        :pswitch_4  #00000002
        :pswitch_2  #00000003
        :pswitch_5  #00000004
        :pswitch_3  #00000005
        :pswitch_6  #00000006
        :pswitch_0  #00000007
    .end packed-switch

    :goto_7
    const-string v3, "channel_"

    goto :goto_1f

    nop

    :goto_8
    invoke-static {p0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object p0

    goto :goto_1d

    nop

    :goto_9
    throw p0

    :pswitch_0  #0x7
    goto :goto_29

    nop

    :goto_a
    const-string v7, "localMcc_"

    goto :goto_e

    nop

    :goto_b
    const-string p1, "\u0000\t\u0000\u0000\u0001\t\t\u0000\u0000\u0000\u0001Ȉ\u0002Ȉ\u0003\u0007\u0004\u0004\u0005Ȉ\u0006Ȉ\u0007Ȉ\b\u0004\t\u0004"

    goto :goto_23

    nop

    :goto_c
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;

    goto :goto_13

    nop

    :goto_d
    aget p0, p0, p1

    goto :goto_12

    nop

    :goto_e
    const-string v8, "remoteMcc_"

    goto :goto_4

    nop

    :goto_f
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    move-result p1

    goto :goto_d

    nop

    :goto_10
    return-object p0

    :pswitch_1  #0x1
    goto :goto_3

    nop

    :goto_11
    invoke-direct {p0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_9

    nop

    :goto_12
    const/4 p1, 0x0

    packed-switch p0, :pswitch_data_0

    goto :goto_24

    nop

    :goto_13
    return-object p0

    :pswitch_2  #0x3
    goto :goto_15

    nop

    :goto_14
    const/4 p0, 0x1

    goto :goto_8

    nop

    :goto_15
    const-string v0, "ssid_"

    goto :goto_20

    nop

    :goto_16
    invoke-direct {p0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;-><init>()V

    goto :goto_6

    nop

    :goto_17
    throw p0

    :goto_18
    goto :goto_25

    nop

    :goto_19
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_f

    nop

    :goto_1a
    monitor-enter p1

    :try_start_0
    sget-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->PARSER:Lcom/google/protobuf/Parser;

    if-nez p0, :cond_0

    new-instance p0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;

    invoke-direct {p0, p2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object p0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_1b

    :catchall_0
    move-exception v0

    move-object p0, v0

    goto :goto_1c

    :cond_0
    :goto_1b
    monitor-exit p1

    return-object p0

    :goto_1c
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_17

    nop

    :goto_1d
    return-object p0

    :pswitch_3  #0x5
    goto :goto_0

    nop

    :goto_1e
    return-object p0

    :pswitch_4  #0x2
    goto :goto_2

    nop

    :goto_1f
    const-string v4, "macAddr_"

    goto :goto_26

    nop

    :goto_20
    const-string v1, "pwd_"

    goto :goto_21

    nop

    :goto_21
    const-string v2, "use5GBand_"

    goto :goto_7

    nop

    :goto_22
    const-string v6, "localIp_"

    goto :goto_a

    nop

    :goto_23
    sget-object p2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$WifiConfig;

    goto :goto_28

    nop

    :goto_24
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_11

    nop

    :goto_25
    return-object p0

    :pswitch_5  #0x4
    goto :goto_c

    nop

    :goto_26
    const-string v5, "remoteIp_"

    goto :goto_22

    nop

    :goto_27
    if-eqz p0, :cond_1

    goto :goto_18

    :cond_1
    goto :goto_1

    nop

    :goto_28
    invoke-static {p2, p1, p0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_1e

    nop

    :goto_29
    return-object p1

    :pswitch_6  #0x6
    goto :goto_14

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
