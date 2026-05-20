"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator.smali
Patches      : 6
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator.smali'
CLASS_FALLBACK_NAMES = ['RowAppearanceCoordinator.smali']
CLASS_ANCHORS        = ['invoke-direct {p0}, Ljava/lang/Object;-><init>()V', 'iput-object p1, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mContext:Landroid/content/Context;', 'iput-object p2, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mAssistantFeedbackController:Lcom/android/systemui/statusbar/notification/AssistantFeedbackController;', 'iput-object p3, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mSectionStyleProvider:Lcom/android/systemui/statusbar/notification/collection/provider/SectionStyleProvider;', 'invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;']

PATCHES = [
    {
        'id':             'p0000__init_',
        'type':           'method_replace',
        'method':         '.method public constructor <init>(Landroid/content/Context;Lcom/android/systemui/statusbar/notification/AssistantFeedbackController;Lcom/android/systemui/statusbar/notification/collection/provider/SectionStyleProvider;)V',
        'method_name':    '<init>',
        'method_anchors': ['invoke-direct {p0}, Ljava/lang/Object;-><init>()V', 'iput-object p1, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mContext:Landroid/content/Context;', 'iput-object p2, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mAssistantFeedbackController:Lcom/android/systemui/statusbar/notification/AssistantFeedbackController;'],
        'search':         '.method public constructor <init>(Landroid/content/Context;Lcom/android/systemui/statusbar/notification/AssistantFeedbackController;Lcom/android/systemui/statusbar/notification/collection/provider/SectionStyleProvider;)V\n    .registers 4\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    iput-object p2, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mAssistantFeedbackController:Lcom/android/systemui/statusbar/notification/AssistantFeedbackController;\n\n    iput-object p3, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mSectionStyleProvider:Lcom/android/systemui/statusbar/notification/collection/provider/SectionStyleProvider;\n\n    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;\n\n    move-result-object p2\n\n    const p3, 0x7f050011\n\n    invoke-virtual {p2, p3}, Landroid/content/res/Resources;->getBoolean(I)Z\n\n    move-result p2\n\n    iput-boolean p2, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mAlwaysExpandNonGroupedNotification:Z\n\n    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;\n\n    move-result-object p1\n\n    const p2, 0x7f050013\n\n    invoke-virtual {p1, p2}, Landroid/content/res/Resources;->getBoolean(I)Z\n\n    move-result p1\n\n    iput-boolean p1, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mAutoExpandFirstNotification:Z\n\n    return-void\n.end method\n',
        'replacement':    '.method public constructor <init>(Landroid/content/Context;Lcom/android/systemui/statusbar/notification/AssistantFeedbackController;Lcom/android/systemui/statusbar/notification/collection/provider/SectionStyleProvider;)V\n    .registers 4\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mContext:Landroid/content/Context;\n\n    iput-object p2, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mAssistantFeedbackController:Lcom/android/systemui/statusbar/notification/AssistantFeedbackController;\n\n    iput-object p3, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mSectionStyleProvider:Lcom/android/systemui/statusbar/notification/collection/provider/SectionStyleProvider;\n\n    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;\n\n    move-result-object p2\n\n    const p3, 0x7f050011\n\n    invoke-virtual {p2, p3}, Landroid/content/res/Resources;->getBoolean(I)Z\n\n    move-result p2\n\n    iput-boolean p2, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mAlwaysExpandNonGroupedNotification:Z\n\n    new-instance p2, Landroid/os/Handler;\n\n    invoke-virtual {p1}, Landroid/content/Context;->getMainLooper()Landroid/os/Looper;\n\n    move-result-object p1\n\n    invoke-direct {p2, p1}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V\n\n    iput-object p2, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mHandler:Landroid/os/Handler;\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->setupExpandTopNotificationObserver()V\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
    {
        'id':             'p0001_setupExpandTopNotificationObserver',
        'type':           'method_add',
        'method':         '.method public final setupExpandTopNotificationObserver()V',
        'method_name':    'setupExpandTopNotificationObserver',
        'method_anchors': ['iget-object v1, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mHandler:Landroid/os/Handler;', 'invoke-direct {v0, p0, v1}, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator$attach$3;-><init>(Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;Landroid/os/Handler;)V', 'iget-object v1, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mContext:Landroid/content/Context;'],
        'search':         None,
        'replacement':    '.method public final setupExpandTopNotificationObserver()V\n    .registers 6\n\n    new-instance v0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator$attach$3;\n\n    iget-object v1, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mHandler:Landroid/os/Handler;\n\n    invoke-direct {v0, p0, v1}, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator$attach$3;-><init>(Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;Landroid/os/Handler;)V\n\n    iget-object v1, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mContext:Landroid/content/Context;\n\n    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;\n\n    move-result-object v1\n\n    const-string v2, "status_bar_expand_top_notification"\n\n    invoke-static {v2}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;\n\n    move-result-object v2\n\n    const/4 v3, 0x0\n\n    const/4 v4, -0x1\n\n    invoke-virtual {v1, v2, v3, v0, v4}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->updateExpandTopNotification()V\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0002_updateExpandTopNotification',
        'type':           'method_add',
        'method':         '.method public final updateExpandTopNotification()V',
        'method_name':    'updateExpandTopNotification',
        'method_anchors': ['iget-object v0, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mContext:Landroid/content/Context;', 'invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;', 'invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I'],
        'search':         None,
        'replacement':    '.method public final updateExpandTopNotification()V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->mContext:Landroid/content/Context;\n\n    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;\n\n    move-result-object v0\n\n    const-string v1, "status_bar_expand_top_notification"\n\n    const/4 v2, 0x0\n\n    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I\n\n    move-result v0\n\n    const/4 v1, 0x1\n\n    if-ne v0, v1, :cond_0\n\n    move v2, v1\n\n    :cond_0\n    iput-boolean v2, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->expandTopNotification:Z\n\n    iget-object p0, p0, Lcom/android/systemui/statusbar/notification/collection/coordinator/RowAppearanceCoordinator;->entryToExpand:Lcom/android/systemui/statusbar/notification/collection/NotificationEntry;\n\n    if-eqz p0, :cond_1\n\n    iget-object p0, p0, Lcom/android/systemui/statusbar/notification/collection/NotificationEntry;->row:Lcom/android/systemui/statusbar/notification/row/ExpandableNotificationRow;\n\n    if-eqz p0, :cond_1\n\n    invoke-virtual {p0, v2}, Lcom/android/systemui/statusbar/notification/row/ExpandableNotificationRow;->setSystemExpanded(Z)V\n\n    :cond_1\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0003_field__field_public_expand',
        'type':           'field_add',
        'method':         '.field public expandTopNotification:Z',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field public expandTopNotification:Z',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added field',
    },
    {
        'id':             'p0004_field__field_public_final_',
        'type':           'field_add',
        'method':         '.field public final mContext:Landroid/content/Context;',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field public final mContext:Landroid/content/Context;',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added field',
    },
    {
        'id':             'p0005_field__field_public_final_',
        'type':           'field_add',
        'method':         '.field public final mHandler:Landroid/os/Handler;',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field public final mHandler:Landroid/os/Handler;',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added field',
    },
]
