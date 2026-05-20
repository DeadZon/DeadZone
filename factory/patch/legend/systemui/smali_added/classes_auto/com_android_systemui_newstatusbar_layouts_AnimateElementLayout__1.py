"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/AnimateElementLayout$1.smali'
CLASS_FALLBACK_NAMES = ['AnimateElementLayout$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$1;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/animation/Animator$AnimatorListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->getAllAnim()Landroid/animation/ObjectAnimator;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onAnimationCancel(Landroid/animation/Animator;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->access$500(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)V

    return-void
.end method

.method public onAnimationEnd(Landroid/animation/Animator;)V
    .registers 6

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->access$000(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)Ljava/lang/Runnable;

    move-result-object v1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->removeCallbacks(Ljava/lang/Runnable;)Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->access$100(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)Z

    move-result v0

    if-eqz v0, :cond_32

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->access$200(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)Landroid/animation/ObjectAnimator;

    move-result-object v0

    if-eqz v0, :cond_32

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->access$300(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)I

    move-result v0

    const/4 v1, 0x1

    if-ne v0, v1, :cond_32

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->access$000(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)Ljava/lang/Runnable;

    move-result-object v1

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;

    invoke-static {v2}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->access$400(Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;)I

    move-result v2

    int-to-long v2, v2

    invoke-virtual {v0, v1, v2, v3}, Lcom/android/systemui/newstatusbar/layouts/AnimateElementLayout;->postDelayed(Ljava/lang/Runnable;J)Z

    :cond_32
    return-void
.end method

.method public onAnimationRepeat(Landroid/animation/Animator;)V
    .registers 2

    return-void
.end method

.method public onAnimationStart(Landroid/animation/Animator;)V
    .registers 2

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_AnimateElementLayout_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
