"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1$1.smali'
CLASS_FALLBACK_NAMES = ['BatteryMeterIconViewMinit$1$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_battery_BatteryMeterIconVi',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1$1;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Ljava/lang/Runnable;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;->run()V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$1:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;\n\n.field final synthetic val$drawable:Landroid/graphics/drawable/Drawable;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;Landroid/graphics/drawable/Drawable;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1$1;->this$1:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;\n\n    iput-object p2, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1$1;->val$drawable:Landroid/graphics/drawable/Drawable;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public run()V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1$1;->this$1:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;\n\n    iget-object v0, v0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;->this$0:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;\n\n    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1$1;->val$drawable:Landroid/graphics/drawable/Drawable;\n\n    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->superSetImageDrawable(Landroid/graphics/drawable/Drawable;)V\n\n    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1$1;->val$drawable:Landroid/graphics/drawable/Drawable;\n\n    instance-of v1, v0, Landroid/graphics/drawable/AnimationDrawable;\n\n    if-eqz v1, :cond_0\n\n    check-cast v0, Landroid/graphics/drawable/AnimationDrawable;\n\n    invoke-virtual {v0}, Landroid/graphics/drawable/AnimationDrawable;->start()V\n\n    :cond_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
