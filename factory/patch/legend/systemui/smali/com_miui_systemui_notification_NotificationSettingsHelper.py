"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/notification/NotificationSettingsHelper.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/notification/NotificationSettingsHelper.smali'
CLASS_FALLBACK_NAMES = ['NotificationSettingsHelper.smali']
CLASS_ANCHORS        = ['sget-boolean v0, Lcom/miui/utils/configs/MiuiDebugConfig;->DEBUG_NOTIFICATION:Z', 'sput-boolean v0, Lcom/miui/systemui/notification/NotificationSettingsHelper;->DEBUG:Z', 'invoke-static {v0}, Landroid/os/ServiceManager;->getService(Ljava/lang/String;)Landroid/os/IBinder;', 'invoke-static {v0}, Landroid/app/INotificationManager$Stub;->asInterface(Landroid/os/IBinder;)Landroid/app/INotificationManager;', 'sput-object v0, Lcom/miui/systemui/notification/NotificationSettingsHelper;->sINM:Landroid/app/INotificationManager;']

PATCHES = [
    {
        'id':             'p0000_showMezoStyle',
        'type':           'method_add',
        'method':         '.method public static showMezoStyle()Z',
        'method_name':    'showMezoStyle',
        'method_anchors': ['invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I'],
        'search':         None,
        'replacement':    '.method public static showMezoStyle()Z\n    .registers 2\n\n    const/4 v1, 0x1\n\n    const-string v0, "icon_mezo_app_color"\n\n    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v0\n\n    return v0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
]
