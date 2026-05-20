"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-framework.jar
Target class : android/provider/MiuiSettings$System
Source MTCR  : miui-framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-framework.jar"
TARGET_CLASS = "android/provider/MiuiSettings$System.smali"

PATCHES = [
    {
        "id":          "replace_class_whole",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public Landroid/provider/MiuiSettings$System;
.super Landroid/provider/SystemSettings$System;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Landroid/provider/MiuiSettings;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x9
    name = "System"
.end annotation

.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Landroid/provider/MiuiSettings$System$SmallWindowType;
    }
.end annotation


# static fields
.field public static final blacklist ACCELEROMETER_ROTATION_INNER:Ljava/lang/String; = "accelerometer_rotation_inner"

.field public static final blacklist ACCELEROMETER_ROTATION_OUTER:Ljava/lang/String; = "accelerometer_rotation_outer"

.field public static final blacklist ACTIVITY_RESOLVE_ORDER:Ljava/lang/String; = "activity_resolve_order"

.field private static final blacklist ACTIVITY_RESOLVE_ORDER_DELIMETER:Ljava/lang/String; = ","

.field public static final blacklist AI_PRELOAD_USER_STATE:Ljava/lang/String; = "ai_preload_user_state"

.field public static final blacklist ALWAYS_ENABLE_MMS:Ljava/lang/String; = "always_enable_mms"

.field public static final blacklist ANR_PACKAGES:Ljava/lang/String; = "anr_pkgs"

.field public static final blacklist AUTO_DUAL_CLOCK:Ljava/lang/String; = "auto_dual_clock"

.field public static final blacklist AUTO_TEST_MODE_ENABLE:Ljava/lang/String; = "auto_test_mode_on"

.field public static final blacklist BATTERY_INDICATOR_STYLE:Ljava/lang/String; = "battery_indicator_style"

.field public static final blacklist BATTERY_INDICATOR_STYLE_DEFAULT:I = 0x1

.field public static final blacklist BATTERY_INDICATOR_STYLE_GRAPHIC:I = 0x0

.field public static final blacklist BATTERY_INDICATOR_STYLE_NUMBER:I = 0x1

.field public static final blacklist BATTERY_INDICATOR_STYLE_NUMBER_NEXT_TO_ICON:I = 0x3

.field public static final blacklist BATTERY_INDICATOR_STYLE_TOP:I = 0x2

.field public static final blacklist BATTERY_LEVEL_LOW_CUSTOMIZED:Ljava/lang/String; = "battery_level_low_customized"

.field public static final blacklist BEIDOU_SATELLITE_STATE:Ljava/lang/String; = "beidou_satellite_state"

.field public static final blacklist BREATHING_LIGHT_COLOR:Ljava/lang/String; = "breathing_light_color"

.field public static final blacklist BREATHING_LIGHT_FREQ:Ljava/lang/String; = "breathing_light_freq"

.field public static final blacklist BRT_BEFORE_OUTDOOR_MODE:Ljava/lang/String; = "brt_before_outdoor_mode"

.field public static final whitelist CALENDAR_ALERT:Ljava/lang/String; = "calendar_alert"

.field public static final blacklist CALENDAR_ALERT_CACHE:Ljava/lang/String; = "calendar_alert_cache"

.field public static final blacklist CALENDAR_ALERT_CACHE_URI:Landroid/net/Uri;

.field public static final blacklist CALL_BREATHING_LIGHT_COLOR:Ljava/lang/String; = "call_breathing_light_color"

.field public static final blacklist CALL_BREATHING_LIGHT_COLOR_DEFAULT:I

.field public static final blacklist CALL_BREATHING_LIGHT_FREQ:Ljava/lang/String; = "call_breathing_light_freq"

.field public static final blacklist CALL_BREATHING_LIGHT_FREQ_DEFAULT:I

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_APP_COMPONENT:Ljava/lang/String; = "camera_key_preferred_action_app_component"

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_SHORTCUT_ID:Ljava/lang/String; = "camera_key_preferred_action_shortcut_id"

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_SHORTCUT_ID_CALL:I = 0x3

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_SHORTCUT_ID_HOME:I = 0x0

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_SHORTCUT_ID_SCREENSHOT:I = 0x1

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_SHORTCUT_ID_SEARCH:I = 0x2

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_SHORTCUT_ID_WAKE:I = 0x4

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_TOGGLE_ID:Ljava/lang/String; = "camera_key_preferred_action_toggle_id"

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_TYPE:Ljava/lang/String; = "camera_key_preferred_action_type"

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_TYPE_APP:I = 0x3

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_TYPE_DEFAULT:I = 0x0

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_TYPE_NONE:I = 0x0

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_TYPE_SHORTCUT:I = 0x1

.field public static final blacklist CAMERA_KEY_PREFERRED_ACTION_TYPE_TOGGLE:I = 0x2

.field public static final blacklist CDMA_PRECISE_ANSWER_STATE:Ljava/lang/String; = "cdma_precise_answer_state"

.field public static final blacklist CDMA_PRECISE_ANSWER_STATE_DEFAULT:I = 0x1

.field public static final blacklist CDMA_PRECISE_ANSWER_STATE_DISABLE:I = 0x0

.field public static final blacklist CDMA_PRECISE_ANSWER_STATE_ENABLE:I = 0x1

.field public static final whitelist CLEAR_SIGNALMAP_DB:Ljava/lang/String; = "clear_signalmap_db"

.field public static final blacklist CLOUD_SLAVE_WIFI_SUPPORT:Ljava/lang/String; = "cloud_slave_wifi_support"

.field public static final blacklist CLOUD_SLA_WHITELIST:Ljava/lang/String; = "cloud_sla_whitelist"

.field public static final blacklist CLOUD_SLS_WHITELIST:Ljava/lang/String; = "cloud_sls_whitelist"

.field private static final blacklist CN_OPERATOR:Ljava/lang/String; = "460"

.field public static final blacklist COLOR_LAMP_TURN_ON:Ljava/lang/String; = "color_lamp_turn_on"

.field public static final blacklist CONFIG_NETWORK_PRIORITY_SUPPORT:Ljava/lang/String; = "sys.net.support.netprio"

.field public static final blacklist CONTRAST_ALPHA:Ljava/lang/String; = "contrast_alpha"

.field public static final blacklist CURRENT_LIVE_WALLPAPER_PACKAGENAME:Ljava/lang/String; = "current_live_wallpaper_packagename"

.field public static final blacklist DANGEROUS_OPTIONS_HINT:Ljava/lang/String; = "dangerous_option_hint"

.field public static final blacklist DATA_AND_WIFI_ROAM:Ljava/lang/String; = "data_and_wifi_roam"

.field public static final blacklist DATA_AND_WIFI_ROAM_DEFAULT:I = 0x0

.field public static final blacklist DEFAULT_ALARM_ALERT:Ljava/lang/String; = "default_alarm_alert"

.field public static final whitelist DEFAULT_CALENDAR_ALERT_URI:Landroid/net/Uri;

.field public static final blacklist DEFAULT_ENABLE_DEMO_MODE:Z = false

.field public static final blacklist DEFAULT_LOCAL_BACKUP_DISABLE:I = 0x0

.field public static final whitelist DEFAULT_NOTES_ALERT_URI:Landroid/net/Uri;

.field public static final whitelist DEFAULT_RINGTONE_URI_SLOT_1:Landroid/net/Uri;

.field public static final whitelist DEFAULT_RINGTONE_URI_SLOT_2:Landroid/net/Uri;

.field public static final blacklist DEFAULT_SCREEN_BUTTONS_TIMEOUT:I = 0x1388

.field public static final whitelist DEFAULT_SMS_DELIVERED_RINGTONE_URI:Landroid/net/Uri;

.field public static final whitelist DEFAULT_SMS_DELIVERED_SOUND_URI_SLOT_1:Landroid/net/Uri;

.field public static final whitelist DEFAULT_SMS_DELIVERED_SOUND_URI_SLOT_2:Landroid/net/Uri;

.field public static final whitelist DEFAULT_SMS_RECEIVED_RINGTONE_URI:Landroid/net/Uri;

.field public static final whitelist DEFAULT_SMS_RECEIVED_SOUND_URI_SLOT_1:Landroid/net/Uri;

.field public static final whitelist DEFAULT_SMS_RECEIVED_SOUND_URI_SLOT_2:Landroid/net/Uri;

.field public static final blacklist DEFAULT_TOUCH_SENSITIVE:Z = false

.field public static final blacklist DELETE_SOUND_EFFECT:Ljava/lang/String; = "delete_sound_effect"

.field public static final blacklist DELETE_SYSTEM_DIALER_PACKAGE:Ljava/lang/String; = "delete_system_dialer_package"

.field public static final blacklist DIAL_PAD_TOUCH_TONE:Ljava/lang/String; = "dial_pad_touch_tone"

.field public static final blacklist DIAL_PAD_TOUCH_TONE_DEFAULT:I = -0x1

.field public static final blacklist DIAL_PAD_TOUCH_TONE_HUMAN:I = 0x1

.field public static final blacklist DIAL_PAD_TOUCH_TONE_PIANO:I = 0x0

.field public static final blacklist DISABLE_WIFI_AUTO_CONNECT_SSID:Ljava/lang/String; = "disable_wifi_auto_connect_ssid"

.field public static final blacklist DRIVE_MODE_CALLING_AUTO_SMS_REPLY:Ljava/lang/String; = "drive_mode_calling_auto_sms_reply"

.field public static final blacklist DRIVE_MODE_DRIVE_MODE:Ljava/lang/String; = "drive_mode_drive_mode"

.field public static final blacklist DRIVE_MODE_INVERT_STOP_REPORT:Ljava/lang/String; = "drive_mode_invert_stop_report"

.field public static final blacklist DRIVE_MODE_ONLY_CONTACT_REPLY:Ljava/lang/String; = "drive_mode_only_contact_reply"

.field public static final blacklist DRIVE_MODE_PHONE_REPORT:Ljava/lang/String; = "drive_mode_phone_report"

.field public static final blacklist DRIVE_MODE_SMS_AUTO_REPLY_CONTENT:Ljava/lang/String; = "drive_mode_sms_auto_reply_content"

.field public static final blacklist DRIVE_MODE_SMS_AUTO_SMS_REPLY:Ljava/lang/String; = "drive_mode_sms_auto_sms_reply"

.field public static final blacklist DRIVE_MODE_SMS_REPORT:Ljava/lang/String; = "drive_mode_sms_report"

.field public static final blacklist EDGE_HANDGRIP_MODE:Ljava/lang/String; = "edge_handgrip"

.field public static final blacklist EDGE_HANDGRIP_MODE_BACK:Ljava/lang/String; = "edge_handgrip_back"

.field public static final blacklist EDGE_HANDGRIP_MODE_CLEAN:Ljava/lang/String; = "edge_handgrip_clean"

.field public static final blacklist EDGE_HANDGRIP_MODE_PHOTO:Ljava/lang/String; = "edge_handgrip_photo"

.field public static final blacklist EDGE_HANDGRIP_MODE_SCREENSHOT:Ljava/lang/String; = "edge_handgrip_screenshot"

.field public static final blacklist ENABLE_AUTO_DISABLE_SCREEN_ROTATION:Ljava/lang/String; = "enable_auto_disable_screen_rotation"

.field public static final blacklist ENABLE_DEMO_MODE:Ljava/lang/String; = "enable_demo_mode"

.field public static final blacklist ENABLE_SCREEN_ON_PROXIMITY_SENSOR:Ljava/lang/String; = "enable_screen_on_proximity_sensor"

.field public static final blacklist ENABLE_SNAPSHOT_SCREENLOCK:Ljava/lang/String; = "enable_snapshot_screenlock"

.field public static final blacklist ENABLE_SNAPSHOT_SCREENLOCK_DEFAULT:I = 0x0

.field public static final blacklist ENABLE_TELOCATION:Ljava/lang/String; = "enable_telocation"

.field public static final blacklist ENABLE_TELOCATION_DEFAULT:I = 0x1

.field public static final blacklist ENHANCED_WIFI_HANDOVER_ENABLED:Ljava/lang/String; = "enhanced_wifi_handover_enabled"

.field public static final blacklist ESCAPE_OPTION:Ljava/lang/String; = "escape_option"

.field public static final blacklist EXTERNAL_DISPLAY_CONNECTED:Ljava/lang/String; = "external_display_connected"

.field public static final blacklist FINGERPRINT_NAV_ACTION_HOME:I = 0x1

.field public static final blacklist FINGERPRINT_NAV_ACTION_NONE:I = 0x0

.field public static final blacklist FINGERPRINT_NAV_CENTER_ACTION:Ljava/lang/String; = "fingerprint_nav_center_action"

.field public static final blacklist FLASH_WHEN_RING_ENABLED:Ljava/lang/String; = "flash_when_ring_enabled"

.field public static final blacklist FLASH_WHEN_RING_ENABLED_DEFAULT:Z = false

.field public static final blacklist GESTURE_WAKEUP_MODE:Ljava/lang/String; = "gesture_wakeup"

.field public static final blacklist GESTURE_WAKEUP_OPTION:Ljava/lang/String; = "gesture_wakeup_option"

.field public static final blacklist GLOVE_MODE_SETTINGS:Ljava/lang/String; = "glove_mode_settings"

.field public static final blacklist HANDY_MODE_ENTER_DIRECT:Ljava/lang/String; = "handy_mode_enter_direct"

.field public static final blacklist HANDY_MODE_SIZE:Ljava/lang/String; = "handy_mode_size"

.field public static final blacklist HANDY_MODE_STATE:Ljava/lang/String; = "handy_mode_state"

.field public static final whitelist HAPTIC_FEEDBACK_LEVEL:Ljava/lang/String; = "haptic_feedback_level"

.field public static final whitelist HAPTIC_FEEDBACK_LEVEL_DEFAULT:I

.field public static final whitelist HAPTIC_FEEDBACK_LEVEL_MAX:I = 0x2

.field public static final whitelist HAPTIC_FEEDBACK_LEVEL_MIN:I = 0x0

.field public static final blacklist HAS_DELETE_SOUND_EFFECT_DEFAULT:Z = true

.field public static final whitelist HAS_FOLLOWED_MIPUB:Ljava/lang/String; = "has_followed_mipub"

.field public static final blacklist HAS_SCREENSHOT_SOUND:Ljava/lang/String; = "has_screenshot_sound"

.field public static final blacklist HAS_SCREENSHOT_SOUND_DEFAULT:Z = true

.field public static final blacklist HIGH_TEMPERATURE_STATE:Ljava/lang/String; = "high_temperature_state"

.field public static final whitelist HIGH_TEMPERATURE_STATE_OFF:I = 0x0

.field public static final whitelist HIGH_TEMPERATURE_STATE_ON:I = 0x1

.field public static final blacklist HOTSOPT_80211AX_SUPPORT:Ljava/lang/String; = "hotspot_80211ax_support"

.field public static final blacklist HOTSOPT_80211AX_SUPPORT_TEMP:Ljava/lang/String; = "hotspot_80211ax_support_temp"

.field public static final blacklist HOTSOPT_MAC_BLACK_SET:Ljava/lang/String; = "hotspot_mac_black_set"

.field public static final blacklist HOTSOPT_MAX_STATION_NUM:Ljava/lang/String; = "hotspot_max_station_num"

.field public static final blacklist HOTSOPT_VENDOR_SPECIFIC:Ljava/lang/String; = "hotspot_vendor_specific"

.field public static final blacklist INCALL_LIGHT_TURN_ON:Ljava/lang/String; = "incall_light_turn_on"

.field public static final blacklist IS_FOLD_DEVICE:Z

.field public static final whitelist IS_P2P1_SSID_CHANGED:Ljava/lang/String; = "is_p2p1_ssid_changed"

.field public static final whitelist IS_P2P1_SSID_CHANGED_DEFAULT:I = 0x0

.field public static final blacklist IS_SECURITY_ENCRYTPION_ENABLED:Ljava/lang/String; = "is_security_encryption_enabled"

.field public static final blacklist IS_SHOW_THREE_GESTURE_ALERT:Ljava/lang/String; = "is_show_three_gesture_alert"

.field public static final blacklist KEEP_LAUNCHER_IN_MEMORY:Ljava/lang/String; = "keep_launcher_in_memory"

.field public static final blacklist KEEP_LAUNCHER_IN_MEMORY_DEFAULT:I = 0x1

.field public static final blacklist KEYGUARD_DISABLE_POWER_KEY_LONG_PRESS:Ljava/lang/String; = "keyguard_disable_power_key_long_press"

.field public static final blacklist KEYGUARD_DISABLE_POWER_KEY_LONG_PRESS_DEFAULT:I = 0x0

.field public static final blacklist KEYGUARD_LEFT_FUNCTION_CHOOSER:Ljava/lang/String; = "keyguard_left_function_chooser"

.field public static final blacklist KEYGUARD_LEFT_FUNCTION_ENABLED:Ljava/lang/String; = "keyguard_left_function_enabled"

.field public static final blacklist KEYGUARD_RIGHT_FUNCTION_CHOOSER:Ljava/lang/String; = "keyguard_right_function_chooser"

.field public static final blacklist KEYGUARD_RIGHT_FUNCTION_ENABLED:Ljava/lang/String; = "keyguard_right_function_enabled"

.field public static final blacklist KEY_AUTO_DISABLE_SCREEN_BUTTON:Ljava/lang/String; = "auto_disable_screen_button"

.field public static final blacklist KEY_CLOSE_LID_DISPLAY_SETTING:Ljava/lang/String; = "close_lid_display_setting"

.field public static final blacklist KEY_COMMON_PASSWORD_CHILDRENMODE:Ljava/lang/String; = "childrenmode"

.field public static final blacklist KEY_COMMON_PASSWORD_KEYGUARD:Ljava/lang/String; = "miui_keyguard"

.field public static final blacklist KEY_FOLD_GESTURE_ANGLE_THRESHOLD:Ljava/lang/String; = "fold_gesture_angle_threshold"

.field public static final blacklist KEY_FUNCTION_LIMIT_SWITCH:Ljava/lang/String; = "persist.sys.func_limit_switch"

.field public static final blacklist KEY_IN_SMALL_WINDOW_MODE:Ljava/lang/String; = "is_small_window"
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation
.end field

.field public static final blacklist KEY_MIDROP_ENABLED:Ljava/lang/String; = "key_midrop_enabled"

.field public static final blacklist KEY_SECURITY_CENTER_ALLOW_CONNECT_NETWORK:Ljava/lang/String; = "persist.sys.sc_allow_conn"

.field public static final blacklist KEY_TOUCH_ASSISTANT_ENABLED:Ljava/lang/String; = "touch_assistant_enabled"

.field public static final blacklist KEY_TOUCH_ASSISTANT_SHOW_ON_KEYGUARD:Ljava/lang/String; = "touch_assistant_show_on_keyguard"

.field public static final blacklist KEY_TOUCH_ASSISTANT_TEMPORARY:Ljava/lang/String; = "touch_assistant_temporary"

.field public static final blacklist KEY_WAKEUP_FOR_KEYGUARD_NOTIFICATION:Ljava/lang/String; = "wakeup_for_keyguard_notification"

.field public static final blacklist LAST_AUDIBLE_RING_VOLUME:Ljava/lang/String; = "last_audible_ring_volume"

.field public static final whitelist LAST_VALID_DEVICE_ID:Ljava/lang/String; = "last_valid_device_id"

.field public static final blacklist LINK_TURBO_CUSTOMIZE:I = 0x1

.field public static final blacklist LINK_TURBO_DEFAULT:I = -0x1

.field public static final blacklist LINK_TURBO_OPTION:Ljava/lang/String; = "link_turbo_option"

.field public static final blacklist LINK_TURBO_RECOMMENDATION:I = 0x0

.field public static final blacklist LOCAL_BACKUP_DISABLE_SERVICE:Ljava/lang/String; = "local_backup_disable_service"

.field public static final blacklist LOCAL_SEA_LEVEL_PRESSURE:Ljava/lang/String; = "persist.sea_level_pres"

.field public static final blacklist LOCKED_APPS:Ljava/lang/String; = "locked_apps"

.field public static final blacklist MEMORY_LOW_THRESHOLD_PROPERTY:Ljava/lang/String; = "sys.memory.threshold.low"

.field public static final blacklist MIUI_ACCOUNT_LOGIN_CHECK:Ljava/lang/String; = "miui_account_login_check"

.field public static final blacklist MIUI_DESKTOP_MODE:Ljava/lang/String; = "miui_dkt_mode"

.field public static final blacklist MIUI_DESKTOP_SWITCH_COLLECT_DEFER:Ljava/lang/String; = "miui_dkt_switch_collect_defer"

.field public static final blacklist MIUI_HOME_ENABLE_AUTO_FILL_EMPTY_CELLS:Ljava/lang/String; = "miui_home_enable_auto_fill_empty_cells"

.field public static final blacklist MIUI_HOME_LOCK_SCREEN_CELLS:Ljava/lang/String; = "miui_home_lock_screen_cells"

.field public static final blacklist MIUI_HOME_SCREEN_CELLS_SIZE:Ljava/lang/String; = "miui_home_screen_cells_size"

.field public static final blacklist MIUI_PERMISSION_CHECK:Ljava/lang/String; = "miui_permission_check"

.field public static final blacklist MIUI_POPUP_GESTURE_CHECK:Ljava/lang/String; = "miui_popup_gesture_check"

.field public static final blacklist MIUI_POPUP_LED_CHECK:Ljava/lang/String; = "miui_popup_led_check"

.field public static final blacklist MIUI_POPUP_LED_DEFAULT:I = 0x0

.field public static final blacklist MIUI_POPUP_LED_INDEX:Ljava/lang/String; = "miui_popup_led_index"

.field public static final blacklist MIUI_POPUP_SOUND_CHECK:Ljava/lang/String; = "miui_popup_sound_check"

.field public static final blacklist MIUI_POPUP_SOUND_DEFAULT:I = 0x0

.field public static final blacklist MIUI_POPUP_SOUND_INDEX:Ljava/lang/String; = "miui_popup_sound_index"

.field public static final blacklist MIUI_RECENTS_PRIVACY_THUMBNAIL_BLUR:Ljava/lang/String; = "miui_recents_privacy_thumbnail_blur"

.field public static final blacklist MIUI_RECENTS_SHOW_MEM_INFO:Ljava/lang/String; = "miui_recents_show_mem_info"

.field public static final blacklist MIUI_RECENTS_SHOW_RECOMMEND:Ljava/lang/String; = "miui_recents_show_recommend"

.field public static final blacklist MIUI_SLIDER_COVER_STATUS:Ljava/lang/String; = "sc_status"

.field public static final blacklist MIUI_SLIDER_HISTORY_COUNT:Ljava/lang/String; = "miui_slider_history_count"

.field public static final blacklist MIUI_SLIDER_LAUNCH_PKG:Ljava/lang/String; = "miui_slider_launch_pkg"

.field public static final blacklist MIUI_SLIDER_SOUND_CHECK:Ljava/lang/String; = "miui_slider_sound_check"

.field public static final blacklist MIUI_SLIDER_SOUND_CLOSE:Ljava/lang/String; = "miui_slider_sound_close"

.field public static final blacklist MIUI_SLIDER_SOUND_DEFAULT:I = 0x0

.field public static final blacklist MIUI_SLIDER_SOUND_INDEX:Ljava/lang/String; = "miui_slider_sound_index"

.field public static final blacklist MIUI_SLIDER_SOUND_ONLINE:I = -0x1

.field public static final blacklist MIUI_SLIDER_SOUND_OPEN:Ljava/lang/String; = "miui_slider_sound_open"

.field public static final blacklist MIUI_SLIDER_TOOL_CHOICE:Ljava/lang/String; = "miui_slider_tool_choice"

.field public static final blacklist MIUI_SLIDER_TOOL_DRAWER:I = 0x2

.field public static final blacklist MIUI_SLIDER_TOOL_LAUNCH_APP:I = 0x3

.field public static final blacklist MIUI_SLIDER_TOOL_NONE:I = 0x0

.field public static final blacklist MIUI_SLIDER_TOOL_SELFIE:I = 0x1

.field public static final blacklist MIUI_SLIDER_VIDEO_BOX:Ljava/lang/String; = "gb_videobox"

.field public static final blacklist MMS_BREATHING_LIGHT_COLOR:Ljava/lang/String; = "mms_breathing_light_color"

.field public static final blacklist MMS_BREATHING_LIGHT_FREQ:Ljava/lang/String; = "mms_breathing_light_freq"

.field public static final blacklist MMS_PRIVATE_ADDRESS_MARKER:Ljava/lang/String; = "mms_private_address_marker"

.field public static final blacklist MMS_SYNC_WILD_MSG_STATE:Ljava/lang/String; = "mms_sync_wild_msg_state"

.field public static final blacklist MMS_SYNC_WILD_MSG_STATE_DONE:I = 0x3

.field public static final blacklist MMS_SYNC_WILD_MSG_STATE_DOWNLOAD_PENDING:I = 0x2

.field public static final blacklist MMS_SYNC_WILD_MSG_STATE_INIT:I = 0x0

.field public static final blacklist MMS_SYNC_WILD_MSG_STATE_MSG_FOUND:I = 0x1

.field public static final blacklist MMS_SYNC_WILD_MSG_STATE_UPGRADE:I = 0x4

.field public static final blacklist MMS_SYNC_WILD_MSG_STATE_UPGRADE_SIM:I = 0x5

.field public static final blacklist MMS_SYNC_WILD_NUMBERS:Ljava/lang/String; = "mms_sync_wild_numbers"

.field public static final blacklist MMS_THREAD_MARKER:Ljava/lang/String; = "mms_thread_marker"

.field public static final blacklist MMS_UPLOAD_OLD_MSG_ACCOUNTS:Ljava/lang/String; = "mms_upload_old_msg_accounts"

.field public static final blacklist MMS_UPLOAD_OLD_MSG_STATE:Ljava/lang/String; = "mms_upload_old_msg_state"

.field public static final blacklist MMS_UPLOAD_OLD_MSG_STATE_INIT:I = 0x0

.field public static final blacklist MMS_UPLOAD_OLD_MSG_STATE_NEED_PROMPT:I = 0x1

.field public static final blacklist NEED_RESET_SCREEN_OFF_TIMEOUT:Ljava/lang/String; = "need_reset_screen_off_timeout"

.field public static final blacklist NETWORK_TRAFFIC_POLICY_MODE_CLOSED:I = 0x0

.field public static final blacklist NETWORK_TRAFFIC_POLICY_MODE_FAST:I = 0x2

.field public static final blacklist NETWORK_TRAFFIC_POLICY_MODE_NORMAL:I = 0x1

.field public static final blacklist NEW_NUMERIC_PASSWORD_TYPE:Ljava/lang/String; = "new_numeric_password_type"

.field public static final blacklist NEXT_ALARM_CLOCK_FORMATTED:Ljava/lang/String; = "next_alarm_clock_formatted"

.field public static final whitelist NOTES_ALERT:Ljava/lang/String; = "notes_alert"

.field public static final blacklist NOTES_ALERT_CACHE:Ljava/lang/String; = "notes_alert_cache"

.field public static final blacklist NOTES_ALERT_CACHE_URI:Landroid/net/Uri;

.field public static final blacklist NOTIFICATION_STYLE_GOOGLE:I = 0x1

.field public static final blacklist NOTIFICATION_STYLE_MIUI:I = 0x0

.field public static final blacklist OPERATOR_WIFI_EAP_METHOD:Ljava/lang/String; = "operator_wifi_eap_method"

.field public static final blacklist PACKAGE_DELETE_BY_RESTORE_PHONE:Ljava/lang/String; = "package_delete_by_restore_phone"

.field public static final blacklist PERSIST_SYS_LINE_BREAKING:Ljava/lang/String; = "persist.sys.line_breaking"

.field public static final blacklist PICK_UP_GESTURE_WAKEUP_MODE:Ljava/lang/String; = "pick_up_gesture_wakeup_mode"

.field public static final blacklist PLUGIN_REFRESH_RATE:Ljava/lang/String; = "plugin_refresh_rate"

.field public static final blacklist POWERMODE_SUPERSAVE_OPEN:Ljava/lang/String; = "power_supersave_mode_open"

.field public static final blacklist POWER_MODE:Ljava/lang/String; = "power_mode"

.field public static final blacklist POWER_MODE_KEY_PROPERTY:Ljava/lang/String; = "persist.sys.aries.power_profile"

.field public static final blacklist POWER_MODE_VALUES:[Ljava/lang/String;

.field public static final blacklist POWER_MODE_VALUE_DEFAULT:Ljava/lang/String; = "middle"

.field public static final blacklist POWER_MODE_VALUE_HIGH:Ljava/lang/String; = "high"

.field public static final blacklist POWER_MODE_VALUE_LOW:Ljava/lang/String; = "low"

.field public static final blacklist POWER_MODE_VALUE_MIDDLE:Ljava/lang/String; = "middle"

.field public static final blacklist PRIVATE_SMS_NOTIFICATION_ENABLED:Ljava/lang/String; = "pref_key_enable_private_notification"

.field public static final blacklist PUBLIC_SETTINGS:Ljava/util/Set;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/Set<",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation
.end field

.field public static final blacklist PUBLIC_SETTINGS_OPEN:Ljava/util/Set;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/Set<",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation
.end field

.field public static final blacklist RANDOM_NOTE_MODE_MUTE_TIME_INTERVAL_MS:Ljava/lang/String; = "random_note_mode_mute_time_interval_ms"

.field public static final blacklist RANDOM_NOTE_MODE_RANDOM_SOUND_NUMBER:Ljava/lang/String; = "random_note_mode_random_sound_number"

.field public static final blacklist RANDOM_NOTE_MODE_SEQUENCE_SOUND_NUMBER:Ljava/lang/String; = "random_note_mode_sequence_sound_number"

.field public static final blacklist RANDOM_NOTE_MODE_SEQUENCE_TIME_INTERVAL_MS:Ljava/lang/String; = "random_note_mode_sequence_time_interval_ms"

.field public static final blacklist RECENT_APPS_KEY_SHOW:Ljava/lang/String; = "recent_apps_key_show"

.field public static final blacklist REMOTE_CONTROL_PACKAGE_NAME:Ljava/lang/String; = "remote_control_pkg_name"

.field public static final blacklist REMOTE_CONTROL_PROCESS_NAME:Ljava/lang/String; = "remote_control_proc_name"

.field public static final blacklist RESIDENT_ID:Ljava/lang/String; = "resident_id"

.field public static final blacklist RESIDENT_TIMEZONE:Ljava/lang/String; = "resident_timezone"

.field public static final whitelist RINGTONE_SOUND_SLOT_1:Ljava/lang/String; = "ringtone_sound_slot_1"

.field public static final blacklist RINGTONE_SOUND_SLOT_1_CACHE:Ljava/lang/String; = "ringtone_sound_slot_1_cache"

.field public static final blacklist RINGTONE_SOUND_SLOT_1_CACHE_URI:Landroid/net/Uri;

.field public static final whitelist RINGTONE_SOUND_SLOT_2:Ljava/lang/String; = "ringtone_sound_slot_2"

.field public static final blacklist RINGTONE_SOUND_SLOT_2_CACHE:Ljava/lang/String; = "ringtone_sound_slot_2_cache"

.field public static final blacklist RINGTONE_SOUND_SLOT_2_CACHE_URI:Landroid/net/Uri;

.field public static final blacklist RINGTONE_SOUND_USE_UNIFORM:Ljava/lang/String; = "ringtone_sound_use_uniform"

.field public static final blacklist SATELLITE_STATE:Ljava/lang/String; = "satellite_state"

.field public static final whitelist SCREENSHOT_NOTIFICATION_ENABLED:Ljava/lang/String; = "screenshot_notification_enabled"

.field public static final blacklist SCREEN_BUTTONS_TIMEOUT:Ljava/lang/String; = "screen_buttons_timeout"

.field public static final blacklist SCREEN_KEY_BACK:I = 0x3

.field public static final blacklist SCREEN_KEY_COUNT:I = 0x4

.field public static final blacklist SCREEN_KEY_HOME:I = 0x1

.field public static final blacklist SCREEN_KEY_LONG_PRESS_ACTION_CLOSE_APP:Ljava/lang/String; = "close_app"

.field public static final blacklist SCREEN_KEY_LONG_PRESS_ACTION_GOOGLE_NOW:Ljava/lang/String; = "google_now"

.field public static final blacklist SCREEN_KEY_LONG_PRESS_ACTION_NONE:Ljava/lang/String; = "none"

.field public static final blacklist SCREEN_KEY_LONG_PRESS_ACTION_QUICK_SEARCH:Ljava/lang/String; = "quick_search"

.field public static final blacklist SCREEN_KEY_LONG_PRESS_ACTION_RECENT_PANEL:Ljava/lang/String; = "recent_panel"

.field public static final blacklist SCREEN_KEY_LONG_PRESS_ACTION_SHOW_MENU:Ljava/lang/String; = "show_menu"

.field public static final blacklist SCREEN_KEY_LONG_PRESS_ACTION_VOICE_ASSISTANT:Ljava/lang/String; = "voice_assistant"

.field public static final blacklist SCREEN_KEY_LONG_PRESS_APP_SWITCH:Ljava/lang/String; = "screen_key_long_press_app_switch"

.field public static final blacklist SCREEN_KEY_LONG_PRESS_BACK:Ljava/lang/String; = "screen_key_long_press_back"

.field public static final blacklist SCREEN_KEY_LONG_PRESS_HOME:Ljava/lang/String; = "screen_key_long_press_home"

.field public static final blacklist SCREEN_KEY_LONG_PRESS_MENU:Ljava/lang/String; = "screen_key_long_press_menu"

.field public static final blacklist SCREEN_KEY_LONG_PRESS_TIMEOUT:Ljava/lang/String; = "screen_key_long_press_timeout"

.field public static final blacklist SCREEN_KEY_LONG_PRESS_TIMEOUT_DEFAULT:I = 0x1f4

.field public static final blacklist SCREEN_KEY_MENU:I = 0x0

.field public static final blacklist SCREEN_KEY_ORDER:Ljava/lang/String; = "screen_key_order"

.field public static final blacklist SCREEN_KEY_PRESS_APP_SWITCH:Ljava/lang/String; = "screen_key_press_app_switch"

.field public static final blacklist SCREEN_KEY_PRESS_APP_SWITCH_DEFAULT:Z = true

.field public static final blacklist SCREEN_KEY_RECENT_APPS:I = 0x2

.field public static final blacklist SCREEN_OFF_BY_LID_PROPERTY_STRING:Ljava/lang/String; = "sys.keyguard.screen_off_by_lid"

.field public static final blacklist SCREEN_OUTDOOR_MODE:Ljava/lang/String; = "outdoor_mode"

.field public static final whitelist SCREEN_OUTDOOR_MODE_OFF:I = 0x0

.field public static final whitelist SCREEN_OUTDOOR_MODE_ON:I = 0x1

.field public static final blacklist SCREEN_SUNLIGHT_MODE:Ljava/lang/String; = "sunlight_mode"

.field public static final whitelist SCREEN_SUNLIGHT_MODE_OFF:I = 0x0

.field public static final whitelist SCREEN_SUNLIGHT_MODE_ON:I = 0x1

.field public static final blacklist SHOW_LOCK_BEFORE_UNLOCK:Ljava/lang/String; = "show_lock_before_unlock"

.field public static final blacklist SHOW_LOCK_BEFORE_UNLOCK_DEFAULT:Z

.field public static final blacklist SHOW_ROUNDED_CORNERS:Ljava/lang/String; = "show_rounded_corners"

.field public static final blacklist SHUTDOWN_ALARM_CLOCK_OFFSET:Ljava/lang/String; = "shutdown_alarm_clock_offset"

.field private static final blacklist SIMPLE_MODE:Ljava/lang/String; = "simple_mode"

.field public static final blacklist SLAVE_WIFI_ON:Ljava/lang/String; = "slave_wifi_on"

.field public static final blacklist SLAVE_WIFI_SSID:Ljava/lang/String; = "slave_wifi_ssid"

.field public static final blacklist SMARTCOVER_DISABLED:I = 0x0
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation
.end field

.field public static final blacklist SMARTCOVER_FULL_MODE:I = 0x4
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation
.end field

.field public static final blacklist SMARTCOVER_GUIDE_KEY:Ljava/lang/String; = "smart_cover_key"
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation
.end field

.field public static final blacklist SMARTCOVER_LATTICE_MODE:I = 0x3
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation
.end field

.field public static final blacklist SMARTCOVER_MODE_DEFAULT_VALUE:I = -0x1
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation
.end field

.field public static final blacklist SMARTCOVER_MODE_KEY:Ljava/lang/String; = "persist.sys.smartcover_mode"
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation
.end field

.field public static final blacklist SMARTCOVER_NORMAL_MODE:I = 0x1
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation
.end field

.field public static final blacklist SMARTCOVER_SMALLWINDOW_MODE:I = 0x2
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation
.end field

.field public static final blacklist SMARTCOVER_SMALLWIN_TYPE:Ljava/lang/String; = "persist.sys.smallwin_type"
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation
.end field

.field public static final whitelist SMS_DELIVERED_SOUND:Ljava/lang/String; = "sms_delivered_sound"

.field public static final blacklist SMS_DELIVERED_SOUND_CACHE:Ljava/lang/String; = "sms_delivered_sound_cahce"

.field public static final blacklist SMS_DELIVERED_SOUND_CACHE_URI:Landroid/net/Uri;

.field public static final whitelist SMS_DELIVERED_SOUND_SLOT_1:Ljava/lang/String; = "sms_delivered_sound_slot_1"

.field public static final blacklist SMS_DELIVERED_SOUND_SLOT_1_CACHE:Ljava/lang/String; = "sms_delivered_sound_slot_1_cache"

.field public static final blacklist SMS_DELIVERED_SOUND_SLOT_1_CACHE_URI:Landroid/net/Uri;

.field public static final whitelist SMS_DELIVERED_SOUND_SLOT_2:Ljava/lang/String; = "sms_delivered_sound_slot_2"

.field public static final blacklist SMS_DELIVERED_SOUND_SLOT_2_CACHE:Ljava/lang/String; = "sms_delivered_sound_slot_2_cache"

.field public static final blacklist SMS_DELIVERED_SOUND_SLOT_2_CACHE_URI:Landroid/net/Uri;

.field public static final blacklist SMS_DELIVERED_SOUND_USE_UNIFORM:Ljava/lang/String; = "sms_delivered_sound_use_uniform"

.field public static final blacklist SMS_NOTIFICATION_BODY_ENABLED:Ljava/lang/String; = "pref_key_enable_notification_body"

.field public static final blacklist SMS_NOTIFICATION_ENABLED:Ljava/lang/String; = "pref_key_enable_notification"

.field public static final whitelist SMS_RECEIVED_SOUND:Ljava/lang/String; = "sms_received_sound"

.field public static final blacklist SMS_RECEIVED_SOUND_CACHE:Ljava/lang/String; = "sms_received_sound_cache"

.field public static final blacklist SMS_RECEIVED_SOUND_CACHE_URI:Landroid/net/Uri;

.field public static final whitelist SMS_RECEIVED_SOUND_SLOT_1:Ljava/lang/String; = "sms_received_sound_slot_1"

.field public static final blacklist SMS_RECEIVED_SOUND_SLOT_1_CACHE:Ljava/lang/String; = "sms_received_sound_slot_1_cache"

.field public static final blacklist SMS_RECEIVED_SOUND_SLOT_1_CACHE_URI:Landroid/net/Uri;

.field public static final whitelist SMS_RECEIVED_SOUND_SLOT_2:Ljava/lang/String; = "sms_received_sound_slot_2"

.field public static final blacklist SMS_RECEIVED_SOUND_SLOT_2_CACHE:Ljava/lang/String; = "sms_received_sound_slot_2_cache"

.field public static final blacklist SMS_RECEIVED_SOUND_SLOT_2_CACHE_URI:Landroid/net/Uri;

.field public static final blacklist SMS_RECEIVED_SOUND_USE_UNIFORM:Ljava/lang/String; = "sms_received_sound_use_uniform"

.field public static final blacklist SMS_WAKE_UP_SCREEN_ENABLED:Ljava/lang/String; = "pref_key_enable_wake_up_screen"

.field public static final blacklist SOFTAP_REPORTED_FREQUENCY:Ljava/lang/String; = "softap_reported_frequency"

.field public static final blacklist SOFTAP_WILL_RESTART:Ljava/lang/String; = "softap_will_restart"

.field public static final whitelist STATUS_BAR_COLLAPSE_AFTER_CLICKED:Ljava/lang/String; = "status_bar_collapse_after_clicked"

.field public static final blacklist STATUS_BAR_CUSTOM_CARRIER:Ljava/lang/String; = "status_bar_custom_carrier"

.field public static final whitelist STATUS_BAR_EXPANDABLE_UNDER_FULLSCREEN:Ljava/lang/String; = "status_bar_expandable_under_fullscreen"

.field public static final whitelist STATUS_BAR_EXPANDABLE_UNDER_KEYGUARD:Ljava/lang/String; = "status_bar_expandable_under_keyguard"

.field public static final blacklist STATUS_BAR_HIDE_ICON_SLOT_NAME:Ljava/lang/String; = "status_bar_hide_icon_slot_name"

.field public static final blacklist STATUS_BAR_IN_CALL_NOTIFICATION_FLOATING:Ljava/lang/String; = "status_bar_in_call_notification_floating"

.field public static final blacklist STATUS_BAR_NOTIFICATION_STYLE:Ljava/lang/String; = "status_bar_notification_style"

.field public static final blacklist STATUS_BAR_REAL_CARRIER:Ljava/lang/String; = "status_bar_real_carrier"

.field public static final blacklist STATUS_BAR_SHOW_CARRIER_UNDER_KEYGUARD:Ljava/lang/String; = "status_bar_show_carrier_under_keyguard"

.field public static final whitelist STATUS_BAR_SHOW_CUSTOM_CARRIER:Ljava/lang/String; = "status_bar_show_custom_carrier"

.field public static final whitelist STATUS_BAR_SHOW_NETWORK_ASSISTANT:Ljava/lang/String; = "status_bar_show_network_assistant"

.field public static final whitelist STATUS_BAR_SHOW_NETWORK_ASSISTANT_DEFAULT:I = 0x0

.field public static final whitelist STATUS_BAR_SHOW_NETWORK_SPEED:Ljava/lang/String; = "status_bar_show_network_speed"

.field public static final whitelist STATUS_BAR_SHOW_NETWORK_SPEED_DEFAULT:I = 0x0

.field public static final whitelist STATUS_BAR_SHOW_NOTIFICATION_ICON:Ljava/lang/String; = "status_bar_show_notification_icon"

.field public static final whitelist STATUS_BAR_SHOW_NOTIFICATION_ICON_DEFAULT:I = 0x7

.field public static final blacklist STATUS_BAR_STYLE:Ljava/lang/String; = "status_bar_style_type"

.field public static final blacklist STATUS_BAR_STYLE_DEFAULT:I = 0x0

.field public static final blacklist STATUS_BAR_STYLE_LIST:I = 0x0

.field public static final blacklist STATUS_BAR_STYLE_PAGE:I = 0x1

.field public static final blacklist STATUS_BAR_TOGGLE_LIST:Ljava/lang/String; = "status_bar_toggle_list_order_new"

.field public static final blacklist STATUS_BAR_TOGGLE_PAGE:Ljava/lang/String; = "status_bar_toggle_page_order"

.field public static final blacklist STATUS_BAR_UPDATE_NETWORK_SPEED_INTERVAL:Ljava/lang/String; = "status_bar_network_speed_interval"

.field public static final blacklist STATUS_BAR_UPDATE_NETWORK_SPEED_INTERVAL_DEFAULT:I = 0xfa0

.field public static final blacklist SUBSCREEN_GESTURE_WAKEUP_MODE:Ljava/lang/String; = "subscreen_gesture_wakeup"

.field public static final blacklist SUBSCREEN_SWITCH_MODE:Ljava/lang/String; = "subscreen_switch"

.field public static final blacklist SYSTEM_NEW_VERSION_FOUND:Ljava/lang/String; = "system_new_version_found"

.field public static final blacklist T9_INDEXING_KEY:Ljava/lang/String; = "t9_indexing_key"

.field public static final blacklist T9_INDEXING_KEY_PINYIN:I = 0x0

.field public static final blacklist T9_INDEXING_KEY_ZHUYIN:I = 0x1

.field public static final blacklist THERMAL_LIMIT_REFRESH_RATE:Ljava/lang/String; = "thermal_limit_refresh_rate"

.field public static final blacklist THREE_GESTURE_SCREENSHOT:Ljava/lang/String; = "three_gesture_screenshot"

.field public static final blacklist THREE_GESTURE_SCREENSHOT_DEFAULT:Z = false

.field public static final blacklist TORCH_STATE:Ljava/lang/String; = "torch_state"

.field public static final blacklist TOUCH_SENSITIVE:Ljava/lang/String; = "touch_sensitive"

.field public static final blacklist TRACKBALL_WAKE_SCREEN:Ljava/lang/String; = "trackball_wake_screen"

.field public static final blacklist UI_MODE_SCALE:Ljava/lang/String; = "ui_mode_scale"

.field public static final blacklist USER_GUIDE_LOCK_SCREEN_UNLOCK:Ljava/lang/String; = "user_guide_lock_screen_unlock"

.field public static final blacklist USER_GUIDE_STATUS_BAR_CALL:Ljava/lang/String; = "user_guide_status_bar_call"

.field public static final blacklist USER_GUIDE_STATUS_BAR_NOTIFICATION:Ljava/lang/String; = "user_guide_status_bar_notification"

.field public static final blacklist USER_GUIDE_STATUS_BAR_TOGGLE:Ljava/lang/String; = "user_guide_status_bar_toggle"

.field public static final blacklist USER_GUIDE_STATUS_BAR_TOGGLE_LIST:Ljava/lang/String; = "user_guide_status_bar_toggle_list"

.field public static final blacklist USER_NETWORK_PRIORITY_ENABLED:Ljava/lang/String; = "user_network_priority_enabled"

.field public static final blacklist USER_ROTATION_INNER:Ljava/lang/String; = "user_rotation_inner"

.field public static final blacklist USER_ROTATION_OUTER:Ljava/lang/String; = "user_rotation_outer"

.field public static final blacklist VIBRATE_IN_NORMAL:Ljava/lang/String; = "vibrate_in_normal"

.field public static final blacklist VIBRATE_IN_NORMAL_DEFAULT:Z

.field public static final whitelist VIBRATE_IN_SILENT:Ljava/lang/String; = "vibrate_in_silent"

.field public static final blacklist VIBRATE_IN_SILENT_DEFAULT:Z = true

.field public static final blacklist VIRTUAL_LASER:Ljava/lang/String; = "virtual_laser_switch"

.field public static final blacklist VOICEASSIST_INVERT_STOP_REPORT:Ljava/lang/String; = "voiceassist_invert_stop_report"

.field public static final blacklist VOICEASSIST_MENU_LONG_LAUNCH:Ljava/lang/String; = "voiceassist_menu_long_press_launch"

.field public static final blacklist VOICEASSIST_PHONE_BY_EAR_LAUNCH:Ljava/lang/String; = "voiceassist_phone_by_ear_launch"

.field public static final blacklist VOICEASSIST_PHONE_REPORT:Ljava/lang/String; = "voiceassist_phone_report"

.field public static final blacklist VOICEASSIST_REPORT_METHOD:Ljava/lang/String; = "voiceassist_report_method"

.field public static final blacklist VOICEASSIST_REPORT_OFF:I = 0x2

.field public static final blacklist VOICEASSIST_REPORT_ON:I = 0x1

.field public static final blacklist VOICEASSIST_REPORT_WIREDON:I = 0x0

.field public static final blacklist VOICEASSIST_SMS_REPORT:Ljava/lang/String; = "voiceassist_sms_report"

.field public static final blacklist VOLUMEKEY_WAKE_SCREEN:Ljava/lang/String; = "volumekey_wake_screen"

.field public static final blacklist WIFI_ASSISTANT:Ljava/lang/String; = "wifi_assistant"

.field public static final blacklist WIFI_ASSISTANT_DATA_PROMPT:Ljava/lang/String; = "wifi_assistant_data_prompt"

.field public static final blacklist WIFI_ASSISTANT_DATA_PROMPT_DEFAULT:I = 0x1

.field public static final blacklist WIFI_ASSISTANT_DEFAULT:I = 0x1

.field public static final blacklist WIFI_AUTO_DISABLE:Ljava/lang/String; = "wifi_auto_disable"

.field public static final blacklist WIFI_CONNECT_TYPE:Ljava/lang/String; = "wifi_connect_type"

.field public static final blacklist WIFI_CONNECT_TYPE_ASK:I = 0x2

.field public static final blacklist WIFI_CONNECT_TYPE_AUTO:I = 0x0

.field public static final blacklist WIFI_CONNECT_TYPE_MANUL:I = 0x1

.field public static final blacklist WIFI_DIALOG_REMIND_TYPE:Ljava/lang/String; = "wifi_dialog_remind_type"

.field public static final blacklist WIFI_DIALOG_REMIND_TYPE_CLOSE:I = 0x0

.field public static final blacklist WIFI_DIALOG_REMIND_TYPE_OPEN:I = 0x1

.field public static final blacklist WIFI_GENERATION:Ljava/lang/String; = "wifi_generation"

.field public static final blacklist WIFI_GENERATION_DEFAULT:I = 0x0

.field public static final blacklist WIFI_MASTER_KEY:Ljava/lang/String; = "wifi_master_key"

.field public static final blacklist WIFI_MASTER_KEY_DEFAULT:I = 0x1

.field public static final blacklist WIFI_PRIORITY_TYPE:Ljava/lang/String; = "wifi_priority_type"

.field public static final blacklist WIFI_PRIORITY_TYPE_DEFAULT:I = 0x0

.field public static final blacklist WIFI_PRIORITY_TYPE_MAMUAL:I = 0x1

.field public static final blacklist WIFI_SELECT_SSID_ASK:I = 0x2

.field public static final blacklist WIFI_SELECT_SSID_AUTO:I = 0x0

.field public static final blacklist WIFI_SELECT_SSID_MANUL:I = 0x1

.field public static final blacklist WIFI_SELECT_SSID_TYPE:Ljava/lang/String; = "wifi_select_ssid_type"

.field public static final blacklist WIFI_SHARE:Ljava/lang/String; = "wifi"

.field public static final whitelist WINDOW_TYPE_LAYER:Ljava/lang/String; = "window_type_layer"

.field public static final blacklist WIRELESS_COMPATIABLE_MODE:I = 0x0

.field public static final blacklist WIRELESS_CONNECT_MODE:Ljava/lang/String; = "wireless_compatible_mode"

.field public static final blacklist WIRELESS_HIGH_MODE:I = 0x1

.field private static final blacklist WORD_PHOTO:Ljava/lang/String; = "word_photo"

.field public static final whitelist XINGWANG_SATELLITE_STATE:Ljava/lang/String; = "xingwang_satellite_state"

.field public static blacklist screenKeys:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Ljava/lang/Integer;",
            ">;"
        }
    .end annotation
.end field


# direct methods
.method static constructor blacklist <clinit>()V
    .registers 11

    nop

    const-string v0, "persist.sys.muiltdisplay_type"

    const/4 v1, 0x0

    invoke-static {v0, v1}, Landroid/os/SystemProperties;->getInt(Ljava/lang/String;I)I

    move-result v0

    const/4 v2, 0x1

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    const/4 v4, 0x2

    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v5

    if-ne v0, v4, :cond_0

    move v0, v2

    goto :goto_0

    :cond_0
    move v0, v1

    :goto_0
    sput-boolean v0, Landroid/provider/MiuiSettings$System;->IS_FOLD_DEVICE:Z

    const-string v0, "ro.haptic.default_level"

    invoke-static {v0, v2}, Landroid/os/SystemProperties;->getInt(Ljava/lang/String;I)I

    move-result v0

    sput v0, Landroid/provider/MiuiSettings$System;->HAPTIC_FEEDBACK_LEVEL_DEFAULT:I

    sget-boolean v0, Lmiui/os/Build;->IS_CM_CUSTOMIZATION_TEST:Z

    if-nez v0, :cond_1

    invoke-static {}, Lmiui/util/HapticFeedbackUtil;->isSupportLinearMotorVibrate()Z

    move-result v0

    if-eqz v0, :cond_2

    :cond_1
    move v1, v2

    :cond_2
    sput-boolean v1, Landroid/provider/MiuiSettings$System;->VIBRATE_IN_NORMAL_DEFAULT:Z

    sget-boolean v0, Lmiui/os/Build;->IS_CM_CUSTOMIZATION_TEST:Z

    xor-int/2addr v0, v2

    sput-boolean v0, Landroid/provider/MiuiSettings$System;->SHOW_LOCK_BEFORE_UNLOCK_DEFAULT:Z

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    sput-object v0, Landroid/provider/MiuiSettings$System;->screenKeys:Ljava/util/ArrayList;

    invoke-static {}, Landroid/provider/MiuiSettings;->-$$Nest$sfgetIS_JP_SOFTBANK()Z

    move-result v0

    const/4 v1, 0x3

    if-eqz v0, :cond_3

    sget-object v0, Landroid/provider/MiuiSettings$System;->screenKeys:Ljava/util/ArrayList;

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->screenKeys:Ljava/util/ArrayList;

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->screenKeys:Ljava/util/ArrayList;

    invoke-virtual {v0, v5}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_1

    :cond_3
    sget-object v0, Landroid/provider/MiuiSettings$System;->screenKeys:Ljava/util/ArrayList;

    invoke-virtual {v0, v5}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->screenKeys:Ljava/util/ArrayList;

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->screenKeys:Ljava/util/ArrayList;

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :goto_1
    const-string v0, "high"

    const-string v1, "middle"

    filled-new-array {v0, v1}, [Ljava/lang/String;

    move-result-object v0

    sput-object v0, Landroid/provider/MiuiSettings$System;->POWER_MODE_VALUES:[Ljava/lang/String;

    invoke-static {}, Landroid/content/res/Resources;->getSystem()Landroid/content/res/Resources;

    move-result-object v0

    const v1, 0x11060002

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getColor(I)I

    move-result v0

    sput v0, Landroid/provider/MiuiSettings$System;->CALL_BREATHING_LIGHT_COLOR_DEFAULT:I

    invoke-static {}, Landroid/content/res/Resources;->getSystem()Landroid/content/res/Resources;

    move-result-object v0

    const v1, 0x110b0015

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getInteger(I)I

    move-result v0

    sput v0, Landroid/provider/MiuiSettings$System;->CALL_BREATHING_LIGHT_FREQ_DEFAULT:I

    nop

    const-string v0, "calendar_alert"

    invoke-static {v0}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    sput-object v1, Landroid/provider/MiuiSettings$System;->DEFAULT_CALENDAR_ALERT_URI:Landroid/net/Uri;

    nop

    const-string v1, "calendar_alert_cache"

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    sput-object v1, Landroid/provider/MiuiSettings$System;->CALENDAR_ALERT_CACHE_URI:Landroid/net/Uri;

    nop

    const-string v1, "notes_alert"

    invoke-static {v1}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v2

    sput-object v2, Landroid/provider/MiuiSettings$System;->DEFAULT_NOTES_ALERT_URI:Landroid/net/Uri;

    nop

    const-string v2, "notes_alert_cache"

    invoke-static {v2}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v2

    sput-object v2, Landroid/provider/MiuiSettings$System;->NOTES_ALERT_CACHE_URI:Landroid/net/Uri;

    nop

    const-string v2, "sms_received_sound_cache"

    invoke-static {v2}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v2

    sput-object v2, Landroid/provider/MiuiSettings$System;->SMS_RECEIVED_SOUND_CACHE_URI:Landroid/net/Uri;

    nop

    const-string v2, "sms_received_sound"

    invoke-static {v2}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v3

    sput-object v3, Landroid/provider/MiuiSettings$System;->DEFAULT_SMS_RECEIVED_RINGTONE_URI:Landroid/net/Uri;

    nop

    const-string v3, "sms_delivered_sound_cahce"

    invoke-static {v3}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v3

    sput-object v3, Landroid/provider/MiuiSettings$System;->SMS_DELIVERED_SOUND_CACHE_URI:Landroid/net/Uri;

    nop

    const-string v3, "sms_delivered_sound"

    invoke-static {v3}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v3

    sput-object v3, Landroid/provider/MiuiSettings$System;->DEFAULT_SMS_DELIVERED_RINGTONE_URI:Landroid/net/Uri;

    nop

    const-string v3, "ringtone_sound_slot_1"

    invoke-static {v3}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    sput-object v4, Landroid/provider/MiuiSettings$System;->DEFAULT_RINGTONE_URI_SLOT_1:Landroid/net/Uri;

    nop

    const-string v4, "ringtone_sound_slot_2"

    invoke-static {v4}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    sput-object v5, Landroid/provider/MiuiSettings$System;->DEFAULT_RINGTONE_URI_SLOT_2:Landroid/net/Uri;

    nop

    const-string v5, "sms_received_sound_slot_1"

    invoke-static {v5}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v6

    sput-object v6, Landroid/provider/MiuiSettings$System;->DEFAULT_SMS_RECEIVED_SOUND_URI_SLOT_1:Landroid/net/Uri;

    nop

    const-string v6, "sms_received_sound_slot_2"

    invoke-static {v6}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v7

    sput-object v7, Landroid/provider/MiuiSettings$System;->DEFAULT_SMS_RECEIVED_SOUND_URI_SLOT_2:Landroid/net/Uri;

    nop

    const-string v7, "sms_delivered_sound_slot_1"

    invoke-static {v7}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v7

    sput-object v7, Landroid/provider/MiuiSettings$System;->DEFAULT_SMS_DELIVERED_SOUND_URI_SLOT_1:Landroid/net/Uri;

    nop

    const-string v7, "sms_delivered_sound_slot_2"

    invoke-static {v7}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v7

    sput-object v7, Landroid/provider/MiuiSettings$System;->DEFAULT_SMS_DELIVERED_SOUND_URI_SLOT_2:Landroid/net/Uri;

    const-string v7, "ringtone_sound_slot_1_cache"

    invoke-static {v7}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v7

    sput-object v7, Landroid/provider/MiuiSettings$System;->RINGTONE_SOUND_SLOT_1_CACHE_URI:Landroid/net/Uri;

    const-string v7, "ringtone_sound_slot_2_cache"

    invoke-static {v7}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v7

    sput-object v7, Landroid/provider/MiuiSettings$System;->RINGTONE_SOUND_SLOT_2_CACHE_URI:Landroid/net/Uri;

    const-string v7, "sms_received_sound_slot_1_cache"

    invoke-static {v7}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v7

    sput-object v7, Landroid/provider/MiuiSettings$System;->SMS_RECEIVED_SOUND_SLOT_1_CACHE_URI:Landroid/net/Uri;

    const-string v7, "sms_received_sound_slot_2_cache"

    invoke-static {v7}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v7

    sput-object v7, Landroid/provider/MiuiSettings$System;->SMS_RECEIVED_SOUND_SLOT_2_CACHE_URI:Landroid/net/Uri;

    const-string v7, "sms_delivered_sound_slot_1_cache"

    invoke-static {v7}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v7

    sput-object v7, Landroid/provider/MiuiSettings$System;->SMS_DELIVERED_SOUND_SLOT_1_CACHE_URI:Landroid/net/Uri;

    const-string v7, "sms_delivered_sound_slot_2_cache"

    invoke-static {v7}, Landroid/provider/Settings$System;->getUriFor(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v7

    sput-object v7, Landroid/provider/MiuiSettings$System;->SMS_DELIVERED_SOUND_SLOT_2_CACHE_URI:Landroid/net/Uri;

    new-instance v7, Landroid/util/ArraySet;

    invoke-direct {v7}, Landroid/util/ArraySet;-><init>()V

    sput-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-call_log-0"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-call_log-1"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "setting_last_time_alert_call_log"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-wifi-0"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-wifi-1"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "setting_last_time_alert_wifi"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-com.miui.gallery.cloud.provider-0"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-com.miui.gallery.cloud.provider-1"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "setting_last_time_alert_com.miui.gallery.cloud.provider"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-records-0"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-records-1"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "setting_last_time_alert_records"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-com.android.calendar-0"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-com.android.calendar-1"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "setting_last_time_alert_com.android.calendar"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-notes-0"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-notes-1"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "setting_last_time_alert_notes"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-sms-0"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-sms-1"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "setting_last_time_alert_sms"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-com.android.contacts-0"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-com.android.contacts-1"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "setting_last_time_alert_com.android.contacts"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-com.miui.browser-0"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-com.miui.browser-1"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "setting_last_time_alert_com.miui.browser"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-antispam-0"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-antispam-1"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "setting_last_time_alert_antispam"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-com.miui.player-0"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "sync_for_sim_com.xiaomi-com.miui.player-1"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "setting_last_time_alert_com.miui.player"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "com.xiaomi.opensdk.pdc.host"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "micloud_network_availability"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "micloud_hosts"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "micloud_accountname"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "micloud_hosts_v2"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "micloud_accountname_v2"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "micloud_updatehosts_third_party"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "micloud_gdpr_permission_granted"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "mms_sync_wild_msg_state"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "mms_sync_wild_numbers"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "mms_upload_old_msg_state"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "mms_upload_old_msg_accounts"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "mms_thread_marker"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "mms_private_address_marker"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "miprofile.settings.miprofile_user_notice"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "miprofile.settings.miprofile_badge_notice"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "miprofile.settings.miprofile_set"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "miprofile.settings.miprofile_on"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "miprofile.settings.miprofile_visible"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "debug_switch"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "debug_dp_path"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "xunlei_token"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "vip_token"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "xunlei_usage_permission"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "default_alarm_alert"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "next_alarm_clock_formatted"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "shutdown_alarm_clock_offset"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "voiceassist_report_method"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "voiceassist_phone_report"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "voiceassist_sms_report"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "last_valid_device_id"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v7, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v8, "lock_wallpaper_provider_authority"

    invoke-interface {v7, v8}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    const-string v7, "clock_changed_time_"

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    new-instance v9, Ljava/lang/StringBuilder;

    invoke-direct {v9}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v9, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    const-string v10, "1x2"

    invoke-virtual {v9, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v9

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    new-instance v9, Ljava/lang/StringBuilder;

    invoke-direct {v9}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v9, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    const-string v10, "2x2"

    invoke-virtual {v9, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v9

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    new-instance v9, Ljava/lang/StringBuilder;

    invoke-direct {v9}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v9, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    const-string v10, "2x4"

    invoke-virtual {v9, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v9

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    new-instance v9, Ljava/lang/StringBuilder;

    invoke-direct {v9}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v9, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    const-string v10, "4x4"

    invoke-virtual {v9, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v9

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    new-instance v9, Ljava/lang/StringBuilder;

    invoke-direct {v9}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v9, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    const-string v10, "3x4"

    invoke-virtual {v9, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v9

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "pref_key_wallpaper_screen_span"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "com.xiaomi.market.enable_share_progress_status"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "com.miui.home.enable_share_progress_status"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "com.xiaomi.discover.enable_share_progress_status"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "com.xiaomi.mipicks.enable_share_progress_status"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "com.xiaomi.market.enable_app_chooser_recommend"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "com.xiaomi.discover.auto_update_enabled"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "com.xiaomi.discover.metered_update_answered"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "com.xiaomi.discover.metered_update_confirm_needed_by_region"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "com.xiaomi.discover.metered_system_update_confirm_needed_by_region"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "com.xiaomi.mipicks.need_show_user_guide_status"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "touch_assistant_enabled"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "touch_assistant_show_on_keyguard"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v9, "frequent_phrases"

    invoke-interface {v8, v9}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    invoke-interface {v8, v3}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    invoke-interface {v8, v4}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    invoke-interface {v8, v2}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    invoke-interface {v8, v5}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    invoke-interface {v8, v6}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v8, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    invoke-interface {v8, v0}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "updatable_system_app_count"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "show_touches"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "handy_mode_state"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "long_press_power_launch_xiaoai"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "send_back_when_xiaoai_appear"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "xiaoai_power_guide"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "xiaoai_recognize_gesture_type"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "content_catcher_network_enabled_content_extension"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "support_long_press_mode"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "long_press_power_launch_smarthome"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "settings_uwb_control_center_shortcut_open"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "settings_uwb_lock_screen_entrance_open"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "double_click_power_key"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "drive_mode_drive_mode"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "ai_preload_user_state"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "auto_dual_clock"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "resident_id"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "resident_timezone"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "random_note_mode_random_sound_number"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "random_note_mode_sequence_sound_number"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "random_note_mode_sequence_time_interval_ms"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "random_note_mode_mute_time_interval_ms"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    const-string v1, "power_supersave_mode_open"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    new-instance v0, Landroid/util/ArraySet;

    invoke-direct {v0}, Landroid/util/ArraySet;-><init>()V

    sput-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS_OPEN:Ljava/util/Set;

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS_OPEN:Ljava/util/Set;

    const-string v1, "ringtone_sound_use_uniform"

    invoke-interface {v0, v1}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS_OPEN:Ljava/util/Set;

    invoke-interface {v0, v3}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS_OPEN:Ljava/util/Set;

    invoke-interface {v0, v4}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS_OPEN:Ljava/util/Set;

    invoke-interface {v0, v2}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS_OPEN:Ljava/util/Set;

    invoke-interface {v0, v5}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS_OPEN:Ljava/util/Set;

    invoke-interface {v0, v6}, Ljava/util/Set;->add(Ljava/lang/Object;)Z

    return-void
.end method

.method public constructor whitelist <init>()V
    .registers 1

    invoke-direct {p0}, Landroid/provider/SystemSettings$System;-><init>()V

    return-void
.end method

.method public static blacklist belongToCrossXSpaceSettings(Ljava/lang/String;I)Z
    .registers 3

    invoke-static {p1}, Lmiui/securityspace/XSpaceUserHandle;->isXSpaceUserId(I)Z

    move-result v0

    if-eqz v0, :cond_0

    sget-object v0, Landroid/provider/MiuiSettings;->CROSS_PROFILE_SETTINGS:Ljava/util/Set;

    invoke-interface {v0, p0}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    return v0
.end method

.method private static blacklist flattenOrderToString(Ljava/util/List;)Ljava/lang/String;
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/List<",
            "Landroid/content/ComponentName;",
            ">;)",
            "Ljava/lang/String;"
        }
    .end annotation

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-interface {p0}, Ljava/util/List;->size()I

    move-result v1

    add-int/lit8 v1, v1, -0x1

    const/4 v2, 0x0

    :goto_0
    invoke-interface {p0, v2}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Landroid/content/ComponentName;

    invoke-virtual {v3}, Landroid/content/ComponentName;->flattenToShortString()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-ne v2, v1, :cond_0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    return-object v3

    :cond_0
    const-string v3, ","

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    add-int/lit8 v2, v2, 0x1

    goto :goto_0
.end method

.method public static blacklist getActivityResolveOrder(Landroid/content/ContentResolver;)Ljava/util/List;
    .registers 2
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/ContentResolver;",
            ")",
            "Ljava/util/List<",
            "Landroid/content/ComponentName;",
            ">;"
        }
    .end annotation

    const-string v0, "activity_resolve_order"

    invoke-static {p0, v0}, Landroid/provider/MiuiSettings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/provider/MiuiSettings$System;->unflattenOrderFromString(Ljava/lang/String;)Ljava/util/List;

    move-result-object v0

    return-object v0
.end method

.method public static whitelist getBooleanForUser(Landroid/content/ContentResolver;Ljava/lang/String;ZI)Z
    .registers 5

    invoke-static {p0, p1, p2, p3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    return v0
.end method

.method public static blacklist getDisableWifiAutoConnectSsid(Landroid/content/Context;)Ljava/util/HashSet;
    .registers 8
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/Context;",
            ")",
            "Ljava/util/HashSet<",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation

    nop

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "disable_wifi_auto_connect_ssid"

    const/4 v2, -0x3

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v0

    new-instance v1, Ljava/util/HashSet;

    invoke-direct {v1}, Ljava/util/HashSet;-><init>()V

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v2

    if-nez v2, :cond_0

    const-string v2, ","

    invoke-virtual {v0, v2}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v2

    if-eqz v2, :cond_0

    const/4 v3, 0x0

    :goto_0
    array-length v4, v2

    if-ge v3, v4, :cond_0

    :try_start_0
    new-instance v4, Ljava/lang/String;

    aget-object v5, v2, v3

    const/4 v6, 0x2

    invoke-static {v5, v6}, Landroid/util/Base64;->decode(Ljava/lang/String;I)[B

    move-result-object v5

    invoke-direct {v4, v5}, Ljava/lang/String;-><init>([B)V

    invoke-virtual {v1, v4}, Ljava/util/HashSet;->add(Ljava/lang/Object;)Z
    :try_end_0
    .catch Ljava/lang/IllegalArgumentException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_1

    :catch_0
    move-exception v4

    :goto_1
    add-int/lit8 v3, v3, 0x1

    goto :goto_0

    :cond_0
    return-object v1
.end method

.method public static blacklist getDisplayWindowSizeInSmartCover()Landroid/graphics/Rect;
    .registers 4
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation

    new-instance v0, Landroid/graphics/Rect;

    const/16 v1, 0x438

    const/16 v2, 0x780

    const/4 v3, 0x0

    invoke-direct {v0, v3, v3, v1, v2}, Landroid/graphics/Rect;-><init>(IIII)V

    return-object v0
.end method

.method public static whitelist getHapticFeedbackLevel(Landroid/content/Context;)I
    .registers 5

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    sget v1, Landroid/provider/MiuiSettings$System;->HAPTIC_FEEDBACK_LEVEL_DEFAULT:I

    const/4 v2, -0x3

    const-string v3, "haptic_feedback_level"

    invoke-static {v0, v3, v1, v2}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    return v0
.end method

.method public static blacklist getHotSpotMacBlackSet(Landroid/content/Context;)Ljava/util/Set;
    .registers 8
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/Context;",
            ")",
            "Ljava/util/Set<",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation

    nop

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "hotspot_mac_black_set"

    const/4 v2, -0x2

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v0

    new-instance v1, Ljava/util/HashSet;

    invoke-direct {v1}, Ljava/util/HashSet;-><init>()V

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v2

    if-nez v2, :cond_0

    const-string v2, ","

    invoke-virtual {v0, v2}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v2

    if-eqz v2, :cond_0

    const/4 v3, 0x0

    :goto_0
    array-length v4, v2

    if-ge v3, v4, :cond_0

    :try_start_0
    new-instance v4, Ljava/lang/String;

    aget-object v5, v2, v3

    const/4 v6, 0x2

    invoke-static {v5, v6}, Landroid/util/Base64;->decode(Ljava/lang/String;I)[B

    move-result-object v5

    invoke-direct {v4, v5}, Ljava/lang/String;-><init>([B)V

    invoke-interface {v1, v4}, Ljava/util/Set;->add(Ljava/lang/Object;)Z
    :try_end_0
    .catch Ljava/lang/IllegalArgumentException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_1

    :catch_0
    move-exception v4

    :goto_1
    add-int/lit8 v3, v3, 0x1

    goto :goto_0

    :cond_0
    return-object v1
.end method

.method public static blacklist getHotSpotMaxStationNum(Landroid/content/Context;)I
    .registers 5

    const/4 v0, 0x0

    nop

    :try_start_0
    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    const-string v2, "hotspot_max_station_num"

    const/4 v3, -0x2

    invoke-static {v1, v2, v3}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1
    :try_end_0
    .catch Landroid/provider/Settings$SettingNotFoundException; {:try_start_0 .. :try_end_0} :catch_0

    move v0, v1

    goto :goto_0

    :catch_0
    move-exception v1

    :goto_0
    return v0
.end method

.method public static blacklist getHotSpotVendorSpecific(Landroid/content/Context;)Ljava/lang/String;
    .registers 4

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "hotspot_vendor_specific"

    const/4 v2, -0x2

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method

.method public static blacklist getRestartWifiApAfterConfigChange(Landroid/content/Context;)Z
    .registers 5

    const/4 v0, 0x0

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    const-string v2, "softap_will_restart"

    const/4 v3, -0x2

    invoke-static {v1, v2, v0, v3}, Landroid/provider/MiuiSettings$System;->getBooleanForUser(Landroid/content/ContentResolver;Ljava/lang/String;ZI)Z

    move-result v0

    goto :goto_0

    :cond_0
    nop

    :goto_0
    return v0
.end method

.method public static blacklist getScreenKeyLongPressAction(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    .registers 5

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const/4 v1, -0x2

    invoke-static {v0, p1, v1}, Landroid/provider/Settings$System;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_3

    const-string v0, "none"

    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    const v2, 0x110300bf

    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getStringArray(I)[Ljava/lang/String;

    move-result-object v1

    const-string v2, "screen_key_long_press_menu"

    invoke-virtual {v2, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_0

    const/4 v2, 0x0

    aget-object v0, v1, v2

    goto :goto_0

    :cond_0
    const-string v2, "screen_key_long_press_home"

    invoke-virtual {v2, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_1

    const/4 v2, 0x1

    aget-object v0, v1, v2

    goto :goto_0

    :cond_1
    const-string v2, "screen_key_long_press_back"

    invoke-virtual {v2, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_2

    const/4 v2, 0x2

    aget-object v0, v1, v2

    goto :goto_0

    :cond_2
    const-string v2, "screen_key_long_press_app_switch"

    invoke-virtual {v2, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_3

    const/4 v2, 0x3

    aget-object v0, v1, v2

    :cond_3
    :goto_0
    return-object v0
.end method

.method public static blacklist getScreenKeyOrder(Landroid/content/Context;)Ljava/util/ArrayList;
    .registers 8
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/Context;",
            ")",
            "Ljava/util/ArrayList<",
            "Ljava/lang/Integer;",
            ">;"
        }
    .end annotation

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    const-string v2, "screen_key_order"

    invoke-static {v1, v2}, Landroid/provider/Settings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v2

    if-nez v2, :cond_1

    const-string v2, " "

    invoke-virtual {v1, v2}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v2

    const/4 v3, 0x0

    :goto_0
    array-length v4, v2

    if-ge v3, v4, :cond_1

    :try_start_0
    aget-object v4, v2, v3

    invoke-static {v4}, Ljava/lang/Integer;->valueOf(Ljava/lang/String;)Ljava/lang/Integer;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/Integer;->intValue()I

    move-result v4

    sget-object v5, Landroid/provider/MiuiSettings$System;->screenKeys:Ljava/util/ArrayList;

    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result v5

    if-eqz v5, :cond_0

    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v5

    invoke-virtual {v0, v5}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    :cond_0
    nop

    add-int/lit8 v3, v3, 0x1

    goto :goto_0

    :catch_0
    move-exception v4

    invoke-virtual {v0}, Ljava/util/ArrayList;->clear()V

    nop

    :cond_1
    sget-object v2, Landroid/provider/MiuiSettings$System;->screenKeys:Ljava/util/ArrayList;

    invoke-virtual {v2}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_1
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    if-eqz v3, :cond_3

    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Ljava/lang/Integer;

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result v4

    if-nez v4, :cond_2

    invoke-virtual {v0, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :cond_2
    goto :goto_1

    :cond_3
    return-object v0
.end method

.method public static whitelist getShowCustomCarrierDefault()I
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_CM_CUSTOMIZATION_TEST:Z

    if-nez v0, :cond_1

    sget-boolean v0, Lmiui/os/Build;->IS_CU_CUSTOMIZATION_TEST:Z

    if-nez v0, :cond_1

    sget-boolean v0, Lmiui/os/Build;->IS_CT_CUSTOMIZATION_TEST:Z

    if-nez v0, :cond_1

    invoke-static {}, Landroid/content/res/Resources;->getSystem()Landroid/content/res/Resources;

    move-result-object v0

    const v1, 0x11050075

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getBoolean(I)Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    goto :goto_1

    :cond_1
    :goto_0
    const/4 v0, 0x1

    :goto_1
    return v0
.end method

.method public static blacklist getSmallWindowMode()Landroid/provider/MiuiSettings$System$SmallWindowType;
    .registers 1
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation

    sget-object v0, Landroid/provider/MiuiSettings$System$SmallWindowType;->A1_STYLE:Landroid/provider/MiuiSettings$System$SmallWindowType;

    return-object v0
.end method

.method public static whitelist getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;
    .registers 3

    invoke-static {p0, p1}, Landroid/provider/Settings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method

.method public static declared-synchronized blacklist getString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .registers 5

    const-class v0, Landroid/provider/MiuiSettings$System;

    monitor-enter v0

    :try_start_0
    invoke-static {p0, p1}, Landroid/provider/Settings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    if-nez v1, :cond_0

    move-object v1, p2

    :cond_0
    monitor-exit v0

    return-object v1

    :catchall_0
    move-exception p0

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw p0
.end method

.method public static whitelist getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;
    .registers 4

    invoke-static {p0, p1, p2}, Landroid/provider/Settings$System;->getStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method

.method public static blacklist getT9IndexingKeyDefault()I
    .registers 1

    const-string v0, "TW"

    invoke-static {v0}, Lmiui/os/Build;->checkRegion(Ljava/lang/String;)Z

    move-result v0

    return v0
.end method

.method public static blacklist isCdmaPreciseAnswerStateEnabled(Landroid/content/Context;)Z
    .registers 4

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "cdma_precise_answer_state"

    const/4 v2, 0x1

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    if-ne v0, v2, :cond_0

    goto :goto_0

    :cond_0
    const/4 v2, 0x0

    :goto_0
    return v2
.end method

.method private static blacklist isCnFromOperator(Ljava/lang/String;)Z
    .registers 4

    const-string v0, ""

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_0

    invoke-virtual {p0}, Ljava/lang/String;->length()I

    move-result v1

    const/4 v2, 0x3

    if-lt v1, v2, :cond_0

    const/4 v1, 0x0

    invoke-virtual {p0, v1, v2}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v0

    :cond_0
    const-string v1, "460"

    invoke-virtual {v1, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    return v1
.end method

.method public static whitelist isHapticFeedbackDisabled(Landroid/content/Context;)Z
    .registers 5

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const/4 v1, -0x3

    const-string v2, "haptic_feedback_enabled"

    const/4 v3, 0x0

    invoke-static {v0, v2, v3, v1}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-nez v0, :cond_0

    const/4 v3, 0x1

    :cond_0
    return v3
.end method

.method public static final blacklist isInCnRegion()Z
    .registers 1

    const/4 v0, 0x1

    return v0
.end method

.method public static blacklist isInSmallWindowMode(Landroid/content/Context;)Z
    .registers 2
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation

    const/4 v0, 0x0

    return v0
.end method

.method public static blacklist isMiDropEnabled(Landroid/content/Context;)Z
    .registers 4

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "key_midrop_enabled"

    const/4 v2, 0x0

    invoke-static {v0, v1, v2}, Landroid/provider/MiuiSettings$System;->getBoolean(Landroid/content/ContentResolver;Ljava/lang/String;Z)Z

    move-result v0

    return v0
.end method

.method public static blacklist isMiuiPublicSettings(Landroid/content/pm/PackageInfo;Ljava/lang/String;)Z
    .registers 5

    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS_OPEN:Ljava/util/Set;

    invoke-interface {v0, p1}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v0

    const/4 v1, 0x1

    const-string v2, "SystemSettings"

    if-eqz v0, :cond_0

    const-string v0, "Hit MiuiSettings.System.PUBLIC_SETTINGS_OPEN"

    invoke-static {v2, v0}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    return v1

    :cond_0
    sget-object v0, Landroid/provider/MiuiSettings$System;->PUBLIC_SETTINGS:Ljava/util/Set;

    invoke-interface {v0, p1}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Landroid/content/pm/PackageInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    invoke-virtual {v0}, Landroid/content/pm/ApplicationInfo;->isSystemApp()Z

    move-result v0

    if-nez v0, :cond_1

    iget-object v0, p0, Landroid/content/pm/PackageInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    invoke-virtual {v0}, Landroid/content/pm/ApplicationInfo;->isSignedWithPlatformKey()Z

    move-result v0

    if-eqz v0, :cond_2

    :cond_1
    return v1

    :cond_2
    const-string v0, "Want to modify SystemSettings? See MiuiSettings.System.PUBLIC_SETTINGS"

    invoke-static {v2, v0}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    const/4 v0, 0x0

    return v0
.end method

.method public static blacklist isSimpleMode(Landroid/content/Context;)Z
    .registers 5

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x1

    xor-int/2addr v0, v1

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    const-string v3, "simple_mode"

    invoke-static {v2, v3, v0}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v2

    if-ne v2, v1, :cond_0

    goto :goto_0

    :cond_0
    const/4 v1, 0x0

    :goto_0
    return v1
.end method

.method public static blacklist isSuperSaveModeOpen(Landroid/content/Context;I)Z
    .registers 5

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "power_supersave_mode_open"

    const/4 v2, 0x0

    invoke-static {v0, v1, v2, p1}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-eqz v0, :cond_0

    const/4 v2, 0x1

    :cond_0
    return v2
.end method

.method public static blacklist isTouchAssistantEnabledForUser(Landroid/content/Context;IZ)Z
    .registers 6

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "touch_assistant_enabled"

    const/4 v2, 0x0

    invoke-static {v0, v1, v2, p1}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    const/4 v1, 0x1

    if-ne v0, v1, :cond_0

    move v2, v1

    :cond_0
    return v2
.end method

.method public static blacklist isTouchAssistantTemporaryForUser(Landroid/content/Context;IZ)Z
    .registers 6

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "touch_assistant_enabled"

    const/4 v2, 0x2

    invoke-static {v0, v1, v2, p1}, Landroid/provider/Settings$System;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I

    move-result v0

    if-ne v0, v2, :cond_0

    const/4 v1, 0x1

    goto :goto_0

    :cond_0
    const/4 v1, 0x0

    :goto_0
    return v1
.end method

.method public static blacklist isXiaoAiExist(Landroid/content/Context;)Z
    .registers 5

    const/4 v0, 0x0

    :try_start_0
    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v1

    const-string v2, "com.miui.voiceassist"

    invoke-virtual {v1, v2, v0}, Landroid/content/pm/PackageManager;->getPackageInfo(Ljava/lang/String;I)Landroid/content/pm/PackageInfo;
    :try_end_0
    .catch Landroid/content/pm/PackageManager$NameNotFoundException; {:try_start_0 .. :try_end_0} :catch_0

    const/4 v0, 0x1

    return v0

    :catch_0
    move-exception v1

    const-string v2, "SystemSettings"

    const-string v3, "isXiaoAiExist: noExist"

    invoke-static {v2, v3}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    return v0
.end method

.method public static blacklist putActivityResolveOrder(Landroid/content/ContentResolver;Ljava/util/List;)V
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/ContentResolver;",
            "Ljava/util/List<",
            "Landroid/content/ComponentName;",
            ">;)V"
        }
    .end annotation

    const-string v0, "activity_resolve_order"

    invoke-static {p1}, Landroid/provider/MiuiSettings$System;->flattenOrderToString(Ljava/util/List;)Ljava/lang/String;

    move-result-object v1

    invoke-static {p0, v0, v1}, Landroid/provider/MiuiSettings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    return-void
.end method

.method public static whitelist putBoolean(Landroid/content/ContentResolver;Ljava/lang/String;Z)Z
    .registers 4

    invoke-static {p0, p1, p2}, Landroid/provider/Settings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    move-result v0

    return v0
.end method

.method public static whitelist putBooleanForUser(Landroid/content/ContentResolver;Ljava/lang/String;ZI)Z
    .registers 5

    invoke-static {p0, p1, p2, p3}, Landroid/provider/Settings$System;->putIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)Z

    move-result v0

    return v0
.end method

.method public static blacklist putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z
    .registers 4

    invoke-static {p0, p1, p2}, Landroid/provider/Settings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    move-result v0

    return v0
.end method

.method public static whitelist putStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;I)Z
    .registers 5

    invoke-static {p0, p1, p2, p3}, Landroid/provider/Settings$System;->putStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;I)Z

    move-result v0

    return v0
.end method

.method public static blacklist setDisableWifiAutoConnectSsid(Landroid/content/Context;Ljava/util/HashSet;)V
    .registers 7
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/Context;",
            "Ljava/util/HashSet<",
            "Ljava/lang/String;",
            ">;)V"
        }
    .end annotation

    if-nez p1, :cond_0

    return-void

    :cond_0
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {p1}, Ljava/util/HashSet;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_0
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_1

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Ljava/lang/String;

    :try_start_0
    invoke-virtual {v2}, Ljava/lang/String;->getBytes()[B

    move-result-object v3

    const/4 v4, 0x2

    invoke-static {v3, v4}, Landroid/util/Base64;->encodeToString([BI)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v3, ","

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    :try_end_0
    .catch Ljava/lang/IllegalArgumentException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_1

    :catch_0
    move-exception v3

    :goto_1
    goto :goto_0

    :cond_1
    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    const-string v3, "disable_wifi_auto_connect_ssid"

    const/4 v4, -0x3

    invoke-static {v1, v3, v2, v4}, Landroid/provider/Settings$System;->putStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;I)Z

    return-void
.end method

.method public static blacklist setHotSpotMacBlackSet(Landroid/content/Context;Ljava/util/Set;)V
    .registers 8
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/Context;",
            "Ljava/util/Set<",
            "Ljava/lang/String;",
            ">;)V"
        }
    .end annotation

    if-eqz p1, :cond_2

    const-string v0, "^[a-fA-F0-9]{2}+:[a-fA-F0-9]{2}+:[a-fA-F0-9]{2}+:[a-fA-F0-9]{2}+:[a-fA-F0-9]{2}+:[a-fA-F0-9]{2}$"

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    invoke-interface {p1}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_0
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    if-eqz v3, :cond_1

    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Ljava/lang/String;

    :try_start_0
    const-string v4, "^[a-fA-F0-9]{2}+:[a-fA-F0-9]{2}+:[a-fA-F0-9]{2}+:[a-fA-F0-9]{2}+:[a-fA-F0-9]{2}+:[a-fA-F0-9]{2}$"

    invoke-virtual {v3, v4}, Ljava/lang/String;->matches(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_0

    invoke-virtual {v3}, Ljava/lang/String;->getBytes()[B

    move-result-object v4

    const/4 v5, 0x2

    invoke-static {v4, v5}, Landroid/util/Base64;->encodeToString([BI)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v4, ","

    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    :try_end_0
    .catch Ljava/lang/IllegalArgumentException; {:try_start_0 .. :try_end_0} :catch_0

    :cond_0
    goto :goto_1

    :catch_0
    move-exception v4

    :goto_1
    goto :goto_0

    :cond_1
    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    const-string v4, "hotspot_mac_black_set"

    const/4 v5, -0x2

    invoke-static {v2, v4, v3, v5}, Landroid/provider/Settings$System;->putStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;I)Z

    :cond_2
    return-void
.end method

.method public static blacklist setHotSpotMaxStationNum(Landroid/content/Context;I)Z
    .registers 5

    if-lez p1, :cond_0

    const/16 v0, 0x7d8

    if-ge p1, v0, :cond_0

    nop

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "hotspot_max_station_num"

    const/4 v2, -0x2

    invoke-static {v0, v1, p1, v2}, Landroid/provider/Settings$System;->putIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)Z

    const/4 v0, 0x1

    return v0

    :cond_0
    const/4 v0, 0x0

    return v0
.end method

.method public static blacklist setHotSpotVendorSpecific(Landroid/content/Context;Ljava/lang/String;)V
    .registers 5

    if-eqz p1, :cond_0

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "hotspot_vendor_specific"

    const/4 v2, -0x2

    invoke-static {v0, v1, p1, v2}, Landroid/provider/Settings$System;->putStringForUser(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;I)Z

    :cond_0
    return-void
.end method

.method public static blacklist setRestartWifiApAfterConfigChange(Landroid/content/Context;Z)V
    .registers 5

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "softap_will_restart"

    const/4 v2, -0x2

    invoke-static {v0, v1, p1, v2}, Landroid/provider/MiuiSettings$System;->putBooleanForUser(Landroid/content/ContentResolver;Ljava/lang/String;ZI)Z

    :cond_0
    return-void
.end method

.method public static blacklist setSimpleMode(Landroid/content/Context;Z)V
    .registers 4

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "simple_mode"

    invoke-static {v0, v1, p1}, Landroid/provider/Settings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    return-void
.end method

.method public static blacklist setSmartCoverMode(Z)V
    .registers 3
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation

    const-string v0, "SmartCover"

    const-string v1, "Stub."

    invoke-static {v0, v1}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    return-void
.end method

.method public static blacklist setUseWordPhoto(Landroid/content/Context;Z)V
    .registers 4

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "word_photo"

    invoke-static {v0, v1, p1}, Landroid/provider/Settings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    return-void
.end method

.method private static blacklist unflattenOrderFromString(Ljava/lang/String;)Ljava/util/List;
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/lang/String;",
            ")",
            "Ljava/util/List<",
            "Landroid/content/ComponentName;",
            ">;"
        }
    .end annotation

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    if-eqz p0, :cond_0

    const-string v1, ","

    invoke-virtual {p0, v1}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x0

    :goto_0
    array-length v3, v1

    if-ge v2, v3, :cond_0

    aget-object v3, v1, v2

    invoke-static {v3}, Landroid/content/ComponentName;->unflattenFromString(Ljava/lang/String;)Landroid/content/ComponentName;

    move-result-object v3

    invoke-interface {v0, v3}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :cond_0
    return-object v0
.end method

.method public static blacklist useWordPhoto(Landroid/content/Context;)Z
    .registers 4

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "word_photo"

    const/4 v2, 0x0

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    const/4 v1, 0x1

    if-ne v0, v1, :cond_0

    move v2, v1

    :cond_0
    return v2
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR modified class (no method-level diff) from miui-framework_Legend.mtcr",
    },
]
