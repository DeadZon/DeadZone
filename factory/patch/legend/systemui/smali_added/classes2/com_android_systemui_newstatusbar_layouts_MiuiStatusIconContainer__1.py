"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1.smali'
CLASS_FALLBACK_NAMES = ['MiuiStatusIconContainer$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_layouts_MiuiStatusIconCont',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;\n\n.field final synthetic val$slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;\n\n    iput-object p2, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;->val$slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 5\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->access$000(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;)Ljava/util/ArrayList;\n\n    move-result-object v0\n\n    monitor-enter v0\n\n    :try_start_0\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;\n\n    invoke-static {v1}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->access$000(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;)Ljava/util/ArrayList;\n\n    move-result-object v1\n\n    invoke-virtual {v1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;\n\n    move-result-object v1\n\n    :goto_0\n    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z\n\n    move-result v2\n\n    if-eqz v2, :cond_0\n\n    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;\n\n    move-result-object v2\n\n    check-cast v2, Lcom/android/systemui/newstatusbar/policy/ISlots;\n\n    iget-object v3, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;->val$slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    invoke-interface {v2, v3}, Lcom/android/systemui/newstatusbar/policy/ISlots;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V\n\n    goto :goto_0\n\n    :cond_0\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;\n\n    invoke-static {v1}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->access$000(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;)Ljava/util/ArrayList;\n\n    move-result-object v1\n\n    invoke-virtual {v1}, Ljava/util/ArrayList;->clear()V\n\n    monitor-exit v0\n\n    return-void\n\n    :catchall_0\n    move-exception v1\n\n    monitor-exit v0\n    :try_end_0\n    .catchall {:try_start_0 .. :try_end_0} :catchall_0\n\n    throw v1\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
