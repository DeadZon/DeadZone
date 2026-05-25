TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/idm/api/IDMClient$IDMClientCallback.smali'
CLASS_FALLBACK_NAMES = ['IDMClient$IDMClientCallback.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_idm_api_IDMClient__IDMClientCallback__onAccountChanged',
        'method': '.method protected onAccountChanged(Ljava/lang/String;Ljava/lang/String;)V',
        'method_name': 'onAccountChanged',
        'method_anchors': ['const-string p0, "onMiIdentityChanged, newIdHash = [%s], subChangeType = [%s]"', 'const-string p2, "IDMClient"', 'invoke-static {p2, p0, p1}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onAccountChanged(Ljava/lang/String;Ljava/lang/String;)V
    .registers 3

    const-string p0, "onMiIdentityChanged, newIdHash = [%s], subChangeType = [%s]"

    filled-new-array {p1, p2}, [Ljava/lang/Object;

    move-result-object p1

    const-string p2, "IDMClient"

    invoke-static {p2, p0, p1}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    return-void
.end method""",
        'replacement': """.method protected onAccountChanged(Ljava/lang/String;Ljava/lang/String;)V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    const-string p2, "IDMClient"

    goto :goto_1

    nop

    :goto_1
    invoke-static {p2, p0, p1}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_3

    nop

    :goto_2
    filled-new-array {p1, p2}, [Ljava/lang/Object;

    move-result-object p1

    goto :goto_0

    nop

    :goto_3
    return-void

    :goto_4
    const-string p0, "onMiIdentityChanged, newIdHash = [%s], subChangeType = [%s]"

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_xiaomi_idm_api_IDMClient__IDMClientCallback__onBlockReceived',
        'method': '.method protected onBlockReceived(Ljava/lang/String;[B)V',
        'method_name': 'onBlockReceived',
        'method_anchors': ['new-instance p0, Ljava/lang/StringBuilder;', 'invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v0, "onBlockReceived, serviceId = "', 'invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'const-string p1, " data(len) = "', 'invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method protected onBlockReceived(Ljava/lang/String;[B)V
    .registers 4

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "onBlockReceived, serviceId = "

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string p1, " data(len) = "

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    array-length p1, p2

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const/4 p1, 0x0

    new-array p1, p1, [Ljava/lang/Object;

    const-string p2, "IDMClient"

    invoke-static {p2, p0, p1}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    return-void
.end method""",
        'replacement': """.method protected onBlockReceived(Ljava/lang/String;[B)V
    .registers 4

    goto :goto_b

    nop

    :goto_0
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_e

    nop

    :goto_1
    new-array p1, p1, [Ljava/lang/Object;

    goto :goto_8

    nop

    :goto_2
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_3
    const-string v0, "onBlockReceived, serviceId = "

    goto :goto_a

    nop

    :goto_4
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_c

    nop

    :goto_5
    invoke-static {p2, p0, p1}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_d

    nop

    :goto_6
    const-string p1, " data(len) = "

    goto :goto_0

    nop

    :goto_7
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_3

    nop

    :goto_8
    const-string p2, "IDMClient"

    goto :goto_5

    nop

    :goto_9
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_4

    nop

    :goto_a
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2

    nop

    :goto_b
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_c
    const/4 p1, 0x0

    goto :goto_1

    nop

    :goto_d
    return-void

    :goto_e
    array-length p1, p2

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_xiaomi_idm_api_IDMClient__IDMClientCallback__onDiscoveryResult',
        'method': '.method protected onDiscoveryResult(I)V',
        'method_name': 'onDiscoveryResult',
        'method_anchors': ['invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'const-string p1, "IDMClient"', 'const-string v0, "onDiscoveryResult, status = [%d]"', 'invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDiscoveryResult(I)V
    .registers 3

    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p0

    filled-new-array {p0}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "IDMClient"

    const-string v0, "onDiscoveryResult, status = [%d]"

    invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    return-void
.end method""",
        'replacement': """.method protected onDiscoveryResult(I)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_2

    nop

    :goto_1
    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p0

    goto :goto_5

    nop

    :goto_2
    return-void

    :goto_3
    const-string p1, "IDMClient"

    goto :goto_4

    nop

    :goto_4
    const-string v0, "onDiscoveryResult, status = [%d]"

    goto :goto_0

    nop

    :goto_5
    filled-new-array {p0}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_xiaomi_idm_api_IDMClient__IDMClientCallback__onInvitationAccepted',
        'method': '.method protected onInvitationAccepted(Lcom/xiaomi/idm/api/IDMService;)V',
        'method_name': 'onInvitationAccepted',
        'method_anchors': ['invoke-virtual {p1}, Lcom/xiaomi/idm/api/IDMService;->getName()Ljava/lang/String;', 'invoke-virtual {p1}, Lcom/xiaomi/idm/api/IDMService;->getServiceId()Ljava/lang/String;', 'const-string p1, "IDMClient"', 'const-string v0, "onInvitationAccepted, service name = [%s]\\nserviceId = [%s]"', 'invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onInvitationAccepted(Lcom/xiaomi/idm/api/IDMService;)V
    .registers 3

    invoke-virtual {p1}, Lcom/xiaomi/idm/api/IDMService;->getName()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p1}, Lcom/xiaomi/idm/api/IDMService;->getServiceId()Ljava/lang/String;

    move-result-object p1

    filled-new-array {p0, p1}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "IDMClient"

    const-string v0, "onInvitationAccepted, service name = [%s]\nserviceId = [%s]"

    invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    return-void
.end method""",
        'replacement': """.method protected onInvitationAccepted(Lcom/xiaomi/idm/api/IDMService;)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p1}, Lcom/xiaomi/idm/api/IDMService;->getServiceId()Ljava/lang/String;

    move-result-object p1

    goto :goto_1

    nop

    :goto_1
    filled-new-array {p0, p1}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_6

    nop

    :goto_2
    invoke-virtual {p1}, Lcom/xiaomi/idm/api/IDMService;->getName()Ljava/lang/String;

    move-result-object p0

    goto :goto_0

    nop

    :goto_3
    return-void

    :goto_4
    invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_3

    nop

    :goto_5
    const-string v0, "onInvitationAccepted, service name = [%s]\nserviceId = [%s]"

    goto :goto_4

    nop

    :goto_6
    const-string p1, "IDMClient"

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_xiaomi_idm_api_IDMClient__IDMClientCallback__onInviteConnection',
        'method': '.method protected onInviteConnection(ILjava/lang/String;)V',
        'method_name': 'onInviteConnection',
        'method_anchors': ['invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'const-string p1, "IDMClient"', 'const-string p2, "onInviteConnection, code = [%d], inviteStr = [%s]"', 'invoke-static {p1, p2, p0}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onInviteConnection(ILjava/lang/String;)V
    .registers 3

    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p0

    filled-new-array {p0, p2}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "IDMClient"

    const-string p2, "onInviteConnection, code = [%d], inviteStr = [%s]"

    invoke-static {p1, p2, p0}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    return-void
.end method""",
        'replacement': """.method protected onInviteConnection(ILjava/lang/String;)V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    filled-new-array {p0, p2}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    const-string p1, "IDMClient"

    goto :goto_2

    nop

    :goto_2
    const-string p2, "onInviteConnection, code = [%d], inviteStr = [%s]"

    goto :goto_4

    nop

    :goto_3
    return-void

    :goto_4
    invoke-static {p1, p2, p0}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_3

    nop

    :goto_5
    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_xiaomi_idm_api_IDMClient__IDMClientCallback__onRpcChannelConnected',
        'method': '.method protected onRpcChannelConnected(Lcom/xiaomi/idm/bean/RpcChannelStatus;)V',
        'method_name': 'onRpcChannelConnected',
        'method_anchors': ['const-string p1, "IDMClient"', 'const-string v0, "onRpcChannelConnected: No Impl"', 'invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->v(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onRpcChannelConnected(Lcom/xiaomi/idm/bean/RpcChannelStatus;)V
    .registers 3

    const/4 p0, 0x0

    new-array p0, p0, [Ljava/lang/Object;

    const-string p1, "IDMClient"

    const-string v0, "onRpcChannelConnected: No Impl"

    invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->v(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    return-void
.end method""",
        'replacement': """.method protected onRpcChannelConnected(Lcom/xiaomi/idm/bean/RpcChannelStatus;)V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    return-void

    :goto_1
    const-string v0, "onRpcChannelConnected: No Impl"

    goto :goto_4

    nop

    :goto_2
    new-array p0, p0, [Ljava/lang/Object;

    goto :goto_3

    nop

    :goto_3
    const-string p1, "IDMClient"

    goto :goto_1

    nop

    :goto_4
    invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->v(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_0

    nop

    :goto_5
    const/4 p0, 0x0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_xiaomi_idm_api_IDMClient__IDMClientCallback__onRpcChannelDisconnected',
        'method': '.method protected onRpcChannelDisconnected(Lcom/xiaomi/idm/bean/RpcChannelStatus;)V',
        'method_name': 'onRpcChannelDisconnected',
        'method_anchors': ['const-string p1, "IDMClient"', 'const-string v0, "onRpcChannelDisconnected: No Impl"', 'invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->v(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onRpcChannelDisconnected(Lcom/xiaomi/idm/bean/RpcChannelStatus;)V
    .registers 3

    const/4 p0, 0x0

    new-array p0, p0, [Ljava/lang/Object;

    const-string p1, "IDMClient"

    const-string v0, "onRpcChannelDisconnected: No Impl"

    invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->v(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    return-void
.end method""",
        'replacement': """.method protected onRpcChannelDisconnected(Lcom/xiaomi/idm/bean/RpcChannelStatus;)V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    return-void

    :goto_1
    invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->v(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_0

    nop

    :goto_2
    new-array p0, p0, [Ljava/lang/Object;

    goto :goto_4

    nop

    :goto_3
    const-string v0, "onRpcChannelDisconnected: No Impl"

    goto :goto_1

    nop

    :goto_4
    const-string p1, "IDMClient"

    goto :goto_3

    nop

    :goto_5
    const/4 p0, 0x0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_xiaomi_idm_api_IDMClient__IDMClientCallback__onServiceLost',
        'method': '.method protected onServiceLost(Lcom/xiaomi/idm/api/IDMService;)V',
        'method_name': 'onServiceLost',
        'method_anchors': ['invoke-virtual {p1}, Lcom/xiaomi/idm/api/IDMService;->getName()Ljava/lang/String;', 'invoke-virtual {p1}, Lcom/xiaomi/idm/api/IDMService;->getServiceId()Ljava/lang/String;', 'const-string p1, "IDMClient"', 'const-string v0, "onServiceLost, service name = [%s]\\nserviceId = [%s]"', 'invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onServiceLost(Lcom/xiaomi/idm/api/IDMService;)V
    .registers 3

    invoke-virtual {p1}, Lcom/xiaomi/idm/api/IDMService;->getName()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p1}, Lcom/xiaomi/idm/api/IDMService;->getServiceId()Ljava/lang/String;

    move-result-object p1

    filled-new-array {p0, p1}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "IDMClient"

    const-string v0, "onServiceLost, service name = [%s]\nserviceId = [%s]"

    invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    return-void
.end method""",
        'replacement': """.method protected onServiceLost(Lcom/xiaomi/idm/api/IDMService;)V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    invoke-static {p1, v0, p0}, Lcom/xiaomi/idm/util/LogUtil;->d(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    filled-new-array {p0, p1}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_5

    nop

    :goto_3
    invoke-virtual {p1}, Lcom/xiaomi/idm/api/IDMService;->getServiceId()Ljava/lang/String;

    move-result-object p1

    goto :goto_2

    nop

    :goto_4
    invoke-virtual {p1}, Lcom/xiaomi/idm/api/IDMService;->getName()Ljava/lang/String;

    move-result-object p0

    goto :goto_3

    nop

    :goto_5
    const-string p1, "IDMClient"

    goto :goto_6

    nop

    :goto_6
    const-string v0, "onServiceLost, service name = [%s]\nserviceId = [%s]"

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
