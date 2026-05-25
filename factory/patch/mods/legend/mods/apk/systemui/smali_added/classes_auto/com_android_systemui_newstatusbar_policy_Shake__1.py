"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/policy/Shake$1.smali'
CLASS_FALLBACK_NAMES = ['Shake$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/policy/Shake$1;
.super Ljava/lang/Object;

# interfaces
.implements Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/policy/Shake;-><init>(Landroid/content/Context;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/policy/Shake;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/policy/Shake;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/policy/Shake$1;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method private injectKeyEvent(I)V
    .registers 19

    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v14

    new-instance v0, Landroid/view/KeyEvent;

    const/4 v6, 0x0

    const/4 v8, 0x0

    const/4 v9, 0x0

    const/4 v10, -0x1

    const/4 v11, 0x0

    const/16 v12, 0x8

    const/16 v13, 0x101

    move-object v1, v0

    move-wide v2, v14

    move-wide v4, v14

    move/from16 v7, p1

    invoke-direct/range {v1 .. v13}, Landroid/view/KeyEvent;-><init>(JJIIIIIIII)V

    move-object/from16 v16, v0

    new-instance v0, Landroid/view/KeyEvent;

    const/4 v6, 0x1

    move-object v1, v0

    invoke-direct/range {v1 .. v13}, Landroid/view/KeyEvent;-><init>(JJIIIIIIII)V

    :try_start_20
    const-string v0, "android.hardware.input.InputManager"

    invoke-static {v0}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v0

    const-string v2, "getInstance"

    const/4 v3, 0x0

    new-array v4, v3, [Ljava/lang/Class;

    invoke-virtual {v0, v2, v4}, Ljava/lang/Class;->getDeclaredMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v0

    const/4 v2, 0x0

    new-array v4, v3, [Ljava/lang/Object;

    invoke-virtual {v0, v2, v4}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v2

    const-string v4, "injectInputEvent"

    const/4 v5, 0x2

    new-array v6, v5, [Ljava/lang/Class;

    const-class v7, Landroid/view/InputEvent;

    aput-object v7, v6, v3

    sget-object v7, Ljava/lang/Integer;->TYPE:Ljava/lang/Class;

    const/4 v8, 0x1

    aput-object v7, v6, v8

    invoke-virtual {v2, v4, v6}, Ljava/lang/Class;->getMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v2

    new-array v4, v5, [Ljava/lang/Object;

    aput-object v16, v4, v3

    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v6

    aput-object v6, v4, v8

    invoke-virtual {v2, v0, v4}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    new-array v4, v5, [Ljava/lang/Object;

    aput-object v1, v4, v3

    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    aput-object v3, v4, v8

    invoke-virtual {v2, v0, v4}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;
    :try_end_66
    .catch Ljava/lang/Exception; {:try_start_20 .. :try_end_66} :catch_68

    nop

    goto :goto_6c

    :catch_68
    move-exception v0

    invoke-virtual {v0}, Ljava/lang/Exception;->printStackTrace()V

    :goto_6c
    return-void
.end method


# virtual methods
.method public clearRam()V
    .registers 4

    new-instance v0, Landroid/content/Intent;

    const-string v1, "com.android.systemui.taskmanager.Clear"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v1, "show_toast"

    const/4 v2, 0x1

    invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/Shake$1;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    iget-object v1, v1, Lcom/android/systemui/newstatusbar/policy/Shake;->mContext:Landroid/content/Context;

    invoke-virtual {v1, v0}, Landroid/content/Context;->sendBroadcast(Landroid/content/Intent;)V

    return-void
.end method

.method public goToSleep()V
    .registers 2

    const/16 v0, 0x1a

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/policy/Shake$1;->injectKeyEvent(I)V

    return-void
.end method

.method public isBlueToothOn()Z
    .registers 3

    invoke-static {}, Landroid/bluetooth/BluetoothAdapter;->getDefaultAdapter()Landroid/bluetooth/BluetoothAdapter;

    move-result-object v0

    invoke-virtual {v0}, Landroid/bluetooth/BluetoothAdapter;->getState()I

    move-result v0

    const/16 v1, 0xb

    if-eq v0, v1, :cond_12

    const/16 v1, 0xc

    if-eq v0, v1, :cond_12

    const/4 v0, 0x0

    return v0

    :cond_12
    const/4 v0, 0x1

    return v0
.end method

.method public launchCustomApp(Landroid/content/Context;)V
    .registers 3

    const-string v0, "shake_mobile_app"

    invoke-static {p1, v0}, Landroid/preference/MiuiCoreSettingsPreference;->LaunchCustomApplication(Landroid/content/Context;Ljava/lang/String;)V

    return-void
.end method

.method public onShake(I)V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$1;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/policy/Shake;->mContext:Landroid/content/Context;

    const-string v1, "shake_mobile"

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    if-eqz v1, :cond_40

    const/4 v2, 0x1

    if-ne v1, v2, :cond_13

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake$1;->clearRam()V

    goto :goto_40

    :cond_13
    const/4 v2, 0x2

    if-ne v1, v2, :cond_1a

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake$1;->goToSleep()V

    goto :goto_40

    :cond_1a
    const/4 v2, 0x3

    if-ne v1, v2, :cond_21

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake$1;->wakeUp()V

    goto :goto_40

    :cond_21
    const/4 v2, 0x4

    if-ne v1, v2, :cond_28

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake$1;->showExpandedStatusBar()V

    goto :goto_40

    :cond_28
    const/4 v2, 0x5

    if-ne v1, v2, :cond_2f

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake$1;->switchBluetooth()V

    goto :goto_40

    :cond_2f
    const/4 v2, 0x6

    if-ne v1, v2, :cond_36

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake$1;->switchWifi()V

    goto :goto_40

    :cond_36
    const/4 v2, 0x7

    if-eq v1, v2, :cond_3d

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/policy/Shake$1;->launchCustomApp(Landroid/content/Context;)V

    goto :goto_40

    :cond_3d
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake$1;->switchMobileData()V

    :cond_40
    :goto_40
    return-void
.end method

.method public showExpandedStatusBar()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$1;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/policy/Shake;->mContext:Landroid/content/Context;

    const-class v1, Landroid/app/StatusBarManager;

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    const/4 v1, 0x0

    new-array v1, v1, [Ljava/lang/Object;

    const-string v2, "expandNotificationsPanel"

    invoke-static {v0, v2, v1}, Landroid/Utils/ReflectionUtil;->invokeInClass(Ljava/lang/Object;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    return-void
.end method

.method public switchBluetooth()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$1;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/policy/Shake;->mContext:Landroid/content/Context;

    invoke-static {}, Landroid/bluetooth/BluetoothAdapter;->getDefaultAdapter()Landroid/bluetooth/BluetoothAdapter;

    move-result-object v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake$1;->isBlueToothOn()Z

    move-result v2

    const/4 v3, 0x0

    if-eqz v2, :cond_1c

    invoke-virtual {v1}, Landroid/bluetooth/BluetoothAdapter;->disable()Z

    const-string v2, "Blutooth Выключен"

    invoke-static {v0, v2, v3}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v2

    invoke-virtual {v2}, Landroid/widget/Toast;->show()V

    return-void

    :cond_1c
    invoke-virtual {v1}, Landroid/bluetooth/BluetoothAdapter;->enable()Z

    const-string v2, "Bluetooth Включен"

    invoke-static {v0, v2, v3}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v2

    invoke-virtual {v2}, Landroid/widget/Toast;->show()V

    return-void
.end method

.method public switchMobileData()V
    .registers 7

    const/4 v0, 0x0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/Shake$1;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    iget-object v1, v1, Lcom/android/systemui/newstatusbar/policy/Shake;->mContext:Landroid/content/Context;

    const-class v2, Landroid/net/ConnectivityManager;

    invoke-virtual {v1, v2}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Landroid/net/ConnectivityManager;

    const/4 v3, 0x0

    if-eqz v2, :cond_22

    new-array v4, v3, [Ljava/lang/Object;

    const-string v5, "getMobileDataEnabled"

    invoke-static {v2, v5, v4}, Landroid/Utils/ReflectionUtil;->invokeInClass(Ljava/lang/Object;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v4

    check-cast v4, Ljava/lang/Boolean;

    invoke-virtual {v4}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v4

    if-eqz v4, :cond_22

    const/4 v4, 0x1

    goto :goto_23

    :cond_22
    move v4, v3

    :goto_23
    if-nez v4, :cond_30

    const-string v5, "Мобил. данные Включены"

    invoke-static {v1, v5, v3}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v3

    invoke-virtual {v3}, Landroid/widget/Toast;->show()V

    const/4 v0, 0x1

    goto :goto_39

    :cond_30
    const-string v5, "Мобил. данные Выключены"

    invoke-static {v1, v5, v3}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v3

    invoke-virtual {v3}, Landroid/widget/Toast;->show()V

    :goto_39
    const-class v3, Landroid/telephony/TelephonyManager;

    invoke-virtual {v1, v3}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Landroid/telephony/TelephonyManager;

    invoke-virtual {v3, v0}, Landroid/telephony/TelephonyManager;->setDataEnabled(Z)V

    new-instance v3, Landroid/content/Intent;

    const-string v5, "android.intent.action.ANY_DATA_STATE"

    invoke-direct {v3, v5}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    invoke-virtual {v1, v3}, Landroid/content/Context;->sendBroadcast(Landroid/content/Intent;)V

    return-void
.end method

.method public switchWifi()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$1;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/policy/Shake;->mContext:Landroid/content/Context;

    const-class v1, Landroid/net/wifi/WifiManager;

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/net/wifi/WifiManager;

    invoke-virtual {v1}, Landroid/net/wifi/WifiManager;->isWifiEnabled()Z

    move-result v2

    const/4 v3, 0x0

    if-eqz v2, :cond_20

    invoke-virtual {v1, v3}, Landroid/net/wifi/WifiManager;->setWifiEnabled(Z)Z

    const-string v2, "Wi-Fi Выключен"

    invoke-static {v0, v2, v3}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v2

    invoke-virtual {v2}, Landroid/widget/Toast;->show()V

    return-void

    :cond_20
    const/4 v2, 0x1

    invoke-virtual {v1, v2}, Landroid/net/wifi/WifiManager;->setWifiEnabled(Z)Z

    const-string v2, "Wi-Fi Включен"

    invoke-static {v0, v2, v3}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v2

    invoke-virtual {v2}, Landroid/widget/Toast;->show()V

    return-void
.end method

.method public wakeUp()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake$1;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/policy/Shake;->mContext:Landroid/content/Context;

    const-class v1, Landroid/os/PowerManager;

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    const/4 v1, 0x1

    new-array v1, v1, [Ljava/lang/Object;

    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v2

    invoke-static {v2, v3}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v2

    const/4 v3, 0x0

    aput-object v2, v1, v3

    const-string v2, "wakeUp"

    invoke-static {v0, v2, v1}, Landroid/Utils/ReflectionUtil;->invokeInClass(Ljava/lang/Object;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/Object;

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_policy_Shake_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
