"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/AnimatorVisibleColorView.smali'
CLASS_FALLBACK_NAMES = ['AnimatorVisibleColorView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;
.super Lcom/android/systemui/newstatusbar/views/AnimatorColorView;


# instance fields
.field private realVisibility:I


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 6

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/views/AnimatorColorView;-><init>(Landroid/content/Context;)V

    const/4 v0, -0x1

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->realVisibility:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->getData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    const/4 v1, 0x1

    new-array v1, v1, [Ljava/lang/String;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v3, v0, Lcom/android/systemui/newstatusbar/data/IconData;->key:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, "_visible"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    const/4 v3, 0x0

    aput-object v2, v1, v3

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 7

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/views/AnimatorColorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, -0x1

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->realVisibility:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->getData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    const/4 v1, 0x1

    new-array v1, v1, [Ljava/lang/String;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v3, v0, Lcom/android/systemui/newstatusbar/data/IconData;->key:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, "_visible"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    const/4 v3, 0x0

    aput-object v2, v1, v3

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 8

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/views/AnimatorColorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const/4 v0, -0x1

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->realVisibility:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->getData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    const/4 v1, 0x1

    new-array v1, v1, [Ljava/lang/String;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v3, v0, Lcom/android/systemui/newstatusbar/data/IconData;->key:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, "_visible"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    const/4 v3, 0x0

    aput-object v2, v1, v3

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 9

    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/newstatusbar/views/AnimatorColorView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    const/4 v0, -0x1

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->realVisibility:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->getData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    const/4 v1, 0x1

    new-array v1, v1, [Ljava/lang/String;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v3, v0, Lcom/android/systemui/newstatusbar/data/IconData;->key:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, "_visible"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    const/4 v3, 0x0

    aput-object v2, v1, v3

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v1

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    return-void
.end method


# virtual methods
.method public setVisibility(I)V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->iconData:Lcom/android/systemui/newstatusbar/data/IconData;

    if-eqz v0, :cond_26

    iput p1, p0, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->realVisibility:I

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->iconData:Lcom/android/systemui/newstatusbar/data/IconData;

    iget-object v1, v1, Lcom/android/systemui/newstatusbar/data/IconData;->key:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "_visible"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const/4 v1, 0x1

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings(Ljava/lang/String;I)Z

    move-result v0

    if-nez v0, :cond_26

    const/16 p1, 0x8

    :cond_26
    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/views/AnimatorColorView;->setVisibility(I)V

    return-void
.end method

.method public update()V
    .registers 3

    invoke-super {p0}, Lcom/android/systemui/newstatusbar/views/AnimatorColorView;->update()V

    iget v0, p0, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->realVisibility:I

    const/4 v1, -0x1

    if-ne v0, v1, :cond_e

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->getVisibility()I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->realVisibility:I

    :cond_e
    iget v0, p0, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->realVisibility:I

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/AnimatorVisibleColorView;->setVisibility(I)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_AnimatorVisibleColorView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
