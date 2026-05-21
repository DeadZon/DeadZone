TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/theme/ActionIconDrawable.smali'
CLASS_FALLBACK_NAMES = ['ActionIconDrawable.smali']
CLASS_ANCHORS = ['.super Landroid/graphics/drawable/VectorDrawable;', '.field private static final STATE_DISABLED:[I', '.field private static final STATE_PRESSED:[I']

PATCHES = [
    {
        'id': 'miuix_theme_ActionIconDrawable__onStateChange',
        'method': '.method protected onStateChange([I)Z',
        'method_name': 'onStateChange',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/graphics/drawable/VectorDrawable;->onStateChange([I)Z', 'sget-object v0, Lmiuix/theme/ActionIconDrawable;->STATE_DISABLED:[I', 'invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z', 'if-eqz v0, :cond_0', 'invoke-direct {p0}, Lmiuix/theme/ActionIconDrawable;->toDisabledState()Z', 'return p0', 'sget-object v0, Lmiuix/theme/ActionIconDrawable;->STATE_PRESSED:[I', 'invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z'],
        'type': 'method_replace',
        'search': """.method protected onStateChange([I)Z
    .registers 3

    invoke-super {p0, p1}, Landroid/graphics/drawable/VectorDrawable;->onStateChange([I)Z

    sget-object v0, Lmiuix/theme/ActionIconDrawable;->STATE_DISABLED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-direct {p0}, Lmiuix/theme/ActionIconDrawable;->toDisabledState()Z

    move-result p0

    return p0

    :cond_0
    sget-object v0, Lmiuix/theme/ActionIconDrawable;->STATE_PRESSED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result p1

    if-eqz p1, :cond_1

    invoke-direct {p0}, Lmiuix/theme/ActionIconDrawable;->toPressedState()Z

    move-result p0

    return p0

    :cond_1
    invoke-direct {p0}, Lmiuix/theme/ActionIconDrawable;->toNormalState()Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected onStateChange([I)Z
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1}, Landroid/graphics/drawable/VectorDrawable;->onStateChange([I)Z

    goto :goto_e

    nop

    :goto_1
    sget-object v0, Lmiuix/theme/ActionIconDrawable;->STATE_PRESSED:[I

    goto :goto_4

    nop

    :goto_2
    return p0

    :goto_3
    goto :goto_1

    nop

    :goto_4
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result p1

    goto :goto_d

    nop

    :goto_5
    return p0

    :goto_6
    return p0

    :goto_7
    goto :goto_9

    nop

    :goto_8
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    goto :goto_b

    nop

    :goto_9
    invoke-direct {p0}, Lmiuix/theme/ActionIconDrawable;->toNormalState()Z

    move-result p0

    goto :goto_5

    nop

    :goto_a
    invoke-direct {p0}, Lmiuix/theme/ActionIconDrawable;->toPressedState()Z

    move-result p0

    goto :goto_6

    nop

    :goto_b
    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_c

    nop

    :goto_c
    invoke-direct {p0}, Lmiuix/theme/ActionIconDrawable;->toDisabledState()Z

    move-result p0

    goto :goto_2

    nop

    :goto_d
    if-nez p1, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_a

    nop

    :goto_e
    sget-object v0, Lmiuix/theme/ActionIconDrawable;->STATE_DISABLED:[I

    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
