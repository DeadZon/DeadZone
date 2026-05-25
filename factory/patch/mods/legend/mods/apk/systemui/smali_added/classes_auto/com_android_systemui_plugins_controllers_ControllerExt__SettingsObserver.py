"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/plugins/controllers/ControllerExt$SettingsObserver.smali'
CLASS_FALLBACK_NAMES = ['ControllerExt$SettingsObserver.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/plugins/controllers/ControllerExt;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x9
    name = "SettingsObserver"
.end annotation

.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;,
        Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;,
        Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;,
        Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "<CE:",
        "Lcom/android/systemui/plugins/controllers/ControllerExt",
        "<+",
        "Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;",
        ">;>",
        "Ljava/lang/Object;"
    }
.end annotation


# instance fields
.field private final controllerExt:Lcom/android/systemui/plugins/controllers/ControllerExt;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "TCE;"
        }
    .end annotation
.end field

.field private final handler:Landroid/os/Handler;

.field private final keys:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;",
            ">;"
        }
    .end annotation
.end field

.field private listener:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;

.field private final observer:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver",
            "<TCE;>.Observer;"
        }
    .end annotation
.end field

.field private final type:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;


# direct methods
.method public constructor <init>(Lcom/android/systemui/plugins/controllers/ControllerExt;)V
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(TCE;)V"
        }
    .end annotation

    sget-object v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->System:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;)V

    return-void
.end method

.method public constructor <init>(Lcom/android/systemui/plugins/controllers/ControllerExt;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;)V
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(TCE;",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;",
            ")V"
        }
    .end annotation

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->keys:Ljava/util/ArrayList;

    new-instance v0, Landroid/os/Handler;

    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;

    move-result-object v1

    invoke-direct {v0, v1}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V

    iput-object v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->handler:Landroid/os/Handler;

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;

    invoke-direct {v0, p0, p0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;)V

    iput-object v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->observer:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;

    iput-object p1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->controllerExt:Lcom/android/systemui/plugins/controllers/ControllerExt;

    iput-object p2, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->type:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    return-void
.end method

