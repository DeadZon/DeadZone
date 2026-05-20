"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/justas/AnimationWeather/MoonAnimation$1.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/justas/AnimationWeather/MoonAnimation$1.smali'
CLASS_FALLBACK_NAMES = ['MoonAnimation$1.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_justas_AnimationWeather_MoonAnimation$1',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/justas/AnimationWeather/MoonAnimation$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/justas/AnimationWeather/MoonAnimation;->generateStars()V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/justas/AnimationWeather/MoonAnimation;\n\n\n# direct methods\n.method constructor <init>(Lcom/justas/AnimationWeather/MoonAnimation;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/justas/AnimationWeather/MoonAnimation$1;->this$0:Lcom/justas/AnimationWeather/MoonAnimation;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 2\n\n    iget-object v0, p0, Lcom/justas/AnimationWeather/MoonAnimation$1;->this$0:Lcom/justas/AnimationWeather/MoonAnimation;\n\n    invoke-static {v0}, Lcom/justas/AnimationWeather/MoonAnimation;->access$000(Lcom/justas/AnimationWeather/MoonAnimation;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
