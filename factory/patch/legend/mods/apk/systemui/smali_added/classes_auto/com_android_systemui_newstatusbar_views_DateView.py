"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/DateView.smali'
CLASS_FALLBACK_NAMES = ['DateView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/views/DateView;
.super Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;

# interfaces
.implements Lcom/android/systemui/plugins/DarkIconDispatcher$DarkReceiver;
.implements Lcom/android/systemui/newstatusbar/policy/ISlots;


# instance fields
.field private final currData:Lcom/android/systemui/newstatusbar/data/TextData;

.field private dispatcher:Lcom/android/systemui/plugins/DarkIconDispatcher;

.field private final formats:[Ljava/lang/String;

.field private mAreas:Ljava/util/ArrayList;

.field private mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

.field private mDarkColor:I

.field private mDarkIntensity:F

.field private mDateFormat:Ljava/lang/String;

.field private final mIntentReceiver:Landroid/content/BroadcastReceiver;

.field private mLastText:Ljava/lang/String;

.field private mLightColor:I

.field private mTint:I

.field private mUseTint:Z

.field private slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 12

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-string v0, "EE d MMMM"

    const-string v1, "d MMMM"

    const-string v2, "EE d"

    const-string v3, "d"

    const-string v4, "d MMMM"

    const-string v5, "d MM yyyy"

    const-string v6, "d MM yy"

    const-string v7, "MM yy"

    const-string v8, "EEEE"

    filled-new-array/range {v0 .. v8}, [Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->formats:[Ljava/lang/String;

    new-instance v0, Lcom/android/systemui/newstatusbar/views/DateView$1;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/views/DateView$1;-><init>(Lcom/android/systemui/newstatusbar/views/DateView;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/TextData;

    const-string v1, "status_date"

    invoke-direct {v0, p1, v1}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    const/4 v1, 0x0

    new-array v1, v1, [Ljava/lang/String;

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/TextData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    const-string v1, "statusbar_date_format"

    filled-new-array {v1}, [Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v1, Lcom/android/systemui/newstatusbar/views/DateView$2;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/views/DateView$2;-><init>(Lcom/android/systemui/newstatusbar/views/DateView;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/TextData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->currData:Lcom/android/systemui/newstatusbar/data/TextData;

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/DateView;->updateDateFormat()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/DateView;->updateDate()V

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/views/DateView;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/DateView;->updateDateFormat()V

    return-void
.end method

.method private setTime()V
    .registers 7

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

    if-nez v0, :cond_b

    new-instance v0, Lmiuix/pickerwidget/date/Calendar;

    invoke-direct {v0}, Lmiuix/pickerwidget/date/Calendar;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

    :cond_b
    :try_start_b
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    const-string v1, "setTimeZone"

    const/4 v2, 0x1

    new-array v3, v2, [Ljava/lang/Class;

    const-class v4, Ljava/util/TimeZone;

    const/4 v5, 0x0

    aput-object v4, v3, v5

    invoke-virtual {v0, v1, v3}, Ljava/lang/Class;->getMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

    new-array v3, v2, [Ljava/lang/Object;

    invoke-static {}, Ljava/util/TimeZone;->getDefault()Ljava/util/TimeZone;

    move-result-object v4

    aput-object v4, v3, v5

    invoke-virtual {v0, v1, v3}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    const-string v1, "setTimeInMillis"

    new-array v3, v2, [Ljava/lang/Class;

    sget-object v4, Ljava/lang/Long;->TYPE:Ljava/lang/Class;

    aput-object v4, v3, v5

    invoke-virtual {v0, v1, v3}, Ljava/lang/Class;->getMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

    new-array v2, v2, [Ljava/lang/Object;

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v3

    invoke-static {v3, v4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v3

    aput-object v3, v2, v5

    invoke-virtual {v0, v1, v2}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;
    :try_end_4f
    .catch Ljava/lang/Exception; {:try_start_b .. :try_end_4f} :catch_50

    goto :goto_51

    :catch_50
    move-exception v0

    :goto_51
    return-void
.end method

.method private updateDateFormat()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->formats:[Ljava/lang/String;

    const-string v1, "statusbar_date_format"

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    aget-object v0, v0, v1

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mDateFormat:Ljava/lang/String;

    return-void
.end method


# virtual methods
.method protected getData()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->currData:Lcom/android/systemui/newstatusbar/data/TextData;

    goto/32 :goto_a

    nop

    :goto_a
    return-object v0
.end method

.method public hasOverlappingRendering()Z
    .registers 2

    const/4 v0, 0x0

    return v0
.end method

.method protected onAttached()V
    .registers 6

    goto/32 :goto_51

    nop

    :goto_4
    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto/32 :goto_80

    nop

    :goto_b
    const-string v1, "android.intent.action.LOCALE_CHANGED"

    goto/32 :goto_4

    nop

    :goto_11
    const-string v1, "android.intent.action.TIME_TICK"

    goto/32 :goto_57

    nop

    :goto_17
    move-object v1, v4

    goto/32 :goto_6c

    nop

    :goto_1c
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/DateView;->update()V

    goto/32 :goto_63

    nop

    :goto_23
    const-string v1, "android.intent.action.TIME_SET"

    goto/32 :goto_29

    nop

    :goto_29
    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto/32 :goto_7a

    nop

    :goto_30
    check-cast v3, Lcom/android/systemui/broadcast/BroadcastDispatcher;

    goto/32 :goto_36

    nop

    :goto_36
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    goto/32 :goto_4a

    nop

    :goto_3c
    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    goto/32 :goto_11

    nop

    :goto_43
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/DateView;->updateDate()V

    goto/32 :goto_1c

    nop

    :goto_4a
    invoke-virtual {v3, v4, v0, v2, v1}, Lcom/android/systemui/broadcast/BroadcastDispatcher;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;Ljava/util/concurrent/Executor;Landroid/os/UserHandle;)V

    goto/32 :goto_43

    nop

    :goto_51
    new-instance v0, Landroid/content/IntentFilter;

    goto/32 :goto_3c

    nop

    :goto_57
    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto/32 :goto_23

    nop

    :goto_5e
    const/4 v1, 0x0

    goto/32 :goto_86

    nop

    :goto_63
    return-void

    :goto_64
    invoke-static {v3}, Lcom/android/systemui/SysDependency;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v3

    goto/32 :goto_30

    nop

    :goto_6c
    goto :goto_6e

    :catch_6d
    move-exception v3

    :goto_6e
    nop

    goto/32 :goto_a4

    nop

    :goto_73
    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto/32 :goto_b

    nop

    :goto_7a
    const-string v1, "android.intent.action.TIMEZONE_CHANGED"

    goto/32 :goto_73

    nop

    :goto_80
    const-string v1, "my.settings.intent.DATE_FORMAT_CHANGED"

    goto/32 :goto_9d

    nop

    :goto_86
    const/4 v2, 0x0

    :try_start_87
    const-class v3, Landroid/os/UserHandle;

    const-string v4, "ALL"

    invoke-virtual {v3, v4}, Ljava/lang/Class;->getField(Ljava/lang/String;)Ljava/lang/reflect/Field;

    move-result-object v3

    const/4 v4, 0x1

    invoke-virtual {v3, v4}, Ljava/lang/reflect/Field;->setAccessible(Z)V

    invoke-virtual {v3, v2}, Ljava/lang/reflect/Field;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v4

    check-cast v4, Landroid/os/UserHandle;
    :try_end_99
    .catch Ljava/lang/Exception; {:try_start_87 .. :try_end_99} :catch_6d

    goto/32 :goto_17

    nop

    :goto_9d
    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto/32 :goto_5e

    nop

    :goto_a4
    const-class v3, Lcom/android/systemui/broadcast/BroadcastDispatcher;

    goto/32 :goto_64

    nop
.end method

.method public onDarkChanged(Ljava/util/ArrayList;FI)V
    .registers 11

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mAreas:Ljava/util/ArrayList;

    iput p2, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mDarkIntensity:F

    iput p3, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mTint:I

    iget v4, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mLightColor:I

    iget v5, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mDarkColor:I

    iget-boolean v6, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mUseTint:Z

    move-object v0, p0

    move-object v1, p1

    move v2, p2

    move v3, p3

    invoke-virtual/range {v0 .. v6}, Lcom/android/systemui/newstatusbar/views/DateView;->updateLightDarkTint$2(Ljava/util/ArrayList;FIIIZ)V

    return-void
.end method

.method protected onDetached()V
    .registers 3

    goto/32 :goto_b

    nop

    :goto_4
    invoke-interface {v0, p0}, Lcom/android/systemui/plugins/DarkIconDispatcher;->removeDarkReceiver(Lcom/android/systemui/plugins/DarkIconDispatcher$DarkReceiver;)V

    :goto_7
    goto/32 :goto_24

    nop

    :goto_b
    const-class v0, Lcom/android/systemui/broadcast/BroadcastDispatcher;

    goto/32 :goto_2b

    nop

    :goto_11
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->dispatcher:Lcom/android/systemui/plugins/DarkIconDispatcher;

    goto/32 :goto_33

    nop

    :goto_17
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    goto/32 :goto_1d

    nop

    :goto_1d
    invoke-virtual {v0, v1}, Lcom/android/systemui/broadcast/BroadcastDispatcher;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V

    goto/32 :goto_11

    nop

    :goto_24
    return-void

    :goto_25
    check-cast v0, Lcom/android/systemui/broadcast/BroadcastDispatcher;

    goto/32 :goto_17

    nop

    :goto_2b
    invoke-static {v0}, Lcom/android/systemui/SysDependency;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    goto/32 :goto_25

    nop

    :goto_33
    if-nez v0, :cond_38

    goto/32 :goto_7

    :cond_38
    goto/32 :goto_4

    nop
.end method

.method public onLightDarkTintChanged(IIZ)V
    .registers 11

    iput p1, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mLightColor:I

    iput p2, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mDarkColor:I

    iput-boolean p3, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mUseTint:Z

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mAreas:Ljava/util/ArrayList;

    iget v2, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mDarkIntensity:F

    iget v3, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mTint:I

    move-object v0, p0

    move v4, p1

    move v5, p2

    move v6, p3

    invoke-virtual/range {v0 .. v6}, Lcom/android/systemui/newstatusbar/views/DateView;->updateLightDarkTint$2(Ljava/util/ArrayList;FIIIZ)V

    return-void
.end method

.method public setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V
    .registers 5

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/views/DateView;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-virtual {v0, p1, p0}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->getDispather(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;Lcom/android/systemui/newstatusbar/policy/ISlots;)Lcom/android/systemui/plugins/DarkIconDispatcher;

    move-result-object v0

    if-eqz v0, :cond_16

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->dispatcher:Lcom/android/systemui/plugins/DarkIconDispatcher;

    invoke-interface {v0, p0}, Lcom/android/systemui/plugins/DarkIconDispatcher;->addDarkReceiver(Lcom/android/systemui/plugins/DarkIconDispatcher$DarkReceiver;)V

    goto :goto_1d

    :cond_16
    sget-object v1, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->TAG:Ljava/lang/String;

    const-string v2, "setSlot: DateView dispatcher = null"

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_1d
    return-void
.end method

.method public updateDate()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mDateFormat:Ljava/lang/String;

    if-nez v0, :cond_10

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->formats:[Ljava/lang/String;

    const-string v1, "statusbar_date_format"

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    aget-object v0, v0, v1

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mDateFormat:Ljava/lang/String;

    :cond_10
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/DateView;->setTime()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/DateView;->getContext()Landroid/content/Context;

    move-result-object v1

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mDateFormat:Ljava/lang/String;

    invoke-virtual {v0, v1, v2}, Lmiuix/pickerwidget/date/Calendar;->format(Landroid/content/Context;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mLastText:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_2c

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/DateView;->setText(Ljava/lang/CharSequence;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/DateView;->mLastText:Ljava/lang/String;

    :cond_2c
    return-void
.end method

.method public updateLightDarkTint$2(Ljava/util/ArrayList;FIIIZ)V
    .registers 9

    if-eqz p6, :cond_7

    invoke-static {p1, p0, p3}, Lcom/android/systemui/plugins/DarkIconDispatcher;->getTint(Ljava/util/Collection;Landroid/view/View;I)I

    move-result v0

    goto :goto_13

    :cond_7
    invoke-static {p1, p0, p2}, Lcom/android/systemui/statusbar/DarkIconDispatcherExt;->getDarkIntensity(Ljava/util/ArrayList;Landroid/view/View;F)F

    move-result v0

    const/4 v1, 0x0

    cmpl-float v0, v0, v1

    if-lez v0, :cond_12

    move v0, p5

    goto :goto_13

    :cond_12
    move v0, p4

    :goto_13
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/DateView;->setTextColor(I)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_DateView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
