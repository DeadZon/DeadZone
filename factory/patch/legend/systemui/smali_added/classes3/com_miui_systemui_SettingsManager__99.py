"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/SettingsManager$99.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/SettingsManager$99.smali'
CLASS_FALLBACK_NAMES = ['SettingsManager$99.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_systemui_SettingsManager$99',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class final synthetic Lcom/miui/systemui/SettingsManager$99;\n.super Lkotlin/jvm/internal/FunctionReferenceImpl;\n\n# interfaces\n.implements Lkotlin/jvm/functions/Function0;\n\n\n# virtual methods\n.method public final invoke()Ljava/lang/Object;\n    .registers 1\n\n    iget-object p0, p0, Lkotlin/jvm/internal/CallableReference;->receiver:Ljava/lang/Object;\n\n    check-cast p0, Lcom/miui/systemui/SettingsManager;\n\n    invoke-virtual {p0}, Lcom/miui/systemui/SettingsManager;->onChargeAnimTypeChanged()V\n\n    sget-object p0, Lkotlin/Unit;->INSTANCE:Lkotlin/Unit;\n\n    return-object p0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
