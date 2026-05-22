TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/theme/symbol/SymbolDrawable.smali'
CLASS_FALLBACK_NAMES = ['SymbolDrawable.smali']
CLASS_ANCHORS = ['.super Landroid/graphics/drawable/Drawable;', '.field private static final STATE_DISABLED:[I', '.field private static final STATE_PRESSED:[I']

PATCHES = [
    {
        'id': 'miuix_theme_symbol_SymbolDrawable__onStateChange',
        'method': '.method protected onStateChange([I)Z',
        'method_name': 'onStateChange',
        'method_anchors': ['iget-object v0, p0, Lmiuix/theme/symbol/SymbolDrawable;->iconBrush:Lmiuix/theme/symbol/SymbolPaint;', 'invoke-virtual {v0, p1}, Lmiuix/theme/symbol/SymbolPaint;->applyState([I)Z', 'iget-object v1, p0, Lmiuix/theme/symbol/SymbolDrawable;->contourBrush:Lmiuix/theme/symbol/SymbolPaint;', 'invoke-virtual {v1, p1}, Lmiuix/theme/symbol/SymbolPaint;->applyState([I)Z', 'if-nez v1, :cond_1', 'if-eqz v0, :cond_0', 'iget-object v1, p0, Lmiuix/theme/symbol/SymbolDrawable;->backgroundBrush:Lmiuix/theme/symbol/SymbolPaint;', 'invoke-virtual {v1, p1}, Lmiuix/theme/symbol/SymbolPaint;->applyState([I)Z'],
        'type': 'method_replace',
        'search': """.method protected onStateChange([I)Z
    .registers 6

    iget-object v0, p0, Lmiuix/theme/symbol/SymbolDrawable;->iconBrush:Lmiuix/theme/symbol/SymbolPaint;

    invoke-virtual {v0, p1}, Lmiuix/theme/symbol/SymbolPaint;->applyState([I)Z

    move-result v0

    iget-object v1, p0, Lmiuix/theme/symbol/SymbolDrawable;->contourBrush:Lmiuix/theme/symbol/SymbolPaint;

    invoke-virtual {v1, p1}, Lmiuix/theme/symbol/SymbolPaint;->applyState([I)Z

    move-result v1

    const/4 v2, 0x0

    const/4 v3, 0x1

    if-nez v1, :cond_1

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    move v0, v2

    goto :goto_1

    :cond_1
    :goto_0
    move v0, v3

    :goto_1
    iget-object v1, p0, Lmiuix/theme/symbol/SymbolDrawable;->backgroundBrush:Lmiuix/theme/symbol/SymbolPaint;

    invoke-virtual {v1, p1}, Lmiuix/theme/symbol/SymbolPaint;->applyState([I)Z

    move-result v1

    if-nez v1, :cond_3

    if-eqz v0, :cond_2

    goto :goto_2

    :cond_2
    move v0, v2

    goto :goto_3

    :cond_3
    :goto_2
    move v0, v3

    :goto_3
    iget-object v1, p0, Lmiuix/theme/symbol/SymbolDrawable;->backgroundContourBrush:Lmiuix/theme/symbol/SymbolPaint;

    invoke-virtual {v1, p1}, Lmiuix/theme/symbol/SymbolPaint;->applyState([I)Z

    move-result v1

    if-nez v1, :cond_4

    if-eqz v0, :cond_5

    :cond_4
    move v2, v3

    :cond_5
    iget-object v0, p0, Lmiuix/theme/symbol/SymbolDrawable;->tint:Landroid/content/res/ColorStateList;

    if-eqz v0, :cond_6

    invoke-direct {p0}, Lmiuix/theme/symbol/SymbolDrawable;->updateTintColor()V

    goto :goto_4

    :cond_6
    move v3, v2

    :goto_4
    invoke-direct {p0}, Lmiuix/theme/symbol/SymbolDrawable;->updateShadow()V

    sget-object v0, Lmiuix/theme/symbol/SymbolDrawable;->STATE_DISABLED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    if-eqz v0, :cond_7

    invoke-direct {p0}, Lmiuix/theme/symbol/SymbolDrawable;->toDisabledState()Z

    return v3

    :cond_7
    sget-object v0, Lmiuix/theme/symbol/SymbolDrawable;->STATE_PRESSED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result p1

    if-eqz p1, :cond_8

    invoke-direct {p0}, Lmiuix/theme/symbol/SymbolDrawable;->toPressedState()Z

    return v3

    :cond_8
    invoke-direct {p0}, Lmiuix/theme/symbol/SymbolDrawable;->toNormalState()Z

    return v3
.end method""",
        'replacement': """.method protected onStateChange([I)Z
    .registers 6

    goto :goto_c

    nop

    :goto_0
    goto :goto_19

    :goto_1
    goto :goto_18

    nop

    :goto_2
    const/4 v3, 0x1

    goto :goto_14

    nop

    :goto_3
    move v0, v3

    :goto_4
    goto :goto_2e

    nop

    :goto_5
    if-nez v0, :cond_0

    goto :goto_1e

    :cond_0
    goto :goto_24

    nop

    :goto_6
    if-nez v0, :cond_1

    goto :goto_30

    :cond_1
    :goto_7
    goto :goto_2f

    nop

    :goto_8
    invoke-virtual {v1, p1}, Lmiuix/theme/symbol/SymbolPaint;->applyState([I)Z

    move-result v1

    goto :goto_35

    nop

    :goto_9
    iget-object v1, p0, Lmiuix/theme/symbol/SymbolDrawable;->contourBrush:Lmiuix/theme/symbol/SymbolPaint;

    goto :goto_36

    nop

    :goto_a
    if-eqz v1, :cond_2

    goto :goto_10

    :cond_2
    goto :goto_2b

    nop

    :goto_b
    if-nez v0, :cond_3

    goto :goto_1

    :cond_3
    goto :goto_11

    nop

    :goto_c
    iget-object v0, p0, Lmiuix/theme/symbol/SymbolDrawable;->iconBrush:Lmiuix/theme/symbol/SymbolPaint;

    goto :goto_22

    nop

    :goto_d
    sget-object v0, Lmiuix/theme/symbol/SymbolDrawable;->STATE_DISABLED:[I

    goto :goto_17

    nop

    :goto_e
    invoke-direct {p0}, Lmiuix/theme/symbol/SymbolDrawable;->toNormalState()Z

    goto :goto_23

    nop

    :goto_f
    goto :goto_4

    :goto_10
    goto :goto_3

    nop

    :goto_11
    invoke-direct {p0}, Lmiuix/theme/symbol/SymbolDrawable;->updateTintColor()V

    goto :goto_0

    nop

    :goto_12
    if-nez p1, :cond_4

    goto :goto_2a

    :cond_4
    goto :goto_2d

    nop

    :goto_13
    iget-object v1, p0, Lmiuix/theme/symbol/SymbolDrawable;->backgroundBrush:Lmiuix/theme/symbol/SymbolPaint;

    goto :goto_25

    nop

    :goto_14
    if-eqz v1, :cond_5

    goto :goto_1c

    :cond_5
    goto :goto_28

    nop

    :goto_15
    move v0, v3

    :goto_16
    goto :goto_13

    nop

    :goto_17
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    goto :goto_5

    nop

    :goto_18
    move v3, v2

    :goto_19
    goto :goto_20

    nop

    :goto_1a
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result p1

    goto :goto_12

    nop

    :goto_1b
    goto :goto_16

    :goto_1c
    goto :goto_15

    nop

    :goto_1d
    return v3

    :goto_1e
    goto :goto_21

    nop

    :goto_1f
    const/4 v2, 0x0

    goto :goto_2

    nop

    :goto_20
    invoke-direct {p0}, Lmiuix/theme/symbol/SymbolDrawable;->updateShadow()V

    goto :goto_d

    nop

    :goto_21
    sget-object v0, Lmiuix/theme/symbol/SymbolDrawable;->STATE_PRESSED:[I

    goto :goto_1a

    nop

    :goto_22
    invoke-virtual {v0, p1}, Lmiuix/theme/symbol/SymbolPaint;->applyState([I)Z

    move-result v0

    goto :goto_9

    nop

    :goto_23
    return v3

    :goto_24
    invoke-direct {p0}, Lmiuix/theme/symbol/SymbolDrawable;->toDisabledState()Z

    goto :goto_1d

    nop

    :goto_25
    invoke-virtual {v1, p1}, Lmiuix/theme/symbol/SymbolPaint;->applyState([I)Z

    move-result v1

    goto :goto_a

    nop

    :goto_26
    goto :goto_10

    :goto_27
    goto :goto_31

    nop

    :goto_28
    if-nez v0, :cond_6

    goto :goto_33

    :cond_6
    goto :goto_32

    nop

    :goto_29
    return v3

    :goto_2a
    goto :goto_e

    nop

    :goto_2b
    if-nez v0, :cond_7

    goto :goto_27

    :cond_7
    goto :goto_26

    nop

    :goto_2c
    iget-object v0, p0, Lmiuix/theme/symbol/SymbolDrawable;->tint:Landroid/content/res/ColorStateList;

    goto :goto_b

    nop

    :goto_2d
    invoke-direct {p0}, Lmiuix/theme/symbol/SymbolDrawable;->toPressedState()Z

    goto :goto_29

    nop

    :goto_2e
    iget-object v1, p0, Lmiuix/theme/symbol/SymbolDrawable;->backgroundContourBrush:Lmiuix/theme/symbol/SymbolPaint;

    goto :goto_8

    nop

    :goto_2f
    move v2, v3

    :goto_30
    goto :goto_2c

    nop

    :goto_31
    move v0, v2

    goto :goto_f

    nop

    :goto_32
    goto :goto_1c

    :goto_33
    goto :goto_34

    nop

    :goto_34
    move v0, v2

    goto :goto_1b

    nop

    :goto_35
    if-eqz v1, :cond_8

    goto :goto_7

    :cond_8
    goto :goto_6

    nop

    :goto_36
    invoke-virtual {v1, p1}, Lmiuix/theme/symbol/SymbolPaint;->applyState([I)Z

    move-result v1

    goto :goto_1f

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
