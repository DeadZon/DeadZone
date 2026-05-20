"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord.smali'
CLASS_FALLBACK_NAMES = ['ElementController$MainLayoutRecord.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/controllers/ElementController;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x9
    name = "MainLayoutRecord"
.end annotation


# instance fields
.field dispatcher:Lcom/android/systemui/plugins/DarkIconDispatcher;

.field dispatchers:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Lcom/android/systemui/newstatusbar/policy/ISlots;",
            ">;"
        }
    .end annotation
.end field

.field mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

.field slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;


# direct methods
.method public constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V
    .registers 4

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->dispatchers:Ljava/util/ArrayList;

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    iput-object p2, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    invoke-virtual {p1, p2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    return-void
.end method


# virtual methods
.method public setDispatcher(Lcom/android/systemui/plugins/DarkIconDispatcher;)V
    .registers 4

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->dispatcher:Lcom/android/systemui/plugins/DarkIconDispatcher;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord$1;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord$1;-><init>(Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->post(Ljava/lang/Runnable;)Z

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_ElementController_MainLayoutRecord',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
