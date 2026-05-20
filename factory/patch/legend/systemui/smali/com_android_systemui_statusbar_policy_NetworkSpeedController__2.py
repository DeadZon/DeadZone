"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/policy/NetworkSpeedController$2.smali
Patches      : 4
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/policy/NetworkSpeedController$2.smali'
CLASS_FALLBACK_NAMES = ['NetworkSpeedController$2.smali']
CLASS_ANCHORS        = ['iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'iget-object v0, v0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->mNetworks:Ljava/util/HashSet;', 'iget-object v1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'invoke-static {v1, p1}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->access$600(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;Landroid/net/Network;)I']

PATCHES = [
    {
        'id':             'p0000__init_',
        'type':           'method_add',
        'method':         '.method constructor <init>(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)V',
        'method_name':    '<init>',
        'method_anchors': ['iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'invoke-direct {p0}, Landroid/net/ConnectivityManager$NetworkCallback;-><init>()V'],
        'search':         None,
        'replacement':    '.method constructor <init>(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    invoke-direct {p0}, Landroid/net/ConnectivityManager$NetworkCallback;-><init>()V\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0001_onAvailable',
        'type':           'method_add',
        'method':         '.method public onAvailable(Landroid/net/Network;)V',
        'method_name':    'onAvailable',
        'method_anchors': ['iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'iget-object v0, v0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->mNetworks:Ljava/util/HashSet;', 'iget-object v1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;'],
        'search':         None,
        'replacement':    '.method public onAvailable(Landroid/net/Network;)V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    iget-object v0, v0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->mNetworks:Ljava/util/HashSet;\n\n    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    invoke-static {v1, p1}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->access$600(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;Landroid/net/Network;)I\n\n    move-result v1\n\n    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;\n\n    move-result-object v1\n\n    invoke-virtual {v0, v1}, Ljava/util/HashSet;->add(Ljava/lang/Object;)Z\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    invoke-static {v0}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->access$700(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)V\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0002_onLost',
        'type':           'method_add',
        'method':         '.method public onLost(Landroid/net/Network;)V',
        'method_name':    'onLost',
        'method_anchors': ['iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'iget-object v0, v0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->mNetworks:Ljava/util/HashSet;', 'iget-object v1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;'],
        'search':         None,
        'replacement':    '.method public onLost(Landroid/net/Network;)V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    iget-object v0, v0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->mNetworks:Ljava/util/HashSet;\n\n    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    invoke-static {v1, p1}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->access$600(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;Landroid/net/Network;)I\n\n    move-result v1\n\n    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;\n\n    move-result-object v1\n\n    invoke-virtual {v0, v1}, Ljava/util/HashSet;->remove(Ljava/lang/Object;)Z\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$2;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    invoke-static {v0}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->access$700(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)V\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0003_field__field_final_synthet',
        'type':           'field_add',
        'method':         '.field final synthetic this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field final synthetic this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added field',
    },
]
