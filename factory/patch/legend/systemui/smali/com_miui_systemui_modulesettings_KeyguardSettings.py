"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/modulesettings/KeyguardSettings.smali
Patches      : 2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/modulesettings/KeyguardSettings.smali'
CLASS_FALLBACK_NAMES = ['KeyguardSettings.smali']
CLASS_ANCHORS        = ['invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;', 'sput-object v0, Lcom/miui/systemui/modulesettings/KeyguardSettings;->WAKEUP_FOR_NOTIFICATION:Landroid/net/Uri;', 'invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;', 'sput-object v0, Lcom/miui/systemui/modulesettings/KeyguardSettings;->CHARGE_ANIM_TYPE:Landroid/net/Uri;']

PATCHES = [
    {
        'id':             'p0000__clinit_',
        'type':           'method_replace',
        'method':         '.method static constructor <clinit>()V',
        'method_name':    '<clinit>',
        'method_anchors': ['invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;', 'sput-object v0, Lcom/miui/systemui/modulesettings/KeyguardSettings;->WAKEUP_FOR_NOTIFICATION:Landroid/net/Uri;', 'invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;'],
        'search':         '.method static constructor <clinit>()V\n    .registers 1\n\n    const-string v0, "wakeup_for_keyguard_notification"\n\n    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;\n\n    move-result-object v0\n\n    sput-object v0, Lcom/miui/systemui/modulesettings/KeyguardSettings;->WAKEUP_FOR_NOTIFICATION:Landroid/net/Uri;\n\n    return-void\n.end method\n',
        'replacement':    '.method static constructor <clinit>()V\n    .registers 1\n\n    const-string v0, "wakeup_for_keyguard_notification"\n\n    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;\n\n    move-result-object v0\n\n    sput-object v0, Lcom/miui/systemui/modulesettings/KeyguardSettings;->WAKEUP_FOR_NOTIFICATION:Landroid/net/Uri;\n\n    const-string v0, "charge_animation_type"\n\n    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;\n\n    move-result-object v0\n\n    sput-object v0, Lcom/miui/systemui/modulesettings/KeyguardSettings;->CHARGE_ANIM_TYPE:Landroid/net/Uri;\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
    {
        'id':             'p0001_field__field_public_static',
        'type':           'field_add',
        'method':         '.field public static final CHARGE_ANIM_TYPE:Landroid/net/Uri;',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field public static final CHARGE_ANIM_TYPE:Landroid/net/Uri;',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added field',
    },
]
