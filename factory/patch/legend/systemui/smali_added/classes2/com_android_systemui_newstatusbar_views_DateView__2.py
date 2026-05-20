"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/views/DateView$2.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/views/DateView$2.smali'
CLASS_FALLBACK_NAMES = ['DateView$2.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_views_DateView$2',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/views/DateView$2;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/views/DateView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/views/DateView;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/views/DateView;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/DateView$2;->this$0:Lcom/android/systemui/newstatusbar/views/DateView;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onDataChanged()V\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView$2;->this$0:Lcom/android/systemui/newstatusbar/views/DateView;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/views/DateView;->update()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
