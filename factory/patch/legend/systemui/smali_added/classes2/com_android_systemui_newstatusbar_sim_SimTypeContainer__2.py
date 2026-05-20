"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/sim/SimTypeContainer$2.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/sim/SimTypeContainer$2.smali'
CLASS_FALLBACK_NAMES = ['SimTypeContainer$2.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_sim_SimTypeContainer$2',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/sim/SimTypeContainer$2;\n.super Landroid/database/ContentObserver;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;Landroid/os/Handler;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer$2;->this$0:Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;\n\n    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onChange(Z)V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer$2;->this$0:Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;\n\n    const-string v1, "show_type_name_mobile"\n\n    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings1(Ljava/lang/String;)Z\n\n    move-result v1\n\n    invoke-static {v0, v1}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->access$002(Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;Z)Z\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer$2;->this$0:Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->access$100(Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;)Z\n\n    move-result v1\n\n    if-eqz v1, :cond_0\n\n    const/4 v1, 0x0\n\n    goto :goto_0\n\n    :cond_0\n    const/16 v1, 0x8\n\n    :goto_0\n    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/sim/SimTypeContainer;->setVisibility(I)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
