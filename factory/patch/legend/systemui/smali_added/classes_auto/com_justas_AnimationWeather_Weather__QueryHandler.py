"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/justas/AnimationWeather/Weather$QueryHandler.smali'
CLASS_FALLBACK_NAMES = ['Weather$QueryHandler.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/justas/AnimationWeather/Weather$QueryHandler;
.super Landroid/content/AsyncQueryHandler;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/justas/AnimationWeather/Weather;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x8
    name = "QueryHandler"
.end annotation


# instance fields
.field private mWeather:Lcom/justas/AnimationWeather/Weather;


# direct methods
.method private constructor <init>(Landroid/content/ContentResolver;)V
    .registers 2

    invoke-direct {p0, p1}, Landroid/content/AsyncQueryHandler;-><init>(Landroid/content/ContentResolver;)V

    return-void
.end method

.method synthetic constructor <init>(Landroid/content/ContentResolver;Lcom/justas/AnimationWeather/Weather$1;)V
    .registers 3

    invoke-direct {p0, p1}, Lcom/justas/AnimationWeather/Weather$QueryHandler;-><init>(Landroid/content/ContentResolver;)V

    return-void
.end method

.method static synthetic access$102(Lcom/justas/AnimationWeather/Weather$QueryHandler;Lcom/justas/AnimationWeather/Weather;)Lcom/justas/AnimationWeather/Weather;
    .registers 2

    iput-object p1, p0, Lcom/justas/AnimationWeather/Weather$QueryHandler;->mWeather:Lcom/justas/AnimationWeather/Weather;

    return-object p1
.end method


# virtual methods
.method protected onQueryComplete(ILjava/lang/Object;Landroid/database/Cursor;)V
    .registers 5

    goto/32 :goto_4

    nop

    :goto_4
    invoke-super {p0, p1, p2, p3}, Landroid/content/AsyncQueryHandler;->onQueryComplete(ILjava/lang/Object;Landroid/database/Cursor;)V

    goto/32 :goto_13

    nop

    :goto_b
    return-void

    :goto_c
    invoke-static {v0, p3}, Lcom/justas/AnimationWeather/Weather;->access$300(Lcom/justas/AnimationWeather/Weather;Landroid/database/Cursor;)V

    goto/32 :goto_b

    nop

    :goto_13
    iget-object v0, p0, Lcom/justas/AnimationWeather/Weather$QueryHandler;->mWeather:Lcom/justas/AnimationWeather/Weather;

    goto/32 :goto_c

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_justas_AnimationWeather_Weather_QueryHandler',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
