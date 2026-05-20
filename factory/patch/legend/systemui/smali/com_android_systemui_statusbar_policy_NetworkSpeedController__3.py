"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/policy/NetworkSpeedController$3.smali
Patches      : 3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/policy/NetworkSpeedController$3.smali'
CLASS_FALLBACK_NAMES = ['NetworkSpeedController$3.smali']
CLASS_ANCHORS        = ['iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'invoke-direct {p0}, Ljava/lang/Object;-><init>()V', 'iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'iput p1, v0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->mCurrentUserId:I', 'iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;']

PATCHES = [
    {
        'id':             'p0000__init_',
        'type':           'method_add',
        'method':         '.method constructor <init>(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)V',
        'method_name':    '<init>',
        'method_anchors': ['iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'invoke-direct {p0}, Ljava/lang/Object;-><init>()V'],
        'search':         None,
        'replacement':    '.method constructor <init>(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0001_onUserChanged',
        'type':           'method_add',
        'method':         '.method public final onUserChanged(ILandroid/content/Context;)V',
        'method_name':    'onUserChanged',
        'method_anchors': ['iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'iput p1, v0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->mCurrentUserId:I', 'iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;'],
        'search':         None,
        'replacement':    '.method public final onUserChanged(ILandroid/content/Context;)V\n    .registers 5\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    iput p1, v0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->mCurrentUserId:I\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    invoke-static {v0}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->access$100(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)Landroid/os/Handler;\n\n    move-result-object v0\n\n    new-instance v1, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3$1;\n\n    invoke-direct {v1, p0}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3$1;-><init>(Lcom/android/systemui/statusbar/policy/NetworkSpeedController$3;)V\n\n    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0002_field__field_final_synthet',
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