.method public constructor <init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;)V
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(TCE;[",
            "Ljava/lang/String;",
            ")V"
        }
    .end annotation

    sget-object v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->System:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;)V

    invoke-virtual {p0, p2}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->addKeys([Ljava/lang/String;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    return-void
.end method

.method public constructor <init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;)V
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(TCE;[",
            "Ljava/lang/String;",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;",
            ")V"
        }
    .end annotation

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, p3, v0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;)V

    return-void
.end method

.method public constructor <init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;)V
    .registers 6
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(TCE;[",
            "Ljava/lang/String;",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;",
            ")V"
        }
    .end annotation

    invoke-direct {p0, p1, p3}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;)V

    invoke-virtual {p0, p4}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->addListener(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    move-result-object v0

    invoke-virtual {v0, p2}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->addKeys([Ljava/lang/String;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    return-void
.end method

.method public constructor <init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;)V
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(TCE;[",
            "Ljava/lang/String;",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;",
            ")V"
        }
    .end annotation

    sget-object v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->System:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;)V

    invoke-virtual {p0, p3}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->addListener(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    move-result-object v0

    invoke-virtual {v0, p2}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->addKeys([Ljava/lang/String;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;)Landroid/os/Handler;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->handler:Landroid/os/Handler;

    return-object v0
.end method

.method static synthetic access$100(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;)Lcom/android/systemui/plugins/controllers/ControllerExt;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->controllerExt:Lcom/android/systemui/plugins/controllers/ControllerExt;

    return-object v0
.end method

.method static synthetic access$200(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->listener:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;

    return-object v0
.end method


# virtual methods
.method public varargs addKeys([Ljava/lang/String;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;
    .registers 7
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "([",
            "Ljava/lang/String;",
            ")",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver",
            "<TCE;>;"
        }
    .end annotation

    array-length v2, p1

    const/4 v1, 0x0

    :goto_2
    if-ge v1, v2, :cond_13

    aget-object v0, p1, v1

    iget-object v3, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->keys:Ljava/util/ArrayList;

    new-instance v4, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;

    invoke-direct {v4, v0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;-><init>(Ljava/lang/String;)V

    invoke-virtual {v3, v4}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    add-int/lit8 v1, v1, 0x1

    goto :goto_2

    :cond_13
    invoke-virtual {p0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->register()V

    return-object p0
.end method

.method public addListener(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;
    .registers 2
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;",
            ")",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver",
            "<TCE;>;"
        }
    .end annotation

    iput-object p1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->listener:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;

    return-object p0
.end method

.method public addUri(Landroid/net/Uri;)Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/net/Uri;",
            ")",
            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver",
            "<TCE;>;"
        }
    .end annotation

    iget-object v1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->controllerExt:Lcom/android/systemui/plugins/controllers/ControllerExt;

    iget-object v1, v1, Lcom/android/systemui/plugins/controllers/ControllerExt;->context:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const/4 v1, 0x0

    iget-object v2, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->observer:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;

    invoke-virtual {v0, p1, v1, v2}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    return-object p0
.end method

.method register()V
    .registers 7

    goto/32 :goto_37

    nop

    :goto_4
    iget-object v2, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->keys:Ljava/util/ArrayList;

    goto/32 :goto_10

    nop

    :goto_a
    iget-object v2, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->keys:Ljava/util/ArrayList;

    goto/32 :goto_f9

    nop

    :goto_10
    invoke-virtual {v2}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_14
    goto/32 :goto_5f

    nop

    :goto_18
    iget-boolean v3, v1, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;->isRegister:Z

    goto/32 :goto_43

    nop

    :goto_1e
    if-nez v3, :cond_23

    goto/32 :goto_33

    :cond_23
    goto/32 :goto_144

    nop

    :goto_27
    iget-object v3, v1, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;->key:Ljava/lang/String;

    goto/32 :goto_7d

    nop

    :goto_2d
    goto :goto_14

    :goto_2e
    goto/32 :goto_70

    nop

    :goto_32
    goto :goto_97

    :goto_33
    goto/32 :goto_6f

    nop

    :goto_37
    const/4 v5, 0x0

    goto/32 :goto_a1

    nop

    :goto_3c
    invoke-virtual {v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;->register()V

    goto/32 :goto_32

    nop

    :goto_43
    if-eqz v3, :cond_48

    goto/32 :goto_14

    :cond_48
    goto/32 :goto_12b

    nop

    :goto_4c
    invoke-virtual {v0, v3, v5, v4}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_d6

    nop

    :goto_53
    iget-object v2, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->type:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    goto/32 :goto_85

    nop

    :goto_59
    goto/16 :goto_fd

    :goto_5b
    goto/32 :goto_9b

    nop

    :goto_5f
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    goto/32 :goto_1e

    nop

    :goto_67
    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto/32 :goto_158

    nop

    :goto_6f
    return-void

    :goto_70
    iget-object v2, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->type:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    goto/32 :goto_e4

    nop

    :goto_76
    invoke-virtual {v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;->register()V

    goto/32 :goto_59

    nop

    :goto_7d
    invoke-static {v3}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v3

    goto/32 :goto_ad

    nop

    :goto_85
    sget-object v3, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->System:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    goto/32 :goto_f0

    nop

    :goto_8b
    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto/32 :goto_14c

    nop

    :goto_93
    invoke-virtual {v2}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_97
    goto/32 :goto_11b

    nop

    :goto_9b
    iget-object v2, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->keys:Ljava/util/ArrayList;

    goto/32 :goto_93

    nop

    :goto_a1
    iget-object v2, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->controllerExt:Lcom/android/systemui/plugins/controllers/ControllerExt;

    goto/32 :goto_ea

    nop

    :goto_a7
    iget-object v4, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->observer:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;

    goto/32 :goto_137

    nop

    :goto_ad
    iget-object v4, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->observer:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;

    goto/32 :goto_dd

    nop

    :goto_b3
    if-eqz v3, :cond_b8

    goto/32 :goto_97

    :cond_b8
    goto/32 :goto_15e

    nop

    :goto_bc
    invoke-static {v3}, Landroid/provider/Settings$Global;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v3

    goto/32 :goto_a7

    nop

    :goto_c4
    if-eq v2, v3, :cond_c9

    goto/32 :goto_5b

    :cond_c9
    goto/32 :goto_a

    nop

    :goto_cd
    if-eqz v3, :cond_d2

    goto/32 :goto_fd

    :cond_d2
    goto/32 :goto_27

    nop

    :goto_d6
    invoke-virtual {v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;->register()V

    goto/32 :goto_2d

    nop

    :goto_dd
    invoke-virtual {v0, v3, v5, v4}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_76

    nop

    :goto_e4
    sget-object v3, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;->Secure:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$SettingsType;

    goto/32 :goto_c4

    nop

    :goto_ea
    iget-object v2, v2, Lcom/android/systemui/plugins/controllers/ControllerExt;->context:Landroid/content/Context;

    goto/32 :goto_164

    nop

    :goto_f0
    if-eq v2, v3, :cond_f5

    goto/32 :goto_2e

    :cond_f5
    goto/32 :goto_4

    nop

    :goto_f9
    invoke-virtual {v2}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_fd
    goto/32 :goto_101

    nop

    :goto_101
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    goto/32 :goto_109

    nop

    :goto_109
    if-nez v3, :cond_10e

    goto/32 :goto_33

    :cond_10e
    goto/32 :goto_8b

    nop

    :goto_112
    if-nez v3, :cond_117

    goto/32 :goto_33

    :cond_117
    goto/32 :goto_67

    nop

    :goto_11b
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    goto/32 :goto_112

    nop

    :goto_123
    invoke-static {v3}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v3

    goto/32 :goto_152

    nop

    :goto_12b
    iget-object v3, v1, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;->key:Ljava/lang/String;

    goto/32 :goto_123

    nop

    :goto_131
    iget-boolean v3, v1, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;->isRegister:Z

    goto/32 :goto_b3

    nop

    :goto_137
    invoke-virtual {v0, v3, v5, v4}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    goto/32 :goto_3c

    nop

    :goto_13e
    check-cast v1, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;

    goto/32 :goto_18

    nop

    :goto_144
    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto/32 :goto_13e

    nop

    :goto_14c
    check-cast v1, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;

    goto/32 :goto_16c

    nop

    :goto_152
    iget-object v4, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;->observer:Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$Observer;

    goto/32 :goto_4c

    nop

    :goto_158
    check-cast v1, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;

    goto/32 :goto_131

    nop

    :goto_15e
    iget-object v3, v1, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;->key:Ljava/lang/String;

    goto/32 :goto_bc

    nop

    :goto_164
    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    goto/32 :goto_53

    nop

    :goto_16c
    iget-boolean v3, v1, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;->isRegister:Z

    goto/32 :goto_cd

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_plugins_controllers_ControllerExt_SettingsObserver',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
