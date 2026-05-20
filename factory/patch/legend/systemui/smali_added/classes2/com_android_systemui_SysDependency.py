"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/SysDependency.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/SysDependency.smali'
CLASS_FALLBACK_NAMES = ['SysDependency.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_SysDependency',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/SysDependency;\n.super Ljava/lang/Object;\n\n\n# direct methods\n.method public constructor <init>()V\n    .registers 1\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n.method public static get(Lcom/android/systemui/Dependency$DependencyKey;)Ljava/lang/Object;\n    .registers 2\n\n    sget-object v0, Lcom/android/systemui/Dependency;->sDependency:Lcom/android/systemui/Dependency;\n\n    invoke-virtual {v0, p0}, Lcom/android/systemui/Dependency;->getDependencyInner(Ljava/lang/Object;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    return-object v0\n.end method\n\n.method public static get(Ljava/lang/Class;)Ljava/lang/Object;\n    .registers 2\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "<T:",\n            "Ljava/lang/Object;",\n            ">(",\n            "Ljava/lang/Class",\n            "<TT;>;)TT;"\n        }\n    .end annotation\n\n    sget-object v0, Lcom/android/systemui/Dependency;->sDependency:Lcom/android/systemui/Dependency;\n\n    invoke-virtual {v0, p0}, Lcom/android/systemui/Dependency;->getDependencyInner(Ljava/lang/Object;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    invoke-virtual {p0, v0}, Ljava/lang/Class;->cast(Ljava/lang/Object;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    return-object v0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
