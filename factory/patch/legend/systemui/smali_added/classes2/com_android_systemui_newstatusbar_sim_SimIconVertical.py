"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/sim/SimIconVertical.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/sim/SimIconVertical.smali'
CLASS_FALLBACK_NAMES = ['SimIconVertical.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_sim_SimIconVertical',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/sim/SimIconVertical;\n.super Lcom/android/systemui/newstatusbar/sim/SimIcon;\n\n\n# instance fields\n.field data:Lcom/android/systemui/newstatusbar/data/IconData;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 6\n\n    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/sim/SimIcon;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->getContext()Landroid/content/Context;\n\n    move-result-object v1\n\n    const-string v2, "vertical_simview"\n\n    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->data:Lcom/android/systemui/newstatusbar/data/IconData;\n\n    iget v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->mIconSize:I\n\n    div-int/lit8 v0, v0, 0x2\n\n    iput v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->mIconSize:I\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 7\n\n    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/sim/SimIcon;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->getContext()Landroid/content/Context;\n\n    move-result-object v1\n\n    const-string v2, "vertical_simview"\n\n    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->data:Lcom/android/systemui/newstatusbar/data/IconData;\n\n    iget v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->mIconSize:I\n\n    div-int/lit8 v0, v0, 0x2\n\n    iput v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->mIconSize:I\n\n    return-void\n.end method\n\n.method private updateData()V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->data:Lcom/android/systemui/newstatusbar/data/IconData;\n\n    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/IconData;->update()Lcom/android/systemui/newstatusbar/data/Data;\n\n    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->isFirstSlot:Z\n\n    if-eqz v1, :cond_0\n\n    const-string v1, "sim_one_color"\n\n    goto :goto_0\n\n    :cond_0\n    const-string v1, "sim_two_color"\n\n    :goto_0\n    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I\n\n    move-result v1\n\n    iput v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->color:I\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public getData()Lcom/android/systemui/newstatusbar/data/IconData;\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->data:Lcom/android/systemui/newstatusbar/data/IconData;\n\n    return-object v0\n.end method\n\n.method public onIconChange()V\n    .registers 1\n\n    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->updateData()V\n\n    invoke-super {p0}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->onIconChange()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
