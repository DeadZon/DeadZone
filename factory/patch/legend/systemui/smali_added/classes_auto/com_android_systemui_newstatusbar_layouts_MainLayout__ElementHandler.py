"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler.smali'
CLASS_FALLBACK_NAMES = ['MainLayout$ElementHandler.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;
.super Landroid/os/Handler;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/layouts/MainLayout;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0xa
    name = "ElementHandler"
.end annotation


# instance fields
.field private final mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;


# direct methods
.method public constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 3

    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;

    move-result-object v0

    invoke-direct {p0, v0}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    return-void
.end method


# virtual methods
.method public handleMessage(Landroid/os/Message;)V
    .registers 4

    iget v0, p1, Landroid/os/Message;->what:I

    packed-switch v0, :pswitch_data_4c

    :goto_5
    :pswitch_5  #0x1fa
    return-void

    :pswitch_6  #0x1f4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->access$000(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    goto :goto_5

    :pswitch_c  #0x1f5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->access$100(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    goto :goto_5

    :pswitch_12  #0x1f6
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->arrangeByPlaces()V

    goto :goto_5

    :pswitch_18  #0x1f7
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->fullUpdate()V

    goto :goto_5

    :pswitch_1e  #0x1f8
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->access$200(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    goto :goto_5

    :pswitch_24  #0x1f9
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->access$300(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    goto :goto_5

    :pswitch_2a  #0x1fd
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->access$400(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    goto :goto_5

    :pswitch_30  #0x1fc
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-static {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->access$500(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    goto :goto_5

    :pswitch_36  #0x1fe
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->findNotificationShade()V

    goto :goto_5

    :pswitch_3c  #0x1ff
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    iget-object v0, p1, Landroid/os/Message;->obj:Ljava/lang/Object;

    check-cast v0, Landroid/view/View;

    invoke-virtual {v1, v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->startMove(Landroid/view/View;)V

    goto :goto_5

    :pswitch_46  #0x1fb
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$ElementHandler;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->updateStatusIcons()V

    goto :goto_5

    :pswitch_data_4c
    .packed-switch 0x1f4
        :pswitch_6  #000001f4
        :pswitch_c  #000001f5
        :pswitch_12  #000001f6
        :pswitch_18  #000001f7
        :pswitch_1e  #000001f8
        :pswitch_24  #000001f9
        :pswitch_5  #000001fa
        :pswitch_46  #000001fb
        :pswitch_30  #000001fc
        :pswitch_2a  #000001fd
        :pswitch_36  #000001fe
        :pswitch_3c  #000001ff
    .end packed-switch
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_MainLayout_ElementHandler',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
