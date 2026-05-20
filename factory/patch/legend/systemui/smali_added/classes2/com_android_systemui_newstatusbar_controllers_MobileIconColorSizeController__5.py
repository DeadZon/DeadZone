"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$5.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$5.smali'
CLASS_FALLBACK_NAMES = ['MobileIconColorSizeController$5.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_MobileIconColo',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$5;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;-><init>(Landroid/content/Context;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$5;->this$0:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onDataChanged()V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController$5;->this$0:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;\n\n    invoke-static {v0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->access$500(Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;)Ljava/util/ArrayList;\n\n    move-result-object v1\n\n    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
