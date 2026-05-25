TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/miconnect/MiMoverService$Events$APEvent.smali'
CLASS_FALLBACK_NAMES = ['MiMoverService$Events$APEvent.smali']
CLASS_ANCHORS = ['.super Lcom/xiaomi/idm/api/IDMService$Event;']

PATCHES = [
    {
        'id': 'com_android_provision_miconnect_MiMoverService__Events__APEvent__onEvent',
        'method': '.method protected onEvent([B)[B',
        'method_name': 'onEvent',
        'method_anchors': ['invoke-static {p1}, LMiMoverService/proto/MiMoverServiceProto$APEvent;->parseFrom([B)LMiMoverService/proto/MiMoverServiceProto$APEvent;', 'iget-object p0, p0, Lcom/android/provision/miconnect/MiMoverService$Events$APEvent;->callback:Lcom/android/provision/miconnect/MiMoverService$Events$APEvent$Callback;', 'invoke-virtual {p1}, LMiMoverService/proto/MiMoverServiceProto$APEvent;->getNameToken()I', 'invoke-virtual {p1}, LMiMoverService/proto/MiMoverServiceProto$APEvent;->getPwdToken()I', 'invoke-interface {p0, v0, p1}, Lcom/android/provision/miconnect/MiMoverService$Events$APEvent$Callback;->onAPEvent(II)V', 'return-object p0', 'const-string p1, "MiMoverService"', 'invoke-virtual {p0}, Ljava/io/IOException;->getMessage()Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method protected onEvent([B)[B
    .registers 3
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Lcom/xiaomi/idm/exception/RmiException;
        }
    .end annotation

    :try_start_0
    invoke-static {p1}, LMiMoverService/proto/MiMoverServiceProto$APEvent;->parseFrom([B)LMiMoverService/proto/MiMoverServiceProto$APEvent;

    move-result-object p1
    :try_end_0
    .catch Lcom/google/protobuf/InvalidProtocolBufferException; {:try_start_0 .. :try_end_0} :catch_0

    iget-object p0, p0, Lcom/android/provision/miconnect/MiMoverService$Events$APEvent;->callback:Lcom/android/provision/miconnect/MiMoverService$Events$APEvent$Callback;

    invoke-virtual {p1}, LMiMoverService/proto/MiMoverServiceProto$APEvent;->getNameToken()I

    move-result v0

    invoke-virtual {p1}, LMiMoverService/proto/MiMoverServiceProto$APEvent;->getPwdToken()I

    move-result p1

    invoke-interface {p0, v0, p1}, Lcom/android/provision/miconnect/MiMoverService$Events$APEvent$Callback;->onAPEvent(II)V

    const/4 p0, 0x0

    return-object p0

    :catch_0
    move-exception p0

    const-string p1, "MiMoverService"

    invoke-virtual {p0}, Ljava/io/IOException;->getMessage()Ljava/lang/String;

    move-result-object v0

    invoke-static {p1, v0, p0}, Lcom/xiaomi/mi_connect_sdk/util/LogUtil;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V

    new-instance p0, Lcom/xiaomi/idm/exception/EventException;

    sget-object p1, Lcom/xiaomi/idm/constant/ResponseCode$EventCode;->EVENT_ERR_PARSE_REQUEST_ERR:Lcom/xiaomi/idm/constant/ResponseCode$EventCode;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/exception/EventException;-><init>(Lcom/xiaomi/idm/constant/ResponseCode$EventCode;)V

    throw p0
.end method""",
        'replacement': """.method protected onEvent([B)[B
    .registers 3
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Lcom/xiaomi/idm/exception/RmiException;
        }
    .end annotation

    :try_start_0
    invoke-static {p1}, LMiMoverService/proto/MiMoverServiceProto$APEvent;->parseFrom([B)LMiMoverService/proto/MiMoverServiceProto$APEvent;

    move-result-object p1
    :try_end_0
    .catch Lcom/google/protobuf/InvalidProtocolBufferException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_3

    nop

    :goto_0
    invoke-interface {p0, v0, p1}, Lcom/android/provision/miconnect/MiMoverService$Events$APEvent$Callback;->onAPEvent(II)V

    goto :goto_1

    nop

    :goto_1
    const/4 p0, 0x0

    goto :goto_2

    nop

    :goto_2
    return-object p0

    :catch_0
    move-exception p0

    goto :goto_c

    nop

    :goto_3
    iget-object p0, p0, Lcom/android/provision/miconnect/MiMoverService$Events$APEvent;->callback:Lcom/android/provision/miconnect/MiMoverService$Events$APEvent$Callback;

    goto :goto_6

    nop

    :goto_4
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/exception/EventException;-><init>(Lcom/xiaomi/idm/constant/ResponseCode$EventCode;)V

    goto :goto_a

    nop

    :goto_5
    new-instance p0, Lcom/xiaomi/idm/exception/EventException;

    goto :goto_b

    nop

    :goto_6
    invoke-virtual {p1}, LMiMoverService/proto/MiMoverServiceProto$APEvent;->getNameToken()I

    move-result v0

    goto :goto_8

    nop

    :goto_7
    invoke-virtual {p0}, Ljava/io/IOException;->getMessage()Ljava/lang/String;

    move-result-object v0

    goto :goto_9

    nop

    :goto_8
    invoke-virtual {p1}, LMiMoverService/proto/MiMoverServiceProto$APEvent;->getPwdToken()I

    move-result p1

    goto :goto_0

    nop

    :goto_9
    invoke-static {p1, v0, p0}, Lcom/xiaomi/mi_connect_sdk/util/LogUtil;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V

    goto :goto_5

    nop

    :goto_a
    throw p0

    :goto_b
    sget-object p1, Lcom/xiaomi/idm/constant/ResponseCode$EventCode;->EVENT_ERR_PARSE_REQUEST_ERR:Lcom/xiaomi/idm/constant/ResponseCode$EventCode;

    goto :goto_4

    nop

    :goto_c
    const-string p1, "MiMoverService"

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
