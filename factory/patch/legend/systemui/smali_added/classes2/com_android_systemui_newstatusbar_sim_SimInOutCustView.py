"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/sim/SimInOutCustView.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/sim/SimInOutCustView.smali'
CLASS_FALLBACK_NAMES = ['SimInOutCustView.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_sim_SimInOutCustView',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/sim/SimInOutCustView;\n.super Lcom/android/systemui/statusbar/AlphaOptimizedImageView;\n\n\n# instance fields\n.field public mIds:I\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 2\n\n    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;)V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 3\n\n    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 4\n\n    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V\n    .registers 5\n\n    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public setImageResource(I)V\n    .registers 5\n\n    iput p1, p0, Lcom/android/systemui/newstatusbar/sim/SimInOutCustView;->mIds:I\n\n    if-lez p1, :cond_0\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimInOutCustView;->getResources()Landroid/content/res/Resources;\n\n    move-result-object v0\n\n    invoke-virtual {v0, p1}, Landroid/content/res/Resources;->getResourceName(I)Ljava/lang/String;\n\n    move-result-object v0\n\n    const-string v1, "com.android.systemui:drawable/"\n\n    const-string v2, ""\n\n    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;\n\n    move-result-object v0\n\n    new-instance v1, Ljava/lang/StringBuilder;\n\n    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V\n\n    const-string v2, "vertical_"\n\n    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v1\n\n    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v1\n\n    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;\n\n    move-result-object v0\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimInOutCustView;->getContext()Landroid/content/Context;\n\n    move-result-object v1\n\n    invoke-static {v1, v0}, Landroid/Utils/Utils;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I\n\n    move-result p1\n\n    if-nez p1, :cond_0\n\n    return-void\n\n    :cond_0\n    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->setImageResource(I)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
