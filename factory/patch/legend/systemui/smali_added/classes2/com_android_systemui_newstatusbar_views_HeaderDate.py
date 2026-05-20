"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/views/HeaderDate.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/views/HeaderDate.smali'
CLASS_FALLBACK_NAMES = ['HeaderDate.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_views_HeaderDate',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/views/HeaderDate;\n.super Lcom/android/systemui/statusbar/views/MiuiClock;\n\n\n# instance fields\n.field private final controller:Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 4\n\n    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MiuiClock;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    const-class v0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;\n\n    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/HeaderDate;->controller:Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 5\n\n    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/MiuiClock;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    const-class v0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;\n\n    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/HeaderDate;->controller:Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public setAlpha(F)V\n    .registers 3\n\n    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setAlpha(F)V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/HeaderDate;->controller:Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;\n\n    if-eqz v0, :cond_0\n\n    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;->onAlphaChange(F)V\n\n    :cond_0\n    return-void\n.end method\n\n.method public setTransitionAlpha(F)V\n    .registers 3\n\n    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTransitionAlpha(F)V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/HeaderDate;->controller:Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;\n\n    if-eqz v0, :cond_0\n\n    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;->onAlphaChange(F)V\n\n    :cond_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
