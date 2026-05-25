"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/keyguard/magazine/utils/LockScreenMagazineUtils.smali
Patches      : 3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/keyguard/magazine/utils/LockScreenMagazineUtils.smali'
CLASS_FALLBACK_NAMES = ['LockScreenMagazineUtils.smali']
CLASS_ANCHORS        = ['sget-boolean v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->USE_GLOBAL_LOCK_SCREEN_MAGAZINE:Z', 'sput-object v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->LOCK_SCREEN_MAGAZINE_PACKAGE_NAME:Ljava/lang/String;', 'sget-boolean v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->USE_GLOBAL_LOCK_SCREEN_MAGAZINE:Z', 'invoke-virtual {v1, v0}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;', 'sput-object v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->CONTENT_URI_LOCK_MAGAZINE_DEFAULT:Ljava/lang/String;']

PATCHES = [
    {
        'id':             'p0000__clinit_',
        'type':           'method_replace',
        'method':         '.method static constructor <clinit>()V',
        'method_name':    '<clinit>',
        'method_anchors': ['sget-boolean v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->USE_GLOBAL_LOCK_SCREEN_MAGAZINE:Z', 'sput-object v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->LOCK_SCREEN_MAGAZINE_PACKAGE_NAME:Ljava/lang/String;', 'sget-boolean v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->USE_GLOBAL_LOCK_SCREEN_MAGAZINE:Z'],
        'search':         '.method static constructor <clinit>()V\n    .registers 2\n\n    sget-boolean v0, Lcom/miui/utils/configs/MiuiConfigs;->IS_INTERNATIONAL_BUILD:Z\n\n    if-eqz v0, :cond_0\n\n    const-string v0, "com.miui.android.fashiongallery"\n\n    goto :goto_0\n\n    :cond_0\n    const-string v0, "com.mfashiongallery.emag"\n\n    :goto_0\n    sput-object v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->LOCK_SCREEN_MAGAZINE_PACKAGE_NAME:Ljava/lang/String;\n\n    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z\n\n    if-eqz v0, :cond_1\n\n    const-string v0, "com.miui.android.fashiongallery.lockscreen_magazine_provider"\n\n    goto :goto_1\n\n    :cond_1\n    const-string v0, "com.xiaomi.tv.gallerylockscreen.lockscreen_magazine_provider"\n\n    :goto_1\n    const-string v1, "content://"\n\n    invoke-virtual {v1, v0}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;\n\n    move-result-object v0\n\n    sput-object v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->CONTENT_URI_LOCK_MAGAZINE_DEFAULT:Ljava/lang/String;\n\n    return-void\n.end method\n',
        'replacement':    '.method static constructor <clinit>()V\n    .registers 2\n\n    sget-boolean v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->USE_GLOBAL_LOCK_SCREEN_MAGAZINE:Z\n\n    if-eqz v0, :cond_0\n\n    const-string v0, "com.miui.android.fashiongallery"\n\n    goto :goto_0\n\n    :cond_0\n    const-string v0, "com.mfashiongallery.emag"\n\n    :goto_0\n    sput-object v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->LOCK_SCREEN_MAGAZINE_PACKAGE_NAME:Ljava/lang/String;\n\n    sget-boolean v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->USE_GLOBAL_LOCK_SCREEN_MAGAZINE:Z\n\n    if-eqz v0, :cond_1\n\n    const-string v0, "com.miui.android.fashiongallery.lockscreen_magazine_provider"\n\n    goto :goto_1\n\n    :cond_1\n    const-string v0, "com.xiaomi.tv.gallerylockscreen.lockscreen_magazine_provider"\n\n    :goto_1\n    const-string v1, "content://"\n\n    invoke-virtual {v1, v0}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;\n\n    move-result-object v0\n\n    sput-object v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->CONTENT_URI_LOCK_MAGAZINE_DEFAULT:Ljava/lang/String;\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI generated generated dex rule modified class',
    },
    {
        'id':             'p0001_isGlobalNeedFeature',
        'type':           'method_replace',
        'method':         '.method public static isGlobalNeedFeature()Z',
        'method_name':    'isGlobalNeedFeature',
        'method_anchors': ['sget-boolean v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->USE_GLOBAL_LOCK_SCREEN_MAGAZINE:Z', 'invoke-static {v0}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;', 'iget-boolean v0, v0, Lcom/android/keyguard/magazine/LockScreenMagazineController;->mIsSupportLockScreenMagazineLeft:Z'],
        'search':         '.method public static isGlobalNeedFeature()Z\n    .registers 1\n\n    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z\n\n    if-eqz v0, :cond_0\n\n    const-class v0, Lcom/android/keyguard/magazine/LockScreenMagazineController;\n\n    invoke-static {v0}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/keyguard/magazine/LockScreenMagazineController;\n\n    iget-boolean v0, v0, Lcom/android/keyguard/magazine/LockScreenMagazineController;->mIsSupportLockScreenMagazineLeft:Z\n\n    if-eqz v0, :cond_0\n\n    const-class v0, Lcom/android/keyguard/wallpaper/MiuiKeyguardWallPaperManager;\n\n    invoke-static {v0}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/keyguard/wallpaper/MiuiKeyguardWallPaperManager;\n\n    invoke-virtual {v0}, Lcom/android/keyguard/wallpaper/MiuiKeyguardWallPaperManager;->isMagazineWallpaper()Z\n\n    move-result v0\n\n    if-eqz v0, :cond_0\n\n    const/4 v0, 0x1\n\n    return v0\n\n    :cond_0\n    const/4 v0, 0x0\n\n    return v0\n.end method\n',
        'replacement':    '.method public static isGlobalNeedFeature()Z\n    .registers 1\n\n    sget-boolean v0, Lcom/android/keyguard/magazine/utils/LockScreenMagazineUtils;->USE_GLOBAL_LOCK_SCREEN_MAGAZINE:Z\n\n    if-eqz v0, :cond_0\n\n    const-class v0, Lcom/android/keyguard/magazine/LockScreenMagazineController;\n\n    invoke-static {v0}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/keyguard/magazine/LockScreenMagazineController;\n\n    iget-boolean v0, v0, Lcom/android/keyguard/magazine/LockScreenMagazineController;->mIsSupportLockScreenMagazineLeft:Z\n\n    if-eqz v0, :cond_0\n\n    const-class v0, Lcom/android/keyguard/wallpaper/MiuiKeyguardWallPaperManager;\n\n    invoke-static {v0}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/keyguard/wallpaper/MiuiKeyguardWallPaperManager;\n\n    invoke-virtual {v0}, Lcom/android/keyguard/wallpaper/MiuiKeyguardWallPaperManager;->isMagazineWallpaper()Z\n\n    move-result v0\n\n    if-eqz v0, :cond_0\n\n    const/4 v0, 0x1\n\n    return v0\n\n    :cond_0\n    const/4 v0, 0x0\n\n    return v0\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI generated generated dex rule modified class',
    },
    {
        'id':             'p0002_field__field_public_static',
        'type':           'field_add',
        'method':         '.field public static final USE_GLOBAL_LOCK_SCREEN_MAGAZINE:Z',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field public static final USE_GLOBAL_LOCK_SCREEN_MAGAZINE:Z',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added field',
    },
]
