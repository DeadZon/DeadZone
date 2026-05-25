TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/api/proto/IDMServiceProto$Endpoint.smali'
CLASS_FALLBACK_NAMES = ['IDMServiceProto$Endpoint.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageLite;', '.implements Lcom/google/protobuf/MessageLiteOrBuilder;', '.field public static final ALTITUDE_FIELD_NUMBER:I = 0xd', '.field public static final AZIMUTH_FIELD_NUMBER:I = 0xe', '.field public static final BDADDR_FIELD_NUMBER:I = 0x5', '.field public static final COMPARENUM_FIELD_NUMBER:I = 0x9']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_api_proto_IDMServiceProto__Endpoint__dynamicMethod',
        'method': '.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'dynamicMethod',
        'method_anchors': ['sget-object v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I', 'invoke-virtual/range {p1 .. p1}, Ljava/lang/Enum;->ordinal()I', 'new-instance v0, Ljava/lang/UnsupportedOperationException;', 'invoke-direct {v0}, Ljava/lang/UnsupportedOperationException;-><init>()V', 'return-object v1', 'invoke-static {v0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;', 'return-object v0', 'sget-object v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->PARSER:Lcom/google/protobuf/Parser;'],
        'type': 'method_replace',
        'search': """.method protected final dynamicMethod(Lcom/google/protobuf/GeneratedMessageLite$MethodToInvoke;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .registers 23

    sget-object v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    invoke-virtual/range {p1 .. p1}, Ljava/lang/Enum;->ordinal()I

    move-result v1

    aget v0, v0, v1

    const/4 v1, 0x0

    packed-switch v0, :pswitch_data_0

    new-instance v0, Ljava/lang/UnsupportedOperationException;

    invoke-direct {v0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    throw v0

    :pswitch_0  #0x7
    return-object v1

    :pswitch_1  #0x6
    const/4 v0, 0x1

    invoke-static {v0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object v0

    return-object v0

    :pswitch_2  #0x5
    sget-object v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->PARSER:Lcom/google/protobuf/Parser;

    if-nez v0, :cond_1

    const-class v1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;

    monitor-enter v1

    :try_start_0
    sget-object v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->PARSER:Lcom/google/protobuf/Parser;

    if-nez v0, :cond_0

    new-instance v0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object v2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;

    invoke-direct {v0, v2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_0

    :catchall_0
    move-exception v0

    goto :goto_1

    :cond_0
    :goto_0
    monitor-exit v1

    return-object v0

    :goto_1
    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v0

    :cond_1
    return-object v0

    :pswitch_3  #0x4
    sget-object v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;

    return-object v0

    :pswitch_4  #0x3
    const-string v2, "idhash_"

    const-string v3, "name_"

    const-string v4, "mac_"

    const-string v5, "ip_"

    const-string v6, "bdAddr_"

    const-string v7, "mcVersion_"

    const-string v8, "verifyStatus_"

    const-string v9, "sdkVersion_"

    const-string v10, "compareNum_"

    const-string v11, "deviceType_"

    const-string v12, "rssi_"

    const-string v13, "distance_"

    const-string v14, "altitude_"

    const-string v15, "azimuth_"

    const-string v16, "idHashOffset_"

    const-string v17, "deviceIdHash_"

    const-string v18, "hasLyra_"

    filled-new-array/range {v2 .. v18}, [Ljava/lang/Object;

    move-result-object v0

    const-string v1, "\u0000\u0011\u0000\u0000\u0001\u0013\u0011\u0000\u0000\u0000\u0001Ȉ\u0002Ȉ\u0003Ȉ\u0004Ȉ\u0005Ȉ\u0006\u0004\u0007\u0004\b\u0004\tȈ\n\u0004\u000b\u0004\f\u0004\r\u0001\u000e\u0001\u0011\u0004\u0012Ȉ\u0013\u0007"

    sget-object v2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;

    invoke-static {v2, v1, v0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    return-object v0

    :pswitch_5  #0x2
    new-instance v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint$Builder;

    invoke-direct {v0, v1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    return-object v0

    :pswitch_6  #0x1
    new-instance v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;

    invoke-direct {v0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;-><init>()V

    return-object v0

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
    .registers 23

    goto :goto_23

    nop

    :goto_0
    monitor-enter v1

    :try_start_0
    sget-object v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->PARSER:Lcom/google/protobuf/Parser;

    if-nez v0, :cond_0

    new-instance v0, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;

    sget-object v2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;

    invoke-direct {v0, v2}, Lcom/google/protobuf/GeneratedMessageLite$DefaultInstanceBasedParser;-><init>(Lcom/google/protobuf/GeneratedMessageLite;)V

    sput-object v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_1

    :catchall_0
    move-exception v0

    goto :goto_2

    :cond_0
    :goto_1
    monitor-exit v1

    return-object v0

    :goto_2
    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_2f

    nop

    :goto_3
    throw v0

    :pswitch_0  #0x7
    goto :goto_c

    nop

    :goto_4
    const-string v11, "deviceType_"

    goto :goto_7

    nop

    :goto_5
    const/4 v1, 0x0

    packed-switch v0, :pswitch_data_0

    goto :goto_8

    nop

    :goto_6
    return-object v0

    :pswitch_1  #0x2
    goto :goto_e

    nop

    :goto_7
    const-string v12, "rssi_"

    goto :goto_24

    nop

    :goto_8
    new-instance v0, Ljava/lang/UnsupportedOperationException;

    goto :goto_26

    nop

    :goto_9
    const-string v17, "deviceIdHash_"

    goto :goto_1c

    nop

    :goto_a
    const-string v5, "ip_"

    goto :goto_10

    nop

    :goto_b
    return-object v0

    :pswitch_2  #0x1
    goto :goto_1a

    nop

    :goto_c
    return-object v1

    :pswitch_3  #0x6
    goto :goto_20

    nop

    :goto_d
    aget v0, v0, v1

    goto :goto_5

    nop

    :goto_e
    new-instance v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint$Builder;

    goto :goto_1b

    nop

    :goto_f
    return-object v0

    :pswitch_4  #0x3
    goto :goto_31

    nop

    :goto_10
    const-string v6, "bdAddr_"

    goto :goto_21

    nop

    :goto_11
    const-string v9, "sdkVersion_"

    goto :goto_18

    nop

    :goto_12
    const-string v15, "azimuth_"

    goto :goto_2d

    nop

    :goto_13
    const-string v4, "mac_"

    goto :goto_a

    nop

    :goto_14
    filled-new-array/range {v2 .. v18}, [Ljava/lang/Object;

    move-result-object v0

    goto :goto_1f

    nop

    :goto_15
    return-object v0

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_2  #00000001
        :pswitch_1  #00000002
        :pswitch_4  #00000003
        :pswitch_5  #00000004
        :pswitch_6  #00000005
        :pswitch_3  #00000006
        :pswitch_0  #00000007
    .end packed-switch

    :goto_16
    return-object v0

    :pswitch_5  #0x4
    goto :goto_28

    nop

    :goto_17
    if-eqz v0, :cond_1

    goto :goto_30

    :cond_1
    goto :goto_2e

    nop

    :goto_18
    const-string v10, "compareNum_"

    goto :goto_4

    nop

    :goto_19
    invoke-direct {v0}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;-><init>()V

    goto :goto_15

    nop

    :goto_1a
    new-instance v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;

    goto :goto_19

    nop

    :goto_1b
    invoke-direct {v0, v1}, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint$Builder;-><init>(Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;)V

    goto :goto_b

    nop

    :goto_1c
    const-string v18, "hasLyra_"

    goto :goto_14

    nop

    :goto_1d
    sget-object v2, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;

    goto :goto_2c

    nop

    :goto_1e
    invoke-static {v0}, Ljava/lang/Byte;->valueOf(B)Ljava/lang/Byte;

    move-result-object v0

    goto :goto_2a

    nop

    :goto_1f
    const-string v1, "\u0000\u0011\u0000\u0000\u0001\u0013\u0011\u0000\u0000\u0000\u0001Ȉ\u0002Ȉ\u0003Ȉ\u0004Ȉ\u0005Ȉ\u0006\u0004\u0007\u0004\b\u0004\tȈ\n\u0004\u000b\u0004\f\u0004\r\u0001\u000e\u0001\u0011\u0004\u0012Ȉ\u0013\u0007"

    goto :goto_1d

    nop

    :goto_20
    const/4 v0, 0x1

    goto :goto_1e

    nop

    :goto_21
    const-string v7, "mcVersion_"

    goto :goto_22

    nop

    :goto_22
    const-string v8, "verifyStatus_"

    goto :goto_11

    nop

    :goto_23
    sget-object v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$1;->$SwitchMap$com$google$protobuf$GeneratedMessageLite$MethodToInvoke:[I

    goto :goto_2b

    nop

    :goto_24
    const-string v13, "distance_"

    goto :goto_27

    nop

    :goto_25
    sget-object v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->PARSER:Lcom/google/protobuf/Parser;

    goto :goto_17

    nop

    :goto_26
    invoke-direct {v0}, Ljava/lang/UnsupportedOperationException;-><init>()V

    goto :goto_3

    nop

    :goto_27
    const-string v14, "altitude_"

    goto :goto_12

    nop

    :goto_28
    sget-object v0, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;->DEFAULT_INSTANCE:Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;

    goto :goto_f

    nop

    :goto_29
    const-string v3, "name_"

    goto :goto_13

    nop

    :goto_2a
    return-object v0

    :pswitch_6  #0x5
    goto :goto_25

    nop

    :goto_2b
    invoke-virtual/range {p1 .. p1}, Ljava/lang/Enum;->ordinal()I

    move-result v1

    goto :goto_d

    nop

    :goto_2c
    invoke-static {v2, v1, v0}, Lcom/google/protobuf/GeneratedMessageLite;->newMessageInfo(Lcom/google/protobuf/MessageLite;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_6

    nop

    :goto_2d
    const-string v16, "idHashOffset_"

    goto :goto_9

    nop

    :goto_2e
    const-class v1, Lcom/xiaomi/idm/api/proto/IDMServiceProto$Endpoint;

    goto :goto_0

    nop

    :goto_2f
    throw v0

    :goto_30
    goto :goto_16

    nop

    :goto_31
    const-string v2, "idhash_"

    goto :goto_29

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
