TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$VoiceAssistState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$VoiceAssistState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;', '.field private static final SOUND_TRIGGER_SUPPORT:Ljava/lang/String; = "sound_trigger_support"', '.field private static final STATE_LOW_POWER_SUPPORT:I = 0x1', '.field private static final STATE_NOT_SUPPORT:I = -0x1', '.field private static final VOICE_ASSIST_COMPLETED:Ljava/lang/String; = "voice_assist_completed"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__VoiceAssistState__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['new-instance v0, Landroid/content/Intent;', 'invoke-direct {v0}, Landroid/content/Intent;-><init>()V', 'const-string v1, "com.miui.voicetrigger"', 'invoke-direct {p0, v1}, Lcom/android/provision/activities/DefaultActivity$VoiceAssistState;->isPkgInstalled(Ljava/lang/String;)Z', 'if-eqz v2, :cond_0', 'invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity$VoiceAssistState;->isSupported()Z', 'if-eqz v2, :cond_0', 'invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity$VoiceAssistState;->isVoiceAssistCompleted()Z'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 4

    new-instance v0, Landroid/content/Intent;

    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    const-string v1, "com.miui.voicetrigger"

    invoke-direct {p0, v1}, Lcom/android/provision/activities/DefaultActivity$VoiceAssistState;->isPkgInstalled(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_0

    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity$VoiceAssistState;->isSupported()Z

    move-result v2

    if-eqz v2, :cond_0

    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity$VoiceAssistState;->isVoiceAssistCompleted()Z

    move-result v2

    if-nez v2, :cond_0

    const-string p0, "com.miui.voicetrigger.SetupTrainingActivity"

    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    return-object v0

    :cond_0
    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity$VoiceAssistState;->isLabWakeupGuideEnable()Z

    move-result p0

    const/4 v1, 0x1

    if-ne p0, v1, :cond_1

    const-string p0, "com.miui.voiceassist"

    const-string v1, "com.xiaomi.voiceassistant.BootupLabVoiceTriggerGuideActivity"

    invoke-virtual {v0, p0, v1}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    :cond_1
    return-object v0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 4

    goto :goto_b

    nop

    :goto_0
    const/4 v1, 0x1

    goto :goto_f

    nop

    :goto_1
    if-eqz v2, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_c

    nop

    :goto_2
    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity$VoiceAssistState;->isLabWakeupGuideEnable()Z

    move-result p0

    goto :goto_0

    nop

    :goto_3
    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    goto :goto_5

    nop

    :goto_4
    invoke-direct {p0, v1}, Lcom/android/provision/activities/DefaultActivity$VoiceAssistState;->isPkgInstalled(Ljava/lang/String;)Z

    move-result v2

    goto :goto_6

    nop

    :goto_5
    const-string v1, "com.miui.voicetrigger"

    goto :goto_4

    nop

    :goto_6
    if-nez v2, :cond_1

    goto :goto_e

    :cond_1
    goto :goto_7

    nop

    :goto_7
    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity$VoiceAssistState;->isSupported()Z

    move-result v2

    goto :goto_12

    nop

    :goto_8
    invoke-virtual {v0, p0, v1}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    :goto_9
    goto :goto_11

    nop

    :goto_a
    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity$VoiceAssistState;->isVoiceAssistCompleted()Z

    move-result v2

    goto :goto_1

    nop

    :goto_b
    new-instance v0, Landroid/content/Intent;

    goto :goto_3

    nop

    :goto_c
    const-string p0, "com.miui.voicetrigger.SetupTrainingActivity"

    goto :goto_14

    nop

    :goto_d
    return-object v0

    :goto_e
    goto :goto_2

    nop

    :goto_f
    if-eq p0, v1, :cond_2

    goto :goto_9

    :cond_2
    goto :goto_10

    nop

    :goto_10
    const-string p0, "com.miui.voiceassist"

    goto :goto_13

    nop

    :goto_11
    return-object v0

    :goto_12
    if-nez v2, :cond_3

    goto :goto_e

    :cond_3
    goto :goto_a

    nop

    :goto_13
    const-string v1, "com.xiaomi.voiceassistant.BootupLabVoiceTriggerGuideActivity"

    goto :goto_8

    nop

    :goto_14
    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
