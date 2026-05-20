"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/sim/SimSlotIndexHelper.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/sim/SimSlotIndexHelper.smali'
CLASS_FALLBACK_NAMES = ['SimSlotIndexHelper.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_sim_SimSlotIndexHelper',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;\n.super Ljava/lang/Object;\n\n\n# static fields\n.field private static instance:Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;\n\n\n# instance fields\n.field private final list:Ljava/util/List;\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "Ljava/util/List<",\n            "Landroid/telephony/SubscriptionInfo;",\n            ">;"\n        }\n    .end annotation\n.end field\n\n\n# direct methods\n.method private constructor <init>(Landroid/content/Context;)V\n    .registers 4\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    const-class v0, Landroid/telephony/SubscriptionManager;\n\n    invoke-virtual {p1, v0}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Landroid/telephony/SubscriptionManager;\n\n    invoke-virtual {v0}, Landroid/telephony/SubscriptionManager;->getActiveSubscriptionInfoList()Ljava/util/List;\n\n    move-result-object v1\n\n    iput-object v1, p0, Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;->list:Ljava/util/List;\n\n    return-void\n.end method\n\n.method public static getInstance(Landroid/content/Context;)Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;\n    .registers 3\n\n    const-class v0, Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;\n\n    monitor-enter v0\n\n    :try_start_0\n    sget-object v1, Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;->instance:Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;\n\n    if-nez v1, :cond_0\n\n    new-instance v1, Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;\n\n    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;-><init>(Landroid/content/Context;)V\n\n    sput-object v1, Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;->instance:Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;\n\n    :cond_0\n    sget-object v1, Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;->instance:Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;\n\n    monitor-exit v0\n\n    return-object v1\n\n    :catchall_0\n    move-exception v1\n\n    monitor-exit v0\n    :try_end_0\n    .catchall {:try_start_0 .. :try_end_0} :catchall_0\n\n    throw v1\n.end method\n\n\n# virtual methods\n.method public getSlot(I)I\n    .registers 6\n\n    const/4 v0, 0x0\n\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/sim/SimSlotIndexHelper;->list:Ljava/util/List;\n\n    invoke-interface {v1}, Ljava/util/List;->iterator()Ljava/util/Iterator;\n\n    move-result-object v1\n\n    :goto_0\n    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z\n\n    move-result v2\n\n    if-eqz v2, :cond_1\n\n    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;\n\n    move-result-object v2\n\n    check-cast v2, Landroid/telephony/SubscriptionInfo;\n\n    invoke-virtual {v2}, Landroid/telephony/SubscriptionInfo;->getSubscriptionId()I\n\n    move-result v3\n\n    if-ne p1, v3, :cond_0\n\n    invoke-virtual {v2}, Landroid/telephony/SubscriptionInfo;->getSimSlotIndex()I\n\n    move-result v1\n\n    return v1\n\n    :cond_0\n    goto :goto_0\n\n    :cond_1\n    return v0\n.end method\n\n.method public setSubs(Ljava/util/List;)V\n    .registers 2\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "(",\n            "Ljava/util/List<",\n            "Landroid/telephony/SubscriptionInfo;",\n            ">;)V"\n        }\n    .end annotation\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
