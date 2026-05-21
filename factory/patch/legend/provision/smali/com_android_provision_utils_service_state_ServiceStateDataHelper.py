TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/utils/service_state/ServiceStateDataHelper.smali'
CLASS_FALLBACK_NAMES = ['ServiceStateDataHelper.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final ANDROID_SYSTEM_VERSION_NUMBER:I = 0xb', '.field public static final AUTHORIZATION_STATUS_HOLD_TIME:I = 0x5', '.field public static final PRIVACY_CONTENT_TYPE:Ljava/lang/String; = "content"', '.field public static final PRIVACY_FASTAPP_TYPE:Ljava/lang/String; = "fast_application"', '.field public static final PRIVACY_GAME_TYPE:Ljava/lang/String; = "game"']

PATCHES = [
    {
        'id': 'com_android_provision_utils_service_state_ServiceStateDataHelper__buildTermsItems',
        'method': '.method private buildTermsItems()Lcom/android/provision/utils/service_state/ServiceItem;',
        'method_name': 'buildTermsItems',
        'method_anchors': ['new-instance v0, Lcom/android/provision/utils/service_state/ServiceItem;', 'invoke-direct {v0}, Lcom/android/provision/utils/service_state/ServiceItem;-><init>()V', 'iget-object p0, p0, Lcom/android/provision/utils/service_state/ServiceStateDataHelper;->mContext:Landroid/content/Context;', 'sget v1, Lcom/android/provision/R$string;->terms_of_label_separator:I', 'invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;', 'sget v2, Lcom/android/provision/R$string;->terms_of_use_label_use_network_china:I', 'invoke-virtual {p0, v2}, Landroid/content/Context;->getString(I)Ljava/lang/String;', 'new-instance v3, Ljava/lang/StringBuilder;'],
        'type': 'policy_skip',
        'search': """.method private buildTermsItems()Lcom/android/provision/utils/service_state/ServiceItem;
    .registers 8

    new-instance v0, Lcom/android/provision/utils/service_state/ServiceItem;

    invoke-direct {v0}, Lcom/android/provision/utils/service_state/ServiceItem;-><init>()V

    iget-object p0, p0, Lcom/android/provision/utils/service_state/ServiceStateDataHelper;->mContext:Landroid/content/Context;

    sget v1, Lcom/android/provision/R$string;->terms_of_label_separator:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    sget v2, Lcom/android/provision/R$string;->terms_of_use_label_use_network_china:I

    invoke-virtual {p0, v2}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v2

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    sget-boolean v4, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v4, :cond_0

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_use_location_and_network_global:I

    invoke-virtual {p0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v3, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_0
    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_use_network_china_append:I

    invoke-virtual {p0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v3, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :goto_0
    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportCloudService(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_1

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_cloud:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1
    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_remote_provisioner:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportCloudBackup(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_2

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_back:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_2
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportFindDevice(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_3

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_finddevice:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_3
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportSecureElementApplication(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_4

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_secure:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_4
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportHome(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_5

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_home:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_5
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportGameCenterService(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_6

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_game:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_6
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportTranslationService(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_7

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_translation:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_7
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportXmsf(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_8

    sget v6, Lcom/android/provision/R$string;->terms_of_use_lable_xmsf:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_8
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportMiuiDaemon(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_9

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_miuiDaemon:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_9
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportMSA(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_a

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_MSA:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_a
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportSimActivateService(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_b

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_simcard:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_b
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportAIAssistant(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_c

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_ai_assistant:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_c
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportPowerKeeper(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_d

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_power_performance:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_d
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportPowerchecker(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_e

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_power_detection:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_e
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportOs(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_f

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_os:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_f
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportJoyose(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_10

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_joyose:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_10
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportWallpaper(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_11

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_wallpaper:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_11
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportHTMLViewer(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_12

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_htmlViewer:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_12
    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_landscape:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-nez v4, :cond_1b

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_system_quality_monitoring:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_webview:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Lcom/android/provision/Utils;->isSupportIntentFilterVerificationService()Z

    move-result v4

    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportUpdater(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_13

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_updater:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-eqz v4, :cond_13

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_13
    if-eqz v4, :cond_14

    sget v4, Lcom/android/provision/R$string;->intent_filter_verification_service:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_14
    sget v4, Lcom/android/provision/R$string;->fidio_declare_permissions:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Lcom/android/provision/cust/buz/chinamobile/ChinaMobileBuzSupporter;->getInstance()Lcom/android/provision/cust/buz/chinamobile/ChinaMobileBuzSupporter;

    move-result-object v4

    invoke-virtual {v4}, Lcom/android/provision/cust/buz/chinamobile/ChinaMobileBuzSupporter;->isFeatureAvailable()Z

    move-result v4

    if-eqz v4, :cond_15

    sget v4, Lcom/android/provision/R$string;->china_mobile_components_manager_app:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_15
    sget v4, Lcom/android/provision/R$string;->image_brain_configuration_service:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v4, Lcom/android/provision/R$string;->power_consumption_statistics_service:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v4, Lcom/android/provision/R$string;->terms_of_label_period:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v4, Lcom/android/provision/R$string;->agreement_declare_use_network_and_location_china:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/4 v4, 0x0

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->length()I

    move-result v6

    invoke-virtual {v5, v4, v6}, Ljava/lang/StringBuilder;->delete(II)Ljava/lang/StringBuilder;

    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportSmartCard(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_16

    sget v4, Lcom/android/provision/R$string;->terms_of_use_lable_smart_cards:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_16
    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_unionplay_security:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportRMS(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_17

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_RMS:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_17
    invoke-static {}, Lcom/android/provision/Utils;->hasGmscore()Z

    move-result v4

    if-eqz v4, :cond_18

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_config_updater:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_18
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportSmartService(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_19

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_smart_service:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_19
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportCommService(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_1a

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_communication_service:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1a
    sget v1, Lcom/android/provision/R$string;->terms_of_use_label_miuisdk:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/CharSequence;)Ljava/lang/StringBuilder;

    goto :goto_1

    :cond_1b
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportQuickApp(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_1c

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_quickapp:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1c
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportAppVault(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_1d

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_app_vault:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1d
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportInfoAssistant(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_1e

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_info_assistant:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1e
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportStatistics(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_1f

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_statistics:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1f
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportMAB(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_20

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_mab:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_20
    sget v4, Lcom/android/provision/R$string;->terms_of_use_lable_gms:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportSmartCard(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_21

    sget v4, Lcom/android/provision/R$string;->terms_of_use_lable_smart_cards:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_21
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportUpdater(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_22

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_updater:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_22
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportMiAccount(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_23

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_mi_account:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_23
    invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v4

    if-eqz v4, :cond_24

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_label_communication_service:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_24
    sget v1, Lcom/android/provision/R$string;->terms_of_label_space:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :goto_1
    sget v1, Lcom/android/provision/R$string;->terms_of_label_period:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getImmId()Ljava/lang/String;

    move-result-object v3

    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v4

    if-nez v4, :cond_27

    const-string v4, "com.facemoji.lite.xiaomi/com.baidu.simeji.SimejiIME"

    invoke-static {v3, v4}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v4

    const-string v5, "\n"

    const-string v6, "\\n"

    if-eqz v4, :cond_25

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_lable_default_input_method_facemoji:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1, v6, v5}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    goto :goto_2

    :cond_25
    const-string v4, "com.mint.keyboard/.services.MintKeyboard"

    invoke-static {v3, v4}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v4

    if-eqz v4, :cond_26

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_lable_default_input_method_mint:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1, v6, v5}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    goto :goto_2

    :cond_26
    const-string v4, "com.kikaoem.xiaomi.qisiemoji.inputmethod/com.android.inputmethod.latin.LatinIME"

    invoke-static {v3, v4}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v3

    if-eqz v3, :cond_27

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_lable_default_input_method_kika:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1, v6, v5}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    :cond_27
    :goto_2
    sget v3, Lcom/android/provision/fragment/TermsAndStatementFragment;->TYPE_TERMS_ITEM:I

    iput v3, v0, Lcom/android/provision/utils/service_state/ServiceItem;->type:I

    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget v3, Lcom/android/provision/R$string;->terms_of_use:I

    invoke-virtual {p0, v3}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object p0

    iput-object p0, v0, Lcom/android/provision/utils/service_state/ServiceItem;->termsName:Ljava/lang/String;

    iput-object v2, v0, Lcom/android/provision/utils/service_state/ServiceItem;->termsTitle:Ljava/lang/String;

    iput-object v1, v0, Lcom/android/provision/utils/service_state/ServiceItem;->termsDescription:Ljava/lang/String;

    return-object v0
.end method""",
        'replacement': """.method private buildTermsItems()Lcom/android/provision/utils/service_state/ServiceItem;
    .registers 8

    new-instance v0, Lcom/android/provision/utils/service_state/ServiceItem;

    invoke-direct {v0}, Lcom/android/provision/utils/service_state/ServiceItem;-><init>()V

    iget-object p0, p0, Lcom/android/provision/utils/service_state/ServiceStateDataHelper;->mContext:Landroid/content/Context;

    sget v1, Lcom/android/provision/R$string;->terms_of_label_separator:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    sget v2, Lcom/android/provision/R$string;->terms_of_use_label_use_network_china:I

    invoke-virtual {p0, v2}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v2

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    sget-boolean v4, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v4, :cond_0

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_use_location_and_network_global:I

    invoke-virtual {p0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v3, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_0
    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_use_network_china_append:I

    invoke-virtual {p0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v3, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :goto_0
    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportCloudService(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_1

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_cloud:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1
    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_remote_provisioner:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportCloudBackup(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_2

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_back:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_2
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportFindDevice(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_3

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_finddevice:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_3
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportSecureElementApplication(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_4

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_secure:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_4
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportHome(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_5

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_home:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_5
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportGameCenterService(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_6

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_game:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_6
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportTranslationService(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_7

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_translation:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_7
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportXmsf(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_8

    sget v6, Lcom/android/provision/R$string;->terms_of_use_lable_xmsf:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_8
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportMiuiDaemon(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_9

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_miuiDaemon:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_9
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportMSA(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_a

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_MSA:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_a
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportSimActivateService(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_b

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_simcard:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_b
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportAIAssistant(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_c

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_ai_assistant:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_c
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportPowerKeeper(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_d

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_power_performance:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_d
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportPowerchecker(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_e

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_power_detection:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_e
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportOs(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_f

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_os:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_f
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportJoyose(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_10

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_joyose:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_10
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportWallpaper(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_11

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_wallpaper:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_11
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportHTMLViewer(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_12

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_htmlViewer:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_12
    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_landscape:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-nez v4, :cond_1b

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_system_quality_monitoring:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_webview:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Lcom/android/provision/Utils;->isSupportIntentFilterVerificationService()Z

    move-result v4

    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportUpdater(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_13

    sget v6, Lcom/android/provision/R$string;->terms_of_use_label_updater:I

    invoke-virtual {p0, v6}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-eqz v4, :cond_13

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_13
    if-eqz v4, :cond_14

    sget v4, Lcom/android/provision/R$string;->intent_filter_verification_service:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_14
    sget v4, Lcom/android/provision/R$string;->fidio_declare_permissions:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Lcom/android/provision/cust/buz/chinamobile/ChinaMobileBuzSupporter;->getInstance()Lcom/android/provision/cust/buz/chinamobile/ChinaMobileBuzSupporter;

    move-result-object v4

    invoke-virtual {v4}, Lcom/android/provision/cust/buz/chinamobile/ChinaMobileBuzSupporter;->isFeatureAvailable()Z

    move-result v4

    if-eqz v4, :cond_15

    sget v4, Lcom/android/provision/R$string;->china_mobile_components_manager_app:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_15
    sget v4, Lcom/android/provision/R$string;->image_brain_configuration_service:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v4, Lcom/android/provision/R$string;->power_consumption_statistics_service:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v4, Lcom/android/provision/R$string;->terms_of_label_period:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v4, Lcom/android/provision/R$string;->agreement_declare_use_network_and_location_china:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/4 v4, 0x0

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->length()I

    move-result v6

    invoke-virtual {v5, v4, v6}, Ljava/lang/StringBuilder;->delete(II)Ljava/lang/StringBuilder;

    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportSmartCard(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_16

    sget v4, Lcom/android/provision/R$string;->terms_of_use_lable_smart_cards:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_16
    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_unionplay_security:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportRMS(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_17

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_RMS:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_17
    invoke-static {}, Lcom/android/provision/Utils;->hasGmscore()Z

    move-result v4

    if-eqz v4, :cond_18

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_config_updater:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_18
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportSmartService(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_19

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_smart_service:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_19
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportCommService(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_1a

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_communication_service:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1a
    sget v1, Lcom/android/provision/R$string;->terms_of_use_label_miuisdk:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/CharSequence;)Ljava/lang/StringBuilder;

    goto :goto_1

    :cond_1b
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportQuickApp(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_1c

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_quickapp:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1c
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportAppVault(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_1d

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_app_vault:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1d
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportInfoAssistant(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_1e

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_info_assistant:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1e
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportStatistics(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_1f

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_statistics:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1f
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportMAB(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_20

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_mab:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_20
    sget v4, Lcom/android/provision/R$string;->terms_of_use_lable_gms:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportSmartCard(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_21

    sget v4, Lcom/android/provision/R$string;->terms_of_use_lable_smart_cards:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_21
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportUpdater(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_22

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_updater:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_22
    invoke-static {p0}, Lcom/android/provision/Utils;->isSupportMiAccount(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_23

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_mi_account:I

    invoke-virtual {p0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_23
    invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v4

    if-eqz v4, :cond_24

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_label_communication_service:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v5, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_24
    sget v1, Lcom/android/provision/R$string;->terms_of_label_space:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :goto_1
    sget v1, Lcom/android/provision/R$string;->terms_of_label_period:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getImmId()Ljava/lang/String;

    move-result-object v3

    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v4

    if-nez v4, :cond_27

    const-string v4, "com.facemoji.lite.xiaomi/com.baidu.simeji.SimejiIME"

    invoke-static {v3, v4}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v4

    const-string v5, "\n"

    const-string v6, "\\n"

    if-eqz v4, :cond_25

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_lable_default_input_method_facemoji:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1, v6, v5}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    goto :goto_2

    :cond_25
    const-string v4, "com.mint.keyboard/.services.MintKeyboard"

    invoke-static {v3, v4}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v4

    if-eqz v4, :cond_26

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_lable_default_input_method_mint:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1, v6, v5}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    goto :goto_2

    :cond_26
    const-string v4, "com.kikaoem.xiaomi.qisiemoji.inputmethod/com.android.inputmethod.latin.LatinIME"

    invoke-static {v3, v4}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v3

    if-eqz v3, :cond_27

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_lable_default_input_method_kika:I

    invoke-virtual {p0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1, v6, v5}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    :cond_27
    :goto_2
    sget v3, Lcom/android/provision/fragment/TermsAndStatementFragment;->TYPE_TERMS_ITEM:I

    iput v3, v0, Lcom/android/provision/utils/service_state/ServiceItem;->type:I

    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget v3, Lcom/android/provision/R$string;->terms_of_use:I

    invoke-virtual {p0, v3}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object p0

    iput-object p0, v0, Lcom/android/provision/utils/service_state/ServiceItem;->termsName:Ljava/lang/String;

    iput-object v2, v0, Lcom/android/provision/utils/service_state/ServiceItem;->termsTitle:Ljava/lang/String;

    iput-object v1, v0, Lcom/android/provision/utils/service_state/ServiceItem;->termsDescription:Ljava/lang/String;

    return-object v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
