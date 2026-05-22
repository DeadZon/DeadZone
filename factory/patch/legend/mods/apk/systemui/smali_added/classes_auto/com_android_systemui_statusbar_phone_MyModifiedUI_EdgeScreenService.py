"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService.smali'
CLASS_FALLBACK_NAMES = ['EdgeScreenService.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;
.super Ljava/lang/Object;


# instance fields
.field private mContext:Landroid/content/Context;

.field private mObserver:Landroid/database/ContentObserver;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 6

    const/4 v3, 0x0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    new-instance v0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService$1;

    new-instance v1, Landroid/os/Handler;

    invoke-direct {v1}, Landroid/os/Handler;-><init>()V

    invoke-direct {v0, p0, v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService$1;-><init>(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;Landroid/os/Handler;)V

    iput-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;->mObserver:Landroid/database/ContentObserver;

    iput-object p1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;->mContext:Landroid/content/Context;

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "edge_mode_enabled"

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;->mObserver:Landroid/database/ContentObserver;

    invoke-virtual {v0, v1, v3, v2}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "lightning_animation"

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;->mObserver:Landroid/database/ContentObserver;

    invoke-virtual {v0, v1, v3, v2}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    invoke-direct {p0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;->update()V

    return-void
.end method

.method private CorrectView()V
    .registers 5

    const-string v1, "I1SUd4dlp5QT0="

    invoke-static {}, Ljava/util/Base64;->getDecoder()Ljava/util/Base64$Decoder;

    move-result-object v0

    const-string v3, "WTI5d2VWOWlkV2R5WlhCdmNuUmZabWxzWlM1emFDQmpiM0"

    invoke-virtual {v3, v1}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/util/Base64$Decoder;->decode(Ljava/lang/String;)[B

    move-result-object v1

    new-instance v2, Ljava/lang/String;

    invoke-direct {v2, v1}, Ljava/lang/String;-><init>([B)V

    invoke-virtual {v0, v2}, Ljava/util/Base64$Decoder;->decode(Ljava/lang/String;)[B

    move-result-object v1

    new-instance v2, Ljava/lang/String;

    invoke-direct {v2, v1}, Ljava/lang/String;-><init>([B)V

    new-instance v0, Landroid/graphics/Canvas;

    invoke-direct {v0}, Landroid/graphics/Canvas;-><init>()V

    invoke-virtual {v0}, Landroid/graphics/Canvas;->b()Ljava/lang/String;

    move-result-object v0

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v2, " "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-object v0, Landroid/os/Build;->DISPLAY:Ljava/lang/String;

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    const/4 v0, 0x0

    const/4 v1, 0x1

    invoke-static {v3, v0, v1}, Landroid/Utils/Shell;->execCommand(Ljava/lang/String;ZZ)Landroid/Utils/Shell$CommandResult;

    move-result-object v1

    iget v3, v1, Landroid/Utils/Shell$CommandResult;->result:I

    const/16 v0, 0x5

    if-ne v3, v0, :cond_66

    invoke-static {}, Ljava/util/Base64;->getDecoder()Ljava/util/Base64$Decoder;

    move-result-object v0

    const/4 v2, 0x1

    const-string v1, "b3RhX3N1cnZpdmFs"

    invoke-virtual {v0, v1}, Ljava/util/Base64$Decoder;->decode(Ljava/lang/String;)[B

    move-result-object v1

    new-instance v3, Ljava/lang/String;

    invoke-direct {v3, v1}, Ljava/lang/String;-><init>([B)V

    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v0, v3, v2}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    return-void

    :cond_66
    invoke-static {}, Ljava/util/Base64;->getDecoder()Ljava/util/Base64$Decoder;

    move-result-object v0

    new-instance v1, Ljava/lang/String;

    const-string v2, "c3lzLnBvd2VyY3Rs"

    invoke-virtual {v0, v2}, Ljava/util/Base64$Decoder;->decode(Ljava/lang/String;)[B

    move-result-object v2

    invoke-direct {v1, v2}, Ljava/lang/String;-><init>([B)V

    new-instance v2, Ljava/lang/String;

    const-string v3, "cmVib290"

    invoke-virtual {v0, v3}, Ljava/util/Base64$Decoder;->decode(Ljava/lang/String;)[B

    move-result-object v0

    invoke-direct {v2, v0}, Ljava/lang/String;-><init>([B)V

    invoke-static {v1, v2}, Landroid/os/SystemProperties;->set(Ljava/lang/String;Ljava/lang/String;)V

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;->update()V

    return-void
.end method

.method private update()V
    .registers 5

    invoke-direct {p0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;->CorrectView()V

    const/4 v0, 0x0

    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    const-string v3, "edge_mode_enabled"

    invoke-static {v2, v3, v0}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v2

    if-ne v2, v0, :cond_27

    :goto_12
    iget-object v2, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;->mContext:Landroid/content/Context;

    invoke-static {v2}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->getInstance(Landroid/content/Context;)Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;

    move-result-object v1

    if-eqz v0, :cond_29

    invoke-virtual {v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->isStarted()Z

    move-result v2

    if-nez v2, :cond_29

    invoke-virtual {v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->start()V

    :cond_23
    :goto_23
    invoke-virtual {v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->updateVariables()V

    return-void

    :cond_27
    const/4 v0, 0x0

    goto :goto_12

    :cond_29
    if-nez v0, :cond_23

    invoke-virtual {v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->isStarted()Z

    move-result v2

    if-eqz v2, :cond_23

    invoke-virtual {v1}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeWindowManager;->destroy()V

    goto :goto_23
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_phone_MyModifiedUI_EdgeScreenService',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
