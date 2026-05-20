"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/UpdateLayoutController$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/UpdateLayoutController$1.smali'
CLASS_FALLBACK_NAMES = ['UpdateLayoutController$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_UpdateLayoutCo',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Landroid/view/View$OnLayoutChangeListener;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onLayoutChange(Landroid/view/View;IIIIIIII)V\n    .registers 20\n\n    move-object v0, p0\n\n    iget-object v1, v0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;\n\n    move v2, p2\n\n    move v3, p3\n\n    move v4, p4\n\n    move v5, p5\n\n    move/from16 v6, p6\n\n    move/from16 v7, p7\n\n    move/from16 v8, p8\n\n    move/from16 v9, p9\n\n    invoke-virtual/range {v1 .. v9}, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->isChange(IIIIIIII)Z\n\n    move-result v1\n\n    new-instance v2, Ljava/lang/StringBuilder;\n\n    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V\n\n    const-string v3, "onLayoutChange: "\n\n    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v2\n\n    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;\n\n    move-result-object v3\n\n    invoke-virtual {v3}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;\n\n    move-result-object v3\n\n    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v2\n\n    const-string v3, "  isChanged = "\n\n    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v2\n\n    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;\n\n    move-result-object v2\n\n    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;\n\n    move-result-object v2\n\n    const-string v3, "Nastya_super_girl"\n\n    invoke-static {v3, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I\n\n    if-eqz v1, :cond_0\n\n    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$1;->this$0:Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;\n\n    invoke-static {v2}, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->access$000(Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;)Lcom/android/systemui/newstatusbar/controllers/ElementController;\n\n    move-result-object v2\n\n    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->updateMainLayouts()V\n\n    :cond_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
