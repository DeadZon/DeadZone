"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/MainLayout$1.smali'
CLASS_FALLBACK_NAMES = ['MainLayout$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/layouts/MainLayout$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/util/Comparator;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/android/systemui/newstatusbar/layouts/MainLayout;->arrangeByPlaces()V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Ljava/lang/Object;",
        "Ljava/util/Comparator",
        "<",
        "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
        ">;"
    }
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/layouts/MainLayout;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/MainLayout$1;->this$0:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public compare(Lcom/android/systemui/newstatusbar/layouts/SingleLayout;Lcom/android/systemui/newstatusbar/layouts/SingleLayout;)I
    .registers 5

    invoke-virtual {p1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I

    move-result v0

    invoke-virtual {p2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I

    move-result v1

    invoke-static {v0, v1}, Ljava/lang/Integer;->compare(II)I

    move-result v0

    return v0
.end method

.method public bridge synthetic compare(Ljava/lang/Object;Ljava/lang/Object;)I
    .registers 4

    check-cast p1, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    check-cast p2, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    invoke-virtual {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout$1;->compare(Lcom/android/systemui/newstatusbar/layouts/SingleLayout;Lcom/android/systemui/newstatusbar/layouts/SingleLayout;)I

    move-result v0

    return v0
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_MainLayout_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
