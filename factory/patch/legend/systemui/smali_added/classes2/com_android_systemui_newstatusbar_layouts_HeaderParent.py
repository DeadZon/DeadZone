"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/layouts/HeaderParent.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/layouts/HeaderParent.smali'
CLASS_FALLBACK_NAMES = ['HeaderParent.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_layouts_HeaderParent',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/layouts/HeaderParent;\n.super Landroid/widget/LinearLayout;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 2\n\n    invoke-direct {p0, p1}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;)V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 3\n\n    invoke-direct {p0, p1, p2}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 4\n\n    invoke-direct {p0, p1, p2, p3}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V\n    .registers 5\n\n    invoke-direct {p0, p1, p2, p3, p4}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method protected onAttachedToWindow()V\n    .registers 2\n\n    goto :goto_1\n\n    nop\n\n    :goto_0\n    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;\n\n    goto :goto_3\n\n    nop\n\n    :goto_1\n    invoke-super {p0}, Landroid/widget/LinearLayout;->onAttachedToWindow()V\n\n    goto :goto_4\n\n    nop\n\n    :goto_2\n    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    goto :goto_0\n\n    nop\n\n    :goto_3\n    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;->setParent(Lcom/android/systemui/newstatusbar/layouts/HeaderParent;)V\n\n    goto :goto_5\n\n    nop\n\n    :goto_4\n    const-class v0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;\n\n    goto :goto_2\n\n    nop\n\n    :goto_5\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
