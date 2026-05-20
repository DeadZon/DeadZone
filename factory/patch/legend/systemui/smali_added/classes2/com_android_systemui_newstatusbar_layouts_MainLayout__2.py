"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/layouts/MainLayout$2.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/layouts/MainLayout$2.smali'
CLASS_FALLBACK_NAMES = ['MainLayout$2.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_layouts_MainLayout$2',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/layouts/MainLayout$2;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/util/Comparator;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/layouts/MainLayout;->arrangeByPlaces()V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n.annotation system Ldalvik/annotation/Signature;\n    value = {\n        "Ljava/lang/Object;",\n        "Ljava/util/Comparator",\n        "<",\n        "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",\n        ">;"\n    }\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$2;->this$0:Lcom/android/systemui/newstatusbar/layouts/MainLayout;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public compare(Lcom/android/systemui/newstatusbar/layouts/SingleLayout;Lcom/android/systemui/newstatusbar/layouts/SingleLayout;)I\n    .registers 5\n\n    invoke-virtual {p1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I\n\n    move-result v0\n\n    invoke-virtual {p2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I\n\n    move-result v1\n\n    invoke-static {v0, v1}, Ljava/lang/Integer;->compare(II)I\n\n    move-result v0\n\n    return v0\n.end method\n\n.method public bridge synthetic compare(Ljava/lang/Object;Ljava/lang/Object;)I\n    .registers 4\n\n    check-cast p1, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;\n\n    check-cast p2, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;\n\n    invoke-virtual {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$2;->compare(Lcom/android/systemui/newstatusbar/layouts/SingleLayout;Lcom/android/systemui/newstatusbar/layouts/SingleLayout;)I\n\n    move-result v0\n\n    return v0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
