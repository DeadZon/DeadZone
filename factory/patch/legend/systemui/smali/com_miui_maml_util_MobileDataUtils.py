"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/maml/util/MobileDataUtils.smali
Patches      : 4
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/maml/util/MobileDataUtils.smali'
CLASS_FALLBACK_NAMES = ['MobileDataUtils.smali']
CLASS_ANCHORS        = ['invoke-direct {p0}, Lcom/miui/maml/util/BaseMobileDataUtils;-><init>()V', 'invoke-static {v0}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;', 'invoke-virtual {v0}, Ljava/lang/Class;->newInstance()Ljava/lang/Object;', 'invoke-direct {v0}, Lcom/miui/maml/util/MobileDataUtils;-><init>()V', 'invoke-virtual {p1, p0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;']

PATCHES = [
    {
        'id':             'p0000_enableMobileData',
        'type':           'method_replace',
        'method':         '.method public enableMobileData(Landroid/content/Context;Z)V',
        'method_name':    'enableMobileData',
        'method_anchors': ['invoke-virtual {p1, p0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;', 'invoke-virtual {p0, p2}, Landroid/telephony/TelephonyManager;->setDataEnabled(Z)V'],
        'search':         '.method public enableMobileData(Landroid/content/Context;Z)V\n    .registers 6\n\n    :try_start_0\n    const-string p0, "connectivity"\n\n    invoke-virtual {p1, p0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;\n\n    move-result-object p0\n\n    check-cast p0, Landroid/net/ConnectivityManager;\n\n    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;\n\n    move-result-object p1\n\n    const-string p2, "setMobileDataEnabled"\n\n    const/4 v0, 0x1\n\n    new-array v0, v0, [Ljava/lang/Class;\n\n    sget-object v1, Ljava/lang/Boolean;->TYPE:Ljava/lang/Class;\n\n    const/4 v2, 0x0\n\n    aput-object v1, v0, v2\n\n    sget-object v1, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;\n\n    filled-new-array {v1}, [Ljava/lang/Object;\n\n    move-result-object v1\n\n    invoke-static {p1, p0, p2, v0, v1}, Lcom/miui/maml/util/ReflectionHelper;->invoke(Ljava/lang/Class;Ljava/lang/Object;Ljava/lang/String;[Ljava/lang/Class;[Ljava/lang/Object;)V\n    :try_end_0\n    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0\n\n    return-void\n\n    :catch_0\n    move-exception p0\n\n    new-instance p1, Ljava/lang/StringBuilder;\n\n    const-string p2, "Invoke | ConnectivityManager_enableMobileData() occur EXCEPTION: "\n\n    invoke-direct {p1, p2}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V\n\n    const-string p2, "BaseMobileDataUtils"\n\n    invoke-static {p0, p1, p2}, Lcom/android/keyguard/WallpaperProvider$$ExternalSyntheticOutline0;->m(Ljava/lang/Exception;Ljava/lang/StringBuilder;Ljava/lang/String;)V\n\n    return-void\n.end method\n',
        'replacement':    '.method public enableMobileData(Landroid/content/Context;Z)V\n    .registers 3\n\n    const-string p0, "phone"\n\n    invoke-virtual {p1, p0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;\n\n    move-result-object p0\n\n    check-cast p0, Landroid/telephony/TelephonyManager;\n\n    invoke-virtual {p0, p2}, Landroid/telephony/TelephonyManager;->setDataEnabled(Z)V\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
    {
        'id':             'p0001_getMobileDataUri',
        'type':           'method_add',
        'method':         '.method public getMobileDataUri(I)Landroid/net/Uri;',
        'method_name':    'getMobileDataUri',
        'method_anchors': ['invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V', 'invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;'],
        'search':         None,
        'replacement':    '.method public getMobileDataUri(I)Landroid/net/Uri;\n    .registers 3\n\n    new-instance p0, Ljava/lang/StringBuilder;\n\n    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V\n\n    const-string v0, "mobile_data"\n\n    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;\n\n    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;\n\n    move-result-object p0\n\n    invoke-static {p0}, Landroid/provider/Settings$Global;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;\n\n    move-result-object p0\n\n    return-object p0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0002_isMobileEnable',
        'type':           'method_add',
        'method':         '.method public isMobileEnable(Landroid/content/Context;)Z',
        'method_name':    'isMobileEnable',
        'method_anchors': ['sget v0, Landroid/os/Build$VERSION;->SDK_INT:I', 'invoke-virtual {p1, p0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;', 'invoke-virtual {p0}, Landroid/telephony/TelephonyManager;->getDataEnabled()Z'],
        'search':         None,
        'replacement':    '.method public isMobileEnable(Landroid/content/Context;)Z\n    .registers 4\n\n    sget v0, Landroid/os/Build$VERSION;->SDK_INT:I\n\n    const/16 v1, 0x17\n\n    if-le v0, v1, :cond_0\n\n    const-string p0, "phone"\n\n    invoke-virtual {p1, p0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;\n\n    move-result-object p0\n\n    check-cast p0, Landroid/telephony/TelephonyManager;\n\n    invoke-virtual {p0}, Landroid/telephony/TelephonyManager;->getDataEnabled()Z\n\n    move-result p0\n\n    return p0\n\n    :cond_0\n    invoke-super {p0, p1}, Lcom/miui/maml/util/BaseMobileDataUtils;->isMobileEnable(Landroid/content/Context;)Z\n\n    move-result p0\n\n    return p0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0003_registerContentObserver',
        'type':           'method_replace',
        'method':         '.method public registerContentObserver(Landroid/content/Context;Landroid/database/ContentObserver;)V',
        'method_name':    'registerContentObserver',
        'method_anchors': ['invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;', 'invoke-virtual {p0}, Lcom/miui/maml/util/BaseMobileDataUtils;->getMobileDataUri()Landroid/net/Uri;', 'invoke-virtual {v0, v1, v2, p2}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V'],
        'search':         '.method public registerContentObserver(Landroid/content/Context;Landroid/database/ContentObserver;)V\n    .registers 4\n\n    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;\n\n    move-result-object p1\n\n    invoke-virtual {p0}, Lcom/miui/maml/util/BaseMobileDataUtils;->getMobileDataUri()Landroid/net/Uri;\n\n    move-result-object p0\n\n    const/4 v0, 0x0\n\n    invoke-virtual {p1, p0, v0, p2}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V\n\n    return-void\n.end method\n',
        'replacement':    '.method public registerContentObserver(Landroid/content/Context;Landroid/database/ContentObserver;)V\n    .registers 8\n\n    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;\n\n    move-result-object v0\n\n    invoke-virtual {p0}, Lcom/miui/maml/util/BaseMobileDataUtils;->getMobileDataUri()Landroid/net/Uri;\n\n    move-result-object v1\n\n    const/4 v2, 0x0\n\n    invoke-virtual {v0, v1, v2, p2}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V\n\n    const-string v0, "phone"\n\n    invoke-virtual {p1, v0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Landroid/telephony/TelephonyManager;\n\n    const/4 v1, 0x0\n\n    :goto_0\n    invoke-virtual {v0}, Landroid/telephony/TelephonyManager;->getPhoneCount()I\n\n    move-result v3\n\n    if-ge v1, v3, :cond_0\n\n    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;\n\n    move-result-object v3\n\n    invoke-virtual {p0, v1}, Lcom/miui/maml/util/MobileDataUtils;->getMobileDataUri(I)Landroid/net/Uri;\n\n    move-result-object v4\n\n    invoke-virtual {v3, v4, v2, p2}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V\n\n    add-int/lit8 v1, v1, 0x1\n\n    goto :goto_0\n\n    :cond_0\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
]
