TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/ProgressDialog.smali'
CLASS_FALLBACK_NAMES = ['ProgressDialog.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AlertDialog;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_ProgressDialog__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;', 'invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;', 'invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;', 'sget-object v2, Lmiuix/appcompat/R$styleable;->AlertDialog:[I', 'invoke-virtual {v1, v3, v2, v4, v5}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[III)Landroid/content/res/TypedArray;', 'invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;', 'invoke-virtual {v2}, Landroid/content/Context;->getTheme()Landroid/content/res/Resources$Theme;', 'sget v4, Lmiuix/appcompat/R$attr;->dialogProgressPercentColor:I'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 10

    invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;

    move-result-object v1

    sget-object v2, Lmiuix/appcompat/R$styleable;->AlertDialog:[I

    const/4 v3, 0x0

    const v4, 0x101005d

    const/4 v5, 0x0

    invoke-virtual {v1, v3, v2, v4, v5}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[III)Landroid/content/res/TypedArray;

    move-result-object v1

    invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;

    move-result-object v2

    invoke-virtual {v2}, Landroid/content/Context;->getTheme()Landroid/content/res/Resources$Theme;

    move-result-object v2

    sget v4, Lmiuix/appcompat/R$attr;->dialogProgressPercentColor:I

    filled-new-array {v4}, [I

    move-result-object v4

    invoke-virtual {v2, v4}, Landroid/content/res/Resources$Theme;->obtainStyledAttributes([I)Landroid/content/res/TypedArray;

    move-result-object v2

    invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;

    move-result-object v4

    invoke-virtual {v4}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v4

    sget v6, Lmiuix/appcompat/R$color;->miuix_appcompat_dialog_default_progress_percent_color:I

    invoke-virtual {v4, v6}, Landroid/content/res/Resources;->getColor(I)I

    move-result v4

    invoke-virtual {v2, v5, v4}, Landroid/content/res/TypedArray;->getColor(II)I

    move-result v4

    invoke-virtual {v2}, Landroid/content/res/TypedArray;->recycle()V

    invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;

    move-result-object v2

    invoke-static {v2}, Lmiuix/core/util/MiuixUIUtils;->getFontLevel(Landroid/content/Context;)I

    move-result v2

    const/4 v6, 0x2

    const/4 v7, 0x1

    if-ne v2, v6, :cond_0

    move v5, v7

    :cond_0
    iget v2, p0, Lmiuix/appcompat/app/ProgressDialog;->mProgressStyle:I

    if-ne v2, v7, :cond_2

    new-instance v2, Lmiuix/appcompat/app/ProgressDialog$1;

    invoke-direct {v2, p0, v4}, Lmiuix/appcompat/app/ProgressDialog$1;-><init>(Lmiuix/appcompat/app/ProgressDialog;I)V

    iput-object v2, p0, Lmiuix/appcompat/app/ProgressDialog;->mViewUpdateHandler:Landroid/os/Handler;

    if-eqz v5, :cond_1

    sget v2, Lmiuix/appcompat/R$layout;->miuix_appcompat_alert_dialog_progress_xl_font:I

    goto :goto_0

    :cond_1
    sget v2, Lmiuix/appcompat/R$layout;->miuix_appcompat_alert_dialog_progress:I

    :goto_0
    sget v4, Lmiuix/appcompat/R$styleable;->AlertDialog_horizontalProgressLayout:I

    invoke-virtual {v1, v4, v2}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v2

    invoke-virtual {v0, v2, v3}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    sget v2, Lmiuix/appcompat/R$id;->progress_percent:I

    invoke-virtual {v0, v2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v2

    check-cast v2, Landroid/widget/TextView;

    iput-object v2, p0, Lmiuix/appcompat/app/ProgressDialog;->mProgressPercentView:Landroid/widget/TextView;

    goto :goto_1

    :cond_2
    sget v2, Lmiuix/appcompat/R$styleable;->AlertDialog_progressLayout:I

    sget v4, Lmiuix/appcompat/R$layout;->miuix_appcompat_progress_dialog:I

    invoke-virtual {v1, v2, v4}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v2

    invoke-virtual {v0, v2, v3}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    :goto_1
    const v2, 0x102000d

    invoke-virtual {v0, v2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v2

    check-cast v2, Lmiuix/androidbasewidget/widget/ProgressBar;

    iput-object v2, p0, Lmiuix/appcompat/app/ProgressDialog;->mProgress:Lmiuix/androidbasewidget/widget/ProgressBar;

    sget v2, Lmiuix/appcompat/R$id;->message:I

    invoke-virtual {v0, v2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v2

    check-cast v2, Landroid/widget/TextView;

    iput-object v2, p0, Lmiuix/appcompat/app/ProgressDialog;->mMessageView:Landroid/widget/TextView;

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/AlertDialog;->setView(Landroid/view/View;)V

    invoke-virtual {v1}, Landroid/content/res/TypedArray;->recycle()V

    iget v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mMax:I

    if-lez v0, :cond_3

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setMax(I)V

    :cond_3
    iget v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mProgressVal:I

    if-lez v0, :cond_4

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setProgress(I)V

    :cond_4
    iget v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mSecondaryProgressVal:I

    if-lez v0, :cond_5

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setSecondaryProgress(I)V

    :cond_5
    iget v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mIncrementBy:I

    if-lez v0, :cond_6

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->incrementProgressBy(I)V

    :cond_6
    iget v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mIncrementSecondaryBy:I

    if-lez v0, :cond_7

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->incrementSecondaryProgressBy(I)V

    :cond_7
    iget-object v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mProgressDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_8

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setProgressDrawable(Landroid/graphics/drawable/Drawable;)V

    :cond_8
    iget-object v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mIndeterminateDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_9

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setIndeterminateDrawable(Landroid/graphics/drawable/Drawable;)V

    :cond_9
    iget-object v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mMessage:Ljava/lang/CharSequence;

    if-eqz v0, :cond_a

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setMessage(Ljava/lang/CharSequence;)V

    :cond_a
    iget-boolean v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mIndeterminate:Z

    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setIndeterminate(Z)V

    invoke-direct {p0}, Lmiuix/appcompat/app/ProgressDialog;->onProgressChanged()V

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->onCreate(Landroid/os/Bundle;)V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 10

    goto :goto_5f

    nop

    :goto_0
    iget v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mMax:I

    goto :goto_4e

    nop

    :goto_1
    const v4, 0x101005d

    goto :goto_47

    nop

    :goto_2
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setIndeterminate(Z)V

    goto :goto_56

    nop

    :goto_3
    sget v4, Lmiuix/appcompat/R$attr;->dialogProgressPercentColor:I

    goto :goto_32

    nop

    :goto_4
    invoke-virtual {v1, v4, v2}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v2

    goto :goto_5b

    nop

    :goto_5
    invoke-virtual {v0, v2, v3}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    :goto_6
    goto :goto_57

    nop

    :goto_7
    invoke-static {v2}, Lmiuix/core/util/MiuixUIUtils;->getFontLevel(Landroid/content/Context;)I

    move-result v2

    goto :goto_36

    nop

    :goto_8
    iget v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mIncrementSecondaryBy:I

    goto :goto_46

    nop

    :goto_9
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setMax(I)V

    :goto_a
    goto :goto_48

    nop

    :goto_b
    iput-object v2, p0, Lmiuix/appcompat/app/ProgressDialog;->mProgress:Lmiuix/androidbasewidget/widget/ProgressBar;

    goto :goto_54

    nop

    :goto_c
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setProgressDrawable(Landroid/graphics/drawable/Drawable;)V

    :goto_d
    goto :goto_19

    nop

    :goto_e
    iput-object v2, p0, Lmiuix/appcompat/app/ProgressDialog;->mProgressPercentView:Landroid/widget/TextView;

    goto :goto_2d

    nop

    :goto_f
    invoke-direct {v2, p0, v4}, Lmiuix/appcompat/app/ProgressDialog$1;-><init>(Lmiuix/appcompat/app/ProgressDialog;I)V

    goto :goto_3b

    nop

    :goto_10
    invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;

    move-result-object v2

    goto :goto_7

    nop

    :goto_11
    const/4 v7, 0x1

    goto :goto_3f

    nop

    :goto_12
    invoke-virtual {v0, v2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v2

    goto :goto_53

    nop

    :goto_13
    invoke-virtual {v4}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v4

    goto :goto_1c

    nop

    :goto_14
    sget v2, Lmiuix/appcompat/R$layout;->miuix_appcompat_alert_dialog_progress_xl_font:I

    goto :goto_37

    nop

    :goto_15
    invoke-virtual {v2, v5, v4}, Landroid/content/res/TypedArray;->getColor(II)I

    move-result v4

    goto :goto_27

    nop

    :goto_16
    invoke-virtual {v2}, Landroid/content/Context;->getTheme()Landroid/content/res/Resources$Theme;

    move-result-object v2

    goto :goto_3

    nop

    :goto_17
    iget-object v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mProgressDrawable:Landroid/graphics/drawable/Drawable;

    goto :goto_29

    nop

    :goto_18
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/AlertDialog;->setView(Landroid/view/View;)V

    goto :goto_2b

    nop

    :goto_19
    iget-object v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mIndeterminateDrawable:Landroid/graphics/drawable/Drawable;

    goto :goto_31

    nop

    :goto_1a
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setProgress(I)V

    :goto_1b
    goto :goto_43

    nop

    :goto_1c
    sget v6, Lmiuix/appcompat/R$color;->miuix_appcompat_dialog_default_progress_percent_color:I

    goto :goto_35

    nop

    :goto_1d
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setIndeterminateDrawable(Landroid/graphics/drawable/Drawable;)V

    :goto_1e
    goto :goto_42

    nop

    :goto_1f
    check-cast v2, Lmiuix/androidbasewidget/widget/ProgressBar;

    goto :goto_b

    nop

    :goto_20
    sget v2, Lmiuix/appcompat/R$id;->progress_percent:I

    goto :goto_12

    nop

    :goto_21
    sget v2, Lmiuix/appcompat/R$layout;->miuix_appcompat_alert_dialog_progress:I

    :goto_22
    goto :goto_2a

    nop

    :goto_23
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setSecondaryProgress(I)V

    :goto_24
    goto :goto_33

    nop

    :goto_25
    const/4 v3, 0x0

    goto :goto_1

    nop

    :goto_26
    iput-object v2, p0, Lmiuix/appcompat/app/ProgressDialog;->mMessageView:Landroid/widget/TextView;

    goto :goto_18

    nop

    :goto_27
    invoke-virtual {v2}, Landroid/content/res/TypedArray;->recycle()V

    goto :goto_10

    nop

    :goto_28
    check-cast v2, Landroid/widget/TextView;

    goto :goto_26

    nop

    :goto_29
    if-nez v0, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_c

    nop

    :goto_2a
    sget v4, Lmiuix/appcompat/R$styleable;->AlertDialog_horizontalProgressLayout:I

    goto :goto_4

    nop

    :goto_2b
    invoke-virtual {v1}, Landroid/content/res/TypedArray;->recycle()V

    goto :goto_0

    nop

    :goto_2c
    invoke-virtual {v0, v2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v2

    goto :goto_1f

    nop

    :goto_2d
    goto :goto_6

    :goto_2e
    goto :goto_34

    nop

    :goto_2f
    invoke-virtual {v2, v4}, Landroid/content/res/Resources$Theme;->obtainStyledAttributes([I)Landroid/content/res/TypedArray;

    move-result-object v2

    goto :goto_45

    nop

    :goto_30
    return-void

    :goto_31
    if-nez v0, :cond_1

    goto :goto_1e

    :cond_1
    goto :goto_1d

    nop

    :goto_32
    filled-new-array {v4}, [I

    move-result-object v4

    goto :goto_2f

    nop

    :goto_33
    iget v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mIncrementBy:I

    goto :goto_55

    nop

    :goto_34
    sget v2, Lmiuix/appcompat/R$styleable;->AlertDialog_progressLayout:I

    goto :goto_3d

    nop

    :goto_35
    invoke-virtual {v4, v6}, Landroid/content/res/Resources;->getColor(I)I

    move-result v4

    goto :goto_15

    nop

    :goto_36
    const/4 v6, 0x2

    goto :goto_11

    nop

    :goto_37
    goto :goto_22

    :goto_38
    goto :goto_21

    nop

    :goto_39
    invoke-virtual {v1, v3, v2, v4, v5}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[III)Landroid/content/res/TypedArray;

    move-result-object v1

    goto :goto_4b

    nop

    :goto_3a
    iget v2, p0, Lmiuix/appcompat/app/ProgressDialog;->mProgressStyle:I

    goto :goto_59

    nop

    :goto_3b
    iput-object v2, p0, Lmiuix/appcompat/app/ProgressDialog;->mViewUpdateHandler:Landroid/os/Handler;

    goto :goto_4c

    nop

    :goto_3c
    iget-boolean v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mIndeterminate:Z

    goto :goto_2

    nop

    :goto_3d
    sget v4, Lmiuix/appcompat/R$layout;->miuix_appcompat_progress_dialog:I

    goto :goto_60

    nop

    :goto_3e
    invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;

    move-result-object v1

    goto :goto_61

    nop

    :goto_3f
    if-eq v2, v6, :cond_2

    goto :goto_4a

    :cond_2
    goto :goto_49

    nop

    :goto_40
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->setMessage(Ljava/lang/CharSequence;)V

    :goto_41
    goto :goto_3c

    nop

    :goto_42
    iget-object v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mMessage:Ljava/lang/CharSequence;

    goto :goto_51

    nop

    :goto_43
    iget v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mSecondaryProgressVal:I

    goto :goto_4d

    nop

    :goto_44
    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    goto :goto_3e

    nop

    :goto_45
    invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;

    move-result-object v4

    goto :goto_13

    nop

    :goto_46
    if-gtz v0, :cond_3

    goto :goto_50

    :cond_3
    goto :goto_4f

    nop

    :goto_47
    const/4 v5, 0x0

    goto :goto_39

    nop

    :goto_48
    iget v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mProgressVal:I

    goto :goto_5a

    nop

    :goto_49
    move v5, v7

    :goto_4a
    goto :goto_3a

    nop

    :goto_4b
    invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;

    move-result-object v2

    goto :goto_16

    nop

    :goto_4c
    if-nez v5, :cond_4

    goto :goto_38

    :cond_4
    goto :goto_14

    nop

    :goto_4d
    if-gtz v0, :cond_5

    goto :goto_24

    :cond_5
    goto :goto_23

    nop

    :goto_4e
    if-gtz v0, :cond_6

    goto :goto_a

    :cond_6
    goto :goto_9

    nop

    :goto_4f
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->incrementSecondaryProgressBy(I)V

    :goto_50
    goto :goto_17

    nop

    :goto_51
    if-nez v0, :cond_7

    goto :goto_41

    :cond_7
    goto :goto_40

    nop

    :goto_52
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AlertDialog;->onCreate(Landroid/os/Bundle;)V

    goto :goto_30

    nop

    :goto_53
    check-cast v2, Landroid/widget/TextView;

    goto :goto_e

    nop

    :goto_54
    sget v2, Lmiuix/appcompat/R$id;->message:I

    goto :goto_58

    nop

    :goto_55
    if-gtz v0, :cond_8

    goto :goto_5e

    :cond_8
    goto :goto_5d

    nop

    :goto_56
    invoke-direct {p0}, Lmiuix/appcompat/app/ProgressDialog;->onProgressChanged()V

    goto :goto_52

    nop

    :goto_57
    const v2, 0x102000d

    goto :goto_2c

    nop

    :goto_58
    invoke-virtual {v0, v2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v2

    goto :goto_28

    nop

    :goto_59
    if-eq v2, v7, :cond_9

    goto :goto_2e

    :cond_9
    goto :goto_5c

    nop

    :goto_5a
    if-gtz v0, :cond_a

    goto :goto_1b

    :cond_a
    goto :goto_1a

    nop

    :goto_5b
    invoke-virtual {v0, v2, v3}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    goto :goto_20

    nop

    :goto_5c
    new-instance v2, Lmiuix/appcompat/app/ProgressDialog$1;

    goto :goto_f

    nop

    :goto_5d
    invoke-virtual {p0, v0}, Lmiuix/appcompat/app/ProgressDialog;->incrementProgressBy(I)V

    :goto_5e
    goto :goto_8

    nop

    :goto_5f
    invoke-virtual {p0}, Landroid/app/Dialog;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_44

    nop

    :goto_60
    invoke-virtual {v1, v2, v4}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v2

    goto :goto_5

    nop

    :goto_61
    sget-object v2, Lmiuix/appcompat/R$styleable;->AlertDialog:[I

    goto :goto_25

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_ProgressDialog__onStop',
        'method': '.method protected onStop()V',
        'method_name': 'onStop',
        'method_anchors': ['invoke-super {p0}, Lmiuix/appcompat/app/AlertDialog;->onStop()V', 'iput-boolean v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mHasStarted:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onStop()V
    .registers 2

    invoke-super {p0}, Lmiuix/appcompat/app/AlertDialog;->onStop()V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mHasStarted:Z

    return-void
.end method""",
        'replacement': """.method protected onStop()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Lmiuix/appcompat/app/AlertDialog;->onStop()V

    goto :goto_1

    nop

    :goto_1
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_2
    iput-boolean v0, p0, Lmiuix/appcompat/app/ProgressDialog;->mHasStarted:Z

    goto :goto_3

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
