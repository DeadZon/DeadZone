"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/battery/PercentInView.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/battery/PercentInView.smali'
CLASS_FALLBACK_NAMES = ['PercentInView.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_battery_PercentInView',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/battery/PercentInView;\n.super Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;\n\n# interfaces\n.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;\n\n\n# instance fields\n.field private final controller:Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 4\n\n    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    const-class v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;\n\n    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentInView;->controller:Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 5\n\n    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    const-class v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;\n\n    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentInView;->controller:Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;\n\n    return-void\n.end method\n\n\n# virtual methods\n.method protected getData()Lcom/android/systemui/newstatusbar/data/TextData;\n    .registers 3\n\n    goto :goto_2\n\n    nop\n\n    :goto_0\n    const/4 v1, 0x0\n\n    goto :goto_1\n\n    nop\n\n    :goto_1\n    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->getTextData(Z)Lcom/android/systemui/newstatusbar/data/TextData;\n\n    move-result-object v0\n\n    goto :goto_3\n\n    nop\n\n    :goto_2\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentInView;->controller:Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;\n\n    goto :goto_0\n\n    nop\n\n    :goto_3\n    return-object v0\n.end method\n\n.method protected onAttached()V\n    .registers 2\n\n    goto :goto_3\n\n    nop\n\n    :goto_0\n    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V\n\n    goto :goto_2\n\n    nop\n\n    :goto_1\n    return-void\n\n    :goto_2\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/PercentInView;->onIconChange()V\n\n    goto :goto_1\n\n    nop\n\n    :goto_3\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentInView;->controller:Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;\n\n    goto :goto_0\n\n    nop\n.end method\n\n.method protected onDetached()V\n    .registers 2\n\n    goto :goto_1\n\n    nop\n\n    :goto_0\n    return-void\n\n    :goto_1\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/PercentInView;->controller:Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;\n\n    goto :goto_2\n\n    nop\n\n    :goto_2\n    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V\n\n    goto :goto_0\n\n    nop\n.end method\n\n.method public onIconChange()V\n    .registers 1\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/PercentInView;->update()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
