"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/clock/ClockSingleLayoutExt.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/clock/ClockSingleLayoutExt.smali'
CLASS_FALLBACK_NAMES = ['ClockSingleLayoutExt.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_clock_ClockSingleLayoutExt',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public abstract Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;\n.super Landroid/widget/FrameLayout;\n\n# interfaces\n.implements Lcom/android/systemui/newstatusbar/clock/IClock;\n\n\n# instance fields\n.field protected firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;\n\n.field protected secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 3\n\n    invoke-direct {p0, p1}, Landroid/widget/FrameLayout;-><init>(Landroid/content/Context;)V\n\n    const/4 v0, 0x0\n\n    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->setClipChildren(Z)V\n\n    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->setClipToPadding(Z)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method protected abstract createView(Landroid/widget/FrameLayout;I)Lcom/android/systemui/newstatusbar/clock/IClock;\n.end method\n\n.method public fullInvalidate()V\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;\n\n    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->fullInvalidate()V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;\n\n    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->fullInvalidate()V\n\n    return-void\n.end method\n\n.method public getTextHeight()F\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;\n\n    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->getTextHeight()F\n\n    move-result v0\n\n    return v0\n.end method\n\n.method public getTextSize()F\n    .registers 2\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;\n\n    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->getTextSize()F\n\n    move-result v0\n\n    return v0\n.end method\n\n.method protected abstract initialize()V\n.end method\n\n.method public setTextSize(F)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;\n\n    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setTextSize(F)V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;\n\n    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setTextSize(F)V\n\n    return-void\n.end method\n\n.method public setTextSizeWidthAnimation(F)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;\n\n    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setTextSizeWidthAnimation(F)V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;\n\n    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setTextSizeWidthAnimation(F)V\n\n    return-void\n.end method\n\n.method public updateTypeface(Landroid/graphics/Typeface;I)V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;\n\n    invoke-interface {v0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/IClock;->updateTypeface(Landroid/graphics/Typeface;I)V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;\n\n    invoke-interface {v0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/IClock;->updateTypeface(Landroid/graphics/Typeface;I)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
