"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition.smali'
CLASS_FALLBACK_NAMES = ['ElementController$LeftElementPosition.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public final enum Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;
.super Ljava/lang/Enum;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/controllers/ElementController;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x4019
    name = "LeftElementPosition"
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Ljava/lang/Enum",
        "<",
        "Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;",
        ">;"
    }
.end annotation


# static fields
.field private static final synthetic $VALUES:[Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

.field public static final enum bottomElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

.field public static final enum twoElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

.field public static final enum twoElemOnRight:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

.field public static final enum upperElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;


# direct methods
.method static constructor <clinit>()V
    .registers 6

    const/4 v5, 0x3

    const/4 v4, 0x2

    const/4 v3, 0x1

    const/4 v2, 0x0

    new-instance v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    const-string v1, "twoElemOnLeft"

    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;-><init>(Ljava/lang/String;I)V

    sput-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->twoElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    new-instance v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    const-string v1, "upperElemOnLeft"

    invoke-direct {v0, v1, v3}, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;-><init>(Ljava/lang/String;I)V

    sput-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->upperElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    new-instance v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    const-string v1, "bottomElemOnLeft"

    invoke-direct {v0, v1, v4}, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;-><init>(Ljava/lang/String;I)V

    sput-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->bottomElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    new-instance v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    const-string v1, "twoElemOnRight"

    invoke-direct {v0, v1, v5}, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;-><init>(Ljava/lang/String;I)V

    sput-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->twoElemOnRight:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    const/4 v0, 0x4

    new-array v0, v0, [Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    sget-object v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->twoElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    aput-object v1, v0, v2

    sget-object v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->upperElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    aput-object v1, v0, v3

    sget-object v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->bottomElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    aput-object v1, v0, v4

    sget-object v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->twoElemOnRight:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    aput-object v1, v0, v5

    sput-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->$VALUES:[Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

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

.method public static valueOf(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;
    .registers 2

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    invoke-static {v0, p0}, Ljava/lang/Enum;->valueOf(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/Enum;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    return-object v0
.end method

.method public static values()[Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;
    .registers 1

    sget-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->$VALUES:[Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    invoke-virtual {v0}, [Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->clone()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, [Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    return-object v0
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_ElementController_LeftElementPosition',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
