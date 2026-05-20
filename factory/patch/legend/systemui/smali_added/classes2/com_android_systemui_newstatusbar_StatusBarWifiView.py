"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/StatusBarWifiView.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/StatusBarWifiView.smali'
CLASS_FALLBACK_NAMES = ['StatusBarWifiView.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_StatusBarWifiView',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/StatusBarWifiView;\n.super Lcom/android/systemui/statusbar/StatusBarWifiView;\n\n\n# instance fields\n.field private isStatusBar:Z\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 3\n\n    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/StatusBarWifiView;-><init>(Landroid/content/Context;)V\n\n    const/4 v0, 0x0\n\n    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->isStatusBar:Z\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 4\n\n    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/StatusBarWifiView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    const/4 v0, 0x0\n\n    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->isStatusBar:Z\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 5\n\n    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/StatusBarWifiView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    const/4 v0, 0x0\n\n    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->isStatusBar:Z\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V\n    .registers 6\n\n    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/statusbar/StatusBarWifiView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V\n\n    const/4 v0, 0x0\n\n    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->isStatusBar:Z\n\n    return-void\n.end method\n\n.method private isStatusbarIcon()Z\n    .registers 2\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->getParent()Landroid/view/ViewParent;\n\n    move-result-object v0\n\n    invoke-interface {v0}, Landroid/view/ViewParent;->getParent()Landroid/view/ViewParent;\n\n    move-result-object v0\n\n    instance-of v0, v0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;\n\n    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->isStatusBar:Z\n\n    return v0\n.end method\n\n.method private moveWiFi()V\n    .registers 1\n\n    return-void\n.end method\n\n\n# virtual methods\n.method protected onAttachedToWindow()V\n    .registers 2\n\n    goto :goto_1\n\n    nop\n\n    :goto_0\n    if-nez v0, :cond_0\n\n    goto :goto_4\n\n    :cond_0\n    goto :goto_3\n\n    nop\n\n    :goto_1\n    invoke-super {p0}, Lcom/android/systemui/statusbar/StatusBarWifiView;->onAttachedToWindow()V\n\n    goto :goto_2\n\n    nop\n\n    :goto_2\n    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->isStatusbarIcon()Z\n\n    move-result v0\n\n    goto :goto_0\n\n    nop\n\n    :goto_3\n    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->moveWiFi()V\n\n    :goto_4\n    goto :goto_5\n\n    nop\n\n    :goto_5\n    return-void\n.end method\n\n.method public setVisibility(I)V\n    .registers 3\n\n    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/StatusBarWifiView;->setVisibility(I)V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/StatusBarWifiView;->mWifiGroup:Landroid/widget/FrameLayout;\n\n    invoke-virtual {v0, p1}, Landroid/widget/FrameLayout;->setVisibility(I)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
