"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/wm/shell/multitasking/stubs/infinitymode/MiuiInfinityModeStatus.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/wm/shell/multitasking/stubs/infinitymode/MiuiInfinityModeStatus.smali'
CLASS_FALLBACK_NAMES = ['MiuiInfinityModeStatus.smali']
CLASS_ANCHORS        = ['invoke-static {v0, v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;', 'invoke-virtual {v2, v3}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z', 'sput-boolean v2, Lcom/android/wm/shell/multitasking/stubs/infinitymode/MiuiInfinityModeStatus;->IS_INTERNATIONAL_BUILD:Z', 'invoke-static {v0, v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;', 'invoke-virtual {v0, v3}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z']

PATCHES = [
    {
        'id':             'p0000__clinit_',
        'type':           'method_replace',
        'method':         '.method static constructor <clinit>()V',
        'method_name':    '<clinit>',
        'method_anchors': ['invoke-static {v0, v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;', 'invoke-virtual {v2, v3}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z', 'sput-boolean v2, Lcom/android/wm/shell/multitasking/stubs/infinitymode/MiuiInfinityModeStatus;->IS_INTERNATIONAL_BUILD:Z'],
        'search':         '.method static constructor <clinit>()V\n    .registers 4\n\n    const-string v0, "ro.product.mod_device"\n\n    const-string v1, ""\n\n    invoke-static {v0, v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;\n\n    move-result-object v2\n\n    const-string v3, "_global"\n\n    invoke-virtual {v2, v3}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z\n\n    move-result v2\n\n    sput-boolean v2, Lcom/android/wm/shell/multitasking/stubs/infinitymode/MiuiInfinityModeStatus;->IS_INTERNATIONAL_BUILD:Z\n\n    invoke-static {v0, v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;\n\n    move-result-object v0\n\n    invoke-virtual {v0, v3}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z\n\n    move-result v0\n\n    sput-boolean v0, Lcom/android/wm/shell/multitasking/stubs/infinitymode/MiuiInfinityModeStatus;->IS_GLOBAL_BUILD:Z\n\n    return-void\n.end method\n',
        'replacement':    '.method static constructor <clinit>()V\n    .registers 4\n\n    const-string v0, "ro.product.device"\n\n    const-string v1, ""\n\n    invoke-static {v0, v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;\n\n    move-result-object v2\n\n    const-string v3, "_global"\n\n    invoke-virtual {v2, v3}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z\n\n    move-result v2\n\n    sput-boolean v2, Lcom/android/wm/shell/multitasking/stubs/infinitymode/MiuiInfinityModeStatus;->IS_INTERNATIONAL_BUILD:Z\n\n    invoke-static {v0, v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;\n\n    move-result-object v0\n\n    invoke-virtual {v0, v3}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z\n\n    move-result v0\n\n    sput-boolean v0, Lcom/android/wm/shell/multitasking/stubs/infinitymode/MiuiInfinityModeStatus;->IS_GLOBAL_BUILD:Z\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
]
