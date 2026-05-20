"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/sim/SimTypeVerticalView.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/sim/SimTypeVerticalView.smali'
CLASS_FALLBACK_NAMES = ['SimTypeVerticalView.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_sim_SimTypeVerticalView',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/sim/SimTypeVerticalView;\n.super Lcom/android/systemui/newstatusbar/sim/SimTypeView;\n\n\n# instance fields\n.field data:Lcom/android/systemui/newstatusbar/data/TextData;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 6\n\n    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/sim/SimTypeView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    new-instance v0, Lcom/android/systemui/newstatusbar/data/TextData;\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeVerticalView;->getContext()Landroid/content/Context;\n\n    move-result-object v1\n\n    const-string v2, "vertical_mobile_type"\n\n    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Landroid/content/Context;Ljava/lang/String;)V\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeVerticalView;->data:Lcom/android/systemui/newstatusbar/data/TextData;\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 7\n\n    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/sim/SimTypeView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    new-instance v0, Lcom/android/systemui/newstatusbar/data/TextData;\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeVerticalView;->getContext()Landroid/content/Context;\n\n    move-result-object v1\n\n    const-string v2, "vertical_mobile_type"\n\n    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Landroid/content/Context;Ljava/lang/String;)V\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeVerticalView;->data:Lcom/android/systemui/newstatusbar/data/TextData;\n\n    return-void\n.end method\n\n.method private updateData()V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeVerticalView;->data:Lcom/android/systemui/newstatusbar/data/TextData;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->update()Lcom/android/systemui/newstatusbar/data/Data;\n\n    const-string v1, "mobile_type_color"\n\n    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I\n\n    move-result v1\n\n    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->color:I\n\n    const-string v1, "mobile_type_typefase"\n\n    const-string v2, "Default"\n\n    invoke-static {v1, v2}, Landroid/preference/SettingsMezoHelper;->getStringofSettings(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;\n\n    move-result-object v1\n\n    iput-object v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFase:Ljava/lang/String;\n\n    const-string v1, "mobile_type_typefasestyle"\n\n    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I\n\n    move-result v1\n\n    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public getData()Lcom/android/systemui/newstatusbar/data/TextData;\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeVerticalView;->data:Lcom/android/systemui/newstatusbar/data/TextData;\n\n    return-object v0\n.end method\n\n.method public onIconChange()V\n    .registers 1\n\n    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeVerticalView;->updateData()V\n\n    invoke-super {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeView;->onIconChange()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
