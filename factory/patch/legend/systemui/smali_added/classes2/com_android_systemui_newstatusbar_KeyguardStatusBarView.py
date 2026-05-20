"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/KeyguardStatusBarView.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/KeyguardStatusBarView.smali'
CLASS_FALLBACK_NAMES = ['KeyguardStatusBarView.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_KeyguardStatusBarView',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/KeyguardStatusBarView;\n.super Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 3\n\n    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/phone/KeyguardStatusBarView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public updateKeyguardStatusBarHeight()V\n    .registers 3\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/KeyguardStatusBarView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;\n\n    move-result-object v0\n\n    const-class v1, Lcom/android/systemui/newstatusbar/controllers/ElementController;\n\n    invoke-static {v1}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v1\n\n    check-cast v1, Lcom/android/systemui/newstatusbar/controllers/ElementController;\n\n    iget v1, v1, Lcom/android/systemui/newstatusbar/controllers/ElementController;->statusBarHeight:I\n\n    iput v1, v0, Landroid/view/ViewGroup$LayoutParams;->height:I\n\n    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/KeyguardStatusBarView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V\n\n    return-void\n.end method\n\n.method public final updateSystemIconsLayoutParams()V\n    .registers 5\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/KeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;\n\n    invoke-virtual {v0}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;\n\n    move-result-object v0\n\n    check-cast v0, Landroid/widget/LinearLayout$LayoutParams;\n\n    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/KeyguardStatusBarView;->mKeyguardUserSwitcherEnabled:Z\n\n    if-eqz v1, :cond_0\n\n    iget v1, p0, Lcom/android/systemui/newstatusbar/KeyguardStatusBarView;->mSystemIconsSwitcherHiddenExpandedMargin:I\n\n    goto :goto_0\n\n    :cond_0\n    const/4 v1, 0x0\n\n    :goto_0\n    iget-object v2, p0, Lcom/android/systemui/newstatusbar/KeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;\n\n    instance-of v2, v2, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;\n\n    if-eqz v2, :cond_1\n\n    invoke-static {}, Landroid/Utils/Utils;->getRealWidth()I\n\n    move-result v2\n\n    div-int/lit8 v2, v2, 0x2\n\n    add-int/lit8 v2, v2, -0x2d\n\n    iget-object v3, p0, Lcom/android/systemui/newstatusbar/KeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;\n\n    invoke-virtual {v3}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;->getPaddingEnd()I\n\n    move-result v3\n\n    sub-int/2addr v2, v3\n\n    sub-int/2addr v2, v1\n\n    iget-object v3, p0, Lcom/android/systemui/newstatusbar/KeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;\n\n    check-cast v3, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;\n\n    invoke-virtual {v3, v2}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusBatteryContainer;->setMaxWidth(I)V\n\n    :cond_1\n    invoke-virtual {v0}, Landroid/widget/LinearLayout$LayoutParams;->getMarginEnd()I\n\n    move-result v2\n\n    if-eq v1, v2, :cond_2\n\n    invoke-virtual {v0, v1}, Landroid/widget/LinearLayout$LayoutParams;->setMarginEnd(I)V\n\n    iget-object v2, p0, Lcom/android/systemui/newstatusbar/KeyguardStatusBarView;->mSystemIconsContainer:Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;\n\n    invoke-virtual {v2, v0}, Lcom/android/systemui/statusbar/views/MiuiStatusBatteryContainer;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V\n\n    :cond_2\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
