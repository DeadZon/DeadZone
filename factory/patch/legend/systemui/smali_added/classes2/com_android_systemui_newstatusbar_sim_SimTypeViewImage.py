"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/sim/SimTypeViewImage.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/sim/SimTypeViewImage.smali'
CLASS_FALLBACK_NAMES = ['SimTypeViewImage.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_sim_SimTypeViewImage',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;\n.super Lcom/android/systemui/statusbar/AlphaOptimizedImageView;\n\n\n# instance fields\n.field private delegate:Landroid/widget/TextView;\n\n.field private isCustColor:Z\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 2\n\n    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;)V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 3\n\n    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 4\n\n    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V\n    .registers 5\n\n    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public getVisibility()I\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->delegate:Landroid/widget/TextView;\n\n    if-eqz v0, :cond_0\n\n    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->isCustColor:Z\n\n    if-eqz v1, :cond_0\n\n    invoke-virtual {v0}, Landroid/widget/TextView;->getVisibility()I\n\n    move-result v0\n\n    return v0\n\n    :cond_0\n    invoke-super {p0}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->getVisibility()I\n\n    move-result v0\n\n    return v0\n.end method\n\n.method public setDelegate(Landroid/widget/TextView;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->delegate:Landroid/widget/TextView;\n\n    return-void\n.end method\n\n.method public setIsCustColor(Z)V\n    .registers 2\n\n    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->isCustColor:Z\n\n    return-void\n.end method\n\n.method public setVisibility(I)V\n    .registers 5\n\n    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->isCustColor:Z\n\n    const/16 v1, 0x8\n\n    if-eqz v0, :cond_0\n\n    move v0, v1\n\n    goto :goto_0\n\n    :cond_0\n    move v0, p1\n\n    :goto_0\n    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->setVisibility(I)V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->delegate:Landroid/widget/TextView;\n\n    if-eqz v0, :cond_2\n\n    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->isCustColor:Z\n\n    if-eqz v2, :cond_1\n\n    move v1, p1\n\n    :cond_1\n    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setVisibility(I)V\n\n    :cond_2\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
