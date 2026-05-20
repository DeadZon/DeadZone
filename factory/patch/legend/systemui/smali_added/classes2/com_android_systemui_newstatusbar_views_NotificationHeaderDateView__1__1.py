"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$1.smali'
CLASS_FALLBACK_NAMES = ['NotificationHeaderDateView$1$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_views_NotificationHeaderDa',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;->onReceive(Landroid/content/Context;Landroid/content/Intent;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$1:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$1;->this$1:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$1;->this$1:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;\n\n    iget-object v0, v0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;->this$0:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->access$000(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
