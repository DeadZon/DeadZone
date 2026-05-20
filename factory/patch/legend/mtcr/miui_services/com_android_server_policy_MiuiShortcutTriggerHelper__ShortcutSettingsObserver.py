"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-services.jar
Target class : com/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver
Source MTCR  : miui-services_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-services.jar"
TARGET_CLASS = "com/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver.smali"

PATCHES = [
    {
        "id":          "replace_method_initShortcutSettingsObserver__V",
        "method":      ".method public initShortcutSettingsObserver()V",
        "type":        "method_replace",
        "search": """\
.method public initShortcutSettingsObserver()V
    .registers 8

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "long_press_power_launch_xiaoai"

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    const/4 v2, 0x0

    const/4 v3, -0x1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "long_press_power_launch_smarthome"

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "screen_key_press_app_switch"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "fingerprint_nav_center_action"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "single_key_use_enable"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "long_press_menu_key_when_lock"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    sget-boolean v0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    if-nez v0, :cond_0

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "xiaoai_power_guide"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p0, v2, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(ZLandroid/net/Uri;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v0, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mSupportXiaoaiLongpressPowerKeyTalk:Z

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "has_lunch_cn_power_guide_count"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p0, v2, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(ZLandroid/net/Uri;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$sfgetSHOULD_LAUNCH_POWER_PANEL()Ljava/lang/String;

    move-result-object v4

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-static {}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$sfgetSHOULD_LAUNCH_POWER_PANEL()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p0, v2, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(ZLandroid/net/Uri;)V

    :cond_0
    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-virtual {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->supportRSARegion()Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v0, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mSupportGlobalPowerGuide_V2:Z

    if-nez v0, :cond_1

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "global_power_guide"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p0, v2, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(ZLandroid/net/Uri;)V

    goto :goto_0

    :cond_1
    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "global_power_guide_v2"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p0, v2, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(ZLandroid/net/Uri;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$sfgetSHOULD_LAUNCH_POWER_PANEL()Ljava/lang/String;

    move-result-object v4

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-static {}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$sfgetSHOULD_LAUNCH_POWER_PANEL()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p0, v2, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(ZLandroid/net/Uri;)V

    :cond_2
    :goto_0
    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "user_setup_complete"

    invoke-static {v4}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v5, "pc_mode_open"

    invoke-static {v5}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "emergency_gesture_enabled"

    invoke-static {v1}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "key_miui_sos_enable"

    invoke-static {v1}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v5, "key_is_in_miui_sos_mode"

    invoke-static {v5}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v6

    invoke-virtual {v0, v6, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v6, "imperceptible_press_power_key"

    invoke-static {v6}, Landroid/provider/Settings$Global;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v6

    invoke-virtual {v0, v6, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v1}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v5}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "long_press_timeout"

    invoke-static {v1}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "torch_state"

    invoke-static {v1}, Landroid/provider/Settings$Global;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "assist_long_press_home_enabled"

    invoke-static {v1}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    sget-object v1, Landroid/provider/MiuiSettings$Secure;->MIUI_OPTIMIZATION:Ljava/lang/String;

    invoke-static {v1}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v4}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-virtual {p0, v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(Z)V

    return-void
.end method
""",
        "replacement": """\
.method public initShortcutSettingsObserver()V
    .registers 8

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "long_press_power_launch_xiaoai"

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    const/4 v2, 0x0

    const/4 v3, -0x1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "long_press_power_launch_smarthome"

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "screen_key_press_app_switch"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "fingerprint_nav_center_action"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "single_key_use_enable"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "long_press_menu_key_when_lock"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    if-nez v0, :cond_0

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "xiaoai_power_guide"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p0, v2, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(ZLandroid/net/Uri;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v0, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mSupportXiaoaiLongpressPowerKeyTalk:Z

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "has_lunch_cn_power_guide_count"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p0, v2, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(ZLandroid/net/Uri;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$sfgetSHOULD_LAUNCH_POWER_PANEL()Ljava/lang/String;

    move-result-object v4

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-static {}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$sfgetSHOULD_LAUNCH_POWER_PANEL()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p0, v2, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(ZLandroid/net/Uri;)V

    :cond_0
    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-virtual {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->supportRSARegion()Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v0, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mSupportGlobalPowerGuide_V2:Z

    if-nez v0, :cond_1

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "global_power_guide"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p0, v2, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(ZLandroid/net/Uri;)V

    goto :goto_0

    :cond_1
    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "global_power_guide_v2"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p0, v2, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(ZLandroid/net/Uri;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$sfgetSHOULD_LAUNCH_POWER_PANEL()Ljava/lang/String;

    move-result-object v4

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v0, v4, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-static {}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$sfgetSHOULD_LAUNCH_POWER_PANEL()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {p0, v2, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(ZLandroid/net/Uri;)V

    :cond_2
    :goto_0
    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v4, "user_setup_complete"

    invoke-static {v4}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v5, "pc_mode_open"

    invoke-static {v5}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "emergency_gesture_enabled"

    invoke-static {v1}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "key_miui_sos_enable"

    invoke-static {v1}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    invoke-virtual {v0, v5, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v5, "key_is_in_miui_sos_mode"

    invoke-static {v5}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v6

    invoke-virtual {v0, v6, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v6, "imperceptible_press_power_key"

    invoke-static {v6}, Landroid/provider/Settings$Global;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v6

    invoke-virtual {v0, v6, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v1}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v5}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "long_press_timeout"

    invoke-static {v1}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "torch_state"

    invoke-static {v1}, Landroid/provider/Settings$Global;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "assist_long_press_home_enabled"

    invoke-static {v1}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    sget-object v1, Landroid/provider/MiuiSettings$Secure;->MIUI_OPTIMIZATION:Ljava/lang/String;

    invoke-static {v1}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    invoke-static {v4}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1, v2, p0, v3}, Landroid/content/ContentResolver;->registerContentObserver(Landroid/net/Uri;ZLandroid/database/ContentObserver;I)V

    invoke-virtual {p0, v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->onChange(Z)V

    return-void
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
    {
        "id":          "replace_method_onChange_Z_V",
        "method":      ".method public onChange(Z)V",
        "type":        "method_replace",
        "search": """\
.method public onChange(Z)V
    .registers 9

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v2

    const-string v3, "long_press_power_launch_xiaoai"

    const/4 v4, 0x0

    invoke-static {v1, v3, v4, v2}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    const/4 v2, 0x1

    if-ne v1, v2, :cond_0

    move v1, v2

    goto :goto_0

    :cond_0
    move v1, v4

    :goto_0
    iput-boolean v1, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mLongPressPowerKeyLaunchXiaoAi:Z

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "screen_key_press_app_switch"

    invoke-static {v1, v5, v2, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    if-eqz v1, :cond_1

    move v1, v2

    goto :goto_1

    :cond_1
    move v1, v4

    :goto_1
    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmPressToAppSwitch(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "fingerprint_nav_center_action"

    const/4 v6, -0x1

    invoke-static {v1, v5, v6, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmFingerPrintNavCenterAction(Lcom/android/server/policy/MiuiShortcutTriggerHelper;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "single_key_use_enable"

    invoke-static {v1, v5, v4, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    if-ne v1, v2, :cond_2

    move v1, v2

    goto :goto_2

    :cond_2
    move v1, v4

    :goto_2
    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmSingleKeyUse(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmSingleKeyUse(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Z

    move-result v1

    iput v1, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mDoubleTapOnHomeBehavior:I

    sget-boolean v0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    if-nez v0, :cond_3

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "xiaoai_power_guide"

    invoke-static {v1, v5, v2, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    iput v1, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mXiaoaiPowerGuideFlag:I

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v0, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mSupportXiaoaiLongpressPowerKeyTalk:Z

    if-eqz v0, :cond_3

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "has_lunch_cn_power_guide_count"

    invoke-static {v1, v5, v4, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    iput v1, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mXiaoaiLongPressPowerKeyTalkGuideCount:I

    :cond_3
    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v3, v3, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mSupportGlobalPowerGuide_V2:Z

    if-eqz v3, :cond_4

    const-string v3, "global_power_guide_v2"

    goto :goto_3

    :cond_4
    const-string v3, "global_power_guide"

    :goto_3
    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v5

    invoke-static {v1, v3, v2, v5}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmRSAGuideStatus(Lcom/android/server/policy/MiuiShortcutTriggerHelper;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "emergency_gesture_enabled"

    invoke-static {v1, v5, v3}, Landroid/provider/Settings$Secure;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmFivePressPowerLaunchGoogleSos(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Ljava/lang/String;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "key_miui_sos_enable"

    invoke-static {v1, v5, v4, v3}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    if-ne v1, v2, :cond_5

    move v1, v2

    goto :goto_4

    :cond_5
    move v1, v4

    :goto_4
    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmFivePressPowerLaunchSos(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "key_is_in_miui_sos_mode"

    invoke-static {v1, v5, v4, v3}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    if-ne v1, v2, :cond_6

    move v1, v2

    goto :goto_5

    :cond_6
    move v1, v4

    :goto_5
    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmIsOnSosMode(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "long_press_timeout"

    invoke-static {v1, v5, v4, v3}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    iput v1, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mDefaultLongPressTimeOut:I

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    const-string v3, "torch_state"

    invoke-static {v1, v3, v4}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    if-eqz v1, :cond_7

    move v1, v2

    goto :goto_6

    :cond_7
    move v1, v4

    :goto_6
    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmTorchEnabled(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    const-string v3, "assist_long_press_home_enabled"

    invoke-static {v1, v3, v2}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    if-ne v1, v2, :cond_8

    move v4, v2

    :cond_8
    invoke-static {v0, v4}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmAOSPAssistantLongPressHomeEnabled(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    const-string v1, "ro.miui.cts"

    invoke-static {v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    const-string v3, "1"

    invoke-virtual {v3, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    xor-int/2addr v1, v2

    const-string v3, "persist.sys.miui_optimization"

    invoke-static {v3, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z

    move-result v1

    xor-int/2addr v1, v2

    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmIsCtsMode(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    return-void
.end method
""",
        "replacement": """\
.method public onChange(Z)V
    .registers 9

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v2

    const-string v3, "long_press_power_launch_xiaoai"

    const/4 v4, 0x0

    invoke-static {v1, v3, v4, v2}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    const/4 v2, 0x1

    if-ne v1, v2, :cond_0

    move v1, v2

    goto :goto_0

    :cond_0
    move v1, v4

    :goto_0
    iput-boolean v1, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mLongPressPowerKeyLaunchXiaoAi:Z

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "screen_key_press_app_switch"

    invoke-static {v1, v5, v2, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    if-eqz v1, :cond_1

    move v1, v2

    goto :goto_1

    :cond_1
    move v1, v4

    :goto_1
    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmPressToAppSwitch(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "fingerprint_nav_center_action"

    const/4 v6, -0x1

    invoke-static {v1, v5, v6, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmFingerPrintNavCenterAction(Lcom/android/server/policy/MiuiShortcutTriggerHelper;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "single_key_use_enable"

    invoke-static {v1, v5, v4, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    if-ne v1, v2, :cond_2

    move v1, v2

    goto :goto_2

    :cond_2
    move v1, v4

    :goto_2
    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmSingleKeyUse(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmSingleKeyUse(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Z

    move-result v1

    iput v1, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mDoubleTapOnHomeBehavior:I

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    if-nez v0, :cond_3

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "xiaoai_power_guide"

    invoke-static {v1, v5, v2, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    iput v1, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mXiaoaiPowerGuideFlag:I

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v0, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mSupportXiaoaiLongpressPowerKeyTalk:Z

    if-eqz v0, :cond_3

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "has_lunch_cn_power_guide_count"

    invoke-static {v1, v5, v4, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    iput v1, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mXiaoaiLongPressPowerKeyTalkGuideCount:I

    :cond_3
    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v3, v3, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mSupportGlobalPowerGuide_V2:Z

    if-eqz v3, :cond_4

    const-string v3, "global_power_guide_v2"

    goto :goto_3

    :cond_4
    const-string v3, "global_power_guide"

    :goto_3
    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v5

    invoke-static {v1, v3, v2, v5}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmRSAGuideStatus(Lcom/android/server/policy/MiuiShortcutTriggerHelper;I)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "emergency_gesture_enabled"

    invoke-static {v1, v5, v3}, Landroid/provider/Settings$Secure;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmFivePressPowerLaunchGoogleSos(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Ljava/lang/String;)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "key_miui_sos_enable"

    invoke-static {v1, v5, v4, v3}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    if-ne v1, v2, :cond_5

    move v1, v2

    goto :goto_4

    :cond_5
    move v1, v4

    :goto_4
    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmFivePressPowerLaunchSos(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "key_is_in_miui_sos_mode"

    invoke-static {v1, v5, v4, v3}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    if-ne v1, v2, :cond_6

    move v1, v2

    goto :goto_5

    :cond_6
    move v1, v4

    :goto_5
    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmIsOnSosMode(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    const-string v5, "long_press_timeout"

    invoke-static {v1, v5, v4, v3}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v1

    iput v1, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mDefaultLongPressTimeOut:I

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    const-string v3, "torch_state"

    invoke-static {v1, v3, v4}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    if-eqz v1, :cond_7

    move v1, v2

    goto :goto_6

    :cond_7
    move v1, v4

    :goto_6
    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmTorchEnabled(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v1

    const-string v3, "assist_long_press_home_enabled"

    invoke-static {v1, v3, v2}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    if-ne v1, v2, :cond_8

    move v4, v2

    :cond_8
    invoke-static {v0, v4}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmAOSPAssistantLongPressHomeEnabled(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    const-string v1, "ro.miui.cts"

    invoke-static {v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    const-string v3, "1"

    invoke-virtual {v3, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    xor-int/2addr v1, v2

    const-string v3, "persist.sys.miui_optimization"

    invoke-static {v3, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z

    move-result v1

    xor-int/2addr v1, v2

    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmIsCtsMode(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    return-void
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
    {
        "id":          "replace_method_onChange_ZLandroid_net_Uri__V",
        "method":      ".method public onChange(ZLandroid/net/Uri;)V",
        "type":        "method_replace",
        "search": """\
.method public onChange(ZLandroid/net/Uri;)V
    .registers 10

    const-string v0, "long_press_power_launch_xiaoai"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    const-string v2, "long_press_power_key"

    const/4 v3, 0x0

    const/4 v4, 0x1

    if-eqz v1, :cond_3

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v5

    iget-object v6, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v6}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v6

    invoke-static {v5, v0, v3, v6}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v4, :cond_0

    move v3, v4

    :cond_0
    iput-boolean v3, v1, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mLongPressPowerKeyLaunchXiaoAi:Z

    sget-boolean v0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    if-eqz v0, :cond_2

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v1, v1, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mLongPressPowerKeyLaunchXiaoAi:Z

    if-eqz v1, :cond_1

    const-string v1, "launch_google_search"

    goto :goto_0

    :cond_1
    const-string v1, "none"

    :goto_0
    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    invoke-static {v0, v2, v1, v3}, Landroid/provider/Settings$System;->putStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;I)Z

    goto :goto_1

    :cond_2
    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v0, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mLongPressPowerKeyLaunchXiaoAi:Z

    if-eqz v0, :cond_19

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v1

    const-string v3, "launch_voice_assistant"

    invoke-static {v0, v2, v3, v1}, Landroid/provider/Settings$System;->putStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;I)Z

    goto :goto_1

    :cond_3
    const-string v0, "long_press_power_launch_smarthome"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_5

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v5

    iget-object v6, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v6}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v6

    invoke-static {v5, v0, v3, v6}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v4, :cond_4

    move v3, v4

    :cond_4
    iput-boolean v3, v1, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mLongPressPowerKeyLaunchSmartHome:Z

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v0, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mLongPressPowerKeyLaunchSmartHome:Z

    if-eqz v0, :cond_19

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v1

    const-string v3, "launch_smarthome"

    invoke-static {v0, v2, v3, v1}, Landroid/provider/Settings$System;->putStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;I)Z

    goto :goto_1

    :cond_5
    const-string v0, "screen_key_press_app_switch"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_7

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v5

    invoke-static {v2, v0, v4, v5}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-eqz v0, :cond_6

    move v3, v4

    :cond_6
    invoke-static {v1, v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmPressToAppSwitch(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    goto :goto_1

    :cond_7
    const-string v0, "fingerprint_nav_center_action"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    const/4 v5, -0x1

    if-eqz v1, :cond_8

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    invoke-static {v2, v0, v5, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    invoke-static {v1, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmFingerPrintNavCenterAction(Lcom/android/server/policy/MiuiShortcutTriggerHelper;I)V

    goto :goto_1

    :cond_8
    const-string v0, "single_key_use_enable"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_a

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v5

    invoke-static {v2, v0, v3, v5}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v4, :cond_9

    move v3, v4

    :cond_9
    invoke-static {v1, v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmSingleKeyUse(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmSingleKeyUse(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Z

    move-result v1

    iput v1, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mDoubleTapOnHomeBehavior:I

    goto :goto_1

    :cond_a
    const-string v0, "xiaoai_power_guide"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_b

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContext(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/Context;

    move-result-object v2

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    invoke-static {v2, v0, v4, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mXiaoaiPowerGuideFlag:I

    goto :goto_1

    :cond_b
    const-string v0, "has_lunch_cn_power_guide_count"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_c

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContext(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/Context;

    move-result-object v2

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v4, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v4}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v4

    invoke-static {v2, v0, v3, v4}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mXiaoaiLongPressPowerKeyTalkGuideCount:I

    goto :goto_1

    :cond_c
    const-string v0, "emergency_gesture_enabled"

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_d

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    invoke-static {v2, v0, v3}, Landroid/provider/Settings$Secure;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmFivePressPowerLaunchGoogleSos(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Ljava/lang/String;)V

    goto :goto_1

    :cond_d
    const-string v0, "key_miui_sos_enable"

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_f

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v5

    invoke-static {v2, v0, v3, v5}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v4, :cond_e

    move v3, v4

    :cond_e
    invoke-static {v1, v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmFivePressPowerLaunchSos(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    goto :goto_1

    :cond_f
    const-string v0, "key_is_in_miui_sos_mode"

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_11

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v5

    invoke-static {v2, v0, v3, v5}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v4, :cond_10

    move v3, v4

    :cond_10
    invoke-static {v1, v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmIsOnSosMode(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    goto :goto_1

    :cond_11
    const-string v0, "global_power_guide"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_12

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    invoke-static {v2, v0, v4, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    invoke-static {v1, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmRSAGuideStatus(Lcom/android/server/policy/MiuiShortcutTriggerHelper;I)V

    goto :goto_1

    :cond_12
    const-string v0, "global_power_guide_v2"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_13

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    invoke-static {v2, v0, v4, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    invoke-static {v1, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmRSAGuideStatus(Lcom/android/server/policy/MiuiShortcutTriggerHelper;I)V

    goto :goto_1

    :cond_13
    invoke-static {}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$sfgetSHOULD_LAUNCH_POWER_PANEL()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {v0, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_14

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v1

    invoke-static {v0, v2, v1}, Landroid/provider/Settings$System;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    invoke-static {}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$sfgetSHOULD_LAUNCH_POWER_PANEL()Ljava/lang/String;

    move-result-object v3

    iget-object v4, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v4}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v4

    invoke-static {v2, v3, v5, v4}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v2

    invoke-static {v1, v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmShouldShowPowerPanel(Lcom/android/server/policy/MiuiShortcutTriggerHelper;I)V

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-virtual {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->setVeryLongPressPowerBehavior()V

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-virtual {v1, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->setLongPressPowerBehavior(Ljava/lang/String;)V

    const-string v1, "MiuiShortcutTriggerHelp"

    const-string v2, "update SHOULD_LAUNCH_POWER_PANEL"

    invoke-static {v1, v2}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1

    :cond_14
    const-string v0, "long_press_timeout"

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_15

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v4, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v4}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v4

    invoke-static {v2, v0, v3, v4}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mDefaultLongPressTimeOut:I

    goto :goto_1

    :cond_15
    const-string v0, "assist_long_press_home_enabled"

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_17

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    invoke-static {v2, v0, v5}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    if-ne v0, v4, :cond_16

    move v3, v4

    :cond_16
    invoke-static {v1, v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmAOSPAssistantLongPressHomeEnabled(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    goto :goto_1

    :cond_17
    sget-object v0, Landroid/provider/MiuiSettings$Secure;->MIUI_OPTIMIZATION:Ljava/lang/String;

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {v0, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_18

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    const-string v1, "ro.miui.cts"

    invoke-static {v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    const-string v2, "1"

    invoke-virtual {v2, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    xor-int/2addr v1, v4

    const-string v2, "persist.sys.miui_optimization"

    invoke-static {v2, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z

    move-result v1

    xor-int/2addr v1, v4

    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmIsCtsMode(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    goto :goto_1

    :cond_18
    const-string v0, "user_setup_complete"

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {v0, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_19

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-virtual {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->setVeryLongPressPowerBehavior()V

    :cond_19
    :goto_1
    invoke-super {p0, p1, p2}, Landroid/database/ContentObserver;->onChange(ZLandroid/net/Uri;)V

    return-void
.end method
""",
        "replacement": """\
.method public onChange(ZLandroid/net/Uri;)V
    .registers 10

    const-string v0, "long_press_power_launch_xiaoai"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    const-string v2, "long_press_power_key"

    const/4 v3, 0x0

    const/4 v4, 0x1

    if-eqz v1, :cond_3

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v5

    iget-object v6, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v6}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v6

    invoke-static {v5, v0, v3, v6}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v4, :cond_0

    move v3, v4

    :cond_0
    iput-boolean v3, v1, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mLongPressPowerKeyLaunchXiaoAi:Z

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz v0, :cond_2

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v1, v1, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mLongPressPowerKeyLaunchXiaoAi:Z

    if-eqz v1, :cond_1

    const-string v1, "launch_google_search"

    goto :goto_0

    :cond_1
    const-string v1, "none"

    :goto_0
    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    invoke-static {v0, v2, v1, v3}, Landroid/provider/Settings$System;->putStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;I)Z

    goto :goto_1

    :cond_2
    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v0, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mLongPressPowerKeyLaunchXiaoAi:Z

    if-eqz v0, :cond_19

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v1

    const-string v3, "launch_voice_assistant"

    invoke-static {v0, v2, v3, v1}, Landroid/provider/Settings$System;->putStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;I)Z

    goto :goto_1

    :cond_3
    const-string v0, "long_press_power_launch_smarthome"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_5

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v5

    iget-object v6, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v6}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v6

    invoke-static {v5, v0, v3, v6}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v4, :cond_4

    move v3, v4

    :cond_4
    iput-boolean v3, v1, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mLongPressPowerKeyLaunchSmartHome:Z

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-boolean v0, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mLongPressPowerKeyLaunchSmartHome:Z

    if-eqz v0, :cond_19

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v1

    const-string v3, "launch_smarthome"

    invoke-static {v0, v2, v3, v1}, Landroid/provider/Settings$System;->putStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;I)Z

    goto :goto_1

    :cond_5
    const-string v0, "screen_key_press_app_switch"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_7

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v5

    invoke-static {v2, v0, v4, v5}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-eqz v0, :cond_6

    move v3, v4

    :cond_6
    invoke-static {v1, v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmPressToAppSwitch(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    goto :goto_1

    :cond_7
    const-string v0, "fingerprint_nav_center_action"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    const/4 v5, -0x1

    if-eqz v1, :cond_8

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    invoke-static {v2, v0, v5, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    invoke-static {v1, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmFingerPrintNavCenterAction(Lcom/android/server/policy/MiuiShortcutTriggerHelper;I)V

    goto :goto_1

    :cond_8
    const-string v0, "single_key_use_enable"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_a

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v5

    invoke-static {v2, v0, v3, v5}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v4, :cond_9

    move v3, v4

    :cond_9
    invoke-static {v1, v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmSingleKeyUse(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmSingleKeyUse(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Z

    move-result v1

    iput v1, v0, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mDoubleTapOnHomeBehavior:I

    goto :goto_1

    :cond_a
    const-string v0, "xiaoai_power_guide"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_b

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContext(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/Context;

    move-result-object v2

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    invoke-static {v2, v0, v4, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mXiaoaiPowerGuideFlag:I

    goto :goto_1

    :cond_b
    const-string v0, "has_lunch_cn_power_guide_count"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_c

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContext(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/Context;

    move-result-object v2

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v4, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v4}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v4

    invoke-static {v2, v0, v3, v4}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mXiaoaiLongPressPowerKeyTalkGuideCount:I

    goto :goto_1

    :cond_c
    const-string v0, "emergency_gesture_enabled"

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_d

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    invoke-static {v2, v0, v3}, Landroid/provider/Settings$Secure;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmFivePressPowerLaunchGoogleSos(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Ljava/lang/String;)V

    goto :goto_1

    :cond_d
    const-string v0, "key_miui_sos_enable"

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_f

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v5

    invoke-static {v2, v0, v3, v5}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v4, :cond_e

    move v3, v4

    :cond_e
    invoke-static {v1, v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmFivePressPowerLaunchSos(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    goto :goto_1

    :cond_f
    const-string v0, "key_is_in_miui_sos_mode"

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_11

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v5, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v5}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v5

    invoke-static {v2, v0, v3, v5}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v4, :cond_10

    move v3, v4

    :cond_10
    invoke-static {v1, v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmIsOnSosMode(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    goto :goto_1

    :cond_11
    const-string v0, "global_power_guide"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_12

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    invoke-static {v2, v0, v4, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    invoke-static {v1, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmRSAGuideStatus(Lcom/android/server/policy/MiuiShortcutTriggerHelper;I)V

    goto :goto_1

    :cond_12
    const-string v0, "global_power_guide_v2"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_13

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v3

    invoke-static {v2, v0, v4, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    invoke-static {v1, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmRSAGuideStatus(Lcom/android/server/policy/MiuiShortcutTriggerHelper;I)V

    goto :goto_1

    :cond_13
    invoke-static {}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$sfgetSHOULD_LAUNCH_POWER_PANEL()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {v0, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_14

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v1

    invoke-static {v0, v2, v1}, Landroid/provider/Settings$System;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    invoke-static {}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$sfgetSHOULD_LAUNCH_POWER_PANEL()Ljava/lang/String;

    move-result-object v3

    iget-object v4, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v4}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v4

    invoke-static {v2, v3, v5, v4}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v2

    invoke-static {v1, v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmShouldShowPowerPanel(Lcom/android/server/policy/MiuiShortcutTriggerHelper;I)V

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-virtual {v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->setVeryLongPressPowerBehavior()V

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-virtual {v1, v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->setLongPressPowerBehavior(Ljava/lang/String;)V

    const-string v1, "MiuiShortcutTriggerHelp"

    const-string v2, "update SHOULD_LAUNCH_POWER_PANEL"

    invoke-static {v1, v2}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1

    :cond_14
    const-string v0, "long_press_timeout"

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_15

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    iget-object v4, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v4}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmCurrentUserId(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)I

    move-result v4

    invoke-static {v2, v0, v3, v4}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    iput v0, v1, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->mDefaultLongPressTimeOut:I

    goto :goto_1

    :cond_15
    const-string v0, "assist_long_press_home_enabled"

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v1, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_17

    iget-object v1, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    iget-object v2, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-static {v2}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fgetmContentResolver(Lcom/android/server/policy/MiuiShortcutTriggerHelper;)Landroid/content/ContentResolver;

    move-result-object v2

    invoke-static {v2, v0, v5}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    if-ne v0, v4, :cond_16

    move v3, v4

    :cond_16
    invoke-static {v1, v3}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmAOSPAssistantLongPressHomeEnabled(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    goto :goto_1

    :cond_17
    sget-object v0, Landroid/provider/MiuiSettings$Secure;->MIUI_OPTIMIZATION:Ljava/lang/String;

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {v0, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_18

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    const-string v1, "ro.miui.cts"

    invoke-static {v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    const-string v2, "1"

    invoke-virtual {v2, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    xor-int/2addr v1, v4

    const-string v2, "persist.sys.miui_optimization"

    invoke-static {v2, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z

    move-result v1

    xor-int/2addr v1, v4

    invoke-static {v0, v1}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->-$$Nest$fputmIsCtsMode(Lcom/android/server/policy/MiuiShortcutTriggerHelper;Z)V

    goto :goto_1

    :cond_18
    const-string v0, "user_setup_complete"

    invoke-static {v0}, Landroid/provider/Settings$Secure;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v0

    invoke-virtual {v0, p2}, Landroid/net/Uri;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_19

    iget-object v0, p0, Lcom/android/server/policy/MiuiShortcutTriggerHelper$ShortcutSettingsObserver;->this$0:Lcom/android/server/policy/MiuiShortcutTriggerHelper;

    invoke-virtual {v0}, Lcom/android/server/policy/MiuiShortcutTriggerHelper;->setVeryLongPressPowerBehavior()V

    :cond_19
    :goto_1
    invoke-super {p0, p1, p2}, Landroid/database/ContentObserver;->onChange(ZLandroid/net/Uri;)V

    return-void
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
]
