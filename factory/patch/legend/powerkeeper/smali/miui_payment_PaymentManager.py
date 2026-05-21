TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'miui/payment/PaymentManager.smali'
CLASS_FALLBACK_NAMES = ['PaymentManager.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final ACTION_PAYMENT:Ljava/lang/String; = "com.xiaomi.xmsf.action.PAYMENT"', '.field public static final CAPABILITY:I = 0x3', '.field private static final DEBUG:Z = true', '.field public static final ERROR_CODE_ACCOUNT_CHANGED:I = 0xa', '.field public static final ERROR_CODE_ACCOUNT_FROZEN:I = 0x9']

PATCHES = [
    {
        'id': 'miui_payment_PaymentManager__isMibiServiceDisabled',
        'method': '.method public isMibiServiceDisabled()Z',
        'method_name': 'isMibiServiceDisabled',
        'method_anchors': ['new-instance v0, Landroid/content/Intent;', 'const-string v1, "com.xiaomi.xmsf.action.PAYMENT"', 'invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V', 'const-string v1, "com.xiaomi.payment"', 'invoke-virtual {v0, v1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;', 'iget-object p0, p0, Lmiui/payment/PaymentManager;->mContext:Landroid/content/Context;', 'invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;', 'invoke-virtual {p0, v0, v1}, Landroid/content/pm/PackageManager;->resolveService(Landroid/content/Intent;I)Landroid/content/pm/ResolveInfo;'],
        'type': 'method_replace',
        'search': """.method public isMibiServiceDisabled()Z
    .registers 3

    new-instance v0, Landroid/content/Intent;

    const-string v1, "com.xiaomi.xmsf.action.PAYMENT"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v1, "com.xiaomi.payment"

    invoke-virtual {v0, v1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    iget-object p0, p0, Lmiui/payment/PaymentManager;->mContext:Landroid/content/Context;

    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object p0

    const/4 v1, 0x0

    invoke-virtual {p0, v0, v1}, Landroid/content/pm/PackageManager;->resolveService(Landroid/content/Intent;I)Landroid/content/pm/ResolveInfo;

    move-result-object p0

    const/4 v0, 0x1

    if-nez p0, :cond_0

    return v0

    :cond_0
    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p0, :cond_1

    const-string p0, "HK"

    invoke-static {p0}, Lmiui/os/Build;->checkRegion(Ljava/lang/String;)Z

    move-result p0

    if-nez p0, :cond_1

    return v0

    :cond_1
    return v1
.end method""",
        'replacement': """.method public isMibiServiceDisabled()Z
    .registers 3

    new-instance v0, Landroid/content/Intent;

    const-string v1, "com.xiaomi.xmsf.action.PAYMENT"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v1, "com.xiaomi.payment"

    invoke-virtual {v0, v1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    iget-object p0, p0, Lmiui/payment/PaymentManager;->mContext:Landroid/content/Context;

    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object p0

    const/4 v1, 0x0

    invoke-virtual {p0, v0, v1}, Landroid/content/pm/PackageManager;->resolveService(Landroid/content/Intent;I)Landroid/content/pm/ResolveInfo;

    move-result-object p0

    const/4 v0, 0x1

    if-nez p0, :cond_0

    return v0

    :cond_0
    sget-boolean p0, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz p0, :cond_1

    const-string p0, "HK"

    invoke-static {p0}, Lmiui/os/Build;->checkRegion(Ljava/lang/String;)Z

    move-result p0

    if-nez p0, :cond_1

    return v0

    :cond_1
    return v1
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
