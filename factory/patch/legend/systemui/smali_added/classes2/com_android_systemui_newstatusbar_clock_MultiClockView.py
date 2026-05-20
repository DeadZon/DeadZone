"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/clock/MultiClockView.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/clock/MultiClockView.smali'
CLASS_FALLBACK_NAMES = ['MultiClockView.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_clock_MultiClockView',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/clock/MultiClockView;\n.super Landroid/widget/LinearLayout;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 3\n\n    invoke-direct {p0, p1}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;)V\n\n    const/4 v0, 0x1\n\n    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/MultiClockView;->setOrientation(I)V\n\n    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/clock/MultiClockView;->createView()V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 4\n\n    invoke-direct {p0, p1, p2}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    const/4 v0, 0x1\n\n    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/MultiClockView;->setOrientation(I)V\n\n    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/clock/MultiClockView;->createView()V\n\n    return-void\n.end method\n\n.method private createView()V\n    .registers 4\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/MultiClockView;->getContext()Landroid/content/Context;\n\n    move-result-object v0\n\n    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;\n\n    move-result-object v0\n\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/clock/MultiClockView;->getContext()Landroid/content/Context;\n\n    move-result-object v1\n\n    const-string v2, "element_clock_multi"\n\n    invoke-static {v1, v2}, Landroid/Utils/Utils;->LayoutToID(Landroid/content/Context;Ljava/lang/String;)I\n\n    move-result v1\n\n    const/4 v2, 0x1\n\n    invoke-virtual {v0, v1, p0, v2}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;Z)Landroid/view/View;\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
