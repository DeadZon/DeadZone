"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/data/Data$OnDataChangeListener.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/data/Data$OnDataChangeListener.smali'
CLASS_FALLBACK_NAMES = ['Data$OnDataChangeListener.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_data_Data$OnDataChangeList',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public interface abstract Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/data/Data;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x609\n    name = "OnDataChangeListener"\n.end annotation\n\n\n# virtual methods\n.method public onDataChanged()V\n    .registers 1\n\n    return-void\n.end method\n\n.method public onDataChanged(Ljava/lang/String;)V\n    .registers 2\n\n    invoke-interface {p0}, Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;->onDataChanged()V\n\n    return-void\n.end method\n\n.method public onDataChanged(Ljava/lang/String;Ljava/lang/String;)V\n    .registers 3\n\n    invoke-interface {p0, p2}, Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;->onDataChanged(Ljava/lang/String;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
