"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable.smali'
CLASS_FALLBACK_NAMES = ['IslandController$ErrorRunable.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_IslandControll',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/controllers/IslandController;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0xa\n    name = "ErrorRunable"\n.end annotation\n\n\n# instance fields\n.field private controller:Lcom/android/systemui/newstatusbar/controllers/IslandController;\n\n.field private final rect:Landroid/graphics/Rect;\n\n\n# direct methods\n.method public constructor <init>()V\n    .registers 2\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    new-instance v0, Landroid/graphics/Rect;\n\n    invoke-direct {v0}, Landroid/graphics/Rect;-><init>()V\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->rect:Landroid/graphics/Rect;\n\n    return-void\n.end method\n\n.method public constructor <init>(Landroid/graphics/Rect;Lcom/android/systemui/newstatusbar/controllers/IslandController;)V\n    .registers 4\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    new-instance v0, Landroid/graphics/Rect;\n\n    invoke-direct {v0}, Landroid/graphics/Rect;-><init>()V\n\n    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->rect:Landroid/graphics/Rect;\n\n    invoke-virtual {v0, p1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V\n\n    iput-object p2, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->controller:Lcom/android/systemui/newstatusbar/controllers/IslandController;\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->controller:Lcom/android/systemui/newstatusbar/controllers/IslandController;\n\n    if-eqz v0, :cond_0\n\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->rect:Landroid/graphics/Rect;\n\n    const/4 v2, 0x0\n\n    invoke-virtual {v0, v1, v2}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->onIslandSizeChanged(Landroid/graphics/Rect;Z)V\n\n    :cond_0\n    return-void\n.end method\n\n.method public setController(Lcom/android/systemui/newstatusbar/controllers/IslandController;)Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->controller:Lcom/android/systemui/newstatusbar/controllers/IslandController;\n\n    return-object p0\n.end method\n\n.method public setRect(Landroid/graphics/Rect;)Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/IslandController$ErrorRunable;->rect:Landroid/graphics/Rect;\n\n    invoke-virtual {v0, p1}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V\n\n    return-object p0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
