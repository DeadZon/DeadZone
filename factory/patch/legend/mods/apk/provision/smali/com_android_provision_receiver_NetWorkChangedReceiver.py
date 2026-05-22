TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/receiver/NetWorkChangedReceiver.smali'
CLASS_FALLBACK_NAMES = ['NetWorkChangedReceiver.smali']
CLASS_ANCHORS = ['.super Landroid/content/BroadcastReceiver;']

PATCHES = [
    {
        'id': 'com_android_provision_receiver_NetWorkChangedReceiver__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/android/provision/receiver/NetWorkChangedReceiver;
.super Landroid/content/BroadcastReceiver;


# direct methods
.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V

    return-void
.end method


# virtual methods
.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    .registers 5

    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    move-result-object p0

    const-string p2, "android.net.conn.CONNECTIVITY_CHANGE"

    invoke-virtual {p0, p2}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p0

    if-eqz p0, :cond_3

    invoke-static {p1}, Lcom/android/provision/Utils;->networkAvailable(Landroid/content/Context;)Z

    move-result p0

    if-eqz p0, :cond_3

    invoke-static {p1}, Lcom/android/provision/Utils;->isClauseAgreed(Landroid/content/Context;)Z

    move-result p0

    if-eqz p0, :cond_3

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getLastLocale()Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p2

    if-nez p2, :cond_3

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getRecommendedOperation()I

    move-result p2

    const/4 v0, -0x1

    if-ne p2, v0, :cond_0

    invoke-static {p0, p1}, Lcom/android/provision/utils/RequestUtils;->prepareAndStartRecommendedRequest(Ljava/lang/String;Landroid/content/Context;)V

    :cond_0
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getPreinstallStatusCode()I

    move-result p2

    if-ne p2, v0, :cond_1

    invoke-static {p1}, Lcom/android/provision/utils/RequestUtils;->prepareAndStartPreinstallRequest(Landroid/content/Context;)V

    :cond_1
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_3

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getCarouselEnable()I

    move-result p1

    if-ne p1, v0, :cond_2

    new-instance p1, Lcom/android/provision/utils/CloudConfigRequest;

    invoke-direct {p1}, Lcom/android/provision/utils/CloudConfigRequest;-><init>()V

    const-string p2, "carousel_switch"

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-virtual {p1, p0, p2, v1}, Lcom/android/provision/utils/CloudConfigRequest;->cloudConfigRequest(Ljava/lang/String;Ljava/lang/String;Landroid/content/Context;)V

    :cond_2
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getDrawerEnable()I

    move-result p1

    if-ne p1, v0, :cond_3

    new-instance p1, Lcom/android/provision/utils/CloudConfigRequest;

    invoke-direct {p1}, Lcom/android/provision/utils/CloudConfigRequest;-><init>()V

    invoke-static {v0}, Lcom/android/provision/DefaultPreferenceHelper;->setDrawerEnable(I)V

    const-string p2, "drawer_switch"

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {p1, p0, p2, v0}, Lcom/android/provision/utils/CloudConfigRequest;->cloudConfigRequest(Ljava/lang/String;Ljava/lang/String;Landroid/content/Context;)V

    :cond_3
    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
