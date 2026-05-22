"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager.smali'
CLASS_FALLBACK_NAMES = ['BatteryMeterIconViewMinit$ResourceManager.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0xa
    name = "ResourceManager"
.end annotation


# instance fields
.field private mRes:Landroid/content/res/Resources;

.field private mResourceContext:Landroid/content/Context;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 4

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    :try_start_3
    const-string v0, "com.three.minit.batteryresources"

    const/4 v1, 0x2

    invoke-virtual {p1, v0, v1}, Landroid/content/Context;->createPackageContext(Ljava/lang/String;I)Landroid/content/Context;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->mResourceContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->mRes:Landroid/content/res/Resources;
    :try_end_12
    .catch Landroid/content/pm/PackageManager$NameNotFoundException; {:try_start_3 .. :try_end_12} :catch_13

    goto :goto_17

    :catch_13
    move-exception v0

    invoke-virtual {v0}, Landroid/content/pm/PackageManager$NameNotFoundException;->printStackTrace()V

    :goto_17
    return-void
.end method


# virtual methods
.method public getDrawable(Ljava/lang/String;)Landroid/graphics/drawable/Drawable;
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->mRes:Landroid/content/res/Resources;

    const-string v1, "drawable"

    invoke-virtual {p0, p1, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->getResourceId(Ljava/lang/String;Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    return-object v0
.end method

.method public getResourceId(Ljava/lang/String;Ljava/lang/String;)I
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->mRes:Landroid/content/res/Resources;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->mResourceContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, p1, p2, v1}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v0

    return v0
.end method

.method public getResources()Landroid/content/res/Resources;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->mRes:Landroid/content/res/Resources;

    return-object v0
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_battery_BatteryMeterIconViewMinit_ResourceManager',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
