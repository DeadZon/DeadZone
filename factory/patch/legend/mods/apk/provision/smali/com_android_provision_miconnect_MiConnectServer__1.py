TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/miconnect/MiConnectServer$1.smali'
CLASS_FALLBACK_NAMES = ['MiConnectServer$1.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/miconnect/MiMoverService$Skeleton;']

PATCHES = [
    {
        'id': 'com_android_provision_miconnect_MiConnectServer__1__onSubscribeAPEvent',
        'method': '.method protected onSubscribeAPEvent(Lcom/xiaomi/idm/bean/ClientInfo;Z)Z',
        'method_name': 'onSubscribeAPEvent',
        'method_anchors': ['invoke-static {}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$sfgetTAG()Ljava/lang/String;', 'new-instance v1, Ljava/lang/StringBuilder;', 'invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v2, "onSubscribeAPEvent: "', 'invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p1}, Lcom/xiaomi/idm/bean/ClientInfo;->toString()Ljava/lang/String;', 'invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'const-string v2, " enabled: "'],
        'type': 'method_replace',
        'search': """.method protected onSubscribeAPEvent(Lcom/xiaomi/idm/bean/ClientInfo;Z)Z
    .registers 6

    invoke-static {}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$sfgetTAG()Ljava/lang/String;

    move-result-object v0

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "onSubscribeAPEvent: "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Lcom/xiaomi/idm/bean/ClientInfo;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v2, " enabled: "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, p2}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-super {p0, p1, p2}, Lcom/android/provision/miconnect/MiMoverService$Skeleton;->onSubscribeAPEvent(Lcom/xiaomi/idm/bean/ClientInfo;Z)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected onSubscribeAPEvent(Lcom/xiaomi/idm/bean/ClientInfo;Z)Z
    .registers 6

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p1}, Lcom/xiaomi/idm/bean/ClientInfo;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_a

    nop

    :goto_1
    invoke-static {}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$sfgetTAG()Ljava/lang/String;

    move-result-object v0

    goto :goto_c

    nop

    :goto_2
    const-string v2, "onSubscribeAPEvent: "

    goto :goto_5

    nop

    :goto_3
    const-string v2, " enabled: "

    goto :goto_9

    nop

    :goto_4
    invoke-super {p0, p1, p2}, Lcom/android/provision/miconnect/MiMoverService$Skeleton;->onSubscribeAPEvent(Lcom/xiaomi/idm/bean/ClientInfo;Z)Z

    move-result p0

    goto :goto_d

    nop

    :goto_5
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    nop

    :goto_6
    invoke-virtual {v1, p2}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_7
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    goto :goto_8

    nop

    :goto_8
    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_4

    nop

    :goto_9
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_a
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_3

    nop

    :goto_b
    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_2

    nop

    :goto_c
    new-instance v1, Ljava/lang/StringBuilder;

    goto :goto_b

    nop

    :goto_d
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_miconnect_MiConnectServer__1__onSubscribeAPEventSuccess',
        'method': '.method protected onSubscribeAPEventSuccess(Lcom/xiaomi/idm/bean/ClientInfo;)V',
        'method_name': 'onSubscribeAPEventSuccess',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/miconnect/MiMoverService$Skeleton;->onSubscribeAPEventSuccess(Lcom/xiaomi/idm/bean/ClientInfo;)V', 'invoke-static {}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$sfgetTAG()Ljava/lang/String;', 'new-instance v1, Ljava/lang/StringBuilder;', 'invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v2, "onSubscribeAPEventSuccess: "', 'invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;', 'invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method protected onSubscribeAPEventSuccess(Lcom/xiaomi/idm/bean/ClientInfo;)V
    .registers 5

    invoke-super {p0, p1}, Lcom/android/provision/miconnect/MiMoverService$Skeleton;->onSubscribeAPEventSuccess(Lcom/xiaomi/idm/bean/ClientInfo;)V

    invoke-static {}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$sfgetTAG()Ljava/lang/String;

    move-result-object v0

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "onSubscribeAPEventSuccess: "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    invoke-static {v0, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object p1, p0, Lcom/android/provision/miconnect/MiConnectServer$1;->this$0:Lcom/android/provision/miconnect/MiConnectServer;

    invoke-static {p1}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$fgetmServerCallback(Lcom/android/provision/miconnect/MiConnectServer;)Lcom/android/provision/miconnect/MiConnectServer$ServerCallback;

    move-result-object p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/miconnect/MiConnectServer$1;->this$0:Lcom/android/provision/miconnect/MiConnectServer;

    invoke-static {p1}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$fgetmServerCallback(Lcom/android/provision/miconnect/MiConnectServer;)Lcom/android/provision/miconnect/MiConnectServer$ServerCallback;

    move-result-object p1

    invoke-interface {p1}, Lcom/android/provision/miconnect/MiConnectServer$ServerCallback;->onClientSubscribed()V

    :cond_0
    iget-object p1, p0, Lcom/android/provision/miconnect/MiConnectServer$1;->this$0:Lcom/android/provision/miconnect/MiConnectServer;

    invoke-static {p1}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$fgetmSSIDToken(Lcom/android/provision/miconnect/MiConnectServer;)I

    move-result v0

    iget-object p0, p0, Lcom/android/provision/miconnect/MiConnectServer$1;->this$0:Lcom/android/provision/miconnect/MiConnectServer;

    invoke-static {p0}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$fgetmPWDToken(Lcom/android/provision/miconnect/MiConnectServer;)I

    move-result p0

    invoke-static {p1, v0, p0}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$mnotifyApData(Lcom/android/provision/miconnect/MiConnectServer;II)V

    return-void
.end method""",
        'replacement': """.method protected onSubscribeAPEventSuccess(Lcom/xiaomi/idm/bean/ClientInfo;)V
    .registers 5

    goto :goto_e

    nop

    :goto_0
    invoke-static {}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$sfgetTAG()Ljava/lang/String;

    move-result-object v0

    goto :goto_4

    nop

    :goto_1
    invoke-static {p1, v0, p0}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$mnotifyApData(Lcom/android/provision/miconnect/MiConnectServer;II)V

    goto :goto_6

    nop

    :goto_2
    invoke-static {p1}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$fgetmSSIDToken(Lcom/android/provision/miconnect/MiConnectServer;)I

    move-result v0

    goto :goto_13

    nop

    :goto_3
    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_9

    nop

    :goto_4
    new-instance v1, Ljava/lang/StringBuilder;

    goto :goto_3

    nop

    :goto_5
    invoke-static {v0, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_a

    nop

    :goto_6
    return-void

    :goto_7
    iget-object p1, p0, Lcom/android/provision/miconnect/MiConnectServer$1;->this$0:Lcom/android/provision/miconnect/MiConnectServer;

    goto :goto_11

    nop

    :goto_8
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_12

    nop

    :goto_9
    const-string v2, "onSubscribeAPEventSuccess: "

    goto :goto_8

    nop

    :goto_a
    iget-object p1, p0, Lcom/android/provision/miconnect/MiConnectServer$1;->this$0:Lcom/android/provision/miconnect/MiConnectServer;

    goto :goto_10

    nop

    :goto_b
    invoke-interface {p1}, Lcom/android/provision/miconnect/MiConnectServer$ServerCallback;->onClientSubscribed()V

    :goto_c
    goto :goto_15

    nop

    :goto_d
    if-nez p1, :cond_0

    goto :goto_c

    :cond_0
    goto :goto_7

    nop

    :goto_e
    invoke-super {p0, p1}, Lcom/android/provision/miconnect/MiMoverService$Skeleton;->onSubscribeAPEventSuccess(Lcom/xiaomi/idm/bean/ClientInfo;)V

    goto :goto_0

    nop

    :goto_f
    invoke-static {p0}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$fgetmPWDToken(Lcom/android/provision/miconnect/MiConnectServer;)I

    move-result p0

    goto :goto_1

    nop

    :goto_10
    invoke-static {p1}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$fgetmServerCallback(Lcom/android/provision/miconnect/MiConnectServer;)Lcom/android/provision/miconnect/MiConnectServer$ServerCallback;

    move-result-object p1

    goto :goto_d

    nop

    :goto_11
    invoke-static {p1}, Lcom/android/provision/miconnect/MiConnectServer;->-$$Nest$fgetmServerCallback(Lcom/android/provision/miconnect/MiConnectServer;)Lcom/android/provision/miconnect/MiConnectServer$ServerCallback;

    move-result-object p1

    goto :goto_b

    nop

    :goto_12
    invoke-virtual {v1, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_14

    nop

    :goto_13
    iget-object p0, p0, Lcom/android/provision/miconnect/MiConnectServer$1;->this$0:Lcom/android/provision/miconnect/MiConnectServer;

    goto :goto_f

    nop

    :goto_14
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_5

    nop

    :goto_15
    iget-object p1, p0, Lcom/android/provision/miconnect/MiConnectServer$1;->this$0:Lcom/android/provision/miconnect/MiConnectServer;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
