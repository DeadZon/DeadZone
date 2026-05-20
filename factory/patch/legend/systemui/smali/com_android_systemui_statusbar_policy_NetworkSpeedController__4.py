"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/policy/NetworkSpeedController$4.smali
Patches      : 3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/policy/NetworkSpeedController$4.smali'
CLASS_FALLBACK_NAMES = ['NetworkSpeedController$4.smali']
CLASS_ANCHORS        = ['value = Lcom/android/systemui/statusbar/policy/NetworkSpeedController;-><init>(Landroid/content/Context;Landroid/os/Looper;Lcom/android/systemui/statusbar/phone/ui/StatusBarIconController;Ljava/util/concurrent/Executor;Lcom/android/systemui/settings/UserTracker;Landroid/net/ConnectivityManager;Lcom/android/systemui/statusbar/policy/MinimalismModeController;Lcom/android/systemui/dump/DumpManager;)V', 'iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$4;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V', 'iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$4;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'invoke-static {v0}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->access$1000(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)V']

PATCHES = [
    {
        'id':             'p0000__init_',
        'type':           'method_add',
        'method':         '.method constructor <init>(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;Landroid/os/Handler;)V',
        'method_name':    '<init>',
        'method_anchors': ['iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$4;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V'],
        'search':         None,
        'replacement':    '.method constructor <init>(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;Landroid/os/Handler;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$4;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0001_onChange',
        'type':           'method_add',
        'method':         '.method public onChange(Z)V',
        'method_name':    'onChange',
        'method_anchors': ['iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$4;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;', 'invoke-static {v0}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->access$1000(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)V', 'iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$4;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;'],
        'search':         None,
        'replacement':    '.method public onChange(Z)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$4;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    invoke-static {v0}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->access$1000(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)V\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$4;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    invoke-static {v0}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->access$800(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)V\n\n    return-void\n.end method\n',
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
