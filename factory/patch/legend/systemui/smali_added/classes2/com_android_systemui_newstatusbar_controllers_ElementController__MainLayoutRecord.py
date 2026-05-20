"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord.smali'
CLASS_FALLBACK_NAMES = ['ElementController$MainLayoutRecord.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_ElementControl',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/controllers/ElementController;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x9\n    name = "MainLayoutRecord"\n.end annotation\n\n\n# instance fields\n.field dispatcher:Lcom/android/systemui/plugins/DarkIconDispatcher;\n\n.field dispatchers:Ljava/util/ArrayList;\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "Ljava/util/ArrayList",\n            "<",\n            "Lcom/android/systemui/newstatusbar/policy/ISlots;",\n            ">;"\n        }\n    .end annotation\n.end field\n\n.field mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n.field slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n\n# direct methods\n.method public constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V\n    .registers 4\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    new-instance v0, Ljava/util/ArrayList;\n\n    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->dispatchers:Ljava/util/ArrayList;\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n    iput-object p2, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    invoke-virtual {p1, p2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public setDispatcher(Lcom/android/systemui/plugins/DarkIconDispatcher;)V\n    .registers 4\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->dispatcher:Lcom/android/systemui/plugins/DarkIconDispatcher;\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord$1;\n\n    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord$1;-><init>(Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;)V\n\n    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->post(Ljava/lang/Runnable;)Z\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
