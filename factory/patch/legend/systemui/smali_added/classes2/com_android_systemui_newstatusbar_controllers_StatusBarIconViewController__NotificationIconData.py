"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/StatusBarIconViewController$NotificationIconData.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/StatusBarIconViewController$NotificationIconData.smali'
CLASS_FALLBACK_NAMES = ['StatusBarIconViewController$NotificationIconData.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_StatusBarIconV',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$NotificationIconData;\n.super Lcom/android/systemui/newstatusbar/data/IconData;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x9\n    name = "NotificationIconData"\n.end annotation\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;Ljava/lang/String;)V\n    .registers 3\n\n    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public update()Lcom/android/systemui/newstatusbar/data/Data;\n    .registers 3\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "<T:",\n            "Lcom/android/systemui/newstatusbar/data/Data;",\n            ">()TT;"\n        }\n    .end annotation\n\n    invoke-super {p0}, Lcom/android/systemui/newstatusbar/data/IconData;->update()Lcom/android/systemui/newstatusbar/data/Data;\n\n    new-instance v0, Ljava/lang/StringBuilder;\n\n    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V\n\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$NotificationIconData;->key:Ljava/lang/String;\n\n    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v0\n\n    const-string v1, "_scale"\n\n    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v0\n\n    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;\n\n    move-result-object v0\n\n    const/16 v1, 0x50\n\n    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v0\n\n    iput v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$NotificationIconData;->scale:I\n\n    new-instance v0, Ljava/lang/StringBuilder;\n\n    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V\n\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$NotificationIconData;->key:Ljava/lang/String;\n\n    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v0\n\n    const-string v1, "_zoom"\n\n    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v0\n\n    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;\n\n    move-result-object v0\n\n    const/16 v1, 0x64\n\n    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v0\n\n    iput v0, p0, Lcom/android/systemui/newstatusbar/controllers/StatusBarIconViewController$NotificationIconData;->zoom:I\n\n    return-object p0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
