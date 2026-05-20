"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/sim/SimIconForVertical.smali'
CLASS_FALLBACK_NAMES = ['SimIconForVertical.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;
.super Lcom/android/systemui/newstatusbar/sim/SimIcon;


# instance fields
.field private final mDelegates:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/sim/SimIcon;",
            ">;"
        }
    .end annotation
.end field

.field private mIds:I


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/sim/SimIcon;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mIds:I

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mDelegates:Ljava/util/ArrayList;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/sim/SimIcon;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mIds:I

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mDelegates:Ljava/util/ArrayList;

    return-void
.end method


# virtual methods
.method public removeDelegate(Lcom/android/systemui/newstatusbar/sim/SimIcon;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mDelegates:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    return-void
.end method

.method public setDelegate(Lcom/android/systemui/newstatusbar/sim/SimIcon;)V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mDelegates:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->isFirstSlot:Z

    iput-boolean v0, p1, Lcom/android/systemui/newstatusbar/sim/SimIcon;->isFirstSlot:Z

    iget v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mIds:I

    if-lez v0, :cond_27

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mDelegates:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_13
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_27

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/sim/SimIcon;

    if-eqz v1, :cond_26

    iget v2, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mIds:I

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->setImageResource(I)V

    :cond_26
    goto :goto_13

    :cond_27
    invoke-virtual {p1}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->onIconChange()V

    return-void
.end method

.method public setImageResource(I)V
    .registers 4

    iput p1, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mIds:I

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->setImageResource(I)V

    if-eqz p1, :cond_27

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mDelegates:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    if-lez v0, :cond_27

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mDelegates:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_15
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_27

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/sim/SimIcon;

    if-eqz v1, :cond_26

    invoke-virtual {v1, p1}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->setImageResource(I)V

    :cond_26
    goto :goto_15

    :cond_27
    return-void
.end method

.method public setImageTintList(Landroid/content/res/ColorStateList;)V
    .registers 4

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->setImageTintList(Landroid/content/res/ColorStateList;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconForVertical;->mDelegates:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_9
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_1b

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/sim/SimIcon;

    if-eqz v1, :cond_1a

    invoke-virtual {v1, p1}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->setImageTintList(Landroid/content/res/ColorStateList;)V

    :cond_1a
    goto :goto_9

    :cond_1b
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_sim_SimIconForVertical',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
