TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'com/miui/powerkeeper/unionpower/utils/UnionPowerConfig.smali'
CLASS_FALLBACK_NAMES = ['UnionPowerConfig.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final a:Z', '.field public static final b:Z', '.field private static final c:Ljava/lang/String;', '.field private static final d:Ljava/lang/String;', '.field private static final e:Ljava/lang/String;']

PATCHES = [
    {
        'id': 'com_miui_powerkeeper_unionpower_utils_UnionPowerConfig__d',
        'method': '.method private static d(Landroid/content/Context;)Ljava/util/Map;',
        'method_name': 'd',
        'method_anchors': ['const-string v0, "list assets error ="', 'const-string v1, "UnionPower"', 'const-string v2, "union_power/"', 'new-instance v3, Ljava/util/HashMap;', 'invoke-direct {v3}, Ljava/util/HashMap;-><init>()V', 'invoke-virtual {p0}, Landroid/content/Context;->getAssets()Landroid/content/res/AssetManager;', 'invoke-virtual {v5, v2}, Landroid/content/res/AssetManager;->list(Ljava/lang/String;)[Ljava/lang/String;', 'if-nez v5, :cond_0'],
        'type': 'method_token_replace',
        'search': 'Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z',
        'replacement': 'Lmiui/os/Build;->IS_MIUI:Z',
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'Scoped token swap only — leaves all string literals (including .+\\.config) exactly as stock, avoids invalid smali escape errors.',
    },
]
