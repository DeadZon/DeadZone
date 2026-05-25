"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer.smali'
CLASS_FALLBACK_NAMES = ['MiuiStatusIconContainer.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;
.super Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;

# interfaces
.implements Lcom/android/systemui/newstatusbar/policy/ISlots;


# instance fields
.field private ignored:Ljava/util/List;

.field private final movedView:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/policy/ISlots;",
            ">;"
        }
    .end annotation
.end field

.field private slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;-><init>(Landroid/content/Context;)V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->movedView:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    const-string v1, "network_speed"

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    const-string v1, "wifi"

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    const-string v1, "mobile"

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 5

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->movedView:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    const-string v1, "network_speed"

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    const-string v1, "wifi"

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    const-string v1, "mobile"

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 6

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->movedView:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    const-string v1, "network_speed"

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    const-string v1, "wifi"

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    const-string v1, "mobile"

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 7

    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->movedView:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    const-string v1, "network_speed"

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    const-string v1, "wifi"

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    const-string v1, "mobile"

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->movedView:Ljava/util/ArrayList;

    return-object v0
.end method

.method static synthetic access$100(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;)Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    return-object v0
.end method


# virtual methods
.method public addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V
    .registers 5

    if-eqz p3, :cond_5

    const/4 v0, -0x2

    iput v0, p3, Landroid/view/ViewGroup$LayoutParams;->height:I

    :cond_5
    invoke-super {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V

    return-void
.end method

.method public onViewAdded(Landroid/view/View;)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->onViewAdded(Landroid/view/View;)V

    new-instance v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$2;

    invoke-direct {v0, p0, p1}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$2;-><init>(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;Landroid/view/View;)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->post(Ljava/lang/Runnable;)Z

    return-void
.end method

.method public onViewRemoved(Landroid/view/View;)V
    .registers 4

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->onViewRemoved(Landroid/view/View;)V

    instance-of v0, p1, Lcom/android/systemui/newstatusbar/policy/ISlots;

    if-eqz v0, :cond_f

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->movedView:Ljava/util/ArrayList;

    move-object v1, p1

    check-cast v1, Lcom/android/systemui/newstatusbar/policy/ISlots;

    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    :cond_f
    return-void
.end method

.method public setIgnoredSlots(Ljava/util/List;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    invoke-interface {p1, v0}, Ljava/util/List;->addAll(Ljava/util/Collection;)Z

    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->setIgnoredSlots(Ljava/util/List;)V

    return-void
.end method

.method public setIsKeyguard()V
    .registers 2

    sget-object v0, Lcom/android/systemui/statusbar/phone/MiuiIconManagerUtils;->MINI_RIGHT_BLOCK_LIST:Ljava/util/ArrayList;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->addIgnoredSlots(Ljava/util/List;)V

    return-void
.end method

.method public setIslandController(Lcom/android/systemui/statusbar/StatusBarIslandControllerImpl;I)V
    .registers 4

    invoke-super {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;->setIslandController(Lcom/android/systemui/statusbar/StatusBarIslandControllerImpl;I)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/IslandController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/IslandController;

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->setController(Lcom/android/systemui/statusbar/StatusBarIslandControllerImpl;)V

    return-void
.end method

.method public setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V
    .registers 3

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->slot:Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;

    new-instance v0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;

    invoke-direct {v0, p0, p1}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer$1;-><init>(Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->post(Ljava/lang/Runnable;)Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->ignored:Ljava/util/List;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/MiuiStatusIconContainer;->addIgnoredSlots(Ljava/util/List;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_MiuiStatusIconContainer',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
