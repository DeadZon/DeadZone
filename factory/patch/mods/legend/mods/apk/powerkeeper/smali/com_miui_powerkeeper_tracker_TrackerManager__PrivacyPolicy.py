TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'com/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy.smali'
CLASS_FALLBACK_NAMES = ['TrackerManager$PrivacyPolicy.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_miui_powerkeeper_tracker_TrackerManager__PrivacyPolicy__updateLicense',
        'method': '.method public updateLicense()V',
        'method_name': 'updateLicense',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mRegion:Ljava/lang/String;', 'const-string v3, "RU"', 'invoke-virtual {v0, v3}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z', 'if-nez v0, :cond_0', 'iput-boolean v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mInternational:Z', 'iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mContext:Landroid/content/Context;'],
        'type': 'method_replace',
        'search': """.method public updateLicense()V
    .registers 5

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    const/4 v2, 0x1

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mRegion:Ljava/lang/String;

    const-string v3, "RU"

    invoke-virtual {v0, v3}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_0

    move v0, v2

    goto :goto_0

    :cond_0
    move v0, v1

    :goto_0
    iput-boolean v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mInternational:Z

    iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lcom/miui/powerkeeper/utils/Utils;->isUserExperienceAndPrivacyAllowed(Landroid/content/Context;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mAllowTrack:Z

    iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lcom/miui/powerkeeper/utils/Utils;->isPrivacyEnable(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_1

    invoke-static {}, Lcom/miui/powerkeeper/utils/Utils;->isInEURegion()Z

    move-result v0

    if-eqz v0, :cond_1

    move v1, v2

    :cond_1
    iput-boolean v1, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mPubSubDisable:Z

    iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lcom/miui/powerkeeper/utils/Utils;->isCloudControlAllowed(Landroid/content/Context;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mIsCloudControlAllow:Z

    iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lcom/miui/powerkeeper/utils/Utils;->isUserAllowed(Landroid/content/Context;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mIsUserAllow:Z

    iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lcom/miui/powerkeeper/utils/Utils;->isPrivacyEnable(Landroid/content/Context;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mIsPrivacyEnable:Z

    return-void
.end method""",
        'replacement': """.method public updateLicense()V
    .registers 5

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    const/4 v1, 0x0

    const/4 v2, 0x1

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mRegion:Ljava/lang/String;

    const-string v3, "RU"

    invoke-virtual {v0, v3}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_0

    move v0, v2

    goto :goto_0

    :cond_0
    move v0, v1

    :goto_0
    iput-boolean v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mInternational:Z

    iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lcom/miui/powerkeeper/utils/Utils;->isUserExperienceAndPrivacyAllowed(Landroid/content/Context;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mAllowTrack:Z

    iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lcom/miui/powerkeeper/utils/Utils;->isPrivacyEnable(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_1

    invoke-static {}, Lcom/miui/powerkeeper/utils/Utils;->isInEURegion()Z

    move-result v0

    if-eqz v0, :cond_1

    move v1, v2

    :cond_1
    iput-boolean v1, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mPubSubDisable:Z

    iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lcom/miui/powerkeeper/utils/Utils;->isCloudControlAllowed(Landroid/content/Context;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mIsCloudControlAllow:Z

    iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lcom/miui/powerkeeper/utils/Utils;->isUserAllowed(Landroid/content/Context;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mIsUserAllow:Z

    iget-object v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mContext:Landroid/content/Context;

    invoke-static {v0}, Lcom/miui/powerkeeper/utils/Utils;->isPrivacyEnable(Landroid/content/Context;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/miui/powerkeeper/tracker/TrackerManager$PrivacyPolicy;->mIsPrivacyEnable:Z

    return-void
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
