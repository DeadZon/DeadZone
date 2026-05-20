"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord$1.smali'
CLASS_FALLBACK_NAMES = ['ElementController$MainLayoutRecord$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_ElementControl',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->setDispatcher(Lcom/android/systemui/plugins/DarkIconDispatcher;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 4\n\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;\n\n    iget-object v1, v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->dispatchers:Ljava/util/ArrayList;\n\n    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;\n\n    move-result-object v1\n\n    :goto_0\n    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z\n\n    move-result v2\n\n    if-eqz v2, :cond_0\n\n    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/systemui/newstatusbar/policy/ISlots;\n\n    iget-object v2, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;\n\n    iget-object v2, v2, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    invoke-interface {v0, v2}, Lcom/android/systemui/newstatusbar/policy/ISlots;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V\n\n    goto :goto_0\n\n    :cond_0\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;\n\n    iget-object v1, v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$MainLayoutRecord;->dispatchers:Ljava/util/ArrayList;\n\n    invoke-virtual {v1}, Ljava/util/ArrayList;->clear()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
