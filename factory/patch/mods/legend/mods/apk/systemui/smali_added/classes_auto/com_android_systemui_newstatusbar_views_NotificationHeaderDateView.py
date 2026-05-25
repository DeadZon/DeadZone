"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/NotificationHeaderDateView.smali'
CLASS_FALLBACK_NAMES = ['NotificationHeaderDateView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;
.super Lcom/android/systemui/statusbar/views/MiuiClock;


# instance fields
.field private final controller:Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;

.field private final currData:Lcom/android/systemui/newstatusbar/data/TextData;

.field private final formats:[Ljava/lang/String;

.field private isAttach:Z

.field private mColorSet:I

.field private mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

.field private mDateFormat:Ljava/lang/String;

.field private final mIntentReceiver:Landroid/content/BroadcastReceiver;

.field private mLastText:Ljava/lang/String;

.field private paint:Landroid/graphics/Paint;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 12

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MiuiClock;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-string v0, "EEEE d MMMM"

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

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->formats:[Ljava/lang/String;

    new-instance v0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;-><init>(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/TextData;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "Notif_date"

    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    const/4 v1, 0x0

    new-array v1, v1, [Ljava/lang/String;

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/TextData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    const-string v1, "Notif_date_format"

    filled-new-array {v1}, [Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v1, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$2;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$2;-><init>(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/TextData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->currData:Lcom/android/systemui/newstatusbar/data/TextData;

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->updateDateFormat()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->updateDate()V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->controller:Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 13

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/MiuiClock;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

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

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->formats:[Ljava/lang/String;

    new-instance v0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$1;-><init>(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/TextData;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "Notif_date"

    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    const/4 v1, 0x0

    new-array v1, v1, [Ljava/lang/String;

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/TextData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    const-string v1, "Notif_date_format"

    filled-new-array {v1}, [Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v1, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$2;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView$2;-><init>(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/TextData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->currData:Lcom/android/systemui/newstatusbar/data/TextData;

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->updateDateFormat()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->updateDate()V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->controller:Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->updateDateFormat()V

    return-void
.end method

.method private getTypeFace(Ljava/lang/String;)Landroid/graphics/Typeface;
    .registers 6

    const/4 v0, 0x0

    :try_start_1
    invoke-static {p1}, Landroid/graphics/Typeface;->createFromFile(Ljava/lang/String;)Landroid/graphics/Typeface;

    move-result-object v1
    :try_end_5
    .catch Ljava/lang/RuntimeException; {:try_start_1 .. :try_end_5} :catch_7

    move-object v0, v1

    goto :goto_15

    :catch_7
    move-exception v1

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v2

    const-string v3, "getTypeFase : fonts not found"

    invoke-static {v2, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_15
    return-object v0
.end method

.method private resetClip()V
    .registers 4

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    instance-of v1, v0, Landroid/view/ViewGroup;

    if-eqz v1, :cond_29

    move-object v1, v0

    check-cast v1, Landroid/view/ViewGroup;

    const/4 v2, 0x0

    invoke-virtual {v1, v2}, Landroid/view/ViewGroup;->setClipChildren(Z)V

    move-object v1, v0

    check-cast v1, Landroid/view/ViewGroup;

    invoke-virtual {v1, v2}, Landroid/view/ViewGroup;->setClipToPadding(Z)V

    invoke-interface {v0}, Landroid/view/ViewParent;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    instance-of v1, v0, Landroid/view/ViewGroup;

    if-eqz v1, :cond_29

    move-object v1, v0

    check-cast v1, Landroid/view/ViewGroup;

    invoke-virtual {v1, v2}, Landroid/view/ViewGroup;->setClipChildren(Z)V

    move-object v1, v0

    check-cast v1, Landroid/view/ViewGroup;

    invoke-virtual {v1, v2}, Landroid/view/ViewGroup;->setClipToPadding(Z)V

    :cond_29
    return-void
.end method

.method private setTime()V
    .registers 7

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

    if-nez v0, :cond_b

    new-instance v0, Lmiuix/pickerwidget/date/Calendar;

    invoke-direct {v0}, Lmiuix/pickerwidget/date/Calendar;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

    :cond_b
    :try_start_b
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

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

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

    new-array v3, v2, [Ljava/lang/Object;

    invoke-static {}, Ljava/util/TimeZone;->getDefault()Ljava/util/TimeZone;

    move-result-object v4

    aput-object v4, v3, v5

    invoke-virtual {v0, v1, v3}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

    invoke-virtual {v0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    const-string v1, "setTimeInMillis"

    new-array v3, v2, [Ljava/lang/Class;

    sget-object v4, Ljava/lang/Long;->TYPE:Ljava/lang/Class;

    aput-object v4, v3, v5

    invoke-virtual {v0, v1, v3}, Ljava/lang/Class;->getMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

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

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->formats:[Ljava/lang/String;

    const-string v1, "Notif_date_format"

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    aget-object v0, v0, v1

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mDateFormat:Ljava/lang/String;

    return-void
.end method

.method private updateDefault()V
    .registers 4

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    if-eqz v0, :cond_23

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getCurrentTextColor()I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->defColor:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getTextSize()F

    move-result v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    invoke-virtual {v2}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v2

    iget v2, v2, Landroid/util/DisplayMetrics;->scaledDensity:F

    div-float/2addr v1, v2

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->defSize:F

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getTypeface()Landroid/graphics/Typeface;

    move-result-object v1

    iput-object v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->defTypefase:Landroid/graphics/Typeface;

    :cond_23
    return-void
.end method

.method private updateTyperface()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->paint:Landroid/graphics/Paint;

    if-nez v0, :cond_a

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->paint:Landroid/graphics/Paint;

    :cond_a
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    if-eqz v0, :cond_24

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->getTypeFace()Landroid/graphics/Typeface;

    move-result-object v1

    iget v2, v0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    invoke-super {p0, v1, v2}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTypeface(Landroid/graphics/Typeface;I)V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->paint:Landroid/graphics/Paint;

    iget v3, v0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    invoke-static {v1, v3}, Landroid/graphics/Typeface;->create(Landroid/graphics/Typeface;I)Landroid/graphics/Typeface;

    move-result-object v3

    invoke-virtual {v2, v3}, Landroid/graphics/Paint;->setTypeface(Landroid/graphics/Typeface;)Landroid/graphics/Typeface;

    :cond_24
    return-void
.end method


# virtual methods
.method protected getData()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->currData:Lcom/android/systemui/newstatusbar/data/TextData;

    goto/32 :goto_a

    nop

    :goto_a
    return-object v0
.end method

.method public onAttachedToWindow()V
    .registers 7

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiClock;->onAttachedToWindow()V

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->isAttach:Z

    const/4 v1, 0x1

    if-nez v0, :cond_d

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->isAttach:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->updateDefault()V

    :cond_d
    new-instance v0, Landroid/content/IntentFilter;

    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    const-string v2, "android.intent.action.TIME_TICK"

    invoke-virtual {v0, v2}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v2, "android.intent.action.TIME_SET"

    invoke-virtual {v0, v2}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v2, "android.intent.action.TIMEZONE_CHANGED"

    invoke-virtual {v0, v2}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v2, "android.intent.action.LOCALE_CHANGED"

    invoke-virtual {v0, v2}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v2, "my.settings.intent.DATE_FORMAT_CHANGED"

    invoke-virtual {v0, v2}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const/4 v2, 0x0

    const/4 v3, 0x0

    :try_start_2d
    const-class v4, Landroid/os/UserHandle;

    const-string v5, "ALL"

    invoke-virtual {v4, v5}, Ljava/lang/Class;->getField(Ljava/lang/String;)Ljava/lang/reflect/Field;

    move-result-object v4

    invoke-virtual {v4, v1}, Ljava/lang/reflect/Field;->setAccessible(Z)V

    invoke-virtual {v4, v3}, Ljava/lang/reflect/Field;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/os/UserHandle;
    :try_end_3e
    .catch Ljava/lang/Exception; {:try_start_2d .. :try_end_3e} :catch_40

    move-object v2, v1

    goto :goto_41

    :catch_40
    move-exception v1

    :goto_41
    nop

    const-class v1, Lcom/android/systemui/broadcast/BroadcastDispatcher;

    invoke-static {v1}, Lcom/android/systemui/SysDependency;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/broadcast/BroadcastDispatcher;

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    invoke-virtual {v1, v4, v0, v3, v2}, Lcom/android/systemui/broadcast/BroadcastDispatcher;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;Ljava/util/concurrent/Executor;Landroid/os/UserHandle;)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->update()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->updateDate()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->resetClip()V

    return-void
.end method

.method public onDetachedFromWindow()V
    .registers 3

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiClock;->onDetachedFromWindow()V

    const-class v0, Lcom/android/systemui/broadcast/BroadcastDispatcher;

    invoke-static {v0}, Lcom/android/systemui/SysDependency;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/broadcast/BroadcastDispatcher;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mIntentReceiver:Landroid/content/BroadcastReceiver;

    invoke-virtual {v0, v1}, Lcom/android/systemui/broadcast/BroadcastDispatcher;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V

    return-void
.end method

.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 8

    goto/32 :goto_4

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->paint:Landroid/graphics/Paint;

    goto/32 :goto_c7

    nop

    :goto_a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->paint:Landroid/graphics/Paint;

    goto/32 :goto_19

    nop

    :goto_10
    if-eqz v2, :cond_15

    goto/32 :goto_107

    :cond_15
    goto/32 :goto_a4

    nop

    :goto_19
    iget v2, v0, Lcom/android/systemui/newstatusbar/data/TextData;->color:I

    goto/32 :goto_10

    nop

    :goto_1f
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->onDraw(Landroid/graphics/Canvas;)V

    goto/32 :goto_4d

    nop

    :goto_26
    const/high16 v3, 0x40000000  # 2.0f

    goto/32 :goto_f5

    nop

    :goto_2c
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->paint:Landroid/graphics/Paint;

    :goto_2e
    goto/32 :goto_80

    nop

    :goto_32
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getHeight()I

    move-result v2

    goto/32 :goto_113

    nop

    :goto_3a
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->paint:Landroid/graphics/Paint;

    goto/32 :goto_aa

    nop

    :goto_40
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    goto/32 :goto_2c

    nop

    :goto_48
    add-float/2addr v3, v4

    goto/32 :goto_b8

    nop

    :goto_4d
    return-void

    :goto_4e
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    goto/32 :goto_fa

    nop

    :goto_56
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    goto/32 :goto_10b

    nop

    :goto_5e
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getText()Ljava/lang/CharSequence;

    move-result-object v4

    goto/32 :goto_4e

    nop

    :goto_66
    if-gt v4, v5, :cond_6b

    goto/32 :goto_77

    :cond_6b
    goto/32 :goto_ef

    nop

    :goto_6f
    invoke-virtual {p1, v3, v4, v2, v5}, Landroid/graphics/Canvas;->drawText(Ljava/lang/String;FFLandroid/graphics/Paint;)V

    goto/32 :goto_1f

    nop

    :goto_76
    goto :goto_d8

    :goto_77
    goto/32 :goto_d6

    nop

    :goto_7b
    int-to-float v1, v1

    goto/32 :goto_88

    nop

    :goto_80
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    goto/32 :goto_a

    nop

    :goto_88
    const/high16 v2, 0x41200000  # 10.0f

    goto/32 :goto_bd

    nop

    :goto_8e
    invoke-virtual {v4}, Landroid/graphics/Paint;->ascent()F

    move-result v4

    goto/32 :goto_48

    nop

    :goto_96
    iget v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->division:I

    goto/32 :goto_7b

    nop

    :goto_9c
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->getColor()I

    move-result v2

    :goto_a0
    goto/32 :goto_dc

    nop

    :goto_a4
    iget v2, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mColorSet:I

    goto/32 :goto_106

    nop

    :goto_aa
    invoke-virtual {v3}, Landroid/graphics/Paint;->descent()F

    move-result v3

    goto/32 :goto_d0

    nop

    :goto_b2
    iget-object v5, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->paint:Landroid/graphics/Paint;

    goto/32 :goto_6f

    nop

    :goto_b8
    div-float/2addr v3, v1

    goto/32 :goto_e3

    nop

    :goto_bd
    div-float/2addr v1, v2

    goto/32 :goto_32

    nop

    :goto_c2
    const/4 v4, 0x0

    goto/32 :goto_b2

    nop

    :goto_c7
    if-eqz v0, :cond_cc

    goto/32 :goto_2e

    :cond_cc
    goto/32 :goto_40

    nop

    :goto_d0
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->paint:Landroid/graphics/Paint;

    goto/32 :goto_8e

    nop

    :goto_d6
    const-string v4, ""

    :goto_d8
    goto/32 :goto_56

    nop

    :goto_dc
    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->setColor(I)V

    goto/32 :goto_96

    nop

    :goto_e3
    sub-float/2addr v2, v3

    goto/32 :goto_100

    nop

    :goto_e8
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    goto/32 :goto_5e

    nop

    :goto_ef
    const-string v4, " "

    goto/32 :goto_76

    nop

    :goto_f5
    div-float/2addr v2, v3

    goto/32 :goto_3a

    nop

    :goto_fa
    iget v4, v0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    goto/32 :goto_118

    nop

    :goto_100
    new-instance v3, Ljava/lang/StringBuilder;

    goto/32 :goto_e8

    nop

    :goto_106
    goto :goto_a0

    :goto_107
    goto/32 :goto_9c

    nop

    :goto_10b
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    goto/32 :goto_c2

    nop

    :goto_113
    int-to-float v2, v2

    goto/32 :goto_26

    nop

    :goto_118
    const/4 v5, 0x1

    goto/32 :goto_66

    nop
.end method

.method protected onMeasure(II)V
    .registers 8

    goto/32 :goto_c2

    nop

    :goto_4
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto/32 :goto_9f

    nop

    :goto_b
    goto :goto_17

    :goto_c
    goto/32 :goto_16

    nop

    :goto_10
    const-string v3, " "

    goto/32 :goto_29

    nop

    :goto_16
    const/4 v2, 0x0

    :goto_17
    goto/32 :goto_b5

    nop

    :goto_1b
    iget-boolean v2, v0, Lcom/android/systemui/newstatusbar/data/TextData;->shadow_enable:Z

    goto/32 :goto_3c

    nop

    :goto_21
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto/32 :goto_6d

    nop

    :goto_29
    goto :goto_30

    :goto_2a
    goto/32 :goto_2e

    nop

    :goto_2e
    const-string v3, ""

    :goto_30
    goto/32 :goto_34

    nop

    :goto_34
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto/32 :goto_21

    nop

    :goto_3c
    if-nez v2, :cond_41

    goto/32 :goto_c

    :cond_41
    goto/32 :goto_89

    nop

    :goto_45
    invoke-virtual {p0, v1, v2}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->setMeasuredDimension(II)V

    goto/32 :goto_61

    nop

    :goto_4c
    iget v3, v0, Lcom/android/systemui/newstatusbar/data/TextData;->typeFaseStyle:I

    goto/32 :goto_68

    nop

    :goto_52
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->paint:Landroid/graphics/Paint;

    goto/32 :goto_58

    nop

    :goto_58
    if-eqz v1, :cond_5d

    goto/32 :goto_80

    :cond_5d
    goto/32 :goto_8f

    nop

    :goto_61
    return-void

    :goto_62
    new-instance v2, Ljava/lang/StringBuilder;

    goto/32 :goto_4

    nop

    :goto_68
    const/4 v4, 0x1

    goto/32 :goto_75

    nop

    :goto_6d
    invoke-virtual {v1, v2}, Landroid/graphics/Paint;->measureText(Ljava/lang/String;)F

    move-result v1

    goto/32 :goto_1b

    nop

    :goto_75
    if-gt v3, v4, :cond_7a

    goto/32 :goto_2a

    :cond_7a
    goto/32 :goto_10

    nop

    :goto_7e
    iput-object v1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->paint:Landroid/graphics/Paint;

    :goto_80
    goto/32 :goto_a7

    nop

    :goto_84
    float-to-int v1, v1

    goto/32 :goto_ba

    nop

    :goto_89
    sget v2, Lcom/android/systemui/newstatusbar/data/TextData;->ShadowRadius:F

    goto/32 :goto_b

    nop

    :goto_8f
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getPaint()Landroid/text/TextPaint;

    move-result-object v1

    goto/32 :goto_7e

    nop

    :goto_97
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto/32 :goto_4c

    nop

    :goto_9f
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getText()Ljava/lang/CharSequence;

    move-result-object v3

    goto/32 :goto_97

    nop

    :goto_a7
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->paint:Landroid/graphics/Paint;

    goto/32 :goto_62

    nop

    :goto_ad
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    goto/32 :goto_52

    nop

    :goto_b5
    add-float/2addr v1, v2

    goto/32 :goto_84

    nop

    :goto_ba
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getMeasuredHeight()I

    move-result v2

    goto/32 :goto_45

    nop

    :goto_c2
    invoke-super {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MiuiClock;->onMeasure(II)V

    goto/32 :goto_ad

    nop
.end method

.method public setAlpha(F)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setAlpha(F)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->controller:Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;

    if-eqz v0, :cond_a

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;->onAlphaChange(F)V

    :cond_a
    return-void
.end method

.method public setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->setTextSize(F)V

    return-void
.end method

.method public setText(Ljava/lang/CharSequence;Landroid/widget/TextView$BufferType;)V
    .registers 3

    return-void
.end method

.method public setTextAppearance(I)V
    .registers 2

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTextAppearance(I)V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->updateDefault()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->update()V

    return-void
.end method

.method public setTextColor()V
    .registers 2

    const/4 v0, 0x0

    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTextColor(I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->invalidate()V

    return-void
.end method

.method public setTextColor(I)V
    .registers 3

    const/4 v0, 0x0

    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTextColor(I)V

    if-eqz p1, :cond_8

    iput p1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mColorSet:I

    :cond_8
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->setTextColor()V

    return-void
.end method

.method public setTextColor(Landroid/content/res/ColorStateList;)V
    .registers 3

    const/4 v0, 0x0

    invoke-static {v0}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;

    move-result-object v0

    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTextColor(Landroid/content/res/ColorStateList;)V

    invoke-virtual {p1}, Landroid/content/res/ColorStateList;->getDefaultColor()I

    move-result v0

    if-eqz v0, :cond_10

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mColorSet:I

    :cond_10
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->setTextColor()V

    return-void
.end method

.method public setTextSize(F)V
    .registers 3

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->getSize()F

    move-result v0

    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTextSize(F)V

    return-void
.end method

.method public setTextSize(IF)V
    .registers 5

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->getSize()F

    move-result v0

    const/4 v1, 0x2

    invoke-super {p0, v1, v0}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTextSize(IF)V

    return-void
.end method

.method public setTransitionAlpha(F)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setTransitionAlpha(F)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->controller:Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;

    if-eqz v0, :cond_a

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;->onAlphaChange(F)V

    :cond_a
    return-void
.end method

.method public setTypeface(Landroid/graphics/Typeface;)V
    .registers 2

    return-void
.end method

.method public setTypeface(Landroid/graphics/Typeface;I)V
    .registers 3

    return-void
.end method

.method public update()V
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->setTextColor()V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->setTextSize(F)V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->updateTyperface()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->invalidate()V

    return-void
.end method

.method public updateDate()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mDateFormat:Ljava/lang/String;

    if-nez v0, :cond_10

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->formats:[Ljava/lang/String;

    const-string v1, "Notif_date_format"

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    aget-object v0, v0, v1

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mDateFormat:Ljava/lang/String;

    :cond_10
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->setTime()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mCurrentTime:Lmiuix/pickerwidget/date/Calendar;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->getContext()Landroid/content/Context;

    move-result-object v1

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mDateFormat:Ljava/lang/String;

    invoke-virtual {v0, v1, v2}, Lmiuix/pickerwidget/date/Calendar;->format(Landroid/content/Context;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mLastText:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_2e

    sget-object v1, Landroid/widget/TextView$BufferType;->NORMAL:Landroid/widget/TextView$BufferType;

    invoke-super {p0, v0, v1}, Lcom/android/systemui/statusbar/views/MiuiClock;->setText(Ljava/lang/CharSequence;Landroid/widget/TextView$BufferType;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/views/NotificationHeaderDateView;->mLastText:Ljava/lang/String;

    :cond_2e
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_NotificationHeaderDateView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
