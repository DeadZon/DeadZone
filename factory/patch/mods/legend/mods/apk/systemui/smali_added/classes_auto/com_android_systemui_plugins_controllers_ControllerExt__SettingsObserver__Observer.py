"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer.smali'
CLASS_FALLBACK_NAMES = ['ControllerExt$SettingsObserver$Observer.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;
.super Landroid/database/ContentObserver;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x2
    name = "Observer"
.end annotation


# instance fields
.field private final settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver",
            "<TCE;>;"
        }
    .end annotation
.end field

.field final synthetic this$0:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;


# direct methods
.method public constructor <init>(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;)V
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver",
            "<TCE;>;)V"
        }
    .end annotation

    iput-object p1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;->this$0:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-static {p2}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->access$000(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;)Landroid/os/Handler;

    move-result-object v0

    invoke-direct {p0, v0}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V

    iput-object p2, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;->settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    return-void
.end method


# virtual methods
.method public onChange(ZLandroid/net/Uri;)V
    .registers 7
    .param p2  # Landroid/net/Uri;
        .annotation build Landroidx/annotation/Nullable;
        .end annotation
    .end param

    iget-object v1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;->settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-static {v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->access$100(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;)Lcom/android/systemui/plugins/controllers/ControllerExt;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/systemui/plugins/controllers/ControllerExt;->onSettingsChange()V

    if-eqz p2, :cond_47

    iget-object v1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;->settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-static {v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->access$100(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;)Lcom/android/systemui/plugins/controllers/ControllerExt;

    move-result-object v1

    invoke-virtual {v1, p2}, Lcom/android/systemui/plugins/controllers/ControllerExt;->onSettingsChange(Landroid/net/Uri;)V

    invoke-virtual {p2}, Landroid/net/Uri;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v2, "content://settings/system/"

    const-string v3, ""

    invoke-virtual {v1, v2, v3}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;->settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-static {v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->access$100(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;)Lcom/android/systemui/plugins/controllers/ControllerExt;

    move-result-object v1

    invoke-virtual {v1, v0}, Lcom/android/systemui/plugins/controllers/ControllerExt;->onSettingsChange(Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;->this$0:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-static {v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->access$200(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;

    move-result-object v1

    if-eqz v1, :cond_47

    iget-object v1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;->this$0:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-static {v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->access$200(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;

    move-result-object v1

    iget-object v2, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;->settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-interface {v1, v2, v0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;->onChange(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;->this$0:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-static {v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->access$200(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;

    move-result-object v1

    iget-object v2, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;->settingsObserver:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    invoke-interface {v1, v2, p2}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;->onChange(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;Landroid/net/Uri;)V

    :cond_47
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_plugins_controllers_ControllerExt_SettingsObserver_Observer',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
