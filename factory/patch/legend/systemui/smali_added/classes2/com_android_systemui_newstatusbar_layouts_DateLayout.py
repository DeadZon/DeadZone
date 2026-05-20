"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/layouts/DateLayout.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/layouts/DateLayout.smali'
CLASS_FALLBACK_NAMES = ['DateLayout.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_layouts_DateLayout',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/layouts/DateLayout;\n.super Lcom/android/systemui/newstatusbar/layouts/ElementLayout;\n\n# interfaces\n.implements Lcom/android/systemui/newstatusbar/policy/ISlots;\n\n\n# instance fields\n.field private child:Lcom/android/systemui/newstatusbar/views/DateView;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 3\n\n    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method getView()Landroid/view/View;\n    .registers 4\n\n    goto :goto_7\n\n    nop\n\n    :goto_0\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/DateLayout;->getContext()Landroid/content/Context;\n\n    move-result-object v1\n\n    goto :goto_3\n\n    nop\n\n    :goto_1\n    check-cast v0, Lcom/android/systemui/newstatusbar/views/DateView;\n\n    goto :goto_9\n\n    nop\n\n    :goto_2\n    return-object v0\n\n    :goto_3\n    const-string v2, "element_date"\n\n    goto :goto_8\n\n    nop\n\n    :goto_4\n    const/4 v2, 0x0\n\n    goto :goto_5\n\n    nop\n\n    :goto_5\n    invoke-virtual {v0, v1, v2}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;\n\n    move-result-object v0\n\n    goto :goto_1\n\n    nop\n\n    :goto_6\n    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;\n\n    move-result-object v0\n\n    goto :goto_0\n\n    nop\n\n    :goto_7\n    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/DateLayout;->getContext()Landroid/content/Context;\n\n    move-result-object v0\n\n    goto :goto_6\n\n    nop\n\n    :goto_8\n    invoke-static {v1, v2}, Landroid/Utils/Utils;->LayoutToID(Landroid/content/Context;Ljava/lang/String;)I\n\n    move-result v1\n\n    goto :goto_4\n\n    nop\n\n    :goto_9\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/DateLayout;->child:Lcom/android/systemui/newstatusbar/views/DateView;\n\n    goto :goto_2\n\n    nop\n.end method\n\n.method public setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/DateLayout;->child:Lcom/android/systemui/newstatusbar/views/DateView;\n\n    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/policy/ISlots;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
