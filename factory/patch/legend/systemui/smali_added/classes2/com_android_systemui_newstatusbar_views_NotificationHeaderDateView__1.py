"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/views/NotificationHeaderDateView$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/views/NotificationHeaderDateView$1.smali'
CLASS_FALLBACK_NAMES = ['NotificationHeaderDateView$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_views_NotificationHeaderDa',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;\n.super Landroid/content/BroadcastReceiver;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;->this$0:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;\n\n    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V\n    .registers 8\n\n    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;\n\n    move-result-object v0\n\n    const-string v1, "android.intent.action.TIME_TICK"\n\n    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v1\n\n    const-string v2, "android.intent.action.TIMEZONE_CHANGED"\n\n    const-string v3, "my.settings.intent.DATE_FORMAT_CHANGED"\n\n    const-string v4, "android.intent.action.LOCALE_CHANGED"\n\n    if-nez v1, :cond_0\n\n    invoke-virtual {v3, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v1\n\n    if-nez v1, :cond_0\n\n    const-string v1, "android.intent.action.TIME_SET"\n\n    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v1\n\n    if-nez v1, :cond_0\n\n    invoke-virtual {v2, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v1\n\n    if-nez v1, :cond_0\n\n    invoke-virtual {v4, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v1\n\n    if-eqz v1, :cond_3\n\n    :cond_0\n    invoke-virtual {v4, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v1\n\n    if-nez v1, :cond_1\n\n    invoke-virtual {v2, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v1\n\n    if-nez v1, :cond_1\n\n    invoke-virtual {v3, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v1\n\n    if-eqz v1, :cond_2\n\n    :cond_1\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;->this$0:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;\n\n    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getHandler()Landroid/os/Handler;\n\n    move-result-object v1\n\n    new-instance v2, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$1;\n\n    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$1;-><init>(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;)V\n\n    invoke-virtual {v1, v2}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z\n\n    :cond_2\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;->this$0:Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;\n\n    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getHandler()Landroid/os/Handler;\n\n    move-result-object v1\n\n    new-instance v2, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$2;\n\n    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1$2;-><init>(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;)V\n\n    invoke-virtual {v1, v2}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z\n\n    :cond_3\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
