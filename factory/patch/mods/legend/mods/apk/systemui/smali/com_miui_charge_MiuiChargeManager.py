"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/charge/MiuiChargeManager.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/charge/MiuiChargeManager.smali'
CLASS_FALLBACK_NAMES = ['MiuiChargeManager.smali']
CLASS_ANCHORS        = ['invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;', 'iget-object v0, p0, Lcom/miui/charge/MiuiChargeManager;->mBatteryStatus:Lcom/miui/systemui/charge/BatteryStatus;', 'iget v1, v0, Lcom/miui/systemui/charge/BatteryStatus;->wireState:I', 'invoke-static {v1, p1}, Lcom/miui/charge/ChargeUtils;->getChargeSpeed(II)I', 'iput v1, v0, Lcom/miui/systemui/charge/BatteryStatus;->chargeSpeed:I']

PATCHES = [
    {
        'id':             'p0000_dump',
        'type':           'method_replace',
        'method':         '.method public final dump(Ljava/io/PrintWriter;[Ljava/lang/String;)V',
        'method_name':    'dump',
        'method_anchors': ['invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V', 'invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->print(Ljava/lang/String;)V', 'invoke-static {}, Lcom/miui/charge/ChargeUtils;->isChargeAnimationDisabled()Z'],
        'search':         '.method public final dump(Ljava/io/PrintWriter;[Ljava/lang/String;)V\n    .registers 3\n\n    const-string p2, "MiuiChargeManager state:"\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V\n\n    const-string p2, "  isChargeAnimationDisabled ="\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->print(Ljava/lang/String;)V\n\n    sget-boolean p2, Lcom/miui/charge/ChargeUtils;->sChargeAnimationDisabled:Z\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->println(Z)V\n\n    const-string p2, "  mLevel ="\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->print(Ljava/lang/String;)V\n\n    iget-object p2, p0, Lcom/miui/charge/MiuiChargeManager;->mBatteryStatus:Lcom/miui/systemui/charge/BatteryStatus;\n\n    iget p2, p2, Lcom/miui/systemui/charge/BatteryStatus;->level:I\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->println(I)V\n\n    const-string p2, "  mWireState ="\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->print(Ljava/lang/String;)V\n\n    iget-object p2, p0, Lcom/miui/charge/MiuiChargeManager;->mBatteryStatus:Lcom/miui/systemui/charge/BatteryStatus;\n\n    iget p2, p2, Lcom/miui/systemui/charge/BatteryStatus;->wireState:I\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->println(I)V\n\n    const-string p2, "  mChargeSpeed ="\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->print(Ljava/lang/String;)V\n\n    iget-object p0, p0, Lcom/miui/charge/MiuiChargeManager;->mBatteryStatus:Lcom/miui/systemui/charge/BatteryStatus;\n\n    iget p0, p0, Lcom/miui/systemui/charge/BatteryStatus;->chargeSpeed:I\n\n    invoke-virtual {p1, p0}, Ljava/io/PrintWriter;->println(I)V\n\n    return-void\n.end method\n',
        'replacement':    '.method public final dump(Ljava/io/PrintWriter;[Ljava/lang/String;)V\n    .registers 3\n\n    const-string p2, "MiuiChargeManager state:"\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V\n\n    const-string p2, "  isChargeAnimationDisabled ="\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->print(Ljava/lang/String;)V\n\n    invoke-static {}, Lcom/miui/charge/ChargeUtils;->isChargeAnimationDisabled()Z\n\n    move-result p2\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->println(Z)V\n\n    const-string p2, "  mLevel ="\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->print(Ljava/lang/String;)V\n\n    iget-object p2, p0, Lcom/miui/charge/MiuiChargeManager;->mBatteryStatus:Lcom/miui/systemui/charge/BatteryStatus;\n\n    iget p2, p2, Lcom/miui/systemui/charge/BatteryStatus;->level:I\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->println(I)V\n\n    const-string p2, "  mWireState ="\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->print(Ljava/lang/String;)V\n\n    iget-object p2, p0, Lcom/miui/charge/MiuiChargeManager;->mBatteryStatus:Lcom/miui/systemui/charge/BatteryStatus;\n\n    iget p2, p2, Lcom/miui/systemui/charge/BatteryStatus;->wireState:I\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->println(I)V\n\n    const-string p2, "  mChargeSpeed ="\n\n    invoke-virtual {p1, p2}, Ljava/io/PrintWriter;->print(Ljava/lang/String;)V\n\n    iget-object p0, p0, Lcom/miui/charge/MiuiChargeManager;->mBatteryStatus:Lcom/miui/systemui/charge/BatteryStatus;\n\n    iget p0, p0, Lcom/miui/systemui/charge/BatteryStatus;->chargeSpeed:I\n\n    invoke-virtual {p1, p0}, Ljava/io/PrintWriter;->println(I)V\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI generated generated dex rule modified class',
    },
]
