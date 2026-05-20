"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/views/WifiView.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/views/WifiView.smali'
CLASS_FALLBACK_NAMES = ['WifiView.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_views_WifiView',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/views/WifiView;\n.super Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;\n\n# interfaces\n.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;\n\n\n# instance fields\n.field protected controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 4\n\n    const/4 v0, 0x0\n\n    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/views/WifiView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 5\n\n    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    const-class v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/WifiView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public getData()Lcom/android/systemui/newstatusbar/data/IconData;\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/WifiView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n    if-nez v0, :cond_0\n\n    const-class v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/WifiView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n    :cond_0\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/WifiView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->getWifiData()Lcom/android/systemui/newstatusbar/data/IconData;\n\n    move-result-object v0\n\n    return-object v0\n.end method\n\n.method protected onAttached()V\n    .registers 2\n\n    goto :goto_2\n\n    nop\n\n    :goto_0\n    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V\n\n    goto :goto_1\n\n    nop\n\n    :goto_1\n    return-void\n\n    :goto_2\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/WifiView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n    goto :goto_0\n\n    nop\n.end method\n\n.method protected onDetached()V\n    .registers 2\n\n    goto :goto_2\n\n    nop\n\n    :goto_0\n    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V\n\n    goto :goto_1\n\n    nop\n\n    :goto_1\n    return-void\n\n    :goto_2\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/WifiView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n    goto :goto_0\n\n    nop\n.end method\n\n.method public onIconChange()V\n    .registers 1\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/WifiView;->update()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
