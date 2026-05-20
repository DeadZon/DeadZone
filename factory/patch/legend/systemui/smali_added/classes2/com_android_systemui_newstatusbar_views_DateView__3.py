"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/views/DateView$3.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/views/DateView$3.smali'
CLASS_FALLBACK_NAMES = ['DateView$3.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_views_DateView$3',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/views/DateView$3;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/views/DateView;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/views/DateView;\n\n.field final synthetic val$slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/views/DateView;Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/DateView$3;->this$0:Lcom/android/systemui/newstatusbar/views/DateView;\n\n    iput-object p2, p0, Lcom/android/systemui/newstatusbar/views/DateView$3;->val$slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 5\n\n    const/4 v0, 0x0\n\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/DateView$3;->val$slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    sget-object v2, Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;->slotA:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;\n\n    if-ne v1, v2, :cond_0\n\n    const-class v1, Lcom/android/systemui/plugins/DarkIconDispatcher;\n\n    invoke-static {v1}, Lcom/android/systemui/SysDependency;->get(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v1\n\n    move-object v0, v1\n\n    check-cast v0, Lcom/android/systemui/plugins/DarkIconDispatcher;\n\n    goto :goto_0\n\n    :cond_0\n    const-class v1, Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarViewDep;\n\n    invoke-static {v1}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v1\n\n    check-cast v1, Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarViewDep;\n\n    if-eqz v1, :cond_1\n\n    iget-object v2, v1, Lcom/android/systemui/statusbar/phone/MiuiPhoneStatusBarViewDep;->darkIconDispatcher:Lcom/android/systemui/statusbar/data/repository/DarkIconDispatcherStoreImpl;\n\n    iget-object v3, p0, Lcom/android/systemui/newstatusbar/views/DateView$3;->this$0:Lcom/android/systemui/newstatusbar/views/DateView;\n\n    invoke-virtual {v3}, Lcom/android/systemui/newstatusbar/views/DateView;->getContext()Landroid/content/Context;\n\n    move-result-object v3\n\n    invoke-virtual {v3}, Landroid/content/Context;->getDisplay()Landroid/view/Display;\n\n    move-result-object v3\n\n    invoke-virtual {v3}, Landroid/view/Display;->getDisplayId()I\n\n    move-result v3\n\n    invoke-virtual {v2, v3}, Lcom/android/systemui/statusbar/data/repository/DarkIconDispatcherStoreImpl;->forDisplay(I)Ljava/lang/Object;\n\n    move-result-object v2\n\n    move-object v0, v2\n\n    check-cast v0, Lcom/android/systemui/plugins/DarkIconDispatcher;\n\n    :cond_1\n    :goto_0\n    if-eqz v0, :cond_2\n\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/DateView$3;->this$0:Lcom/android/systemui/newstatusbar/views/DateView;\n\n    invoke-interface {v0, v1}, Lcom/android/systemui/plugins/DarkIconDispatcher;->addDarkReceiver(Lcom/android/systemui/plugins/DarkIconDispatcher$DarkReceiver;)V\n\n    :cond_2\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
