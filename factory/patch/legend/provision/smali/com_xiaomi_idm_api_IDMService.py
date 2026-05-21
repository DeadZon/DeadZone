TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/api/IDMService.smali'
CLASS_FALLBACK_NAMES = ['IDMService.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final TAG:Ljava/lang/String; = "IDMService"', '.field public static final TYPE_HANDOFF:Ljava/lang/String; = "urn:aiot-spec-v3:service:handoff:00000001:1"', '.field public static final TYPE_INPUT:Ljava/lang/String; = "urn:aiot-spec-v3:service:input:00000001:1"', '.field public static final TYPE_IOT:Ljava/lang/String; = "urn:aiot-spec-v3:service:iot-local-control:00000001:1"', '.field public static final TYPE_IPC:Ljava/lang/String; = "urn:aiot-spec-v3:service:ip-camera:00000001:1"']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_api_IDMService__notifyEvent',
        'method': '.method protected notifyEvent(Lcom/xiaomi/idm/api/IDMService$Event;Ljava/lang/String;Z)Lcom/xiaomi/idm/task/CallFuture;',
        'method_name': 'notifyEvent',
        'method_anchors': ['iget-object p0, p0, Lcom/xiaomi/idm/api/IDMService;->mEventCallback:Lcom/xiaomi/idm/api/IDMService$IDMEventCallback;', 'if-eqz p0, :cond_0', 'invoke-interface {p0, p1, p2, p3}, Lcom/xiaomi/idm/api/IDMService$IDMEventCallback;->onNotifyEvent(Lcom/xiaomi/idm/api/IDMService$Event;Ljava/lang/String;Z)Lcom/xiaomi/idm/task/CallFuture;', 'return-object p0', 'new-instance p0, Lcom/xiaomi/idm/exception/EventException;', 'sget-object p1, Lcom/xiaomi/idm/constant/ResponseCode$EventCode;->EVENT_ERR_EVENT_CALLBACK_NOT_SET_YET:Lcom/xiaomi/idm/constant/ResponseCode$EventCode;', 'invoke-direct {p0, p1}, Lcom/xiaomi/idm/exception/EventException;-><init>(Lcom/xiaomi/idm/constant/ResponseCode$EventCode;)V'],
        'type': 'method_replace',
        'search': """.method protected notifyEvent(Lcom/xiaomi/idm/api/IDMService$Event;Ljava/lang/String;Z)Lcom/xiaomi/idm/task/CallFuture;
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Ljava/lang/Object;",
            ">(",
            "Lcom/xiaomi/idm/api/IDMService$Event;",
            "Ljava/lang/String;",
            "Z)",
            "Lcom/xiaomi/idm/task/CallFuture;"
        }
    .end annotation

    .annotation system Ldalvik/annotation/Throws;
        value = {
            Lcom/xiaomi/idm/exception/EventException;
        }
    .end annotation

    iget-object p0, p0, Lcom/xiaomi/idm/api/IDMService;->mEventCallback:Lcom/xiaomi/idm/api/IDMService$IDMEventCallback;

    if-eqz p0, :cond_0

    invoke-interface {p0, p1, p2, p3}, Lcom/xiaomi/idm/api/IDMService$IDMEventCallback;->onNotifyEvent(Lcom/xiaomi/idm/api/IDMService$Event;Ljava/lang/String;Z)Lcom/xiaomi/idm/task/CallFuture;

    move-result-object p0

    return-object p0

    :cond_0
    new-instance p0, Lcom/xiaomi/idm/exception/EventException;

    sget-object p1, Lcom/xiaomi/idm/constant/ResponseCode$EventCode;->EVENT_ERR_EVENT_CALLBACK_NOT_SET_YET:Lcom/xiaomi/idm/constant/ResponseCode$EventCode;

    invoke-direct {p0, p1}, Lcom/xiaomi/idm/exception/EventException;-><init>(Lcom/xiaomi/idm/constant/ResponseCode$EventCode;)V

    throw p0
.end method""",
        'replacement': """.method protected notifyEvent(Lcom/xiaomi/idm/api/IDMService$Event;Ljava/lang/String;Z)Lcom/xiaomi/idm/task/CallFuture;
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Ljava/lang/Object;",
            ">(",
            "Lcom/xiaomi/idm/api/IDMService$Event;",
            "Ljava/lang/String;",
            "Z)",
            "Lcom/xiaomi/idm/task/CallFuture;"
        }
    .end annotation

    .annotation system Ldalvik/annotation/Throws;
        value = {
            Lcom/xiaomi/idm/exception/EventException;
        }
    .end annotation

    goto :goto_7

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_3

    nop

    :goto_1
    new-instance p0, Lcom/xiaomi/idm/exception/EventException;

    goto :goto_6

    nop

    :goto_2
    invoke-direct {p0, p1}, Lcom/xiaomi/idm/exception/EventException;-><init>(Lcom/xiaomi/idm/constant/ResponseCode$EventCode;)V

    goto :goto_8

    nop

    :goto_3
    invoke-interface {p0, p1, p2, p3}, Lcom/xiaomi/idm/api/IDMService$IDMEventCallback;->onNotifyEvent(Lcom/xiaomi/idm/api/IDMService$Event;Ljava/lang/String;Z)Lcom/xiaomi/idm/task/CallFuture;

    move-result-object p0

    goto :goto_4

    nop

    :goto_4
    return-object p0

    :goto_5
    goto :goto_1

    nop

    :goto_6
    sget-object p1, Lcom/xiaomi/idm/constant/ResponseCode$EventCode;->EVENT_ERR_EVENT_CALLBACK_NOT_SET_YET:Lcom/xiaomi/idm/constant/ResponseCode$EventCode;

    goto :goto_2

    nop

    :goto_7
    iget-object p0, p0, Lcom/xiaomi/idm/api/IDMService;->mEventCallback:Lcom/xiaomi/idm/api/IDMService$IDMEventCallback;

    goto :goto_0

    nop

    :goto_8
    throw p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_xiaomi_idm_api_IDMService__setServiceId',
        'method': '.method setServiceId(Ljava/lang/String;)V',
        'method_name': 'setServiceId',
        'method_anchors': ['iput-object p1, p0, Lcom/xiaomi/idm/api/IDMService;->mServiceId:Ljava/lang/String;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setServiceId(Ljava/lang/String;)V
    .registers 2

    iput-object p1, p0, Lcom/xiaomi/idm/api/IDMService;->mServiceId:Ljava/lang/String;

    return-void
.end method""",
        'replacement': """.method setServiceId(Ljava/lang/String;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-object p1, p0, Lcom/xiaomi/idm/api/IDMService;->mServiceId:Ljava/lang/String;

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
