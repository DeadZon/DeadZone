"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType.smali'
CLASS_FALLBACK_NAMES = ['ControllerExt$SettingsObserver$SettingsType.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public final enum Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;
.super Ljava/lang/Enum;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x4019
    name = "SettingsType"
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Ljava/lang/Enum",
        "<",
        "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;",
        ">;"
    }
.end annotation


# static fields
.field private static final synthetic $VALUES:[Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

.field public static final enum Global:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

.field public static final enum Secure:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

.field public static final enum System:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;


# direct methods
.method static constructor <clinit>()V
    .registers 5

    const/4 v4, 0x2

    const/4 v3, 0x1

    const/4 v2, 0x0

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    const-string v1, "System"

    invoke-direct {v0, v1, v2}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;-><init>(Ljava/lang/String;I)V

    sput-object v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->System:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    const-string v1, "Global"

    invoke-direct {v0, v1, v3}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;-><init>(Ljava/lang/String;I)V

    sput-object v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->Global:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    const-string v1, "Secure"

    invoke-direct {v0, v1, v4}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;-><init>(Ljava/lang/String;I)V

    sput-object v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->Secure:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    const/4 v0, 0x3

    new-array v0, v0, [Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    sget-object v1, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->System:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    aput-object v1, v0, v2

    sget-object v1, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->Global:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    aput-object v1, v0, v3

    sget-object v1, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->Secure:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    aput-object v1, v0, v4

    sput-object v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->$VALUES:[Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    return-void
.end method

.method private constructor <init>(Ljava/lang/String;I)V
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "()V"
        }
    .end annotation

    invoke-direct {p0, p1, p2}, Ljava/lang/Enum;-><init>(Ljava/lang/String;I)V

    return-void
.end method

.method public static valueOf(Ljava/lang/String;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;
    .registers 2

    const-class v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    invoke-static {v0, p0}, Ljava/lang/Enum;->valueOf(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/Enum;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    return-object v0
.end method

.method public static values()[Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;
    .registers 1

    sget-object v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->$VALUES:[Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    invoke-virtual {v0}, [Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->clone()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, [Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    return-object v0
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_plugins_controllers_ControllerExt_SettingsObserver_SettingsType',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
