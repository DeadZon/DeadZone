"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/ClockSingleLayoutExt.smali'
CLASS_FALLBACK_NAMES = ['ClockSingleLayoutExt.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public abstract Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;
.super Landroid/widget/FrameLayout;

# interfaces
.implements Lcom/android/systemui/newstatusbar/clock/IClock;


# instance fields
.field protected firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

.field protected secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0, p1}, Landroid/widget/FrameLayout;-><init>(Landroid/content/Context;)V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->setClipChildren(Z)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->setClipToPadding(Z)V

    return-void
.end method


# virtual methods
.method protected abstract createView(Landroid/widget/FrameLayout;I)Lcom/android/systemui/newstatusbar/clock/IClock;
.end method

.method public fullInvalidate()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->fullInvalidate()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->fullInvalidate()V

    return-void
.end method

.method public getTextHeight()F
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->getTextHeight()F

    move-result v0

    return v0
.end method

.method public getTextSize()F
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0}, Lcom/android/systemui/newstatusbar/clock/IClock;->getTextSize()F

    move-result v0

    return v0
.end method

.method protected abstract initialize()V
.end method

.method public setTextSize(F)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setTextSize(F)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setTextSize(F)V

    return-void
.end method

.method public setTextSizeWidthAnimation(F)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setTextSizeWidthAnimation(F)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/clock/IClock;->setTextSizeWidthAnimation(F)V

    return-void
.end method

.method public updateTypeface(Landroid/graphics/Typeface;I)V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->firstCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/IClock;->updateTypeface(Landroid/graphics/Typeface;I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/clock/ClockSingleLayoutExt;->secondCharacter:Lcom/android/systemui/newstatusbar/clock/IClock;

    invoke-interface {v0, p1, p2}, Lcom/android/systemui/newstatusbar/clock/IClock;->updateTypeface(Landroid/graphics/Typeface;I)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_ClockSingleLayoutExt',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
