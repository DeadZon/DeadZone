TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/utils/CarouselUtils.smali'
CLASS_FALLBACK_NAMES = ['CarouselUtils.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final CONTENT_URI_LOCK_MAGAZINE_DEFAULT:Ljava/lang/String;', '.field private static final EXTRAS_GET_CAROUSEL_MESSAGE:Ljava/lang/String; = "type"', '.field private static final METHOD_GET_CAROUSEL_MESSAGE:Ljava/lang/String; = "provision_get_message"', '.field private static final METHOD_SET_CAROUSEL_MESSAGE:Ljava/lang/String; = "provision_set_message"', '.field public static final PEP_MODEL:Z']

PATCHES = [
    {
        'id': 'com_android_provision_utils_CarouselUtils__isProviderAvailable',
        'method': '.method private static isProviderAvailable()Z',
        'method_name': 'isProviderAvailable',
        'method_anchors': ['invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;', 'sget-object v1, Lcom/android/provision/utils/CarouselUtils;->CONTENT_URI_LOCK_MAGAZINE_DEFAULT:Ljava/lang/String;', 'invoke-static {v1}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;', 'invoke-virtual {v0, v1}, Landroid/content/ContentResolver;->acquireUnstableProvider(Landroid/net/Uri;)Landroid/content/IContentProvider;', 'if-eqz v1, :cond_0', 'invoke-virtual {v0, v1}, Landroid/content/ContentResolver;->releaseUnstableProvider(Landroid/content/IContentProvider;)Z'],
        'type': 'method_add',
        'search': None,
        'replacement': """.method private static isProviderAvailable()Z
    .registers 2

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    sget-object v1, Lcom/android/provision/utils/CarouselUtils;->CONTENT_URI_LOCK_MAGAZINE_DEFAULT:Ljava/lang/String;

    invoke-static {v1}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/content/ContentResolver;->acquireUnstableProvider(Landroid/net/Uri;)Landroid/content/IContentProvider;

    move-result-object v1

    if-eqz v1, :cond_0

    invoke-virtual {v0, v1}, Landroid/content/ContentResolver;->releaseUnstableProvider(Landroid/content/IContentProvider;)Z

    const/4 v0, 0x1

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    return v0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_CarouselUtils__shouldShowCarousel',
        'method': '.method private static shouldShowCarousel()Z',
        'method_name': 'shouldShowCarousel',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_1', 'invoke-static {}, Lcom/android/provision/utils/CarouselUtils;->isCarouselForbid()Z', 'if-nez v0, :cond_1', 'sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sCarouselSupport:Ljava/util/HashMap;', 'invoke-static {}, Lmiui/os/Build;->getRegion()Ljava/lang/String;', 'invoke-virtual {v1}, Ljava/lang/String;->toUpperCase()Ljava/lang/String;', 'invoke-virtual {v0, v1}, Ljava/util/HashMap;->containsKey(Ljava/lang/Object;)Z'],
        'type': 'method_replace',
        'search': """.method private static shouldShowCarousel()Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    invoke-static {}, Lcom/android/provision/utils/CarouselUtils;->isCarouselForbid()Z

    move-result v0

    if-nez v0, :cond_1

    sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sCarouselSupport:Ljava/util/HashMap;

    invoke-static {}, Lmiui/os/Build;->getRegion()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/String;->toUpperCase()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/util/HashMap;->containsKey(Ljava/lang/Object;)Z

    move-result v0

    const/4 v1, 0x1

    if-nez v0, :cond_0

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getCarouselEnable()I

    move-result v0

    if-ne v0, v1, :cond_1

    :cond_0
    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result v0

    if-nez v0, :cond_1

    return v1

    :cond_1
    const/4 v0, 0x0

    return v0
.end method""",
        'replacement': """.method private static shouldShowCarousel()Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    invoke-static {}, Lcom/android/provision/utils/CarouselUtils;->isCarouselForbid()Z

    move-result v0

    if-nez v0, :cond_1

    sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sCarouselSupport:Ljava/util/HashMap;

    invoke-static {}, Lmiui/os/Build;->getRegion()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/String;->toUpperCase()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/util/HashMap;->containsKey(Ljava/lang/Object;)Z

    move-result v0

    const/4 v1, 0x1

    if-nez v0, :cond_0

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getCarouselEnable()I

    move-result v0

    if-ne v0, v1, :cond_1

    :cond_0
    invoke-static {}, Lcom/android/provision/utils/CarouselUtils;->isProviderAvailable()Z

    move-result v0

    if-eqz v0, :cond_1

    return v1

    :cond_1
    const/4 v0, 0x0

    return v0
.end method""",
        'required': True,
        'policy_status': 'BUILD_FLAG_PARTIALLY_SKIPPED',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_utils_CarouselUtils__clinit',
        'method': '.method static constructor <clinit>()V',
        'method_name': '<clinit>',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'const-string v0, "com.miui.android.fashiongallery.lockscreen_magazine_provider"', 'const-string v0, "com.xiaomi.tv.gallerylockscreen.lockscreen_magazine_provider"', 'sput-object v0, Lcom/android/provision/utils/CarouselUtils;->PROVIDER_URI_LOCK_MAGAZINE_DEFAULT:Ljava/lang/String;', 'new-instance v1, Ljava/lang/StringBuilder;', 'invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v2, "content://"'],
        'type': 'method_replace',
        'search': """.method static constructor <clinit>()V
    .registers 24

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    const-string v0, "com.miui.android.fashiongallery.lockscreen_magazine_provider"

    goto :goto_0

    :cond_0
    const-string v0, "com.xiaomi.tv.gallerylockscreen.lockscreen_magazine_provider"

    :goto_0
    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->PROVIDER_URI_LOCK_MAGAZINE_DEFAULT:Ljava/lang/String;

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "content://"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->CONTENT_URI_LOCK_MAGAZINE_DEFAULT:Ljava/lang/String;

    const-string v0, "ro.com.miui.rsa.feature"

    invoke-static {v0}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    const-string v1, "tier3"

    invoke-virtual {v1, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    sput-boolean v0, Lcom/android/provision/utils/CarouselUtils;->PEP_MODEL:Z

    new-instance v0, Ljava/util/ArrayList;

    const-string v15, "cz_vodafone"

    const-string v16, "ro_vodafone"

    const-string v1, "mx_telcel"

    const-string v2, "mx_at"

    const-string v3, "lm_cr"

    const-string v4, "jp_kd"

    const-string v5, "cl_entel"

    const-string v6, "es_telefonica"

    const-string v7, "es_vodafone"

    const-string v8, "ie_vodafone"

    const-string v9, "de_vodafone"

    const-string v10, "nl_vodafone"

    const-string v11, "pt_vodafone"

    const-string v12, "gr_vodafone"

    const-string v13, "gb_vodafone"

    const-string v14, "it_vodafone"

    filled-new-array/range {v1 .. v16}, [Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v1

    invoke-direct {v0, v1}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->sUnsupportedGalleryRegion:Ljava/util/List;

    const-string v22, "redwoodin"

    const-string v23, "water"

    const-string v2, "diting"

    const-string v3, "plato"

    const-string v4, "nuwa"

    const-string v5, "fuxi"

    const-string v6, "ishtar"

    const-string v7, "ruby"

    const-string v8, "rubypro"

    const-string v9, "sunstone"

    const-string v10, "moonstone"

    const-string v11, "earth"

    const-string v12, "aether"

    const-string v13, "redwood"

    const-string v14, "ziyi"

    const-string v15, "tapas"

    const-string v16, "topaz"

    const-string v17, "cloud"

    const-string v18, "diamond"

    const-string v19, "mondrian"

    const-string v20, "marble"

    const-string v21, "marblein"

    filled-new-array/range {v2 .. v23}, [Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v0

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->mSupportRSA4:Ljava/util/List;

    const-string v0, "TF"

    const-string v1, "AT"

    const-string v2, "VF"

    filled-new-array {v2, v0, v1}, [Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v0

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->sUnsupportedGalleryCota:Ljava/util/List;

    new-instance v0, Lcom/android/provision/utils/CarouselUtils$1;

    invoke-direct {v0}, Lcom/android/provision/utils/CarouselUtils$1;-><init>()V

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->sCarouselSupport:Ljava/util/HashMap;

    new-instance v0, Ljava/util/HashMap;

    invoke-direct {v0}, Ljava/util/HashMap;-><init>()V

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->sMultiRegion:Ljava/util/HashMap;

    invoke-static {}, Lcom/android/provision/utils/CarouselUtils;->isJpSbDevice()Z

    move-result v0

    const/4 v1, 0x0

    const-string v2, "JP"

    if-eqz v0, :cond_1

    sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sMultiRegion:Ljava/util/HashMap;

    new-instance v3, Lcom/android/provision/beans/CarouselBean;

    invoke-direct {v3, v1}, Lcom/android/provision/beans/CarouselBean;-><init>(Z)V

    invoke-virtual {v3}, Lcom/android/provision/beans/CarouselBean;->buildGlance()Lcom/android/provision/beans/CarouselBean;

    move-result-object v1

    invoke-virtual {v0, v2, v1}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_1

    :cond_1
    sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sMultiRegion:Ljava/util/HashMap;

    new-instance v3, Lcom/android/provision/beans/CarouselBean;

    invoke-direct {v3, v1}, Lcom/android/provision/beans/CarouselBean;-><init>(Z)V

    const/4 v1, 0x1

    invoke-virtual {v3, v1}, Lcom/android/provision/beans/CarouselBean;->withGdpr(Z)Lcom/android/provision/beans/CarouselBean;

    move-result-object v1

    const-string v3, "https://www.taboola.com/ja/policies/%e3%83%97%e3%83%a9%e3%82%a4%e3%83%90%e3%82%b7%e3%83%bc%e3%83%9d%e3%83%aa%e3%82%b7%e3%83%bc"

    invoke-virtual {v1, v3}, Lcom/android/provision/beans/CarouselBean;->withPrivacy(Ljava/lang/String;)Lcom/android/provision/beans/CarouselBean;

    move-result-object v1

    const-string v3, "https://www.taboola.com/ja/policies/xiaomi-taboola-terms-of-service"

    invoke-virtual {v1, v3}, Lcom/android/provision/beans/CarouselBean;->withAgreement(Ljava/lang/String;)Lcom/android/provision/beans/CarouselBean;

    move-result-object v1

    const-string v3, "https://www.taboola.com/ja/policies/cookie-policy"

    invoke-virtual {v1, v3}, Lcom/android/provision/beans/CarouselBean;->withCookie(Ljava/lang/String;)Lcom/android/provision/beans/CarouselBean;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/provision/beans/CarouselBean;->buildTaboola()Lcom/android/provision/beans/CarouselBean;

    move-result-object v1

    invoke-virtual {v0, v2, v1}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :goto_1
    new-instance v0, Lcom/android/provision/utils/CarouselUtils$2;

    invoke-direct {v0}, Lcom/android/provision/utils/CarouselUtils$2;-><init>()V

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->sNiceRegion:Ljava/util/HashMap;

    new-instance v0, Lcom/android/provision/utils/CarouselUtils$3;

    invoke-direct {v0}, Lcom/android/provision/utils/CarouselUtils$3;-><init>()V

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->sTaboolaRegion:Ljava/util/HashMap;

    sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sCarouselSupport:Ljava/util/HashMap;

    sget-object v1, Lcom/android/provision/utils/CarouselUtils;->sNiceRegion:Ljava/util/HashMap;

    invoke-virtual {v0, v1}, Ljava/util/HashMap;->putAll(Ljava/util/Map;)V

    sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sCarouselSupport:Ljava/util/HashMap;

    sget-object v1, Lcom/android/provision/utils/CarouselUtils;->sTaboolaRegion:Ljava/util/HashMap;

    invoke-virtual {v0, v1}, Ljava/util/HashMap;->putAll(Ljava/util/Map;)V

    sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sCarouselSupport:Ljava/util/HashMap;

    sget-object v1, Lcom/android/provision/utils/CarouselUtils;->sMultiRegion:Ljava/util/HashMap;

    invoke-virtual {v0, v1}, Ljava/util/HashMap;->putAll(Ljava/util/Map;)V

    return-void
.end method""",
        'replacement': """.method static constructor <clinit>()V
    .registers 24

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "content://"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-object v1, Lcom/android/provision/utils/CarouselUtils;->PROVIDER_URI_LOCK_MAGAZINE_DEFAULT:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->CONTENT_URI_LOCK_MAGAZINE_DEFAULT:Ljava/lang/String;

    const-string v0, "ro.com.miui.rsa.feature"

    invoke-static {v0}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    const-string v1, "tier3"

    invoke-virtual {v1, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    sput-boolean v0, Lcom/android/provision/utils/CarouselUtils;->PEP_MODEL:Z

    new-instance v0, Ljava/util/ArrayList;

    const-string v15, "cz_vodafone"

    const-string v16, "ro_vodafone"

    const-string v1, "mx_telcel"

    const-string v2, "mx_at"

    const-string v3, "lm_cr"

    const-string v4, "jp_kd"

    const-string v5, "cl_entel"

    const-string v6, "es_telefonica"

    const-string v7, "es_vodafone"

    const-string v8, "ie_vodafone"

    const-string v9, "de_vodafone"

    const-string v10, "nl_vodafone"

    const-string v11, "pt_vodafone"

    const-string v12, "gr_vodafone"

    const-string v13, "gb_vodafone"

    const-string v14, "it_vodafone"

    filled-new-array/range {v1 .. v16}, [Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v1

    invoke-direct {v0, v1}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->sUnsupportedGalleryRegion:Ljava/util/List;

    const-string v22, "redwoodin"

    const-string v23, "water"

    const-string v2, "diting"

    const-string v3, "plato"

    const-string v4, "nuwa"

    const-string v5, "fuxi"

    const-string v6, "ishtar"

    const-string v7, "ruby"

    const-string v8, "rubypro"

    const-string v9, "sunstone"

    const-string v10, "moonstone"

    const-string v11, "earth"

    const-string v12, "aether"

    const-string v13, "redwood"

    const-string v14, "ziyi"

    const-string v15, "tapas"

    const-string v16, "topaz"

    const-string v17, "cloud"

    const-string v18, "diamond"

    const-string v19, "mondrian"

    const-string v20, "marble"

    const-string v21, "marblein"

    filled-new-array/range {v2 .. v23}, [Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v0

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->mSupportRSA4:Ljava/util/List;

    const-string v0, "TF"

    const-string v1, "AT"

    const-string v2, "VF"

    filled-new-array {v2, v0, v1}, [Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v0

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->sUnsupportedGalleryCota:Ljava/util/List;

    new-instance v0, Lcom/android/provision/utils/CarouselUtils$1;

    invoke-direct {v0}, Lcom/android/provision/utils/CarouselUtils$1;-><init>()V

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->sCarouselSupport:Ljava/util/HashMap;

    new-instance v0, Ljava/util/HashMap;

    invoke-direct {v0}, Ljava/util/HashMap;-><init>()V

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->sMultiRegion:Ljava/util/HashMap;

    invoke-static {}, Lcom/android/provision/utils/CarouselUtils;->isJpSbDevice()Z

    move-result v0

    const/4 v1, 0x0

    const-string v2, "JP"

    if-eqz v0, :cond_0

    sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sMultiRegion:Ljava/util/HashMap;

    new-instance v3, Lcom/android/provision/beans/CarouselBean;

    invoke-direct {v3, v1}, Lcom/android/provision/beans/CarouselBean;-><init>(Z)V

    invoke-virtual {v3}, Lcom/android/provision/beans/CarouselBean;->buildGlance()Lcom/android/provision/beans/CarouselBean;

    move-result-object v1

    invoke-virtual {v0, v2, v1}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_0

    :cond_0
    sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sMultiRegion:Ljava/util/HashMap;

    new-instance v3, Lcom/android/provision/beans/CarouselBean;

    invoke-direct {v3, v1}, Lcom/android/provision/beans/CarouselBean;-><init>(Z)V

    const/4 v1, 0x1

    invoke-virtual {v3, v1}, Lcom/android/provision/beans/CarouselBean;->withGdpr(Z)Lcom/android/provision/beans/CarouselBean;

    move-result-object v1

    const-string v3, "https://www.taboola.com/ja/policies/%e3%83%97%e3%83%a9%e3%82%a4%e3%83%90%e3%82%b7%e3%83%bc%e3%83%9d%e3%83%aa%e3%82%b7%e3%83%bc"

    invoke-virtual {v1, v3}, Lcom/android/provision/beans/CarouselBean;->withPrivacy(Ljava/lang/String;)Lcom/android/provision/beans/CarouselBean;

    move-result-object v1

    const-string v3, "https://www.taboola.com/ja/policies/xiaomi-taboola-terms-of-service"

    invoke-virtual {v1, v3}, Lcom/android/provision/beans/CarouselBean;->withAgreement(Ljava/lang/String;)Lcom/android/provision/beans/CarouselBean;

    move-result-object v1

    const-string v3, "https://www.taboola.com/ja/policies/cookie-policy"

    invoke-virtual {v1, v3}, Lcom/android/provision/beans/CarouselBean;->withCookie(Ljava/lang/String;)Lcom/android/provision/beans/CarouselBean;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/provision/beans/CarouselBean;->buildTaboola()Lcom/android/provision/beans/CarouselBean;

    move-result-object v1

    invoke-virtual {v0, v2, v1}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :goto_0
    new-instance v0, Lcom/android/provision/utils/CarouselUtils$2;

    invoke-direct {v0}, Lcom/android/provision/utils/CarouselUtils$2;-><init>()V

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->sNiceRegion:Ljava/util/HashMap;

    new-instance v0, Lcom/android/provision/utils/CarouselUtils$3;

    invoke-direct {v0}, Lcom/android/provision/utils/CarouselUtils$3;-><init>()V

    sput-object v0, Lcom/android/provision/utils/CarouselUtils;->sTaboolaRegion:Ljava/util/HashMap;

    sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sCarouselSupport:Ljava/util/HashMap;

    sget-object v1, Lcom/android/provision/utils/CarouselUtils;->sNiceRegion:Ljava/util/HashMap;

    invoke-virtual {v0, v1}, Ljava/util/HashMap;->putAll(Ljava/util/Map;)V

    sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sCarouselSupport:Ljava/util/HashMap;

    sget-object v1, Lcom/android/provision/utils/CarouselUtils;->sTaboolaRegion:Ljava/util/HashMap;

    invoke-virtual {v0, v1}, Ljava/util/HashMap;->putAll(Ljava/util/Map;)V

    sget-object v0, Lcom/android/provision/utils/CarouselUtils;->sCarouselSupport:Ljava/util/HashMap;

    sget-object v1, Lcom/android/provision/utils/CarouselUtils;->sMultiRegion:Ljava/util/HashMap;

    invoke-virtual {v0, v1}, Ljava/util/HashMap;->putAll(Ljava/util/Map;)V

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
