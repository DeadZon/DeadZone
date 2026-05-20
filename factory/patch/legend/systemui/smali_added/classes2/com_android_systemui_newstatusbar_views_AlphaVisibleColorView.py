"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/views/AlphaVisibleColorView.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/views/AlphaVisibleColorView.smali'
CLASS_FALLBACK_NAMES = ['AlphaVisibleColorView.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_views_AlphaVisibleColorVie',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;\n.super Lcom/android/systemui/newstatusbar/views/AlphaColorView;\n\n\n# instance fields\n.field private realVisibility:I\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 3\n\n    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;-><init>(Landroid/content/Context;)V\n\n    const/4 v0, -0x1\n\n    iput v0, p0, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->realVisibility:I\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 4\n\n    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    const/4 v0, -0x1\n\n    iput v0, p0, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->realVisibility:I\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 5\n\n    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    const/4 v0, -0x1\n\n    iput v0, p0, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->realVisibility:I\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public setVisibility(I)V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->iconData:Lcom/android/systemui/newstatusbar/data/IconData;\n\n    if-eqz v0, :cond_0\n\n    iput p1, p0, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->realVisibility:I\n\n    new-instance v0, Ljava/lang/StringBuilder;\n\n    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V\n\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->iconData:Lcom/android/systemui/newstatusbar/data/IconData;\n\n    iget-object v1, v1, Lcom/android/systemui/newstatusbar/data/IconData;->key:Ljava/lang/String;\n\n    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v0\n\n    const-string v1, "_visible"\n\n    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v0\n\n    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;\n\n    move-result-object v0\n\n    const/4 v1, 0x1\n\n    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings(Ljava/lang/String;I)Z\n\n    move-result v0\n\n    if-nez v0, :cond_0\n\n    const/16 p1, 0x8\n\n    :cond_0\n    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->setVisibility(I)V\n\n    return-void\n.end method\n\n.method public update()V\n    .registers 3\n\n    invoke-super {p0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->update()V\n\n    iget v0, p0, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->realVisibility:I\n\n    const/4 v1, -0x1\n\n    if-ne v0, v1, :cond_0\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->getVisibility()I\n\n    move-result v0\n\n    iput v0, p0, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->realVisibility:I\n\n    :cond_0\n    iget v0, p0, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->realVisibility:I\n\n    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/AlphaVisibleColorView;->setVisibility(I)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
