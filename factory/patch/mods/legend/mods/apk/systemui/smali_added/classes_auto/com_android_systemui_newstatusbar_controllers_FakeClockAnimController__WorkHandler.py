"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler.smali'
CLASS_FALLBACK_NAMES = ['FakeClockAnimController$WorkHandler.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;
.super Landroid/os/Handler;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0xa
    name = "WorkHandler"
.end annotation


# instance fields
.field private final controller:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;


# direct methods
.method public constructor <init>(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)V
    .registers 3

    invoke-static {}, Landroid/os/Looper;->myLooper()Landroid/os/Looper;

    move-result-object v0

    invoke-direct {p0, v0}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;->controller:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    return-void
.end method


# virtual methods
.method public handleMessage(Landroid/os/Message;)V
    .registers 7

    iget v0, p1, Landroid/os/Message;->what:I

    const/16 v1, 0x1f5

    const/4 v2, 0x2

    if-eq v0, v1, :cond_3e

    const/16 v1, 0x1f6

    if-eq v0, v1, :cond_c

    return-void

    :cond_c
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;->controller:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->access$500(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;->controller:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-static {v1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->access$200(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;->controller:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-static {v1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->access$100(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;->controller:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    iget-object v3, v0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v3}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v3

    invoke-virtual {v3}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->getSize()F

    move-result v3

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;->controller:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-static {v4}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->access$700(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)Landroid/content/Context;

    move-result-object v4

    invoke-virtual {v4}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v4

    invoke-virtual {v4}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v4

    invoke-static {v2, v3, v4}, Landroid/util/TypedValue;->applyDimension(IFLandroid/util/DisplayMetrics;)F

    move-result v2

    invoke-static {v1, v2}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->access$602(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;F)F

    return-void

    :cond_3e
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;->controller:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->access$000(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;->controller:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-static {v1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->access$100(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;->controller:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-static {v1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->access$200(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;->controller:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    iget-object v3, v0, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->clockSettings:Lcom/android/systemui/newstatusbar/clock/ClockSettings;

    invoke-virtual {v3}, Lcom/android/systemui/newstatusbar/clock/ClockSettings;->getClockData()Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;

    move-result-object v3

    invoke-virtual {v3}, Lcom/android/systemui/newstatusbar/clock/ClockSettings$ClockData;->getSize()F

    move-result v3

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;->controller:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-static {v4}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->access$400(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)Landroid/content/Context;

    move-result-object v4

    invoke-virtual {v4}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v4

    invoke-virtual {v4}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v4

    invoke-static {v2, v3, v4}, Landroid/util/TypedValue;->applyDimension(IFLandroid/util/DisplayMetrics;)F

    move-result v2

    invoke-static {v1, v2}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->access$302(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;F)F

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_FakeClockAnimController_WorkHandler',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
