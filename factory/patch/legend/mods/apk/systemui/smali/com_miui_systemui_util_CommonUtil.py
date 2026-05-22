"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/util/CommonUtil.smali
Patches      : 2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/util/CommonUtil.smali'
CLASS_FALLBACK_NAMES = ['CommonUtil.smali']
CLASS_ANCHORS        = ['invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V', 'invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;', 'invoke-virtual {v0, v1}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;', 'invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;', 'invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;']

PATCHES = [
    {
        'id':             'p0000_startCalendarApp',
        'type':           'method_replace',
        'method':         '.method public static startCalendarApp(Landroid/content/Context;)V',
        'method_name':    'startCalendarApp',
        'method_anchors': ['invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V', 'invoke-static {}, Landroid/app/ActivityManager;->getCurrentUser()I', 'invoke-static {p0, v1, v2}, Lcom/miui/utils/PackageUtils;->isAppEnabledForUser(Landroid/content/Context;ILjava/lang/String;)Z'],
        'search':         '.method public static startCalendarApp(Landroid/content/Context;)V\n    .registers 6\n\n    new-instance v0, Landroid/content/Intent;\n\n    const-string v1, "android.intent.action.MAIN"\n\n    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V\n\n    invoke-static {}, Landroid/app/ActivityManager;->getCurrentUser()I\n\n    move-result v1\n\n    sget-boolean v2, Lcom/miui/utils/configs/MiuiConfigs;->IS_INTERNATIONAL_BUILD:Z\n\n    const-string v3, "com.android.calendar"\n\n    if-eqz v2, :cond_2\n\n    const-string v2, "com.xiaomi.calendar"\n\n    invoke-static {p0, v1, v2}, Lcom/miui/utils/PackageUtils;->isAppInstalledForUser(Landroid/content/Context;ILjava/lang/String;)Z\n\n    move-result v4\n\n    if-eqz v4, :cond_0\n\n    move-object v3, v2\n\n    goto :goto_0\n\n    :cond_0\n    invoke-static {p0, v1, v3}, Lcom/miui/utils/PackageUtils;->isAppInstalledForUser(Landroid/content/Context;ILjava/lang/String;)Z\n\n    move-result p0\n\n    if-eqz p0, :cond_1\n\n    goto :goto_0\n\n    :cond_1\n    const-string v3, "com.google.android.calendar"\n\n    :cond_2\n    :goto_0\n    invoke-virtual {v0, v3}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;\n\n    const-string p0, "android.intent.category.LAUNCHER"\n\n    invoke-virtual {v0, p0}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;\n\n    const/high16 p0, 0x10000000\n\n    invoke-virtual {v0, p0}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;\n\n    const-class p0, Lcom/android/systemui/plugins/ActivityStarter;\n\n    invoke-static {p0}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object p0\n\n    check-cast p0, Lcom/android/systemui/plugins/ActivityStarter;\n\n    const/4 v1, 0x1\n\n    invoke-interface {p0, v0, v1}, Lcom/android/systemui/plugins/ActivityStarter;->startActivity(Landroid/content/Intent;Z)V\n\n    return-void\n.end method\n',
        'replacement':    '.method public static startCalendarApp(Landroid/content/Context;)V\n    .registers 5\n\n    new-instance v0, Landroid/content/Intent;\n\n    const-string v1, "android.intent.action.MAIN"\n\n    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V\n\n    invoke-static {}, Landroid/app/ActivityManager;->getCurrentUser()I\n\n    move-result v1\n\n    const-string v2, "com.google.android.calendar"\n\n    invoke-static {p0, v1, v2}, Lcom/miui/utils/PackageUtils;->isAppEnabledForUser(Landroid/content/Context;ILjava/lang/String;)Z\n\n    move-result v3\n\n    if-nez v3, :cond_0\n\n    const-string v2, "com.xiaomi.calendar"\n\n    invoke-static {p0, v1, v2}, Lcom/miui/utils/PackageUtils;->isAppEnabledForUser(Landroid/content/Context;ILjava/lang/String;)Z\n\n    move-result p0\n\n    if-nez p0, :cond_0\n\n    const-string v2, "com.android.calendar"\n\n    :cond_0\n    invoke-virtual {v0, v2}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;\n\n    const-string p0, "android.intent.category.LAUNCHER"\n\n    invoke-virtual {v0, p0}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;\n\n    const/high16 p0, 0x10000000\n\n    invoke-virtual {v0, p0}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;\n\n    const-class p0, Lcom/android/systemui/plugins/ActivityStarter;\n\n    invoke-static {p0}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object p0\n\n    check-cast p0, Lcom/android/systemui/plugins/ActivityStarter;\n\n    const/4 v1, 0x1\n\n    invoke-interface {p0, v0, v1}, Lcom/android/systemui/plugins/ActivityStarter;->startActivity(Landroid/content/Intent;Z)V\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI generated generated dex rule modified class',
    },
    {
        'id':             'p0001_startWeatherApp',
        'type':           'method_add',
        'method':         '.method public static startWeatherApp()V',
        'method_name':    'startWeatherApp',
        'method_anchors': ['invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V', 'invoke-virtual {v0, v1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;', 'invoke-virtual {v0, v1}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;'],
        'search':         None,
        'replacement':    '.method public static startWeatherApp()V\n    .registers 3\n\n    new-instance v0, Landroid/content/Intent;\n\n    const-string v1, "android.intent.action.MAIN"\n\n    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V\n\n    const-string v1, "com.miui.weather2"\n\n    invoke-virtual {v0, v1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;\n\n    const-string v1, "android.intent.category.LAUNCHER"\n\n    invoke-virtual {v0, v1}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;\n\n    const/high16 v1, 0x10000000\n\n    invoke-virtual {v0, v1}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;\n\n    const-class v1, Lcom/android/systemui/plugins/ActivityStarter;\n\n    invoke-static {v1}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v1\n\n    check-cast v1, Lcom/android/systemui/plugins/ActivityStarter;\n\n    const/4 v2, 0x1\n\n    invoke-interface {v1, v0, v2}, Lcom/android/systemui/plugins/ActivityStarter;->startActivity(Landroid/content/Intent;Z)V\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
]
