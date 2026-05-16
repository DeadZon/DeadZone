# classes7.dex

.class public final Landroid/security/WukongFrameworkBridge;
.super Ljava/lang/Object;
.source "WukongFrameworkBridge.java"


# static fields
.field private static final CURRENT_APP:Ljava/lang/reflect/Method;

.field private static final CURRENT_PACKAGE:Ljava/lang/reflect/Method;

.field private static final CURRENT_THREAD:Ljava/lang/reflect/Method;

.field private static final EXTRA_ALGORITHM:Ljava/lang/String; = "algorithm"

.field private static final EXTRA_ALIAS:Ljava/lang/String; = "alias"

.field private static final EXTRA_ATTESTATION_CHALLENGE:Ljava/lang/String; = "attestation_challenge"

.field private static final EXTRA_ATTEST_ALIAS:Ljava/lang/String; = "attest_alias"

.field private static final EXTRA_ATTEST_DOMAIN:Ljava/lang/String; = "attest_domain"

.field private static final EXTRA_ATTEST_NAMESPACE:Ljava/lang/String; = "attest_namespace"

.field private static final EXTRA_BRAND:Ljava/lang/String; = "brand"

.field private static final EXTRA_CERTIFICATE:Ljava/lang/String; = "certificate"

.field private static final EXTRA_CERTIFICATE_CHAIN:Ljava/lang/String; = "certificate_chain"

.field private static final EXTRA_CERTIFICATE_NOT_AFTER:Ljava/lang/String; = "certificate_not_after"

.field private static final EXTRA_CERTIFICATE_NOT_BEFORE:Ljava/lang/String; = "certificate_not_before"

.field private static final EXTRA_CERTIFICATE_SERIAL:Ljava/lang/String; = "certificate_serial"

.field private static final EXTRA_CERTIFICATE_SUBJECT:Ljava/lang/String; = "certificate_subject"

.field private static final EXTRA_DEVICE:Ljava/lang/String; = "device"

.field private static final EXTRA_DIGESTS:Ljava/lang/String; = "digests"

.field private static final EXTRA_DOMAIN:Ljava/lang/String; = "domain"

.field private static final EXTRA_EC_CURVE:Ljava/lang/String; = "ec_curve"

.field private static final EXTRA_ENTROPY:Ljava/lang/String; = "entropy"

.field private static final EXTRA_FLAGS:Ljava/lang/String; = "flags"

.field private static final EXTRA_IMEI:Ljava/lang/String; = "imei"

.field private static final EXTRA_INTERCEPTED:Ljava/lang/String; = "intercepted"

.field private static final EXTRA_KEY_SIZE:Ljava/lang/String; = "key_size"

.field private static final EXTRA_MANUFACTURER:Ljava/lang/String; = "manufacturer"

.field private static final EXTRA_MEID:Ljava/lang/String; = "meid"

.field private static final EXTRA_MODEL:Ljava/lang/String; = "model"

.field private static final EXTRA_NAMESPACE:Ljava/lang/String; = "namespace"

.field private static final EXTRA_PRODUCT:Ljava/lang/String; = "product"

.field private static final EXTRA_PURPOSES:Ljava/lang/String; = "purposes"

.field private static final EXTRA_RSA_PUBLIC_EXPONENT:Ljava/lang/String; = "rsa_public_exponent"

.field private static final EXTRA_SECOND_IMEI:Ljava/lang/String; = "second_imei"

.field private static final EXTRA_SECURITY_LEVEL:Ljava/lang/String; = "security_level"

.field private static final EXTRA_SERIAL:Ljava/lang/String; = "serial"

.field private static final GET_SERVICE:Ljava/lang/reflect/Method;

.field private static final KS2_SERVICE:Ljava/lang/String; = "android.system.keystore2.IKeystoreService/default"

.field private static final MANAGER_PACKAGE:Ljava/lang/String; = "io.github.beakthoven.wukong.manager"

.field private static final METHOD_DELETE_KEY:Ljava/lang/String; = "delete_key"

.field private static final METHOD_GENERATE_KEY:Ljava/lang/String; = "generate_key"

.field private static final METHOD_POST_GET_KEY_ENTRY:Ljava/lang/String; = "post_get_key_entry"

.field private static final METHOD_PRE_GET_KEY_ENTRY:Ljava/lang/String; = "pre_get_key_entry"

.field private static final PROVIDER_AUTHORITY:Ljava/lang/String; = "io.github.beakthoven.wukong.manager.bridge"

.field private static final TAG:Ljava/lang/String; = "WukongFrameworkBridge"

.field private static final WAIT_FOR_SERVICE:Ljava/lang/reflect/Method;


