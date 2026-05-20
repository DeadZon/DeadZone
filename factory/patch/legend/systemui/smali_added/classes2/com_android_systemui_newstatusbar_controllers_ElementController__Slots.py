"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/ElementController$Slots.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/ElementController$Slots.smali'
CLASS_FALLBACK_NAMES = ['ElementController$Slots.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_ElementControl',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final enum Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n.super Ljava/lang/Enum;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/controllers/ElementController;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x4019\n    name = "Slots"\n.end annotation\n\n.annotation system Ldalvik/annotation/Signature;\n    value = {\n        "Ljava/lang/Enum",\n        "<",\n        "Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;",\n        ">;"\n    }\n.end annotation\n\n\n# static fields\n.field private static final synthetic $VALUES:[Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n.field public static final enum slotA:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n.field public static final enum slotB:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n\n# direct methods\n.method static constructor <clinit>()V\n    .registers 4\n\n    const/4 v3, 0x1\n\n    const/4 v2, 0x0\n\n    new-instance v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    const-string v1, "slotA"\n\n    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;-><init>(Ljava/lang/String;I)V\n\n    sput-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->slotA:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    new-instance v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    const-string v1, "slotB"\n\n    invoke-direct {v0, v1, v3}, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;-><init>(Ljava/lang/String;I)V\n\n    sput-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->slotB:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    const/4 v0, 0x2\n\n    new-array v0, v0, [Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    sget-object v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->slotA:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    aput-object v1, v0, v2\n\n    sget-object v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->slotB:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    aput-object v1, v0, v3\n\n    sput-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->$VALUES:[Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    return-void\n.end method\n\n.method private constructor <init>(Ljava/lang/String;I)V\n    .registers 3\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "()V"\n        }\n    .end annotation\n\n    invoke-direct {p0, p1, p2}, Ljava/lang/Enum;-><init>(Ljava/lang/String;I)V\n\n    return-void\n.end method\n\n.method public static valueOf(Ljava/lang/String;)Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n    .registers 2\n\n    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    invoke-static {v0, p0}, Ljava/lang/Enum;->valueOf(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/Enum;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    return-object v0\n.end method\n\n.method public static values()[Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n    .registers 1\n\n    sget-object v0, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->$VALUES:[Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    invoke-virtual {v0}, [Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->clone()Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, [Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    return-object v0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
