"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/views/AlphaColorView.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/views/AlphaColorView.smali'
CLASS_FALLBACK_NAMES = ['AlphaColorView.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_views_AlphaColorView',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/views/AlphaColorView;\n.super Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;\n\n\n# instance fields\n.field iconData:Lcom/android/systemui/newstatusbar/data/IconData;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 3\n\n    const/4 v0, 0x0\n\n    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 4\n\n    const/4 v0, 0x0\n\n    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 7\n\n    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/views/ext/ExtIconAlpha;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    const/4 v0, 0x0\n\n    const-string v1, "settingsKey"\n\n    invoke-interface {p2, v0, v1}, Landroid/util/AttributeSet;->getAttributeValue(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;\n\n    move-result-object v0\n\n    if-nez v0, :cond_0\n\n    const-string v0, ""\n\n    :cond_0\n    new-instance v1, Lcom/android/systemui/newstatusbar/data/IconData;\n\n    invoke-direct {v1, p1, v0}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V\n\n    const/4 v2, 0x0\n\n    new-array v2, v2, [Ljava/lang/String;\n\n    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;\n\n    move-result-object v1\n\n    new-instance v2, Lcom/android/systemui/newstatusbar/views/AlphaColorView$1;\n\n    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView$1;-><init>(Lcom/android/systemui/newstatusbar/views/AlphaColorView;)V\n\n    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;\n\n    move-result-object v1\n\n    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;\n\n    move-result-object v1\n\n    check-cast v1, Lcom/android/systemui/newstatusbar/data/IconData;\n\n    iput-object v1, p0, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->iconData:Lcom/android/systemui/newstatusbar/data/IconData;\n\n    return-void\n.end method\n\n.method private checkDrawable()V\n    .registers 2\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->getDrawable()Landroid/graphics/drawable/Drawable;\n\n    move-result-object v0\n\n    if-eqz v0, :cond_0\n\n    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V\n\n    :cond_0\n    return-void\n.end method\n\n\n# virtual methods\n.method public getData()Lcom/android/systemui/newstatusbar/data/IconData;\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->iconData:Lcom/android/systemui/newstatusbar/data/IconData;\n\n    return-object v0\n.end method\n\n.method protected onAttached()V\n    .registers 1\n\n    goto :goto_0\n\n    nop\n\n    :goto_0\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->update()V\n\n    goto :goto_2\n\n    nop\n\n    :goto_1\n    return-void\n\n    :goto_2\n    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/AlphaColorView;->checkDrawable()V\n\n    goto :goto_1\n\n    nop\n.end method\n\n.method protected onDetached()V\n    .registers 1\n\n    goto :goto_0\n\n    nop\n\n    :goto_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
