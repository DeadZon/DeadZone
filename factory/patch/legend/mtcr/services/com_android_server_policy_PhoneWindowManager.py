"""
Legend MTCR patch - class-level rule.

Target JAR   : services.jar
Target class : com/android/server/policy/PhoneWindowManager
Source MTCR  : Service_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "services.jar"
TARGET_CLASS = "com/android/server/policy/PhoneWindowManager.smali"

PATCHES = [
    {
        "id":          "replace_method__init___V",
        "method":      ".method public constructor <init>()V",
        "type":        "method_replace",
        "search": """\
.method public constructor <init>()V
    .registers 5

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/lang/Object;

    invoke-direct {v0}, Ljava/lang/Object;-><init>()V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mLock:Ljava/lang/Object;

    new-instance v0, Landroid/util/SparseArray;

    invoke-direct {v0}, Landroid/util/SparseArray;-><init>()V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mScreenOnListeners:Landroid/util/SparseArray;

    new-instance v0, Ljava/lang/Object;

    invoke-direct {v0}, Ljava/lang/Object;-><init>()V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mServiceAcquireLock:Ljava/lang/Object;

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mEnableBugReportKeyboardShortcut:Z

    const/4 v1, 0x1

    iput-boolean v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mEnableCarDockHomeCapture:Z

    new-instance v2, Lcom/android/server/policy/PhoneWindowManager$1;

    invoke-direct {v2, p0}, Lcom/android/server/policy/PhoneWindowManager$1;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v2, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDrawnCallback:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate$DrawnListener;

    iput-boolean v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mNavBarVirtualKeyHapticFeedbackEnabled:Z

    const/4 v2, -0x1

    iput v2, p0, Lcom/android/server/policy/PhoneWindowManager;->mPendingWakeKey:I

    iput v2, p0, Lcom/android/server/policy/PhoneWindowManager;->mCameraLensCoverState:I

    iput-boolean v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStylusButtonsEnabled:Z

    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHasSoftInput:Z

    new-instance v1, Ljava/util/HashSet;

    invoke-direct {v1}, Ljava/util/HashSet;-><init>()V

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAllowLockscreenWhenOnDisplays:Ljava/util/HashSet;

    iput v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mRingerToggleChord:I

    new-instance v1, Landroid/util/SparseArray;

    invoke-direct {v1}, Landroid/util/SparseArray;-><init>()V

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mConsumedKeysForDevice:Landroid/util/SparseArray;

    new-instance v1, Lcom/android/internal/policy/LogDecelerateInterpolator;

    const/16 v3, 0x64

    invoke-direct {v1, v3, v0}, Lcom/android/internal/policy/LogDecelerateInterpolator;-><init>(II)V

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mLogDecelerateInterpolator:Lcom/android/internal/policy/LogDecelerateInterpolator;

    new-instance v1, Lcom/android/server/policy/DeferredKeyActionExecutor;

    invoke-direct {v1}, Lcom/android/server/policy/DeferredKeyActionExecutor;-><init>()V

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mDeferredKeyActionExecutor:Lcom/android/server/policy/DeferredKeyActionExecutor;

    iput v2, p0, Lcom/android/server/policy/PhoneWindowManager;->mTopFocusedDisplayId:I

    const/16 v1, 0x320

    iput v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mPowerButtonSuppressionDelayMillis:I

    new-instance v1, Lcom/android/server/policy/PhoneWindowManager$PowerKeyRule;

    invoke-direct {v1, p0}, Lcom/android/server/policy/PhoneWindowManager$PowerKeyRule;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mPowerKeyRule:Lcom/android/server/policy/PhoneWindowManager$PowerKeyRule;

    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mLockNowPending:Z

    const/16 v0, 0x3e8

    iput v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDrawnTimeout:I

    invoke-static {}, Landroid/os/UserManager;->isVisibleBackgroundUsersEnabled()Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mVisibleBackgroundUsersEnabled:Z

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$2;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$2;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHDMIObserver:Landroid/os/UEventObserver;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$3;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$3;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHDMISwitchObserver:Landroid/os/UEventObserver;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$4;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$4;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mExtEventObserver:Landroid/os/UEventObserver;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$5;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$5;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mPersistentVrModeListener:Landroid/service/vr/IPersistentVrStateCallbacks;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$6;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$6;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mEndCallLongPress:Ljava/lang/Runnable;

    new-instance v0, Landroid/util/SparseArray;

    invoke-direct {v0}, Landroid/util/SparseArray;-><init>()V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDisplayHomeButtonHandlers:Landroid/util/SparseArray;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$15;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$15;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDockReceiver:Landroid/content/BroadcastReceiver;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$16;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$16;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mMultiuserReceiver:Landroid/content/BroadcastReceiver;

    const/4 v0, 0x0

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mBootMsgDialog:Landroid/app/ProgressDialog;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$ScreenLockTimeout;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$ScreenLockTimeout;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mScreenLockTimeout:Lcom/android/server/policy/PhoneWindowManager$ScreenLockTimeout;

    return-void
.end method
""",
        "replacement": """\
.method public constructor <init>()V
    .registers 5

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/lang/Object;

    invoke-direct {v0}, Ljava/lang/Object;-><init>()V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mLock:Ljava/lang/Object;

    new-instance v0, Landroid/util/SparseArray;

    invoke-direct {v0}, Landroid/util/SparseArray;-><init>()V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mScreenOnListeners:Landroid/util/SparseArray;

    new-instance v0, Ljava/lang/Object;

    invoke-direct {v0}, Ljava/lang/Object;-><init>()V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mServiceAcquireLock:Ljava/lang/Object;

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mEnableBugReportKeyboardShortcut:Z

    const/4 v1, 0x1

    iput-boolean v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mEnableCarDockHomeCapture:Z

    new-instance v2, Lcom/android/server/policy/PhoneWindowManager$1;

    invoke-direct {v2, p0}, Lcom/android/server/policy/PhoneWindowManager$1;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v2, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDrawnCallback:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate$DrawnListener;

    iput-boolean v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mNavBarVirtualKeyHapticFeedbackEnabled:Z

    const/4 v2, -0x1

    iput v2, p0, Lcom/android/server/policy/PhoneWindowManager;->mPendingWakeKey:I

    iput v2, p0, Lcom/android/server/policy/PhoneWindowManager;->mCameraLensCoverState:I

    iput-boolean v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStylusButtonsEnabled:Z

    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHasSoftInput:Z

    new-instance v1, Ljava/util/HashSet;

    invoke-direct {v1}, Ljava/util/HashSet;-><init>()V

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAllowLockscreenWhenOnDisplays:Ljava/util/HashSet;

    iput v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mRingerToggleChord:I

    new-instance v1, Landroid/util/SparseArray;

    invoke-direct {v1}, Landroid/util/SparseArray;-><init>()V

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mConsumedKeysForDevice:Landroid/util/SparseArray;

    new-instance v1, Lcom/android/internal/policy/LogDecelerateInterpolator;

    const/16 v3, 0x64

    invoke-direct {v1, v3, v0}, Lcom/android/internal/policy/LogDecelerateInterpolator;-><init>(II)V

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mLogDecelerateInterpolator:Lcom/android/internal/policy/LogDecelerateInterpolator;

    new-instance v1, Lcom/android/server/policy/DeferredKeyActionExecutor;

    invoke-direct {v1}, Lcom/android/server/policy/DeferredKeyActionExecutor;-><init>()V

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mDeferredKeyActionExecutor:Lcom/android/server/policy/DeferredKeyActionExecutor;

    iput v2, p0, Lcom/android/server/policy/PhoneWindowManager;->mTopFocusedDisplayId:I

    const/16 v1, 0x320

    iput v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mPowerButtonSuppressionDelayMillis:I

    new-instance v1, Lcom/android/server/policy/PhoneWindowManager$PowerKeyRule;

    invoke-direct {v1, p0}, Lcom/android/server/policy/PhoneWindowManager$PowerKeyRule;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mPowerKeyRule:Lcom/android/server/policy/PhoneWindowManager$PowerKeyRule;

    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mLockNowPending:Z

    const/16 v0, 0x3e8

    iput v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDrawnTimeout:I

    invoke-static {}, Landroid/os/UserManager;->isVisibleBackgroundUsersEnabled()Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mVisibleBackgroundUsersEnabled:Z

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$2;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$2;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHDMIObserver:Landroid/os/UEventObserver;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$3;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$3;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHDMISwitchObserver:Landroid/os/UEventObserver;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$4;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$4;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mExtEventObserver:Landroid/os/UEventObserver;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$5;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$5;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mPersistentVrModeListener:Landroid/service/vr/IPersistentVrStateCallbacks;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$6;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$6;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mEndCallLongPress:Ljava/lang/Runnable;

    new-instance v0, Landroid/util/SparseArray;

    invoke-direct {v0}, Landroid/util/SparseArray;-><init>()V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDisplayHomeButtonHandlers:Landroid/util/SparseArray;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$15;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$15;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDockReceiver:Landroid/content/BroadcastReceiver;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$16;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$16;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mMultiuserReceiver:Landroid/content/BroadcastReceiver;

    const/4 v0, 0x0

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mBootMsgDialog:Landroid/app/ProgressDialog;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$ScreenLockTimeout;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$ScreenLockTimeout;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mScreenLockTimeout:Lcom/android/server/policy/PhoneWindowManager$ScreenLockTimeout;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$MusicPrev;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$MusicPrev;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mVolumeDownLongPress:Ljava/lang/Runnable;

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$MusicNext;

    invoke-direct {v0, p0}, Lcom/android/server/policy/PhoneWindowManager$MusicNext;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mVolumeUpLongPress:Ljava/lang/Runnable;

    return-void
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "add_method_CheckDisplayState__Z",
        "method":      ".method private CheckDisplayState()Z",
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method private CheckDisplayState()Z
    .registers 4

    const/4 v1, 0x0

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    invoke-virtual {v0}, Lcom/android/server/wm/DisplayPolicy;->isScreenOnFully()Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardLocked()Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    const-string v2, "audio"

    invoke-virtual {v0, v2}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/media/AudioManager;

    invoke-virtual {v0}, Landroid/media/AudioManager;->isMusicActive()Z

    move-result v0

    if-nez v0, :cond_1

    :cond_0
    const/4 v0, 0x1

    :goto_0
    return v0

    :cond_1
    move v0, v1

    goto :goto_0

    :cond_2
    move v0, v1

    goto :goto_0
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Service_Legend.mtcr",
    },
    {
        "id":          "add_method_checkVolBtn_Landroid_view_KeyEvent__I",
        "method":      ".method private checkVolBtn(Landroid/view/KeyEvent;)I",
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method private checkVolBtn(Landroid/view/KeyEvent;)I
    .registers 6

    const/4 v2, 0x1

    const/4 v1, 0x0

    invoke-direct {p0}, Lcom/android/server/policy/PhoneWindowManager;->CheckDisplayState()Z

    move-result v3

    if-nez v3, :cond_2

    sget-boolean v3, Lcom/android/server/policy/VolBtnHelper;->mVolBtnMusicControls:Z

    if-eqz v3, :cond_2

    invoke-virtual {p1}, Landroid/view/KeyEvent;->getKeyCode()I

    move-result v0

    invoke-virtual {p1}, Landroid/view/KeyEvent;->getAction()I

    move-result v3

    if-nez v3, :cond_0

    invoke-direct {p0, v0}, Lcom/android/server/policy/PhoneWindowManager;->handleVolumeLongPress(I)V

    :goto_0
    return v1

    :cond_0
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->handleVolumeLongPressAbort()V

    sget-boolean v3, Lcom/android/server/policy/VolBtnHelper;->mIsVolLongPressed:Z

    if-nez v3, :cond_1

    invoke-static {p1, v1}, Landroid/view/KeyEvent;->changeAction(Landroid/view/KeyEvent;I)Landroid/view/KeyEvent;

    move-result-object v3

    invoke-direct {p0, v3}, Lcom/android/server/policy/PhoneWindowManager;->dispatchDirectAudioEvent(Landroid/view/KeyEvent;)V

    invoke-static {p1, v2}, Landroid/view/KeyEvent;->changeAction(Landroid/view/KeyEvent;I)Landroid/view/KeyEvent;

    move-result-object v3

    invoke-direct {p0, v3}, Lcom/android/server/policy/PhoneWindowManager;->dispatchDirectAudioEvent(Landroid/view/KeyEvent;)V

    :cond_1
    sput-boolean v1, Lcom/android/server/policy/VolBtnHelper;->mIsVolLongPressed:Z

    :cond_2
    move v1, v2

    goto :goto_0
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Service_Legend.mtcr",
    },
    {
        "id":          "add_method_handleVolumeLongPress_I_V",
        "method":      ".method private handleVolumeLongPress(I)V",
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method private handleVolumeLongPress(I)V
    .registers 6

    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    const/16 v0, 0x18

    if-ne p1, v0, :cond_0

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mVolumeUpLongPress:Ljava/lang/Runnable;

    :goto_0
    sget v2, Lcom/android/server/policy/VolBtnHelper;->mVolBtnTimeout:I

    int-to-long v2, v2

    invoke-virtual {v1, v0, v2, v3}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void

    :cond_0
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mVolumeDownLongPress:Ljava/lang/Runnable;

    goto :goto_0
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Service_Legend.mtcr",
    },
    {
        "id":          "add_method_responseToTheCall_Landroid_view_KeyEvent__V",
        "method":      ".method private responseToTheCall(Landroid/view/KeyEvent;)V",
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method private responseToTheCall(Landroid/view/KeyEvent;)V
    .registers 9

    invoke-virtual {p1}, Landroid/view/KeyEvent;->getKeyCode()I

    move-result v2

    const-string v4, "WindowManager"

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "ResponseToTheCall: "

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v4, v5}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->getTelecommService()Landroid/telecom/TelecomManager;

    move-result-object v3

    if-eqz v3, :cond_0

    const/16 v4, 0xa4

    if-ne v2, v4, :cond_1

    invoke-virtual {v3}, Landroid/telecom/TelecomManager;->silenceRinger()V

    :cond_0
    :goto_0
    return-void

    :cond_1
    const/16 v4, 0x18

    if-ne v2, v4, :cond_2

    const-string v1, "answer_from_volume_up_key"

    :goto_1
    iget-object v4, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v4}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v4

    const/4 v5, 0x0

    invoke-static {v4, v1, v5}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    const-string v4, "WindowManager"

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "ResponseToTheCall: "

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v4, v5}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    packed-switch v0, :pswitch_data_0

    goto :goto_0

    :pswitch_0  #0x1
    invoke-virtual {v3}, Landroid/telecom/TelecomManager;->endCall()Z

    goto :goto_0

    :cond_2
    const-string v1, "answer_from_volume_down_key"

    goto :goto_1

    :pswitch_1  #0x2
    invoke-virtual {v3}, Landroid/telecom/TelecomManager;->acceptRingingCall()V

    goto :goto_0

    :pswitch_2  #0x3
    invoke-virtual {v3}, Landroid/telecom/TelecomManager;->silenceRinger()V

    goto :goto_0

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_0  #00000001
        :pswitch_1  #00000002
        :pswitch_2  #00000003
    .end packed-switch
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_createHomeDockIntent__Landroid_content_Intent_",
        "method":      ".method createHomeDockIntent()Landroid/content/Intent;",
        "type":        "method_replace",
        "search": """\
.method createHomeDockIntent()Landroid/content/Intent;
    .registers 7

    const/4 v0, 0x0

    iget v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiMode:I

    const/4 v2, 0x3

    if-ne v1, v2, :cond_0

    iget-boolean v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mEnableCarDockHomeCapture:Z

    if-eqz v1, :cond_5

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mCarDockIntent:Landroid/content/Intent;

    goto :goto_0

    :cond_0
    iget v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiMode:I

    const/4 v3, 0x2

    if-ne v1, v3, :cond_1

    goto :goto_0

    :cond_1
    iget v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiMode:I

    const/4 v3, 0x6

    if-ne v1, v3, :cond_4

    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    invoke-virtual {v1}, Lcom/android/server/wm/DisplayPolicy;->getDockMode()I

    move-result v1

    const/4 v3, 0x1

    if-eq v1, v3, :cond_2

    const/4 v3, 0x4

    if-eq v1, v3, :cond_2

    if-ne v1, v2, :cond_3

    :cond_2
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDeskDockIntent:Landroid/content/Intent;

    :cond_3
    goto :goto_0

    :cond_4
    iget v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiMode:I

    const/4 v2, 0x7

    if-ne v1, v2, :cond_3

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mVrHeadsetHomeIntent:Landroid/content/Intent;

    :cond_5
    :goto_0
    const/4 v1, 0x0

    if-nez v0, :cond_6

    return-object v1

    :cond_6
    const/4 v2, 0x0

    iget-object v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mPackageManager:Landroid/content/pm/PackageManager;

    const v4, 0x10080

    iget v5, p0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    invoke-virtual {v3, v0, v4, v5}, Landroid/content/pm/PackageManager;->resolveActivityAsUser(Landroid/content/Intent;II)Landroid/content/pm/ResolveInfo;

    move-result-object v3

    if-eqz v3, :cond_7

    iget-object v2, v3, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    :cond_7
    if-eqz v2, :cond_8

    iget-object v4, v2, Landroid/content/pm/ActivityInfo;->metaData:Landroid/os/Bundle;

    if-eqz v4, :cond_8

    iget-object v4, v2, Landroid/content/pm/ActivityInfo;->metaData:Landroid/os/Bundle;

    const-string v5, "android.dock_home"

    invoke-virtual {v4, v5}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_8

    new-instance v1, Landroid/content/Intent;

    invoke-direct {v1, v0}, Landroid/content/Intent;-><init>(Landroid/content/Intent;)V

    iget-object v0, v2, Landroid/content/pm/ActivityInfo;->packageName:Ljava/lang/String;

    iget-object v4, v2, Landroid/content/pm/ActivityInfo;->name:Ljava/lang/String;

    invoke-virtual {v1, v0, v4}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    return-object v1

    :cond_8
    return-object v1
.end method
""",
        "replacement": """\
.method createHomeDockIntent()Landroid/content/Intent;
    .registers 7

    goto :goto_2e

    nop

    :goto_0
    iget v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiMode:I

    goto :goto_1a

    nop

    :goto_1
    invoke-virtual {v1, v0, v4}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_8

    nop

    :goto_2
    iget-boolean v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mEnableCarDockHomeCapture:Z

    goto :goto_e

    nop

    :goto_3
    iget-object v0, v2, Landroid/content/pm/ActivityInfo;->packageName:Ljava/lang/String;

    goto :goto_23

    nop

    :goto_4
    iget v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiMode:I

    goto :goto_10

    nop

    :goto_5
    if-nez v2, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_15

    nop

    :goto_6
    if-eq v1, v2, :cond_1

    goto :goto_35

    :cond_1
    goto :goto_2

    nop

    :goto_7
    iget-object v4, v2, Landroid/content/pm/ActivityInfo;->metaData:Landroid/os/Bundle;

    goto :goto_25

    nop

    :goto_8
    return-object v1

    :goto_9
    goto :goto_32

    nop

    :goto_a
    iget-object v2, v3, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    :goto_b
    goto :goto_5

    nop

    :goto_c
    invoke-virtual {v3, v0, v4, v5}, Landroid/content/pm/PackageManager;->resolveActivityAsUser(Landroid/content/Intent;II)Landroid/content/pm/ResolveInfo;

    move-result-object v3

    goto :goto_3c

    nop

    :goto_d
    const/4 v1, 0x0

    goto :goto_39

    nop

    :goto_e
    if-nez v1, :cond_2

    goto :goto_2b

    :cond_2
    goto :goto_3b

    nop

    :goto_f
    const v4, 0x10080

    goto :goto_33

    nop

    :goto_10
    const/4 v2, 0x3

    goto :goto_6

    nop

    :goto_11
    if-nez v4, :cond_3

    goto :goto_9

    :cond_3
    goto :goto_38

    nop

    :goto_12
    iget-object v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mPackageManager:Landroid/content/pm/PackageManager;

    goto :goto_f

    nop

    :goto_13
    if-eq v1, v2, :cond_4

    goto :goto_1e

    :cond_4
    goto :goto_2a

    nop

    :goto_14
    if-eq v1, v3, :cond_5

    goto :goto_17

    :cond_5
    goto :goto_19

    nop

    :goto_15
    iget-object v4, v2, Landroid/content/pm/ActivityInfo;->metaData:Landroid/os/Bundle;

    goto :goto_26

    nop

    :goto_16
    goto :goto_2b

    :goto_17
    goto :goto_0

    nop

    :goto_18
    invoke-direct {v1, v0}, Landroid/content/Intent;-><init>(Landroid/content/Intent;)V

    goto :goto_3

    nop

    :goto_19
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    goto :goto_29

    nop

    :goto_1a
    const/4 v2, 0x7

    goto :goto_13

    nop

    :goto_1b
    goto :goto_2b

    :goto_1c
    goto :goto_36

    nop

    :goto_1d
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDeskDockIntent:Landroid/content/Intent;

    :goto_1e
    goto :goto_16

    nop

    :goto_1f
    const/4 v3, 0x1

    goto :goto_2d

    nop

    :goto_20
    return-object v1

    :goto_21
    goto :goto_2f

    nop

    :goto_22
    if-ne v1, v3, :cond_6

    goto :goto_31

    :cond_6
    goto :goto_30

    nop

    :goto_23
    iget-object v4, v2, Landroid/content/pm/ActivityInfo;->name:Ljava/lang/String;

    goto :goto_1

    nop

    :goto_24
    const/4 v3, 0x2

    goto :goto_27

    nop

    :goto_25
    const-string v5, "android.dock_home"

    goto :goto_28

    nop

    :goto_26
    if-nez v4, :cond_7

    goto :goto_9

    :cond_7
    goto :goto_7

    nop

    :goto_27
    if-eq v1, v3, :cond_8

    goto :goto_1c

    :cond_8
    goto :goto_1b

    nop

    :goto_28
    invoke-virtual {v4, v5}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;)Z

    move-result v4

    goto :goto_11

    nop

    :goto_29
    invoke-virtual {v1}, Lcom/android/server/wm/DisplayPolicy;->getDockMode()I

    move-result v1

    goto :goto_1f

    nop

    :goto_2a
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mVrHeadsetHomeIntent:Landroid/content/Intent;

    :goto_2b
    goto :goto_d

    nop

    :goto_2c
    iget v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiMode:I

    goto :goto_24

    nop

    :goto_2d
    if-ne v1, v3, :cond_9

    goto :goto_31

    :cond_9
    goto :goto_3a

    nop

    :goto_2e
    const/4 v0, 0x0

    goto :goto_4

    nop

    :goto_2f
    const/4 v2, 0x0

    goto :goto_12

    nop

    :goto_30
    if-eq v1, v2, :cond_a

    goto :goto_1e

    :cond_a
    :goto_31
    goto :goto_1d

    nop

    :goto_32
    return-object v1

    :goto_33
    iget v5, p0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    goto :goto_c

    nop

    :goto_34
    goto :goto_2b

    :goto_35
    goto :goto_2c

    nop

    :goto_36
    iget v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiMode:I

    goto :goto_37

    nop

    :goto_37
    const/4 v3, 0x6

    goto :goto_14

    nop

    :goto_38
    new-instance v1, Landroid/content/Intent;

    goto :goto_18

    nop

    :goto_39
    if-eqz v0, :cond_b

    goto :goto_21

    :cond_b
    goto :goto_20

    nop

    :goto_3a
    const/4 v3, 0x4

    goto :goto_22

    nop

    :goto_3b
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mCarDockIntent:Landroid/content/Intent;

    goto :goto_34

    nop

    :goto_3c
    if-nez v3, :cond_c

    goto :goto_b

    :cond_c
    goto :goto_a

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_dispatchMediaKeyRepeatWithWakeLock_Landroid_view_KeyEvent__V",
        "method":      ".method dispatchMediaKeyRepeatWithWakeLock(Landroid/view/KeyEvent;)V",
        "type":        "method_replace",
        "search": """\
.method dispatchMediaKeyRepeatWithWakeLock(Landroid/view/KeyEvent;)V
    .registers 6

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHavePendingMediaKeyRepeatWithWakeLock:Z

    nop

    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v0

    invoke-virtual {p1}, Landroid/view/KeyEvent;->getFlags()I

    move-result v2

    or-int/lit16 v2, v2, 0x80

    const/4 v3, 0x1

    invoke-static {p1, v0, v1, v3, v2}, Landroid/view/KeyEvent;->changeTimeRepeat(Landroid/view/KeyEvent;JII)Landroid/view/KeyEvent;

    move-result-object v0

    sget-boolean v1, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    if-eqz v1, :cond_0

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "dispatchMediaKeyRepeatWithWakeLock: "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v2, "WindowManager"

    invoke-static {v2, v1}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_0
    invoke-virtual {p0, v0}, Lcom/android/server/policy/PhoneWindowManager;->dispatchMediaKeyWithWakeLockToAudioService(Landroid/view/KeyEvent;)V

    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    invoke-virtual {v1}, Landroid/os/PowerManager$WakeLock;->release()V

    return-void
.end method
""",
        "replacement": """\
.method dispatchMediaKeyRepeatWithWakeLock(Landroid/view/KeyEvent;)V
    .registers 6

    goto :goto_7

    nop

    :goto_0
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    goto :goto_3

    nop

    :goto_1
    const/4 v3, 0x1

    goto :goto_11

    nop

    :goto_2
    sget-boolean v1, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    goto :goto_a

    nop

    :goto_3
    const-string v2, "WindowManager"

    goto :goto_8

    nop

    :goto_4
    new-instance v1, Ljava/lang/StringBuilder;

    goto :goto_10

    nop

    :goto_5
    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v0

    goto :goto_12

    nop

    :goto_6
    invoke-virtual {p0, v0}, Lcom/android/server/policy/PhoneWindowManager;->dispatchMediaKeyWithWakeLockToAudioService(Landroid/view/KeyEvent;)V

    goto :goto_e

    nop

    :goto_7
    const/4 v0, 0x0

    goto :goto_d

    nop

    :goto_8
    invoke-static {v2, v1}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_9
    goto :goto_6

    nop

    :goto_a
    if-nez v1, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_4

    nop

    :goto_b
    invoke-virtual {v1}, Landroid/os/PowerManager$WakeLock;->release()V

    goto :goto_14

    nop

    :goto_c
    const-string v2, "dispatchMediaKeyRepeatWithWakeLock: "

    goto :goto_f

    nop

    :goto_d
    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHavePendingMediaKeyRepeatWithWakeLock:Z

    nop

    goto :goto_5

    nop

    :goto_e
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    goto :goto_b

    nop

    :goto_f
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    goto :goto_13

    nop

    :goto_10
    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_c

    nop

    :goto_11
    invoke-static {p1, v0, v1, v3, v2}, Landroid/view/KeyEvent;->changeTimeRepeat(Landroid/view/KeyEvent;JII)Landroid/view/KeyEvent;

    move-result-object v0

    goto :goto_2

    nop

    :goto_12
    invoke-virtual {p1}, Landroid/view/KeyEvent;->getFlags()I

    move-result v2

    goto :goto_15

    nop

    :goto_13
    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v1

    goto :goto_0

    nop

    :goto_14
    return-void

    :goto_15
    or-int/lit16 v2, v2, 0x80

    goto :goto_1

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_dispatchMediaKeyWithWakeLock_Landroid_view_KeyEvent__V",
        "method":      ".method dispatchMediaKeyWithWakeLock(Landroid/view/KeyEvent;)V",
        "type":        "method_replace",
        "search": """\
.method dispatchMediaKeyWithWakeLock(Landroid/view/KeyEvent;)V
    .registers 6

    sget-boolean v0, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    const-string v1, "WindowManager"

    if-eqz v0, :cond_0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "dispatchMediaKeyWithWakeLock: "

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_0
    iget-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHavePendingMediaKeyRepeatWithWakeLock:Z

    const/4 v2, 0x4

    if-eqz v0, :cond_2

    sget-boolean v0, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    if-eqz v0, :cond_1

    const-string v0, "dispatchMediaKeyWithWakeLock: canceled repeat"

    invoke-static {v1, v0}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_1
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    invoke-virtual {v0, v2}, Landroid/os/Handler;->removeMessages(I)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHavePendingMediaKeyRepeatWithWakeLock:Z

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->release()V

    :cond_2
    invoke-virtual {p0, p1}, Lcom/android/server/policy/PhoneWindowManager;->dispatchMediaKeyWithWakeLockToAudioService(Landroid/view/KeyEvent;)V

    invoke-virtual {p1}, Landroid/view/KeyEvent;->getAction()I

    move-result v0

    if-nez v0, :cond_3

    invoke-virtual {p1}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-nez v0, :cond_3

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHavePendingMediaKeyRepeatWithWakeLock:Z

    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    invoke-virtual {v1, v2, p1}, Landroid/os/Handler;->obtainMessage(ILjava/lang/Object;)Landroid/os/Message;

    move-result-object v1

    invoke-virtual {v1, v0}, Landroid/os/Message;->setAsynchronous(Z)V

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    invoke-static {}, Landroid/view/ViewConfiguration;->getKeyRepeatTimeout()I

    move-result v2

    int-to-long v2, v2

    invoke-virtual {v0, v1, v2, v3}, Landroid/os/Handler;->sendMessageDelayed(Landroid/os/Message;J)Z

    goto :goto_0

    :cond_3
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->release()V

    :goto_0
    return-void
.end method
""",
        "replacement": """\
.method dispatchMediaKeyWithWakeLock(Landroid/view/KeyEvent;)V
    .registers 6

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_1d

    nop

    :goto_1
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_11

    nop

    :goto_2
    sget-boolean v0, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    goto :goto_d

    nop

    :goto_3
    if-nez v0, :cond_0

    goto :goto_1c

    :cond_0
    goto :goto_18

    nop

    :goto_4
    invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->release()V

    :goto_5
    goto :goto_10

    nop

    :goto_6
    if-eqz v0, :cond_1

    goto :goto_c

    :cond_1
    goto :goto_a

    nop

    :goto_7
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_1a

    nop

    :goto_8
    invoke-static {}, Landroid/view/ViewConfiguration;->getKeyRepeatTimeout()I

    move-result v2

    goto :goto_2c

    nop

    :goto_9
    sget-boolean v0, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    goto :goto_26

    nop

    :goto_a
    invoke-virtual {p1}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    goto :goto_f

    nop

    :goto_b
    goto :goto_5

    :goto_c
    goto :goto_2d

    nop

    :goto_d
    const-string v1, "WindowManager"

    goto :goto_3

    nop

    :goto_e
    const-string v2, "dispatchMediaKeyWithWakeLock: "

    goto :goto_19

    nop

    :goto_f
    if-eqz v0, :cond_2

    goto :goto_c

    :cond_2
    goto :goto_1e

    nop

    :goto_10
    return-void

    :goto_11
    invoke-virtual {v1, v2, p1}, Landroid/os/Handler;->obtainMessage(ILjava/lang/Object;)Landroid/os/Message;

    move-result-object v1

    goto :goto_20

    nop

    :goto_12
    invoke-virtual {p1}, Landroid/view/KeyEvent;->getAction()I

    move-result v0

    goto :goto_6

    nop

    :goto_13
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    goto :goto_2a

    nop

    :goto_14
    iget-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHavePendingMediaKeyRepeatWithWakeLock:Z

    goto :goto_27

    nop

    :goto_15
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_e

    nop

    :goto_16
    const-string v0, "dispatchMediaKeyWithWakeLock: canceled repeat"

    goto :goto_21

    nop

    :goto_17
    invoke-virtual {v0, v1, v2, v3}, Landroid/os/Handler;->sendMessageDelayed(Landroid/os/Message;J)Z

    goto :goto_b

    nop

    :goto_18
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_15

    nop

    :goto_19
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_0

    nop

    :goto_1a
    invoke-virtual {v0, v2}, Landroid/os/Handler;->removeMessages(I)V

    goto :goto_25

    nop

    :goto_1b
    invoke-static {v1, v0}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_1c
    goto :goto_14

    nop

    :goto_1d
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_1b

    nop

    :goto_1e
    const/4 v0, 0x1

    goto :goto_24

    nop

    :goto_1f
    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHavePendingMediaKeyRepeatWithWakeLock:Z

    goto :goto_13

    nop

    :goto_20
    invoke-virtual {v1, v0}, Landroid/os/Message;->setAsynchronous(Z)V

    goto :goto_28

    nop

    :goto_21
    invoke-static {v1, v0}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_22
    goto :goto_7

    nop

    :goto_23
    invoke-virtual {p0, p1}, Lcom/android/server/policy/PhoneWindowManager;->dispatchMediaKeyWithWakeLockToAudioService(Landroid/view/KeyEvent;)V

    goto :goto_12

    nop

    :goto_24
    iput-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHavePendingMediaKeyRepeatWithWakeLock:Z

    goto :goto_1

    nop

    :goto_25
    const/4 v0, 0x0

    goto :goto_1f

    nop

    :goto_26
    if-nez v0, :cond_3

    goto :goto_22

    :cond_3
    goto :goto_16

    nop

    :goto_27
    const/4 v2, 0x4

    goto :goto_29

    nop

    :goto_28
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_8

    nop

    :goto_29
    if-nez v0, :cond_4

    goto :goto_2b

    :cond_4
    goto :goto_9

    nop

    :goto_2a
    invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->release()V

    :goto_2b
    goto :goto_23

    nop

    :goto_2c
    int-to-long v2, v2

    goto :goto_17

    nop

    :goto_2d
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    goto :goto_4

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_dispatchMediaKeyWithWakeLockToAudioService_Landroid_view_Key",
        "method":      ".method dispatchMediaKeyWithWakeLockToAudioService(Landroid/view/KeyEvent;)V",
        "type":        "method_replace",
        "search": """\
.method dispatchMediaKeyWithWakeLockToAudioService(Landroid/view/KeyEvent;)V
    .registers 4

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mActivityManagerInternal:Landroid/app/ActivityManagerInternal;

    invoke-virtual {v0}, Landroid/app/ActivityManagerInternal;->isSystemReady()Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-static {v0}, Landroid/media/session/MediaSessionLegacyHelper;->getHelper(Landroid/content/Context;)Landroid/media/session/MediaSessionLegacyHelper;

    move-result-object v0

    const/4 v1, 0x1

    invoke-virtual {v0, p1, v1}, Landroid/media/session/MediaSessionLegacyHelper;->sendMediaButtonEvent(Landroid/view/KeyEvent;Z)V

    :cond_0
    return-void
.end method
""",
        "replacement": """\
.method dispatchMediaKeyWithWakeLockToAudioService(Landroid/view/KeyEvent;)V
    .registers 4

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mActivityManagerInternal:Landroid/app/ActivityManagerInternal;

    goto :goto_8

    nop

    :goto_1
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_7

    nop

    :goto_2
    invoke-static {v0}, Landroid/media/session/MediaSessionLegacyHelper;->getHelper(Landroid/content/Context;)Landroid/media/session/MediaSessionLegacyHelper;

    move-result-object v0

    goto :goto_5

    nop

    :goto_3
    invoke-virtual {v0, p1, v1}, Landroid/media/session/MediaSessionLegacyHelper;->sendMediaButtonEvent(Landroid/view/KeyEvent;Z)V

    :goto_4
    goto :goto_6

    nop

    :goto_5
    const/4 v1, 0x1

    goto :goto_3

    nop

    :goto_6
    return-void

    :goto_7
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_2

    nop

    :goto_8
    invoke-virtual {v0}, Landroid/app/ActivityManagerInternal;->isSystemReady()Z

    move-result v0

    goto :goto_1

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getAccessibilityManagerInternal__Lcom_android_server_Accessi",
        "method":      ".method getAccessibilityManagerInternal()Lcom/android/server/AccessibilityManagerInternal;",
        "type":        "method_replace",
        "search": """\
.method getAccessibilityManagerInternal()Lcom/android/server/AccessibilityManagerInternal;
    .registers 3

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mServiceAcquireLock:Ljava/lang/Object;

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAccessibilityManagerInternal:Lcom/android/server/AccessibilityManagerInternal;

    if-nez v1, :cond_0

    const-class v1, Lcom/android/server/AccessibilityManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/AccessibilityManagerInternal;

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAccessibilityManagerInternal:Lcom/android/server/AccessibilityManagerInternal;

    :cond_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAccessibilityManagerInternal:Lcom/android/server/AccessibilityManagerInternal;

    monitor-exit v0

    return-object v1

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method getAccessibilityManagerInternal()Lcom/android/server/AccessibilityManagerInternal;
    .registers 3

    goto :goto_2

    nop

    :goto_0
    throw v1

    :goto_1
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAccessibilityManagerInternal:Lcom/android/server/AccessibilityManagerInternal;

    if-nez v1, :cond_0

    const-class v1, Lcom/android/server/AccessibilityManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/AccessibilityManagerInternal;

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAccessibilityManagerInternal:Lcom/android/server/AccessibilityManagerInternal;

    :cond_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAccessibilityManagerInternal:Lcom/android/server/AccessibilityManagerInternal;

    monitor-exit v0

    return-object v1

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_0

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mServiceAcquireLock:Ljava/lang/Object;

    goto :goto_1

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getAudioManagerInternal__Landroid_media_AudioManagerInternal",
        "method":      ".method getAudioManagerInternal()Landroid/media/AudioManagerInternal;",
        "type":        "method_replace",
        "search": """\
.method getAudioManagerInternal()Landroid/media/AudioManagerInternal;
    .registers 3

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mServiceAcquireLock:Ljava/lang/Object;

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAudioManagerInternal:Landroid/media/AudioManagerInternal;

    if-nez v1, :cond_0

    const-class v1, Landroid/media/AudioManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/media/AudioManagerInternal;

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAudioManagerInternal:Landroid/media/AudioManagerInternal;

    :cond_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAudioManagerInternal:Landroid/media/AudioManagerInternal;

    monitor-exit v0

    return-object v1

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method getAudioManagerInternal()Landroid/media/AudioManagerInternal;
    .registers 3

    goto :goto_2

    nop

    :goto_0
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAudioManagerInternal:Landroid/media/AudioManagerInternal;

    if-nez v1, :cond_0

    const-class v1, Landroid/media/AudioManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/media/AudioManagerInternal;

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAudioManagerInternal:Landroid/media/AudioManagerInternal;

    :cond_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mAudioManagerInternal:Landroid/media/AudioManagerInternal;

    monitor-exit v0

    return-object v1

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1

    nop

    :goto_1
    throw v1

    :goto_2
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mServiceAcquireLock:Ljava/lang/Object;

    goto :goto_0

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getNotificationService__Landroid_app_NotificationManager_",
        "method":      ".method getNotificationService()Landroid/app/NotificationManager;",
        "type":        "method_replace",
        "search": """\
.method getNotificationService()Landroid/app/NotificationManager;
    .registers 3

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    const-class v1, Landroid/app/NotificationManager;

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/app/NotificationManager;

    return-object v0
.end method
""",
        "replacement": """\
.method getNotificationService()Landroid/app/NotificationManager;
    .registers 3

    goto :goto_4

    nop

    :goto_0
    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_3

    nop

    :goto_1
    return-object v0

    :goto_2
    const-class v1, Landroid/app/NotificationManager;

    goto :goto_0

    nop

    :goto_3
    check-cast v0, Landroid/app/NotificationManager;

    goto :goto_1

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_2

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getStatusBarManagerInternal__Lcom_android_server_statusbar_S",
        "method":      ".method getStatusBarManagerInternal()Lcom/android/server/statusbar/StatusBarManagerInternal;",
        "type":        "method_replace",
        "search": """\
.method getStatusBarManagerInternal()Lcom/android/server/statusbar/StatusBarManagerInternal;
    .registers 3

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mServiceAcquireLock:Ljava/lang/Object;

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStatusBarManagerInternal:Lcom/android/server/statusbar/StatusBarManagerInternal;

    if-nez v1, :cond_0

    const-class v1, Lcom/android/server/statusbar/StatusBarManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/statusbar/StatusBarManagerInternal;

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStatusBarManagerInternal:Lcom/android/server/statusbar/StatusBarManagerInternal;

    :cond_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStatusBarManagerInternal:Lcom/android/server/statusbar/StatusBarManagerInternal;

    monitor-exit v0

    return-object v1

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method getStatusBarManagerInternal()Lcom/android/server/statusbar/StatusBarManagerInternal;
    .registers 3

    goto :goto_1

    nop

    :goto_0
    throw v1

    :goto_1
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mServiceAcquireLock:Ljava/lang/Object;

    goto :goto_2

    nop

    :goto_2
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStatusBarManagerInternal:Lcom/android/server/statusbar/StatusBarManagerInternal;

    if-nez v1, :cond_0

    const-class v1, Lcom/android/server/statusbar/StatusBarManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/statusbar/StatusBarManagerInternal;

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStatusBarManagerInternal:Lcom/android/server/statusbar/StatusBarManagerInternal;

    :cond_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStatusBarManagerInternal:Lcom/android/server/statusbar/StatusBarManagerInternal;

    monitor-exit v0

    return-object v1

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_0

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getStatusBarService__Lcom_android_internal_statusbar_IStatus",
        "method":      ".method getStatusBarService()Lcom/android/internal/statusbar/IStatusBarService;",
        "type":        "method_replace",
        "search": """\
.method getStatusBarService()Lcom/android/internal/statusbar/IStatusBarService;
    .registers 3

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mServiceAcquireLock:Ljava/lang/Object;

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStatusBarService:Lcom/android/internal/statusbar/IStatusBarService;

    if-nez v1, :cond_0

    const-string v1, "statusbar"

    invoke-static {v1}, Landroid/os/ServiceManager;->getService(Ljava/lang/String;)Landroid/os/IBinder;

    move-result-object v1

    invoke-static {v1}, Lcom/android/internal/statusbar/IStatusBarService$Stub;->asInterface(Landroid/os/IBinder;)Lcom/android/internal/statusbar/IStatusBarService;

    move-result-object v1

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStatusBarService:Lcom/android/internal/statusbar/IStatusBarService;

    :cond_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStatusBarService:Lcom/android/internal/statusbar/IStatusBarService;

    monitor-exit v0

    return-object v1

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method getStatusBarService()Lcom/android/internal/statusbar/IStatusBarService;
    .registers 3

    goto :goto_1

    nop

    :goto_0
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStatusBarService:Lcom/android/internal/statusbar/IStatusBarService;

    if-nez v1, :cond_0

    const-string v1, "statusbar"

    invoke-static {v1}, Landroid/os/ServiceManager;->getService(Ljava/lang/String;)Landroid/os/IBinder;

    move-result-object v1

    invoke-static {v1}, Lcom/android/internal/statusbar/IStatusBarService$Stub;->asInterface(Landroid/os/IBinder;)Lcom/android/internal/statusbar/IStatusBarService;

    move-result-object v1

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStatusBarService:Lcom/android/internal/statusbar/IStatusBarService;

    :cond_0
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mStatusBarService:Lcom/android/internal/statusbar/IStatusBarService;

    monitor-exit v0

    return-object v1

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_2

    nop

    :goto_1
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mServiceAcquireLock:Ljava/lang/Object;

    goto :goto_0

    nop

    :goto_2
    throw v1
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getTelecommService__Landroid_telecom_TelecomManager_",
        "method":      ".method getTelecommService()Landroid/telecom/TelecomManager;",
        "type":        "method_replace",
        "search": """\
.method getTelecommService()Landroid/telecom/TelecomManager;
    .registers 3

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    const-string v1, "telecom"

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/telecom/TelecomManager;

    return-object v0
.end method
""",
        "replacement": """\
.method getTelecommService()Landroid/telecom/TelecomManager;
    .registers 3

    goto :goto_3

    nop

    :goto_0
    const-string v1, "telecom"

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_2

    nop

    :goto_2
    check-cast v0, Landroid/telecom/TelecomManager;

    goto :goto_4

    nop

    :goto_3
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_0

    nop

    :goto_4
    return-object v0
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_goHome__Z",
        "method":      ".method goHome()Z",
        "type":        "method_replace",
        "search": """\
.method goHome()Z
    .registers 24

    move-object/from16 v1, p0

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->isUserSetupComplete()Z

    move-result v0

    const-string v2, "WindowManager"

    const/4 v3, 0x0

    if-nez v0, :cond_0

    const-string v0, "Not going home because user setup is in progress."

    invoke-static {v2, v0}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v3

    :cond_0
    const/4 v4, 0x1

    :try_start_0
    const-string v0, "persist.sys.uts-test-mode"

    invoke-static {v0, v3}, Landroid/os/SystemProperties;->getInt(Ljava/lang/String;I)I

    move-result v0

    if-ne v0, v4, :cond_1

    const-string v0, "UTS-TEST-MODE"

    invoke-static {v2, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0

    :cond_1
    invoke-static {}, Landroid/app/ActivityManager;->getService()Landroid/app/IActivityManager;

    move-result-object v0

    invoke-interface {v0}, Landroid/app/IActivityManager;->stopAppSwitches()V

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->sendCloseSystemWindows()V

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->createHomeDockIntent()Landroid/content/Intent;

    move-result-object v0

    move-object v9, v0

    if-eqz v9, :cond_2

    invoke-static {}, Landroid/app/ActivityTaskManager;->getService()Landroid/app/IActivityTaskManager;

    move-result-object v5

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getOpPackageName()Ljava/lang/String;

    move-result-object v7

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getAttributionTag()Ljava/lang/String;

    move-result-object v8

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    invoke-virtual {v9, v0}, Landroid/content/Intent;->resolveTypeIfNeeded(Landroid/content/ContentResolver;)Ljava/lang/String;

    move-result-object v10

    const/4 v6, 0x0

    const/4 v11, 0x0

    const/4 v12, 0x0

    const/4 v13, 0x0

    const/4 v14, 0x1

    const/4 v15, 0x0

    const/16 v16, 0x0

    const/16 v17, -0x2

    invoke-interface/range {v5 .. v17}, Landroid/app/IActivityTaskManager;->startActivityAsUser(Landroid/app/IApplicationThread;Ljava/lang/String;Ljava/lang/String;Landroid/content/Intent;Ljava/lang/String;Landroid/os/IBinder;Ljava/lang/String;IILandroid/app/ProfilerInfo;Landroid/os/Bundle;I)I

    move-result v0

    if-ne v0, v4, :cond_2

    return v3

    :cond_2
    :goto_0
    invoke-static {}, Landroid/app/ActivityTaskManager;->getService()Landroid/app/IActivityTaskManager;

    move-result-object v10

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getOpPackageName()Ljava/lang/String;

    move-result-object v12

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getAttributionTag()Ljava/lang/String;

    move-result-object v13

    iget-object v14, v1, Lcom/android/server/policy/PhoneWindowManager;->mHomeIntent:Landroid/content/Intent;

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHomeIntent:Landroid/content/Intent;

    iget-object v2, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/content/Intent;->resolveTypeIfNeeded(Landroid/content/ContentResolver;)Ljava/lang/String;

    move-result-object v15

    const/4 v11, 0x0

    const/16 v16, 0x0

    const/16 v17, 0x0

    const/16 v18, 0x0

    const/16 v19, 0x1

    const/16 v20, 0x0

    const/16 v21, 0x0

    const/16 v22, -0x2

    invoke-interface/range {v10 .. v22}, Landroid/app/IActivityTaskManager;->startActivityAsUser(Landroid/app/IApplicationThread;Ljava/lang/String;Ljava/lang/String;Landroid/content/Intent;Ljava/lang/String;Landroid/os/IBinder;Ljava/lang/String;IILandroid/app/ProfilerInfo;Landroid/os/Bundle;I)I

    move-result v0
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    if-ne v0, v4, :cond_3

    return v3

    :cond_3
    goto :goto_1

    :catch_0
    move-exception v0

    :goto_1
    return v4
.end method
""",
        "replacement": """\
.method goHome()Z
    .registers 24

    goto :goto_c

    nop

    :goto_0
    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->isUserSetupComplete()Z

    move-result v0

    goto :goto_8

    nop

    :goto_1
    if-eqz v0, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_f

    nop

    :goto_2
    invoke-static {v2, v0}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_d

    nop

    :goto_3
    return v4

    :goto_4
    return v3

    :goto_5
    goto :goto_a

    nop

    :goto_6
    const/4 v4, 0x1

    :try_start_0
    const-string v0, "persist.sys.uts-test-mode"

    invoke-static {v0, v3}, Landroid/os/SystemProperties;->getInt(Ljava/lang/String;I)I

    move-result v0

    if-ne v0, v4, :cond_1

    const-string v0, "UTS-TEST-MODE"

    invoke-static {v2, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_7

    :cond_1
    invoke-static {}, Landroid/app/ActivityManager;->getService()Landroid/app/IActivityManager;

    move-result-object v0

    invoke-interface {v0}, Landroid/app/IActivityManager;->stopAppSwitches()V

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->sendCloseSystemWindows()V

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->createHomeDockIntent()Landroid/content/Intent;

    move-result-object v0

    move-object v9, v0

    if-eqz v9, :cond_2

    invoke-static {}, Landroid/app/ActivityTaskManager;->getService()Landroid/app/IActivityTaskManager;

    move-result-object v5

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getOpPackageName()Ljava/lang/String;

    move-result-object v7

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getAttributionTag()Ljava/lang/String;

    move-result-object v8

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    invoke-virtual {v9, v0}, Landroid/content/Intent;->resolveTypeIfNeeded(Landroid/content/ContentResolver;)Ljava/lang/String;

    move-result-object v10

    const/4 v6, 0x0

    const/4 v11, 0x0

    const/4 v12, 0x0

    const/4 v13, 0x0

    const/4 v14, 0x1

    const/4 v15, 0x0

    const/16 v16, 0x0

    const/16 v17, -0x2

    invoke-interface/range {v5 .. v17}, Landroid/app/IActivityTaskManager;->startActivityAsUser(Landroid/app/IApplicationThread;Ljava/lang/String;Ljava/lang/String;Landroid/content/Intent;Ljava/lang/String;Landroid/os/IBinder;Ljava/lang/String;IILandroid/app/ProfilerInfo;Landroid/os/Bundle;I)I

    move-result v0

    if-ne v0, v4, :cond_2

    return v3

    :cond_2
    :goto_7
    invoke-static {}, Landroid/app/ActivityTaskManager;->getService()Landroid/app/IActivityTaskManager;

    move-result-object v10

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getOpPackageName()Ljava/lang/String;

    move-result-object v12

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getAttributionTag()Ljava/lang/String;

    move-result-object v13

    iget-object v14, v1, Lcom/android/server/policy/PhoneWindowManager;->mHomeIntent:Landroid/content/Intent;

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHomeIntent:Landroid/content/Intent;

    iget-object v2, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/content/Intent;->resolveTypeIfNeeded(Landroid/content/ContentResolver;)Ljava/lang/String;

    move-result-object v15

    const/4 v11, 0x0

    const/16 v16, 0x0

    const/16 v17, 0x0

    const/16 v18, 0x0

    const/16 v19, 0x1

    const/16 v20, 0x0

    const/16 v21, 0x0

    const/16 v22, -0x2

    invoke-interface/range {v10 .. v22}, Landroid/app/IActivityTaskManager;->startActivityAsUser(Landroid/app/IApplicationThread;Ljava/lang/String;Ljava/lang/String;Landroid/content/Intent;Ljava/lang/String;Landroid/os/IBinder;Ljava/lang/String;IILandroid/app/ProfilerInfo;Landroid/os/Bundle;I)I

    move-result v0
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_10

    nop

    :goto_8
    const-string v2, "WindowManager"

    goto :goto_9

    nop

    :goto_9
    const/4 v3, 0x0

    goto :goto_1

    nop

    :goto_a
    goto :goto_b

    :catch_0
    move-exception v0

    :goto_b
    goto :goto_3

    nop

    :goto_c
    move-object/from16 v1, p0

    goto :goto_0

    nop

    :goto_d
    return v3

    :goto_e
    goto :goto_6

    nop

    :goto_f
    const-string v0, "Not going home because user setup is in progress."

    goto :goto_2

    nop

    :goto_10
    if-eq v0, v4, :cond_3

    goto :goto_5

    :cond_3
    goto :goto_4

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_handleKeyGestureEvent_Landroid_hardware_input_KeyGestureEven",
        "method":      ".method handleKeyGestureEvent(Landroid/hardware/input/KeyGestureEvent;Landroid/os/IBinder;)V",
        "type":        "method_replace",
        "search": """\
.method handleKeyGestureEvent(Landroid/hardware/input/KeyGestureEvent;Landroid/os/IBinder;)V
    .registers 19

    move-object/from16 v1, p0

    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getAction()I

    move-result v0

    const/4 v2, 0x0

    const/4 v3, 0x1

    if-ne v0, v3, :cond_0

    move v0, v3

    goto :goto_0

    :cond_0
    move v0, v2

    :goto_0
    move v7, v0

    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getAction()I

    move-result v0

    const/4 v4, 0x2

    if-ne v0, v4, :cond_1

    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->isCancelled()Z

    move-result v0

    if-nez v0, :cond_1

    move v0, v3

    goto :goto_1

    :cond_1
    move v0, v2

    :goto_1
    move v8, v0

    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getDeviceId()I

    move-result v5

    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getKeyGestureType()I

    move-result v9

    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getDisplayId()I

    move-result v10

    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getModifierState()I

    move-result v11

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->keyguardOn()Z

    move-result v12

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->isUserSetupComplete()Z

    move-result v0

    if-eqz v0, :cond_2

    if-nez v12, :cond_2

    move v0, v3

    goto :goto_2

    :cond_2
    move v0, v2

    :goto_2
    move v13, v0

    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->isCancelled()Z

    move-result v0

    if-nez v0, :cond_3

    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getKeycodes()[I

    move-result-object v0

    invoke-static {v0}, Ljava/util/Arrays;->stream([I)Ljava/util/stream/IntStream;

    move-result-object v0

    new-instance v6, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda3;

    invoke-direct {v6}, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda3;-><init>()V

    invoke-interface {v0, v6}, Ljava/util/stream/IntStream;->anyMatch(Ljava/util/function/IntPredicate;)Z

    move-result v0

    if-eqz v0, :cond_3

    iput-boolean v3, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerKeyHandled:Z

    :cond_3
    const/4 v0, -0x1

    const/4 v6, 0x0

    const-string v14, "WindowManager"

    sparse-switch v9, :sswitch_data_0

    move-object/from16 v15, p2

    move v3, v5

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "Received a key gesture "

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    move-object/from16 v2, p1

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v4, " that was not registered by this handler"

    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v14, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_7

    :sswitch_0
    if-eqz v8, :cond_4

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mVoiceAccessShortcutController:Lcom/android/server/policy/VoiceAccessShortcutController;

    iget v2, v1, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    invoke-virtual {v0, v2}, Lcom/android/server/policy/VoiceAccessShortcutController;->toggleVoiceAccess(I)Z

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_4
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_1
    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getNotificationService()Landroid/app/NotificationManager;

    move-result-object v0

    if-eqz v0, :cond_7

    invoke-virtual {v0}, Landroid/app/NotificationManager;->getZenMode()I

    move-result v4

    if-eqz v4, :cond_5

    move v4, v3

    goto :goto_3

    :cond_5
    move v4, v2

    :goto_3
    if-eqz v4, :cond_6

    goto :goto_4

    :cond_6
    move v2, v3

    :goto_4
    nop

    const-string v14, "Key gesture DND"

    invoke-virtual {v0, v2, v6, v14, v3}, Landroid/app/NotificationManager;->setZenMode(ILandroid/net/Uri;Ljava/lang/String;Z)V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_7
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_2
    if-eqz v8, :cond_8

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mTalkbackShortcutController:Lcom/android/server/policy/TalkbackShortcutController;

    iget v2, v1, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    sget-object v3, Lcom/android/server/policy/TalkbackShortcutController$ShortcutSource;->KEYBOARD:Lcom/android/server/policy/TalkbackShortcutController$ShortcutSource;

    invoke-virtual {v0, v2, v3}, Lcom/android/server/policy/TalkbackShortcutController;->toggleTalkback(ILcom/android/server/policy/TalkbackShortcutController$ShortcutSource;)Z

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_8
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_3
    if-eqz v8, :cond_9

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->closeSystemDialogs()V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_9
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_4
    if-eqz v8, :cond_a

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mAccessibilityShortcutController:Lcom/android/internal/accessibility/AccessibilityShortcutController;

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardLocked()Z

    move-result v2

    invoke-virtual {v0, v2}, Lcom/android/internal/accessibility/AccessibilityShortcutController;->isAccessibilityShortcutAvailable(Z)Z

    move-result v0

    if-eqz v0, :cond_a

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    iget-object v2, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    const/16 v3, 0x11

    invoke-virtual {v2, v3}, Landroid/os/Handler;->obtainMessage(I)Landroid/os/Message;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_a
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_5
    if-eqz v7, :cond_b

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->interceptBugreportGestureTv()V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_b
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->cancelBugreportGestureTv()V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_6
    if-eqz v7, :cond_c

    const/16 v0, 0x2713

    const-string v2, "KEY_GESTURE_TYPE_GLOBAL_ACTIONS - Global Actions"

    invoke-direct {v1, v0, v2}, Lcom/android/server/policy/PhoneWindowManager;->performHapticFeedback(ILjava/lang/String;)V

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->showGlobalActions()V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_c
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->cancelGlobalActionsAction()V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_7
    if-eqz v7, :cond_d

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->interceptRingerToggleChord()V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_d
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->cancelPendingRingerToggleChordAction()V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_8
    if-eqz v7, :cond_e

    invoke-direct {v1, v3}, Lcom/android/server/policy/PhoneWindowManager;->showRecentApps(Z)V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_e
    invoke-direct {v1, v3, v2}, Lcom/android/server/policy/PhoneWindowManager;->hideRecentApps(ZZ)V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_9
    if-eqz v8, :cond_10

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getStatusBarManagerInternal()Lcom/android/server/statusbar/StatusBarManagerInternal;

    move-result-object v0

    if-eqz v0, :cond_f

    nop

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->getTargetDisplayIdForKeyGestureEvent(Landroid/hardware/input/KeyGestureEvent;)I

    move-result v2

    invoke-interface {v0, v2}, Lcom/android/server/statusbar/StatusBarManagerInternal;->moveFocusedTaskToFullscreen(I)V

    :cond_f
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_10
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_a
    if-eqz v8, :cond_12

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getStatusBarManagerInternal()Lcom/android/server/statusbar/StatusBarManagerInternal;

    move-result-object v0

    if-eqz v0, :cond_11

    nop

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->getTargetDisplayIdForKeyGestureEvent(Landroid/hardware/input/KeyGestureEvent;)I

    move-result v2

    invoke-interface {v0, v2}, Lcom/android/server/statusbar/StatusBarManagerInternal;->moveFocusedTaskToDesktop(I)V

    :cond_11
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_12
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_b
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getAppLaunchData()Landroid/hardware/input/AppLaunchData;

    move-result-object v0

    if-eqz v8, :cond_14

    if-eqz v13, :cond_14

    if-eqz v0, :cond_14

    iget-object v2, v1, Lcom/android/server/policy/PhoneWindowManager;->mModifierShortcutManager:Lcom/android/server/policy/ModifierShortcutManager;

    invoke-virtual {v2, v0}, Lcom/android/server/policy/ModifierShortcutManager;->launchApplication(Landroid/hardware/input/AppLaunchData;)Z

    move-result v2

    if-eqz v2, :cond_13

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->dismissKeyboardShortcutsMenu()V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_13
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_14
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_c
    if-eqz v8, :cond_15

    invoke-virtual {v1, v6}, Lcom/android/server/policy/PhoneWindowManager;->lockNow(Landroid/os/Bundle;)V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_15
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_d
    if-eqz v8, :cond_17

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mEnableBugReportKeyboardShortcut:Z

    if-eqz v0, :cond_17

    :try_start_0
    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mActivityManagerService:Landroid/app/IActivityManager;

    invoke-interface {v0}, Landroid/app/IActivityManager;->launchBugReportHandlerApp()Z

    move-result v0

    if-nez v0, :cond_16

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mActivityManagerService:Landroid/app/IActivityManager;

    invoke-interface {v0}, Landroid/app/IActivityManager;->requestInteractiveBugReport()V
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_5

    :catch_0
    move-exception v0

    const-string v2, "Error taking bugreport"

    invoke-static {v14, v2, v0}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_16
    :goto_5
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_17
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_e
    if-eqz v8, :cond_18

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->getTargetDisplayIdForKeyGestureEvent(Landroid/hardware/input/KeyGestureEvent;)I

    move-result v0

    invoke-direct {v1, v0, v2}, Lcom/android/server/policy/PhoneWindowManager;->moveFocusedTaskToStageSplit(IZ)V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_18
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_f
    if-eqz v8, :cond_19

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->getTargetDisplayIdForKeyGestureEvent(Landroid/hardware/input/KeyGestureEvent;)I

    move-result v0

    invoke-direct {v1, v0, v3}, Lcom/android/server/policy/PhoneWindowManager;->moveFocusedTaskToStageSplit(IZ)V

    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :cond_19
    move-object/from16 v2, p1

    move-object/from16 v15, p2

    move v3, v5

    goto :goto_7

    :sswitch_10
    if-eqz v8, :cond_1b

    and-int/lit16 v2, v11, 0xc1

    if-eqz v2, :cond_1a

    move v3, v0

    :cond_1a
    move-object/from16 v15, p2

    invoke-direct {v1, v10, v15, v3}, Lcom/android/server/policy/PhoneWindowManager;->sendSwitchKeyboardLayout(ILandroid/os/IBinder;I)V

    move-object/from16 v2, p1

    move v3, v5

    goto :goto_7

    :cond_1b
    move-object/from16 v15, p2

    move-object/from16 v2, p1

    move v3, v5

    goto :goto_7

    :sswitch_11
    move-object/from16 v15, p2

    if-eqz v8, :cond_1c

    if-eqz v13, :cond_1c

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->launchTargetSearchActivity()V

    move-object/from16 v2, p1

    move v3, v5

    goto :goto_7

    :cond_1c
    move-object/from16 v2, p1

    move v3, v5

    goto :goto_7

    :sswitch_12
    move-object/from16 v15, p2

    if-eqz v8, :cond_1d

    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getDisplayId()I

    move-result v0

    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getKeycodes()[I

    move-result-object v3

    aget v2, v3, v2

    const-string v3, "launchAllAppsViaA11y"

    invoke-direct {v1, v0, v2, v3}, Lcom/android/server/policy/PhoneWindowManager;->isKeyEventForCurrentUser(IILjava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_1d

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->launchAllAppsAction()V

    move-object/from16 v2, p1

    move v3, v5

    goto :goto_7

    :cond_1d
    move-object/from16 v2, p1

    move v3, v5

    goto :goto_7

    :sswitch_13
    move-object/from16 v15, p2

    if-eqz v8, :cond_1f

    const/16 v2, 0xd

    if-ne v9, v2, :cond_1e

    goto :goto_6

    :cond_1e
    move v3, v0

    :goto_6
    invoke-direct {v1, v10, v3}, Lcom/android/server/policy/PhoneWindowManager;->changeDisplayBrightnessValue(II)V

    move-object/from16 v2, p1

    move v3, v5

    goto :goto_7

    :cond_1f
    move-object/from16 v2, p1

    move v3, v5

    goto :goto_7

    :sswitch_14
    move-object/from16 v15, p2

    if-eqz v8, :cond_20

    invoke-direct {v1, v5}, Lcom/android/server/policy/PhoneWindowManager;->toggleKeyboardShortcutsMenu(I)V

    move-object/from16 v2, p1

    move v3, v5

    goto :goto_7

    :cond_20
    move-object/from16 v2, p1

    move v3, v5

    goto :goto_7

    :sswitch_15
    move-object/from16 v15, p2

    if-eqz v7, :cond_21

    nop

    move v6, v5

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->getScreenshotChordLongPressDelay()J

    move-result-wide v4

    invoke-direct {v1, v3, v4, v5}, Lcom/android/server/policy/PhoneWindowManager;->interceptScreenshotChord(IJ)V

    move-object/from16 v2, p1

    move v3, v6

    goto :goto_7

    :cond_21
    move v6, v5

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->cancelPendingScreenshotChordAction()V

    move-object/from16 v2, p1

    move v3, v6

    goto :goto_7

    :sswitch_16
    move-object/from16 v15, p2

    move v6, v5

    if-eqz v8, :cond_22

    const-wide/16 v2, 0x0

    invoke-direct {v1, v4, v2, v3}, Lcom/android/server/policy/PhoneWindowManager;->interceptScreenshotChord(IJ)V

    move-object/from16 v2, p1

    move v3, v6

    goto :goto_7

    :cond_22
    move-object/from16 v2, p1

    move v3, v6

    goto :goto_7

    :sswitch_17
    move-object/from16 v15, p2

    move v6, v5

    if-eqz v8, :cond_23

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->toggleNotificationPanel()V

    move-object/from16 v2, p1

    move v3, v6

    goto :goto_7

    :cond_23
    move-object/from16 v2, p1

    move v3, v6

    goto :goto_7

    :sswitch_18
    move-object/from16 v15, p2

    move v6, v5

    if-eqz v8, :cond_24

    if-eqz v13, :cond_24

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->showSystemSettings()V

    move-object/from16 v2, p1

    move v3, v6

    goto :goto_7

    :cond_24
    move-object/from16 v2, p1

    move v3, v6

    goto :goto_7

    :sswitch_19
    move-object/from16 v15, p2

    move v6, v5

    if-eqz v8, :cond_25

    if-eqz v13, :cond_25

    nop

    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v4

    const-string v2, "android.intent.extra.ASSIST_INPUT_HINT_KEYBOARD"

    move v3, v6

    const/4 v6, 0x0

    invoke-direct/range {v1 .. v6}, Lcom/android/server/policy/PhoneWindowManager;->launchAssistAction(Ljava/lang/String;IJI)V

    move-object/from16 v2, p1

    goto :goto_7

    :cond_25
    move v3, v6

    move-object/from16 v2, p1

    goto :goto_7

    :sswitch_1a
    move-object/from16 v15, p2

    move v3, v5

    if-nez v12, :cond_28

    if-eqz v7, :cond_26

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->preloadRecentApps()V

    move-object/from16 v2, p1

    goto :goto_7

    :cond_26
    if-eqz v8, :cond_27

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->toggleRecentApps()V

    move-object/from16 v2, p1

    goto :goto_7

    :cond_27
    move-object/from16 v2, p1

    goto :goto_7

    :cond_28
    move-object/from16 v2, p1

    goto :goto_7

    :sswitch_1b
    move-object/from16 v15, p2

    move v3, v5

    if-eqz v8, :cond_29

    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v4

    invoke-direct {v1, v4, v5}, Lcom/android/server/policy/PhoneWindowManager;->injectBackGesture(J)V

    move-object/from16 v2, p1

    goto :goto_7

    :cond_29
    move-object/from16 v2, p1

    goto :goto_7

    :sswitch_1c
    move-object/from16 v15, p2

    move v3, v5

    if-eqz v8, :cond_2a

    invoke-direct {v1, v2}, Lcom/android/server/policy/PhoneWindowManager;->showRecentApps(Z)V

    move-object/from16 v2, p1

    goto :goto_7

    :cond_2a
    move-object/from16 v2, p1

    goto :goto_7

    :sswitch_1d
    move-object/from16 v15, p2

    move v3, v5

    if-eqz v8, :cond_2b

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    new-instance v2, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda4;

    invoke-direct {v2, v1, v10}, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda4;-><init>(Lcom/android/server/policy/PhoneWindowManager;I)V

    invoke-virtual {v0, v2}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    move-object/from16 v2, p1

    goto :goto_7

    :cond_2b
    move-object/from16 v2, p1

    :goto_7
    return-void

    nop

    :sswitch_data_0
    .sparse-switch
        0x1 -> :sswitch_1d
        0x2 -> :sswitch_1c
        0x3 -> :sswitch_1b
        0x4 -> :sswitch_1a
        0x5 -> :sswitch_19
        0x6 -> :sswitch_19
        0x7 -> :sswitch_18
        0x8 -> :sswitch_17
        0xa -> :sswitch_16
        0xb -> :sswitch_15
        0xc -> :sswitch_14
        0xd -> :sswitch_13
        0xe -> :sswitch_13
        0x15 -> :sswitch_12
        0x16 -> :sswitch_11
        0x17 -> :sswitch_10
        0x1b -> :sswitch_f
        0x1c -> :sswitch_e
        0x1f -> :sswitch_d
        0x20 -> :sswitch_c
        0x33 -> :sswitch_b
        0x34 -> :sswitch_a
        0x35 -> :sswitch_9
        0x36 -> :sswitch_8
        0x38 -> :sswitch_7
        0x39 -> :sswitch_6
        0x3b -> :sswitch_5
        0x3c -> :sswitch_4
        0x3d -> :sswitch_3
        0x3f -> :sswitch_2
        0x4b -> :sswitch_1
        0x4c -> :sswitch_0
    .end sparse-switch
.end method
""",
        "replacement": """\
.method handleKeyGestureEvent(Landroid/hardware/input/KeyGestureEvent;Landroid/os/IBinder;)V
    .registers 19

    goto :goto_83

    nop

    :goto_0
    if-nez v7, :cond_0

    goto :goto_131

    :cond_0
    nop

    goto :goto_69

    nop

    :goto_1
    move-object/from16 v2, p1

    goto :goto_109

    nop

    :goto_2
    move-object/from16 v15, p2

    goto :goto_12e

    nop

    :goto_3
    move-object/from16 v2, p1

    goto :goto_b

    nop

    :goto_4
    move-object/from16 v2, p1

    goto :goto_c

    nop

    :goto_5
    move-object/from16 v2, p1

    goto :goto_160

    nop

    :goto_6
    move v3, v6

    goto :goto_a9

    nop

    :goto_7
    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->isUserSetupComplete()Z

    move-result v0

    goto :goto_2e

    nop

    :goto_8
    invoke-direct {v1, v0, v2, v3}, Lcom/android/server/policy/PhoneWindowManager;->isKeyEventForCurrentUser(IILjava/lang/String;)Z

    move-result v0

    goto :goto_13

    nop

    :goto_9
    move-object/from16 v15, p2

    goto :goto_40

    nop

    :goto_a
    invoke-direct {v1, v4, v2, v3}, Lcom/android/server/policy/PhoneWindowManager;->interceptScreenshotChord(IJ)V

    goto :goto_162

    nop

    :goto_b
    move v3, v5

    goto :goto_126

    nop

    :goto_c
    move-object/from16 v15, p2

    goto :goto_19a

    nop

    :goto_d
    if-nez v7, :cond_1

    goto :goto_170

    :cond_1
    goto :goto_c4

    nop

    :goto_e
    if-nez v8, :cond_2

    goto :goto_d1

    :cond_2
    goto :goto_46

    nop

    :goto_f
    if-nez v0, :cond_3

    goto :goto_3d

    :cond_3
    :try_start_0
    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mActivityManagerService:Landroid/app/IActivityManager;

    invoke-interface {v0}, Landroid/app/IActivityManager;->launchBugReportHandlerApp()Z

    move-result v0

    if-nez v0, :cond_19

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mActivityManagerService:Landroid/app/IActivityManager;

    invoke-interface {v0}, Landroid/app/IActivityManager;->requestInteractiveBugReport()V
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_8f

    nop

    :goto_10
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getKeyGestureType()I

    move-result v9

    goto :goto_d2

    nop

    :goto_11
    goto :goto_1ac

    :goto_12
    goto :goto_139

    nop

    :goto_13
    if-nez v0, :cond_4

    goto :goto_1c3

    :cond_4
    goto :goto_87

    nop

    :goto_14
    const-string v14, "Key gesture DND"

    goto :goto_1de

    nop

    :goto_15
    move-object/from16 v2, p1

    goto :goto_18f

    nop

    :goto_16
    move v3, v5

    goto :goto_23

    nop

    :goto_17
    if-nez v0, :cond_5

    goto :goto_148

    :cond_5
    goto :goto_147

    nop

    :goto_18
    move-object/from16 v2, p1

    goto :goto_38

    nop

    :goto_19
    move-object/from16 v2, p1

    goto :goto_b6

    nop

    :goto_1a
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getKeycodes()[I

    move-result-object v3

    goto :goto_196

    nop

    :goto_1b
    goto :goto_1ac

    :goto_1c
    goto :goto_1

    nop

    :goto_1d
    const/16 v0, 0x2713

    goto :goto_1a9

    nop

    :goto_1e
    move v3, v5

    goto :goto_182

    nop

    :goto_1f
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getDeviceId()I

    move-result v5

    goto :goto_10

    nop

    :goto_20
    if-nez v8, :cond_6

    goto :goto_ac

    :cond_6
    goto :goto_e1

    nop

    :goto_21
    move-object/from16 v2, p1

    goto :goto_a2

    nop

    :goto_22
    move v3, v5

    goto :goto_12f

    nop

    :goto_23
    goto :goto_1ac

    :sswitch_0
    goto :goto_142

    nop

    :goto_24
    move v3, v6

    goto :goto_187

    nop

    :goto_25
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->cancelPendingScreenshotChordAction()V

    goto :goto_dd

    nop

    :goto_26
    goto :goto_1ac

    :sswitch_1
    goto :goto_149

    nop

    :goto_27
    if-eq v0, v3, :cond_7

    goto :goto_5a

    :cond_7
    goto :goto_1cd

    nop

    :goto_28
    move-object/from16 v2, p1

    goto :goto_47

    nop

    :goto_29
    move-object/from16 v2, p1

    goto :goto_1b8

    nop

    :goto_2a
    invoke-virtual {v2, v0}, Lcom/android/server/policy/ModifierShortcutManager;->launchApplication(Landroid/hardware/input/AppLaunchData;)Z

    move-result v2

    goto :goto_15f

    nop

    :goto_2b
    goto :goto_1ac

    :sswitch_2
    goto :goto_132

    nop

    :goto_2c
    new-instance v2, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda4;

    goto :goto_1b5

    nop

    :goto_2d
    move-object/from16 v15, p2

    goto :goto_1cb

    nop

    :goto_2e
    if-nez v0, :cond_8

    goto :goto_ae

    :cond_8
    goto :goto_145

    nop

    :goto_2f
    move v6, v5

    goto :goto_137

    nop

    :goto_30
    move v3, v5

    goto :goto_185

    nop

    :goto_31
    move-object/from16 v2, p1

    goto :goto_19c

    nop

    :goto_32
    goto :goto_1ac

    :sswitch_3
    goto :goto_6b

    nop

    :goto_33
    invoke-direct {v1, v10, v15, v3}, Lcom/android/server/policy/PhoneWindowManager;->sendSwitchKeyboardLayout(ILandroid/os/IBinder;I)V

    goto :goto_15

    nop

    :goto_34
    invoke-direct {v1, v0, v3}, Lcom/android/server/policy/PhoneWindowManager;->moveFocusedTaskToStageSplit(IZ)V

    goto :goto_1af

    nop

    :goto_35
    const-wide/16 v2, 0x0

    goto :goto_a

    nop

    :goto_36
    goto :goto_1ac

    :goto_37
    goto :goto_71

    nop

    :goto_38
    move v3, v6

    goto :goto_130

    nop

    :goto_39
    move v3, v5

    goto :goto_a3

    nop

    :goto_3a
    move-object/from16 v15, p2

    goto :goto_1c4

    nop

    :goto_3b
    if-nez v8, :cond_9

    goto :goto_1c

    :cond_9
    goto :goto_76

    nop

    :goto_3c
    goto :goto_1ac

    :goto_3d
    goto :goto_d8

    nop

    :goto_3e
    goto :goto_1ac

    :goto_3f
    goto :goto_6c

    nop

    :goto_40
    move v3, v5

    goto :goto_154

    nop

    :goto_41
    const-string v2, "Error taking bugreport"

    goto :goto_de

    nop

    :goto_42
    move-object/from16 v2, p1

    goto :goto_158

    nop

    :goto_43
    invoke-interface {v0, v6}, Ljava/util/stream/IntStream;->anyMatch(Ljava/util/function/IntPredicate;)Z

    move-result v0

    goto :goto_17

    nop

    :goto_44
    if-nez v0, :cond_a

    goto :goto_f8

    :cond_a
    nop

    goto :goto_1c8

    nop

    :goto_45
    goto :goto_1ac

    :sswitch_4
    goto :goto_fc

    nop

    :goto_46
    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mTalkbackShortcutController:Lcom/android/server/policy/TalkbackShortcutController;

    goto :goto_1a0

    nop

    :goto_47
    move v3, v6

    goto :goto_3e

    nop

    :goto_48
    invoke-static {v0}, Ljava/util/Arrays;->stream([I)Ljava/util/stream/IntStream;

    move-result-object v0

    goto :goto_66

    nop

    :goto_49
    move-object/from16 v15, p2

    goto :goto_f9

    nop

    :goto_4a
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->cancelBugreportGestureTv()V

    goto :goto_a1

    nop

    :goto_4b
    move-object/from16 v15, p2

    goto :goto_17d

    nop

    :goto_4c
    move-object/from16 v2, p1

    goto :goto_b1

    nop

    :goto_4d
    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_14c

    nop

    :goto_4e
    const/4 v6, 0x0

    goto :goto_115

    nop

    :goto_4f
    move-object/from16 v15, p2

    goto :goto_f0

    nop

    :goto_50
    move v3, v5

    goto :goto_c1

    nop

    :goto_51
    if-nez v8, :cond_b

    goto :goto_9c

    :cond_b
    goto :goto_102

    nop

    :goto_52
    const/4 v2, 0x0

    goto :goto_7b

    nop

    :goto_53
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_96

    nop

    :goto_54
    goto :goto_1ac

    :goto_55
    goto :goto_85

    nop

    :goto_56
    move-object/from16 v2, p1

    goto :goto_8a

    nop

    :goto_57
    move v6, v5

    goto :goto_f1

    nop

    :goto_58
    return-void

    :sswitch_data_0
    .sparse-switch
        0x1 -> :sswitch_16
        0x2 -> :sswitch_14
        0x3 -> :sswitch_17
        0x4 -> :sswitch_11
        0x5 -> :sswitch_b
        0x6 -> :sswitch_b
        0x7 -> :sswitch_a
        0x8 -> :sswitch_4
        0xa -> :sswitch_9
        0xb -> :sswitch_0
        0xc -> :sswitch_13
        0xd -> :sswitch_15
        0xe -> :sswitch_15
        0x15 -> :sswitch_1
        0x16 -> :sswitch_1b
        0x17 -> :sswitch_c
        0x1b -> :sswitch_6
        0x1c -> :sswitch_8
        0x1f -> :sswitch_7
        0x20 -> :sswitch_12
        0x33 -> :sswitch_e
        0x34 -> :sswitch_1a
        0x35 -> :sswitch_18
        0x36 -> :sswitch_5
        0x38 -> :sswitch_19
        0x39 -> :sswitch_10
        0x3b -> :sswitch_3
        0x3c -> :sswitch_f
        0x3d -> :sswitch_2
        0x3f -> :sswitch_1c
        0x4b -> :sswitch_d
        0x4c -> :sswitch_1d
    .end sparse-switch

    :goto_59
    goto :goto_15d

    :goto_5a
    goto :goto_15c

    nop

    :goto_5b
    move v3, v5

    goto :goto_54

    nop

    :goto_5c
    const-string v4, " that was not registered by this handler"

    goto :goto_10a

    nop

    :goto_5d
    goto :goto_1ac

    :goto_5e
    goto :goto_cf

    nop

    :goto_5f
    move-object/from16 v2, p1

    goto :goto_a8

    nop

    :goto_60
    move v3, v5

    goto :goto_104

    nop

    :goto_61
    move-object/from16 v2, p1

    goto :goto_134

    nop

    :goto_62
    goto :goto_1ac

    :goto_63
    goto :goto_5

    nop

    :goto_64
    move-object/from16 v2, p1

    goto :goto_15b

    nop

    :goto_65
    move-object/from16 v2, p1

    goto :goto_49

    nop

    :goto_66
    new-instance v6, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda3;

    goto :goto_b7

    nop

    :goto_67
    if-nez v8, :cond_c

    goto :goto_1c3

    :cond_c
    goto :goto_b5

    nop

    :goto_68
    goto :goto_1ac

    :sswitch_5
    goto :goto_97

    nop

    :goto_69
    move v6, v5

    goto :goto_14a

    nop

    :goto_6a
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getKeycodes()[I

    move-result-object v0

    goto :goto_48

    nop

    :goto_6b
    if-nez v7, :cond_d

    goto :goto_180

    :cond_d
    goto :goto_1b0

    nop

    :goto_6c
    move-object/from16 v2, p1

    goto :goto_1df

    nop

    :goto_6d
    invoke-direct {v1, v10, v3}, Lcom/android/server/policy/PhoneWindowManager;->changeDisplayBrightnessValue(II)V

    goto :goto_163

    nop

    :goto_6e
    move-object/from16 v15, p2

    goto :goto_8b

    nop

    :goto_6f
    if-nez v8, :cond_e

    goto :goto_14f

    :cond_e
    goto :goto_ed

    nop

    :goto_70
    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getNotificationService()Landroid/app/NotificationManager;

    move-result-object v0

    goto :goto_11b

    nop

    :goto_71
    move-object/from16 v2, p1

    goto :goto_1d5

    nop

    :goto_72
    goto :goto_1ac

    :goto_73
    goto :goto_10b

    nop

    :goto_74
    move-object/from16 v15, p2

    goto :goto_ca

    nop

    :goto_75
    move-object/from16 v15, p2

    goto :goto_22

    nop

    :goto_76
    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->getTargetDisplayIdForKeyGestureEvent(Landroid/hardware/input/KeyGestureEvent;)I

    move-result v0

    goto :goto_ef

    nop

    :goto_77
    move-object/from16 v2, p1

    goto :goto_1a4

    nop

    :goto_78
    goto :goto_1ac

    :sswitch_6
    goto :goto_51

    nop

    :goto_79
    move-object/from16 v2, p1

    goto :goto_199

    nop

    :goto_7a
    if-nez v8, :cond_f

    goto :goto_1c1

    :cond_f
    goto :goto_9e

    nop

    :goto_7b
    const/4 v3, 0x1

    goto :goto_27

    nop

    :goto_7c
    move-object/from16 v2, p1

    goto :goto_ce

    nop

    :goto_7d
    goto :goto_1ac

    :sswitch_7
    goto :goto_1d7

    nop

    :goto_7e
    move-object/from16 v15, p2

    goto :goto_167

    nop

    :goto_7f
    invoke-interface {v0, v2}, Lcom/android/server/statusbar/StatusBarManagerInternal;->moveFocusedTaskToDesktop(I)V

    :goto_80
    goto :goto_cc

    nop

    :goto_81
    goto :goto_1ac

    :goto_82
    goto :goto_42

    nop

    :goto_83
    move-object/from16 v1, p0

    goto :goto_19b

    nop

    :goto_84
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->launchTargetSearchActivity()V

    goto :goto_155

    nop

    :goto_85
    invoke-direct {v1, v3, v2}, Lcom/android/server/policy/PhoneWindowManager;->hideRecentApps(ZZ)V

    goto :goto_c0

    nop

    :goto_86
    invoke-virtual {v0, v2, v3}, Lcom/android/server/policy/TalkbackShortcutController;->toggleTalkback(ILcom/android/server/policy/TalkbackShortcutController$ShortcutSource;)Z

    goto :goto_5f

    nop

    :goto_87
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->launchAllAppsAction()V

    goto :goto_8c

    nop

    :goto_88
    invoke-virtual {v0, v2}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    goto :goto_aa

    nop

    :goto_89
    invoke-direct {v1, v0, v2}, Lcom/android/server/policy/PhoneWindowManager;->performHapticFeedback(ILjava/lang/String;)V

    goto :goto_e3

    nop

    :goto_8a
    move v3, v5

    goto :goto_15a

    nop

    :goto_8b
    move v3, v5

    goto :goto_16f

    nop

    :goto_8c
    move-object/from16 v2, p1

    goto :goto_18c

    nop

    :goto_8d
    if-nez v8, :cond_10

    goto :goto_bb

    :cond_10
    goto :goto_e0

    nop

    :goto_8e
    move v8, v0

    goto :goto_1f

    nop

    :goto_8f
    goto :goto_df

    :catch_0
    move-exception v0

    goto :goto_41

    nop

    :goto_90
    move-object/from16 v2, p1

    goto :goto_9

    nop

    :goto_91
    goto :goto_e9

    :goto_92
    goto :goto_e8

    nop

    :goto_93
    move-object/from16 v15, p2

    goto :goto_143

    nop

    :goto_94
    move-object/from16 v2, p1

    goto :goto_1d1

    nop

    :goto_95
    move-object/from16 v15, p2

    goto :goto_168

    nop

    :goto_96
    const-string v2, "Received a key gesture "

    goto :goto_1c5

    nop

    :goto_97
    if-nez v7, :cond_11

    goto :goto_55

    :cond_11
    goto :goto_194

    nop

    :goto_98
    invoke-direct {v1, v2}, Lcom/android/server/policy/PhoneWindowManager;->showRecentApps(Z)V

    goto :goto_bc

    nop

    :goto_99
    move-object/from16 v2, p1

    goto :goto_1bc

    nop

    :goto_9a
    if-nez v7, :cond_12

    goto :goto_5e

    :cond_12
    goto :goto_a0

    nop

    :goto_9b
    goto :goto_1ac

    :goto_9c
    goto :goto_cd

    nop

    :goto_9d
    move-object/from16 v15, p2

    goto :goto_af

    nop

    :goto_9e
    if-nez v13, :cond_13

    goto :goto_1c1

    :cond_13
    goto :goto_1ce

    nop

    :goto_9f
    if-nez v8, :cond_14

    goto :goto_135

    :cond_14
    goto :goto_136

    nop

    :goto_a0
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->preloadRecentApps()V

    goto :goto_117

    nop

    :goto_a1
    move-object/from16 v2, p1

    goto :goto_2d

    nop

    :goto_a2
    move v3, v6

    goto :goto_62

    nop

    :goto_a3
    goto :goto_1ac

    :goto_a4
    goto :goto_133

    nop

    :goto_a5
    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mVoiceAccessShortcutController:Lcom/android/server/policy/VoiceAccessShortcutController;

    goto :goto_161

    nop

    :goto_a6
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->toggleRecentApps()V

    goto :goto_1c9

    nop

    :goto_a7
    goto :goto_1ac

    :sswitch_8
    goto :goto_3b

    nop

    :goto_a8
    move-object/from16 v15, p2

    goto :goto_f3

    nop

    :goto_a9
    goto :goto_1ac

    :sswitch_9
    goto :goto_e2

    nop

    :goto_aa
    move-object/from16 v2, p1

    goto :goto_d9

    nop

    :goto_ab
    goto :goto_1ac

    :goto_ac
    goto :goto_99

    nop

    :goto_ad
    goto :goto_114

    :goto_ae
    goto :goto_113

    nop

    :goto_af
    move v3, v5

    goto :goto_e6

    nop

    :goto_b0
    if-eqz v0, :cond_15

    goto :goto_1dd

    :cond_15
    goto :goto_16c

    nop

    :goto_b1
    move-object/from16 v15, p2

    goto :goto_150

    nop

    :goto_b2
    move v3, v5

    goto :goto_16a

    nop

    :goto_b3
    if-nez v8, :cond_16

    goto :goto_18b

    :cond_16
    goto :goto_11f

    nop

    :goto_b4
    move v3, v5

    goto :goto_36

    nop

    :goto_b5
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getDisplayId()I

    move-result v0

    goto :goto_1a

    nop

    :goto_b6
    move-object/from16 v15, p2

    goto :goto_128

    nop

    :goto_b7
    invoke-direct {v6}, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda3;-><init>()V

    goto :goto_43

    nop

    :goto_b8
    goto :goto_1ac

    :sswitch_a
    goto :goto_1b2

    nop

    :goto_b9
    goto :goto_1ac

    :sswitch_b
    goto :goto_184

    nop

    :goto_ba
    goto :goto_1ac

    :goto_bb
    goto :goto_183

    nop

    :goto_bc
    move-object/from16 v2, p1

    goto :goto_1a2

    nop

    :goto_bd
    move-object/from16 v2, p1

    goto :goto_74

    nop

    :goto_be
    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mAccessibilityShortcutController:Lcom/android/internal/accessibility/AccessibilityShortcutController;

    goto :goto_108

    nop

    :goto_bf
    move v13, v0

    goto :goto_105

    nop

    :goto_c0
    move-object/from16 v2, p1

    goto :goto_15e

    nop

    :goto_c1
    if-nez v8, :cond_17

    goto :goto_1a3

    :cond_17
    goto :goto_98

    nop

    :goto_c2
    invoke-direct {v1, v4, v5}, Lcom/android/server/policy/PhoneWindowManager;->injectBackGesture(J)V

    goto :goto_11e

    nop

    :goto_c3
    invoke-virtual {v0, v2}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z

    goto :goto_94

    nop

    :goto_c4
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->interceptRingerToggleChord()V

    goto :goto_10d

    nop

    :goto_c5
    move-object/from16 v15, p2

    goto :goto_1e0

    nop

    :goto_c6
    move v3, v5

    goto :goto_120

    nop

    :goto_c7
    move-object/from16 v15, p2

    goto :goto_f4

    nop

    :goto_c8
    move v3, v5

    goto :goto_198

    nop

    :goto_c9
    move-object/from16 v2, p1

    goto :goto_95

    nop

    :goto_ca
    move v3, v5

    goto :goto_1c0

    nop

    :goto_cb
    move-object/from16 v2, p1

    goto :goto_173

    nop

    :goto_cc
    move-object/from16 v2, p1

    goto :goto_2

    nop

    :goto_cd
    move-object/from16 v2, p1

    goto :goto_9d

    nop

    :goto_ce
    move v3, v5

    goto :goto_190

    nop

    :goto_cf
    if-nez v8, :cond_18

    goto :goto_16e

    :cond_18
    goto :goto_a6

    nop

    :goto_d0
    goto :goto_1ac

    :goto_d1
    goto :goto_65

    nop

    :goto_d2
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getDisplayId()I

    move-result v10

    goto :goto_138

    nop

    :goto_d3
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getAction()I

    move-result v0

    goto :goto_197

    nop

    :goto_d4
    move-object/from16 v15, p2

    goto :goto_30

    nop

    :goto_d5
    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v4

    goto :goto_c2

    nop

    :goto_d6
    move v3, v0

    :goto_d7
    goto :goto_fa

    nop

    :goto_d8
    move-object/from16 v2, p1

    goto :goto_116

    nop

    :goto_d9
    goto :goto_1ac

    :goto_da
    goto :goto_1ab

    nop

    :goto_db
    move v0, v3

    goto :goto_ad

    nop

    :goto_dc
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getAppLaunchData()Landroid/hardware/input/AppLaunchData;

    move-result-object v0

    goto :goto_7a

    nop

    :goto_dd
    move-object/from16 v2, p1

    goto :goto_6

    nop

    :goto_de
    invoke-static {v14, v2, v0}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_19
    :goto_df
    goto :goto_106

    nop

    :goto_e0
    if-nez v13, :cond_1a

    goto :goto_bb

    :cond_1a
    goto :goto_84

    nop

    :goto_e1
    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getStatusBarManagerInternal()Lcom/android/server/statusbar/StatusBarManagerInternal;

    move-result-object v0

    goto :goto_44

    nop

    :goto_e2
    move-object/from16 v15, p2

    goto :goto_57

    nop

    :goto_e3
    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->showGlobalActions()V

    goto :goto_181

    nop

    :goto_e4
    if-nez v0, :cond_1b

    goto :goto_80

    :cond_1b
    nop

    goto :goto_101

    nop

    :goto_e5
    move v3, v5

    goto :goto_a7

    nop

    :goto_e6
    goto :goto_1ac

    :sswitch_c
    goto :goto_107

    nop

    :goto_e7
    move-object/from16 v15, p2

    goto :goto_156

    nop

    :goto_e8
    move v3, v0

    :goto_e9
    goto :goto_6d

    nop

    :goto_ea
    move-object/from16 v2, p1

    goto :goto_16

    nop

    :goto_eb
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_5c

    nop

    :goto_ec
    move v3, v6

    goto :goto_45

    nop

    :goto_ed
    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getStatusBarManagerInternal()Lcom/android/server/statusbar/StatusBarManagerInternal;

    move-result-object v0

    goto :goto_e4

    nop

    :goto_ee
    move-object/from16 v15, p2

    goto :goto_b3

    nop

    :goto_ef
    invoke-direct {v1, v0, v2}, Lcom/android/server/policy/PhoneWindowManager;->moveFocusedTaskToStageSplit(IZ)V

    goto :goto_77

    nop

    :goto_f0
    move v3, v5

    goto :goto_3c

    nop

    :goto_f1
    if-nez v8, :cond_1c

    goto :goto_73

    :cond_1c
    goto :goto_35

    nop

    :goto_f2
    move v6, v5

    goto :goto_153

    nop

    :goto_f3
    move v3, v5

    goto :goto_d0

    nop

    :goto_f4
    move v3, v5

    goto :goto_ab

    nop

    :goto_f5
    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_103

    nop

    :goto_f6
    move-object/from16 v2, p1

    goto :goto_c7

    nop

    :goto_f7
    invoke-interface {v0, v2}, Lcom/android/server/statusbar/StatusBarManagerInternal;->moveFocusedTaskToFullscreen(I)V

    :goto_f8
    goto :goto_f6

    nop

    :goto_f9
    move v3, v5

    goto :goto_2b

    nop

    :goto_fa
    move-object/from16 v15, p2

    goto :goto_33

    nop

    :goto_fb
    const/4 v0, -0x1

    goto :goto_12a

    nop

    :goto_fc
    move-object/from16 v15, p2

    goto :goto_f2

    nop

    :goto_fd
    goto :goto_1ac

    :goto_fe
    goto :goto_1aa

    nop

    :goto_ff
    invoke-virtual {v0, v2}, Lcom/android/internal/accessibility/AccessibilityShortcutController;->isAccessibilityShortcutAvailable(Z)Z

    move-result v0

    goto :goto_10e

    nop

    :goto_100
    move v3, v5

    goto :goto_1b3

    nop

    :goto_101
    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->getTargetDisplayIdForKeyGestureEvent(Landroid/hardware/input/KeyGestureEvent;)I

    move-result v2

    goto :goto_7f

    nop

    :goto_102
    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->getTargetDisplayIdForKeyGestureEvent(Landroid/hardware/input/KeyGestureEvent;)I

    move-result v0

    goto :goto_34

    nop

    :goto_103
    invoke-virtual {v0}, Landroid/content/Context;->closeSystemDialogs()V

    goto :goto_4c

    nop

    :goto_104
    goto :goto_1ac

    :sswitch_d
    goto :goto_70

    nop

    :goto_105
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->isCancelled()Z

    move-result v0

    goto :goto_125

    nop

    :goto_106
    move-object/from16 v2, p1

    goto :goto_4f

    nop

    :goto_107
    if-nez v8, :cond_1d

    goto :goto_fe

    :cond_1d
    goto :goto_13f

    nop

    :goto_108
    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardLocked()Z

    move-result v2

    goto :goto_ff

    nop

    :goto_109
    move-object/from16 v15, p2

    goto :goto_1bf

    nop

    :goto_10a
    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_191

    nop

    :goto_10b
    move-object/from16 v2, p1

    goto :goto_ec

    nop

    :goto_10c
    move v3, v5

    goto :goto_179

    nop

    :goto_10d
    move-object/from16 v2, p1

    goto :goto_6e

    nop

    :goto_10e
    if-nez v0, :cond_1e

    goto :goto_a4

    :cond_1e
    goto :goto_4d

    nop

    :goto_10f
    move-object/from16 v15, p2

    goto :goto_c6

    nop

    :goto_110
    iget-object v2, v1, Lcom/android/server/policy/PhoneWindowManager;->mModifierShortcutManager:Lcom/android/server/policy/ModifierShortcutManager;

    goto :goto_2a

    nop

    :goto_111
    invoke-static {v14, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1d3

    nop

    :goto_112
    invoke-virtual {v0}, Landroid/app/NotificationManager;->getZenMode()I

    move-result v4

    goto :goto_1cc

    nop

    :goto_113
    move v0, v2

    :goto_114
    goto :goto_bf

    nop

    :goto_115
    invoke-direct/range {v1 .. v6}, Lcom/android/server/policy/PhoneWindowManager;->launchAssistAction(Ljava/lang/String;IJI)V

    goto :goto_61

    nop

    :goto_116
    move-object/from16 v15, p2

    goto :goto_e5

    nop

    :goto_117
    move-object/from16 v2, p1

    goto :goto_5d

    nop

    :goto_118
    if-eq v9, v2, :cond_1f

    goto :goto_92

    :cond_1f
    goto :goto_91

    nop

    :goto_119
    if-nez v7, :cond_20

    goto :goto_16b

    :cond_20
    goto :goto_1d

    nop

    :goto_11a
    move v7, v0

    goto :goto_d3

    nop

    :goto_11b
    if-nez v0, :cond_21

    goto :goto_37

    :cond_21
    goto :goto_112

    nop

    :goto_11c
    invoke-direct {v1, v3, v4, v5}, Lcom/android/server/policy/PhoneWindowManager;->interceptScreenshotChord(IJ)V

    goto :goto_18

    nop

    :goto_11d
    if-nez v13, :cond_22

    goto :goto_63

    :cond_22
    goto :goto_1ca

    nop

    :goto_11e
    move-object/from16 v2, p1

    goto :goto_81

    nop

    :goto_11f
    const/16 v2, 0xd

    goto :goto_118

    nop

    :goto_120
    goto :goto_1ac

    :goto_121
    goto :goto_c9

    nop

    :goto_122
    move v3, v5

    goto :goto_18a

    nop

    :goto_123
    move v3, v5

    goto :goto_17e

    nop

    :goto_124
    move v3, v6

    goto :goto_4e

    nop

    :goto_125
    if-eqz v0, :cond_23

    goto :goto_148

    :cond_23
    goto :goto_6a

    nop

    :goto_126
    goto :goto_1ac

    :goto_127
    goto :goto_ea

    nop

    :goto_128
    move v3, v5

    goto :goto_19e

    nop

    :goto_129
    invoke-virtual {v1, v6}, Lcom/android/server/policy/PhoneWindowManager;->lockNow(Landroid/os/Bundle;)V

    goto :goto_1a7

    nop

    :goto_12a
    const/4 v6, 0x0

    goto :goto_12b

    nop

    :goto_12b
    const-string v14, "WindowManager"

    sparse-switch v9, :sswitch_data_0

    goto :goto_93

    nop

    :goto_12c
    move-object/from16 v15, p2

    goto :goto_50

    nop

    :goto_12d
    if-nez v8, :cond_24

    goto :goto_da

    :cond_24
    goto :goto_1ba

    nop

    :goto_12e
    move v3, v5

    goto :goto_14e

    nop

    :goto_12f
    goto :goto_1ac

    :sswitch_e
    goto :goto_dc

    nop

    :goto_130
    goto :goto_1ac

    :goto_131
    goto :goto_188

    nop

    :goto_132
    if-nez v8, :cond_25

    goto :goto_13b

    :cond_25
    goto :goto_f5

    nop

    :goto_133
    move-object/from16 v2, p1

    goto :goto_e7

    nop

    :goto_134
    goto :goto_1ac

    :goto_135
    goto :goto_24

    nop

    :goto_136
    if-nez v13, :cond_26

    goto :goto_135

    :cond_26
    nop

    goto :goto_166

    nop

    :goto_137
    if-nez v8, :cond_27

    goto :goto_63

    :cond_27
    goto :goto_11d

    nop

    :goto_138
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getModifierState()I

    move-result v11

    goto :goto_1d4

    nop

    :goto_139
    move-object/from16 v2, p1

    goto :goto_1d2

    nop

    :goto_13a
    goto :goto_1ac

    :goto_13b
    goto :goto_29

    nop

    :goto_13c
    goto :goto_1ac

    :sswitch_f
    goto :goto_1cf

    nop

    :goto_13d
    goto :goto_1ac

    :sswitch_10
    goto :goto_119

    nop

    :goto_13e
    move-object/from16 v15, p2

    goto :goto_b2

    nop

    :goto_13f
    and-int/lit16 v2, v11, 0xc1

    goto :goto_1ad

    nop

    :goto_140
    move v3, v5

    goto :goto_13c

    nop

    :goto_141
    invoke-virtual {v0, v2}, Lcom/android/server/policy/VoiceAccessShortcutController;->toggleVoiceAccess(I)Z

    goto :goto_1b1

    nop

    :goto_142
    move-object/from16 v15, p2

    goto :goto_0

    nop

    :goto_143
    move v3, v5

    goto :goto_14b

    nop

    :goto_144
    move v4, v3

    goto :goto_1b6

    nop

    :goto_145
    if-eqz v12, :cond_28

    goto :goto_ae

    :cond_28
    goto :goto_db

    nop

    :goto_146
    move v3, v5

    goto :goto_26

    nop

    :goto_147
    iput-boolean v3, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerKeyHandled:Z

    :goto_148
    goto :goto_fb

    nop

    :goto_149
    move-object/from16 v15, p2

    goto :goto_67

    nop

    :goto_14a
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->getScreenshotChordLongPressDelay()J

    move-result-wide v4

    goto :goto_11c

    nop

    :goto_14b
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_53

    nop

    :goto_14c
    iget-object v2, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_159

    nop

    :goto_14d
    move-object/from16 v2, p1

    goto :goto_c5

    nop

    :goto_14e
    goto :goto_1ac

    :goto_14f
    goto :goto_1a8

    nop

    :goto_150
    move v3, v5

    goto :goto_13a

    nop

    :goto_151
    goto :goto_1ac

    :sswitch_11
    goto :goto_d4

    nop

    :goto_152
    sget-object v3, Lcom/android/server/policy/TalkbackShortcutController$ShortcutSource;->KEYBOARD:Lcom/android/server/policy/TalkbackShortcutController$ShortcutSource;

    goto :goto_86

    nop

    :goto_153
    if-nez v8, :cond_29

    goto :goto_3f

    :cond_29
    goto :goto_1db

    nop

    :goto_154
    goto :goto_1ac

    :sswitch_12
    goto :goto_17a

    nop

    :goto_155
    move-object/from16 v2, p1

    goto :goto_18e

    nop

    :goto_156
    move v3, v5

    goto :goto_32

    nop

    :goto_157
    goto :goto_1ac

    :sswitch_13
    goto :goto_1d0

    nop

    :goto_158
    goto :goto_1ac

    :sswitch_14
    goto :goto_12c

    nop

    :goto_159
    const/16 v3, 0x11

    goto :goto_1d6

    nop

    :goto_15a
    goto :goto_1ac

    :sswitch_15
    goto :goto_ee

    nop

    :goto_15b
    goto :goto_1ac

    :sswitch_16
    goto :goto_4b

    nop

    :goto_15c
    move v0, v2

    :goto_15d
    goto :goto_11a

    nop

    :goto_15e
    move-object/from16 v15, p2

    goto :goto_10c

    nop

    :goto_15f
    if-nez v2, :cond_2a

    goto :goto_19f

    :cond_2a
    goto :goto_17c

    nop

    :goto_160
    move v3, v6

    goto :goto_b9

    nop

    :goto_161
    iget v2, v1, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    goto :goto_141

    nop

    :goto_162
    move-object/from16 v2, p1

    goto :goto_1d8

    nop

    :goto_163
    move-object/from16 v2, p1

    goto :goto_122

    nop

    :goto_164
    move v4, v2

    :goto_165
    goto :goto_189

    nop

    :goto_166
    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v4

    goto :goto_17b

    nop

    :goto_167
    move v3, v5

    goto :goto_11

    nop

    :goto_168
    move v3, v5

    goto :goto_7d

    nop

    :goto_169
    move-object/from16 v2, p1

    goto :goto_175

    nop

    :goto_16a
    goto :goto_1ac

    :goto_16b
    goto :goto_1b9

    nop

    :goto_16c
    move v0, v3

    goto :goto_1dc

    nop

    :goto_16d
    goto :goto_1ac

    :goto_16e
    goto :goto_31

    nop

    :goto_16f
    goto :goto_1ac

    :goto_170
    goto :goto_1a6

    nop

    :goto_171
    move-object/from16 v15, p2

    goto :goto_8d

    nop

    :goto_172
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->isCancelled()Z

    move-result v0

    goto :goto_b0

    nop

    :goto_173
    goto :goto_1ac

    :sswitch_17
    goto :goto_1be

    nop

    :goto_174
    move v6, v5

    goto :goto_9f

    nop

    :goto_175
    move-object/from16 v15, p2

    goto :goto_b4

    nop

    :goto_176
    goto :goto_1c7

    :goto_177
    goto :goto_1c6

    nop

    :goto_178
    const-string v3, "launchAllAppsViaA11y"

    goto :goto_8

    nop

    :goto_179
    goto :goto_1ac

    :sswitch_18
    goto :goto_20

    nop

    :goto_17a
    if-nez v8, :cond_2b

    goto :goto_121

    :cond_2b
    goto :goto_129

    nop

    :goto_17b
    const-string v2, "android.intent.extra.ASSIST_INPUT_HINT_KEYBOARD"

    goto :goto_124

    nop

    :goto_17c
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->dismissKeyboardShortcutsMenu()V

    goto :goto_19

    nop

    :goto_17d
    move v3, v5

    goto :goto_12d

    nop

    :goto_17e
    goto :goto_1ac

    :sswitch_19
    goto :goto_d

    nop

    :goto_17f
    goto :goto_1ac

    :goto_180
    goto :goto_4a

    nop

    :goto_181
    move-object/from16 v2, p1

    goto :goto_13e

    nop

    :goto_182
    goto :goto_1ac

    :sswitch_1a
    goto :goto_6f

    nop

    :goto_183
    move-object/from16 v2, p1

    goto :goto_146

    nop

    :goto_184
    move-object/from16 v15, p2

    goto :goto_174

    nop

    :goto_185
    if-eqz v12, :cond_2c

    goto :goto_19d

    :cond_2c
    goto :goto_9a

    nop

    :goto_186
    if-nez v8, :cond_2d

    goto :goto_127

    :cond_2d
    goto :goto_192

    nop

    :goto_187
    move-object/from16 v2, p1

    goto :goto_151

    nop

    :goto_188
    move v6, v5

    goto :goto_25

    nop

    :goto_189
    if-nez v4, :cond_2e

    goto :goto_177

    :cond_2e
    goto :goto_176

    nop

    :goto_18a
    goto :goto_1ac

    :goto_18b
    goto :goto_193

    nop

    :goto_18c
    move v3, v5

    goto :goto_1c2

    nop

    :goto_18d
    move-object/from16 v2, p1

    goto :goto_195

    nop

    :goto_18e
    move v3, v5

    goto :goto_ba

    nop

    :goto_18f
    move v3, v5

    goto :goto_fd

    nop

    :goto_190
    goto :goto_1ac

    :sswitch_1b
    goto :goto_171

    nop

    :goto_191
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_111

    nop

    :goto_192
    invoke-direct {v1, v5}, Lcom/android/server/policy/PhoneWindowManager;->toggleKeyboardShortcutsMenu(I)V

    goto :goto_3

    nop

    :goto_193
    move-object/from16 v2, p1

    goto :goto_1b4

    nop

    :goto_194
    invoke-direct {v1, v3}, Lcom/android/server/policy/PhoneWindowManager;->showRecentApps(Z)V

    goto :goto_79

    nop

    :goto_195
    move-object/from16 v15, p2

    goto :goto_123

    nop

    :goto_196
    aget v2, v3, v2

    goto :goto_178

    nop

    :goto_197
    const/4 v4, 0x2

    goto :goto_1a1

    nop

    :goto_198
    goto :goto_1ac

    :sswitch_1c
    goto :goto_e

    nop

    :goto_199
    move-object/from16 v15, p2

    goto :goto_5b

    nop

    :goto_19a
    move v3, v5

    goto :goto_17f

    nop

    :goto_19b
    invoke-virtual/range {p1 .. p1}, Landroid/hardware/input/KeyGestureEvent;->getAction()I

    move-result v0

    goto :goto_52

    nop

    :goto_19c
    goto :goto_1ac

    :goto_19d
    goto :goto_cb

    nop

    :goto_19e
    goto :goto_1ac

    :goto_19f
    goto :goto_bd

    nop

    :goto_1a0
    iget v2, v1, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    goto :goto_152

    nop

    :goto_1a1
    if-eq v0, v4, :cond_2f

    goto :goto_1dd

    :cond_2f
    goto :goto_172

    nop

    :goto_1a2
    goto :goto_1ac

    :goto_1a3
    goto :goto_64

    nop

    :goto_1a4
    move-object/from16 v15, p2

    goto :goto_1bd

    nop

    :goto_1a5
    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mEnableBugReportKeyboardShortcut:Z

    goto :goto_f

    nop

    :goto_1a6
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->cancelPendingRingerToggleChordAction()V

    goto :goto_14d

    nop

    :goto_1a7
    move-object/from16 v2, p1

    goto :goto_10f

    nop

    :goto_1a8
    move-object/from16 v2, p1

    goto :goto_75

    nop

    :goto_1a9
    const-string v2, "KEY_GESTURE_TYPE_GLOBAL_ACTIONS - Global Actions"

    goto :goto_89

    nop

    :goto_1aa
    move-object/from16 v15, p2

    goto :goto_7c

    nop

    :goto_1ab
    move-object/from16 v2, p1

    :goto_1ac
    goto :goto_58

    nop

    :goto_1ad
    if-nez v2, :cond_30

    goto :goto_d7

    :cond_30
    goto :goto_d6

    nop

    :goto_1ae
    move-object/from16 v2, p1

    goto :goto_eb

    nop

    :goto_1af
    move-object/from16 v2, p1

    goto :goto_3a

    nop

    :goto_1b0
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->interceptBugreportGestureTv()V

    goto :goto_4

    nop

    :goto_1b1
    move-object/from16 v2, p1

    goto :goto_7e

    nop

    :goto_1b2
    move-object/from16 v15, p2

    goto :goto_2f

    nop

    :goto_1b3
    if-nez v8, :cond_31

    goto :goto_82

    :cond_31
    goto :goto_d5

    nop

    :goto_1b4
    move v3, v5

    goto :goto_157

    nop

    :goto_1b5
    invoke-direct {v2, v1, v10}, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda4;-><init>(Lcom/android/server/policy/PhoneWindowManager;I)V

    goto :goto_88

    nop

    :goto_1b6
    goto :goto_165

    :goto_1b7
    goto :goto_164

    nop

    :goto_1b8
    move-object/from16 v15, p2

    goto :goto_140

    nop

    :goto_1b9
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->cancelGlobalActionsAction()V

    goto :goto_18d

    nop

    :goto_1ba
    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_2c

    nop

    :goto_1bb
    if-nez v8, :cond_32

    goto :goto_12

    :cond_32
    goto :goto_a5

    nop

    :goto_1bc
    move-object/from16 v15, p2

    goto :goto_1e

    nop

    :goto_1bd
    move v3, v5

    goto :goto_1b

    nop

    :goto_1be
    move-object/from16 v15, p2

    goto :goto_100

    nop

    :goto_1bf
    move v3, v5

    goto :goto_78

    nop

    :goto_1c0
    goto :goto_1ac

    :goto_1c1
    goto :goto_90

    nop

    :goto_1c2
    goto :goto_1ac

    :goto_1c3
    goto :goto_56

    nop

    :goto_1c4
    move v3, v5

    goto :goto_9b

    nop

    :goto_1c5
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_1ae

    nop

    :goto_1c6
    move v2, v3

    :goto_1c7
    nop

    goto :goto_14

    nop

    :goto_1c8
    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->getTargetDisplayIdForKeyGestureEvent(Landroid/hardware/input/KeyGestureEvent;)I

    move-result v2

    goto :goto_f7

    nop

    :goto_1c9
    move-object/from16 v2, p1

    goto :goto_16d

    nop

    :goto_1ca
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->showSystemSettings()V

    goto :goto_21

    nop

    :goto_1cb
    move v3, v5

    goto :goto_13d

    nop

    :goto_1cc
    if-nez v4, :cond_33

    goto :goto_1b7

    :cond_33
    goto :goto_144

    nop

    :goto_1cd
    move v0, v3

    goto :goto_59

    nop

    :goto_1ce
    if-nez v0, :cond_34

    goto :goto_1c1

    :cond_34
    goto :goto_110

    nop

    :goto_1cf
    if-nez v8, :cond_35

    goto :goto_a4

    :cond_35
    goto :goto_be

    nop

    :goto_1d0
    move-object/from16 v15, p2

    goto :goto_186

    nop

    :goto_1d1
    move-object/from16 v15, p2

    goto :goto_39

    nop

    :goto_1d2
    move-object/from16 v15, p2

    goto :goto_60

    nop

    :goto_1d3
    goto :goto_1ac

    :sswitch_1d
    goto :goto_1bb

    nop

    :goto_1d4
    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->keyguardOn()Z

    move-result v12

    goto :goto_7

    nop

    :goto_1d5
    move-object/from16 v15, p2

    goto :goto_c8

    nop

    :goto_1d6
    invoke-virtual {v2, v3}, Landroid/os/Handler;->obtainMessage(I)Landroid/os/Message;

    move-result-object v2

    goto :goto_c3

    nop

    :goto_1d7
    if-nez v8, :cond_36

    goto :goto_3d

    :cond_36
    goto :goto_1a5

    nop

    :goto_1d8
    move v3, v6

    goto :goto_72

    nop

    :goto_1d9
    move v0, v2

    :goto_1da
    goto :goto_8e

    nop

    :goto_1db
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->toggleNotificationPanel()V

    goto :goto_28

    nop

    :goto_1dc
    goto :goto_1da

    :goto_1dd
    goto :goto_1d9

    nop

    :goto_1de
    invoke-virtual {v0, v2, v6, v14, v3}, Landroid/app/NotificationManager;->setZenMode(ILandroid/net/Uri;Ljava/lang/String;Z)V

    goto :goto_169

    nop

    :goto_1df
    move v3, v6

    goto :goto_b8

    nop

    :goto_1e0
    move v3, v5

    goto :goto_68

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "add_method_handleVolumeLongPressAbort__V",
        "method":      ".method handleVolumeLongPressAbort()V",
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method handleVolumeLongPressAbort()V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_2

    nop

    :goto_1
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mVolumeDownLongPress:Ljava/lang/Runnable;

    goto :goto_6

    nop

    :goto_2
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mVolumeUpLongPress:Ljava/lang/Runnable;

    goto :goto_3

    nop

    :goto_3
    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    goto :goto_4

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_1

    nop

    :goto_5
    return-void

    :goto_6
    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    goto :goto_5

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_init_Lcom_android_server_policy_PhoneWindowManager_Injector_",
        "method":      ".method init(Lcom/android/server/policy/PhoneWindowManager$Injector;)V",
        "type":        "method_replace",
        "search": """\
.method init(Lcom/android/server/policy/PhoneWindowManager$Injector;)V
    .registers 21

    move-object/from16 v0, p0

    invoke-virtual/range {p1 .. p1}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getContext()Landroid/content/Context;

    move-result-object v1

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual/range {p1 .. p1}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getWindowManager()Landroid/view/IWindowManager;

    move-result-object v1

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mWindowManager:Landroid/view/IWindowManager;

    invoke-virtual/range {p1 .. p1}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getWindowManagerFuncs()Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;

    move-result-object v1

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerFuncs:Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;

    invoke-static {}, Lcom/android/server/ufw/UltraFrameworkServiceFactory;->getInstance()Lcom/android/server/ufw/UltraFrameworkServiceFactory;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/server/ufw/UltraFrameworkServiceFactory;->makeUnisocPhoneWindowManagerUtil()Lcom/android/server/policy/UFwPhoneWindowManagerUtil;

    move-result-object v1

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mUnisocPhoneWindowUtil:Lcom/android/server/policy/UFwPhoneWindowManagerUtil;

    const-class v1, Lcom/android/server/wm/WindowManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/wm/WindowManagerInternal;

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerInternal:Lcom/android/server/wm/WindowManagerInternal;

    const-class v1, Landroid/app/ActivityManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/app/ActivityManagerInternal;

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mActivityManagerInternal:Landroid/app/ActivityManagerInternal;

    invoke-virtual/range {p1 .. p1}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getActivityManagerService()Landroid/app/IActivityManager;

    move-result-object v1

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mActivityManagerService:Landroid/app/IActivityManager;

    const-class v1, Lcom/android/server/wm/ActivityTaskManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/wm/ActivityTaskManagerInternal;

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mActivityTaskManagerInternal:Lcom/android/server/wm/ActivityTaskManagerInternal;

    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    const-class v2, Landroid/hardware/input/InputManager;

    invoke-virtual {v1, v2}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/hardware/input/InputManager;

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mInputManager:Landroid/hardware/input/InputManager;

    const-class v1, Lcom/android/server/input/InputManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/input/InputManagerInternal;

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mInputManagerInternal:Lcom/android/server/input/InputManagerInternal;

    const-class v1, Landroid/service/dreams/DreamManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/service/dreams/DreamManagerInternal;

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mDreamManagerInternal:Landroid/service/dreams/DreamManagerInternal;

    const-class v1, Landroid/os/PowerManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/os/PowerManagerInternal;

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManagerInternal:Landroid/os/PowerManagerInternal;

    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    const-class v2, Landroid/app/AppOpsManager;

    invoke-virtual {v1, v2}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/app/AppOpsManager;

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mAppOpsManager:Landroid/app/AppOpsManager;

    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    const-class v2, Landroid/hardware/SensorPrivacyManager;

    invoke-virtual {v1, v2}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/hardware/SensorPrivacyManager;

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mSensorPrivacyManager:Landroid/hardware/SensorPrivacyManager;

    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    const-class v2, Landroid/hardware/display/DisplayManager;

    invoke-virtual {v1, v2}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/hardware/display/DisplayManager;

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mDisplayManager:Landroid/hardware/display/DisplayManager;

    const-class v1, Landroid/hardware/display/DisplayManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/hardware/display/DisplayManagerInternal;

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mDisplayManagerInternal:Landroid/hardware/display/DisplayManagerInternal;

    const-class v1, Lcom/android/server/pm/UserManagerInternal;

    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/pm/UserManagerInternal;

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mUserManagerInternal:Lcom/android/server/pm/UserManagerInternal;

    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v1

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mPackageManager:Landroid/content/pm/PackageManager;

    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mPackageManager:Landroid/content/pm/PackageManager;

    const-string v2, "android.hardware.type.watch"

    invoke-virtual {v1, v2}, Landroid/content/pm/PackageManager;->hasSystemFeature(Ljava/lang/String;)Z

    move-result v1

    iput-boolean v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mHasFeatureWatch:Z

    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mPackageManager:Landroid/content/pm/PackageManager;

    const-string v2, "android.software.leanback"

    invoke-virtual {v1, v2}, Landroid/content/pm/PackageManager;->hasSystemFeature(Ljava/lang/String;)Z

    move-result v1

    iput-boolean v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mHasFeatureLeanback:Z

    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mPackageManager:Landroid/content/pm/PackageManager;

    const-string v2, "android.hardware.type.automotive"

    invoke-virtual {v1, v2}, Landroid/content/pm/PackageManager;->hasSystemFeature(Ljava/lang/String;)Z

    move-result v1

    iput-boolean v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mHasFeatureAuto:Z

    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mPackageManager:Landroid/content/pm/PackageManager;

    const-string v2, "android.hardware.hdmi.cec"

    invoke-virtual {v1, v2}, Landroid/content/pm/PackageManager;->hasSystemFeature(Ljava/lang/String;)Z

    move-result v1

    iput-boolean v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mHasFeatureHdmiCec:Z

    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    new-instance v2, Landroid/os/Handler;

    invoke-direct {v2}, Landroid/os/Handler;-><init>()V

    iget v3, v0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    move-object/from16 v4, p1

    invoke-virtual {v4, v1, v2, v3}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getAccessibilityShortcutController(Landroid/content/Context;Landroid/os/Handler;I)Lcom/android/internal/accessibility/AccessibilityShortcutController;

    move-result-object v1

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mAccessibilityShortcutController:Lcom/android/internal/accessibility/AccessibilityShortcutController;

    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getGlobalActionsFactory()Ljava/util/function/Supplier;

    move-result-object v1

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mGlobalActionsFactory:Ljava/util/function/Supplier;

    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getLockPatternUtils()Lcom/android/internal/widget/LockPatternUtils;

    move-result-object v1

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mLockPatternUtils:Lcom/android/internal/widget/LockPatternUtils;

    const-string v1, "ro.boot.factorybuild"

    const/4 v2, 0x0

    invoke-static {v1, v2}, Landroid/os/SystemProperties;->getInt(Ljava/lang/String;I)I

    move-result v1

    iput v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mIsFactoryBuild:I

    new-instance v1, Lcom/android/internal/logging/MetricsLogger;

    invoke-direct {v1}, Lcom/android/internal/logging/MetricsLogger;-><init>()V

    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mLogger:Lcom/android/internal/logging/MetricsLogger;

    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    nop

    const v3, 0x11102b5

    invoke-virtual {v1, v3}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v3

    iput-boolean v3, v0, Lcom/android/server/policy/PhoneWindowManager;->mWakeOnDpadKeyPress:Z

    nop

    const v3, 0x11102b3

    invoke-virtual {v1, v3}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v3

    iput-boolean v3, v0, Lcom/android/server/policy/PhoneWindowManager;->mWakeOnAssistKeyPress:Z

    nop

    const v3, 0x11102b4

    invoke-virtual {v1, v3}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v3

    iput-boolean v3, v0, Lcom/android/server/policy/PhoneWindowManager;->mWakeOnBackKeyPress:Z

    iget-object v3, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v3}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    const v5, 0x111016f

    invoke-virtual {v3, v5}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v3

    nop

    const-string v5, "persist.debug.force_burn_in"

    invoke-static {v5, v2}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z

    move-result v5

    if-nez v3, :cond_0

    if-eqz v5, :cond_3

    :cond_0
    if-eqz v5, :cond_2

    const/4 v6, -0x8

    const/16 v7, 0x8

    const/4 v8, -0x8

    const/4 v9, -0x4

    invoke-direct {v0}, Lcom/android/server/policy/PhoneWindowManager;->isRoundWindow()Z

    move-result v10

    if-eqz v10, :cond_1

    const/4 v10, 0x6

    goto :goto_0

    :cond_1
    const/4 v10, -0x1

    :goto_0
    move v14, v6

    move v15, v7

    move/from16 v16, v8

    move/from16 v17, v9

    move/from16 v18, v10

    goto :goto_1

    :cond_2
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x10e0046

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v7

    const v8, 0x10e0043

    invoke-virtual {v6, v8}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v8

    const v9, 0x10e0047

    invoke-virtual {v6, v9}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v9

    const v10, 0x10e0045

    invoke-virtual {v6, v10}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v10

    const v11, 0x10e0044

    invoke-virtual {v6, v11}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v11

    move v14, v7

    move v15, v8

    move/from16 v16, v9

    move/from16 v17, v10

    move/from16 v18, v11

    :goto_1
    new-instance v12, Lcom/android/server/policy/BurnInProtectionHelper;

    iget-object v13, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-direct/range {v12 .. v18}, Lcom/android/server/policy/BurnInProtectionHelper;-><init>(Landroid/content/Context;IIIII)V

    iput-object v12, v0, Lcom/android/server/policy/PhoneWindowManager;->mBurnInProtectionHelper:Lcom/android/server/policy/BurnInProtectionHelper;

    :cond_3
    new-instance v6, Lcom/android/server/policy/PhoneWindowManager$PolicyHandler;

    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getLooper()Landroid/os/Looper;

    move-result-object v7

    const/4 v8, 0x0

    invoke-direct {v6, v0, v7, v8}, Lcom/android/server/policy/PhoneWindowManager$PolicyHandler;-><init>(Lcom/android/server/policy/PhoneWindowManager;Landroid/os/Looper;Lcom/android/server/policy/PhoneWindowManager-IA;)V

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    new-instance v6, Lcom/android/server/policy/PhoneWindowManager$MyWakeGestureListener;

    iget-object v7, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    invoke-direct {v6, v0, v7, v9}, Lcom/android/server/policy/PhoneWindowManager$MyWakeGestureListener;-><init>(Lcom/android/server/policy/PhoneWindowManager;Landroid/content/Context;Landroid/os/Handler;)V

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mWakeGestureListener:Lcom/android/server/policy/PhoneWindowManager$MyWakeGestureListener;

    new-instance v6, Lcom/android/server/policy/PhoneWindowManager$SettingsObserver;

    iget-object v7, v0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    invoke-direct {v6, v0, v7}, Lcom/android/server/policy/PhoneWindowManager$SettingsObserver;-><init>(Lcom/android/server/policy/PhoneWindowManager;Landroid/os/Handler;)V

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSettingsObserver:Lcom/android/server/policy/PhoneWindowManager$SettingsObserver;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSettingsObserver:Lcom/android/server/policy/PhoneWindowManager$SettingsObserver;

    invoke-virtual {v6}, Lcom/android/server/policy/PhoneWindowManager$SettingsObserver;->observe()V

    new-instance v6, Lcom/android/server/policy/ModifierShortcutManager;

    iget-object v7, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    iget v10, v0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    invoke-static {v10}, Landroid/os/UserHandle;->of(I)Landroid/os/UserHandle;

    move-result-object v10

    invoke-direct {v6, v7, v9, v10}, Lcom/android/server/policy/ModifierShortcutManager;-><init>(Landroid/content/Context;Landroid/os/Handler;Landroid/os/UserHandle;)V

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mModifierShortcutManager:Lcom/android/server/policy/ModifierShortcutManager;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x10e0073

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mUiMode:I

    new-instance v6, Landroid/content/Intent;

    const-string v7, "android.intent.action.MAIN"

    invoke-direct {v6, v7, v8}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mHomeIntent:Landroid/content/Intent;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mHomeIntent:Landroid/content/Intent;

    const-string v9, "android.intent.category.HOME"

    invoke-virtual {v6, v9}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mHomeIntent:Landroid/content/Intent;

    const/high16 v9, 0x10200000

    invoke-virtual {v6, v9}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v10, 0x1110170

    invoke-virtual {v6, v10}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mEnableCarDockHomeCapture:Z

    new-instance v6, Landroid/content/Intent;

    invoke-direct {v6, v7, v8}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mCarDockIntent:Landroid/content/Intent;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mCarDockIntent:Landroid/content/Intent;

    const-string v10, "android.intent.category.CAR_DOCK"

    invoke-virtual {v6, v10}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mCarDockIntent:Landroid/content/Intent;

    invoke-virtual {v6, v9}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    new-instance v6, Landroid/content/Intent;

    invoke-direct {v6, v7, v8}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mDeskDockIntent:Landroid/content/Intent;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mDeskDockIntent:Landroid/content/Intent;

    const-string v10, "android.intent.category.DESK_DOCK"

    invoke-virtual {v6, v10}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mDeskDockIntent:Landroid/content/Intent;

    invoke-virtual {v6, v9}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    new-instance v6, Landroid/content/Intent;

    invoke-direct {v6, v7, v8}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mVrHeadsetHomeIntent:Landroid/content/Intent;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mVrHeadsetHomeIntent:Landroid/content/Intent;

    const-string v7, "android.intent.category.VR_HOME"

    invoke-virtual {v6, v7}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mVrHeadsetHomeIntent:Landroid/content/Intent;

    invoke-virtual {v6, v9}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    const-string v7, "power"

    invoke-virtual {v6, v7}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v6

    check-cast v6, Landroid/os/PowerManager;

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    const-string v7, "PhoneWindowManager.mBroadcastWakeLock"

    const/4 v8, 0x1

    invoke-virtual {v6, v8, v7}, Landroid/os/PowerManager;->newWakeLock(ILjava/lang/String;)Landroid/os/PowerManager$WakeLock;

    move-result-object v6

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    const-string v7, "PhoneWindowManager.mPowerKeyWakeLock"

    invoke-virtual {v6, v8, v7}, Landroid/os/PowerManager;->newWakeLock(ILjava/lang/String;)Landroid/os/PowerManager$WakeLock;

    move-result-object v6

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerKeyWakeLock:Landroid/os/PowerManager$WakeLock;

    const-string v6, "ro.debuggable"

    invoke-static {v6}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v6

    const-string v7, "1"

    invoke-virtual {v7, v6}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v6

    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mEnableBugReportKeyboardShortcut:Z

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x10e00c1

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mLidKeyboardAccessibility:I

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x10e00c2

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mLidNavigationAccessibility:I

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x11101bb

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mGoToSleepOnButtonPressTheaterMode:Z

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x1110267

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSupportLongPressPowerWhenNonInteractive:Z

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x111026b

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSupportShortPressPowerWhenDefaultDisplayOn:Z

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x10e00c6

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnBackBehavior:I

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x10e00c8

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnPowerBehavior:I

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x10e00c9

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    int-to-long v6, v6

    iput-wide v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnPowerAssistantTimeoutMs:J

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x10e0169

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mVeryLongPressOnPowerBehavior:I

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x10402c7

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-static {v6}, Landroid/content/ComponentName;->unflattenFromString(Ljava/lang/String;)Landroid/content/ComponentName;

    move-result-object v6

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerDoublePressTargetActivity:Landroid/content/ComponentName;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x1040316

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-static {v6}, Landroid/content/ComponentName;->unflattenFromString(Ljava/lang/String;)Landroid/content/ComponentName;

    move-result-object v6

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPrimaryShortPressTargetActivity:Landroid/content/ComponentName;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x10e014c

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mShortPressOnSleepBehavior:I

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x1110248

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSilenceRingerOnSleepKey:Z

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v7, 0x1110024

    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mAllowStartActivityForLongPressOnPowerDuringSetup:Z

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-static {v6}, Landroid/media/AudioSystem;->getPlatformType(Landroid/content/Context;)I

    move-result v6

    const/4 v7, 0x2

    if-ne v6, v7, :cond_4

    goto :goto_2

    :cond_4
    move v8, v2

    :goto_2
    iput-boolean v8, v0, Lcom/android/server/policy/PhoneWindowManager;->mUseTvRouting:Z

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v8, 0x11101c0

    invoke-virtual {v6, v8}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mHandleVolumeKeysInWM:Z

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v8, 0x10e0177

    invoke-virtual {v6, v8}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    int-to-long v8, v6

    iput-wide v8, v0, Lcom/android/server/policy/PhoneWindowManager;->mWakeUpToLastStateTimeout:J

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v8, 0x10e0148

    invoke-virtual {v6, v8}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSearchKeyBehavior:I

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    const v8, 0x104032e

    invoke-virtual {v6, v8}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v6

    invoke-static {v6}, Landroid/content/ComponentName;->unflattenFromString(Ljava/lang/String;)Landroid/content/ComponentName;

    move-result-object v6

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSearchKeyTargetActivity:Landroid/content/ComponentName;

    invoke-direct {v0}, Lcom/android/server/policy/PhoneWindowManager;->readConfigurationDependentBehaviors()V

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-static {v6, v2}, Lcom/android/server/policy/DisplayFoldController;->create(Landroid/content/Context;I)Lcom/android/server/policy/DisplayFoldController;

    move-result-object v6

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mDisplayFoldController:Lcom/android/server/policy/DisplayFoldController;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    const-class v8, Landroid/view/accessibility/AccessibilityManager;

    invoke-virtual {v6, v8}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v6

    check-cast v6, Landroid/view/accessibility/AccessibilityManager;

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mAccessibilityManager:Landroid/view/accessibility/AccessibilityManager;

    new-instance v6, Landroid/content/IntentFilter;

    invoke-direct {v6}, Landroid/content/IntentFilter;-><init>()V

    sget-object v8, Landroid/app/UiModeManager;->ACTION_ENTER_CAR_MODE:Ljava/lang/String;

    invoke-virtual {v6, v8}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    sget-object v8, Landroid/app/UiModeManager;->ACTION_EXIT_CAR_MODE:Ljava/lang/String;

    invoke-virtual {v6, v8}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    sget-object v8, Landroid/app/UiModeManager;->ACTION_ENTER_DESK_MODE:Ljava/lang/String;

    invoke-virtual {v6, v8}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    sget-object v8, Landroid/app/UiModeManager;->ACTION_EXIT_DESK_MODE:Ljava/lang/String;

    invoke-virtual {v6, v8}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v8, "android.intent.action.DOCK_EVENT"

    invoke-virtual {v6, v8}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    iget-object v8, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mDockReceiver:Landroid/content/BroadcastReceiver;

    invoke-virtual {v8, v9, v6}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;)Landroid/content/Intent;

    new-instance v8, Landroid/content/IntentFilter;

    const-string v9, "android.intent.action.USER_SWITCHED"

    invoke-direct {v8, v9}, Landroid/content/IntentFilter;-><init>(Ljava/lang/String;)V

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mMultiuserReceiver:Landroid/content/BroadcastReceiver;

    invoke-virtual {v6, v9, v8}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;)Landroid/content/Intent;

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    const-string v9, "vibrator"

    invoke-virtual {v6, v9}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v6

    check-cast v6, Landroid/os/Vibrator;

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mVibrator:Landroid/os/Vibrator;

    new-instance v6, Lcom/android/server/policy/GlobalKeyManager;

    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-direct {v6, v9}, Lcom/android/server/policy/GlobalKeyManager;-><init>(Landroid/content/Context;)V

    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mGlobalKeyManager:Lcom/android/server/policy/GlobalKeyManager;

    invoke-static {}, Lcom/android/server/policy/PhoneWindowManagerStub;->getInstance()Lcom/android/server/policy/PhoneWindowManagerStub;

    move-result-object v6

    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-interface {v6, v9}, Lcom/android/server/policy/PhoneWindowManagerStub;->init(Landroid/content/Context;)V

    invoke-virtual {v0}, Lcom/android/server/policy/PhoneWindowManager;->initializeHdmiState()V

    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    invoke-virtual {v6}, Landroid/os/PowerManager;->isInteractive()Z

    move-result v6

    if-nez v6, :cond_5

    invoke-virtual {v0, v2, v7}, Lcom/android/server/policy/PhoneWindowManager;->startedGoingToSleep(II)V

    invoke-virtual {v0, v2, v7}, Lcom/android/server/policy/PhoneWindowManager;->finishedGoingToSleep(II)V

    :cond_5
    new-instance v6, Lcom/android/server/policy/PhoneWindowManager$7;

    invoke-direct {v6, v0, v2}, Lcom/android/server/policy/PhoneWindowManager$7;-><init>(Lcom/android/server/policy/PhoneWindowManager;I)V

    iget-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerInternal:Lcom/android/server/wm/WindowManagerInternal;

    invoke-virtual {v2, v6}, Lcom/android/server/wm/WindowManagerInternal;->registerAppTransitionListener(Lcom/android/server/wm/WindowManagerInternal$AppTransitionListener;)V

    iget-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    const v7, 0x10e00ba

    invoke-virtual {v2, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v2

    iput v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDrawnTimeout:I

    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getKeyguardServiceDelegate()Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    move-result-object v2

    iput-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getTalkbackShortcutController()Lcom/android/server/policy/TalkbackShortcutController;

    move-result-object v2

    iput-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mTalkbackShortcutController:Lcom/android/server/policy/TalkbackShortcutController;

    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getVoiceAccessShortcutController()Lcom/android/server/policy/VoiceAccessShortcutController;

    move-result-object v2

    iput-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mVoiceAccessShortcutController:Lcom/android/server/policy/VoiceAccessShortcutController;

    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getWindowWakeUpPolicy()Lcom/android/server/policy/WindowWakeUpPolicy;

    move-result-object v2

    iput-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mWindowWakeUpPolicy:Lcom/android/server/policy/WindowWakeUpPolicy;

    invoke-direct {v0}, Lcom/android/server/policy/PhoneWindowManager;->initKeyCombinationRules()V

    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getLooper()Landroid/os/Looper;

    move-result-object v2

    invoke-direct {v0, v2}, Lcom/android/server/policy/PhoneWindowManager;->initSingleKeyGestureRules(Landroid/os/Looper;)V

    invoke-direct {v0}, Lcom/android/server/policy/PhoneWindowManager;->initKeyGestures()V

    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getButtonOverridePermissionChecker()Lcom/android/server/policy/PhoneWindowManager$ButtonOverridePermissionChecker;

    move-result-object v2

    iput-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mButtonOverridePermissionChecker:Lcom/android/server/policy/PhoneWindowManager$ButtonOverridePermissionChecker;

    new-instance v2, Lcom/android/server/policy/SideFpsEventHandler;

    iget-object v7, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    iget-object v10, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    invoke-direct {v2, v7, v9, v10}, Lcom/android/server/policy/SideFpsEventHandler;-><init>(Landroid/content/Context;Landroid/os/Handler;Landroid/os/PowerManager;)V

    iput-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mSideFpsEventHandler:Lcom/android/server/policy/SideFpsEventHandler;

    return-void
.end method
""",
        "replacement": """\
.method init(Lcom/android/server/policy/PhoneWindowManager$Injector;)V
    .registers 21

    goto :goto_176

    nop

    :goto_0
    invoke-virtual/range {p1 .. p1}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getActivityManagerService()Landroid/app/IActivityManager;

    move-result-object v1

    goto :goto_c6

    nop

    :goto_1
    invoke-direct {v6, v0, v7, v9}, Lcom/android/server/policy/PhoneWindowManager$MyWakeGestureListener;-><init>(Lcom/android/server/policy/PhoneWindowManager;Landroid/content/Context;Landroid/os/Handler;)V

    goto :goto_db

    nop

    :goto_2
    invoke-virtual {v1, v2}, Landroid/content/pm/PackageManager;->hasSystemFeature(Ljava/lang/String;)Z

    move-result v1

    goto :goto_18d

    nop

    :goto_3
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_10b

    nop

    :goto_4
    iget-object v13, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_195

    nop

    :goto_5
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_2f

    nop

    :goto_6
    iput-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    goto :goto_f5

    nop

    :goto_7
    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnBackBehavior:I

    goto :goto_131

    nop

    :goto_8
    const v7, 0x10e0169

    goto :goto_d5

    nop

    :goto_9
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mUserManagerInternal:Lcom/android/server/pm/UserManagerInternal;

    goto :goto_3d

    nop

    :goto_a
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mPackageManager:Landroid/content/pm/PackageManager;

    goto :goto_17c

    nop

    :goto_b
    invoke-virtual {v1, v2}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_184

    nop

    :goto_c
    const/high16 v9, 0x10200000

    goto :goto_c7

    nop

    :goto_d
    invoke-virtual {v6}, Lcom/android/server/policy/PhoneWindowManager$SettingsObserver;->observe()V

    goto :goto_aa

    nop

    :goto_e
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mDeskDockIntent:Landroid/content/Intent;

    goto :goto_85

    nop

    :goto_f
    const/4 v8, 0x1

    goto :goto_172

    nop

    :goto_10
    invoke-virtual {v2, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v2

    goto :goto_10c

    nop

    :goto_11
    invoke-static {v6}, Landroid/content/ComponentName;->unflattenFromString(Ljava/lang/String;)Landroid/content/ComponentName;

    move-result-object v6

    goto :goto_a4

    nop

    :goto_12
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_76

    nop

    :goto_13
    iget v10, v0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    goto :goto_f2

    nop

    :goto_14
    iget-object v10, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    goto :goto_1ad

    nop

    :goto_15
    if-nez v5, :cond_0

    goto :goto_af

    :cond_0
    :goto_16
    goto :goto_8d

    nop

    :goto_17
    new-instance v6, Landroid/content/Intent;

    goto :goto_143

    nop

    :goto_18
    invoke-virtual {v6, v11}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v11

    goto :goto_be

    nop

    :goto_19
    const/4 v9, -0x4

    goto :goto_63

    nop

    :goto_1a
    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_7e

    nop

    :goto_1b
    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSupportShortPressPowerWhenDefaultDisplayOn:Z

    goto :goto_2e

    nop

    :goto_1c
    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_186

    nop

    :goto_1d
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_15f

    nop

    :goto_1e
    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_13

    nop

    :goto_1f
    const/4 v8, -0x8

    goto :goto_19

    nop

    :goto_20
    invoke-direct {v6}, Landroid/content/IntentFilter;-><init>()V

    goto :goto_a6

    nop

    :goto_21
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_b1

    nop

    :goto_22
    const v9, 0x10e0047

    goto :goto_73

    nop

    :goto_23
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mHomeIntent:Landroid/content/Intent;

    goto :goto_c

    nop

    :goto_24
    invoke-static {v6}, Landroid/content/ComponentName;->unflattenFromString(Ljava/lang/String;)Landroid/content/ComponentName;

    move-result-object v6

    goto :goto_cd

    nop

    :goto_25
    check-cast v1, Landroid/hardware/display/DisplayManager;

    goto :goto_196

    nop

    :goto_26
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_b2

    nop

    :goto_27
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mDeskDockIntent:Landroid/content/Intent;

    goto :goto_fd

    nop

    :goto_28
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    goto :goto_68

    nop

    :goto_29
    invoke-virtual {v6, v8}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto :goto_41

    nop

    :goto_2a
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_75

    nop

    :goto_2b
    const-class v1, Landroid/app/ActivityManagerInternal;

    goto :goto_b4

    nop

    :goto_2c
    invoke-virtual {v6, v8}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto :goto_162

    nop

    :goto_2d
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    goto :goto_33

    nop

    :goto_2e
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_134

    nop

    :goto_2f
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_171

    nop

    :goto_30
    new-instance v6, Landroid/content/Intent;

    goto :goto_192

    nop

    :goto_31
    const-string v7, "android.intent.category.VR_HOME"

    goto :goto_e7

    nop

    :goto_32
    invoke-virtual {v6, v8}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto :goto_3a

    nop

    :goto_33
    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSilenceRingerOnSleepKey:Z

    goto :goto_12b

    nop

    :goto_34
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_1af

    nop

    :goto_35
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerInternal:Lcom/android/server/wm/WindowManagerInternal;

    goto :goto_2b

    nop

    :goto_36
    new-instance v6, Landroid/content/IntentFilter;

    goto :goto_20

    nop

    :goto_37
    check-cast v6, Landroid/os/Vibrator;

    goto :goto_a1

    nop

    :goto_38
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    goto :goto_1b

    nop

    :goto_39
    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mGoToSleepOnButtonPressTheaterMode:Z

    goto :goto_165

    nop

    :goto_3a
    iget-object v8, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_59

    nop

    :goto_3b
    const v7, 0x11101bb

    goto :goto_f9

    nop

    :goto_3c
    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mAllowStartActivityForLongPressOnPowerDuringSetup:Z

    goto :goto_10d

    nop

    :goto_3d
    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_6c

    nop

    :goto_3e
    invoke-virtual {v1, v3}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v3

    goto :goto_17e

    nop

    :goto_3f
    const-string v1, "ro.boot.factorybuild"

    goto :goto_18b

    nop

    :goto_40
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mUnisocPhoneWindowUtil:Lcom/android/server/policy/UFwPhoneWindowManagerUtil;

    goto :goto_154

    nop

    :goto_41
    sget-object v8, Landroid/app/UiModeManager;->ACTION_ENTER_DESK_MODE:Ljava/lang/String;

    goto :goto_110

    nop

    :goto_42
    iput v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mIsFactoryBuild:I

    goto :goto_83

    nop

    :goto_43
    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mUiMode:I

    goto :goto_30

    nop

    :goto_44
    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mPackageManager:Landroid/content/pm/PackageManager;

    goto :goto_103

    nop

    :goto_45
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mCarDockIntent:Landroid/content/Intent;

    goto :goto_d2

    nop

    :goto_46
    check-cast v1, Lcom/android/server/wm/WindowManagerInternal;

    goto :goto_35

    nop

    :goto_47
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_16a

    nop

    :goto_48
    invoke-virtual {v2}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    goto :goto_1a2

    nop

    :goto_49
    iget-object v7, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_b3

    nop

    :goto_4a
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mActivityTaskManagerInternal:Lcom/android/server/wm/ActivityTaskManagerInternal;

    goto :goto_a7

    nop

    :goto_4b
    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_170

    nop

    :goto_4c
    new-instance v6, Landroid/content/Intent;

    goto :goto_fe

    nop

    :goto_4d
    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mPackageManager:Landroid/content/pm/PackageManager;

    goto :goto_bf

    nop

    :goto_4e
    new-instance v6, Landroid/content/Intent;

    goto :goto_1a6

    nop

    :goto_4f
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    goto :goto_6d

    nop

    :goto_50
    new-instance v6, Lcom/android/server/policy/GlobalKeyManager;

    goto :goto_132

    nop

    :goto_51
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    goto :goto_14a

    nop

    :goto_52
    const v3, 0x11102b5

    goto :goto_3e

    nop

    :goto_53
    const v10, 0x1110170

    goto :goto_107

    nop

    :goto_54
    invoke-virtual {v8, v9, v6}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;)Landroid/content/Intent;

    goto :goto_187

    nop

    :goto_55
    const-class v1, Lcom/android/server/input/InputManagerInternal;

    goto :goto_1a

    nop

    :goto_56
    const-string v9, "android.intent.category.HOME"

    goto :goto_91

    nop

    :goto_57
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    goto :goto_de

    nop

    :goto_58
    new-instance v2, Landroid/os/Handler;

    goto :goto_62

    nop

    :goto_59
    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mDockReceiver:Landroid/content/BroadcastReceiver;

    goto :goto_54

    nop

    :goto_5a
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_199

    nop

    :goto_5b
    const v7, 0x10e0073

    goto :goto_11f

    nop

    :goto_5c
    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSearchKeyBehavior:I

    goto :goto_174

    nop

    :goto_5d
    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_125

    nop

    :goto_5e
    iput-boolean v3, v0, Lcom/android/server/policy/PhoneWindowManager;->mWakeOnAssistKeyPress:Z

    nop

    goto :goto_18f

    nop

    :goto_5f
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mLockPatternUtils:Lcom/android/internal/widget/LockPatternUtils;

    goto :goto_3f

    nop

    :goto_60
    iput-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mSideFpsEventHandler:Lcom/android/server/policy/SideFpsEventHandler;

    goto :goto_161

    nop

    :goto_61
    const-string v5, "persist.debug.force_burn_in"

    goto :goto_c1

    nop

    :goto_62
    invoke-direct {v2}, Landroid/os/Handler;-><init>()V

    goto :goto_d6

    nop

    :goto_63
    invoke-direct {v0}, Lcom/android/server/policy/PhoneWindowManager;->isRoundWindow()Z

    move-result v10

    goto :goto_183

    nop

    :goto_64
    invoke-direct {v0}, Lcom/android/server/policy/PhoneWindowManager;->initKeyGestures()V

    goto :goto_120

    nop

    :goto_65
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mSensorPrivacyManager:Landroid/hardware/SensorPrivacyManager;

    goto :goto_7f

    nop

    :goto_66
    goto :goto_81

    :goto_67
    goto :goto_80

    nop

    :goto_68
    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mShortPressOnSleepBehavior:I

    goto :goto_19b

    nop

    :goto_69
    check-cast v6, Landroid/os/PowerManager;

    goto :goto_167

    nop

    :goto_6a
    iput-boolean v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mHasFeatureHdmiCec:Z

    goto :goto_d3

    nop

    :goto_6b
    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getKeyguardServiceDelegate()Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    move-result-object v2

    goto :goto_6

    nop

    :goto_6c
    invoke-virtual {v1}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v1

    goto :goto_a

    nop

    :goto_6d
    int-to-long v6, v6

    goto :goto_181

    nop

    :goto_6e
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    goto :goto_ad

    nop

    :goto_6f
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    goto :goto_13b

    nop

    :goto_70
    invoke-direct {v6, v0, v7, v8}, Lcom/android/server/policy/PhoneWindowManager$PolicyHandler;-><init>(Lcom/android/server/policy/PhoneWindowManager;Landroid/os/Looper;Lcom/android/server/policy/PhoneWindowManager-IA;)V

    goto :goto_e0

    nop

    :goto_71
    iput-boolean v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mHasFeatureAuto:Z

    goto :goto_44

    nop

    :goto_72
    iget-object v3, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_122

    nop

    :goto_73
    invoke-virtual {v6, v9}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v9

    goto :goto_d7

    nop

    :goto_74
    invoke-virtual/range {p1 .. p1}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getContext()Landroid/content/Context;

    move-result-object v1

    goto :goto_e1

    nop

    :goto_75
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_3b

    nop

    :goto_76
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_77

    nop

    :goto_77
    const v8, 0x11101c0

    goto :goto_e4

    nop

    :goto_78
    const-string v10, "android.intent.category.DESK_DOCK"

    goto :goto_155

    nop

    :goto_79
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v6

    goto :goto_11

    nop

    :goto_7a
    iget-object v7, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_86

    nop

    :goto_7b
    const v8, 0x10e0148

    goto :goto_121

    nop

    :goto_7c
    invoke-virtual {v2, v6}, Lcom/android/server/wm/WindowManagerInternal;->registerAppTransitionListener(Lcom/android/server/wm/WindowManagerInternal$AppTransitionListener;)V

    goto :goto_158

    nop

    :goto_7d
    const/4 v6, -0x8

    goto :goto_11a

    nop

    :goto_7e
    check-cast v1, Lcom/android/server/input/InputManagerInternal;

    goto :goto_ed

    nop

    :goto_7f
    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_c8

    nop

    :goto_80
    const/4 v10, -0x1

    :goto_81
    goto :goto_9b

    nop

    :goto_82
    const v7, 0x10402c7

    goto :goto_92

    nop

    :goto_83
    new-instance v1, Lcom/android/internal/logging/MetricsLogger;

    goto :goto_a9

    nop

    :goto_84
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mGlobalActionsFactory:Ljava/util/function/Supplier;

    goto :goto_14b

    nop

    :goto_85
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mDeskDockIntent:Landroid/content/Intent;

    goto :goto_78

    nop

    :goto_86
    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_1

    nop

    :goto_87
    iget-object v7, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_1e

    nop

    :goto_88
    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mHandleVolumeKeysInWM:Z

    goto :goto_112

    nop

    :goto_89
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_ef

    nop

    :goto_8a
    move/from16 v17, v9

    goto :goto_a3

    nop

    :goto_8b
    check-cast v1, Lcom/android/server/pm/UserManagerInternal;

    goto :goto_9

    nop

    :goto_8c
    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mPackageManager:Landroid/content/pm/PackageManager;

    goto :goto_8f

    nop

    :goto_8d
    if-nez v5, :cond_1

    goto :goto_149

    :cond_1
    goto :goto_7d

    nop

    :goto_8e
    invoke-direct {v8, v9}, Landroid/content/IntentFilter;-><init>(Ljava/lang/String;)V

    goto :goto_113

    nop

    :goto_8f
    const-string v2, "android.software.leanback"

    goto :goto_2

    nop

    :goto_90
    const v7, 0x10e014c

    goto :goto_28

    nop

    :goto_91
    invoke-virtual {v6, v9}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_23

    nop

    :goto_92
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v6

    goto :goto_105

    nop

    :goto_93
    iget-object v7, v0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_17a

    nop

    :goto_94
    invoke-direct {v6, v7, v8}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V

    goto :goto_b0

    nop

    :goto_95
    new-instance v6, Lcom/android/server/policy/PhoneWindowManager$PolicyHandler;

    goto :goto_a0

    nop

    :goto_96
    sget-object v8, Landroid/app/UiModeManager;->ACTION_EXIT_CAR_MODE:Ljava/lang/String;

    goto :goto_29

    nop

    :goto_97
    check-cast v1, Landroid/app/AppOpsManager;

    goto :goto_133

    nop

    :goto_98
    iget-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerInternal:Lcom/android/server/wm/WindowManagerInternal;

    goto :goto_7c

    nop

    :goto_99
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_14e

    nop

    :goto_9a
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_34

    nop

    :goto_9b
    move v14, v6

    goto :goto_146

    nop

    :goto_9c
    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_15b

    nop

    :goto_9d
    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mLidNavigationAccessibility:I

    goto :goto_2a

    nop

    :goto_9e
    move/from16 v18, v11

    :goto_9f
    goto :goto_153

    nop

    :goto_a0
    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getLooper()Landroid/os/Looper;

    move-result-object v7

    goto :goto_f1

    nop

    :goto_a1
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mVibrator:Landroid/os/Vibrator;

    goto :goto_50

    nop

    :goto_a2
    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_f8

    nop

    :goto_a3
    move/from16 v18, v10

    goto :goto_148

    nop

    :goto_a4
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPrimaryShortPressTargetActivity:Landroid/content/ComponentName;

    goto :goto_99

    nop

    :goto_a5
    if-eqz v6, :cond_2

    goto :goto_118

    :cond_2
    goto :goto_c5

    nop

    :goto_a6
    sget-object v8, Landroid/app/UiModeManager;->ACTION_ENTER_CAR_MODE:Ljava/lang/String;

    goto :goto_142

    nop

    :goto_a7
    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_140

    nop

    :goto_a8
    if-eqz v3, :cond_3

    goto :goto_16

    :cond_3
    goto :goto_15

    nop

    :goto_a9
    invoke-direct {v1}, Lcom/android/internal/logging/MetricsLogger;-><init>()V

    goto :goto_19f

    nop

    :goto_aa
    new-instance v6, Lcom/android/server/policy/ModifierShortcutManager;

    goto :goto_87

    nop

    :goto_ab
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_177

    nop

    :goto_ac
    if-eq v6, v7, :cond_4

    goto :goto_bb

    :cond_4
    goto :goto_ba

    nop

    :goto_ad
    const-string v7, "PhoneWindowManager.mBroadcastWakeLock"

    goto :goto_f

    nop

    :goto_ae
    iput-object v12, v0, Lcom/android/server/policy/PhoneWindowManager;->mBurnInProtectionHelper:Lcom/android/server/policy/BurnInProtectionHelper;

    :goto_af
    goto :goto_95

    nop

    :goto_b0
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mHomeIntent:Landroid/content/Intent;

    goto :goto_10f

    nop

    :goto_b1
    const-class v8, Landroid/view/accessibility/AccessibilityManager;

    goto :goto_189

    nop

    :goto_b2
    const v7, 0x1040316

    goto :goto_79

    nop

    :goto_b3
    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_14

    nop

    :goto_b4
    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_16c

    nop

    :goto_b5
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mGlobalKeyManager:Lcom/android/server/policy/GlobalKeyManager;

    goto :goto_15d

    nop

    :goto_b6
    invoke-direct {v6, v9}, Lcom/android/server/policy/GlobalKeyManager;-><init>(Landroid/content/Context;)V

    goto :goto_b5

    nop

    :goto_b7
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mActivityManagerInternal:Landroid/app/ActivityManagerInternal;

    goto :goto_0

    nop

    :goto_b8
    invoke-virtual {v6, v8}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    goto :goto_bc

    nop

    :goto_b9
    invoke-virtual {v6, v9}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v6

    goto :goto_37

    nop

    :goto_ba
    goto :goto_1ac

    :goto_bb
    goto :goto_1ab

    nop

    :goto_bc
    int-to-long v8, v6

    goto :goto_10a

    nop

    :goto_bd
    const v8, 0x104032e

    goto :goto_d9

    nop

    :goto_be
    move v14, v7

    goto :goto_188

    nop

    :goto_bf
    const-string v2, "android.hardware.type.automotive"

    goto :goto_1a8

    nop

    :goto_c0
    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mEnableBugReportKeyboardShortcut:Z

    goto :goto_178

    nop

    :goto_c1
    invoke-static {v5, v2}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z

    move-result v5

    goto :goto_a8

    nop

    :goto_c2
    invoke-virtual {v1, v2}, Landroid/content/pm/PackageManager;->hasSystemFeature(Ljava/lang/String;)Z

    move-result v1

    goto :goto_109

    nop

    :goto_c3
    invoke-virtual {v6, v7}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v6

    goto :goto_69

    nop

    :goto_c4
    invoke-static {v1, v2}, Landroid/os/SystemProperties;->getInt(Ljava/lang/String;I)I

    move-result v1

    goto :goto_42

    nop

    :goto_c5
    invoke-virtual {v0, v2, v7}, Lcom/android/server/policy/PhoneWindowManager;->startedGoingToSleep(II)V

    goto :goto_117

    nop

    :goto_c6
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mActivityManagerService:Landroid/app/IActivityManager;

    goto :goto_19d

    nop

    :goto_c7
    invoke-virtual {v6, v9}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    goto :goto_15e

    nop

    :goto_c8
    const-class v2, Landroid/hardware/display/DisplayManager;

    goto :goto_c9

    nop

    :goto_c9
    invoke-virtual {v1, v2}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_25

    nop

    :goto_ca
    invoke-virtual {v6, v10}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_45

    nop

    :goto_cb
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_147

    nop

    :goto_cc
    move/from16 v16, v8

    goto :goto_8a

    nop

    :goto_cd
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSearchKeyTargetActivity:Landroid/content/ComponentName;

    goto :goto_100

    nop

    :goto_ce
    invoke-virtual {v4, v1, v2, v3}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getAccessibilityShortcutController(Landroid/content/Context;Landroid/os/Handler;I)Lcom/android/internal/accessibility/AccessibilityShortcutController;

    move-result-object v1

    goto :goto_119

    nop

    :goto_cf
    invoke-virtual {v3, v5}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v3

    nop

    goto :goto_61

    nop

    :goto_d0
    const v7, 0x10e00c9

    goto :goto_4f

    nop

    :goto_d1
    invoke-virtual {v6, v9, v8}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;)Landroid/content/Intent;

    goto :goto_156

    nop

    :goto_d2
    invoke-virtual {v6, v9}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    goto :goto_4e

    nop

    :goto_d3
    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_58

    nop

    :goto_d4
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mVrHeadsetHomeIntent:Landroid/content/Intent;

    goto :goto_12e

    nop

    :goto_d5
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    goto :goto_197

    nop

    :goto_d6
    iget v3, v0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    goto :goto_17b

    nop

    :goto_d7
    const v10, 0x10e0045

    goto :goto_1a1

    nop

    :goto_d8
    iput-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mVoiceAccessShortcutController:Lcom/android/server/policy/VoiceAccessShortcutController;

    goto :goto_17f

    nop

    :goto_d9
    invoke-virtual {v6, v8}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v6

    goto :goto_24

    nop

    :goto_da
    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mEnableCarDockHomeCapture:Z

    goto :goto_4c

    nop

    :goto_db
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mWakeGestureListener:Lcom/android/server/policy/PhoneWindowManager$MyWakeGestureListener;

    goto :goto_15a

    nop

    :goto_dc
    invoke-virtual {v1, v2}, Landroid/content/pm/PackageManager;->hasSystemFeature(Ljava/lang/String;)Z

    move-result v1

    goto :goto_6a

    nop

    :goto_dd
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mInputManager:Landroid/hardware/input/InputManager;

    goto :goto_55

    nop

    :goto_de
    iput-boolean v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSupportLongPressPowerWhenNonInteractive:Z

    goto :goto_5

    nop

    :goto_df
    invoke-virtual {v1, v2}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_97

    nop

    :goto_e0
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    goto :goto_1a4

    nop

    :goto_e1
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_194

    nop

    :goto_e2
    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_12c

    nop

    :goto_e3
    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getGlobalActionsFactory()Ljava/util/function/Supplier;

    move-result-object v1

    goto :goto_84

    nop

    :goto_e4
    invoke-virtual {v6, v8}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    goto :goto_88

    nop

    :goto_e5
    const-string v9, "vibrator"

    goto :goto_b9

    nop

    :goto_e6
    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_1aa

    nop

    :goto_e7
    invoke-virtual {v6, v7}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_d4

    nop

    :goto_e8
    iput-boolean v3, v0, Lcom/android/server/policy/PhoneWindowManager;->mWakeOnBackKeyPress:Z

    goto :goto_72

    nop

    :goto_e9
    iput-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mButtonOverridePermissionChecker:Lcom/android/server/policy/PhoneWindowManager$ButtonOverridePermissionChecker;

    goto :goto_180

    nop

    :goto_ea
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_26

    nop

    :goto_eb
    const/4 v7, 0x2

    goto :goto_ac

    nop

    :goto_ec
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_173

    nop

    :goto_ed
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mInputManagerInternal:Lcom/android/server/input/InputManagerInternal;

    goto :goto_18e

    nop

    :goto_ee
    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_46

    nop

    :goto_ef
    const v7, 0x10e00c8

    goto :goto_159

    nop

    :goto_f0
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_16b

    nop

    :goto_f1
    const/4 v8, 0x0

    goto :goto_70

    nop

    :goto_f2
    invoke-static {v10}, Landroid/os/UserHandle;->of(I)Landroid/os/UserHandle;

    move-result-object v10

    goto :goto_124

    nop

    :goto_f3
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    goto :goto_7

    nop

    :goto_f4
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mDisplayFoldController:Lcom/android/server/policy/DisplayFoldController;

    goto :goto_21

    nop

    :goto_f5
    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getTalkbackShortcutController()Lcom/android/server/policy/TalkbackShortcutController;

    move-result-object v2

    goto :goto_18c

    nop

    :goto_f6
    const-string v7, "PhoneWindowManager.mPowerKeyWakeLock"

    goto :goto_fc

    nop

    :goto_f7
    invoke-static {v6}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v6

    goto :goto_106

    nop

    :goto_f8
    check-cast v1, Landroid/hardware/display/DisplayManagerInternal;

    goto :goto_185

    nop

    :goto_f9
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    goto :goto_39

    nop

    :goto_fa
    invoke-direct {v0, v2}, Lcom/android/server/policy/PhoneWindowManager;->initSingleKeyGestureRules(Landroid/os/Looper;)V

    goto :goto_64

    nop

    :goto_fb
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManagerInternal:Landroid/os/PowerManagerInternal;

    goto :goto_5d

    nop

    :goto_fc
    invoke-virtual {v6, v8, v7}, Landroid/os/PowerManager;->newWakeLock(ILjava/lang/String;)Landroid/os/PowerManager$WakeLock;

    move-result-object v6

    goto :goto_138

    nop

    :goto_fd
    invoke-virtual {v6, v9}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    goto :goto_17

    nop

    :goto_fe
    invoke-direct {v6, v7, v8}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V

    goto :goto_11e

    nop

    :goto_ff
    const-string v9, "android.intent.action.USER_SWITCHED"

    goto :goto_8e

    nop

    :goto_100
    invoke-direct {v0}, Lcom/android/server/policy/PhoneWindowManager;->readConfigurationDependentBehaviors()V

    goto :goto_47

    nop

    :goto_101
    invoke-virtual {v6, v8}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v8

    goto :goto_22

    nop

    :goto_102
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mModifierShortcutManager:Lcom/android/server/policy/ModifierShortcutManager;

    goto :goto_157

    nop

    :goto_103
    const-string v2, "android.hardware.hdmi.cec"

    goto :goto_dc

    nop

    :goto_104
    sget-object v8, Landroid/app/UiModeManager;->ACTION_EXIT_DESK_MODE:Ljava/lang/String;

    goto :goto_2c

    nop

    :goto_105
    invoke-static {v6}, Landroid/content/ComponentName;->unflattenFromString(Ljava/lang/String;)Landroid/content/ComponentName;

    move-result-object v6

    goto :goto_19a

    nop

    :goto_106
    const-string v7, "1"

    goto :goto_136

    nop

    :goto_107
    invoke-virtual {v6, v10}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    goto :goto_da

    nop

    :goto_108
    invoke-virtual {v0}, Lcom/android/server/policy/PhoneWindowManager;->initializeHdmiState()V

    goto :goto_13a

    nop

    :goto_109
    iput-boolean v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mHasFeatureWatch:Z

    goto :goto_8c

    nop

    :goto_10a
    iput-wide v8, v0, Lcom/android/server/policy/PhoneWindowManager;->mWakeUpToLastStateTimeout:J

    goto :goto_ab

    nop

    :goto_10b
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_d0

    nop

    :goto_10c
    iput v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDrawnTimeout:I

    goto :goto_6b

    nop

    :goto_10d
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_129

    nop

    :goto_10e
    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getLooper()Landroid/os/Looper;

    move-result-object v2

    goto :goto_fa

    nop

    :goto_10f
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mHomeIntent:Landroid/content/Intent;

    goto :goto_56

    nop

    :goto_110
    invoke-virtual {v6, v8}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto :goto_104

    nop

    :goto_111
    const v11, 0x10e0044

    goto :goto_18

    nop

    :goto_112
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_130

    nop

    :goto_113
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_16f

    nop

    :goto_114
    const-class v1, Lcom/android/server/pm/UserManagerInternal;

    goto :goto_145

    nop

    :goto_115
    const-class v1, Landroid/os/PowerManagerInternal;

    goto :goto_4b

    nop

    :goto_116
    invoke-virtual {v6}, Landroid/os/PowerManager;->isInteractive()Z

    move-result v6

    goto :goto_a5

    nop

    :goto_117
    invoke-virtual {v0, v2, v7}, Lcom/android/server/policy/PhoneWindowManager;->finishedGoingToSleep(II)V

    :goto_118
    goto :goto_1a3

    nop

    :goto_119
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mAccessibilityShortcutController:Lcom/android/internal/accessibility/AccessibilityShortcutController;

    goto :goto_e3

    nop

    :goto_11a
    const/16 v7, 0x8

    goto :goto_1f

    nop

    :goto_11b
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_5b

    nop

    :goto_11c
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerFuncs:Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;

    goto :goto_152

    nop

    :goto_11d
    const-string v2, "android.hardware.type.watch"

    goto :goto_c2

    nop

    :goto_11e
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mCarDockIntent:Landroid/content/Intent;

    goto :goto_17d

    nop

    :goto_11f
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    goto :goto_43

    nop

    :goto_120
    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getButtonOverridePermissionChecker()Lcom/android/server/policy/PhoneWindowManager$ButtonOverridePermissionChecker;

    move-result-object v2

    goto :goto_e9

    nop

    :goto_121
    invoke-virtual {v6, v8}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    goto :goto_5c

    nop

    :goto_122
    invoke-virtual {v3}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    goto :goto_191

    nop

    :goto_123
    invoke-virtual/range {p1 .. p1}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getWindowManagerFuncs()Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;

    move-result-object v1

    goto :goto_11c

    nop

    :goto_124
    invoke-direct {v6, v7, v9, v10}, Lcom/android/server/policy/ModifierShortcutManager;-><init>(Landroid/content/Context;Landroid/os/Handler;Landroid/os/UserHandle;)V

    goto :goto_102

    nop

    :goto_125
    const-class v2, Landroid/app/AppOpsManager;

    goto :goto_df

    nop

    :goto_126
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mVrHeadsetHomeIntent:Landroid/content/Intent;

    goto :goto_14d

    nop

    :goto_127
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mWindowManager:Landroid/view/IWindowManager;

    goto :goto_123

    nop

    :goto_128
    move/from16 v17, v10

    goto :goto_9e

    nop

    :goto_129
    invoke-static {v6}, Landroid/media/AudioSystem;->getPlatformType(Landroid/content/Context;)I

    move-result v6

    goto :goto_eb

    nop

    :goto_12a
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_12d

    nop

    :goto_12b
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_12a

    nop

    :goto_12c
    check-cast v1, Landroid/service/dreams/DreamManagerInternal;

    goto :goto_16d

    nop

    :goto_12d
    const v7, 0x1110024

    goto :goto_1a5

    nop

    :goto_12e
    invoke-virtual {v6, v9}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    goto :goto_175

    nop

    :goto_12f
    const-string v6, "ro.debuggable"

    goto :goto_f7

    nop

    :goto_130
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_18a

    nop

    :goto_131
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_89

    nop

    :goto_132
    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_b6

    nop

    :goto_133
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mAppOpsManager:Landroid/app/AppOpsManager;

    goto :goto_9c

    nop

    :goto_134
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_144

    nop

    :goto_135
    move/from16 v16, v9

    goto :goto_128

    nop

    :goto_136
    invoke-virtual {v7, v6}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v6

    goto :goto_c0

    nop

    :goto_137
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_bd

    nop

    :goto_138
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerKeyWakeLock:Landroid/os/PowerManager$WakeLock;

    goto :goto_12f

    nop

    :goto_139
    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnPowerBehavior:I

    goto :goto_3

    nop

    :goto_13a
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    goto :goto_116

    nop

    :goto_13b
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    goto :goto_f6

    nop

    :goto_13c
    const v8, 0x10e0043

    goto :goto_101

    nop

    :goto_13d
    const v3, 0x11102b3

    goto :goto_163

    nop

    :goto_13e
    iput-boolean v8, v0, Lcom/android/server/policy/PhoneWindowManager;->mUseTvRouting:Z

    goto :goto_12

    nop

    :goto_13f
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_82

    nop

    :goto_140
    const-class v2, Landroid/hardware/input/InputManager;

    goto :goto_166

    nop

    :goto_141
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_13f

    nop

    :goto_142
    invoke-virtual {v6, v8}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto :goto_96

    nop

    :goto_143
    invoke-direct {v6, v7, v8}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V

    goto :goto_126

    nop

    :goto_144
    const v7, 0x10e00c6

    goto :goto_f3

    nop

    :goto_145
    invoke-static {v1}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_8b

    nop

    :goto_146
    move v15, v7

    goto :goto_cc

    nop

    :goto_147
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_8

    nop

    :goto_148
    goto :goto_9f

    :goto_149
    goto :goto_9a

    nop

    :goto_14a
    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mLidKeyboardAccessibility:I

    goto :goto_151

    nop

    :goto_14b
    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getLockPatternUtils()Lcom/android/internal/widget/LockPatternUtils;

    move-result-object v1

    goto :goto_5f

    nop

    :goto_14c
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSettingsObserver:Lcom/android/server/policy/PhoneWindowManager$SettingsObserver;

    goto :goto_15c

    nop

    :goto_14d
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mVrHeadsetHomeIntent:Landroid/content/Intent;

    goto :goto_31

    nop

    :goto_14e
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_90

    nop

    :goto_14f
    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getVoiceAccessShortcutController()Lcom/android/server/policy/VoiceAccessShortcutController;

    move-result-object v2

    goto :goto_d8

    nop

    :goto_150
    const/4 v10, 0x6

    goto :goto_66

    nop

    :goto_151
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_ec

    nop

    :goto_152
    invoke-static {}, Lcom/android/server/ufw/UltraFrameworkServiceFactory;->getInstance()Lcom/android/server/ufw/UltraFrameworkServiceFactory;

    move-result-object v1

    goto :goto_182

    nop

    :goto_153
    new-instance v12, Lcom/android/server/policy/BurnInProtectionHelper;

    goto :goto_4

    nop

    :goto_154
    const-class v1, Lcom/android/server/wm/WindowManagerInternal;

    goto :goto_ee

    nop

    :goto_155
    invoke-virtual {v6, v10}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_27

    nop

    :goto_156
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_e5

    nop

    :goto_157
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_11b

    nop

    :goto_158
    iget-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_48

    nop

    :goto_159
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    goto :goto_139

    nop

    :goto_15a
    new-instance v6, Lcom/android/server/policy/PhoneWindowManager$SettingsObserver;

    goto :goto_93

    nop

    :goto_15b
    const-class v2, Landroid/hardware/SensorPrivacyManager;

    goto :goto_b

    nop

    :goto_15c
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mSettingsObserver:Lcom/android/server/policy/PhoneWindowManager$SettingsObserver;

    goto :goto_d

    nop

    :goto_15d
    invoke-static {}, Lcom/android/server/policy/PhoneWindowManagerStub;->getInstance()Lcom/android/server/policy/PhoneWindowManagerStub;

    move-result-object v6

    goto :goto_1a9

    nop

    :goto_15e
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_179

    nop

    :goto_15f
    const v7, 0x1110248

    goto :goto_2d

    nop

    :goto_160
    invoke-interface {v6, v9}, Lcom/android/server/policy/PhoneWindowManagerStub;->init(Landroid/content/Context;)V

    goto :goto_108

    nop

    :goto_161
    return-void

    :goto_162
    const-string v8, "android.intent.action.DOCK_EVENT"

    goto :goto_32

    nop

    :goto_163
    invoke-virtual {v1, v3}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v3

    goto :goto_5e

    nop

    :goto_164
    invoke-direct {v0}, Lcom/android/server/policy/PhoneWindowManager;->initKeyCombinationRules()V

    goto :goto_10e

    nop

    :goto_165
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_f0

    nop

    :goto_166
    invoke-virtual {v1, v2}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_1a7

    nop

    :goto_167
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    goto :goto_6e

    nop

    :goto_168
    const-class v1, Landroid/hardware/display/DisplayManagerInternal;

    goto :goto_a2

    nop

    :goto_169
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v7

    goto :goto_13c

    nop

    :goto_16a
    invoke-static {v6, v2}, Lcom/android/server/policy/DisplayFoldController;->create(Landroid/content/Context;I)Lcom/android/server/policy/DisplayFoldController;

    move-result-object v6

    goto :goto_f4

    nop

    :goto_16b
    const v7, 0x1110267

    goto :goto_57

    nop

    :goto_16c
    check-cast v1, Landroid/app/ActivityManagerInternal;

    goto :goto_b7

    nop

    :goto_16d
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mDreamManagerInternal:Landroid/service/dreams/DreamManagerInternal;

    goto :goto_115

    nop

    :goto_16e
    const-string v7, "power"

    goto :goto_c3

    nop

    :goto_16f
    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mMultiuserReceiver:Landroid/content/BroadcastReceiver;

    goto :goto_d1

    nop

    :goto_170
    check-cast v1, Landroid/os/PowerManagerInternal;

    goto :goto_fb

    nop

    :goto_171
    const v7, 0x111026b

    goto :goto_38

    nop

    :goto_172
    invoke-virtual {v6, v8, v7}, Landroid/os/PowerManager;->newWakeLock(ILjava/lang/String;)Landroid/os/PowerManager$WakeLock;

    move-result-object v6

    goto :goto_6f

    nop

    :goto_173
    const v7, 0x10e00c2

    goto :goto_193

    nop

    :goto_174
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_137

    nop

    :goto_175
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_16e

    nop

    :goto_176
    move-object/from16 v0, p0

    goto :goto_74

    nop

    :goto_177
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_7b

    nop

    :goto_178
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_5a

    nop

    :goto_179
    invoke-virtual {v6}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    goto :goto_53

    nop

    :goto_17a
    invoke-direct {v6, v0, v7}, Lcom/android/server/policy/PhoneWindowManager$SettingsObserver;-><init>(Lcom/android/server/policy/PhoneWindowManager;Landroid/os/Handler;)V

    goto :goto_14c

    nop

    :goto_17b
    move-object/from16 v4, p1

    goto :goto_ce

    nop

    :goto_17c
    iget-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mPackageManager:Landroid/content/pm/PackageManager;

    goto :goto_11d

    nop

    :goto_17d
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mCarDockIntent:Landroid/content/Intent;

    goto :goto_1a0

    nop

    :goto_17e
    iput-boolean v3, v0, Lcom/android/server/policy/PhoneWindowManager;->mWakeOnDpadKeyPress:Z

    nop

    goto :goto_13d

    nop

    :goto_17f
    invoke-virtual {v4}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getWindowWakeUpPolicy()Lcom/android/server/policy/WindowWakeUpPolicy;

    move-result-object v2

    goto :goto_190

    nop

    :goto_180
    new-instance v2, Lcom/android/server/policy/SideFpsEventHandler;

    goto :goto_49

    nop

    :goto_181
    iput-wide v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnPowerAssistantTimeoutMs:J

    goto :goto_cb

    nop

    :goto_182
    invoke-virtual {v1}, Lcom/android/server/ufw/UltraFrameworkServiceFactory;->makeUnisocPhoneWindowManagerUtil()Lcom/android/server/policy/UFwPhoneWindowManagerUtil;

    move-result-object v1

    goto :goto_40

    nop

    :goto_183
    if-nez v10, :cond_5

    goto :goto_67

    :cond_5
    goto :goto_150

    nop

    :goto_184
    check-cast v1, Landroid/hardware/SensorPrivacyManager;

    goto :goto_65

    nop

    :goto_185
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mDisplayManagerInternal:Landroid/hardware/display/DisplayManagerInternal;

    goto :goto_114

    nop

    :goto_186
    invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    nop

    goto :goto_52

    nop

    :goto_187
    new-instance v8, Landroid/content/IntentFilter;

    goto :goto_ff

    nop

    :goto_188
    move v15, v8

    goto :goto_135

    nop

    :goto_189
    invoke-virtual {v6, v8}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v6

    goto :goto_19c

    nop

    :goto_18a
    const v8, 0x10e0177

    goto :goto_b8

    nop

    :goto_18b
    const/4 v2, 0x0

    goto :goto_c4

    nop

    :goto_18c
    iput-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mTalkbackShortcutController:Lcom/android/server/policy/TalkbackShortcutController;

    goto :goto_14f

    nop

    :goto_18d
    iput-boolean v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mHasFeatureLeanback:Z

    goto :goto_4d

    nop

    :goto_18e
    const-class v1, Landroid/service/dreams/DreamManagerInternal;

    goto :goto_e2

    nop

    :goto_18f
    const v3, 0x11102b4

    goto :goto_198

    nop

    :goto_190
    iput-object v2, v0, Lcom/android/server/policy/PhoneWindowManager;->mWindowWakeUpPolicy:Lcom/android/server/policy/WindowWakeUpPolicy;

    goto :goto_164

    nop

    :goto_191
    const v5, 0x111016f

    goto :goto_cf

    nop

    :goto_192
    const-string v7, "android.intent.action.MAIN"

    goto :goto_94

    nop

    :goto_193
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v6

    goto :goto_9d

    nop

    :goto_194
    invoke-virtual/range {p1 .. p1}, Lcom/android/server/policy/PhoneWindowManager$Injector;->getWindowManager()Landroid/view/IWindowManager;

    move-result-object v1

    goto :goto_127

    nop

    :goto_195
    invoke-direct/range {v12 .. v18}, Lcom/android/server/policy/BurnInProtectionHelper;-><init>(Landroid/content/Context;IIIII)V

    goto :goto_ae

    nop

    :goto_196
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mDisplayManager:Landroid/hardware/display/DisplayManager;

    goto :goto_168

    nop

    :goto_197
    iput v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mVeryLongPressOnPowerBehavior:I

    goto :goto_141

    nop

    :goto_198
    invoke-virtual {v1, v3}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v3

    goto :goto_e8

    nop

    :goto_199
    const v7, 0x10e00c1

    goto :goto_51

    nop

    :goto_19a
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mPowerDoublePressTargetActivity:Landroid/content/ComponentName;

    goto :goto_ea

    nop

    :goto_19b
    iget-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_1d

    nop

    :goto_19c
    check-cast v6, Landroid/view/accessibility/AccessibilityManager;

    goto :goto_19e

    nop

    :goto_19d
    const-class v1, Lcom/android/server/wm/ActivityTaskManagerInternal;

    goto :goto_e6

    nop

    :goto_19e
    iput-object v6, v0, Lcom/android/server/policy/PhoneWindowManager;->mAccessibilityManager:Landroid/view/accessibility/AccessibilityManager;

    goto :goto_36

    nop

    :goto_19f
    iput-object v1, v0, Lcom/android/server/policy/PhoneWindowManager;->mLogger:Lcom/android/internal/logging/MetricsLogger;

    goto :goto_1c

    nop

    :goto_1a0
    const-string v10, "android.intent.category.CAR_DOCK"

    goto :goto_ca

    nop

    :goto_1a1
    invoke-virtual {v6, v10}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v10

    goto :goto_111

    nop

    :goto_1a2
    const v7, 0x10e00ba

    goto :goto_10

    nop

    :goto_1a3
    new-instance v6, Lcom/android/server/policy/PhoneWindowManager$7;

    goto :goto_1ae

    nop

    :goto_1a4
    new-instance v6, Lcom/android/server/policy/PhoneWindowManager$MyWakeGestureListener;

    goto :goto_7a

    nop

    :goto_1a5
    invoke-virtual {v6, v7}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v6

    goto :goto_3c

    nop

    :goto_1a6
    invoke-direct {v6, v7, v8}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V

    goto :goto_e

    nop

    :goto_1a7
    check-cast v1, Landroid/hardware/input/InputManager;

    goto :goto_dd

    nop

    :goto_1a8
    invoke-virtual {v1, v2}, Landroid/content/pm/PackageManager;->hasSystemFeature(Ljava/lang/String;)Z

    move-result v1

    goto :goto_71

    nop

    :goto_1a9
    iget-object v9, v0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_160

    nop

    :goto_1aa
    check-cast v1, Lcom/android/server/wm/ActivityTaskManagerInternal;

    goto :goto_4a

    nop

    :goto_1ab
    move v8, v2

    :goto_1ac
    goto :goto_13e

    nop

    :goto_1ad
    invoke-direct {v2, v7, v9, v10}, Lcom/android/server/policy/SideFpsEventHandler;-><init>(Landroid/content/Context;Landroid/os/Handler;Landroid/os/PowerManager;)V

    goto :goto_60

    nop

    :goto_1ae
    invoke-direct {v6, v0, v2}, Lcom/android/server/policy/PhoneWindowManager$7;-><init>(Lcom/android/server/policy/PhoneWindowManager;I)V

    goto :goto_98

    nop

    :goto_1af
    const v7, 0x10e0046

    goto :goto_169

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_initializeHdmiState__V",
        "method":      ".method initializeHdmiState()V",
        "type":        "method_replace",
        "search": """\
.method initializeHdmiState()V
    .registers 3

    invoke-static {}, Landroid/os/StrictMode;->allowThreadDiskReadsMask()I

    move-result v0

    :try_start_0
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->initializeHdmiStateInternal()V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {v0}, Landroid/os/StrictMode;->setThreadPolicyMask(I)V

    nop

    return-void

    :catchall_0
    move-exception v1

    invoke-static {v0}, Landroid/os/StrictMode;->setThreadPolicyMask(I)V

    throw v1
.end method
""",
        "replacement": """\
.method initializeHdmiState()V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    invoke-static {v0}, Landroid/os/StrictMode;->setThreadPolicyMask(I)V

    goto :goto_4

    nop

    :goto_1
    return-void

    :catchall_0
    move-exception v1

    goto :goto_0

    nop

    :goto_2
    invoke-static {v0}, Landroid/os/StrictMode;->setThreadPolicyMask(I)V

    nop

    goto :goto_1

    nop

    :goto_3
    invoke-static {}, Landroid/os/StrictMode;->allowThreadDiskReadsMask()I

    move-result v0

    :try_start_0
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->initializeHdmiStateInternal()V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_2

    nop

    :goto_4
    throw v1
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_initializeHdmiStateInternal__V",
        "method":      ".method initializeHdmiStateInternal()V",
        "type":        "method_replace",
        "search": """\
.method initializeHdmiStateInternal()V
    .registers 12

    const-string v0, "Couldn\\'t read hdmi state from /sys/class/switch/hdmi/state: "

    const-string v1, "WindowManager"

    const/4 v2, 0x0

    invoke-static {}, Lxiaomi/platform/flags/Flags;->qcomEnabled()Z

    move-result v3

    if-eqz v3, :cond_0

    iget-object v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mExtEventObserver:Landroid/os/UEventObserver;

    const-string v4, "mdss_mdp/drm/card"

    invoke-virtual {v3, v4}, Landroid/os/UEventObserver;->startObserving(Ljava/lang/String;)V

    :cond_0
    invoke-static {}, Lxiaomi/platform/flags/Flags;->qcomEnabled()Z

    move-result v3

    if-eqz v3, :cond_1

    iget-object v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mHDMISwitchObserver:Landroid/os/UEventObserver;

    const-string v4, "change@/devices/virtual/graphics/fb2"

    invoke-virtual {v3, v4}, Landroid/os/UEventObserver;->startObserving(Ljava/lang/String;)V

    :cond_1
    new-instance v3, Ljava/io/File;

    const-string v4, "/sys/devices/virtual/switch/hdmi/state"

    invoke-direct {v3, v4}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    invoke-virtual {v3}, Ljava/io/File;->exists()Z

    move-result v3

    const/4 v4, 0x0

    const/4 v5, 0x1

    if-eqz v3, :cond_6

    iget-object v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mHDMIObserver:Landroid/os/UEventObserver;

    const-string v6, "DEVPATH=/devices/virtual/switch/hdmi"

    invoke-virtual {v3, v6}, Landroid/os/UEventObserver;->startObserving(Ljava/lang/String;)V

    const-string v3, "/sys/class/switch/hdmi/state"

    const/4 v6, 0x0

    :try_start_0
    new-instance v7, Ljava/io/FileReader;

    const-string v8, "/sys/class/switch/hdmi/state"

    invoke-direct {v7, v8}, Ljava/io/FileReader;-><init>(Ljava/lang/String;)V

    move-object v6, v7

    const/16 v7, 0xf

    new-array v7, v7, [C

    invoke-virtual {v6, v7}, Ljava/io/FileReader;->read([C)I

    move-result v8

    if-le v8, v5, :cond_3

    new-instance v9, Ljava/lang/String;

    add-int/lit8 v10, v8, -0x1

    invoke-direct {v9, v7, v4, v10}, Ljava/lang/String;-><init>([CII)V

    invoke-static {v9}, Ljava/lang/Integer;->parseInt(Ljava/lang/String;)I

    move-result v0
    :try_end_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_2
    .catch Ljava/lang/NumberFormatException; {:try_start_0 .. :try_end_0} :catch_1
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    if-eqz v0, :cond_2

    move v4, v5

    :cond_2
    move v2, v4

    :cond_3
    nop

    :try_start_1
    invoke-virtual {v6}, Ljava/io/FileReader;->close()V
    :try_end_1
    .catch Ljava/io/IOException; {:try_start_1 .. :try_end_1} :catch_0

    :goto_0
    goto :goto_1

    :catch_0
    move-exception v0

    goto :goto_0

    :catchall_0
    move-exception v0

    goto :goto_2

    :catch_1
    move-exception v4

    :try_start_2
    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v7, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    nop

    if-eqz v6, :cond_4

    :try_start_3
    invoke-virtual {v6}, Ljava/io/FileReader;->close()V
    :try_end_3
    .catch Ljava/io/IOException; {:try_start_3 .. :try_end_3} :catch_0

    goto :goto_0

    :catch_2
    move-exception v4

    :try_start_4
    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v7, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_0

    nop

    if-eqz v6, :cond_4

    :try_start_5
    invoke-virtual {v6}, Ljava/io/FileReader;->close()V
    :try_end_5
    .catch Ljava/io/IOException; {:try_start_5 .. :try_end_5} :catch_0

    goto :goto_0

    :cond_4
    :goto_1
    goto :goto_4

    :goto_2
    if-eqz v6, :cond_5

    :try_start_6
    invoke-virtual {v6}, Ljava/io/FileReader;->close()V
    :try_end_6
    .catch Ljava/io/IOException; {:try_start_6 .. :try_end_6} :catch_3

    goto :goto_3

    :catch_3
    move-exception v1

    :cond_5
    :goto_3
    throw v0

    :cond_6
    const-string v0, "HDMI"

    filled-new-array {v0}, [Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Lcom/android/server/ExtconUEventObserver$ExtconInfo;->getExtconInfoForTypes([Ljava/lang/String;)Ljava/util/List;

    move-result-object v0

    invoke-interface {v0}, Ljava/util/List;->isEmpty()Z

    move-result v1

    if-nez v1, :cond_7

    new-instance v1, Lcom/android/server/policy/PhoneWindowManager$HdmiVideoExtconUEventObserver;

    const/4 v3, 0x0

    invoke-direct {v1, p0, v3}, Lcom/android/server/policy/PhoneWindowManager$HdmiVideoExtconUEventObserver;-><init>(Lcom/android/server/policy/PhoneWindowManager;Lcom/android/server/policy/PhoneWindowManager-IA;)V

    invoke-interface {v0, v4}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lcom/android/server/ExtconUEventObserver$ExtconInfo;

    invoke-static {v1, v3}, Lcom/android/server/policy/PhoneWindowManager$HdmiVideoExtconUEventObserver;->-$$Nest$minit(Lcom/android/server/policy/PhoneWindowManager$HdmiVideoExtconUEventObserver;Lcom/android/server/ExtconUEventObserver$ExtconInfo;)Z

    move-result v2

    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mHDMIObserver:Landroid/os/UEventObserver;

    :cond_7
    :goto_4
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    invoke-virtual {v0, v2, v5}, Lcom/android/server/wm/DisplayPolicy;->setHdmiPlugged(ZZ)V

    return-void
.end method
""",
        "replacement": """\
.method initializeHdmiStateInternal()V
    .registers 12

    goto :goto_1

    nop

    :goto_0
    goto :goto_31

    :catchall_0
    move-exception v0

    goto :goto_4

    nop

    :goto_1
    const-string v0, "Couldn\\'t read hdmi state from /sys/class/switch/hdmi/state: "

    goto :goto_2e

    nop

    :goto_2
    filled-new-array {v0}, [Ljava/lang/String;

    move-result-object v0

    goto :goto_14

    nop

    :goto_3
    invoke-interface {v0}, Ljava/util/List;->isEmpty()Z

    move-result v1

    goto :goto_10

    nop

    :goto_4
    goto :goto_d

    :catch_0
    move-exception v4

    :try_start_0
    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v7, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    nop

    goto :goto_3c

    nop

    :goto_5
    const-string v3, "/sys/class/switch/hdmi/state"

    goto :goto_3b

    nop

    :goto_6
    if-nez v6, :cond_0

    goto :goto_33

    :cond_0
    :try_start_1
    invoke-virtual {v6}, Ljava/io/FileReader;->close()V
    :try_end_1
    .catch Ljava/io/IOException; {:try_start_1 .. :try_end_1} :catch_2

    goto :goto_32

    nop

    :goto_7
    invoke-direct {v3, v4}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    goto :goto_27

    nop

    :goto_8
    if-nez v6, :cond_1

    goto :goto_2a

    :cond_1
    :try_start_2
    invoke-virtual {v6}, Ljava/io/FileReader;->close()V
    :try_end_2
    .catch Ljava/io/IOException; {:try_start_2 .. :try_end_2} :catch_1

    goto :goto_29

    nop

    :goto_9
    iput-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mHDMIObserver:Landroid/os/UEventObserver;

    :goto_a
    goto :goto_36

    nop

    :goto_b
    if-nez v3, :cond_2

    goto :goto_25

    :cond_2
    goto :goto_2c

    nop

    :goto_c
    goto :goto_a

    :goto_d
    goto :goto_8

    nop

    :goto_e
    const/4 v5, 0x1

    goto :goto_21

    nop

    :goto_f
    const-string v6, "DEVPATH=/devices/virtual/switch/hdmi"

    goto :goto_2f

    nop

    :goto_10
    if-eqz v1, :cond_3

    goto :goto_a

    :cond_3
    goto :goto_39

    nop

    :goto_11
    invoke-static {}, Lxiaomi/platform/flags/Flags;->qcomEnabled()Z

    move-result v3

    goto :goto_b

    nop

    :goto_12
    invoke-static {v1, v3}, Lcom/android/server/policy/PhoneWindowManager$HdmiVideoExtconUEventObserver;->-$$Nest$minit(Lcom/android/server/policy/PhoneWindowManager$HdmiVideoExtconUEventObserver;Lcom/android/server/ExtconUEventObserver$ExtconInfo;)Z

    move-result v2

    goto :goto_9

    nop

    :goto_13
    invoke-static {}, Lxiaomi/platform/flags/Flags;->qcomEnabled()Z

    move-result v3

    goto :goto_28

    nop

    :goto_14
    invoke-static {v0}, Lcom/android/server/ExtconUEventObserver$ExtconInfo;->getExtconInfoForTypes([Ljava/lang/String;)Ljava/util/List;

    move-result-object v0

    goto :goto_3

    nop

    :goto_15
    move v4, v5

    :goto_16
    goto :goto_30

    nop

    :goto_17
    const/4 v4, 0x0

    goto :goto_e

    nop

    :goto_18
    throw v0

    :goto_19
    goto :goto_26

    nop

    :goto_1a
    check-cast v3, Lcom/android/server/ExtconUEventObserver$ExtconInfo;

    goto :goto_12

    nop

    :goto_1b
    if-nez v0, :cond_4

    goto :goto_16

    :cond_4
    goto :goto_15

    nop

    :goto_1c
    const-string v4, "change@/devices/virtual/graphics/fb2"

    goto :goto_1e

    nop

    :goto_1d
    invoke-direct {v1, p0, v3}, Lcom/android/server/policy/PhoneWindowManager$HdmiVideoExtconUEventObserver;-><init>(Lcom/android/server/policy/PhoneWindowManager;Lcom/android/server/policy/PhoneWindowManager-IA;)V

    goto :goto_35

    nop

    :goto_1e
    invoke-virtual {v3, v4}, Landroid/os/UEventObserver;->startObserving(Ljava/lang/String;)V

    :goto_1f
    goto :goto_37

    nop

    :goto_20
    iget-object v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mHDMISwitchObserver:Landroid/os/UEventObserver;

    goto :goto_1c

    nop

    :goto_21
    if-nez v3, :cond_5

    goto :goto_19

    :cond_5
    goto :goto_2b

    nop

    :goto_22
    return-void

    :goto_23
    const-string v4, "mdss_mdp/drm/card"

    goto :goto_24

    nop

    :goto_24
    invoke-virtual {v3, v4}, Landroid/os/UEventObserver;->startObserving(Ljava/lang/String;)V

    :goto_25
    goto :goto_13

    nop

    :goto_26
    const-string v0, "HDMI"

    goto :goto_2

    nop

    :goto_27
    invoke-virtual {v3}, Ljava/io/File;->exists()Z

    move-result v3

    goto :goto_17

    nop

    :goto_28
    if-nez v3, :cond_6

    goto :goto_1f

    :cond_6
    goto :goto_20

    nop

    :goto_29
    goto :goto_2a

    :catch_1
    move-exception v1

    :goto_2a
    goto :goto_18

    nop

    :goto_2b
    iget-object v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mHDMIObserver:Landroid/os/UEventObserver;

    goto :goto_f

    nop

    :goto_2c
    iget-object v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mExtEventObserver:Landroid/os/UEventObserver;

    goto :goto_23

    nop

    :goto_2d
    const-string v4, "/sys/devices/virtual/switch/hdmi/state"

    goto :goto_7

    nop

    :goto_2e
    const-string v1, "WindowManager"

    goto :goto_34

    nop

    :goto_2f
    invoke-virtual {v3, v6}, Landroid/os/UEventObserver;->startObserving(Ljava/lang/String;)V

    goto :goto_5

    nop

    :goto_30
    move v2, v4

    :cond_7
    nop

    :try_start_3
    invoke-virtual {v6}, Ljava/io/FileReader;->close()V
    :try_end_3
    .catch Ljava/io/IOException; {:try_start_3 .. :try_end_3} :catch_2

    :goto_31
    goto :goto_3a

    nop

    :goto_32
    goto :goto_31

    :goto_33
    goto :goto_c

    nop

    :goto_34
    const/4 v2, 0x0

    goto :goto_11

    nop

    :goto_35
    invoke-interface {v0, v4}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v3

    goto :goto_1a

    nop

    :goto_36
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    goto :goto_38

    nop

    :goto_37
    new-instance v3, Ljava/io/File;

    goto :goto_2d

    nop

    :goto_38
    invoke-virtual {v0, v2, v5}, Lcom/android/server/wm/DisplayPolicy;->setHdmiPlugged(ZZ)V

    goto :goto_22

    nop

    :goto_39
    new-instance v1, Lcom/android/server/policy/PhoneWindowManager$HdmiVideoExtconUEventObserver;

    goto :goto_3d

    nop

    :goto_3a
    goto :goto_33

    :catch_2
    move-exception v0

    goto :goto_0

    nop

    :goto_3b
    const/4 v6, 0x0

    :try_start_4
    new-instance v7, Ljava/io/FileReader;

    const-string v8, "/sys/class/switch/hdmi/state"

    invoke-direct {v7, v8}, Ljava/io/FileReader;-><init>(Ljava/lang/String;)V

    move-object v6, v7

    const/16 v7, 0xf

    new-array v7, v7, [C

    invoke-virtual {v6, v7}, Ljava/io/FileReader;->read([C)I

    move-result v8

    if-le v8, v5, :cond_7

    new-instance v9, Ljava/lang/String;

    add-int/lit8 v10, v8, -0x1

    invoke-direct {v9, v7, v4, v10}, Ljava/lang/String;-><init>([CII)V

    invoke-static {v9}, Ljava/lang/Integer;->parseInt(Ljava/lang/String;)I

    move-result v0
    :try_end_4
    .catch Ljava/io/IOException; {:try_start_4 .. :try_end_4} :catch_3
    .catch Ljava/lang/NumberFormatException; {:try_start_4 .. :try_end_4} :catch_0
    .catchall {:try_start_4 .. :try_end_4} :catchall_0

    goto :goto_1b

    nop

    :goto_3c
    if-nez v6, :cond_8

    goto :goto_33

    :cond_8
    :try_start_5
    invoke-virtual {v6}, Ljava/io/FileReader;->close()V
    :try_end_5
    .catch Ljava/io/IOException; {:try_start_5 .. :try_end_5} :catch_2

    goto :goto_3e

    nop

    :goto_3d
    const/4 v3, 0x0

    goto :goto_1d

    nop

    :goto_3e
    goto :goto_31

    :catch_3
    move-exception v4

    :try_start_6
    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v7, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_6
    .catchall {:try_start_6 .. :try_end_6} :catchall_0

    nop

    goto :goto_6

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_interceptKeyBeforeQueueing_Landroid_view_KeyEvent_I_I",
        "method":      ".method public interceptKeyBeforeQueueing(Landroid/view/KeyEvent;I)I",
        "type":        "method_replace",
        "search": """\
.method public interceptKeyBeforeQueueing(Landroid/view/KeyEvent;I)I
    .registers 37

    move-object/from16 v1, p0

    move-object/from16 v2, p1

    move/from16 v3, p2

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getKeyCode()I

    move-result v4

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getAction()I

    move-result v0

    const/4 v5, 0x0

    if-nez v0, :cond_0

    const/4 v0, 0x1

    goto :goto_0

    :cond_0
    move v0, v5

    :goto_0
    move v7, v0

    and-int/lit8 v0, v3, 0x1

    if-nez v0, :cond_2

    invoke-virtual {v2}, Landroid/view/KeyEvent;->isWakeKey()Z

    move-result v0

    if-eqz v0, :cond_1

    goto :goto_1

    :cond_1
    move v0, v5

    goto :goto_2

    :cond_2
    :goto_1
    const/4 v0, 0x1

    :goto_2
    const/high16 v8, 0x40000

    and-int/2addr v8, v3

    if-eqz v8, :cond_3

    const/4 v8, 0x1

    goto :goto_3

    :cond_3
    move v8, v5

    :goto_3
    iget-boolean v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mVisibleBackgroundUsersEnabled:Z

    const/4 v10, 0x0

    if-eqz v9, :cond_4

    invoke-static {v4}, Landroid/view/KeyEvent;->isVisibleBackgroundUserAllowedKey(I)Z

    move-result v9

    if-nez v9, :cond_4

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDisplayId()I

    move-result v9

    invoke-direct {v1, v9, v4, v10}, Lcom/android/server/policy/PhoneWindowManager;->isKeyEventForCurrentUser(IILjava/lang/String;)Z

    move-result v9

    if-nez v9, :cond_4

    return v5

    :cond_4
    invoke-static {}, Lxiaomi/platform/flags/Flags;->mtkEnabled()Z

    move-result v9

    const-string v11, "WindowManager"

    if-eqz v9, :cond_6

    const-string v9, "sys.hu.status"

    invoke-static {v9, v10}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v9

    if-eqz v9, :cond_6

    const-string v10, ""

    invoke-virtual {v9, v10}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v10

    if-nez v10, :cond_6

    const-string v10, "shutdown"

    invoke-virtual {v9, v10}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v10

    if-nez v10, :cond_5

    const-string v10, "boot_started"

    invoke-virtual {v9, v10}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v10

    if-eqz v10, :cond_6

    :cond_5
    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v10, "IPO skip key request when huStatus is "

    invoke-virtual {v6, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v11, v6}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    return v5

    :cond_6
    iget-boolean v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mSystemBooted:Z

    const/16 v10, 0xb1

    const/16 v12, 0x1a

    if-nez v9, :cond_c

    const/4 v6, 0x0

    if-eqz v7, :cond_8

    if-eq v4, v12, :cond_7

    if-ne v4, v10, :cond_8

    :cond_7
    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->wakeUpFromWakeKey(Landroid/view/KeyEvent;)V

    const/4 v6, 0x1

    goto :goto_4

    :cond_8
    if-eqz v7, :cond_a

    if-nez v0, :cond_9

    const/16 v9, 0xe0

    if-ne v4, v9, :cond_a

    :cond_9
    invoke-direct {v1, v4}, Lcom/android/server/policy/PhoneWindowManager;->isWakeKeyWhenScreenOff(I)Z

    move-result v9

    if-eqz v9, :cond_a

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->wakeUpFromWakeKey(Landroid/view/KeyEvent;)V

    const/4 v6, 0x1

    :cond_a
    :goto_4
    if-eqz v6, :cond_b

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->getHdmiControl()Lcom/android/server/policy/PhoneWindowManager$HdmiControl;

    move-result-object v9

    if-eqz v9, :cond_b

    invoke-virtual {v9}, Lcom/android/server/policy/PhoneWindowManager$HdmiControl;->turnOnTv()V

    :cond_b
    return v5

    :cond_c
    const/high16 v9, 0x20000000

    and-int/2addr v9, v3

    if-eqz v9, :cond_d

    const/4 v9, 0x1

    goto :goto_5

    :cond_d
    move v9, v5

    :goto_5
    invoke-virtual {v2}, Landroid/view/KeyEvent;->isCanceled()Z

    move-result v13

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDisplayId()I

    move-result v14

    const/high16 v15, 0x1000000

    and-int/2addr v15, v3

    if-eqz v15, :cond_e

    const/4 v15, 0x1

    goto :goto_6

    :cond_e
    move v15, v5

    :goto_6
    move/from16 v16, v5

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getKeyCode()I

    move-result v5

    if-ne v5, v12, :cond_f

    if-eqz v7, :cond_f

    iget-object v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mSideFpsEventHandler:Lcom/android/server/policy/SideFpsEventHandler;

    invoke-virtual {v5}, Lcom/android/server/policy/SideFpsEventHandler;->notifyPowerPressed()V

    :cond_f
    sget-boolean v5, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    if-eqz v5, :cond_12

    iget-object v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    if-eqz v5, :cond_11

    if-eqz v9, :cond_10

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardShowingAndNotOccluded()Z

    move-result v5

    if-eqz v5, :cond_11

    goto :goto_7

    :cond_10
    iget-object v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    invoke-virtual {v5}, Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;->isShowing()Z

    move-result v5

    if-eqz v5, :cond_11

    :goto_7
    const/4 v5, 0x1

    goto :goto_8

    :cond_11
    move/from16 v5, v16

    :goto_8
    new-instance v12, Ljava/lang/StringBuilder;

    invoke-direct {v12}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "interceptKeyTq keycode="

    invoke-virtual {v12, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v12, " interactive="

    invoke-virtual {v6, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v9}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v12, " keyguardActive="

    invoke-virtual {v6, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v5}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v12, " policyFlags="

    invoke-virtual {v6, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-static {v3}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;

    move-result-object v12

    invoke-virtual {v6, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v11, v6}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_12
    invoke-static {}, Lcom/android/server/policy/PhoneWindowManagerStub;->getInstance()Lcom/android/server/policy/PhoneWindowManagerStub;

    move-result-object v5

    invoke-interface {v5, v2}, Lcom/android/server/policy/PhoneWindowManagerStub;->interceptKeyBeforeQueueing(Landroid/view/KeyEvent;)Z

    move-result v5

    if-eqz v5, :cond_13

    return v16

    :cond_13
    invoke-static {}, Lxiaomi/platform/flags/Flags;->mtkEnabled()Z

    move-result v5

    const/4 v6, -0x1

    if-eqz v5, :cond_14

    if-nez v9, :cond_14

    if-eqz v15, :cond_14

    if-nez v0, :cond_14

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v12, "Inject keyevent when screen off. ignore! keyevent="

    invoke-virtual {v5, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v11, v5}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    const/4 v5, 0x0

    move v12, v5

    move v5, v0

    goto :goto_a

    :cond_14
    if-nez v9, :cond_1a

    if-eqz v15, :cond_15

    if-nez v0, :cond_15

    goto :goto_9

    :cond_15
    invoke-direct {v1, v14, v4}, Lcom/android/server/policy/PhoneWindowManager;->shouldDispatchInputWhenNonInteractive(II)Z

    move-result v5

    if-eqz v5, :cond_16

    const/4 v5, 0x1

    iput v6, v1, Lcom/android/server/policy/PhoneWindowManager;->mPendingWakeKey:I

    move v12, v5

    move v5, v0

    goto :goto_a

    :cond_16
    const/4 v5, 0x0

    if-eqz v0, :cond_18

    if-eqz v7, :cond_17

    invoke-direct {v1, v4}, Lcom/android/server/policy/PhoneWindowManager;->isWakeKeyWhenScreenOff(I)Z

    move-result v12

    if-nez v12, :cond_18

    :cond_17
    const/4 v0, 0x0

    :cond_18
    if-eqz v0, :cond_19

    if-eqz v7, :cond_19

    iput v4, v1, Lcom/android/server/policy/PhoneWindowManager;->mPendingWakeKey:I

    :cond_19
    move v12, v5

    move v5, v0

    goto :goto_a

    :cond_1a
    :goto_9
    const/4 v5, 0x1

    const/4 v0, 0x0

    if-eqz v9, :cond_1c

    iget v12, v1, Lcom/android/server/policy/PhoneWindowManager;->mPendingWakeKey:I

    if-ne v4, v12, :cond_1b

    if-nez v7, :cond_1b

    const/4 v5, 0x0

    :cond_1b
    iput v6, v1, Lcom/android/server/policy/PhoneWindowManager;->mPendingWakeKey:I

    move v12, v5

    move v5, v0

    goto :goto_a

    :cond_1c
    move v12, v5

    move v5, v0

    :goto_a
    invoke-static {v4}, Lcom/android/server/policy/PhoneWindowManager;->isValidGlobalKey(I)Z

    move-result v0

    if-eqz v0, :cond_1f

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mGlobalKeyManager:Lcom/android/server/policy/GlobalKeyManager;

    invoke-virtual {v0, v4}, Lcom/android/server/policy/GlobalKeyManager;->shouldHandleGlobalKey(I)Z

    move-result v0

    if-eqz v0, :cond_1f

    if-nez v9, :cond_1d

    if-eqz v5, :cond_1d

    if-eqz v7, :cond_1d

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mGlobalKeyManager:Lcom/android/server/policy/GlobalKeyManager;

    invoke-virtual {v0, v4}, Lcom/android/server/policy/GlobalKeyManager;->shouldDispatchFromNonInteractive(I)Z

    move-result v0

    if-eqz v0, :cond_1d

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mGlobalKeyManager:Lcom/android/server/policy/GlobalKeyManager;

    invoke-virtual {v0}, Lcom/android/server/policy/GlobalKeyManager;->setBeganFromNonInteractive()V

    const/4 v12, 0x1

    iput v6, v1, Lcom/android/server/policy/PhoneWindowManager;->mPendingWakeKey:I

    :cond_1d
    if-eqz v5, :cond_1e

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->wakeUpFromWakeKey(Landroid/view/KeyEvent;)V

    :cond_1e
    return v12

    :cond_1f
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->getHdmiControlManager()Landroid/hardware/hdmi/HdmiControlManager;

    move-result-object v19

    if-ne v4, v10, :cond_21

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHasFeatureLeanback:Z

    if-eqz v0, :cond_21

    if-eqz v19, :cond_20

    invoke-virtual/range {v19 .. v19}, Landroid/hardware/hdmi/HdmiControlManager;->shouldHandleTvPowerKey()Z

    move-result v0

    if-nez v0, :cond_21

    :cond_20
    nop

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDownTime()J

    move-result-wide v20

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getEventTime()J

    move-result-wide v22

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getAction()I

    move-result v24

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v26

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getMetaState()I

    move-result v27

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDeviceId()I

    move-result v28

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getScanCode()I

    move-result v29

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getFlags()I

    move-result v30

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getSource()I

    move-result v31

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDisplayId()I

    move-result v32

    const/16 v25, 0x1a

    const/16 v33, 0x0

    invoke-static/range {v20 .. v33}, Landroid/view/KeyEvent;->obtain(JJIIIIIIIIILjava/lang/String;)Landroid/view/KeyEvent;

    move-result-object v0

    invoke-virtual {v1, v0, v3}, Lcom/android/server/policy/PhoneWindowManager;->interceptKeyBeforeQueueing(Landroid/view/KeyEvent;I)I

    move-result v2

    return v2

    :cond_21
    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplay:Landroid/view/Display;

    invoke-virtual {v0}, Landroid/view/Display;->getState()I

    move-result v0

    invoke-static {v0}, Landroid/view/Display;->isOnState(I)Z

    move-result v10

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    invoke-virtual {v0}, Lcom/android/server/wm/DisplayPolicy;->isAwake()Z

    move-result v20

    if-eqz v9, :cond_22

    if-eqz v20, :cond_22

    const/4 v0, 0x1

    goto :goto_b

    :cond_22
    move/from16 v0, v16

    :goto_b
    move/from16 v21, v0

    if-eqz v8, :cond_23

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mSingleKeyGestureDetector:Lcom/android/server/policy/SingleKeyGestureDetector;

    invoke-virtual {v0}, Lcom/android/server/policy/SingleKeyGestureDetector;->reset()V

    move/from16 v6, v21

    goto :goto_c

    :cond_23
    invoke-virtual {v2}, Landroid/view/KeyEvent;->getFlags()I

    move-result v0

    and-int/lit16 v0, v0, 0x400

    if-nez v0, :cond_25

    invoke-static {}, Lcom/android/server/policy/PhoneWindowManagerStub;->getInstance()Lcom/android/server/policy/PhoneWindowManagerStub;

    move-result-object v0

    invoke-interface {v0, v2}, Lcom/android/server/policy/PhoneWindowManagerStub;->skipKeyGesutre(Landroid/view/KeyEvent;)Z

    move-result v0

    if-nez v0, :cond_24

    move/from16 v6, v21

    invoke-direct {v1, v2, v6, v10}, Lcom/android/server/policy/PhoneWindowManager;->handleKeyGesture(Landroid/view/KeyEvent;ZZ)V

    goto :goto_c

    :cond_24
    move/from16 v6, v21

    goto :goto_c

    :cond_25
    move/from16 v6, v21

    :goto_c
    invoke-virtual {v2}, Landroid/view/KeyEvent;->getFlags()I

    move-result v0

    and-int/lit8 v0, v0, 0x40

    if-eqz v0, :cond_26

    const/4 v0, 0x1

    goto :goto_d

    :cond_26
    move/from16 v0, v16

    :goto_d
    move/from16 v21, v0

    if-eqz v7, :cond_28

    and-int/lit8 v0, v3, 0x2

    if-eqz v0, :cond_28

    if-eqz v21, :cond_27

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mNavBarVirtualKeyHapticFeedbackEnabled:Z

    if-eqz v0, :cond_28

    :cond_27
    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-nez v0, :cond_28

    const/4 v0, 0x1

    goto :goto_e

    :cond_28
    move/from16 v0, v16

    :goto_e
    move/from16 v23, v0

    const/16 v0, 0x22

    const/4 v3, 0x3

    sparse-switch v4, :sswitch_data_0

    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1b

    :sswitch_0
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/com/android/hardware/input/Flags;->enableNew25q2Keycodes()Z

    move-result v0

    if-nez v0, :cond_29

    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1c

    :cond_29
    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1b

    :sswitch_1
    invoke-static {}, Lcom/android/server/policy/PhoneWindowManagerStub;->getInstance()Lcom/android/server/policy/PhoneWindowManagerStub;

    move-result-object v0

    invoke-interface {v0, v2}, Lcom/android/server/policy/PhoneWindowManagerStub;->skipInterceptMacroEvent(Landroid/view/KeyEvent;)Z

    move-result v0

    if-eqz v0, :cond_2a

    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1b

    :cond_2a
    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1c

    :sswitch_2
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Stylus buttons event: "

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v3, " received. Should handle event? "

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    iget-boolean v3, v1, Lcom/android/server/policy/PhoneWindowManager;->mStylusButtonsEnabled:Z

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v11, v0}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mStylusButtonsEnabled:Z

    if-eqz v0, :cond_2b

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->sendSystemKeyToStatusBarAsync(Landroid/view/KeyEvent;)V

    :cond_2b
    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1c

    :sswitch_3
    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1c

    :sswitch_4
    const/16 v0, 0x23

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    and-int/lit8 v12, v12, -0x2

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->interceptSystemNavigationKey(Landroid/view/KeyEvent;)V

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1c

    :sswitch_5
    const/16 v0, 0x24

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    and-int/lit8 v12, v12, -0x2

    const/4 v5, 0x0

    if-nez v7, :cond_2c

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerManagerInternal:Landroid/os/PowerManagerInternal;

    invoke-virtual {v0}, Landroid/os/PowerManagerInternal;->setUserInactiveOverrideFromWindowManager()V

    :cond_2c
    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->sendSystemKeyToStatusBarAsync(Landroid/view/KeyEvent;)V

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1c

    :sswitch_6
    if-eqz v7, :cond_2d

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-nez v0, :cond_2d

    and-int/lit8 v0, v12, 0x1

    if-nez v0, :cond_2d

    move/from16 v25, v9

    move/from16 v26, v10

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDownTime()J

    move-result-wide v9

    invoke-direct {v1, v4, v9, v10}, Lcom/android/server/policy/PhoneWindowManager;->setDeferredKeyActionsExecutableAsync(IJ)V

    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_2d
    move/from16 v25, v9

    move/from16 v26, v10

    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :sswitch_7
    move/from16 v25, v9

    move/from16 v26, v10

    if-nez v7, :cond_2e

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->acquire()V

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    const/16 v3, 0xc

    invoke-virtual {v0, v3}, Landroid/os/Handler;->obtainMessage(I)Landroid/os/Message;

    move-result-object v0

    const/4 v3, 0x1

    invoke-virtual {v0, v3}, Landroid/os/Message;->setAsynchronous(Z)V

    invoke-virtual {v0}, Landroid/os/Message;->sendToTarget()V

    const/4 v3, 0x6

    invoke-direct {v1, v2, v3}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompleted(Landroid/view/KeyEvent;I)V

    :cond_2e
    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1c

    :sswitch_8
    move/from16 v25, v9

    move/from16 v26, v10

    const/16 v0, 0x25

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    and-int/lit8 v12, v12, -0x2

    const/4 v5, 0x1

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1c

    :sswitch_9
    move/from16 v25, v9

    move/from16 v26, v10

    const/16 v0, 0x24

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    and-int/lit8 v12, v12, -0x2

    const/4 v5, 0x0

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    invoke-virtual {v0}, Landroid/os/PowerManager;->isInteractive()Z

    move-result v0

    if-nez v0, :cond_2f

    const/16 v23, 0x0

    :cond_2f
    if-eqz v7, :cond_30

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->sleepPress()V

    goto :goto_f

    :cond_30
    invoke-virtual {v2}, Landroid/view/KeyEvent;->getEventTime()J

    move-result-wide v9

    invoke-direct {v1, v9, v10}, Lcom/android/server/policy/PhoneWindowManager;->sleepRelease(J)V

    :goto_f
    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->sendSystemKeyToStatusBarAsync(Landroid/view/KeyEvent;)V

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1c

    :sswitch_a
    move/from16 v25, v9

    move/from16 v26, v10

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-lez v0, :cond_31

    const/4 v0, 0x1

    goto :goto_10

    :cond_31
    move/from16 v0, v16

    :goto_10
    if-eqz v7, :cond_32

    if-nez v0, :cond_32

    iget-object v3, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDeviceId()I

    move-result v9

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getEventTime()J

    move-result-wide v27

    invoke-static/range {v27 .. v28}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v10

    move/from16 v17, v0

    const/16 v0, 0x17

    move/from16 v24, v5

    move/from16 v5, v16

    invoke-virtual {v3, v0, v9, v5, v10}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object v0

    const/4 v3, 0x1

    invoke-virtual {v0, v3}, Landroid/os/Message;->setAsynchronous(Z)V

    invoke-virtual {v0}, Landroid/os/Message;->sendToTarget()V

    const/4 v3, 0x5

    invoke-direct {v1, v2, v3}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompleted(Landroid/view/KeyEvent;I)V

    goto :goto_11

    :cond_32
    move/from16 v17, v0

    move/from16 v24, v5

    :goto_11
    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v5, v24

    goto :goto_1c

    :sswitch_b
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    and-int/lit8 v12, v12, -0x2

    const/4 v5, 0x0

    if-eqz v7, :cond_33

    if-eqz v19, :cond_33

    invoke-virtual/range {v19 .. v19}, Landroid/hardware/hdmi/HdmiControlManager;->toggleAndFollowTvPower()V

    :cond_33
    :goto_12
    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1c

    :sswitch_c
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    iget v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mShortPressOnWindowBehavior:I

    const/4 v3, 0x1

    if-ne v0, v3, :cond_36

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mPictureInPictureVisible:Z

    if-eqz v0, :cond_35

    if-nez v7, :cond_34

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->showPictureInPictureMenu(Landroid/view/KeyEvent;)V

    :cond_34
    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v5, v24

    goto :goto_1c

    :cond_35
    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_36
    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :sswitch_d
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    and-int/lit8 v12, v12, -0x2

    if-eqz v7, :cond_37

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-nez v0, :cond_37

    const/16 v0, 0x1a

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompleted(Landroid/view/KeyEvent;I)V

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->toggleMicrophoneMuteFromKey()V

    :cond_37
    :goto_13
    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v5, v24

    goto :goto_1c

    :sswitch_e
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    const/16 v0, 0x26

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-static {v0}, Landroid/media/session/MediaSessionLegacyHelper;->getHelper(Landroid/content/Context;)Landroid/media/session/MediaSessionLegacyHelper;

    move-result-object v0

    invoke-virtual {v0}, Landroid/media/session/MediaSessionLegacyHelper;->isGlobalPriorityActive()Z

    move-result v0

    if-eqz v0, :cond_38

    and-int/lit8 v12, v12, -0x2

    :cond_38
    and-int/lit8 v0, v12, 0x1

    if-nez v0, :cond_37

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->acquire()V

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    new-instance v5, Landroid/view/KeyEvent;

    invoke-direct {v5, v2}, Landroid/view/KeyEvent;-><init>(Landroid/view/KeyEvent;)V

    invoke-virtual {v0, v3, v5}, Landroid/os/Handler;->obtainMessage(ILjava/lang/Object;)Landroid/os/Message;

    move-result-object v0

    const/4 v3, 0x1

    invoke-virtual {v0, v3}, Landroid/os/Message;->setAsynchronous(Z)V

    invoke-virtual {v0}, Landroid/os/Message;->sendToTarget()V

    goto :goto_13

    :sswitch_f
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    if-eqz v7, :cond_3a

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-nez v0, :cond_3a

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getMetaState()I

    move-result v0

    and-int/lit16 v0, v0, -0xc2

    const/16 v3, 0x1000

    invoke-static {v0, v3}, Landroid/view/KeyEvent;->metaStateHasModifiers(II)Z

    move-result v0

    if-eqz v0, :cond_39

    new-instance v0, Landroid/view/KeyEvent;

    invoke-direct {v0, v2}, Landroid/view/KeyEvent;-><init>(Landroid/view/KeyEvent;)V

    invoke-direct {v1, v0}, Lcom/android/server/policy/PhoneWindowManager;->handleSwitchKeyboardLayoutToast(Landroid/view/KeyEvent;)V

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_39
    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_3a
    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :sswitch_10
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    nop

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getAction()I

    move-result v0

    invoke-static {v0}, Landroid/view/KeyEvent;->actionToString(I)Ljava/lang/String;

    move-result-object v0

    iget-boolean v3, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerKeyHandled:Z

    iget-object v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mSingleKeyGestureDetector:Lcom/android/server/policy/SingleKeyGestureDetector;

    const/16 v9, 0x1a

    invoke-virtual {v5, v9}, Lcom/android/server/policy/SingleKeyGestureDetector;->getKeyPressCounter(I)I

    move-result v5

    invoke-static {v0, v3, v5}, Lcom/android/server/policy/EventLogTags;->writeInterceptPower(Ljava/lang/String;II)V

    and-int/lit8 v12, v12, -0x2

    const/4 v5, 0x0

    if-eqz v7, :cond_3b

    invoke-direct {v1, v2, v6, v8}, Lcom/android/server/policy/PhoneWindowManager;->interceptPowerKeyDown(Landroid/view/KeyEvent;ZZ)V

    goto :goto_12

    :cond_3b
    invoke-direct {v1, v2, v13}, Lcom/android/server/policy/PhoneWindowManager;->interceptPowerKeyUp(Landroid/view/KeyEvent;Z)V

    goto :goto_12

    :sswitch_11
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    const/16 v0, 0x19

    if-ne v4, v0, :cond_3c

    const/16 v0, 0x13

    goto :goto_14

    :cond_3c
    const/16 v0, 0x18

    if-ne v4, v0, :cond_3d

    const/16 v0, 0x12

    goto :goto_14

    :cond_3d
    const/16 v0, 0x14

    :goto_14
    move v5, v0

    invoke-direct {v1, v2, v5}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionDown(Landroid/view/KeyEvent;I)V

    if-eqz v7, :cond_44

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->sendSystemKeyToStatusBarAsync(Landroid/view/KeyEvent;)V

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getNotificationService()Landroid/app/NotificationManager;

    move-result-object v10

    if-eqz v10, :cond_3e

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandleVolumeKeysInWM:Z

    if-nez v0, :cond_3e

    invoke-virtual {v10}, Landroid/app/NotificationManager;->silenceNotificationSound()V

    :cond_3e
    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getTelecommService()Landroid/telecom/TelecomManager;

    move-result-object v17

    if-eqz v17, :cond_3f

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandleVolumeKeysInWM:Z

    if-nez v0, :cond_3f

    invoke-virtual/range {v17 .. v17}, Landroid/telecom/TelecomManager;->isRinging()Z

    move-result v0

    if-eqz v0, :cond_3f

    const-string v0, "interceptKeyBeforeQueueing: VOLUME key-down while ringing: Silence ringer!"

    invoke-static {v11, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual/range {v17 .. v17}, Landroid/telecom/TelecomManager;->silenceRinger()V

    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v5, v24

    goto :goto_1c

    :cond_3f
    const/16 v27, 0x0

    :try_start_0
    invoke-static {}, Lcom/android/server/policy/PhoneWindowManager;->getAudioService()Landroid/media/IAudioService;

    move-result-object v0

    invoke-interface {v0}, Landroid/media/IAudioService;->getMode()I

    move-result v0
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    move/from16 v27, v0

    goto :goto_15

    :catch_0
    move-exception v0

    const-string v9, "Error getting AudioService in interceptKeyBeforeQueueing."

    invoke-static {v11, v9, v0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    move/from16 v0, v27

    :goto_15
    if-eqz v17, :cond_40

    invoke-virtual/range {v17 .. v17}, Landroid/telecom/TelecomManager;->isInCall()Z

    move-result v9

    if-nez v9, :cond_41

    :cond_40
    if-ne v0, v3, :cond_42

    :cond_41
    const/4 v3, 0x1

    goto :goto_16

    :cond_42
    const/4 v3, 0x0

    :goto_16
    if-eqz v3, :cond_43

    and-int/lit8 v9, v12, 0x1

    if-nez v9, :cond_43

    iget-object v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-static {v9}, Landroid/media/session/MediaSessionLegacyHelper;->getHelper(Landroid/content/Context;)Landroid/media/session/MediaSessionLegacyHelper;

    move-result-object v9

    move/from16 v27, v3

    move/from16 v16, v5

    const/high16 v3, -0x80000000

    const/4 v5, 0x0

    invoke-virtual {v9, v2, v3, v5}, Landroid/media/session/MediaSessionLegacyHelper;->sendVolumeKeyEvent(Landroid/view/KeyEvent;IZ)V

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_43
    move/from16 v27, v3

    move/from16 v16, v5

    goto :goto_17

    :cond_44
    move/from16 v16, v5

    :goto_17
    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mUseTvRouting:Z

    if-nez v0, :cond_47

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandleVolumeKeysInWM:Z

    if-eqz v0, :cond_45

    goto :goto_18

    :cond_45
    and-int/lit8 v0, v12, 0x1

    if-nez v0, :cond_46

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-static {v0}, Landroid/media/session/MediaSessionLegacyHelper;->getHelper(Landroid/content/Context;)Landroid/media/session/MediaSessionLegacyHelper;

    move-result-object v0

    const/high16 v3, -0x80000000

    const/4 v5, 0x1

    invoke-virtual {v0, v2, v3, v5}, Landroid/media/session/MediaSessionLegacyHelper;->sendVolumeKeyEvent(Landroid/view/KeyEvent;IZ)V

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_46
    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_47
    :goto_18
    or-int/lit8 v12, v12, 0x1

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v5, v24

    goto :goto_1c

    :sswitch_12
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    and-int/lit8 v12, v12, -0x2

    if-eqz v7, :cond_4a

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getTelecommService()Landroid/telecom/TelecomManager;

    move-result-object v0

    const/4 v3, 0x0

    if-eqz v0, :cond_48

    invoke-virtual {v0}, Landroid/telecom/TelecomManager;->endCall()Z

    move-result v3

    :cond_48
    if-eqz v25, :cond_49

    if-nez v3, :cond_49

    const/4 v5, 0x0

    iput-boolean v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndCallKeyHandled:Z

    iget-object v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    iget-object v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndCallLongPress:Ljava/lang/Runnable;

    iget-object v10, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-static {v10}, Landroid/view/ViewConfiguration;->get(Landroid/content/Context;)Landroid/view/ViewConfiguration;

    move-result-object v10

    move/from16 v27, v6

    move/from16 v17, v7

    invoke-virtual {v10}, Landroid/view/ViewConfiguration;->getDeviceGlobalActionKeyTimeout()J

    move-result-wide v6

    invoke-virtual {v5, v9, v6, v7}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    goto :goto_19

    :cond_49
    move/from16 v27, v6

    move/from16 v17, v7

    const/4 v5, 0x1

    iput-boolean v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndCallKeyHandled:Z

    :goto_19
    goto :goto_1b

    :cond_4a
    move/from16 v27, v6

    move/from16 v17, v7

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndCallKeyHandled:Z

    if-nez v0, :cond_51

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    iget-object v3, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndCallLongPress:Ljava/lang/Runnable;

    invoke-virtual {v0, v3}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    if-nez v13, :cond_51

    iget v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndcallBehavior:I

    const/16 v18, 0x1

    and-int/lit8 v0, v0, 0x1

    if-eqz v0, :cond_4b

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->goHome()Z

    move-result v0

    if-eqz v0, :cond_4b

    goto :goto_1b

    :cond_4b
    iget v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndcallBehavior:I

    and-int/lit8 v0, v0, 0x2

    if-eqz v0, :cond_51

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getEventTime()J

    move-result-wide v5

    const/4 v0, 0x4

    const/4 v3, 0x0

    invoke-direct {v1, v5, v6, v0, v3}, Lcom/android/server/policy/PhoneWindowManager;->sleepDefaultDisplay(JII)V

    const/4 v5, 0x0

    goto :goto_1c

    :sswitch_13
    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    if-eqz v17, :cond_51

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getTelecommService()Landroid/telecom/TelecomManager;

    move-result-object v0

    if-eqz v0, :cond_4c

    invoke-virtual {v0}, Landroid/telecom/TelecomManager;->isRinging()Z

    move-result v3

    if-eqz v3, :cond_4c

    const-string v3, "interceptKeyBeforeQueueing: CALL key-down while ringing: Answer the call!"

    invoke-static {v11, v3}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {v0}, Landroid/telecom/TelecomManager;->acceptRingingCall()V

    and-int/lit8 v12, v12, -0x2

    :cond_4c
    move/from16 v5, v24

    goto :goto_1c

    :sswitch_14
    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    invoke-direct {v1, v2, v3}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    if-eqz v17, :cond_4f

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-lez v0, :cond_4d

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getFlags()I

    move-result v0

    and-int/lit16 v0, v0, 0x80

    if-eqz v0, :cond_4d

    const/4 v3, 0x1

    goto :goto_1a

    :cond_4d
    const/4 v3, 0x0

    :goto_1a
    if-nez v3, :cond_4e

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerInternal:Lcom/android/server/wm/WindowManagerInternal;

    invoke-virtual {v0}, Lcom/android/server/wm/WindowManagerInternal;->moveFocusToAdjacentEmbeddedActivityIfNeeded()Z

    const/4 v5, 0x0

    iput-boolean v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mBackKeyHandled:Z

    :cond_4e
    goto :goto_1b

    :cond_4f
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->hasLongPressOnBackBehavior()Z

    move-result v0

    if-nez v0, :cond_50

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mBackKeyHandled:Z

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->backKeyPress()Z

    move-result v3

    or-int/2addr v0, v3

    iput-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mBackKeyHandled:Z

    :cond_50
    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mBackKeyHandled:Z

    if-eqz v0, :cond_51

    and-int/lit8 v12, v12, -0x2

    move/from16 v5, v24

    goto :goto_1c

    :cond_51
    :goto_1b
    move/from16 v5, v24

    :goto_1c
    if-eqz v23, :cond_52

    const-string v0, "Virtual Key - Press"

    const/4 v3, 0x1

    invoke-direct {v1, v3, v0}, Lcom/android/server/policy/PhoneWindowManager;->performHapticFeedback(ILjava/lang/String;)V

    :cond_52
    if-eqz v5, :cond_53

    invoke-static {}, Lcom/android/server/policy/PhoneWindowManagerStub;->getInstance()Lcom/android/server/policy/PhoneWindowManagerStub;

    move-result-object v0

    invoke-interface {v0, v2}, Lcom/android/server/policy/PhoneWindowManagerStub;->interceptWakeKey(Landroid/view/KeyEvent;)Z

    move-result v0

    if-nez v0, :cond_53

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->wakeUpFromWakeKey(Landroid/view/KeyEvent;)V

    :cond_53
    and-int/lit8 v0, v12, 0x1

    if-eqz v0, :cond_55

    const/4 v3, -0x1

    if-eq v14, v3, :cond_55

    iget v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mTopFocusedDisplayId:I

    if-eq v14, v0, :cond_55

    invoke-static {}, Lcom/android/server/policy/PhoneWindowManagerStub;->getInstance()Lcom/android/server/policy/PhoneWindowManagerStub;

    move-result-object v0

    invoke-interface {v0, v4}, Lcom/android/server/policy/PhoneWindowManagerStub;->shouldMoveDisplayToTop(I)Z

    move-result v0

    if-nez v0, :cond_54

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Don\\'t move non-focused display "

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, v14}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v3, " to top because a key "

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v3, " is targeting it"

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v11, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v12

    :cond_54
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Attempting to move non-focused display "

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, v14}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v3, " to top because a key is targeting it"

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v11, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerFuncs:Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;

    invoke-interface {v0, v14}, Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;->moveDisplayToTopIfAllowed(I)V

    :cond_55
    return v12

    :sswitch_data_0
    .sparse-switch
        0x4 -> :sswitch_14
        0x5 -> :sswitch_13
        0x6 -> :sswitch_12
        0x18 -> :sswitch_11
        0x19 -> :sswitch_11
        0x1a -> :sswitch_10
        0x3e -> :sswitch_f
        0x4f -> :sswitch_e
        0x55 -> :sswitch_e
        0x56 -> :sswitch_e
        0x57 -> :sswitch_e
        0x58 -> :sswitch_e
        0x59 -> :sswitch_e
        0x5a -> :sswitch_e
        0x5b -> :sswitch_d
        0x7e -> :sswitch_e
        0x7f -> :sswitch_e
        0x82 -> :sswitch_e
        0xa4 -> :sswitch_11
        0xab -> :sswitch_c
        0xb1 -> :sswitch_b
        0xdb -> :sswitch_a
        0xde -> :sswitch_e
        0xdf -> :sswitch_9
        0xe0 -> :sswitch_8
        0xe7 -> :sswitch_7
        0x108 -> :sswitch_6
        0x114 -> :sswitch_5
        0x118 -> :sswitch_4
        0x119 -> :sswitch_4
        0x11a -> :sswitch_4
        0x11b -> :sswitch_4
        0x121 -> :sswitch_3
        0x122 -> :sswitch_3
        0x123 -> :sswitch_3
        0x124 -> :sswitch_3
        0x125 -> :sswitch_3
        0x126 -> :sswitch_3
        0x127 -> :sswitch_3
        0x128 -> :sswitch_3
        0x129 -> :sswitch_3
        0x12a -> :sswitch_3
        0x12b -> :sswitch_3
        0x12c -> :sswitch_3
        0x12d -> :sswitch_3
        0x12e -> :sswitch_3
        0x12f -> :sswitch_3
        0x130 -> :sswitch_3
        0x134 -> :sswitch_2
        0x135 -> :sswitch_2
        0x136 -> :sswitch_2
        0x137 -> :sswitch_2
        0x139 -> :sswitch_1
        0x13a -> :sswitch_1
        0x13b -> :sswitch_1
        0x13c -> :sswitch_1
        0x13f -> :sswitch_0
        0x140 -> :sswitch_0
        0x141 -> :sswitch_0
        0x143 -> :sswitch_0
        0x146 -> :sswitch_0
        0x147 -> :sswitch_0
        0x148 -> :sswitch_0
        0x149 -> :sswitch_0
        0x14a -> :sswitch_0
        0x14b -> :sswitch_0
        0x14c -> :sswitch_0
        0x14d -> :sswitch_0
        0x14e -> :sswitch_0
        0x14f -> :sswitch_0
        0x150 -> :sswitch_0
        0x151 -> :sswitch_0
    .end sparse-switch
.end method
""",
        "replacement": """\
.method public interceptKeyBeforeQueueing(Landroid/view/KeyEvent;I)I
    .registers 37

    move-object/from16 v1, p0

    move-object/from16 v2, p1

    move/from16 v3, p2

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getKeyCode()I

    move-result v4

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getAction()I

    move-result v0

    const/4 v5, 0x0

    if-nez v0, :cond_0

    const/4 v0, 0x1

    goto :goto_0

    :cond_0
    move v0, v5

    :goto_0
    move v7, v0

    and-int/lit8 v0, v3, 0x1

    if-nez v0, :cond_2

    invoke-virtual {v2}, Landroid/view/KeyEvent;->isWakeKey()Z

    move-result v0

    if-eqz v0, :cond_1

    goto :goto_1

    :cond_1
    move v0, v5

    goto :goto_2

    :cond_2
    :goto_1
    const/4 v0, 0x1

    :goto_2
    const/high16 v8, 0x40000

    and-int/2addr v8, v3

    if-eqz v8, :cond_3

    const/4 v8, 0x1

    goto :goto_3

    :cond_3
    move v8, v5

    :goto_3
    iget-boolean v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mVisibleBackgroundUsersEnabled:Z

    const/4 v10, 0x0

    if-eqz v9, :cond_4

    invoke-static {v4}, Landroid/view/KeyEvent;->isVisibleBackgroundUserAllowedKey(I)Z

    move-result v9

    if-nez v9, :cond_4

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDisplayId()I

    move-result v9

    invoke-direct {v1, v9, v4, v10}, Lcom/android/server/policy/PhoneWindowManager;->isKeyEventForCurrentUser(IILjava/lang/String;)Z

    move-result v9

    if-nez v9, :cond_4

    return v5

    :cond_4
    invoke-static {}, Lxiaomi/platform/flags/Flags;->mtkEnabled()Z

    move-result v9

    const-string v11, "WindowManager"

    if-eqz v9, :cond_6

    const-string v9, "sys.hu.status"

    invoke-static {v9, v10}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v9

    if-eqz v9, :cond_6

    const-string v10, ""

    invoke-virtual {v9, v10}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v10

    if-nez v10, :cond_6

    const-string v10, "shutdown"

    invoke-virtual {v9, v10}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v10

    if-nez v10, :cond_5

    const-string v10, "boot_started"

    invoke-virtual {v9, v10}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v10

    if-eqz v10, :cond_6

    :cond_5
    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v10, "IPO skip key request when huStatus is "

    invoke-virtual {v6, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v11, v6}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    return v5

    :cond_6
    iget-boolean v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mSystemBooted:Z

    const/16 v10, 0xb1

    const/16 v12, 0x1a

    if-nez v9, :cond_c

    const/4 v6, 0x0

    if-eqz v7, :cond_8

    if-eq v4, v12, :cond_7

    if-ne v4, v10, :cond_8

    :cond_7
    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->wakeUpFromWakeKey(Landroid/view/KeyEvent;)V

    const/4 v6, 0x1

    goto :goto_4

    :cond_8
    if-eqz v7, :cond_a

    if-nez v0, :cond_9

    const/16 v9, 0xe0

    if-ne v4, v9, :cond_a

    :cond_9
    invoke-direct {v1, v4}, Lcom/android/server/policy/PhoneWindowManager;->isWakeKeyWhenScreenOff(I)Z

    move-result v9

    if-eqz v9, :cond_a

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->wakeUpFromWakeKey(Landroid/view/KeyEvent;)V

    const/4 v6, 0x1

    :cond_a
    :goto_4
    if-eqz v6, :cond_b

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->getHdmiControl()Lcom/android/server/policy/PhoneWindowManager$HdmiControl;

    move-result-object v9

    if-eqz v9, :cond_b

    invoke-virtual {v9}, Lcom/android/server/policy/PhoneWindowManager$HdmiControl;->turnOnTv()V

    :cond_b
    return v5

    :cond_c
    const/high16 v9, 0x20000000

    and-int/2addr v9, v3

    if-eqz v9, :cond_d

    const/4 v9, 0x1

    goto :goto_5

    :cond_d
    move v9, v5

    :goto_5
    invoke-virtual {v2}, Landroid/view/KeyEvent;->isCanceled()Z

    move-result v13

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDisplayId()I

    move-result v14

    const/high16 v15, 0x1000000

    and-int/2addr v15, v3

    if-eqz v15, :cond_e

    const/4 v15, 0x1

    goto :goto_6

    :cond_e
    move v15, v5

    :goto_6
    move/from16 v16, v5

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getKeyCode()I

    move-result v5

    if-ne v5, v12, :cond_f

    if-eqz v7, :cond_f

    iget-object v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mSideFpsEventHandler:Lcom/android/server/policy/SideFpsEventHandler;

    invoke-virtual {v5}, Lcom/android/server/policy/SideFpsEventHandler;->notifyPowerPressed()V

    :cond_f
    sget-boolean v5, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    if-eqz v5, :cond_12

    iget-object v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    if-eqz v5, :cond_11

    if-eqz v9, :cond_10

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardShowingAndNotOccluded()Z

    move-result v5

    if-eqz v5, :cond_11

    goto :goto_7

    :cond_10
    iget-object v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    invoke-virtual {v5}, Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;->isShowing()Z

    move-result v5

    if-eqz v5, :cond_11

    :goto_7
    const/4 v5, 0x1

    goto :goto_8

    :cond_11
    move/from16 v5, v16

    :goto_8
    new-instance v12, Ljava/lang/StringBuilder;

    invoke-direct {v12}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "interceptKeyTq keycode="

    invoke-virtual {v12, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v12, " interactive="

    invoke-virtual {v6, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v9}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v12, " keyguardActive="

    invoke-virtual {v6, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v5}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v6

    const-string v12, " policyFlags="

    invoke-virtual {v6, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-static {v3}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;

    move-result-object v12

    invoke-virtual {v6, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v11, v6}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_12
    invoke-static {}, Lcom/android/server/policy/PhoneWindowManagerStub;->getInstance()Lcom/android/server/policy/PhoneWindowManagerStub;

    move-result-object v5

    invoke-interface {v5, v2}, Lcom/android/server/policy/PhoneWindowManagerStub;->interceptKeyBeforeQueueing(Landroid/view/KeyEvent;)Z

    move-result v5

    if-eqz v5, :cond_13

    return v16

    :cond_13
    invoke-static {}, Lxiaomi/platform/flags/Flags;->mtkEnabled()Z

    move-result v5

    const/4 v6, -0x1

    if-eqz v5, :cond_14

    if-nez v9, :cond_14

    if-eqz v15, :cond_14

    if-nez v0, :cond_14

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v12, "Inject keyevent when screen off. ignore! keyevent="

    invoke-virtual {v5, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-static {v11, v5}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    const/4 v5, 0x0

    move v12, v5

    move v5, v0

    goto :goto_a

    :cond_14
    if-nez v9, :cond_1a

    if-eqz v15, :cond_15

    if-nez v0, :cond_15

    goto :goto_9

    :cond_15
    invoke-direct {v1, v14, v4}, Lcom/android/server/policy/PhoneWindowManager;->shouldDispatchInputWhenNonInteractive(II)Z

    move-result v5

    if-eqz v5, :cond_16

    const/4 v5, 0x1

    iput v6, v1, Lcom/android/server/policy/PhoneWindowManager;->mPendingWakeKey:I

    move v12, v5

    move v5, v0

    goto :goto_a

    :cond_16
    const/4 v5, 0x0

    if-eqz v0, :cond_18

    if-eqz v7, :cond_17

    invoke-direct {v1, v4}, Lcom/android/server/policy/PhoneWindowManager;->isWakeKeyWhenScreenOff(I)Z

    move-result v12

    if-nez v12, :cond_18

    :cond_17
    const/4 v0, 0x0

    :cond_18
    if-eqz v0, :cond_19

    if-eqz v7, :cond_19

    iput v4, v1, Lcom/android/server/policy/PhoneWindowManager;->mPendingWakeKey:I

    :cond_19
    move v12, v5

    move v5, v0

    goto :goto_a

    :cond_1a
    :goto_9
    const/4 v5, 0x1

    const/4 v0, 0x0

    if-eqz v9, :cond_1c

    iget v12, v1, Lcom/android/server/policy/PhoneWindowManager;->mPendingWakeKey:I

    if-ne v4, v12, :cond_1b

    if-nez v7, :cond_1b

    const/4 v5, 0x0

    :cond_1b
    iput v6, v1, Lcom/android/server/policy/PhoneWindowManager;->mPendingWakeKey:I

    move v12, v5

    move v5, v0

    goto :goto_a

    :cond_1c
    move v12, v5

    move v5, v0

    :goto_a
    invoke-static {v4}, Lcom/android/server/policy/PhoneWindowManager;->isValidGlobalKey(I)Z

    move-result v0

    if-eqz v0, :cond_1f

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mGlobalKeyManager:Lcom/android/server/policy/GlobalKeyManager;

    invoke-virtual {v0, v4}, Lcom/android/server/policy/GlobalKeyManager;->shouldHandleGlobalKey(I)Z

    move-result v0

    if-eqz v0, :cond_1f

    if-nez v9, :cond_1d

    if-eqz v5, :cond_1d

    if-eqz v7, :cond_1d

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mGlobalKeyManager:Lcom/android/server/policy/GlobalKeyManager;

    invoke-virtual {v0, v4}, Lcom/android/server/policy/GlobalKeyManager;->shouldDispatchFromNonInteractive(I)Z

    move-result v0

    if-eqz v0, :cond_1d

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mGlobalKeyManager:Lcom/android/server/policy/GlobalKeyManager;

    invoke-virtual {v0}, Lcom/android/server/policy/GlobalKeyManager;->setBeganFromNonInteractive()V

    const/4 v12, 0x1

    iput v6, v1, Lcom/android/server/policy/PhoneWindowManager;->mPendingWakeKey:I

    :cond_1d
    if-eqz v5, :cond_1e

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->wakeUpFromWakeKey(Landroid/view/KeyEvent;)V

    :cond_1e
    return v12

    :cond_1f
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->getHdmiControlManager()Landroid/hardware/hdmi/HdmiControlManager;

    move-result-object v19

    if-ne v4, v10, :cond_21

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHasFeatureLeanback:Z

    if-eqz v0, :cond_21

    if-eqz v19, :cond_20

    invoke-virtual/range {v19 .. v19}, Landroid/hardware/hdmi/HdmiControlManager;->shouldHandleTvPowerKey()Z

    move-result v0

    if-nez v0, :cond_21

    :cond_20
    nop

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDownTime()J

    move-result-wide v20

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getEventTime()J

    move-result-wide v22

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getAction()I

    move-result v24

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v26

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getMetaState()I

    move-result v27

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDeviceId()I

    move-result v28

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getScanCode()I

    move-result v29

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getFlags()I

    move-result v30

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getSource()I

    move-result v31

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDisplayId()I

    move-result v32

    const/16 v25, 0x1a

    const/16 v33, 0x0

    invoke-static/range {v20 .. v33}, Landroid/view/KeyEvent;->obtain(JJIIIIIIIIILjava/lang/String;)Landroid/view/KeyEvent;

    move-result-object v0

    invoke-virtual {v1, v0, v3}, Lcom/android/server/policy/PhoneWindowManager;->interceptKeyBeforeQueueing(Landroid/view/KeyEvent;I)I

    move-result v2

    return v2

    :cond_21
    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplay:Landroid/view/Display;

    invoke-virtual {v0}, Landroid/view/Display;->getState()I

    move-result v0

    invoke-static {v0}, Landroid/view/Display;->isOnState(I)Z

    move-result v10

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    invoke-virtual {v0}, Lcom/android/server/wm/DisplayPolicy;->isAwake()Z

    move-result v20

    if-eqz v9, :cond_22

    if-eqz v20, :cond_22

    const/4 v0, 0x1

    goto :goto_b

    :cond_22
    move/from16 v0, v16

    :goto_b
    move/from16 v21, v0

    if-eqz v8, :cond_23

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mSingleKeyGestureDetector:Lcom/android/server/policy/SingleKeyGestureDetector;

    invoke-virtual {v0}, Lcom/android/server/policy/SingleKeyGestureDetector;->reset()V

    move/from16 v6, v21

    goto :goto_c

    :cond_23
    invoke-virtual {v2}, Landroid/view/KeyEvent;->getFlags()I

    move-result v0

    and-int/lit16 v0, v0, 0x400

    if-nez v0, :cond_25

    invoke-static {}, Lcom/android/server/policy/PhoneWindowManagerStub;->getInstance()Lcom/android/server/policy/PhoneWindowManagerStub;

    move-result-object v0

    invoke-interface {v0, v2}, Lcom/android/server/policy/PhoneWindowManagerStub;->skipKeyGesutre(Landroid/view/KeyEvent;)Z

    move-result v0

    if-nez v0, :cond_24

    move/from16 v6, v21

    invoke-direct {v1, v2, v6, v10}, Lcom/android/server/policy/PhoneWindowManager;->handleKeyGesture(Landroid/view/KeyEvent;ZZ)V

    goto :goto_c

    :cond_24
    move/from16 v6, v21

    goto :goto_c

    :cond_25
    move/from16 v6, v21

    :goto_c
    invoke-virtual {v2}, Landroid/view/KeyEvent;->getFlags()I

    move-result v0

    and-int/lit8 v0, v0, 0x40

    if-eqz v0, :cond_26

    const/4 v0, 0x1

    goto :goto_d

    :cond_26
    move/from16 v0, v16

    :goto_d
    move/from16 v21, v0

    if-eqz v7, :cond_28

    and-int/lit8 v0, v3, 0x2

    if-eqz v0, :cond_28

    if-eqz v21, :cond_27

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mNavBarVirtualKeyHapticFeedbackEnabled:Z

    if-eqz v0, :cond_28

    :cond_27
    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-nez v0, :cond_28

    const/4 v0, 0x1

    goto :goto_e

    :cond_28
    move/from16 v0, v16

    :goto_e
    move/from16 v23, v0

    const/16 v0, 0x22

    const/4 v3, 0x3

    sparse-switch v4, :sswitch_data_0

    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1b

    :sswitch_0
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/com/android/hardware/input/Flags;->enableNew25q2Keycodes()Z

    move-result v0

    if-nez v0, :cond_29

    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1c

    :cond_29
    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1b

    :sswitch_1
    invoke-static {}, Lcom/android/server/policy/PhoneWindowManagerStub;->getInstance()Lcom/android/server/policy/PhoneWindowManagerStub;

    move-result-object v0

    invoke-interface {v0, v2}, Lcom/android/server/policy/PhoneWindowManagerStub;->skipInterceptMacroEvent(Landroid/view/KeyEvent;)Z

    move-result v0

    if-eqz v0, :cond_2a

    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1b

    :cond_2a
    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1c

    :sswitch_2
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Stylus buttons event: "

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v3, " received. Should handle event? "

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    iget-boolean v3, v1, Lcom/android/server/policy/PhoneWindowManager;->mStylusButtonsEnabled:Z

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v11, v0}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mStylusButtonsEnabled:Z

    if-eqz v0, :cond_2b

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->sendSystemKeyToStatusBarAsync(Landroid/view/KeyEvent;)V

    :cond_2b
    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1c

    :sswitch_3
    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1c

    :sswitch_4
    const/16 v0, 0x23

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    and-int/lit8 v12, v12, -0x2

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->interceptSystemNavigationKey(Landroid/view/KeyEvent;)V

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1c

    :sswitch_5
    const/16 v0, 0x24

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    and-int/lit8 v12, v12, -0x2

    const/4 v5, 0x0

    if-nez v7, :cond_2c

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerManagerInternal:Landroid/os/PowerManagerInternal;

    invoke-virtual {v0}, Landroid/os/PowerManagerInternal;->setUserInactiveOverrideFromWindowManager()V

    :cond_2c
    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->sendSystemKeyToStatusBarAsync(Landroid/view/KeyEvent;)V

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    goto :goto_1c

    :sswitch_6
    if-eqz v7, :cond_2d

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-nez v0, :cond_2d

    and-int/lit8 v0, v12, 0x1

    if-nez v0, :cond_2d

    move/from16 v25, v9

    move/from16 v26, v10

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDownTime()J

    move-result-wide v9

    invoke-direct {v1, v4, v9, v10}, Lcom/android/server/policy/PhoneWindowManager;->setDeferredKeyActionsExecutableAsync(IJ)V

    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_2d
    move/from16 v25, v9

    move/from16 v26, v10

    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :sswitch_7
    move/from16 v25, v9

    move/from16 v26, v10

    if-nez v7, :cond_2e

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->acquire()V

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    const/16 v3, 0xc

    invoke-virtual {v0, v3}, Landroid/os/Handler;->obtainMessage(I)Landroid/os/Message;

    move-result-object v0

    const/4 v3, 0x1

    invoke-virtual {v0, v3}, Landroid/os/Message;->setAsynchronous(Z)V

    invoke-virtual {v0}, Landroid/os/Message;->sendToTarget()V

    const/4 v3, 0x6

    invoke-direct {v1, v2, v3}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompleted(Landroid/view/KeyEvent;I)V

    :cond_2e
    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1c

    :sswitch_8
    move/from16 v25, v9

    move/from16 v26, v10

    const/16 v0, 0x25

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    and-int/lit8 v12, v12, -0x2

    const/4 v5, 0x1

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1c

    :sswitch_9
    move/from16 v25, v9

    move/from16 v26, v10

    const/16 v0, 0x24

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    and-int/lit8 v12, v12, -0x2

    const/4 v5, 0x0

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    invoke-virtual {v0}, Landroid/os/PowerManager;->isInteractive()Z

    move-result v0

    if-nez v0, :cond_2f

    const/16 v23, 0x0

    :cond_2f
    if-eqz v7, :cond_30

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->sleepPress()V

    goto :goto_f

    :cond_30
    invoke-virtual {v2}, Landroid/view/KeyEvent;->getEventTime()J

    move-result-wide v9

    invoke-direct {v1, v9, v10}, Lcom/android/server/policy/PhoneWindowManager;->sleepRelease(J)V

    :goto_f
    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->sendSystemKeyToStatusBarAsync(Landroid/view/KeyEvent;)V

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1c

    :sswitch_a
    move/from16 v25, v9

    move/from16 v26, v10

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-lez v0, :cond_31

    const/4 v0, 0x1

    goto :goto_10

    :cond_31
    move/from16 v0, v16

    :goto_10
    if-eqz v7, :cond_32

    if-nez v0, :cond_32

    iget-object v3, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getDeviceId()I

    move-result v9

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getEventTime()J

    move-result-wide v27

    invoke-static/range {v27 .. v28}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v10

    move/from16 v17, v0

    const/16 v0, 0x17

    move/from16 v24, v5

    move/from16 v5, v16

    invoke-virtual {v3, v0, v9, v5, v10}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object v0

    const/4 v3, 0x1

    invoke-virtual {v0, v3}, Landroid/os/Message;->setAsynchronous(Z)V

    invoke-virtual {v0}, Landroid/os/Message;->sendToTarget()V

    const/4 v3, 0x5

    invoke-direct {v1, v2, v3}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompleted(Landroid/view/KeyEvent;I)V

    goto :goto_11

    :cond_32
    move/from16 v17, v0

    move/from16 v24, v5

    :goto_11
    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v5, v24

    goto :goto_1c

    :sswitch_b
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    and-int/lit8 v12, v12, -0x2

    const/4 v5, 0x0

    if-eqz v7, :cond_33

    if-eqz v19, :cond_33

    invoke-virtual/range {v19 .. v19}, Landroid/hardware/hdmi/HdmiControlManager;->toggleAndFollowTvPower()V

    :cond_33
    :goto_12
    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1c

    :sswitch_c
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    iget v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mShortPressOnWindowBehavior:I

    const/4 v3, 0x1

    if-ne v0, v3, :cond_36

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mPictureInPictureVisible:Z

    if-eqz v0, :cond_35

    if-nez v7, :cond_34

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->showPictureInPictureMenu(Landroid/view/KeyEvent;)V

    :cond_34
    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v5, v24

    goto :goto_1c

    :cond_35
    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_36
    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :sswitch_d
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    and-int/lit8 v12, v12, -0x2

    if-eqz v7, :cond_37

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-nez v0, :cond_37

    const/16 v0, 0x1a

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompleted(Landroid/view/KeyEvent;I)V

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->toggleMicrophoneMuteFromKey()V

    :cond_37
    :goto_13
    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v5, v24

    goto :goto_1c

    :sswitch_e
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    const/16 v0, 0x26

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-static {v0}, Landroid/media/session/MediaSessionLegacyHelper;->getHelper(Landroid/content/Context;)Landroid/media/session/MediaSessionLegacyHelper;

    move-result-object v0

    invoke-virtual {v0}, Landroid/media/session/MediaSessionLegacyHelper;->isGlobalPriorityActive()Z

    move-result v0

    if-eqz v0, :cond_38

    and-int/lit8 v12, v12, -0x2

    :cond_38
    and-int/lit8 v0, v12, 0x1

    if-nez v0, :cond_37

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->acquire()V

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    new-instance v5, Landroid/view/KeyEvent;

    invoke-direct {v5, v2}, Landroid/view/KeyEvent;-><init>(Landroid/view/KeyEvent;)V

    invoke-virtual {v0, v3, v5}, Landroid/os/Handler;->obtainMessage(ILjava/lang/Object;)Landroid/os/Message;

    move-result-object v0

    const/4 v3, 0x1

    invoke-virtual {v0, v3}, Landroid/os/Message;->setAsynchronous(Z)V

    invoke-virtual {v0}, Landroid/os/Message;->sendToTarget()V

    goto :goto_13

    :sswitch_f
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    if-eqz v7, :cond_3a

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-nez v0, :cond_3a

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getMetaState()I

    move-result v0

    and-int/lit16 v0, v0, -0xc2

    const/16 v3, 0x1000

    invoke-static {v0, v3}, Landroid/view/KeyEvent;->metaStateHasModifiers(II)Z

    move-result v0

    if-eqz v0, :cond_39

    new-instance v0, Landroid/view/KeyEvent;

    invoke-direct {v0, v2}, Landroid/view/KeyEvent;-><init>(Landroid/view/KeyEvent;)V

    invoke-direct {v1, v0}, Lcom/android/server/policy/PhoneWindowManager;->handleSwitchKeyboardLayoutToast(Landroid/view/KeyEvent;)V

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_39
    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_3a
    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :sswitch_10
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    invoke-direct {v1, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    nop

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getAction()I

    move-result v0

    invoke-static {v0}, Landroid/view/KeyEvent;->actionToString(I)Ljava/lang/String;

    move-result-object v0

    iget-boolean v3, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerKeyHandled:Z

    iget-object v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mSingleKeyGestureDetector:Lcom/android/server/policy/SingleKeyGestureDetector;

    const/16 v9, 0x1a

    invoke-virtual {v5, v9}, Lcom/android/server/policy/SingleKeyGestureDetector;->getKeyPressCounter(I)I

    move-result v5

    invoke-static {v0, v3, v5}, Lcom/android/server/policy/EventLogTags;->writeInterceptPower(Ljava/lang/String;II)V

    and-int/lit8 v12, v12, -0x2

    const/4 v5, 0x0

    if-eqz v7, :cond_3b

    invoke-direct {v1, v2, v6, v8}, Lcom/android/server/policy/PhoneWindowManager;->interceptPowerKeyDown(Landroid/view/KeyEvent;ZZ)V

    goto :goto_12

    :cond_3b
    invoke-direct {v1, v2, v13}, Lcom/android/server/policy/PhoneWindowManager;->interceptPowerKeyUp(Landroid/view/KeyEvent;Z)V

    goto :goto_12

    :sswitch_11
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->checkVolBtn(Landroid/view/KeyEvent;)I

    move-result v0

    if-nez v0, :cond_3c

    return v0

    :cond_3c
    const/16 v0, 0x19

    if-ne v4, v0, :cond_3d

    const/16 v0, 0x13

    goto :goto_14

    :cond_3d
    const/16 v0, 0x18

    if-ne v4, v0, :cond_3e

    const/16 v0, 0x12

    goto :goto_14

    :cond_3e
    const/16 v0, 0x14

    :goto_14
    move v5, v0

    invoke-direct {v1, v2, v5}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionDown(Landroid/view/KeyEvent;I)V

    if-eqz v7, :cond_45

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->sendSystemKeyToStatusBarAsync(Landroid/view/KeyEvent;)V

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getNotificationService()Landroid/app/NotificationManager;

    move-result-object v10

    if-eqz v10, :cond_3f

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandleVolumeKeysInWM:Z

    if-nez v0, :cond_3f

    invoke-virtual {v10}, Landroid/app/NotificationManager;->silenceNotificationSound()V

    :cond_3f
    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getTelecommService()Landroid/telecom/TelecomManager;

    move-result-object v17

    if-eqz v17, :cond_40

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandleVolumeKeysInWM:Z

    if-nez v0, :cond_40

    invoke-virtual/range {v17 .. v17}, Landroid/telecom/TelecomManager;->isRinging()Z

    move-result v0

    if-eqz v0, :cond_40

    const-string v0, "interceptKeyBeforeQueueing: VOLUME key-down while ringing: Silence ringer!"

    invoke-static {v11, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->responseToTheCall(Landroid/view/KeyEvent;)V

    and-int/lit8 v12, v12, -0x2

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v5, v24

    goto :goto_1c

    :cond_40
    const/16 v27, 0x0

    :try_start_0
    invoke-static {}, Lcom/android/server/policy/PhoneWindowManager;->getAudioService()Landroid/media/IAudioService;

    move-result-object v0

    invoke-interface {v0}, Landroid/media/IAudioService;->getMode()I

    move-result v0
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    move/from16 v27, v0

    goto :goto_15

    :catch_0
    move-exception v0

    const-string v9, "Error getting AudioService in interceptKeyBeforeQueueing."

    invoke-static {v11, v9, v0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    move/from16 v0, v27

    :goto_15
    if-eqz v17, :cond_41

    invoke-virtual/range {v17 .. v17}, Landroid/telecom/TelecomManager;->isInCall()Z

    move-result v9

    if-nez v9, :cond_42

    :cond_41
    if-ne v0, v3, :cond_43

    :cond_42
    const/4 v3, 0x1

    goto :goto_16

    :cond_43
    const/4 v3, 0x0

    :goto_16
    if-eqz v3, :cond_44

    and-int/lit8 v9, v12, 0x1

    if-nez v9, :cond_44

    iget-object v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-static {v9}, Landroid/media/session/MediaSessionLegacyHelper;->getHelper(Landroid/content/Context;)Landroid/media/session/MediaSessionLegacyHelper;

    move-result-object v9

    move/from16 v27, v3

    move/from16 v16, v5

    const/high16 v3, -0x80000000

    const/4 v5, 0x0

    invoke-virtual {v9, v2, v3, v5}, Landroid/media/session/MediaSessionLegacyHelper;->sendVolumeKeyEvent(Landroid/view/KeyEvent;IZ)V

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_44
    move/from16 v27, v3

    move/from16 v16, v5

    goto :goto_17

    :cond_45
    move/from16 v16, v5

    :goto_17
    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mUseTvRouting:Z

    if-nez v0, :cond_48

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandleVolumeKeysInWM:Z

    if-eqz v0, :cond_46

    goto :goto_18

    :cond_46
    and-int/lit8 v0, v12, 0x1

    if-nez v0, :cond_47

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-static {v0}, Landroid/media/session/MediaSessionLegacyHelper;->getHelper(Landroid/content/Context;)Landroid/media/session/MediaSessionLegacyHelper;

    move-result-object v0

    const/high16 v3, -0x80000000

    const/4 v5, 0x1

    invoke-virtual {v0, v2, v3, v5}, Landroid/media/session/MediaSessionLegacyHelper;->sendVolumeKeyEvent(Landroid/view/KeyEvent;IZ)V

    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_47
    move/from16 v27, v6

    move/from16 v17, v7

    goto :goto_1b

    :cond_48
    :goto_18
    or-int/lit8 v12, v12, 0x1

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v5, v24

    goto :goto_1c

    :sswitch_12
    move/from16 v24, v5

    move/from16 v25, v9

    move/from16 v26, v10

    and-int/lit8 v12, v12, -0x2

    if-eqz v7, :cond_4b

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getTelecommService()Landroid/telecom/TelecomManager;

    move-result-object v0

    const/4 v3, 0x0

    if-eqz v0, :cond_49

    invoke-virtual {v0}, Landroid/telecom/TelecomManager;->endCall()Z

    move-result v3

    :cond_49
    if-eqz v25, :cond_4a

    if-nez v3, :cond_4a

    const/4 v5, 0x0

    iput-boolean v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndCallKeyHandled:Z

    iget-object v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    iget-object v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndCallLongPress:Ljava/lang/Runnable;

    iget-object v10, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-static {v10}, Landroid/view/ViewConfiguration;->get(Landroid/content/Context;)Landroid/view/ViewConfiguration;

    move-result-object v10

    move/from16 v27, v6

    move/from16 v17, v7

    invoke-virtual {v10}, Landroid/view/ViewConfiguration;->getDeviceGlobalActionKeyTimeout()J

    move-result-wide v6

    invoke-virtual {v5, v9, v6, v7}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    goto :goto_19

    :cond_4a
    move/from16 v27, v6

    move/from16 v17, v7

    const/4 v5, 0x1

    iput-boolean v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndCallKeyHandled:Z

    :goto_19
    goto :goto_1b

    :cond_4b
    move/from16 v27, v6

    move/from16 v17, v7

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndCallKeyHandled:Z

    if-nez v0, :cond_52

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mHandler:Landroid/os/Handler;

    iget-object v3, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndCallLongPress:Ljava/lang/Runnable;

    invoke-virtual {v0, v3}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    if-nez v13, :cond_52

    iget v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndcallBehavior:I

    const/16 v18, 0x1

    and-int/lit8 v0, v0, 0x1

    if-eqz v0, :cond_4c

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->goHome()Z

    move-result v0

    if-eqz v0, :cond_4c

    goto :goto_1b

    :cond_4c
    iget v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndcallBehavior:I

    and-int/lit8 v0, v0, 0x2

    if-eqz v0, :cond_52

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getEventTime()J

    move-result-wide v5

    const/4 v0, 0x4

    const/4 v3, 0x0

    invoke-direct {v1, v5, v6, v0, v3}, Lcom/android/server/policy/PhoneWindowManager;->sleepDefaultDisplay(JII)V

    const/4 v5, 0x0

    goto :goto_1c

    :sswitch_13
    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    if-eqz v17, :cond_52

    invoke-virtual {v1}, Lcom/android/server/policy/PhoneWindowManager;->getTelecommService()Landroid/telecom/TelecomManager;

    move-result-object v0

    if-eqz v0, :cond_4d

    invoke-virtual {v0}, Landroid/telecom/TelecomManager;->isRinging()Z

    move-result v3

    if-eqz v3, :cond_4d

    const-string v3, "interceptKeyBeforeQueueing: CALL key-down while ringing: Answer the call!"

    invoke-static {v11, v3}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {v0}, Landroid/telecom/TelecomManager;->acceptRingingCall()V

    and-int/lit8 v12, v12, -0x2

    :cond_4d
    move/from16 v5, v24

    goto :goto_1c

    :sswitch_14
    move/from16 v24, v5

    move/from16 v27, v6

    move/from16 v17, v7

    move/from16 v25, v9

    move/from16 v26, v10

    invoke-direct {v1, v2, v3}, Lcom/android/server/policy/PhoneWindowManager;->notifyKeyGestureCompletedOnActionUp(Landroid/view/KeyEvent;I)V

    if-eqz v17, :cond_50

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v0

    if-lez v0, :cond_4e

    invoke-virtual {v2}, Landroid/view/KeyEvent;->getFlags()I

    move-result v0

    and-int/lit16 v0, v0, 0x80

    if-eqz v0, :cond_4e

    const/4 v3, 0x1

    goto :goto_1a

    :cond_4e
    const/4 v3, 0x0

    :goto_1a
    if-nez v3, :cond_4f

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerInternal:Lcom/android/server/wm/WindowManagerInternal;

    invoke-virtual {v0}, Lcom/android/server/wm/WindowManagerInternal;->moveFocusToAdjacentEmbeddedActivityIfNeeded()Z

    const/4 v5, 0x0

    iput-boolean v5, v1, Lcom/android/server/policy/PhoneWindowManager;->mBackKeyHandled:Z

    :cond_4f
    goto :goto_1b

    :cond_50
    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->hasLongPressOnBackBehavior()Z

    move-result v0

    if-nez v0, :cond_51

    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mBackKeyHandled:Z

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->backKeyPress()Z

    move-result v3

    or-int/2addr v0, v3

    iput-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mBackKeyHandled:Z

    :cond_51
    iget-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mBackKeyHandled:Z

    if-eqz v0, :cond_52

    and-int/lit8 v12, v12, -0x2

    move/from16 v5, v24

    goto :goto_1c

    :cond_52
    :goto_1b
    move/from16 v5, v24

    :goto_1c
    if-eqz v23, :cond_53

    const-string v0, "Virtual Key - Press"

    const/4 v3, 0x1

    invoke-direct {v1, v3, v0}, Lcom/android/server/policy/PhoneWindowManager;->performHapticFeedback(ILjava/lang/String;)V

    :cond_53
    if-eqz v5, :cond_54

    invoke-static {}, Lcom/android/server/policy/PhoneWindowManagerStub;->getInstance()Lcom/android/server/policy/PhoneWindowManagerStub;

    move-result-object v0

    invoke-interface {v0, v2}, Lcom/android/server/policy/PhoneWindowManagerStub;->interceptWakeKey(Landroid/view/KeyEvent;)Z

    move-result v0

    if-nez v0, :cond_54

    invoke-direct/range {p0 .. p1}, Lcom/android/server/policy/PhoneWindowManager;->wakeUpFromWakeKey(Landroid/view/KeyEvent;)V

    :cond_54
    and-int/lit8 v0, v12, 0x1

    if-eqz v0, :cond_56

    const/4 v3, -0x1

    if-eq v14, v3, :cond_56

    iget v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mTopFocusedDisplayId:I

    if-eq v14, v0, :cond_56

    invoke-static {}, Lcom/android/server/policy/PhoneWindowManagerStub;->getInstance()Lcom/android/server/policy/PhoneWindowManagerStub;

    move-result-object v0

    invoke-interface {v0, v4}, Lcom/android/server/policy/PhoneWindowManagerStub;->shouldMoveDisplayToTop(I)Z

    move-result v0

    if-nez v0, :cond_55

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Don\\'t move non-focused display "

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, v14}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v3, " to top because a key "

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v3, " is targeting it"

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v11, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v12

    :cond_55
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Attempting to move non-focused display "

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, v14}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v3, " to top because a key is targeting it"

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v11, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerFuncs:Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;

    invoke-interface {v0, v14}, Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;->moveDisplayToTopIfAllowed(I)V

    :cond_56
    return v12

    nop

    :sswitch_data_0
    .sparse-switch
        0x4 -> :sswitch_14
        0x5 -> :sswitch_13
        0x6 -> :sswitch_12
        0x18 -> :sswitch_11
        0x19 -> :sswitch_11
        0x1a -> :sswitch_10
        0x3e -> :sswitch_f
        0x4f -> :sswitch_e
        0x55 -> :sswitch_e
        0x56 -> :sswitch_e
        0x57 -> :sswitch_e
        0x58 -> :sswitch_e
        0x59 -> :sswitch_e
        0x5a -> :sswitch_e
        0x5b -> :sswitch_d
        0x7e -> :sswitch_e
        0x7f -> :sswitch_e
        0x82 -> :sswitch_e
        0xa4 -> :sswitch_11
        0xab -> :sswitch_c
        0xb1 -> :sswitch_b
        0xdb -> :sswitch_a
        0xde -> :sswitch_e
        0xdf -> :sswitch_9
        0xe0 -> :sswitch_8
        0xe7 -> :sswitch_7
        0x108 -> :sswitch_6
        0x114 -> :sswitch_5
        0x118 -> :sswitch_4
        0x119 -> :sswitch_4
        0x11a -> :sswitch_4
        0x11b -> :sswitch_4
        0x121 -> :sswitch_3
        0x122 -> :sswitch_3
        0x123 -> :sswitch_3
        0x124 -> :sswitch_3
        0x125 -> :sswitch_3
        0x126 -> :sswitch_3
        0x127 -> :sswitch_3
        0x128 -> :sswitch_3
        0x129 -> :sswitch_3
        0x12a -> :sswitch_3
        0x12b -> :sswitch_3
        0x12c -> :sswitch_3
        0x12d -> :sswitch_3
        0x12e -> :sswitch_3
        0x12f -> :sswitch_3
        0x130 -> :sswitch_3
        0x134 -> :sswitch_2
        0x135 -> :sswitch_2
        0x136 -> :sswitch_2
        0x137 -> :sswitch_2
        0x139 -> :sswitch_1
        0x13a -> :sswitch_1
        0x13b -> :sswitch_1
        0x13c -> :sswitch_1
        0x13f -> :sswitch_0
        0x140 -> :sswitch_0
        0x141 -> :sswitch_0
        0x143 -> :sswitch_0
        0x146 -> :sswitch_0
        0x147 -> :sswitch_0
        0x148 -> :sswitch_0
        0x149 -> :sswitch_0
        0x14a -> :sswitch_0
        0x14b -> :sswitch_0
        0x14c -> :sswitch_0
        0x14d -> :sswitch_0
        0x14e -> :sswitch_0
        0x14f -> :sswitch_0
        0x150 -> :sswitch_0
        0x151 -> :sswitch_0
    .end sparse-switch
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_isDeviceProvisioned__Z",
        "method":      ".method isDeviceProvisioned()Z",
        "type":        "method_replace",
        "search": """\
.method isDeviceProvisioned()Z
    .registers 4

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "device_provisioned"

    const/4 v2, 0x0

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    if-eqz v0, :cond_0

    const/4 v2, 0x1

    :cond_0
    return v2
.end method
""",
        "replacement": """\
.method isDeviceProvisioned()Z
    .registers 4

    goto :goto_7

    nop

    :goto_0
    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    goto :goto_2

    nop

    :goto_1
    return v2

    :goto_2
    const-string v1, "device_provisioned"

    goto :goto_8

    nop

    :goto_3
    invoke-static {v0, v1, v2}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    goto :goto_4

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_5

    nop

    :goto_5
    const/4 v2, 0x1

    :goto_6
    goto :goto_1

    nop

    :goto_7
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_0

    nop

    :goto_8
    const/4 v2, 0x0

    goto :goto_3

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_keyguardOn__Z",
        "method":      ".method keyguardOn()Z",
        "type":        "method_replace",
        "search": """\
.method keyguardOn()Z
    .registers 2

    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardShowingAndNotOccluded()Z

    move-result v0

    if-nez v0, :cond_1

    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->inKeyguardRestrictedKeyInputMode()Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    goto :goto_1

    :cond_1
    :goto_0
    const/4 v0, 0x1

    :goto_1
    return v0
.end method
""",
        "replacement": """\
.method keyguardOn()Z
    .registers 2

    goto :goto_7

    nop

    :goto_0
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->inKeyguardRestrictedKeyInputMode()Z

    move-result v0

    goto :goto_4

    nop

    :goto_1
    goto :goto_6

    :goto_2
    goto :goto_5

    nop

    :goto_3
    return v0

    :goto_4
    if-nez v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_8

    nop

    :goto_5
    const/4 v0, 0x1

    :goto_6
    goto :goto_3

    nop

    :goto_7
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardShowingAndNotOccluded()Z

    move-result v0

    goto :goto_b

    nop

    :goto_8
    goto :goto_2

    :goto_9
    goto :goto_a

    nop

    :goto_a
    const/4 v0, 0x0

    goto :goto_1

    nop

    :goto_b
    if-eqz v0, :cond_1

    goto :goto_2

    :cond_1
    goto :goto_0

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_launchHomeFromHotKey_I_V",
        "method":      ".method launchHomeFromHotKey(I)V",
        "type":        "method_replace",
        "search": """\
.method launchHomeFromHotKey(I)V
    .registers 3

    const/4 v0, 0x1

    invoke-virtual {p0, p1, v0, v0}, Lcom/android/server/policy/PhoneWindowManager;->launchHomeFromHotKey(IZZ)V

    return-void
.end method
""",
        "replacement": """\
.method launchHomeFromHotKey(I)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0, p1, v0, v0}, Lcom/android/server/policy/PhoneWindowManager;->launchHomeFromHotKey(IZZ)V

    goto :goto_2

    nop

    :goto_1
    const/4 v0, 0x1

    goto :goto_0

    nop

    :goto_2
    return-void
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_launchHomeFromHotKey_IZZ_V",
        "method":      ".method launchHomeFromHotKey(IZZ)V",
        "type":        "method_replace",
        "search": """\
.method launchHomeFromHotKey(IZZ)V
    .registers 6

    if-eqz p3, :cond_1

    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardShowingAndNotOccluded()Z

    move-result v0

    if-eqz v0, :cond_0

    return-void

    :cond_0
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardOccluded()Z

    move-result v0

    if-nez v0, :cond_1

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    invoke-virtual {v0}, Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;->isInputRestricted()Z

    move-result v0

    if-eqz v0, :cond_1

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    new-instance v1, Lcom/android/server/policy/PhoneWindowManager$14;

    invoke-direct {v1, p0, p1, p2}, Lcom/android/server/policy/PhoneWindowManager$14;-><init>(Lcom/android/server/policy/PhoneWindowManager;IZ)V

    invoke-virtual {v0, v1}, Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;->verifyUnlock(Lcom/android/server/policy/WindowManagerPolicy$OnKeyguardExitResult;)V

    return-void

    :cond_1
    iget-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mRecentsVisible:Z

    const/4 v1, 0x1

    if-eqz v0, :cond_4

    iget-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mVisibleBackgroundUsersEnabled:Z

    if-eqz v0, :cond_2

    if-nez p1, :cond_4

    :cond_2
    :try_start_0
    invoke-static {}, Landroid/app/ActivityManager;->getService()Landroid/app/IActivityManager;

    move-result-object v0

    invoke-interface {v0}, Landroid/app/IActivityManager;->stopAppSwitches()V
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception v0

    :goto_0
    nop

    if-eqz p2, :cond_3

    invoke-static {}, Lcom/android/server/policy/PhoneWindowManager;->awakenDreams()V

    :cond_3
    const/4 v0, 0x0

    invoke-direct {p0, v0, v1}, Lcom/android/server/policy/PhoneWindowManager;->hideRecentApps(ZZ)V

    goto :goto_1

    :cond_4
    invoke-virtual {p0, p1, v1, p2}, Lcom/android/server/policy/PhoneWindowManager;->startDockOrHome(IZZ)V

    :goto_1
    return-void
.end method
""",
        "replacement": """\
.method launchHomeFromHotKey(IZZ)V
    .registers 6

    goto :goto_8

    nop

    :goto_0
    return-void

    :goto_1
    goto :goto_9

    nop

    :goto_2
    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_14

    nop

    :goto_3
    invoke-virtual {v0}, Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;->isInputRestricted()Z

    move-result v0

    goto :goto_20

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardShowingAndNotOccluded()Z

    move-result v0

    goto :goto_1c

    nop

    :goto_5
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    goto :goto_16

    nop

    :goto_6
    invoke-static {}, Lcom/android/server/policy/PhoneWindowManager;->awakenDreams()V

    :goto_7
    goto :goto_b

    nop

    :goto_8
    if-nez p3, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_4

    nop

    :goto_9
    iget-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mRecentsVisible:Z

    goto :goto_19

    nop

    :goto_a
    invoke-direct {v1, p0, p1, p2}, Lcom/android/server/policy/PhoneWindowManager$14;-><init>(Lcom/android/server/policy/PhoneWindowManager;IZ)V

    goto :goto_e

    nop

    :goto_b
    const/4 v0, 0x0

    goto :goto_17

    nop

    :goto_c
    return-void

    :goto_d
    if-nez p2, :cond_2

    goto :goto_7

    :cond_2
    goto :goto_6

    nop

    :goto_e
    invoke-virtual {v0, v1}, Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;->verifyUnlock(Lcom/android/server/policy/WindowManagerPolicy$OnKeyguardExitResult;)V

    goto :goto_0

    nop

    :goto_f
    if-eqz p1, :cond_3

    goto :goto_22

    :cond_3
    :goto_10
    :try_start_0
    invoke-static {}, Landroid/app/ActivityManager;->getService()Landroid/app/IActivityManager;

    move-result-object v0

    invoke-interface {v0}, Landroid/app/IActivityManager;->stopAppSwitches()V
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_1a

    nop

    :goto_11
    if-nez v0, :cond_4

    goto :goto_10

    :cond_4
    goto :goto_f

    nop

    :goto_12
    invoke-virtual {p0, p1, v1, p2}, Lcom/android/server/policy/PhoneWindowManager;->startDockOrHome(IZZ)V

    :goto_13
    goto :goto_c

    nop

    :goto_14
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    goto :goto_3

    nop

    :goto_15
    if-nez v0, :cond_5

    goto :goto_22

    :cond_5
    goto :goto_18

    nop

    :goto_16
    new-instance v1, Lcom/android/server/policy/PhoneWindowManager$14;

    goto :goto_a

    nop

    :goto_17
    invoke-direct {p0, v0, v1}, Lcom/android/server/policy/PhoneWindowManager;->hideRecentApps(ZZ)V

    goto :goto_21

    nop

    :goto_18
    iget-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mVisibleBackgroundUsersEnabled:Z

    goto :goto_11

    nop

    :goto_19
    const/4 v1, 0x1

    goto :goto_15

    nop

    :goto_1a
    goto :goto_1b

    :catch_0
    move-exception v0

    :goto_1b
    nop

    goto :goto_d

    nop

    :goto_1c
    if-nez v0, :cond_6

    goto :goto_1e

    :cond_6
    goto :goto_1d

    nop

    :goto_1d
    return-void

    :goto_1e
    goto :goto_1f

    nop

    :goto_1f
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardOccluded()Z

    move-result v0

    goto :goto_2

    nop

    :goto_20
    if-nez v0, :cond_7

    goto :goto_1

    :cond_7
    goto :goto_5

    nop

    :goto_21
    goto :goto_13

    :goto_22
    goto :goto_12

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_launchVoiceAssistWithWakeLock__V",
        "method":      ".method launchVoiceAssistWithWakeLock()V",
        "type":        "method_replace",
        "search": """\
.method launchVoiceAssistWithWakeLock()V
    .registers 5

    const-string v0, "assist"

    invoke-virtual {p0, v0}, Lcom/android/server/policy/PhoneWindowManager;->sendCloseSystemWindows(Ljava/lang/String;)V

    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->keyguardOn()Z

    move-result v0

    if-nez v0, :cond_0

    new-instance v0, Landroid/content/Intent;

    const-string v1, "android.speech.action.WEB_SEARCH"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    const-class v1, Landroid/os/DeviceIdleManager;

    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/os/DeviceIdleManager;

    if-eqz v0, :cond_1

    const-string v1, "voice-search"

    invoke-virtual {v0, v1}, Landroid/os/DeviceIdleManager;->endIdle(Ljava/lang/String;)V

    :cond_1
    new-instance v1, Landroid/content/Intent;

    const-string v2, "android.speech.action.VOICE_SEARCH_HANDS_FREE"

    invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v2, "android.speech.extras.EXTRA_SECURE"

    const/4 v3, 0x1

    invoke-virtual {v1, v2, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    move-object v0, v1

    :goto_0
    sget-object v1, Landroid/os/UserHandle;->CURRENT_OR_SELF:Landroid/os/UserHandle;

    invoke-direct {p0, v0, v1}, Lcom/android/server/policy/PhoneWindowManager;->startActivityAsUser(Landroid/content/Intent;Landroid/os/UserHandle;)V

    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    invoke-virtual {v1}, Landroid/os/PowerManager$WakeLock;->release()V

    return-void
.end method
""",
        "replacement": """\
.method launchVoiceAssistWithWakeLock()V
    .registers 5

    goto :goto_14

    nop

    :goto_0
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->keyguardOn()Z

    move-result v0

    goto :goto_7

    nop

    :goto_1
    goto :goto_c

    :goto_2
    goto :goto_18

    nop

    :goto_3
    const-class v1, Landroid/os/DeviceIdleManager;

    goto :goto_9

    nop

    :goto_4
    invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    goto :goto_10

    nop

    :goto_5
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mBroadcastWakeLock:Landroid/os/PowerManager$WakeLock;

    goto :goto_12

    nop

    :goto_6
    new-instance v1, Landroid/content/Intent;

    goto :goto_1d

    nop

    :goto_7
    if-eqz v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_e

    nop

    :goto_8
    check-cast v0, Landroid/os/DeviceIdleManager;

    goto :goto_15

    nop

    :goto_9
    invoke-virtual {v0, v1}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_8

    nop

    :goto_a
    const/4 v3, 0x1

    goto :goto_d

    nop

    :goto_b
    move-object v0, v1

    :goto_c
    goto :goto_1c

    nop

    :goto_d
    invoke-virtual {v1, v2, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    goto :goto_b

    nop

    :goto_e
    new-instance v0, Landroid/content/Intent;

    goto :goto_f

    nop

    :goto_f
    const-string v1, "android.speech.action.WEB_SEARCH"

    goto :goto_17

    nop

    :goto_10
    const-string v2, "android.speech.extras.EXTRA_SECURE"

    goto :goto_a

    nop

    :goto_11
    return-void

    :goto_12
    invoke-virtual {v1}, Landroid/os/PowerManager$WakeLock;->release()V

    goto :goto_11

    nop

    :goto_13
    invoke-virtual {p0, v0}, Lcom/android/server/policy/PhoneWindowManager;->sendCloseSystemWindows(Ljava/lang/String;)V

    goto :goto_0

    nop

    :goto_14
    const-string v0, "assist"

    goto :goto_13

    nop

    :goto_15
    if-nez v0, :cond_1

    goto :goto_1b

    :cond_1
    goto :goto_19

    nop

    :goto_16
    invoke-direct {p0, v0, v1}, Lcom/android/server/policy/PhoneWindowManager;->startActivityAsUser(Landroid/content/Intent;Landroid/os/UserHandle;)V

    goto :goto_5

    nop

    :goto_17
    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    goto :goto_1

    nop

    :goto_18
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_3

    nop

    :goto_19
    const-string v1, "voice-search"

    goto :goto_1a

    nop

    :goto_1a
    invoke-virtual {v0, v1}, Landroid/os/DeviceIdleManager;->endIdle(Ljava/lang/String;)V

    :goto_1b
    goto :goto_6

    nop

    :goto_1c
    sget-object v1, Landroid/os/UserHandle;->CURRENT_OR_SELF:Landroid/os/UserHandle;

    goto :goto_16

    nop

    :goto_1d
    const-string v2, "android.speech.action.VOICE_SEARCH_HANDS_FREE"

    goto :goto_4

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_performStemPrimaryDoublePressSwitchToRecentTask__V",
        "method":      ".method performStemPrimaryDoublePressSwitchToRecentTask()V",
        "type":        "method_replace",
        "search": """\
.method performStemPrimaryDoublePressSwitchToRecentTask()V
    .registers 6

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mBackgroundRecentTaskInfoOnStemPrimarySingleKeyUp:Landroid/app/ActivityManager$RecentTaskInfo;

    const-string v1, "WindowManager"

    if-nez v0, :cond_1

    sget-boolean v2, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    if-eqz v2, :cond_0

    const-string v2, "No recent task available! Show wallpaper."

    invoke-static {v1, v2}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    :cond_0
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->goHome()Z

    return-void

    :cond_1
    sget-boolean v2, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    if-eqz v2, :cond_2

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Starting task from recents. id="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget v3, v0, Landroid/app/ActivityManager$RecentTaskInfo;->id:I

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, ", persistentId="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget v3, v0, Landroid/app/ActivityManager$RecentTaskInfo;->persistentId:I

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, ", topActivity="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget-object v3, v0, Landroid/app/ActivityManager$RecentTaskInfo;->topActivity:Landroid/content/ComponentName;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, ", baseIntent="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget-object v3, v0, Landroid/app/ActivityManager$RecentTaskInfo;->baseIntent:Landroid/content/Intent;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_2
    :try_start_0
    iget-object v2, p0, Lcom/android/server/policy/PhoneWindowManager;->mActivityManagerService:Landroid/app/IActivityManager;

    iget v3, v0, Landroid/app/ActivityManager$RecentTaskInfo;->persistentId:I

    const/4 v4, 0x0

    invoke-interface {v2, v3, v4}, Landroid/app/IActivityManager;->startActivityFromRecents(ILandroid/os/Bundle;)I
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0
    .catch Ljava/lang/IllegalArgumentException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception v2

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "Failed to start task "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget v4, v0, Landroid/app/ActivityManager$RecentTaskInfo;->persistentId:I

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, " from recents"

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v1, v3, v2}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :goto_0
    return-void
.end method
""",
        "replacement": """\
.method performStemPrimaryDoublePressSwitchToRecentTask()V
    .registers 6

    goto :goto_a

    nop

    :goto_0
    iget-object v3, v0, Landroid/app/ActivityManager$RecentTaskInfo;->baseIntent:Landroid/content/Intent;

    goto :goto_4

    nop

    :goto_1
    const-string v4, " from recents"

    goto :goto_24

    nop

    :goto_2
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_d

    nop

    :goto_3
    const-string v2, "No recent task available! Show wallpaper."

    goto :goto_25

    nop

    :goto_4
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_21

    nop

    :goto_5
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_18

    nop

    :goto_6
    const-string v1, "WindowManager"

    goto :goto_27

    nop

    :goto_7
    invoke-static {v1, v2}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_8
    :try_start_0
    iget-object v2, p0, Lcom/android/server/policy/PhoneWindowManager;->mActivityManagerService:Landroid/app/IActivityManager;

    iget v3, v0, Landroid/app/ActivityManager$RecentTaskInfo;->persistentId:I

    const/4 v4, 0x0

    invoke-interface {v2, v3, v4}, Landroid/app/IActivityManager;->startActivityFromRecents(ILandroid/os/Bundle;)I
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0
    .catch Ljava/lang/IllegalArgumentException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_10

    nop

    :goto_9
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_2a

    nop

    :goto_a
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mBackgroundRecentTaskInfoOnStemPrimarySingleKeyUp:Landroid/app/ActivityManager$RecentTaskInfo;

    goto :goto_6

    nop

    :goto_b
    return-void

    :goto_c
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v3

    goto :goto_1

    nop

    :goto_d
    const-string v3, ", topActivity="

    goto :goto_2c

    nop

    :goto_e
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_16

    nop

    :goto_f
    sget-boolean v2, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    goto :goto_12

    nop

    :goto_10
    goto :goto_1b

    :catch_0
    move-exception v2

    goto :goto_2b

    nop

    :goto_11
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_13

    nop

    :goto_12
    if-nez v2, :cond_0

    goto :goto_26

    :cond_0
    goto :goto_3

    nop

    :goto_13
    const-string v4, "Failed to start task "

    goto :goto_19

    nop

    :goto_14
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_0

    nop

    :goto_15
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_5

    nop

    :goto_16
    iget v3, v0, Landroid/app/ActivityManager$RecentTaskInfo;->id:I

    goto :goto_9

    nop

    :goto_17
    if-nez v2, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_15

    nop

    :goto_18
    const-string v3, "Starting task from recents. id="

    goto :goto_e

    nop

    :goto_19
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    goto :goto_28

    nop

    :goto_1a
    invoke-static {v1, v3, v2}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :goto_1b
    goto :goto_b

    nop

    :goto_1c
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_23

    nop

    :goto_1d
    return-void

    :goto_1e
    goto :goto_2e

    nop

    :goto_1f
    iget v3, v0, Landroid/app/ActivityManager$RecentTaskInfo;->persistentId:I

    goto :goto_2

    nop

    :goto_20
    iget-object v3, v0, Landroid/app/ActivityManager$RecentTaskInfo;->topActivity:Landroid/content/ComponentName;

    goto :goto_1c

    nop

    :goto_21
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_7

    nop

    :goto_22
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_1f

    nop

    :goto_23
    const-string v3, ", baseIntent="

    goto :goto_14

    nop

    :goto_24
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    goto :goto_2d

    nop

    :goto_25
    invoke-static {v1, v2}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    :goto_26
    goto :goto_29

    nop

    :goto_27
    if-eqz v0, :cond_2

    goto :goto_1e

    :cond_2
    goto :goto_f

    nop

    :goto_28
    iget v4, v0, Landroid/app/ActivityManager$RecentTaskInfo;->persistentId:I

    goto :goto_c

    nop

    :goto_29
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->goHome()Z

    goto :goto_1d

    nop

    :goto_2a
    const-string v3, ", persistentId="

    goto :goto_22

    nop

    :goto_2b
    new-instance v3, Ljava/lang/StringBuilder;

    goto :goto_11

    nop

    :goto_2c
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_20

    nop

    :goto_2d
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    goto :goto_1a

    nop

    :goto_2e
    sget-boolean v2, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    goto :goto_17

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_powerPress_JII_V",
        "method":      ".method powerPress(JII)V",
        "type":        "method_replace",
        "search": """\
.method powerPress(JII)V
    .registers 13

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    invoke-virtual {v0}, Lcom/android/server/wm/DisplayPolicy;->isScreenOnEarly()Z

    move-result v0

    const-string v1, "WindowManager"

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    invoke-virtual {v0}, Lcom/android/server/wm/DisplayPolicy;->isScreenOnFully()Z

    move-result v0

    if-nez v0, :cond_0

    const-string v0, "Suppressed redundant power key press while already in the process of turning the screen on."

    invoke-static {v1, v0}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_0
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    invoke-virtual {v0}, Lcom/android/server/wm/DisplayPolicy;->isAwake()Z

    move-result v0

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "powerPress: eventTime="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, p1, p2}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, " interactive="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, " count="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, p3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, " mShortPressOnPowerBehavior="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mShortPressOnPowerBehavior:I

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    const/4 v2, 0x2

    if-ne p3, v2, :cond_1

    iget v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mDoublePressOnPowerBehavior:I

    invoke-direct {p0, p1, p2, v0, v1}, Lcom/android/server/policy/PhoneWindowManager;->powerMultiPressAction(JZI)V

    goto :goto_3

    :cond_1
    const/4 v2, 0x3

    if-ne p3, v2, :cond_2

    iget v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mTriplePressOnPowerBehavior:I

    invoke-direct {p0, p1, p2, v0, v1}, Lcom/android/server/policy/PhoneWindowManager;->powerMultiPressAction(JZI)V

    goto :goto_3

    :cond_2
    if-le p3, v2, :cond_3

    invoke-direct {p0}, Lcom/android/server/policy/PhoneWindowManager;->getMaxMultiPressPowerCount()I

    move-result v2

    if-gt p3, v2, :cond_3

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "No behavior defined for power press count "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, p3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_3

    :cond_3
    const/4 v2, 0x1

    if-ne p3, v2, :cond_e

    invoke-direct {p0, v0, p1, p2}, Lcom/android/server/policy/PhoneWindowManager;->shouldHandleShortPressPowerAction(ZJ)Z

    move-result v3

    if-eqz v3, :cond_e

    invoke-static {}, Landroid/os/microsoft/flags/Flags;->ltwEnabled()Z

    move-result v3

    if-eqz v3, :cond_4

    invoke-static {}, Lcom/android/server/wm/BlackScreenWindowManager;->getInstance()Lcom/android/server/wm/BlackScreenWindowManager;

    move-result-object v3

    invoke-virtual {v3}, Lcom/android/server/wm/BlackScreenWindowManager;->interceptPowerKey()Z

    move-result v3

    if-eqz v3, :cond_4

    return-void

    :cond_4
    iget v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mShortPressOnPowerBehavior:I

    const/4 v4, 0x0

    packed-switch v3, :pswitch_data_0

    goto :goto_3

    :pswitch_0  #0x9
    new-instance v1, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda2;

    invoke-direct {v1, p0, p1, p2}, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda2;-><init>(Lcom/android/server/policy/PhoneWindowManager;J)V

    invoke-direct {p0, v2, v2, v1}, Lcom/android/server/policy/PhoneWindowManager;->attemptToDreamOrAwakeFromShortPowerButtonPress(ZZLjava/lang/Runnable;)V

    goto :goto_3

    :pswitch_1  #0x8
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    const-string v5, "glanceable_hub_enabled"

    invoke-static {v1, v5, v2, v3}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    if-ne v1, v2, :cond_5

    move v1, v2

    goto :goto_0

    :cond_5
    move v1, v4

    :goto_0
    invoke-direct {p0}, Lcom/android/server/policy/PhoneWindowManager;->getDreamManagerInternal()Landroid/service/dreams/DreamManagerInternal;

    move-result-object v3

    if-nez v3, :cond_6

    goto :goto_3

    :cond_6
    invoke-virtual {v3}, Landroid/service/dreams/DreamManagerInternal;->isDreaming()Z

    move-result v5

    if-nez v5, :cond_9

    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardShowing()Z

    move-result v5

    if-eqz v5, :cond_7

    goto :goto_1

    :cond_7
    iget-object v5, p0, Lcom/android/server/policy/PhoneWindowManager;->mLockPatternUtils:Lcom/android/internal/widget/LockPatternUtils;

    iget v6, p0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    invoke-virtual {v5, v6}, Lcom/android/internal/widget/LockPatternUtils;->isLockScreenDisabled(I)Z

    move-result v5

    xor-int/2addr v5, v2

    iget-object v6, p0, Lcom/android/server/policy/PhoneWindowManager;->mUserManagerInternal:Lcom/android/server/pm/UserManagerInternal;

    iget v7, p0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    invoke-virtual {v6, v7}, Lcom/android/server/pm/UserManagerInternal;->isUserUnlocked(I)Z

    move-result v6

    if-eqz v6, :cond_8

    if-eqz v1, :cond_8

    if-eqz v5, :cond_8

    invoke-virtual {v3}, Landroid/service/dreams/DreamManagerInternal;->dreamConditionActive()Z

    move-result v6

    if-eqz v6, :cond_8

    new-instance v4, Landroid/os/Bundle;

    invoke-direct {v4}, Landroid/os/Bundle;-><init>()V

    const-string v6, "extra_trigger_hub"

    invoke-virtual {v4, v6, v2}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    invoke-virtual {p0, v4}, Lcom/android/server/policy/PhoneWindowManager;->lockNow(Landroid/os/Bundle;)V

    goto :goto_3

    :cond_8
    new-instance v6, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda1;

    invoke-direct {v6, p0, p1, p2}, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda1;-><init>(Lcom/android/server/policy/PhoneWindowManager;J)V

    invoke-direct {p0, v2, v4, v6}, Lcom/android/server/policy/PhoneWindowManager;->attemptToDreamOrAwakeFromShortPowerButtonPress(ZZLjava/lang/Runnable;)V

    goto :goto_3

    :cond_9
    :goto_1
    invoke-direct {p0, p1, p2, v4}, Lcom/android/server/policy/PhoneWindowManager;->sleepDefaultDisplayFromPowerButton(JI)Z

    goto :goto_3

    :pswitch_2  #0x7
    new-instance v1, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda0;

    invoke-direct {v1, p0, p1, p2}, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda0;-><init>(Lcom/android/server/policy/PhoneWindowManager;J)V

    invoke-direct {p0, v2, v4, v1}, Lcom/android/server/policy/PhoneWindowManager;->attemptToDreamOrAwakeFromShortPowerButtonPress(ZZLjava/lang/Runnable;)V

    goto :goto_3

    :pswitch_3  #0x6
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    if-eqz v1, :cond_b

    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    invoke-virtual {v1}, Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;->hasKeyguard()Z

    move-result v1

    if-eqz v1, :cond_b

    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    iget v2, p0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    invoke-virtual {v1, v2}, Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;->isSecure(I)Z

    move-result v1

    if-eqz v1, :cond_b

    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->keyguardOn()Z

    move-result v1

    if-eqz v1, :cond_a

    goto :goto_2

    :cond_a
    const/4 v1, 0x0

    invoke-virtual {p0, v1}, Lcom/android/server/policy/PhoneWindowManager;->lockNow(Landroid/os/Bundle;)V

    goto :goto_3

    :cond_b
    :goto_2
    invoke-direct {p0, p1, p2, v4}, Lcom/android/server/policy/PhoneWindowManager;->sleepDefaultDisplayFromPowerButton(JI)Z

    goto :goto_3

    :pswitch_4  #0x5
    iget-boolean v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mDismissImeOnBackKeyPressed:Z

    if-eqz v1, :cond_c

    invoke-static {}, Lcom/android/server/inputmethod/InputMethodManagerInternal;->get()Lcom/android/server/inputmethod/InputMethodManagerInternal;

    move-result-object v1

    const/16 v2, 0x11

    invoke-virtual {v1, v2, p4}, Lcom/android/server/inputmethod/InputMethodManagerInternal;->hideInputMethod(II)V

    goto :goto_3

    :cond_c
    invoke-direct {p0}, Lcom/android/server/policy/PhoneWindowManager;->shortPressPowerGoHome()V

    goto :goto_3

    :pswitch_5  #0x4
    invoke-direct {p0}, Lcom/android/server/policy/PhoneWindowManager;->shortPressPowerGoHome()V

    goto :goto_3

    :pswitch_6  #0x3
    invoke-direct {p0, p1, p2, v2}, Lcom/android/server/policy/PhoneWindowManager;->sleepDefaultDisplayFromPowerButton(JI)Z

    move-result v1

    if-eqz v1, :cond_e

    invoke-virtual {p0, v4}, Lcom/android/server/policy/PhoneWindowManager;->launchHomeFromHotKey(I)V

    goto :goto_3

    :pswitch_7  #0x2
    invoke-direct {p0, p1, p2, v2}, Lcom/android/server/policy/PhoneWindowManager;->sleepDefaultDisplayFromPowerButton(JI)Z

    goto :goto_3

    :pswitch_8  #0x1
    sget-boolean v2, Lmiui/enterprise/EnterpriseManagerStub;->ENTERPRISE_ACTIVATED:Z

    if-eqz v2, :cond_d

    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object v2

    const-string v3, "disable_key_behavior_short_press_power_key"

    invoke-interface {v2, v3}, Lmiui/enterprise/IRestrictionsHelper;->isRestriction(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_d

    const-string v2, "enterprise Restriction behavior: short press power key to sleep."

    invoke-static {v1, v2}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_d
    invoke-direct {p0, p1, p2, v4}, Lcom/android/server/policy/PhoneWindowManager;->sleepDefaultDisplayFromPowerButton(JI)Z

    goto :goto_3

    :pswitch_9  #0x0
    nop

    :cond_e
    :goto_3
    return-void

    :pswitch_data_0
    .packed-switch 0x0
        :pswitch_9  #00000000
        :pswitch_8  #00000001
        :pswitch_7  #00000002
        :pswitch_6  #00000003
        :pswitch_5  #00000004
        :pswitch_4  #00000005
        :pswitch_3  #00000006
        :pswitch_2  #00000007
        :pswitch_1  #00000008
        :pswitch_0  #00000009
    .end packed-switch
.end method
""",
        "replacement": """\
.method powerPress(JII)V
    .registers 13

    goto :goto_98

    nop

    :goto_0
    invoke-virtual {v3}, Landroid/service/dreams/DreamManagerInternal;->dreamConditionActive()Z

    move-result v6

    goto :goto_9a

    nop

    :goto_1
    const-string v3, " interactive="

    goto :goto_7b

    nop

    :goto_2
    invoke-virtual {v2, p1, p2}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_1

    nop

    :goto_3
    goto :goto_a7

    :goto_4
    goto :goto_75

    nop

    :goto_5
    const-string v3, " count="

    goto :goto_9f

    nop

    :goto_6
    iget v2, p0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    goto :goto_9e

    nop

    :goto_7
    invoke-direct {v6, p0, p1, p2}, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda1;-><init>(Lcom/android/server/policy/PhoneWindowManager;J)V

    goto :goto_72

    nop

    :goto_8
    invoke-static {v1, v0}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_11

    nop

    :goto_9
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_46

    nop

    :goto_a
    invoke-virtual {v0}, Lcom/android/server/wm/DisplayPolicy;->isScreenOnEarly()Z

    move-result v0

    goto :goto_76

    nop

    :goto_b
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    goto :goto_1d

    nop

    :goto_c
    iget v7, p0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    goto :goto_5f

    nop

    :goto_d
    return-void

    :goto_e
    goto :goto_3f

    nop

    :goto_f
    iget v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mTriplePressOnPowerBehavior:I

    goto :goto_66

    nop

    :goto_10
    return-void

    nop

    :pswitch_data_0
    .packed-switch 0x0
        :pswitch_7  #00000000
        :pswitch_3  #00000001
        :pswitch_2  #00000002
        :pswitch_5  #00000003
        :pswitch_1  #00000004
        :pswitch_0  #00000005
        :pswitch_9  #00000006
        :pswitch_4  #00000007
        :pswitch_6  #00000008
        :pswitch_8  #00000009
    .end packed-switch

    :goto_11
    return-void

    :goto_12
    goto :goto_91

    nop

    :goto_13
    if-nez v5, :cond_0

    goto :goto_4b

    :cond_0
    goto :goto_0

    nop

    :goto_14
    invoke-direct {p0, p1, p2, v0, v1}, Lcom/android/server/policy/PhoneWindowManager;->powerMultiPressAction(JZI)V

    goto :goto_3

    nop

    :goto_15
    goto :goto_a7

    :goto_16
    goto :goto_5c

    nop

    :goto_17
    new-instance v6, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda1;

    goto :goto_7

    nop

    :goto_18
    const/4 v1, 0x0

    goto :goto_24

    nop

    :goto_19
    iget-object v6, p0, Lcom/android/server/policy/PhoneWindowManager;->mUserManagerInternal:Lcom/android/server/pm/UserManagerInternal;

    goto :goto_c

    nop

    :goto_1a
    iget v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    goto :goto_2a

    nop

    :goto_1b
    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object v2

    goto :goto_2f

    nop

    :goto_1c
    invoke-virtual {v0}, Lcom/android/server/wm/DisplayPolicy;->isAwake()Z

    move-result v0

    goto :goto_65

    nop

    :goto_1d
    invoke-virtual {v0}, Lcom/android/server/wm/DisplayPolicy;->isScreenOnFully()Z

    move-result v0

    goto :goto_70

    nop

    :goto_1e
    if-nez v3, :cond_1

    goto :goto_a7

    :cond_1
    goto :goto_5e

    nop

    :goto_1f
    if-eqz v3, :cond_2

    goto :goto_42

    :cond_2
    goto :goto_41

    nop

    :goto_20
    invoke-direct {p0, v2, v2, v1}, Lcom/android/server/policy/PhoneWindowManager;->attemptToDreamOrAwakeFromShortPowerButtonPress(ZZLjava/lang/Runnable;)V

    goto :goto_97

    nop

    :goto_21
    goto :goto_3c

    :goto_22
    goto :goto_18

    nop

    :goto_23
    new-instance v1, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda0;

    goto :goto_8f

    nop

    :goto_24
    invoke-virtual {p0, v1}, Lcom/android/server/policy/PhoneWindowManager;->lockNow(Landroid/os/Bundle;)V

    goto :goto_3b

    nop

    :goto_25
    invoke-virtual {v1}, Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;->hasKeyguard()Z

    move-result v1

    goto :goto_8b

    nop

    :goto_26
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    goto :goto_25

    nop

    :goto_27
    new-instance v4, Landroid/os/Bundle;

    goto :goto_a9

    nop

    :goto_28
    goto :goto_a7

    :pswitch_0  #0x5
    goto :goto_92

    nop

    :goto_29
    if-eq p3, v2, :cond_3

    goto :goto_7d

    :cond_3
    goto :goto_f

    nop

    :goto_2a
    const-string v5, "glanceable_hub_enabled"

    goto :goto_47

    nop

    :goto_2b
    invoke-direct {v1, p0, p1, p2}, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda2;-><init>(Lcom/android/server/policy/PhoneWindowManager;J)V

    goto :goto_20

    nop

    :goto_2c
    invoke-virtual {v2, p3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_30

    nop

    :goto_2d
    invoke-direct {p0}, Lcom/android/server/policy/PhoneWindowManager;->getDreamManagerInternal()Landroid/service/dreams/DreamManagerInternal;

    move-result-object v3

    goto :goto_1f

    nop

    :goto_2e
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_9c

    nop

    :goto_2f
    const-string v3, "disable_key_behavior_short_press_power_key"

    goto :goto_4c

    nop

    :goto_30
    const-string v3, " mShortPressOnPowerBehavior="

    goto :goto_90

    nop

    :goto_31
    goto :goto_a7

    :goto_32
    goto :goto_50

    nop

    :goto_33
    iget v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mShortPressOnPowerBehavior:I

    goto :goto_45

    nop

    :goto_34
    xor-int/2addr v5, v2

    goto :goto_19

    nop

    :goto_35
    if-nez v6, :cond_4

    goto :goto_4b

    :cond_4
    goto :goto_4f

    nop

    :goto_36
    invoke-direct {p0, p1, p2, v2}, Lcom/android/server/policy/PhoneWindowManager;->sleepDefaultDisplayFromPowerButton(JI)Z

    goto :goto_6f

    nop

    :goto_37
    invoke-virtual {v1, v2, p4}, Lcom/android/server/inputmethod/InputMethodManagerInternal;->hideInputMethod(II)V

    goto :goto_73

    nop

    :goto_38
    goto :goto_3e

    :goto_39
    goto :goto_3d

    nop

    :goto_3a
    if-eqz v5, :cond_5

    goto :goto_32

    :cond_5
    goto :goto_82

    nop

    :goto_3b
    goto :goto_a7

    :goto_3c
    goto :goto_52

    nop

    :goto_3d
    move v1, v4

    :goto_3e
    goto :goto_2d

    nop

    :goto_3f
    invoke-direct {p0, p1, p2, v4}, Lcom/android/server/policy/PhoneWindowManager;->sleepDefaultDisplayFromPowerButton(JI)Z

    goto :goto_a6

    nop

    :goto_40
    if-nez v1, :cond_6

    goto :goto_3c

    :cond_6
    goto :goto_5d

    nop

    :goto_41
    goto :goto_a7

    :goto_42
    goto :goto_7e

    nop

    :goto_43
    invoke-static {}, Lcom/android/server/wm/BlackScreenWindowManager;->getInstance()Lcom/android/server/wm/BlackScreenWindowManager;

    move-result-object v3

    goto :goto_4e

    nop

    :goto_44
    if-eq v1, v2, :cond_7

    goto :goto_39

    :cond_7
    goto :goto_84

    nop

    :goto_45
    const/4 v4, 0x0

    packed-switch v3, :pswitch_data_0

    goto :goto_aa

    nop

    :goto_46
    const-string v3, "powerPress: eventTime="

    goto :goto_81

    nop

    :goto_47
    invoke-static {v1, v5, v2, v3}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    goto :goto_44

    nop

    :goto_48
    invoke-virtual {v4, v6, v2}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    goto :goto_62

    nop

    :goto_49
    iget v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mShortPressOnPowerBehavior:I

    goto :goto_78

    nop

    :goto_4a
    goto :goto_a7

    :goto_4b
    goto :goto_17

    nop

    :goto_4c
    invoke-interface {v2, v3}, Lmiui/enterprise/IRestrictionsHelper;->isRestriction(Ljava/lang/String;)Z

    move-result v2

    goto :goto_79

    nop

    :goto_4d
    invoke-direct {p0}, Lcom/android/server/policy/PhoneWindowManager;->getMaxMultiPressPowerCount()I

    move-result v2

    goto :goto_a2

    nop

    :goto_4e
    invoke-virtual {v3}, Lcom/android/server/wm/BlackScreenWindowManager;->interceptPowerKey()Z

    move-result v3

    goto :goto_7a

    nop

    :goto_4f
    if-nez v1, :cond_8

    goto :goto_4b

    :cond_8
    goto :goto_13

    nop

    :goto_50
    invoke-direct {p0, p1, p2, v4}, Lcom/android/server/policy/PhoneWindowManager;->sleepDefaultDisplayFromPowerButton(JI)Z

    goto :goto_8d

    nop

    :goto_51
    const/4 v2, 0x2

    goto :goto_8e

    nop

    :goto_52
    invoke-direct {p0, p1, p2, v4}, Lcom/android/server/policy/PhoneWindowManager;->sleepDefaultDisplayFromPowerButton(JI)Z

    goto :goto_28

    nop

    :goto_53
    const-string v0, "Suppressed redundant power key press while already in the process of turning the screen on."

    goto :goto_8

    nop

    :goto_54
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_a0

    nop

    :goto_55
    if-eq p3, v2, :cond_9

    goto :goto_a7

    :cond_9
    goto :goto_88

    nop

    :goto_56
    const-string v6, "extra_trigger_hub"

    goto :goto_48

    nop

    :goto_57
    goto :goto_32

    :goto_58
    goto :goto_64

    nop

    :goto_59
    return-void

    :goto_5a
    goto :goto_33

    nop

    :goto_5b
    if-nez v1, :cond_a

    goto :goto_a7

    :cond_a
    goto :goto_6e

    nop

    :goto_5c
    const/4 v2, 0x1

    goto :goto_55

    nop

    :goto_5d
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->keyguardOn()Z

    move-result v1

    goto :goto_77

    nop

    :goto_5e
    invoke-static {}, Landroid/os/microsoft/flags/Flags;->ltwEnabled()Z

    move-result v3

    goto :goto_a5

    nop

    :goto_5f
    invoke-virtual {v6, v7}, Lcom/android/server/pm/UserManagerInternal;->isUserUnlocked(I)Z

    move-result v6

    goto :goto_35

    nop

    :goto_60
    goto :goto_a7

    :pswitch_1  #0x4
    goto :goto_95

    nop

    :goto_61
    goto :goto_a7

    :pswitch_2  #0x2
    goto :goto_36

    nop

    :goto_62
    invoke-virtual {p0, v4}, Lcom/android/server/policy/PhoneWindowManager;->lockNow(Landroid/os/Bundle;)V

    goto :goto_4a

    nop

    :goto_63
    iget v6, p0, Lcom/android/server/policy/PhoneWindowManager;->mCurrentUserId:I

    goto :goto_86

    nop

    :goto_64
    iget-object v5, p0, Lcom/android/server/policy/PhoneWindowManager;->mLockPatternUtils:Lcom/android/internal/widget/LockPatternUtils;

    goto :goto_63

    nop

    :goto_65
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_66
    invoke-direct {p0, p1, p2, v0, v1}, Lcom/android/server/policy/PhoneWindowManager;->powerMultiPressAction(JZI)V

    goto :goto_7c

    nop

    :goto_67
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_69

    nop

    :goto_68
    if-gt p3, v2, :cond_b

    goto :goto_16

    :cond_b
    goto :goto_4d

    nop

    :goto_69
    invoke-virtual {v2, p3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_2e

    nop

    :goto_6a
    invoke-direct {p0, p1, p2, v2}, Lcom/android/server/policy/PhoneWindowManager;->sleepDefaultDisplayFromPowerButton(JI)Z

    move-result v1

    goto :goto_5b

    nop

    :goto_6b
    invoke-static {v1, v2}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_51

    nop

    :goto_6c
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_ac

    nop

    :goto_6d
    if-nez v0, :cond_c

    goto :goto_12

    :cond_c
    goto :goto_b

    nop

    :goto_6e
    invoke-virtual {p0, v4}, Lcom/android/server/policy/PhoneWindowManager;->launchHomeFromHotKey(I)V

    goto :goto_61

    nop

    :goto_6f
    goto :goto_a7

    :pswitch_3  #0x1
    goto :goto_7f

    nop

    :goto_70
    if-eqz v0, :cond_d

    goto :goto_12

    :cond_d
    goto :goto_53

    nop

    :goto_71
    const/16 v2, 0x11

    goto :goto_37

    nop

    :goto_72
    invoke-direct {p0, v2, v4, v6}, Lcom/android/server/policy/PhoneWindowManager;->attemptToDreamOrAwakeFromShortPowerButtonPress(ZZLjava/lang/Runnable;)V

    goto :goto_31

    nop

    :goto_73
    goto :goto_a7

    :goto_74
    goto :goto_9b

    nop

    :goto_75
    const/4 v2, 0x3

    goto :goto_29

    nop

    :goto_76
    const-string v1, "WindowManager"

    goto :goto_6d

    nop

    :goto_77
    if-nez v1, :cond_e

    goto :goto_22

    :cond_e
    goto :goto_21

    nop

    :goto_78
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_8c

    nop

    :goto_79
    if-nez v2, :cond_f

    goto :goto_e

    :cond_f
    goto :goto_83

    nop

    :goto_7a
    if-nez v3, :cond_10

    goto :goto_5a

    :cond_10
    goto :goto_59

    nop

    :goto_7b
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_a3

    nop

    :goto_7c
    goto :goto_a7

    :goto_7d
    goto :goto_68

    nop

    :goto_7e
    invoke-virtual {v3}, Landroid/service/dreams/DreamManagerInternal;->isDreaming()Z

    move-result v5

    goto :goto_3a

    nop

    :goto_7f
    sget-boolean v2, Lmiui/enterprise/EnterpriseManagerStub;->ENTERPRISE_ACTIVATED:Z

    goto :goto_8a

    nop

    :goto_80
    if-nez v1, :cond_11

    goto :goto_74

    :cond_11
    goto :goto_a8

    nop

    :goto_81
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_2

    nop

    :goto_82
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardShowing()Z

    move-result v5

    goto :goto_94

    nop

    :goto_83
    const-string v2, "enterprise Restriction behavior: short press power key to sleep."

    goto :goto_a4

    nop

    :goto_84
    move v1, v2

    goto :goto_38

    nop

    :goto_85
    new-instance v1, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda2;

    goto :goto_2b

    nop

    :goto_86
    invoke-virtual {v5, v6}, Lcom/android/internal/widget/LockPatternUtils;->isLockScreenDisabled(I)Z

    move-result v5

    goto :goto_34

    nop

    :goto_87
    if-nez v1, :cond_12

    goto :goto_3c

    :cond_12
    goto :goto_26

    nop

    :goto_88
    invoke-direct {p0, v0, p1, p2}, Lcom/android/server/policy/PhoneWindowManager;->shouldHandleShortPressPowerAction(ZJ)Z

    move-result v3

    goto :goto_1e

    nop

    :goto_89
    iget v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mDoublePressOnPowerBehavior:I

    goto :goto_14

    nop

    :goto_8a
    if-nez v2, :cond_13

    goto :goto_e

    :cond_13
    goto :goto_1b

    nop

    :goto_8b
    if-nez v1, :cond_14

    goto :goto_3c

    :cond_14
    goto :goto_93

    nop

    :goto_8c
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_6b

    nop

    :goto_8d
    goto :goto_a7

    :pswitch_4  #0x7
    goto :goto_23

    nop

    :goto_8e
    if-eq p3, v2, :cond_15

    goto :goto_4

    :cond_15
    goto :goto_89

    nop

    :goto_8f
    invoke-direct {v1, p0, p1, p2}, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda0;-><init>(Lcom/android/server/policy/PhoneWindowManager;J)V

    goto :goto_99

    nop

    :goto_90
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_49

    nop

    :goto_91
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    goto :goto_1c

    nop

    :goto_92
    iget-boolean v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mDismissImeOnBackKeyPressed:Z

    goto :goto_80

    nop

    :goto_93
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    goto :goto_6

    nop

    :goto_94
    if-nez v5, :cond_16

    goto :goto_58

    :cond_16
    goto :goto_57

    nop

    :goto_95
    invoke-direct {p0}, Lcom/android/server/policy/PhoneWindowManager;->shortPressPowerGoHome()V

    goto :goto_96

    nop

    :goto_96
    goto :goto_a7

    :pswitch_5  #0x3
    goto :goto_6a

    nop

    :goto_97
    goto :goto_a7

    :pswitch_6  #0x8
    goto :goto_6c

    nop

    :goto_98
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    goto :goto_a

    nop

    :goto_99
    invoke-direct {p0, v2, v4, v1}, Lcom/android/server/policy/PhoneWindowManager;->attemptToDreamOrAwakeFromShortPowerButtonPress(ZZLjava/lang/Runnable;)V

    goto :goto_ab

    nop

    :goto_9a
    if-nez v6, :cond_17

    goto :goto_4b

    :cond_17
    goto :goto_27

    nop

    :goto_9b
    invoke-direct {p0}, Lcom/android/server/policy/PhoneWindowManager;->shortPressPowerGoHome()V

    goto :goto_60

    nop

    :goto_9c
    invoke-static {v1, v2}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_15

    nop

    :goto_9d
    const-string v3, "No behavior defined for power press count "

    goto :goto_67

    nop

    :goto_9e
    invoke-virtual {v1, v2}, Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;->isSecure(I)Z

    move-result v1

    goto :goto_40

    nop

    :goto_9f
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_2c

    nop

    :goto_a0
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_9d

    nop

    :goto_a1
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mKeyguardDelegate:Lcom/android/server/policy/keyguard/KeyguardServiceDelegate;

    goto :goto_87

    nop

    :goto_a2
    if-le p3, v2, :cond_18

    goto :goto_16

    :cond_18
    goto :goto_54

    nop

    :goto_a3
    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_5

    nop

    :goto_a4
    invoke-static {v1, v2}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_d

    nop

    :goto_a5
    if-nez v3, :cond_19

    goto :goto_5a

    :cond_19
    goto :goto_43

    nop

    :goto_a6
    goto :goto_a7

    :pswitch_7  #0x0
    nop

    :goto_a7
    goto :goto_10

    nop

    :goto_a8
    invoke-static {}, Lcom/android/server/inputmethod/InputMethodManagerInternal;->get()Lcom/android/server/inputmethod/InputMethodManagerInternal;

    move-result-object v1

    goto :goto_71

    nop

    :goto_a9
    invoke-direct {v4}, Landroid/os/Bundle;-><init>()V

    goto :goto_56

    nop

    :goto_aa
    goto :goto_a7

    :pswitch_8  #0x9
    goto :goto_85

    nop

    :goto_ab
    goto :goto_a7

    :pswitch_9  #0x6
    goto :goto_a1

    nop

    :goto_ac
    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    goto :goto_1a

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_readLidState__V",
        "method":      ".method readLidState()V",
        "type":        "method_replace",
        "search": """\
.method readLidState()V
    .registers 3

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerFuncs:Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;

    invoke-interface {v1}, Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;->getLidState()I

    move-result v1

    invoke-virtual {v0, v1}, Lcom/android/server/wm/DisplayPolicy;->setLidState(I)V

    return-void
.end method
""",
        "replacement": """\
.method readLidState()V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    invoke-interface {v1}, Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;->getLidState()I

    move-result v1

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {v0, v1}, Lcom/android/server/wm/DisplayPolicy;->setLidState(I)V

    goto :goto_0

    nop

    :goto_3
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mDefaultDisplayPolicy:Lcom/android/server/wm/DisplayPolicy;

    goto :goto_4

    nop

    :goto_4
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerFuncs:Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;

    goto :goto_1

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_requestBugreportForTv__V",
        "method":      ".method requestBugreportForTv()V",
        "type":        "method_replace",
        "search": """\
.method requestBugreportForTv()V
    .registers 4

    :try_start_0
    invoke-static {}, Landroid/app/ActivityManager;->getService()Landroid/app/IActivityManager;

    move-result-object v0

    invoke-interface {v0}, Landroid/app/IActivityManager;->launchBugReportHandlerApp()Z

    move-result v0

    if-nez v0, :cond_0

    invoke-static {}, Landroid/app/ActivityManager;->getService()Landroid/app/IActivityManager;

    move-result-object v0

    invoke-interface {v0}, Landroid/app/IActivityManager;->requestInteractiveBugReport()V
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    :cond_0
    goto :goto_0

    :catch_0
    move-exception v0

    const-string v1, "WindowManager"

    const-string v2, "Error taking bugreport"

    invoke-static {v1, v2, v0}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :goto_0
    return-void
.end method
""",
        "replacement": """\
.method requestBugreportForTv()V
    .registers 4

    :try_start_0
    invoke-static {}, Landroid/app/ActivityManager;->getService()Landroid/app/IActivityManager;

    move-result-object v0

    invoke-interface {v0}, Landroid/app/IActivityManager;->launchBugReportHandlerApp()Z

    move-result v0

    if-nez v0, :cond_0

    invoke-static {}, Landroid/app/ActivityManager;->getService()Landroid/app/IActivityManager;

    move-result-object v0

    invoke-interface {v0}, Landroid/app/IActivityManager;->requestInteractiveBugReport()V
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    :cond_0
    goto :goto_3

    nop

    :goto_0
    const-string v2, "Error taking bugreport"

    goto :goto_4

    nop

    :goto_1
    const-string v1, "WindowManager"

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    goto :goto_5

    :catch_0
    move-exception v0

    goto :goto_1

    nop

    :goto_4
    invoke-static {v1, v2, v0}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :goto_5
    goto :goto_2

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_sendCloseSystemWindows__V",
        "method":      ".method sendCloseSystemWindows()V",
        "type":        "method_replace",
        "search": """\
.method sendCloseSystemWindows()V
    .registers 3

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    const/4 v1, 0x0

    invoke-static {v0, v1}, Lcom/android/internal/policy/PhoneWindow;->sendCloseSystemWindows(Landroid/content/Context;Ljava/lang/String;)V

    return-void
.end method
""",
        "replacement": """\
.method sendCloseSystemWindows()V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    invoke-static {v0, v1}, Lcom/android/internal/policy/PhoneWindow;->sendCloseSystemWindows(Landroid/content/Context;Ljava/lang/String;)V

    goto :goto_3

    nop

    :goto_1
    const/4 v1, 0x0

    goto :goto_0

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_1

    nop

    :goto_3
    return-void
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_sendCloseSystemWindows_Ljava_lang_String__V",
        "method":      ".method sendCloseSystemWindows(Ljava/lang/String;)V",
        "type":        "method_replace",
        "search": """\
.method sendCloseSystemWindows(Ljava/lang/String;)V
    .registers 3

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-static {v0, p1}, Lcom/android/internal/policy/PhoneWindow;->sendCloseSystemWindows(Landroid/content/Context;Ljava/lang/String;)V

    return-void
.end method
""",
        "replacement": """\
.method sendCloseSystemWindows(Ljava/lang/String;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-static {v0, p1}, Lcom/android/internal/policy/PhoneWindow;->sendCloseSystemWindows(Landroid/content/Context;Ljava/lang/String;)V

    goto :goto_1

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "add_method_sendMediaButtonEvent_I_V",
        "method":      ".method public sendMediaButtonEvent(I)V",
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method public sendMediaButtonEvent(I)V
    .registers 11

    const/4 v6, 0x0

    sget-boolean v0, Lcom/android/server/policy/VolBtnHelper;->mVolBtnVibrate:Z

    if-eqz v0, :cond_0

    const-string v0, "Power - Long Press - Global Actions"

    invoke-direct {p0, v6, v0}, Lcom/android/server/policy/PhoneWindowManager;->performHapticFeedback(ILjava/lang/String;)V

    :cond_0
    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v2

    new-instance v1, Landroid/view/KeyEvent;

    move-wide v4, v2

    move v7, p1

    move v8, v6

    invoke-direct/range {v1 .. v8}, Landroid/view/KeyEvent;-><init>(JJIII)V

    invoke-virtual {p0, v1}, Lcom/android/server/policy/PhoneWindowManager;->dispatchMediaKeyWithWakeLockToAudioService(Landroid/view/KeyEvent;)V

    const/4 v0, 0x1

    invoke-static {v1, v0}, Landroid/view/KeyEvent;->changeAction(Landroid/view/KeyEvent;I)Landroid/view/KeyEvent;

    move-result-object v0

    invoke-virtual {p0, v0}, Lcom/android/server/policy/PhoneWindowManager;->dispatchMediaKeyWithWakeLockToAudioService(Landroid/view/KeyEvent;)V

    return-void
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setDebugSwitch_Z_V",
        "method":      ".method protected setDebugSwitch(Z)V",
        "type":        "method_replace",
        "search": """\
.method protected setDebugSwitch(Z)V
    .registers 3

    sput-boolean p1, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mSingleKeyGestureDetector:Lcom/android/server/policy/SingleKeyGestureDetector;

    invoke-virtual {v0, p1}, Lcom/android/server/policy/SingleKeyGestureDetector;->setDebugSwitch(Z)V

    return-void
.end method
""",
        "replacement": """\
.method protected setDebugSwitch(Z)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mSingleKeyGestureDetector:Lcom/android/server/policy/SingleKeyGestureDetector;

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {v0, p1}, Lcom/android/server/policy/SingleKeyGestureDetector;->setDebugSwitch(Z)V

    goto :goto_1

    nop

    :goto_3
    sput-boolean p1, Lcom/android/server/policy/PhoneWindowManager;->DEBUG_INPUT:Z

    goto :goto_0

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_showGlobalActionsInternal__V",
        "method":      ".method showGlobalActionsInternal()V",
        "type":        "method_replace",
        "search": """\
.method showGlobalActionsInternal()V
    .registers 6

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mGlobalActions:Lcom/android/server/policy/GlobalActions;

    if-nez v0, :cond_0

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mGlobalActionsFactory:Ljava/util/function/Supplier;

    invoke-interface {v0}, Ljava/util/function/Supplier;->get()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/server/policy/GlobalActions;

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mGlobalActions:Lcom/android/server/policy/GlobalActions;

    :cond_0
    sget-boolean v0, Lmiui/enterprise/EnterpriseManagerStub;->ENTERPRISE_ACTIVATED:Z

    if-eqz v0, :cond_1

    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object v0

    const-string v1, "disable_key_behavior_long_press_power_key"

    invoke-interface {v0, v1}, Lmiui/enterprise/IRestrictionsHelper;->isRestriction(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_1

    const-string v0, "WindowManager"

    const-string v1, "enterprise Restriction show dialog"

    invoke-static {v0, v1}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_1
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardShowingAndNotOccluded()Z

    move-result v0

    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mGlobalActions:Lcom/android/server/policy/GlobalActions;

    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isDeviceProvisioned()Z

    move-result v2

    invoke-virtual {v1, v0, v2}, Lcom/android/server/policy/GlobalActions;->showDialog(ZZ)V

    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v2

    const/4 v4, 0x0

    invoke-virtual {v1, v2, v3, v4}, Landroid/os/PowerManager;->userActivity(JZ)V

    return-void
.end method
""",
        "replacement": """\
.method showGlobalActionsInternal()V
    .registers 6

    goto :goto_21

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mGlobalActions:Lcom/android/server/policy/GlobalActions;

    goto :goto_1a

    nop

    :goto_1
    invoke-interface {v0, v1}, Lmiui/enterprise/IRestrictionsHelper;->isRestriction(Ljava/lang/String;)Z

    move-result v0

    goto :goto_19

    nop

    :goto_2
    if-nez v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_1f

    nop

    :goto_3
    invoke-interface {v0}, Ljava/util/function/Supplier;->get()Ljava/lang/Object;

    move-result-object v0

    goto :goto_14

    nop

    :goto_4
    if-nez v0, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_c

    nop

    :goto_5
    return-void

    :goto_6
    goto :goto_18

    nop

    :goto_7
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mGlobalActionsFactory:Ljava/util/function/Supplier;

    goto :goto_3

    nop

    :goto_8
    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mGlobalActions:Lcom/android/server/policy/GlobalActions;

    :goto_9
    goto :goto_b

    nop

    :goto_a
    const-string v0, "WindowManager"

    goto :goto_1d

    nop

    :goto_b
    sget-boolean v0, Lmiui/enterprise/EnterpriseManagerStub;->ENTERPRISE_ACTIVATED:Z

    goto :goto_2

    nop

    :goto_c
    goto :goto_11

    :goto_d
    goto :goto_0

    nop

    :goto_e
    const-string v1, "disable_key_behavior_long_press_power_key"

    goto :goto_1

    nop

    :goto_f
    invoke-static {v0, v1}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_5

    nop

    :goto_10
    invoke-virtual {v1, v2, v3, v4}, Landroid/os/PowerManager;->userActivity(JZ)V

    :goto_11
    goto :goto_1b

    nop

    :goto_12
    if-eqz v0, :cond_2

    goto :goto_d

    :cond_2
    goto :goto_13

    nop

    :goto_13
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardLocked()Z

    move-result v0

    goto :goto_4

    nop

    :goto_14
    check-cast v0, Lcom/android/server/policy/GlobalActions;

    goto :goto_8

    nop

    :goto_15
    const/4 v4, 0x0

    goto :goto_10

    nop

    :goto_16
    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v2

    goto :goto_15

    nop

    :goto_17
    invoke-virtual {v1, v0, v2}, Lcom/android/server/policy/GlobalActions;->showDialog(ZZ)V

    goto :goto_20

    nop

    :goto_18
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isKeyguardShowingAndNotOccluded()Z

    move-result v0

    goto :goto_1e

    nop

    :goto_19
    if-nez v0, :cond_3

    goto :goto_6

    :cond_3
    goto :goto_a

    nop

    :goto_1a
    if-eqz v0, :cond_4

    goto :goto_9

    :cond_4
    goto :goto_7

    nop

    :goto_1b
    return-void

    :goto_1c
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isDeviceProvisioned()Z

    move-result v2

    goto :goto_17

    nop

    :goto_1d
    const-string v1, "enterprise Restriction show dialog"

    goto :goto_f

    nop

    :goto_1e
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mGlobalActions:Lcom/android/server/policy/GlobalActions;

    goto :goto_1c

    nop

    :goto_1f
    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object v0

    goto :goto_e

    nop

    :goto_20
    iget-object v1, p0, Lcom/android/server/policy/PhoneWindowManager;->mPowerManager:Landroid/os/PowerManager;

    goto :goto_16

    nop

    :goto_21
    iget-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mPowerMenuUnderKeyguard:Z

    goto :goto_12

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_startDockOrHome_IZZ_V",
        "method":      ".method startDockOrHome(IZZ)V",
        "type":        "method_replace",
        "search": """\
.method startDockOrHome(IZZ)V
    .registers 5

    const-string v0, "startDockOrHome"

    invoke-virtual {p0, p1, p2, p3, v0}, Lcom/android/server/policy/PhoneWindowManager;->startDockOrHome(IZZLjava/lang/String;)V

    return-void
.end method
""",
        "replacement": """\
.method startDockOrHome(IZZ)V
    .registers 5

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    const-string v0, "startDockOrHome"

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, p1, p2, p3, v0}, Lcom/android/server/policy/PhoneWindowManager;->startDockOrHome(IZZLjava/lang/String;)V

    goto :goto_0

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_startDockOrHome_IZZLjava_lang_String__V",
        "method":      ".method startDockOrHome(IZZLjava/lang/String;)V",
        "type":        "method_replace",
        "search": """\
.method startDockOrHome(IZZLjava/lang/String;)V
    .registers 14

    :try_start_0
    invoke-static {}, Landroid/app/ActivityManager;->getService()Landroid/app/IActivityManager;

    move-result-object v0

    invoke-interface {v0}, Landroid/app/IActivityManager;->stopAppSwitches()V
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception v0

    :goto_0
    nop

    const-string v0, "homekey"

    invoke-virtual {p0, v0}, Lcom/android/server/policy/PhoneWindowManager;->sendCloseSystemWindows(Ljava/lang/String;)V

    if-eqz p3, :cond_0

    invoke-static {}, Lcom/android/server/policy/PhoneWindowManager;->awakenDreams()V

    :cond_0
    iget-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHasFeatureAuto:Z

    const-string v1, "WindowManager"

    if-nez v0, :cond_1

    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isUserSetupComplete()Z

    move-result v0

    if-nez v0, :cond_1

    const-string v0, "Not going home because user setup is in progress."

    invoke-static {v1, v0}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_1
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->createHomeDockIntent()Landroid/content/Intent;

    move-result-object v2

    if-eqz v2, :cond_3

    if-eqz p2, :cond_2

    :try_start_1
    const-string v0, "android.intent.extra.FROM_HOME_KEY"

    invoke-virtual {v2, v0, p2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    :cond_2
    sget-object v0, Landroid/os/UserHandle;->CURRENT:Landroid/os/UserHandle;

    invoke-direct {p0, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->startActivityAsUser(Landroid/content/Intent;Landroid/os/UserHandle;)V
    :try_end_1
    .catch Landroid/content/ActivityNotFoundException; {:try_start_1 .. :try_end_1} :catch_1

    return-void

    :catch_1
    move-exception v0

    :cond_3
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "startDockOrHome: startReason= "

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mUserManagerInternal:Lcom/android/server/pm/UserManagerInternal;

    invoke-virtual {v0, p1}, Lcom/android/server/pm/UserManagerInternal;->getUserAssignedToDisplay(I)I

    move-result v4

    iget-object v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mActivityTaskManagerInternal:Lcom/android/server/wm/ActivityTaskManagerInternal;

    const/4 v7, 0x1

    move v6, p1

    move v8, p2

    move-object v5, p4

    invoke-virtual/range {v3 .. v8}, Lcom/android/server/wm/ActivityTaskManagerInternal;->startHomeOnDisplay(ILjava/lang/String;IZZ)Z

    return-void
.end method
""",
        "replacement": """\
.method startDockOrHome(IZZLjava/lang/String;)V
    .registers 14

    :try_start_0
    invoke-static {}, Landroid/app/ActivityManager;->getService()Landroid/app/IActivityManager;

    move-result-object v0

    invoke-interface {v0}, Landroid/app/IActivityManager;->stopAppSwitches()V
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_b

    nop

    :goto_0
    return-void

    :goto_1
    const-string v0, "homekey"

    goto :goto_16

    nop

    :goto_2
    move v8, p2

    goto :goto_4

    nop

    :goto_3
    const-string v3, "startDockOrHome: startReason= "

    goto :goto_8

    nop

    :goto_4
    move-object v5, p4

    goto :goto_10

    nop

    :goto_5
    const/4 v7, 0x1

    goto :goto_13

    nop

    :goto_6
    invoke-virtual {v0, p4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_21

    nop

    :goto_7
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mUserManagerInternal:Lcom/android/server/pm/UserManagerInternal;

    goto :goto_1b

    nop

    :goto_8
    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_6

    nop

    :goto_9
    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_7

    nop

    :goto_a
    iget-boolean v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mHasFeatureAuto:Z

    goto :goto_22

    nop

    :goto_b
    goto :goto_c

    :catch_0
    move-exception v0

    :goto_c
    nop

    goto :goto_1

    nop

    :goto_d
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->createHomeDockIntent()Landroid/content/Intent;

    move-result-object v2

    goto :goto_1a

    nop

    :goto_e
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_f

    nop

    :goto_f
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_3

    nop

    :goto_10
    invoke-virtual/range {v3 .. v8}, Lcom/android/server/wm/ActivityTaskManagerInternal;->startHomeOnDisplay(ILjava/lang/String;IZZ)Z

    goto :goto_0

    nop

    :goto_11
    invoke-static {}, Lcom/android/server/policy/PhoneWindowManager;->awakenDreams()V

    :goto_12
    goto :goto_a

    nop

    :goto_13
    move v6, p1

    goto :goto_2

    nop

    :goto_14
    return-void

    :catch_1
    move-exception v0

    :goto_15
    goto :goto_e

    nop

    :goto_16
    invoke-virtual {p0, v0}, Lcom/android/server/policy/PhoneWindowManager;->sendCloseSystemWindows(Ljava/lang/String;)V

    goto :goto_19

    nop

    :goto_17
    return-void

    :goto_18
    goto :goto_d

    nop

    :goto_19
    if-nez p3, :cond_0

    goto :goto_12

    :cond_0
    goto :goto_11

    nop

    :goto_1a
    if-nez v2, :cond_1

    goto :goto_15

    :cond_1
    goto :goto_24

    nop

    :goto_1b
    invoke-virtual {v0, p1}, Lcom/android/server/pm/UserManagerInternal;->getUserAssignedToDisplay(I)I

    move-result v4

    goto :goto_1e

    nop

    :goto_1c
    const-string v0, "Not going home because user setup is in progress."

    goto :goto_1f

    nop

    :goto_1d
    if-eqz v0, :cond_2

    goto :goto_18

    :cond_2
    goto :goto_23

    nop

    :goto_1e
    iget-object v3, p0, Lcom/android/server/policy/PhoneWindowManager;->mActivityTaskManagerInternal:Lcom/android/server/wm/ActivityTaskManagerInternal;

    goto :goto_5

    nop

    :goto_1f
    invoke-static {v1, v0}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_17

    nop

    :goto_20
    if-eqz v0, :cond_3

    goto :goto_18

    :cond_3
    goto :goto_1c

    nop

    :goto_21
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_9

    nop

    :goto_22
    const-string v1, "WindowManager"

    goto :goto_1d

    nop

    :goto_23
    invoke-virtual {p0}, Lcom/android/server/policy/PhoneWindowManager;->isUserSetupComplete()Z

    move-result v0

    goto :goto_20

    nop

    :goto_24
    if-nez p2, :cond_4

    goto :goto_25

    :cond_4
    :try_start_1
    const-string v0, "android.intent.extra.FROM_HOME_KEY"

    invoke-virtual {v2, v0, p2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    :goto_25
    sget-object v0, Landroid/os/UserHandle;->CURRENT:Landroid/os/UserHandle;

    invoke-direct {p0, v2, v0}, Lcom/android/server/policy/PhoneWindowManager;->startActivityAsUser(Landroid/content/Intent;Landroid/os/UserHandle;)V
    :try_end_1
    .catch Landroid/content/ActivityNotFoundException; {:try_start_1 .. :try_end_1} :catch_1

    goto :goto_14

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_updateRotation_Z_V",
        "method":      ".method updateRotation(Z)V",
        "type":        "method_replace",
        "search": """\
.method updateRotation(Z)V
    .registers 4

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerFuncs:Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;

    const/4 v1, 0x0

    invoke-interface {v0, p1, v1}, Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;->updateRotation(ZZ)V

    return-void
.end method
""",
        "replacement": """\
.method updateRotation(Z)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    const/4 v1, 0x0

    goto :goto_1

    nop

    :goto_1
    invoke-interface {v0, p1, v1}, Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;->updateRotation(ZZ)V

    goto :goto_3

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mWindowManagerFuncs:Lcom/android/server/policy/WindowManagerPolicy$WindowManagerFuncs;

    goto :goto_0

    nop

    :goto_3
    return-void
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_updateSettings_Landroid_os_Handler__V",
        "method":      ".method updateSettings(Landroid/os/Handler;)V",
        "type":        "method_replace",
        "search": """\
.method updateSettings(Landroid/os/Handler;)V
    .registers 18

    move-object/from16 v1, p0

    move-object/from16 v2, p1

    if-eqz v2, :cond_0

    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda6;

    invoke-direct {v0, v1}, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda6;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    invoke-virtual {v2, v0}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    return-void

    :cond_0
    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v3

    const/4 v4, 0x0

    const/4 v5, 0x0

    iget-object v6, v1, Lcom/android/server/policy/PhoneWindowManager;->mLock:Ljava/lang/Object;

    monitor-enter v6

    :try_start_0
    const-string v0, "end_button_behavior"

    const/4 v7, 0x2

    const/4 v8, -0x2

    invoke-static {v3, v0, v7, v8}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndcallBehavior:I

    const-string v0, "incall_power_button_behavior"

    const/4 v7, 0x1

    invoke-static {v3, v0, v7, v8}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mIncallPowerBehavior:I

    const-string v0, "incall_back_button_behavior"

    const/4 v9, 0x0

    invoke-static {v3, v0, v9, v8}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mIncallBackBehavior:I

    const-string v0, "system_navigation_keys_enabled"

    invoke-static {v3, v0, v9, v8}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v7, :cond_1

    move v0, v7

    goto :goto_0

    :cond_1
    move v0, v9

    :goto_0
    iput-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mSystemNavigationKeysEnabled:Z

    const-string v0, "volume_hush_gesture"

    invoke-static {v3, v0, v9, v8}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mRingerToggleChord:I

    const-string v0, "power_button_suppression_delay_after_gesture_wake"

    const/16 v10, 0x320

    invoke-static {v3, v0, v10}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerButtonSuppressionDelayMillis:I

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const v10, 0x11102af

    invoke-virtual {v0, v10}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v0

    if-nez v0, :cond_2

    iput v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mRingerToggleChord:I

    :cond_2
    const/4 v0, 0x0

    iget-boolean v10, v1, Lcom/android/server/policy/PhoneWindowManager;->mWakeGestureEnabledSetting:Z

    if-eq v10, v0, :cond_3

    iput-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mWakeGestureEnabledSetting:Z

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->updateWakeGestureListenerLp()V

    :cond_3
    const-string v10, "screen_off_timeout"

    invoke-static {v3, v10, v9, v8}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v10

    iput v10, v1, Lcom/android/server/policy/PhoneWindowManager;->mLockScreenTimeout:I

    const-string v10, "default_input_method"

    invoke-static {v3, v10, v8}, Landroid/provider/Settings$Secure;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v10

    if-eqz v10, :cond_4

    invoke-virtual {v10}, Ljava/lang/String;->length()I

    move-result v11

    if-lez v11, :cond_4

    move v11, v7

    goto :goto_1

    :cond_4
    move v11, v9

    :goto_1
    iget-boolean v12, v1, Lcom/android/server/policy/PhoneWindowManager;->mHasSoftInput:Z

    if-eq v12, v11, :cond_5

    iput-boolean v11, v1, Lcom/android/server/policy/PhoneWindowManager;->mHasSoftInput:Z

    const/4 v4, 0x1

    :cond_5
    const-string v12, "power_button_short_press"

    iget-object v13, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v13}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v13

    const v14, 0x10e014b

    invoke-virtual {v13, v14}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v13

    invoke-static {v3, v12, v13}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v12

    iput v12, v1, Lcom/android/server/policy/PhoneWindowManager;->mShortPressOnPowerBehavior:I

    const-string v12, "power_button_double_press"

    iget-object v13, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v13}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v13

    const v14, 0x10e008c

    invoke-virtual {v13, v14}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v13

    invoke-static {v3, v12, v13}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v12

    iput v12, v1, Lcom/android/server/policy/PhoneWindowManager;->mDoublePressOnPowerBehavior:I

    const-string v12, "power_button_triple_press"

    iget-object v13, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v13}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v13

    const v14, 0x10e0163

    invoke-virtual {v13, v14}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v13

    invoke-static {v3, v12, v13}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v12

    iput v12, v1, Lcom/android/server/policy/PhoneWindowManager;->mTriplePressOnPowerBehavior:I

    const-string v12, "power_button_long_press"

    iget-object v13, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v13}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v13

    const v14, 0x10e00c8

    invoke-virtual {v13, v14}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v13

    invoke-static {v3, v12, v13}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v12

    const-string v13, "power_button_very_long_press"

    iget-object v14, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v14}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v14

    const v15, 0x10e0169

    invoke-virtual {v14, v15}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v14

    invoke-static {v3, v13, v14}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v13

    iget v14, v1, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnPowerBehavior:I

    if-ne v14, v12, :cond_6

    iget v14, v1, Lcom/android/server/policy/PhoneWindowManager;->mVeryLongPressOnPowerBehavior:I

    if-eq v14, v13, :cond_7

    :cond_6
    iput v12, v1, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnPowerBehavior:I

    iput v13, v1, Lcom/android/server/policy/PhoneWindowManager;->mVeryLongPressOnPowerBehavior:I

    :cond_7
    iget-object v14, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v14}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v14

    const-string v15, "power_button_long_press_duration_ms"

    iget-object v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v9}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v9

    const v7, 0x10e00c9

    invoke-virtual {v9, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v7

    int-to-long v8, v7

    invoke-static {v14, v15, v8, v9}, Landroid/provider/Settings$Global;->getLong(Landroid/content/ContentResolver;Ljava/lang/String;J)J

    move-result-wide v7

    iput-wide v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnPowerAssistantTimeoutMs:J

    const-string v7, "key_chord_power_volume_up"

    iget-object v8, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v8}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    const v9, 0x10e00b8

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v8

    invoke-static {v3, v7, v8}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v7

    iput v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerVolUpBehavior:I

    const-string v7, "stem_primary_button_short_press"

    iget-object v8, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v8}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    const v9, 0x10e014d

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v8

    invoke-static {v3, v7, v8}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v7

    iput v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mShortPressOnStemPrimaryBehavior:I

    const-string v7, "stem_primary_button_double_press"

    iget-object v8, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v8}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    const v9, 0x10e008d

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v8

    invoke-static {v3, v7, v8}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v7

    iput v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mDoublePressOnStemPrimaryBehavior:I

    const-string v7, "stem_primary_button_triple_press"

    iget-object v8, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v8}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    const v9, 0x10e0164

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v8

    invoke-static {v3, v7, v8}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v7

    iput v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mTriplePressOnStemPrimaryBehavior:I

    const-string v7, "stem_primary_button_long_press"

    iget-object v8, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v8}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    const v9, 0x10e00ca

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v8

    invoke-static {v3, v7, v8}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v7

    iput v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnStemPrimaryBehavior:I

    iget-object v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v7}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v7

    const v8, 0x111023c

    invoke-virtual {v7, v8}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v7

    iput-boolean v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mShouldEarlyShortPressOnPower:Z

    iget-object v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v7}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v7

    const v8, 0x111023d

    invoke-virtual {v7, v8}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v7

    iput-boolean v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mShouldEarlyShortPressOnStemPrimary:Z

    const-string v7, "stylus_buttons_enabled"

    const/4 v8, -0x2

    const/4 v9, 0x1

    invoke-static {v3, v7, v9, v8}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v7

    if-ne v7, v9, :cond_8

    const/4 v7, 0x1

    goto :goto_2

    :cond_8
    const/4 v7, 0x0

    :goto_2
    iput-boolean v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mStylusButtonsEnabled:Z

    iget-object v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mInputManagerInternal:Lcom/android/server/input/InputManagerInternal;

    iget-boolean v8, v1, Lcom/android/server/policy/PhoneWindowManager;->mStylusButtonsEnabled:Z

    invoke-virtual {v7, v8}, Lcom/android/server/input/InputManagerInternal;->setStylusButtonMotionEventsEnabled(Z)V

    const-string v7, "nav_bar_kids_mode"

    const/4 v8, -0x2

    const/4 v9, 0x0

    invoke-static {v3, v7, v9, v8}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v7

    const/4 v8, 0x1

    if-ne v7, v8, :cond_9

    const/4 v9, 0x1

    :cond_9
    iget-boolean v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mKidsModeEnabled:Z

    if-eq v7, v9, :cond_a

    iput-boolean v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mKidsModeEnabled:Z

    const/4 v5, 0x1

    :cond_a
    monitor-exit v6
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    if-eqz v5, :cond_b

    invoke-direct {v1, v9}, Lcom/android/server/policy/PhoneWindowManager;->updateKidsModeSettings(Z)V

    :cond_b
    if-eqz v4, :cond_c

    const/4 v8, 0x1

    invoke-virtual {v1, v8}, Lcom/android/server/policy/PhoneWindowManager;->updateRotation(Z)V

    :cond_c
    return-void

    :catchall_0
    move-exception v0

    :try_start_1
    monitor-exit v6
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw v0
.end method
""",
        "replacement": """\
.method updateSettings(Landroid/os/Handler;)V
    .registers 18

    goto :goto_6

    nop

    :goto_0
    monitor-enter v6

    :try_start_0
    const-string v0, "end_button_behavior"

    const/4 v7, 0x2

    const/4 v8, -0x2

    invoke-static {v3, v0, v7, v8}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mEndcallBehavior:I

    const-string v0, "incall_power_button_behavior"

    const/4 v7, 0x1

    invoke-static {v3, v0, v7, v8}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mIncallPowerBehavior:I

    const-string v0, "incall_back_button_behavior"

    const/4 v9, 0x0

    invoke-static {v3, v0, v9, v8}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mIncallBackBehavior:I

    const-string v0, "system_navigation_keys_enabled"

    invoke-static {v3, v0, v9, v8}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v7, :cond_0

    move v0, v7

    goto :goto_1

    :cond_0
    move v0, v9

    :goto_1
    iput-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mSystemNavigationKeysEnabled:Z

    const-string v0, "power_menu_under_keyguard"

    invoke-static {v3, v0, v7, v8}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v7, :cond_1

    move v0, v7

    goto :goto_2

    :cond_1
    move v0, v9

    :goto_2
    iput-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerMenuUnderKeyguard:Z

    const-string v0, "volume_hush_gesture"

    invoke-static {v3, v0, v9, v8}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mRingerToggleChord:I

    const-string v0, "power_button_suppression_delay_after_gesture_wake"

    const/16 v10, 0x320

    invoke-static {v3, v0, v10}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerButtonSuppressionDelayMillis:I

    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const v10, 0x11102af

    invoke-virtual {v0, v10}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v0

    if-nez v0, :cond_2

    iput v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mRingerToggleChord:I

    :cond_2
    const/4 v0, 0x0

    iget-boolean v10, v1, Lcom/android/server/policy/PhoneWindowManager;->mWakeGestureEnabledSetting:Z

    if-eq v10, v0, :cond_3

    iput-boolean v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mWakeGestureEnabledSetting:Z

    invoke-direct {v1}, Lcom/android/server/policy/PhoneWindowManager;->updateWakeGestureListenerLp()V

    :cond_3
    const-string v10, "screen_off_timeout"

    invoke-static {v3, v10, v9, v8}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v10

    iput v10, v1, Lcom/android/server/policy/PhoneWindowManager;->mLockScreenTimeout:I

    const-string v10, "default_input_method"

    invoke-static {v3, v10, v8}, Landroid/provider/Settings$Secure;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v10

    if-eqz v10, :cond_4

    invoke-virtual {v10}, Ljava/lang/String;->length()I

    move-result v11

    if-lez v11, :cond_4

    move v11, v7

    goto :goto_3

    :cond_4
    move v11, v9

    :goto_3
    iget-boolean v12, v1, Lcom/android/server/policy/PhoneWindowManager;->mHasSoftInput:Z

    if-eq v12, v11, :cond_5

    iput-boolean v11, v1, Lcom/android/server/policy/PhoneWindowManager;->mHasSoftInput:Z

    const/4 v4, 0x1

    :cond_5
    const-string v12, "power_button_short_press"

    iget-object v13, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v13}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v13

    const v14, 0x10e014b

    invoke-virtual {v13, v14}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v13

    invoke-static {v3, v12, v13}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v12

    iput v12, v1, Lcom/android/server/policy/PhoneWindowManager;->mShortPressOnPowerBehavior:I

    const-string v12, "power_button_double_press"

    iget-object v13, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v13}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v13

    const v14, 0x10e008c

    invoke-virtual {v13, v14}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v13

    invoke-static {v3, v12, v13}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v12

    iput v12, v1, Lcom/android/server/policy/PhoneWindowManager;->mDoublePressOnPowerBehavior:I

    const-string v12, "power_button_triple_press"

    iget-object v13, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v13}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v13

    const v14, 0x10e0163

    invoke-virtual {v13, v14}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v13

    invoke-static {v3, v12, v13}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v12

    iput v12, v1, Lcom/android/server/policy/PhoneWindowManager;->mTriplePressOnPowerBehavior:I

    const-string v12, "power_button_long_press"

    iget-object v13, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v13}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v13

    const v14, 0x10e00c8

    invoke-virtual {v13, v14}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v13

    invoke-static {v3, v12, v13}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v12

    const-string v13, "power_button_very_long_press"

    iget-object v14, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v14}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v14

    const v15, 0x10e0169

    invoke-virtual {v14, v15}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v14

    invoke-static {v3, v13, v14}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v13

    iget v14, v1, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnPowerBehavior:I

    if-ne v14, v12, :cond_6

    iget v14, v1, Lcom/android/server/policy/PhoneWindowManager;->mVeryLongPressOnPowerBehavior:I

    if-eq v14, v13, :cond_7

    :cond_6
    iput v12, v1, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnPowerBehavior:I

    iput v13, v1, Lcom/android/server/policy/PhoneWindowManager;->mVeryLongPressOnPowerBehavior:I

    :cond_7
    iget-object v14, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v14}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v14

    const-string v15, "power_button_long_press_duration_ms"

    iget-object v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v9}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v9

    const v7, 0x10e00c9

    invoke-virtual {v9, v7}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v7

    int-to-long v8, v7

    invoke-static {v14, v15, v8, v9}, Landroid/provider/Settings$Global;->getLong(Landroid/content/ContentResolver;Ljava/lang/String;J)J

    move-result-wide v7

    iput-wide v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnPowerAssistantTimeoutMs:J

    const-string v7, "key_chord_power_volume_up"

    iget-object v8, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v8}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    const v9, 0x10e00b8

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v8

    invoke-static {v3, v7, v8}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v7

    iput v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mPowerVolUpBehavior:I

    const-string v7, "stem_primary_button_short_press"

    iget-object v8, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v8}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    const v9, 0x10e014d

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v8

    invoke-static {v3, v7, v8}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v7

    iput v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mShortPressOnStemPrimaryBehavior:I

    const-string v7, "stem_primary_button_double_press"

    iget-object v8, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v8}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    const v9, 0x10e008d

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v8

    invoke-static {v3, v7, v8}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v7

    iput v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mDoublePressOnStemPrimaryBehavior:I

    const-string v7, "stem_primary_button_triple_press"

    iget-object v8, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v8}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    const v9, 0x10e0164

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v8

    invoke-static {v3, v7, v8}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v7

    iput v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mTriplePressOnStemPrimaryBehavior:I

    const-string v7, "stem_primary_button_long_press"

    iget-object v8, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v8}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    const v9, 0x10e00ca

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v8

    invoke-static {v3, v7, v8}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v7

    iput v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mLongPressOnStemPrimaryBehavior:I

    iget-object v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v7}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v7

    const v8, 0x111023c

    invoke-virtual {v7, v8}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v7

    iput-boolean v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mShouldEarlyShortPressOnPower:Z

    iget-object v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    invoke-virtual {v7}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v7

    const v8, 0x111023d

    invoke-virtual {v7, v8}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v7

    iput-boolean v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mShouldEarlyShortPressOnStemPrimary:Z

    const-string v7, "stylus_buttons_enabled"

    const/4 v8, -0x2

    const/4 v9, 0x1

    invoke-static {v3, v7, v9, v8}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v7

    if-ne v7, v9, :cond_8

    const/4 v7, 0x1

    goto :goto_4

    :cond_8
    const/4 v7, 0x0

    :goto_4
    iput-boolean v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mStylusButtonsEnabled:Z

    iget-object v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mInputManagerInternal:Lcom/android/server/input/InputManagerInternal;

    iget-boolean v8, v1, Lcom/android/server/policy/PhoneWindowManager;->mStylusButtonsEnabled:Z

    invoke-virtual {v7, v8}, Lcom/android/server/input/InputManagerInternal;->setStylusButtonMotionEventsEnabled(Z)V

    const-string v7, "nav_bar_kids_mode"

    const/4 v8, -0x2

    const/4 v9, 0x0

    invoke-static {v3, v7, v9, v8}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v7

    const/4 v8, 0x1

    if-ne v7, v8, :cond_9

    const/4 v9, 0x1

    :cond_9
    iget-boolean v7, v1, Lcom/android/server/policy/PhoneWindowManager;->mKidsModeEnabled:Z

    if-eq v7, v9, :cond_a

    iput-boolean v9, v1, Lcom/android/server/policy/PhoneWindowManager;->mKidsModeEnabled:Z

    const/4 v5, 0x1

    :cond_a
    monitor-exit v6
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_5

    nop

    :goto_5
    if-nez v5, :cond_b

    goto :goto_13

    :cond_b
    goto :goto_12

    nop

    :goto_6
    move-object/from16 v1, p0

    goto :goto_19

    nop

    :goto_7
    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v3

    goto :goto_14

    nop

    :goto_8
    if-nez v4, :cond_c

    goto :goto_11

    :cond_c
    goto :goto_18

    nop

    :goto_9
    iget-object v6, v1, Lcom/android/server/policy/PhoneWindowManager;->mLock:Ljava/lang/Object;

    goto :goto_0

    nop

    :goto_a
    throw v0

    :goto_b
    new-instance v0, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda6;

    goto :goto_e

    nop

    :goto_c
    return-void

    :goto_d
    goto :goto_15

    nop

    :goto_e
    invoke-direct {v0, v1}, Lcom/android/server/policy/PhoneWindowManager$$ExternalSyntheticLambda6;-><init>(Lcom/android/server/policy/PhoneWindowManager;)V

    goto :goto_f

    nop

    :goto_f
    invoke-virtual {v2, v0}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    goto :goto_c

    nop

    :goto_10
    invoke-virtual {v1, v8}, Lcom/android/server/policy/PhoneWindowManager;->updateRotation(Z)V

    :goto_11
    goto :goto_16

    nop

    :goto_12
    invoke-direct {v1, v9}, Lcom/android/server/policy/PhoneWindowManager;->updateKidsModeSettings(Z)V

    :goto_13
    goto :goto_8

    nop

    :goto_14
    const/4 v4, 0x0

    goto :goto_17

    nop

    :goto_15
    iget-object v0, v1, Lcom/android/server/policy/PhoneWindowManager;->mContext:Landroid/content/Context;

    goto :goto_7

    nop

    :goto_16
    return-void

    :catchall_0
    move-exception v0

    :try_start_1
    monitor-exit v6
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_a

    nop

    :goto_17
    const/4 v5, 0x0

    goto :goto_9

    nop

    :goto_18
    const/4 v8, 0x1

    goto :goto_10

    nop

    :goto_19
    move-object/from16 v2, p1

    goto :goto_1a

    nop

    :goto_1a
    if-nez v2, :cond_d

    goto :goto_d

    :cond_d
    goto :goto_b

    nop
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_updateUiMode__V",
        "method":      ".method updateUiMode()V",
        "type":        "method_replace",
        "search": """\
.method updateUiMode()V
    .registers 2

    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiModeManager:Landroid/app/IUiModeManager;

    if-nez v0, :cond_0

    nop

    const-string v0, "uimode"

    invoke-static {v0}, Landroid/os/ServiceManager;->getService(Ljava/lang/String;)Landroid/os/IBinder;

    move-result-object v0

    invoke-static {v0}, Landroid/app/IUiModeManager$Stub;->asInterface(Landroid/os/IBinder;)Landroid/app/IUiModeManager;

    move-result-object v0

    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiModeManager:Landroid/app/IUiModeManager;

    :cond_0
    :try_start_0
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiModeManager:Landroid/app/IUiModeManager;

    invoke-interface {v0}, Landroid/app/IUiModeManager;->getCurrentModeType()I

    move-result v0

    iput v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiMode:I
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception v0

    :goto_0
    return-void
.end method
""",
        "replacement": """\
.method updateUiMode()V
    .registers 2

    goto :goto_8

    nop

    :goto_0
    const-string v0, "uimode"

    goto :goto_6

    nop

    :goto_1
    goto :goto_2

    :catch_0
    move-exception v0

    :goto_2
    goto :goto_9

    nop

    :goto_3
    iput-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiModeManager:Landroid/app/IUiModeManager;

    :goto_4
    :try_start_0
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiModeManager:Landroid/app/IUiModeManager;

    invoke-interface {v0}, Landroid/app/IUiModeManager;->getCurrentModeType()I

    move-result v0

    iput v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiMode:I
    :try_end_0
    .catch Landroid/os/RemoteException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_1

    nop

    :goto_5
    if-eqz v0, :cond_0

    goto :goto_4

    :cond_0
    nop

    goto :goto_0

    nop

    :goto_6
    invoke-static {v0}, Landroid/os/ServiceManager;->getService(Ljava/lang/String;)Landroid/os/IBinder;

    move-result-object v0

    goto :goto_7

    nop

    :goto_7
    invoke-static {v0}, Landroid/app/IUiModeManager$Stub;->asInterface(Landroid/os/IBinder;)Landroid/app/IUiModeManager;

    move-result-object v0

    goto :goto_3

    nop

    :goto_8
    iget-object v0, p0, Lcom/android/server/policy/PhoneWindowManager;->mUiModeManager:Landroid/app/IUiModeManager;

    goto :goto_5

    nop

    :goto_9
    return-void
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
]
