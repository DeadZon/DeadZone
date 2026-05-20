"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/justas/AnimationWeather/Weather$QueryHandler.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/justas/AnimationWeather/Weather$QueryHandler.smali'
CLASS_FALLBACK_NAMES = ['Weather$QueryHandler.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_justas_AnimationWeather_Weather$QueryHandler',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/justas/AnimationWeather/Weather$QueryHandler;\n.super Landroid/content/AsyncQueryHandler;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/justas/AnimationWeather/Weather;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x8\n    name = "QueryHandler"\n.end annotation\n\n\n# instance fields\n.field private mWeather:Lcom/justas/AnimationWeather/Weather;\n\n\n# direct methods\n.method private constructor <init>(Landroid/content/ContentResolver;)V\n    .registers 2\n\n    invoke-direct {p0, p1}, Landroid/content/AsyncQueryHandler;-><init>(Landroid/content/ContentResolver;)V\n\n    return-void\n.end method\n\n.method synthetic constructor <init>(Landroid/content/ContentResolver;Lcom/justas/AnimationWeather/Weather$1;)V\n    .registers 3\n\n    invoke-direct {p0, p1}, Lcom/justas/AnimationWeather/Weather$QueryHandler;-><init>(Landroid/content/ContentResolver;)V\n\n    return-void\n.end method\n\n.method static synthetic access$102(Lcom/justas/AnimationWeather/Weather$QueryHandler;Lcom/justas/AnimationWeather/Weather;)Lcom/justas/AnimationWeather/Weather;\n    .registers 2\n\n    iput-object p1, p0, Lcom/justas/AnimationWeather/Weather$QueryHandler;->mWeather:Lcom/justas/AnimationWeather/Weather;\n\n    return-object p1\n.end method\n\n\n# virtual methods\n.method protected onQueryComplete(ILjava/lang/Object;Landroid/database/Cursor;)V\n    .registers 5\n\n    goto :goto_0\n\n    nop\n\n    :goto_0\n    invoke-super {p0, p1, p2, p3}, Landroid/content/AsyncQueryHandler;->onQueryComplete(ILjava/lang/Object;Landroid/database/Cursor;)V\n\n    goto :goto_3\n\n    nop\n\n    :goto_1\n    return-void\n\n    :goto_2\n    invoke-static {v0, p3}, Lcom/justas/AnimationWeather/Weather;->access$300(Lcom/justas/AnimationWeather/Weather;Landroid/database/Cursor;)V\n\n    goto :goto_1\n\n    nop\n\n    :goto_3\n    iget-object v0, p0, Lcom/justas/AnimationWeather/Weather$QueryHandler;->mWeather:Lcom/justas/AnimationWeather/Weather;\n\n    goto :goto_2\n\n    nop\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
