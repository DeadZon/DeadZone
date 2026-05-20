"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/utils/PackageUtils.smali
Patches      : 2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/utils/PackageUtils.smali'
CLASS_FALLBACK_NAMES = ['PackageUtils.smali']
CLASS_ANCHORS        = ['invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;', 'invoke-virtual {p0, p1}, Landroid/content/pm/PackageManager;->getResourcesForApplication(Ljava/lang/String;)Landroid/content/res/Resources;', 'invoke-virtual {p0, p2, v1, p1}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I', 'invoke-virtual {p0, p2, v0}, Landroid/content/res/Resources;->getDrawable(ILandroid/content/res/Resources$Theme;)Landroid/graphics/drawable/Drawable;', 'invoke-static {p0, p1, p2}, Landroidx/constraintlayout/motion/widget/MotionLayout$$ExternalSyntheticOutline0;->m$1(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V']

PATCHES = [
    {
        'id':             'p0000_isAppEnabledForUser',
        'type':           'method_add',
        'method':         '.method public static isAppEnabledForUser(Landroid/content/Context;ILjava/lang/String;)Z',
        'method_name':    'isAppEnabledForUser',
        'method_anchors': ['invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;', 'invoke-virtual {p0, p2, v0, p1}, Landroid/content/pm/PackageManager;->getApplicationInfoAsUser(Ljava/lang/String;II)Landroid/content/pm/ApplicationInfo;', 'iget-boolean p0, p0, Landroid/content/pm/ApplicationInfo;->enabled:Z'],
        'search':         None,
        'replacement':    '.method public static isAppEnabledForUser(Landroid/content/Context;ILjava/lang/String;)Z\n    .registers 4\n\n    const/4 v0, 0x0\n\n    :try_start_0\n    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;\n\n    move-result-object p0\n\n    invoke-virtual {p0, p2, v0, p1}, Landroid/content/pm/PackageManager;->getApplicationInfoAsUser(Ljava/lang/String;II)Landroid/content/pm/ApplicationInfo;\n\n    move-result-object p0\n\n    iget-boolean p0, p0, Landroid/content/pm/ApplicationInfo;->enabled:Z\n    :try_end_0\n    .catch Landroid/content/pm/PackageManager$NameNotFoundException; {:try_start_0 .. :try_end_0} :catch_0\n\n    return p0\n\n    :catch_0\n    return v0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0001_isAppInstalledForUser',
        'type':           'method_replace',
        'method':         '.method public static isAppInstalledForUser(Landroid/content/Context;ILjava/lang/String;)Z',
        'method_name':    'isAppInstalledForUser',
        'method_anchors': ['invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;', 'invoke-virtual {p0, p2, v0, p1}, Landroid/content/pm/PackageManager;->getPackageInfoAsUser(Ljava/lang/String;II)Landroid/content/pm/PackageInfo;'],
        'search':         '.method public static isAppInstalledForUser(Landroid/content/Context;ILjava/lang/String;)Z\n    .registers 4\n\n    :try_start_0\n    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;\n\n    move-result-object p0\n\n    const/4 v0, 0x1\n\n    invoke-virtual {p0, p2, v0, p1}, Landroid/content/pm/PackageManager;->getPackageInfoAsUser(Ljava/lang/String;II)Landroid/content/pm/PackageInfo;\n    :try_end_0\n    .catch Landroid/content/pm/PackageManager$NameNotFoundException; {:try_start_0 .. :try_end_0} :catch_0\n\n    return v0\n\n    :catch_0\n    const-string p0, "name not found pkg="\n\n    const-string p1, "PackageUtils"\n\n    invoke-static {p0, p2, p1}, Landroidx/constraintlayout/motion/widget/MotionLayout$$ExternalSyntheticOutline0;->m$1(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V\n\n    const/4 p0, 0x0\n\n    return p0\n.end method\n',
        'replacement':    '.method public static isAppInstalledForUser(Landroid/content/Context;ILjava/lang/String;)Z\n    .registers 4\n\n    :try_start_0\n    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;\n\n    move-result-object p0\n\n    const/4 v0, 0x1\n\n    invoke-virtual {p0, p2, v0, p1}, Landroid/content/pm/PackageManager;->getPackageInfoAsUser(Ljava/lang/String;II)Landroid/content/pm/PackageInfo;\n    :try_end_0\n    .catch Landroid/content/pm/PackageManager$NameNotFoundException; {:try_start_0 .. :try_end_0} :catch_0\n\n    return v0\n\n    :catch_0\n    const/4 p0, 0x0\n\n    return p0\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
]
