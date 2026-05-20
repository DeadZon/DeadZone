"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager.smali'
CLASS_FALLBACK_NAMES = ['BatteryMeterIconViewMinit$ResourceManager.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_battery_BatteryMeterIconVi',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0xa\n    name = "ResourceManager"\n.end annotation\n\n\n# instance fields\n.field private mRes:Landroid/content/res/Resources;\n\n.field private mResourceContext:Landroid/content/Context;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 4\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    :try_start_0\n    const-string v0, "com.three.minit.batteryresources"\n\n    const/4 v1, 0x2\n\n    invoke-virtual {p1, v0, v1}, Landroid/content/Context;->createPackageContext(Ljava/lang/String;I)Landroid/content/Context;\n\n    move-result-object v0\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->mResourceContext:Landroid/content/Context;\n\n    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;\n\n    move-result-object v0\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->mRes:Landroid/content/res/Resources;\n    :try_end_0\n    .catch Landroid/content/pm/PackageManager$NameNotFoundException; {:try_start_0 .. :try_end_0} :catch_0\n\n    goto :goto_0\n\n    :catch_0\n    move-exception v0\n\n    invoke-virtual {v0}, Landroid/content/pm/PackageManager$NameNotFoundException;->printStackTrace()V\n\n    :goto_0\n    return-void\n.end method\n\n\n# virtual methods\n.method public getDrawable(Ljava/lang/String;)Landroid/graphics/drawable/Drawable;\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->mRes:Landroid/content/res/Resources;\n\n    const-string v1, "drawable"\n\n    invoke-virtual {p0, p1, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->getResourceId(Ljava/lang/String;Ljava/lang/String;)I\n\n    move-result v1\n\n    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDrawable(I)Landroid/graphics/drawable/Drawable;\n\n    move-result-object v0\n\n    return-object v0\n.end method\n\n.method public getResourceId(Ljava/lang/String;Ljava/lang/String;)I\n    .registers 5\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->mRes:Landroid/content/res/Resources;\n\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->mResourceContext:Landroid/content/Context;\n\n    invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;\n\n    move-result-object v1\n\n    invoke-virtual {v0, p1, p2, v1}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I\n\n    move-result v0\n\n    return v0\n.end method\n\n.method public getResources()Landroid/content/res/Resources;\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->mRes:Landroid/content/res/Resources;\n\n    return-object v0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
