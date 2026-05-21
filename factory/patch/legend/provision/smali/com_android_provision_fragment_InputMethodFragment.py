TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/InputMethodFragment.smali'
CLASS_FALLBACK_NAMES = ['InputMethodFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseListFragment;', '.field public static final GLOBAL_DEFAULT_IME_BAIDU_FACEMOJI:Ljava/lang/String; = "com.facemoji.lite.xiaomi/com.baidu.simeji.SimejiIME"', '.field public static final GLOBAL_DEFAULT_IME_EMOJI:Ljava/lang/String; = "com.preff.kb.xm/com.preff.kb.LatinIME"', '.field public static final GLOBAL_DEFAULT_IME_GBOARD:Ljava/lang/String; = "com.google.android.inputmethod.latin/com.android.inputmethod.latin.LatinIME"', '.field public static final GLOBAL_DEFAULT_IME_KIKA:Ljava/lang/String; = "com.kikaoem.xiaomi.qisiemoji.inputmethod/com.android.inputmethod.latin.LatinIME"', '.field public static final GLOBAL_DEFAULT_IME_MINT:Ljava/lang/String; = "com.mint.keyboard/.services.MintKeyboard"']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_InputMethodFragment__initInputMethodList',
        'method': '.method private initInputMethodList()V',
        'method_name': 'initInputMethodList',
        'method_anchors': ['iget-object v0, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodManager:Landroid/view/inputmethod/InputMethodManager;', 'invoke-virtual {v0}, Landroid/view/inputmethod/InputMethodManager;->getInputMethodList()Ljava/util/List;', 'iput-object v0, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodInfos:Ljava/util/List;', 'invoke-interface {v0}, Ljava/util/List;->size()I', 'if-ltz v0, :cond_1', 'sget-object v1, Lcom/android/provision/fragment/InputMethodFragment;->sBlackImmSet:Ljava/util/HashSet;', 'iget-object v2, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodInfos:Ljava/util/List;', 'invoke-interface {v2, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;'],
        'type': 'policy_skip',
        'search': """.method private initInputMethodList()V
    .registers 4

    iget-object v0, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodManager:Landroid/view/inputmethod/InputMethodManager;

    invoke-virtual {v0}, Landroid/view/inputmethod/InputMethodManager;->getInputMethodList()Ljava/util/List;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodInfos:Ljava/util/List;

    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v0

    add-int/lit8 v0, v0, -0x1

    :goto_0
    if-ltz v0, :cond_1

    sget-object v1, Lcom/android/provision/fragment/InputMethodFragment;->sBlackImmSet:Ljava/util/HashSet;

    iget-object v2, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodInfos:Ljava/util/List;

    invoke-interface {v2, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Landroid/view/inputmethod/InputMethodInfo;

    invoke-virtual {v2}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/util/HashSet;->contains(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_0

    iget-object v1, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodInfos:Ljava/util/List;

    invoke-interface {v1, v0}, Ljava/util/List;->remove(I)Ljava/lang/Object;

    :cond_0
    add-int/lit8 v0, v0, -0x1

    goto :goto_0

    :cond_1
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_2

    invoke-direct {p0}, Lcom/android/provision/fragment/InputMethodFragment;->getOrganizedImeList()[Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodInfos:Ljava/util/List;

    new-instance v2, Lcom/android/provision/fragment/InputMethodFragment$2;

    invoke-direct {v2, p0, v0}, Lcom/android/provision/fragment/InputMethodFragment$2;-><init>(Lcom/android/provision/fragment/InputMethodFragment;[Ljava/lang/String;)V

    invoke-static {v1, v2}, Ljava/util/Collections;->sort(Ljava/util/List;Ljava/util/Comparator;)V

    iget-object v0, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodInfos:Ljava/util/List;

    const/4 v1, 0x0

    invoke-interface {v0, v1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/view/inputmethod/InputMethodInfo;

    invoke-virtual {v0}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/fragment/InputMethodFragment;->mCurrentInputMethod:Ljava/lang/String;

    return-void

    :cond_2
    invoke-direct {p0}, Lcom/android/provision/fragment/InputMethodFragment;->getDefaultIme()Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/fragment/InputMethodFragment;->mCurrentInputMethod:Ljava/lang/String;

    invoke-direct {p0}, Lcom/android/provision/fragment/InputMethodFragment;->resortInputMethodItem()V

    return-void
.end method""",
        'replacement': """.method private initInputMethodList()V
    .registers 4

    iget-object v0, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodManager:Landroid/view/inputmethod/InputMethodManager;

    invoke-virtual {v0}, Landroid/view/inputmethod/InputMethodManager;->getInputMethodList()Ljava/util/List;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodInfos:Ljava/util/List;

    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v0

    add-int/lit8 v0, v0, -0x1

    :goto_0
    if-ltz v0, :cond_1

    sget-object v1, Lcom/android/provision/fragment/InputMethodFragment;->sBlackImmSet:Ljava/util/HashSet;

    iget-object v2, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodInfos:Ljava/util/List;

    invoke-interface {v2, v0}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Landroid/view/inputmethod/InputMethodInfo;

    invoke-virtual {v2}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/util/HashSet;->contains(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_0

    iget-object v1, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodInfos:Ljava/util/List;

    invoke-interface {v1, v0}, Ljava/util/List;->remove(I)Ljava/lang/Object;

    :cond_0
    add-int/lit8 v0, v0, -0x1

    goto :goto_0

    :cond_1
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_2

    invoke-direct {p0}, Lcom/android/provision/fragment/InputMethodFragment;->getOrganizedImeList()[Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodInfos:Ljava/util/List;

    new-instance v2, Lcom/android/provision/fragment/InputMethodFragment$2;

    invoke-direct {v2, p0, v0}, Lcom/android/provision/fragment/InputMethodFragment$2;-><init>(Lcom/android/provision/fragment/InputMethodFragment;[Ljava/lang/String;)V

    invoke-static {v1, v2}, Ljava/util/Collections;->sort(Ljava/util/List;Ljava/util/Comparator;)V

    iget-object v0, p0, Lcom/android/provision/fragment/InputMethodFragment;->mInputMethodInfos:Ljava/util/List;

    const/4 v1, 0x0

    invoke-interface {v0, v1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/view/inputmethod/InputMethodInfo;

    invoke-virtual {v0}, Landroid/view/inputmethod/InputMethodInfo;->getId()Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/fragment/InputMethodFragment;->mCurrentInputMethod:Ljava/lang/String;

    return-void

    :cond_2
    invoke-direct {p0}, Lcom/android/provision/fragment/InputMethodFragment;->getDefaultIme()Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/fragment/InputMethodFragment;->mCurrentInputMethod:Ljava/lang/String;

    invoke-direct {p0}, Lcom/android/provision/fragment/InputMethodFragment;->resortInputMethodItem()V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
