"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1.smali'
CLASS_FALLBACK_NAMES = ['ControlPanelWindowManager$windowViewOnDrawListener$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_controlcenter_phone_ControlPanelWindowM',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Landroid/view/ViewTreeObserver$OnDrawListener;\n\n\n# instance fields\n.field public final synthetic $r8$classId:I\n\n.field public final synthetic this$0:Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;\n\n\n# direct methods\n.method public synthetic constructor <init>(Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;I)V\n    .registers 3\n\n    iput p2, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1;->$r8$classId:I\n\n    iput-object p1, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1;->this$0:Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public final onDraw()V\n    .registers 3\n\n    iget v0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1;->$r8$classId:I\n\n    const/4 v1, 0x0\n\n    packed-switch v0, :pswitch_data_0\n\n    goto :goto_0\n\n    :pswitch_0  #0x0\n    iget-object p0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1;->this$0:Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;\n\n    iget-boolean v0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->pendingNotifyListeners:Z\n\n    if-eqz v0, :cond_0\n\n    iput-boolean v1, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->pendingNotifyListeners:Z\n\n    iget-object v0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->notifyListeners:Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$applyLayout$1;\n\n    iget-object p0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->choreographer:Landroid/view/Choreographer;\n\n    invoke-virtual {p0, v0}, Landroid/view/Choreographer;->postFrameCallback(Landroid/view/Choreographer$FrameCallback;)V\n\n    :cond_0\n    return-void\n\n    :goto_0\n    iget-object p0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1;->this$0:Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;\n\n    iget-boolean v0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->pendingApplyLayout:Z\n\n    if-eqz v0, :cond_1\n\n    iput-boolean v1, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->pendingApplyLayout:Z\n\n    iget-object v0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->applyLayout:Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$applyLayout$1;\n\n    iget-object p0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->choreographer:Landroid/view/Choreographer;\n\n    invoke-virtual {p0, v0}, Landroid/view/Choreographer;->postFrameCallback(Landroid/view/Choreographer$FrameCallback;)V\n\n    :cond_1\n    return-void\n\n    nop\n\n    :pswitch_data_0\n    .packed-switch 0x0\n        :pswitch_0  #00000000\n    .end packed-switch\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
