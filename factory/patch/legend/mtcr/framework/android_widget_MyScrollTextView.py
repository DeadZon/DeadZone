"""
Legend MTCR patch - class-level rule.

Target JAR   : framework.jar
Target class : android/widget/MyScrollTextView
Source MTCR  : Framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "framework.jar"
TARGET_CLASS = "android/widget/MyScrollTextView.smali"
CLASS_FALLBACK_NAMES = ['MyScrollTextView.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "add_class_android_widget_MyScrollTextView",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public Landroid/widget/MyScrollTextView;
.super Landroid/widget/TextView;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 4

    const/4 v1, 0x1

    invoke-direct {p0, p1}, Landroid/widget/TextView;-><init>(Landroid/content/Context;)V

    sget-object v0, Landroid/text/TextUtils$TruncateAt;->MARQUEE:Landroid/text/TextUtils$TruncateAt;

    invoke-virtual {p0, v0}, Landroid/widget/MyScrollTextView;->setEllipsize(Landroid/text/TextUtils$TruncateAt;)V

    invoke-virtual {p0, v1}, Landroid/widget/MyScrollTextView;->setHorizontallyScrolling(Z)V

    invoke-virtual {p0, v1}, Landroid/widget/MyScrollTextView;->setMaxLines(I)V

    const/4 v0, -0x1

    invoke-virtual {p0, v0}, Landroid/widget/MyScrollTextView;->setMarqueeRepeatLimit(I)V

    invoke-virtual {p0, v1}, Landroid/widget/MyScrollTextView;->setSingleLine(Z)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 5

    const/4 v1, 0x1

    invoke-direct {p0, p1, p2}, Landroid/widget/TextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    sget-object v0, Landroid/text/TextUtils$TruncateAt;->MARQUEE:Landroid/text/TextUtils$TruncateAt;

    invoke-virtual {p0, v0}, Landroid/widget/MyScrollTextView;->setEllipsize(Landroid/text/TextUtils$TruncateAt;)V

    invoke-virtual {p0, v1}, Landroid/widget/MyScrollTextView;->setHorizontallyScrolling(Z)V

    invoke-virtual {p0, v1}, Landroid/widget/MyScrollTextView;->setMaxLines(I)V

    const/4 v0, -0x1

    invoke-virtual {p0, v0}, Landroid/widget/MyScrollTextView;->setMarqueeRepeatLimit(I)V

    invoke-virtual {p0, v1}, Landroid/widget/MyScrollTextView;->setSingleLine(Z)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 6

    const/4 v1, 0x1

    invoke-direct {p0, p1, p2, p3}, Landroid/widget/TextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    sget-object v0, Landroid/text/TextUtils$TruncateAt;->MARQUEE:Landroid/text/TextUtils$TruncateAt;

    invoke-virtual {p0, v0}, Landroid/widget/MyScrollTextView;->setEllipsize(Landroid/text/TextUtils$TruncateAt;)V

    invoke-virtual {p0, v1}, Landroid/widget/MyScrollTextView;->setHorizontallyScrolling(Z)V

    invoke-virtual {p0, v1}, Landroid/widget/MyScrollTextView;->setMaxLines(I)V

    const/4 v0, -0x1

    invoke-virtual {p0, v0}, Landroid/widget/MyScrollTextView;->setMarqueeRepeatLimit(I)V

    invoke-virtual {p0, v1}, Landroid/widget/MyScrollTextView;->setSingleLine(Z)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 7

    const/4 v1, 0x1

    invoke-direct {p0, p1, p2, p3, p4}, Landroid/widget/TextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    sget-object v0, Landroid/text/TextUtils$TruncateAt;->MARQUEE:Landroid/text/TextUtils$TruncateAt;

    invoke-virtual {p0, v0}, Landroid/widget/MyScrollTextView;->setEllipsize(Landroid/text/TextUtils$TruncateAt;)V

    invoke-virtual {p0, v1}, Landroid/widget/MyScrollTextView;->setHorizontallyScrolling(Z)V

    invoke-virtual {p0, v1}, Landroid/widget/MyScrollTextView;->setMaxLines(I)V

    const/4 v0, -0x1

    invoke-virtual {p0, v0}, Landroid/widget/MyScrollTextView;->setMarqueeRepeatLimit(I)V

    invoke-virtual {p0, v1}, Landroid/widget/MyScrollTextView;->setSingleLine(Z)V

    return-void
.end method


# virtual methods
.method public isFocused()Z
    .registers 2

    const/4 v0, 0x1

    return v0
.end method

.method protected onFocusChanged(ZILandroid/graphics/Rect;)V
    .registers 4

    if-eqz p1, :cond_0

    invoke-super {p0, p1, p2, p3}, Landroid/widget/TextView;->onFocusChanged(ZILandroid/graphics/Rect;)V

    :cond_0
    return-void
.end method

.method public onWindowFocusChanged(Z)V
    .registers 2

    if-eqz p1, :cond_0

    invoke-super {p0, p1}, Landroid/widget/TextView;->onWindowFocusChanged(Z)V

    :cond_0
    return-void
.end method

.method public setEllipsize(Landroid/text/TextUtils$TruncateAt;)V
    .registers 3

    sget-object v0, Landroid/text/TextUtils$TruncateAt;->MARQUEE:Landroid/text/TextUtils$TruncateAt;

    invoke-super {p0, v0}, Landroid/widget/TextView;->setEllipsize(Landroid/text/TextUtils$TruncateAt;)V

    return-void
.end method

.method public setHorizontallyScrolling(Z)V
    .registers 3

    const/4 v0, 0x1

    invoke-super {p0, v0}, Landroid/widget/TextView;->setHorizontallyScrolling(Z)V

    return-void
.end method

.method public setMarqueeRepeatLimit(I)V
    .registers 2

    const/4 p1, -0x1

    invoke-super {p0, p1}, Landroid/widget/TextView;->setMarqueeRepeatLimit(I)V

    return-void
.end method

.method public setMaxLines(I)V
    .registers 2

    const/4 p1, 0x1

    invoke-super {p0, p1}, Landroid/widget/TextView;->setMaxLines(I)V

    return-void
.end method

.method public setSingleLine(Z)V
    .registers 3

    const/4 v0, 0x1

    invoke-super {p0, v0}, Landroid/widget/TextView;->setSingleLine(Z)V

    return-void
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from Framework_Legend.mtcr",
    },
]