# direct methods
.method static constructor <clinit>()V
    .registers 2

    .line 70
    const-string v0, "currentApplication"

    const-string v1, "android.app.ActivityThread"

    invoke-static {v1, v0}, Landroid/security/WukongFrameworkBridge;->getStaticMethod(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/reflect/Method;

    move-result-object v0

    sput-object v0, Landroid/security/WukongFrameworkBridge;->CURRENT_APP:Ljava/lang/reflect/Method;

    .line 71
    const-string v0, "currentActivityThread"

    invoke-static {v1, v0}, Landroid/security/WukongFrameworkBridge;->getStaticMethod(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/reflect/Method;

    move-result-object v0

    sput-object v0, Landroid/security/WukongFrameworkBridge;->CURRENT_THREAD:Ljava/lang/reflect/Method;

    .line 72
    const-string v0, "currentPackageName"

    invoke-static {v1, v0}, Landroid/security/WukongFrameworkBridge;->getStaticMethod(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/reflect/Method;

    move-result-object v0

    sput-object v0, Landroid/security/WukongFrameworkBridge;->CURRENT_PACKAGE:Ljava/lang/reflect/Method;

    .line 73
    const-string v0, "waitForService"

    invoke-static {v0}, Landroid/security/WukongFrameworkBridge;->getServiceMethod(Ljava/lang/String;)Ljava/lang/reflect/Method;

    move-result-object v0

    sput-object v0, Landroid/security/WukongFrameworkBridge;->WAIT_FOR_SERVICE:Ljava/lang/reflect/Method;

    .line 74
    const-string v0, "getService"

    invoke-static {v0}, Landroid/security/WukongFrameworkBridge;->getServiceMethod(Ljava/lang/String;)Ljava/lang/reflect/Method;

    move-result-object v0

    sput-object v0, Landroid/security/WukongFrameworkBridge;->GET_SERVICE:Ljava/lang/reflect/Method;

    return-void
.end method

.method private constructor <init>()V
    .registers 1

    .line 76
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method private static acquireProvider(Ljava/lang/Object;Landroid/app/Application;)Ljava/lang/Object;
    .registers 10
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/Exception;
        }
    .end annotation

    .line 340
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    const/4 v1, 0x4

    new-array v2, v1, [Ljava/lang/Class;

    const-class v3, Landroid/content/Context;

    const/4 v4, 0x0

    aput-object v3, v2, v4

    const-class v3, Ljava/lang/String;

    const/4 v5, 0x1

    aput-object v3, v2, v5

    sget-object v3, Ljava/lang/Integer;->TYPE:Ljava/lang/Class;

    const/4 v6, 0x2

    aput-object v3, v2, v6

    sget-object v3, Ljava/lang/Boolean;->TYPE:Ljava/lang/Class;

    const/4 v7, 0x3

    aput-object v3, v2, v7

    const-string v3, "acquireProvider"

    invoke-virtual {v0, v3, v2}, Ljava/lang/Class;->getMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v0

    .line 346
    invoke-virtual {v0, v5}, Ljava/lang/reflect/Method;->setAccessible(Z)V

    .line 347
    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    new-array v1, v1, [Ljava/lang/Object;

    aput-object p1, v1, v4

    const-string p1, "io.github.beakthoven.wukong.manager.bridge"

    aput-object p1, v1, v5

    aput-object v2, v1, v6

    sget-object p1, Ljava/lang/Boolean;->TRUE:Ljava/lang/Boolean;

    aput-object p1, v1, v7

    invoke-virtual {v0, p0, v1}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0
.end method

.method private static buildAuthorizations(Landroid/os/Bundle;I)[Landroid/system/keystore2/Authorization;
    .registers 9

    .line 234
    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    .line 235
    const-string v1, "purposes"

    invoke-virtual {p0, v1}, Landroid/os/Bundle;->getIntArray(Ljava/lang/String;)[I

    move-result-object v1

    .line 236
    const/4 v2, 0x0

    if-eqz v1, :cond_25

    .line 237
    array-length v3, v1

    const/4 v4, 0x0

    :goto_10
    if-ge v4, v3, :cond_25

    aget v5, v1, v4

    .line 238
    const v6, 0x20000001

    invoke-static {v5}, Landroid/hardware/security/keymint/KeyParameterValue;->keyPurpose(I)Landroid/hardware/security/keymint/KeyParameterValue;

    move-result-object v5

    invoke-static {v6, v5, p1}, Landroid/security/WukongFrameworkBridge;->newAuthorization(ILandroid/hardware/security/keymint/KeyParameterValue;I)Landroid/system/keystore2/Authorization;

    move-result-object v5

    invoke-virtual {v0, v5}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 237
    add-int/lit8 v4, v4, 0x1

    goto :goto_10

    .line 241
    :cond_25
    const-string v1, "digests"

    invoke-virtual {p0, v1}, Landroid/os/Bundle;->getIntArray(Ljava/lang/String;)[I

    move-result-object v1

    .line 242
    if-eqz v1, :cond_44

    .line 243
    array-length v3, v1

    const/4 v4, 0x0

    :goto_2f
    if-ge v4, v3, :cond_44

    aget v5, v1, v4

    .line 244
    const v6, 0x20000005

    invoke-static {v5}, Landroid/hardware/security/keymint/KeyParameterValue;->digest(I)Landroid/hardware/security/keymint/KeyParameterValue;

    move-result-object v5

    invoke-static {v6, v5, p1}, Landroid/security/WukongFrameworkBridge;->newAuthorization(ILandroid/hardware/security/keymint/KeyParameterValue;I)Landroid/system/keystore2/Authorization;

    move-result-object v5

    invoke-virtual {v0, v5}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 243
    add-int/lit8 v4, v4, 0x1

    goto :goto_2f

    .line 247
    :cond_44
    const-string v1, "algorithm"

    invoke-virtual {p0, v1, v2}, Landroid/os/Bundle;->getInt(Ljava/lang/String;I)I

    move-result v1

    invoke-static {v1}, Landroid/hardware/security/keymint/KeyParameterValue;->algorithm(I)Landroid/hardware/security/keymint/KeyParameterValue;

    move-result-object v1

    const v3, 0x10000002

    invoke-static {v3, v1, p1}, Landroid/security/WukongFrameworkBridge;->newAuthorization(ILandroid/hardware/security/keymint/KeyParameterValue;I)Landroid/system/keystore2/Authorization;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 248
    const-string v1, "key_size"

    invoke-virtual {p0, v1, v2}, Landroid/os/Bundle;->getInt(Ljava/lang/String;I)I

    move-result v1

    invoke-static {v1}, Landroid/hardware/security/keymint/KeyParameterValue;->integer(I)Landroid/hardware/security/keymint/KeyParameterValue;

    move-result-object v1

    const v3, 0x30000003

    invoke-static {v3, v1, p1}, Landroid/security/WukongFrameworkBridge;->newAuthorization(ILandroid/hardware/security/keymint/KeyParameterValue;I)Landroid/system/keystore2/Authorization;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 249
    const-string v1, "ec_curve"

    invoke-virtual {p0, v1, v2}, Landroid/os/Bundle;->getInt(Ljava/lang/String;I)I

    move-result p0

    invoke-static {p0}, Landroid/hardware/security/keymint/KeyParameterValue;->ecCurve(I)Landroid/hardware/security/keymint/KeyParameterValue;

    move-result-object p0

    const v1, 0x1000000a

    invoke-static {v1, p0, p1}, Landroid/security/WukongFrameworkBridge;->newAuthorization(ILandroid/hardware/security/keymint/KeyParameterValue;I)Landroid/system/keystore2/Authorization;

    move-result-object p0

    invoke-virtual {v0, p0}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 250
    const p0, 0x700001f7

    const/4 v1, 0x1

    invoke-static {v1}, Landroid/hardware/security/keymint/KeyParameterValue;->boolValue(Z)Landroid/hardware/security/keymint/KeyParameterValue;

    move-result-object v1

    invoke-static {p0, v1, p1}, Landroid/security/WukongFrameworkBridge;->newAuthorization(ILandroid/hardware/security/keymint/KeyParameterValue;I)Landroid/system/keystore2/Authorization;

    move-result-object p0

    invoke-virtual {v0, p0}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 251
    new-array p0, v2, [Landroid/system/keystore2/Authorization;

    invoke-virtual {v0, p0}, Ljava/util/ArrayList;->toArray([Ljava/lang/Object;)[Ljava/lang/Object;

    move-result-object p0

    check-cast p0, [Landroid/system/keystore2/Authorization;

    return-object p0
.end method

.method private static buildMetadata(Landroid/system/keystore2/KeyDescriptor;Landroid/os/Bundle;)Landroid/system/keystore2/KeyMetadata;
    .registers 4

    .line 224
    new-instance v0, Landroid/system/keystore2/KeyMetadata;

    invoke-direct {v0}, Landroid/system/keystore2/KeyMetadata;-><init>()V

    .line 225
    invoke-static {p0}, Landroid/security/WukongFrameworkBridge;->cloneDescriptor(Landroid/system/keystore2/KeyDescriptor;)Landroid/system/keystore2/KeyDescriptor;

    move-result-object p0

    iput-object p0, v0, Landroid/system/keystore2/KeyMetadata;->key:Landroid/system/keystore2/KeyDescriptor;

    .line 226
    const-string p0, "security_level"

    const/4 v1, 0x1

    invoke-virtual {p1, p0, v1}, Landroid/os/Bundle;->getInt(Ljava/lang/String;I)I

    move-result p0

    iput p0, v0, Landroid/system/keystore2/KeyMetadata;->keySecurityLevel:I

    .line 227
    const-string p0, "certificate"

    invoke-virtual {p1, p0}, Landroid/os/Bundle;->getByteArray(Ljava/lang/String;)[B

    move-result-object p0

    iput-object p0, v0, Landroid/system/keystore2/KeyMetadata;->certificate:[B

    .line 228
    const-string p0, "certificate_chain"

    invoke-virtual {p1, p0}, Landroid/os/Bundle;->getByteArray(Ljava/lang/String;)[B

    move-result-object p0

    iput-object p0, v0, Landroid/system/keystore2/KeyMetadata;->certificateChain:[B

    .line 229
    iget p0, v0, Landroid/system/keystore2/KeyMetadata;->keySecurityLevel:I

    invoke-static {p1, p0}, Landroid/security/WukongFrameworkBridge;->buildAuthorizations(Landroid/os/Bundle;I)[Landroid/system/keystore2/Authorization;

    move-result-object p0

    iput-object p0, v0, Landroid/system/keystore2/KeyMetadata;->authorizations:[Landroid/system/keystore2/Authorization;

    .line 230
    return-object v0
.end method

.method private static callBridge(Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;
    .registers 16

    .line 288
    invoke-static {}, Landroid/security/WukongFrameworkBridge;->currentApplication()Landroid/app/Application;

    move-result-object v0

    .line 289
    const-string v1, "WukongFrameworkBridge"

    const/4 v2, 0x0

    if-nez v0, :cond_20

    .line 290
    new-instance p1, Ljava/lang/StringBuilder;

    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "No current application for method "

    invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object p1

    invoke-virtual {p1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-static {v1, p0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    .line 291
    return-object v2

    .line 293
    :cond_20
    invoke-static {}, Landroid/security/WukongFrameworkBridge;->currentActivityThread()Ljava/lang/Object;

    move-result-object v3

    .line 294
    if-nez v3, :cond_3d

    .line 295
    new-instance p1, Ljava/lang/StringBuilder;

    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "No current ActivityThread for method "

    invoke-virtual {p1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object p1

    invoke-virtual {p1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-static {v1, p0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    .line 296
    return-object v2

    .line 298
    :cond_3d
    nop

    .line 300
    :try_start_3e
    invoke-static {v3, v0}, Landroid/security/WukongFrameworkBridge;->acquireProvider(Ljava/lang/Object;Landroid/app/Application;)Ljava/lang/Object;

    move-result-object v0
    :try_end_42
    .catchall {:try_start_3e .. :try_end_42} :catchall_c7

    .line 301
    if-nez v0, :cond_63

    .line 302
    :try_start_44
    invoke-static {}, Landroid/security/WukongFrameworkBridge;->safePackageName()Ljava/lang/String;

    move-result-object p1

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "Failed to acquire provider for "

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object p1

    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    invoke-static {v1, p1}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_5e
    .catchall {:try_start_44 .. :try_end_5e} :catchall_c5

    .line 303
    nop

    .line 325
    invoke-static {v3, v0}, Landroid/security/WukongFrameworkBridge;->releaseProvider(Ljava/lang/Object;Ljava/lang/Object;)V

    .line 303
    return-object v2

    .line 305
    :cond_63
    :try_start_63
    const-string v4, "android.content.IContentProvider"

    invoke-static {v4}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v4

    const-string v5, "call"

    const/4 v6, 0x5

    new-array v7, v6, [Ljava/lang/Class;

    const-class v8, Landroid/content/AttributionSource;

    const/4 v9, 0x0

    aput-object v8, v7, v9

    const-class v8, Ljava/lang/String;

    const/4 v10, 0x1

    aput-object v8, v7, v10

    const-class v8, Ljava/lang/String;

    const/4 v11, 0x2

    aput-object v8, v7, v11

    const-class v8, Ljava/lang/String;

    const/4 v12, 0x3

    aput-object v8, v7, v12

    const/4 v13, 0x4

    const-class v8, Landroid/os/Bundle;

    aput-object v8, v7, v13

    invoke-virtual {v4, v5, v7}, Ljava/lang/Class;->getMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v4

    .line 311
    nop

    .line 313
    new-instance v5, Landroid/content/AttributionSource$Builder;

    invoke-static {}, Landroid/os/Process;->myUid()I

    move-result v7

    invoke-direct {v5, v7}, Landroid/content/AttributionSource$Builder;-><init>(I)V

    invoke-static {}, Landroid/security/WukongFrameworkBridge;->safePackageName()Ljava/lang/String;

    move-result-object v8

    invoke-virtual {v5, v8}, Landroid/content/AttributionSource$Builder;->setPackageName(Ljava/lang/String;)Landroid/content/AttributionSource$Builder;

    move-result-object v5

    invoke-virtual {v5}, Landroid/content/AttributionSource$Builder;->build()Landroid/content/AttributionSource;

    move-result-object v5

    new-array v6, v6, [Ljava/lang/Object;

    aput-object v5, v6, v9

    const-string v5, "io.github.beakthoven.wukong.manager.bridge"

    aput-object v5, v6, v10

    aput-object p0, v6, v11

    aput-object v2, v6, v12

    aput-object p1, v6, v13

    .line 311
    invoke-virtual {v4, v0, v6}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Landroid/os/Bundle;

    .line 317
    if-eqz p1, :cond_c0

    .line 318
    const-class v4, Landroid/security/WukongFrameworkBridge;

    invoke-virtual {v4}, Ljava/lang/Class;->getClassLoader()Ljava/lang/ClassLoader;

    move-result-object v4

    invoke-virtual {p1, v4}, Landroid/os/Bundle;->setClassLoader(Ljava/lang/ClassLoader;)V
    :try_end_c0
    .catchall {:try_start_63 .. :try_end_c0} :catchall_c5

    .line 320
    :cond_c0
    nop

    .line 325
    invoke-static {v3, v0}, Landroid/security/WukongFrameworkBridge;->releaseProvider(Ljava/lang/Object;Ljava/lang/Object;)V

    .line 320
    return-object p1

    .line 321
    :catchall_c5
    move-exception p1

    goto :goto_c9

    :catchall_c7
    move-exception p1

    move-object v0, v2

    .line 322
    :goto_c9
    :try_start_c9
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "Bridge call failed: "

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    invoke-static {v1, p0, p1}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I
    :try_end_df
    .catchall {:try_start_c9 .. :try_end_df} :catchall_e4

    .line 323
    nop

    .line 325
    invoke-static {v3, v0}, Landroid/security/WukongFrameworkBridge;->releaseProvider(Ljava/lang/Object;Ljava/lang/Object;)V

    .line 323
    return-object v2

    .line 325
    :catchall_e4
    move-exception p0

    invoke-static {v3, v0}, Landroid/security/WukongFrameworkBridge;->releaseProvider(Ljava/lang/Object;Ljava/lang/Object;)V

    .line 326
    throw p0
.end method

.method private static cloneDescriptor(Landroid/system/keystore2/KeyDescriptor;)Landroid/system/keystore2/KeyDescriptor;
    .registers 4

    .line 265
    new-instance v0, Landroid/system/keystore2/KeyDescriptor;

    invoke-direct {v0}, Landroid/system/keystore2/KeyDescriptor;-><init>()V

    .line 266
    if-eqz p0, :cond_17

    .line 267
    iget-object v1, p0, Landroid/system/keystore2/KeyDescriptor;->alias:Ljava/lang/String;

    iput-object v1, v0, Landroid/system/keystore2/KeyDescriptor;->alias:Ljava/lang/String;

    .line 268
    iget v1, p0, Landroid/system/keystore2/KeyDescriptor;->domain:I

    iput v1, v0, Landroid/system/keystore2/KeyDescriptor;->domain:I

    .line 269
    iget-wide v1, p0, Landroid/system/keystore2/KeyDescriptor;->nspace:J

    iput-wide v1, v0, Landroid/system/keystore2/KeyDescriptor;->nspace:J

    .line 270
    iget-object p0, p0, Landroid/system/keystore2/KeyDescriptor;->blob:[B

    iput-object p0, v0, Landroid/system/keystore2/KeyDescriptor;->blob:[B

    .line 272
    :cond_17
    return-object v0
.end method

.method private static currentActivityThread()Ljava/lang/Object;
    .registers 3

    .line 331
    const/4 v0, 0x0

    :try_start_1
    sget-object v1, Landroid/security/WukongFrameworkBridge;->CURRENT_THREAD:Ljava/lang/reflect/Method;

    if-eqz v1, :cond_f

    .line 332
    sget-object v1, Landroid/security/WukongFrameworkBridge;->CURRENT_THREAD:Ljava/lang/reflect/Method;

    const/4 v2, 0x0

    new-array v2, v2, [Ljava/lang/Object;

    invoke-virtual {v1, v0, v2}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0
    :try_end_e
    .catchall {:try_start_1 .. :try_end_e} :catchall_10

    return-object v0

    .line 335
    :cond_f
    goto :goto_11

    .line 334
    :catchall_10
    move-exception v1

    .line 336
    :goto_11
    return-object v0
.end method

.method private static currentApplication()Landroid/app/Application;
    .registers 3

    .line 417
    const/4 v0, 0x0

    :try_start_1
    sget-object v1, Landroid/security/WukongFrameworkBridge;->CURRENT_APP:Ljava/lang/reflect/Method;

    if-eqz v1, :cond_f

    sget-object v1, Landroid/security/WukongFrameworkBridge;->CURRENT_APP:Ljava/lang/reflect/Method;

    const/4 v2, 0x0

    new-array v2, v2, [Ljava/lang/Object;

    invoke-virtual {v1, v0, v2}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_10

    :cond_f
    move-object v1, v0

    .line 418
    :goto_10
    instance-of v2, v1, Landroid/app/Application;

    if-eqz v2, :cond_17

    check-cast v1, Landroid/app/Application;
    :try_end_16
    .catchall {:try_start_1 .. :try_end_16} :catchall_18

    move-object v0, v1

    :cond_17
    return-object v0

    .line 419
    :catchall_18
    move-exception v1

    .line 420
    return-object v0
.end method

.method private static currentPackageName()Ljava/lang/String;
    .registers 3

    .line 403
    const/4 v0, 0x0

    :try_start_1
    sget-object v1, Landroid/security/WukongFrameworkBridge;->CURRENT_PACKAGE:Ljava/lang/reflect/Method;

    if-eqz v1, :cond_15

    .line 404
    sget-object v1, Landroid/security/WukongFrameworkBridge;->CURRENT_PACKAGE:Ljava/lang/reflect/Method;

    const/4 v2, 0x0

    new-array v2, v2, [Ljava/lang/Object;

    invoke-virtual {v1, v0, v2}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    .line 405
    instance-of v2, v1, Ljava/lang/String;

    if-eqz v2, :cond_15

    .line 406
    check-cast v1, Ljava/lang/String;
    :try_end_14
    .catchall {:try_start_1 .. :try_end_14} :catchall_16

    return-object v1

    .line 410
    :cond_15
    goto :goto_17

    .line 409
    :catchall_16
    move-exception v1

    .line 411
    :goto_17
    invoke-static {}, Landroid/security/WukongFrameworkBridge;->currentApplication()Landroid/app/Application;

    move-result-object v1

    .line 412
    if-eqz v1, :cond_21

    invoke-virtual {v1}, Landroid/app/Application;->getPackageName()Ljava/lang/String;

    move-result-object v0

    :cond_21
    return-object v0
.end method

.method public static deleteKey(Landroid/system/keystore2/KeyDescriptor;)V
    .registers 3

    .line 137
    invoke-static {}, Landroid/security/WukongFrameworkBridge;->shouldBypass()Z

    move-result v0

    if-eqz v0, :cond_7

    .line 138
    return-void

    .line 140
    :cond_7
    new-instance v0, Landroid/os/Bundle;

    invoke-direct {v0}, Landroid/os/Bundle;-><init>()V

    .line 141
    const/4 v1, 0x0

    invoke-static {v0, p0, v1}, Landroid/security/WukongFrameworkBridge;->putDescriptor(Landroid/os/Bundle;Landroid/system/keystore2/KeyDescriptor;Z)V

    .line 142
    const-string p0, "delete_key"

    invoke-static {p0, v0}, Landroid/security/WukongFrameworkBridge;->callBridge(Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;

    .line 143
    return-void
.end method

.method private static getKeystoreBinder()Landroid/os/IBinder;
    .registers 7
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/Exception;
        }
    .end annotation

    .line 379
    const-string v0, "android.os.ServiceManager"

    invoke-static {v0}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v0

    .line 380
    sget-object v1, Landroid/security/WukongFrameworkBridge;->WAIT_FOR_SERVICE:Ljava/lang/reflect/Method;

    const-string v2, "android.system.keystore2.IKeystoreService/default"

    const/4 v3, 0x0

    const/4 v4, 0x0

    const/4 v5, 0x1

    if-eqz v1, :cond_1c

    .line 381
    sget-object v0, Landroid/security/WukongFrameworkBridge;->WAIT_FOR_SERVICE:Ljava/lang/reflect/Method;

    new-array v1, v5, [Ljava/lang/Object;

    aput-object v2, v1, v4

    invoke-virtual {v0, v3, v1}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/os/IBinder;

    return-object v0

    .line 383
    :cond_1c
    sget-object v1, Landroid/security/WukongFrameworkBridge;->GET_SERVICE:Ljava/lang/reflect/Method;

    if-eqz v1, :cond_2d

    .line 384
    sget-object v0, Landroid/security/WukongFrameworkBridge;->GET_SERVICE:Ljava/lang/reflect/Method;

    new-array v1, v5, [Ljava/lang/Object;

    aput-object v2, v1, v4

    invoke-virtual {v0, v3, v1}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/os/IBinder;

    return-object v0

    .line 386
    :cond_2d
    new-array v1, v5, [Ljava/lang/Class;

    const-class v6, Ljava/lang/String;

    aput-object v6, v1, v4

    const-string v6, "getService"

    invoke-virtual {v0, v6, v1}, Ljava/lang/Class;->getDeclaredMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v0

    .line 387
    invoke-virtual {v0, v5}, Ljava/lang/reflect/Method;->setAccessible(Z)V

    .line 388
    new-array v1, v5, [Ljava/lang/Object;

    aput-object v2, v1, v4

    invoke-virtual {v0, v3, v1}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/os/IBinder;

    return-object v0
.end method

.method private static getSecurityLevelInterface(I)Landroid/system/keystore2/IKeystoreSecurityLevel;
    .registers 3

    .line 367
    const/4 v0, 0x0

    :try_start_1
    invoke-static {}, Landroid/security/WukongFrameworkBridge;->getKeystoreBinder()Landroid/os/IBinder;

    move-result-object v1

    .line 368
    if-nez v1, :cond_8

    .line 369
    return-object v0

    .line 371
    :cond_8
    invoke-static {v1}, Landroid/system/keystore2/IKeystoreService$Stub;->asInterface(Landroid/os/IBinder;)Landroid/system/keystore2/IKeystoreService;

    move-result-object v1

    .line 372
    if-eqz v1, :cond_12

    invoke-interface {v1, p0}, Landroid/system/keystore2/IKeystoreService;->getSecurityLevel(I)Landroid/system/keystore2/IKeystoreSecurityLevel;

    move-result-object v0
    :try_end_12
    .catchall {:try_start_1 .. :try_end_12} :catchall_13

    :cond_12
    return-object v0

    .line 373
    :catchall_13
    move-exception p0

    .line 374
    return-object v0
.end method

.method private static getServiceMethod(Ljava/lang/String;)Ljava/lang/reflect/Method;
    .registers 6

    .line 436
    :try_start_0
    const-string v0, "android.os.ServiceManager"

    invoke-static {v0}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v0

    const/4 v1, 0x1

    new-array v2, v1, [Ljava/lang/Class;

    const-class v3, Ljava/lang/String;

    const/4 v4, 0x0

    aput-object v3, v2, v4

    invoke-virtual {v0, p0, v2}, Ljava/lang/Class;->getDeclaredMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object p0

    .line 437
    invoke-virtual {p0, v1}, Ljava/lang/reflect/Method;->setAccessible(Z)V
    :try_end_15
    .catchall {:try_start_0 .. :try_end_15} :catchall_16

    .line 438
    return-object p0

    .line 439
    :catchall_16
    move-exception p0

    .line 440
    const/4 p0, 0x0

    return-object p0
.end method

.method private static getStaticMethod(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/reflect/Method;
    .registers 3

    .line 426
    :try_start_0
    invoke-static {p0}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object p0

    const/4 v0, 0x0

    new-array v0, v0, [Ljava/lang/Class;

    invoke-virtual {p0, p1, v0}, Ljava/lang/Class;->getDeclaredMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object p0

    .line 427
    const/4 p1, 0x1

    invoke-virtual {p0, p1}, Ljava/lang/reflect/Method;->setAccessible(Z)V
    :try_end_f
    .catchall {:try_start_0 .. :try_end_f} :catchall_10

    .line 428
    return-object p0

    .line 429
    :catchall_10
    move-exception p0

    .line 430
    const/4 p0, 0x0

    return-object p0
.end method

.method public static maybeGenerateKey(Landroid/system/keystore2/KeyDescriptor;Landroid/system/keystore2/KeyDescriptor;Ljava/util/Collection;I[BI)Landroid/system/keystore2/KeyMetadata;
    .registers 10
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/system/keystore2/KeyDescriptor;",
            "Landroid/system/keystore2/KeyDescriptor;",
            "Ljava/util/Collection<",
            "Landroid/hardware/security/keymint/KeyParameter;",
            ">;I[BI)",
            "Landroid/system/keystore2/KeyMetadata;"
        }
    .end annotation

    .line 85
    invoke-static {}, Landroid/security/WukongFrameworkBridge;->shouldBypass()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_8

    .line 86
    return-object v1

    .line 88
    :cond_8
    new-instance v0, Landroid/os/Bundle;

    invoke-direct {v0}, Landroid/os/Bundle;-><init>()V

    .line 89
    const/4 v2, 0x0

    invoke-static {v0, p0, v2}, Landroid/security/WukongFrameworkBridge;->putDescriptor(Landroid/os/Bundle;Landroid/system/keystore2/KeyDescriptor;Z)V

    .line 90
    const/4 v3, 0x1

    invoke-static {v0, p1, v3}, Landroid/security/WukongFrameworkBridge;->putDescriptor(Landroid/os/Bundle;Landroid/system/keystore2/KeyDescriptor;Z)V

    .line 91
    const-string p1, "flags"

    invoke-virtual {v0, p1, p3}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    .line 92
    const-string p1, "entropy"

    invoke-virtual {v0, p1, p4}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 93
    const-string p1, "security_level"

    invoke-virtual {v0, p1, p5}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    .line 94
    invoke-static {v0, p2}, Landroid/security/WukongFrameworkBridge;->serializeArgs(Landroid/os/Bundle;Ljava/util/Collection;)V

    .line 95
    const-string p1, "generate_key"

    invoke-static {p1, v0}, Landroid/security/WukongFrameworkBridge;->callBridge(Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;

    move-result-object p1

    .line 96
    if-eqz p1, :cond_3d

    const-string p2, "intercepted"

    invoke-virtual {p1, p2, v2}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;Z)Z

    move-result p2

    if-nez p2, :cond_38

    goto :goto_3d

    .line 99
    :cond_38
    invoke-static {p0, p1}, Landroid/security/WukongFrameworkBridge;->buildMetadata(Landroid/system/keystore2/KeyDescriptor;Landroid/os/Bundle;)Landroid/system/keystore2/KeyMetadata;

    move-result-object p0

    return-object p0

    .line 97
    :cond_3d
    :goto_3d
    return-object v1
.end method

.method private static newAuthorization(ILandroid/hardware/security/keymint/KeyParameterValue;I)Landroid/system/keystore2/Authorization;
    .registers 5

    .line 255
    new-instance v0, Landroid/system/keystore2/Authorization;

    invoke-direct {v0}, Landroid/system/keystore2/Authorization;-><init>()V

    .line 256
    new-instance v1, Landroid/hardware/security/keymint/KeyParameter;

    invoke-direct {v1}, Landroid/hardware/security/keymint/KeyParameter;-><init>()V

    .line 257
    iput p0, v1, Landroid/hardware/security/keymint/KeyParameter;->tag:I

    .line 258
    iput-object p1, v1, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    .line 259
    iput-object v1, v0, Landroid/system/keystore2/Authorization;->keyParameter:Landroid/hardware/security/keymint/KeyParameter;

    .line 260
    iput p2, v0, Landroid/system/keystore2/Authorization;->securityLevel:I

    .line 261
    return-object v0
.end method

.method public static postGetKeyEntry(Landroid/system/keystore2/KeyDescriptor;Landroid/system/keystore2/KeyEntryResponse;)Landroid/system/keystore2/KeyEntryResponse;
    .registers 6

    .line 120
    if-eqz p1, :cond_51

    iget-object v0, p1, Landroid/system/keystore2/KeyEntryResponse;->metadata:Landroid/system/keystore2/KeyMetadata;

    if-eqz v0, :cond_51

    iget-object v0, p1, Landroid/system/keystore2/KeyEntryResponse;->metadata:Landroid/system/keystore2/KeyMetadata;

    iget-object v0, v0, Landroid/system/keystore2/KeyMetadata;->certificate:[B

    if-eqz v0, :cond_51

    invoke-static {}, Landroid/security/WukongFrameworkBridge;->shouldBypass()Z

    move-result v0

    if-eqz v0, :cond_13

    goto :goto_51

    .line 123
    :cond_13
    new-instance v0, Landroid/os/Bundle;

    invoke-direct {v0}, Landroid/os/Bundle;-><init>()V

    .line 124
    const/4 v1, 0x0

    invoke-static {v0, p0, v1}, Landroid/security/WukongFrameworkBridge;->putDescriptor(Landroid/os/Bundle;Landroid/system/keystore2/KeyDescriptor;Z)V

    .line 125
    iget-object p0, p1, Landroid/system/keystore2/KeyEntryResponse;->metadata:Landroid/system/keystore2/KeyMetadata;

    iget-object p0, p0, Landroid/system/keystore2/KeyMetadata;->certificate:[B

    const-string v2, "certificate"

    invoke-virtual {v0, v2, p0}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 126
    iget-object p0, p1, Landroid/system/keystore2/KeyEntryResponse;->metadata:Landroid/system/keystore2/KeyMetadata;

    iget-object p0, p0, Landroid/system/keystore2/KeyMetadata;->certificateChain:[B

    const-string v3, "certificate_chain"

    invoke-virtual {v0, v3, p0}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 127
    const-string p0, "post_get_key_entry"

    invoke-static {p0, v0}, Landroid/security/WukongFrameworkBridge;->callBridge(Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;

    move-result-object p0

    .line 128
    if-eqz p0, :cond_50

    const-string v0, "intercepted"

    invoke-virtual {p0, v0, v1}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;Z)Z

    move-result v0

    if-nez v0, :cond_3f

    goto :goto_50

    .line 131
    :cond_3f
    iget-object v0, p1, Landroid/system/keystore2/KeyEntryResponse;->metadata:Landroid/system/keystore2/KeyMetadata;

    invoke-virtual {p0, v2}, Landroid/os/Bundle;->getByteArray(Ljava/lang/String;)[B

    move-result-object v1

    iput-object v1, v0, Landroid/system/keystore2/KeyMetadata;->certificate:[B

    .line 132
    iget-object v0, p1, Landroid/system/keystore2/KeyEntryResponse;->metadata:Landroid/system/keystore2/KeyMetadata;

    invoke-virtual {p0, v3}, Landroid/os/Bundle;->getByteArray(Ljava/lang/String;)[B

    move-result-object p0

    iput-object p0, v0, Landroid/system/keystore2/KeyMetadata;->certificateChain:[B

    .line 133
    return-object p1

    .line 129
    :cond_50
    :goto_50
    return-object p1

    .line 121
    :cond_51
    :goto_51
    return-object p1
.end method

.method public static preGetKeyEntry(Landroid/system/keystore2/KeyDescriptor;)Landroid/system/keystore2/KeyEntryResponse;
    .registers 5

    .line 103
    invoke-static {}, Landroid/security/WukongFrameworkBridge;->shouldBypass()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_8

    .line 104
    return-object v1

    .line 106
    :cond_8
    new-instance v0, Landroid/os/Bundle;

    invoke-direct {v0}, Landroid/os/Bundle;-><init>()V

    .line 107
    const/4 v2, 0x0

    invoke-static {v0, p0, v2}, Landroid/security/WukongFrameworkBridge;->putDescriptor(Landroid/os/Bundle;Landroid/system/keystore2/KeyDescriptor;Z)V

    .line 108
    const-string v3, "pre_get_key_entry"

    invoke-static {v3, v0}, Landroid/security/WukongFrameworkBridge;->callBridge(Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;

    move-result-object v0

    .line 109
    if-eqz v0, :cond_36

    const-string v3, "intercepted"

    invoke-virtual {v0, v3, v2}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;Z)Z

    move-result v2

    if-nez v2, :cond_22

    goto :goto_36

    .line 112
    :cond_22
    invoke-static {p0, v0}, Landroid/security/WukongFrameworkBridge;->buildMetadata(Landroid/system/keystore2/KeyDescriptor;Landroid/os/Bundle;)Landroid/system/keystore2/KeyMetadata;

    move-result-object p0

    .line 113
    new-instance v0, Landroid/system/keystore2/KeyEntryResponse;

    invoke-direct {v0}, Landroid/system/keystore2/KeyEntryResponse;-><init>()V

    .line 114
    iput-object p0, v0, Landroid/system/keystore2/KeyEntryResponse;->metadata:Landroid/system/keystore2/KeyMetadata;

    .line 115
    iget p0, p0, Landroid/system/keystore2/KeyMetadata;->keySecurityLevel:I

    invoke-static {p0}, Landroid/security/WukongFrameworkBridge;->getSecurityLevelInterface(I)Landroid/system/keystore2/IKeystoreSecurityLevel;

    move-result-object p0

    iput-object p0, v0, Landroid/system/keystore2/KeyEntryResponse;->iSecurityLevel:Landroid/system/keystore2/IKeystoreSecurityLevel;

    .line 116
    return-object v0

    .line 110
    :cond_36
    :goto_36
    return-object v1
.end method

.method private static putDescriptor(Landroid/os/Bundle;Landroid/system/keystore2/KeyDescriptor;Z)V
    .registers 6

    .line 276
    if-nez p1, :cond_3

    .line 277
    return-void

    .line 279
    :cond_3
    if-eqz p2, :cond_8

    const-string v0, "attest_alias"

    goto :goto_a

    :cond_8
    const-string v0, "alias"

    .line 280
    :goto_a
    if-eqz p2, :cond_f

    const-string v1, "attest_domain"

    goto :goto_11

    :cond_f
    const-string v1, "domain"

    .line 281
    :goto_11
    if-eqz p2, :cond_16

    const-string p2, "attest_namespace"

    goto :goto_18

    :cond_16
    const-string p2, "namespace"

    .line 282
    :goto_18
    iget-object v2, p1, Landroid/system/keystore2/KeyDescriptor;->alias:Ljava/lang/String;

    invoke-virtual {p0, v0, v2}, Landroid/os/Bundle;->putString(Ljava/lang/String;Ljava/lang/String;)V

    .line 283
    iget v0, p1, Landroid/system/keystore2/KeyDescriptor;->domain:I

    invoke-virtual {p0, v1, v0}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    .line 284
    iget-wide v0, p1, Landroid/system/keystore2/KeyDescriptor;->nspace:J

    invoke-virtual {p0, p2, v0, v1}, Landroid/os/Bundle;->putLong(Ljava/lang/String;J)V

    .line 285
    return-void
.end method

.method private static releaseProvider(Ljava/lang/Object;Ljava/lang/Object;)V
    .registers 9

    .line 351
    if-eqz p0, :cond_31

    if-nez p1, :cond_5

    goto :goto_31

    .line 355
    :cond_5
    :try_start_5
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    const-string v1, "releaseProvider"

    const/4 v2, 0x2

    new-array v3, v2, [Ljava/lang/Class;

    const-string v4, "android.content.IContentProvider"

    .line 357
    invoke-static {v4}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v4

    const/4 v5, 0x0

    aput-object v4, v3, v5

    sget-object v4, Ljava/lang/Boolean;->TYPE:Ljava/lang/Class;

    const/4 v6, 0x1

    aput-object v4, v3, v6

    .line 355
    invoke-virtual {v0, v1, v3}, Ljava/lang/Class;->getMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v0

    .line 359
    invoke-virtual {v0, v6}, Ljava/lang/reflect/Method;->setAccessible(Z)V

    .line 360
    new-array v1, v2, [Ljava/lang/Object;

    aput-object p1, v1, v5

    sget-object p1, Ljava/lang/Boolean;->TRUE:Ljava/lang/Boolean;

    aput-object p1, v1, v6

    invoke-virtual {v0, p0, v1}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;
    :try_end_2e
    .catchall {:try_start_5 .. :try_end_2e} :catchall_2f

    .line 362
    goto :goto_30

    .line 361
    :catchall_2f
    move-exception p0

    .line 363
    :goto_30
    return-void

    .line 352
    :cond_31
    :goto_31
    return-void
.end method

.method private static safePackageName()Ljava/lang/String;
    .registers 1

    .line 397
    invoke-static {}, Landroid/security/WukongFrameworkBridge;->currentPackageName()Ljava/lang/String;

    move-result-object v0

    .line 398
    if-eqz v0, :cond_7

    goto :goto_9

    :cond_7
    const-string v0, "android"

    :goto_9
    return-object v0
.end method

.method private static serializeArgs(Landroid/os/Bundle;Ljava/util/Collection;)V
    .registers 7
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/os/Bundle;",
            "Ljava/util/Collection<",
            "Landroid/hardware/security/keymint/KeyParameter;",
            ">;)V"
        }
    .end annotation

    .line 146
    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    .line 147
    new-instance v1, Ljava/util/ArrayList;

    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V

    .line 148
    if-eqz p1, :cond_132

    .line 149
    invoke-interface {p1}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object p1

    :cond_10
    :goto_10
    invoke-interface {p1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_132

    invoke-interface {p1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Landroid/hardware/security/keymint/KeyParameter;

    .line 150
    if-eqz v2, :cond_10

    iget-object v3, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    if-nez v3, :cond_23

    .line 151
    goto :goto_10

    .line 153
    :cond_23
    iget v3, v2, Landroid/hardware/security/keymint/KeyParameter;->tag:I

    sparse-switch v3, :sswitch_data_146

    goto/16 :goto_130

    .line 176
    :sswitch_2a
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getDateTime()J

    move-result-wide v2

    const-string v4, "certificate_not_after"

    invoke-virtual {p0, v4, v2, v3}, Landroid/os/Bundle;->putLong(Ljava/lang/String;J)V

    .line 177
    goto/16 :goto_130

    .line 173
    :sswitch_37
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getDateTime()J

    move-result-wide v2

    const-string v4, "certificate_not_before"

    invoke-virtual {p0, v4, v2, v3}, Landroid/os/Bundle;->putLong(Ljava/lang/String;J)V

    .line 174
    goto/16 :goto_130

    .line 182
    :sswitch_44
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getLongInteger()J

    move-result-wide v2

    invoke-static {v2, v3}, Ljava/math/BigInteger;->valueOf(J)Ljava/math/BigInteger;

    move-result-object v2

    invoke-virtual {v2}, Ljava/math/BigInteger;->toByteArray()[B

    move-result-object v2

    const-string v3, "rsa_public_exponent"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 183
    goto/16 :goto_130

    .line 164
    :sswitch_59
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getInteger()I

    move-result v2

    const-string v3, "key_size"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    .line 165
    goto/16 :goto_130

    .line 158
    :sswitch_66
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getDigest()I

    move-result v2

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 159
    goto/16 :goto_130

    .line 155
    :sswitch_75
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getKeyPurpose()I

    move-result v2

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    invoke-virtual {v0, v2}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    .line 156
    goto/16 :goto_130

    .line 167
    :sswitch_84
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getEcCurve()I

    move-result v2

    const-string v3, "ec_curve"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    .line 168
    goto/16 :goto_130

    .line 161
    :sswitch_91
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getAlgorithm()I

    move-result v2

    const-string v3, "algorithm"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    .line 162
    goto/16 :goto_130

    .line 179
    :sswitch_9e
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getBlob()[B

    move-result-object v2

    const-string v3, "certificate_subject_der"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 180
    goto/16 :goto_130

    .line 206
    :sswitch_ab
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getBlob()[B

    move-result-object v2

    const-string v3, "second_imei"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 207
    goto/16 :goto_130

    .line 200
    :sswitch_b8
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getBlob()[B

    move-result-object v2

    const-string v3, "model"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 201
    goto :goto_130

    .line 197
    :sswitch_c4
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getBlob()[B

    move-result-object v2

    const-string v3, "manufacturer"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 198
    goto :goto_130

    .line 209
    :sswitch_d0
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getBlob()[B

    move-result-object v2

    const-string v3, "meid"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 210
    goto :goto_130

    .line 203
    :sswitch_dc
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getBlob()[B

    move-result-object v2

    const-string v3, "imei"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 204
    goto :goto_130

    .line 212
    :sswitch_e8
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getBlob()[B

    move-result-object v2

    const-string v3, "serial"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 213
    goto :goto_130

    .line 194
    :sswitch_f4
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getBlob()[B

    move-result-object v2

    const-string v3, "product"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 195
    goto :goto_130

    .line 191
    :sswitch_100
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getBlob()[B

    move-result-object v2

    const-string v3, "device"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 192
    goto :goto_130

    .line 188
    :sswitch_10c
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getBlob()[B

    move-result-object v2

    const-string v3, "brand"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 189
    goto :goto_130

    .line 185
    :sswitch_118
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getBlob()[B

    move-result-object v2

    const-string v3, "attestation_challenge"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 186
    goto :goto_130

    .line 170
    :sswitch_124
    iget-object v2, v2, Landroid/hardware/security/keymint/KeyParameter;->value:Landroid/hardware/security/keymint/KeyParameterValue;

    invoke-virtual {v2}, Landroid/hardware/security/keymint/KeyParameterValue;->getBlob()[B

    move-result-object v2

    const-string v3, "certificate_serial"

    invoke-virtual {p0, v3, v2}, Landroid/os/Bundle;->putByteArray(Ljava/lang/String;[B)V

    .line 171
    nop

    .line 217
    :goto_130
    goto/16 :goto_10

    .line 219
    :cond_132
    const-string p1, "purposes"

    invoke-static {v0}, Landroid/security/WukongFrameworkBridge;->toIntArray(Ljava/util/ArrayList;)[I

    move-result-object v0

    invoke-virtual {p0, p1, v0}, Landroid/os/Bundle;->putIntArray(Ljava/lang/String;[I)V

    .line 220
    const-string p1, "digests"

    invoke-static {v1}, Landroid/security/WukongFrameworkBridge;->toIntArray(Ljava/util/ArrayList;)[I

    move-result-object v0

    invoke-virtual {p0, p1, v0}, Landroid/os/Bundle;->putIntArray(Ljava/lang/String;[I)V

    .line 221
    return-void

    nop

    :sswitch_data_146
    .sparse-switch
        -0x7ffffc12 -> :sswitch_124
        -0x6ffffd3c -> :sswitch_118
        -0x6ffffd3a -> :sswitch_10c
        -0x6ffffd39 -> :sswitch_100
        -0x6ffffd38 -> :sswitch_f4
        -0x6ffffd37 -> :sswitch_e8
        -0x6ffffd36 -> :sswitch_dc
        -0x6ffffd35 -> :sswitch_d0
        -0x6ffffd34 -> :sswitch_c4
        -0x6ffffd33 -> :sswitch_b8
        -0x6ffffd2d -> :sswitch_ab
        -0x6ffffc11 -> :sswitch_9e
        0x10000002 -> :sswitch_91
        0x1000000a -> :sswitch_84
        0x20000001 -> :sswitch_75
        0x20000005 -> :sswitch_66
        0x30000003 -> :sswitch_59
        0x500000c8 -> :sswitch_44
        0x600003f0 -> :sswitch_37
        0x600003f1 -> :sswitch_2a
    .end sparse-switch
.end method

.method private static shouldBypass()Z
    .registers 2

    .line 392
    invoke-static {}, Landroid/security/WukongFrameworkBridge;->currentPackageName()Ljava/lang/String;

    move-result-object v0

    .line 393
    if-eqz v0, :cond_11

    const-string v1, "io.github.beakthoven.wukong.manager"

    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_f

    goto :goto_11

    :cond_f
    const/4 v0, 0x0

    goto :goto_12

    :cond_11
    :goto_11
    const/4 v0, 0x1

    :goto_12
    return v0
.end method

.method private static toIntArray(Ljava/util/ArrayList;)[I
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/ArrayList<",
            "Ljava/lang/Integer;",
            ">;)[I"
        }
    .end annotation

    .line 445
    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    move-result v0

    new-array v0, v0, [I

    .line 446
    const/4 v1, 0x0

    :goto_7
    invoke-virtual {p0}, Ljava/util/ArrayList;->size()I

    move-result v2

    if-ge v1, v2, :cond_1c

    .line 447
    invoke-virtual {p0, v1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Ljava/lang/Integer;

    invoke-virtual {v2}, Ljava/lang/Integer;->intValue()I

    move-result v2

    aput v2, v0, v1

    .line 446
    add-int/lit8 v1, v1, 0x1

    goto :goto_7

    .line 449
    :cond_1c
    return-object v0
.end method
