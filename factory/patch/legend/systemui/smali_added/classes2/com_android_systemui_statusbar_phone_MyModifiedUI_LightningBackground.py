"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/phone/MyModifiedUI/LightningBackground.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/phone/MyModifiedUI/LightningBackground.smali'
CLASS_FALLBACK_NAMES = ['LightningBackground.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_statusbar_phone_MyModifiedUI_LightningB',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningBackground;\n.super Landroid/graphics/drawable/AnimationDrawable;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;Ljava/lang/String;)V\n    .registers 9\n\n    invoke-direct {p0}, Landroid/graphics/drawable/AnimationDrawable;-><init>()V\n\n    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;\n\n    move-result-object v3\n\n    invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;\n\n    move-result-object v2\n\n    const/4 v1, 0x1\n\n    :goto_0\n    const/16 v4, 0x23\n\n    if-ge v1, v4, :cond_1\n\n    new-instance v4, Ljava/lang/StringBuilder;\n\n    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V\n\n    invoke-virtual {v4, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v5\n\n    const/16 v4, 0xa\n\n    if-ge v1, v4, :cond_0\n\n    const-string v4, "000"\n\n    :goto_1\n    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v4\n\n    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;\n\n    move-result-object v4\n\n    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;\n\n    move-result-object v4\n\n    const-string v5, "drawable"\n\n    invoke-virtual {v3, v4, v5, v2}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I\n\n    move-result v4\n\n    invoke-virtual {p1, v4}, Landroid/content/Context;->getDrawable(I)Landroid/graphics/drawable/Drawable;\n\n    move-result-object v0\n\n    const/16 v4, 0x64\n\n    invoke-virtual {p0, v0, v4}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/LightningBackground;->addFrame(Landroid/graphics/drawable/Drawable;I)V\n\n    add-int/lit8 v1, v1, 0x1\n\n    goto :goto_0\n\n    :cond_0\n    const-string v4, "00"\n\n    goto :goto_1\n\n    :cond_1\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
