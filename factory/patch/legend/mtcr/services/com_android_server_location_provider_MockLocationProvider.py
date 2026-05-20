"""
Legend MTCR patch - class-level rule.

Target JAR   : services.jar
Target class : com/android/server/location/provider/MockLocationProvider
Source MTCR  : Service_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "services.jar"
TARGET_CLASS = "com/android/server/location/provider/MockLocationProvider.smali"
CLASS_FALLBACK_NAMES = ['MockLocationProvider.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "replace_method_onExtraCommand_IILjava_lang_String_Landroid_os_Bundle__V",
        "method":      ".method protected onExtraCommand(IILjava/lang/String;Landroid/os/Bundle;)V",
        "method_name": 'onExtraCommand',
        "type":        "method_replace",
        "search": """\
.method protected onExtraCommand(IILjava/lang/String;Landroid/os/Bundle;)V
    .registers 5

    return-void
.end method
""",
        "replacement": """\
.method protected onExtraCommand(IILjava/lang/String;Landroid/os/Bundle;)V
    .registers 5

    goto :goto_0

    nop

    :goto_0
    return-void
.end method
""",
        "method_anchors": ['return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_onFlush_Ljava_lang_Runnable__V",
        "method":      ".method protected onFlush(Ljava/lang/Runnable;)V",
        "method_name": 'onFlush',
        "type":        "method_replace",
        "search": """\
.method protected onFlush(Ljava/lang/Runnable;)V
    .registers 2

    invoke-interface {p1}, Ljava/lang/Runnable;->run()V

    return-void
.end method
""",
        "replacement": """\
.method protected onFlush(Ljava/lang/Runnable;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-interface {p1}, Ljava/lang/Runnable;->run()V

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['invoke-interface {p1}, Ljava/lang/Runnable;->run()V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setProviderLocation_Landroid_location_Location__V",
        "method":      ".method public setProviderLocation(Landroid/location/Location;)V",
        "method_name": 'setProviderLocation',
        "type":        "method_replace",
        "search": """\
.method public setProviderLocation(Landroid/location/Location;)V
    .registers 5

    new-instance v0, Landroid/location/Location;

    invoke-direct {v0, p1}, Landroid/location/Location;-><init>(Landroid/location/Location;)V

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Landroid/location/Location;->setIsFromMockProvider(Z)V

    iput-object v0, p0, Lcom/android/server/location/provider/MockLocationProvider;->mLocation:Landroid/location/Location;

    :try_start_0
    new-array v1, v1, [Landroid/location/Location;

    const/4 v2, 0x0

    aput-object v0, v1, v2

    invoke-static {v1}, Landroid/location/LocationResult;->wrap([Landroid/location/Location;)Landroid/location/LocationResult;

    move-result-object v1

    invoke-virtual {v1}, Landroid/location/LocationResult;->validate()Landroid/location/LocationResult;

    move-result-object v1

    invoke-virtual {p0, v1}, Lcom/android/server/location/provider/MockLocationProvider;->reportLocation(Landroid/location/LocationResult;)V
    :try_end_0
    .catch Landroid/location/LocationResult$BadLocationException; {:try_start_0 .. :try_end_0} :catch_0

    nop

    return-void

    :catch_0
    move-exception v1

    new-instance v2, Ljava/lang/IllegalArgumentException;

    invoke-direct {v2, v1}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/Throwable;)V

    throw v2
.end method
""",
        "replacement": """\
.method public setProviderLocation(Landroid/location/Location;)V
    .registers 5

    const/4 v1, 0x1

    const-string v0, "enable_mezo_mock_locations"

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    if-eqz v0, :cond_0

    const/4 v1, 0x0

    :cond_0
    new-instance v0, Landroid/location/Location;

    invoke-direct {v0, p1}, Landroid/location/Location;-><init>(Landroid/location/Location;)V

    invoke-virtual {v0, v1}, Landroid/location/Location;->setIsFromMockProvider(Z)V

    iput-object v0, p0, Lcom/android/server/location/provider/MockLocationProvider;->mLocation:Landroid/location/Location;

    :try_start_0
    new-array v1, v1, [Landroid/location/Location;

    const/4 v2, 0x0

    aput-object v0, v1, v2

    invoke-static {v1}, Landroid/location/LocationResult;->wrap([Landroid/location/Location;)Landroid/location/LocationResult;

    move-result-object v1

    invoke-virtual {v1}, Landroid/location/LocationResult;->validate()Landroid/location/LocationResult;

    move-result-object v1

    invoke-virtual {p0, v1}, Lcom/android/server/location/provider/MockLocationProvider;->reportLocation(Landroid/location/LocationResult;)V
    :try_end_0
    .catch Landroid/location/LocationResult$BadLocationException; {:try_start_0 .. :try_end_0} :catch_0

    nop

    return-void

    :catch_0
    move-exception v1

    new-instance v2, Ljava/lang/IllegalArgumentException;

    invoke-direct {v2, v1}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/Throwable;)V

    throw v2
.end method
""",
        "method_anchors": ['new-instance v0, Landroid/location/Location;', 'invoke-direct {v0, p1}, Landroid/location/Location;-><init>(Landroid/location/Location;)V', 'invoke-virtual {v0, v1}, Landroid/location/Location;->setIsFromMockProvider(Z)V', 'iput-object v0, p0, Lcom/android/server/location/provider/MockLocationProvider;->mLocation:Landroid/location/Location;', 'invoke-static {v1}, Landroid/location/LocationResult;->wrap([Landroid/location/Location;)Landroid/location/LocationResult;', 'move-result-object v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
]
