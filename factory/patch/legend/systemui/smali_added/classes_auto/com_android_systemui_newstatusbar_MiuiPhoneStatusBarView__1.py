"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1.smali'
CLASS_FALLBACK_NAMES = ['MiuiPhoneStatusBarView$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->refreshStatusBarHeight(Z)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;

.field final synthetic val$configuration:Landroid/content/res/Configuration;

.field final synthetic val$controller:Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;

.field final synthetic val$isCloseSettings:Z

.field final synthetic val$mConfigurationController:Lcom/android/systemui/statusbar/phone/ConfigurationControllerImpl;

.field final synthetic val$orient:I

.field final synthetic val$view:Landroid/view/View;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;Landroid/view/View;Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;ZLcom/android/systemui/statusbar/phone/ConfigurationControllerImpl;Landroid/content/res/Configuration;I)V
    .registers 8

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->this$0:Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;

    iput-object p2, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$view:Landroid/view/View;

    iput-object p3, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$controller:Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;

    iput-boolean p4, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$isCloseSettings:Z

    iput-object p5, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$mConfigurationController:Lcom/android/systemui/statusbar/phone/ConfigurationControllerImpl;

    iput-object p6, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$configuration:Landroid/content/res/Configuration;

    iput p7, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$orient:I

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$view:Landroid/view/View;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/view/View;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$view:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->requestApplyInsets()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$controller:Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;

    iget-object v0, v0, Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;->mWindowManager:Landroid/view/WindowManager;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$view:Landroid/view/View;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$controller:Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;

    iget-object v2, v2, Lcom/android/systemui/statusbar/window/StatusBarWindowControllerImpl;->mLp:Landroid/view/WindowManager$LayoutParams;

    invoke-interface {v0, v1, v2}, Landroid/view/WindowManager;->updateViewLayout(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->this$0:Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->access$000(Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;)Landroid/view/View;

    move-result-object v0

    if-eqz v0, :cond_4e

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->this$0:Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->access$000(Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;)Landroid/view/View;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->this$0:Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;

    invoke-static {v1}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->access$000(Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;)Landroid/view/View;

    move-result-object v1

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredWidth()I

    move-result v1

    const/high16 v2, 0x40000000  # 2.0f

    invoke-static {v1, v2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v1

    iget-boolean v3, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$isCloseSettings:Z

    if-eqz v3, :cond_45

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->this$0:Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;

    invoke-virtual {v3}, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView;->getContext()Landroid/content/Context;

    move-result-object v3

    invoke-static {v3}, Lcom/android/internal/policy/SystemBarUtils;->getStatusBarHeight(Landroid/content/Context;)I

    move-result v3

    goto :goto_47

    :cond_45
    const/16 v3, 0xfa

    :goto_47
    invoke-static {v3, v2}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    invoke-virtual {v0, v1, v2}, Landroid/view/View;->measure(II)V

    :cond_4e
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$mConfigurationController:Lcom/android/systemui/statusbar/phone/ConfigurationControllerImpl;

    if-eqz v0, :cond_5f

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$configuration:Landroid/content/res/Configuration;

    iget v1, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$orient:I

    iput v1, v0, Landroid/content/res/Configuration;->orientation:I

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$mConfigurationController:Lcom/android/systemui/statusbar/phone/ConfigurationControllerImpl;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/MiuiPhoneStatusBarView$1;->val$configuration:Landroid/content/res/Configuration;

    invoke-virtual {v0, v1}, Lcom/android/systemui/statusbar/phone/ConfigurationControllerImpl;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    :cond_5f
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_MiuiPhoneStatusBarView_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
