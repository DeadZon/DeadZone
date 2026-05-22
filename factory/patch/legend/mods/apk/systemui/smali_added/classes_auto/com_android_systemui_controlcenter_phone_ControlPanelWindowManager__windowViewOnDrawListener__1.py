"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1.smali'
CLASS_FALLBACK_NAMES = ['ControlPanelWindowManager$windowViewOnDrawListener$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public final Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/view/ViewTreeObserver$OnDrawListener;


# instance fields
.field public final synthetic $r8$classId:I

.field public final synthetic this$0:Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;


# direct methods
.method public synthetic constructor <init>(Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;I)V
    .registers 3

    iput p2, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1;->$r8$classId:I

    iput-object p1, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1;->this$0:Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public final onDraw()V
    .registers 3

    iget v0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1;->$r8$classId:I

    const/4 v1, 0x0

    packed-switch v0, :pswitch_data_28

    goto :goto_17

    :pswitch_7  #0x0
    iget-object p0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1;->this$0:Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;

    iget-boolean v0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->pendingNotifyListeners:Z

    if-eqz v0, :cond_16

    iput-boolean v1, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->pendingNotifyListeners:Z

    iget-object v0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->notifyListeners:Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$applyLayout$1;

    iget-object p0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->choreographer:Landroid/view/Choreographer;

    invoke-virtual {p0, v0}, Landroid/view/Choreographer;->postFrameCallback(Landroid/view/Choreographer$FrameCallback;)V

    :cond_16
    return-void

    :goto_17
    iget-object p0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$windowViewOnDrawListener$1;->this$0:Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;

    iget-boolean v0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->pendingApplyLayout:Z

    if-eqz v0, :cond_26

    iput-boolean v1, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->pendingApplyLayout:Z

    iget-object v0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->applyLayout:Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$applyLayout$1;

    iget-object p0, p0, Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager;->choreographer:Landroid/view/Choreographer;

    invoke-virtual {p0, v0}, Landroid/view/Choreographer;->postFrameCallback(Landroid/view/Choreographer$FrameCallback;)V

    :cond_26
    return-void

    nop

    :pswitch_data_28
    .packed-switch 0x0
        :pswitch_7  #00000000
    .end packed-switch
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_controlcenter_phone_ControlPanelWindowManager_windowViewOnDrawListener_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
