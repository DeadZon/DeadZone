"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/FakeClockAnimController$2.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/FakeClockAnimController$2.smali'
CLASS_FALLBACK_NAMES = ['FakeClockAnimController$2.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_FakeClockAnimC',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$2;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$2;->this$0:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$2;->this$0:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->access$800(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;\n\n    move-result-object v0\n\n    const/16 v1, 0x1f6\n\n    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;->sendEmptyMessage(I)Z\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
