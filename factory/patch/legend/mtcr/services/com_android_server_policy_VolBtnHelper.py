"""
Legend MTCR patch - class-level rule.

Target JAR   : services.jar
Target class : com/android/server/policy/VolBtnHelper
Source MTCR  : Service_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "services.jar"
TARGET_CLASS = "com/android/server/policy/VolBtnHelper.smali"

PATCHES = [
    {
        "id":          "add_class_com_android_server_policy_VolBtnHelper",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public Lcom/android/server/policy/VolBtnHelper;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/preference/CustomUpdater$CustomReceiver;


# static fields
.field private static final instance:Lcom/android/server/policy/VolBtnHelper;

.field public static mIsVolLongPressed:Z = false

.field public static mVolBtnMusicControls:Z = false

.field public static mVolBtnTimeout:I = 0x0

.field public static mVolBtnVibrate:Z = false

.field public static mVolBtnVolDown:I = 0x0

.field public static mVolBtnVolUp:I = 0x0

.field private static final sKeys:Ljava/lang/String; = "lock_screen_volume"


# direct methods
.method static constructor <clinit>()V
    .registers 1

    new-instance v0, Lcom/android/server/policy/VolBtnHelper;

    invoke-direct {v0}, Lcom/android/server/policy/VolBtnHelper;-><init>()V

    sput-object v0, Lcom/android/server/policy/VolBtnHelper;->instance:Lcom/android/server/policy/VolBtnHelper;

    return-void
.end method

.method private constructor <init>()V
    .registers 3

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    invoke-static {}, Landroid/preference/CustomUpdater;->getInstance()Landroid/preference/CustomUpdater;

    move-result-object v0

    const-string v1, "lock_screen_volume"

    invoke-virtual {v0, p0, v1}, Landroid/preference/CustomUpdater;->addCustomReceiver(Landroid/preference/CustomUpdater$CustomReceiver;Ljava/lang/String;)V

    const-string v0, "lock_screen_volume"

    invoke-virtual {p0, v0}, Lcom/android/server/policy/VolBtnHelper;->onCustomChanged(Ljava/lang/String;)V

    return-void
.end method

.method private update()V
    .registers 6

    const/4 v3, 0x1

    const-string v4, "volbtn_music_controls"

    invoke-static {v4, v3}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v4

    if-nez v4, :cond_0

    const/4 v3, 0x0

    :cond_0
    sput-boolean v3, Lcom/android/server/policy/VolBtnHelper;->mVolBtnMusicControls:Z

    const-string v3, "volbtn_timeout"

    const/16 v4, 0x1f4

    invoke-static {v3, v4}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    if-nez v0, :cond_1

    const/16 v0, 0x1f4

    :cond_1
    sput v0, Lcom/android/server/policy/VolBtnHelper;->mVolBtnTimeout:I

    const-string v3, "volbtn_vol_up"

    const/16 v4, 0x57

    invoke-static {v3, v4}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v1

    if-nez v1, :cond_2

    const/16 v1, 0x57

    :cond_2
    sput v1, Lcom/android/server/policy/VolBtnHelper;->mVolBtnVolUp:I

    const-string v3, "volbtn_vol_down"

    const/16 v4, 0x58

    invoke-static {v3, v4}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v2

    if-nez v2, :cond_3

    const/16 v2, 0x58

    :cond_3
    sput v2, Lcom/android/server/policy/VolBtnHelper;->mVolBtnVolDown:I

    const-string v3, "volbtn_vibrate"

    invoke-static {v3}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings1(Ljava/lang/String;)Z

    move-result v3

    sput-boolean v3, Lcom/android/server/policy/VolBtnHelper;->mVolBtnVibrate:Z

    return-void
.end method


# virtual methods
.method public onCustomChanged(Ljava/lang/String;)V
    .registers 3

    const-string v0, "lock_screen_volume"

    invoke-virtual {p1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-direct {p0}, Lcom/android/server/policy/VolBtnHelper;->update()V

    :cond_0
    return-void
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from Service_Legend.mtcr",
    },
]
