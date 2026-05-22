"""
Legend MTCR patch - class-level rule.

Target JAR   : framework.jar
Target class : android/preference/MiuiPictureSelectionPreference
Source MTCR  : Framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "framework.jar"
TARGET_CLASS = "android/preference/MiuiPictureSelectionPreference.smali"
CLASS_FALLBACK_NAMES = ['MiuiPictureSelectionPreference.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "add_class_android_preference_MiuiPictureSelectionPreference",
        "method":      "",
        "type":        "class_add",
        "search":      None,
        "replacement": """\
.class public Landroid/preference/MiuiPictureSelectionPreference;
.super Ljava/lang/Object;


# direct methods
.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static getDrawableFromPath(Ljava/lang/String;)Landroid/graphics/drawable/Drawable;
    .registers 15

    const/4 v2, 0x0

    const-string v0, "android"

    invoke-static {v0}, Landroid/Utils/Utils;->getContext(Ljava/lang/Object;)Landroid/content/Context;

    move-result-object v13

    const/4 v11, 0x0

    invoke-virtual {v13}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v0

    iget v0, v0, Landroid/content/res/Configuration;->uiMode:I

    and-int/lit8 v0, v0, 0x30

    const/16 v1, 0x20

    if-ne v0, v1, :cond_0

    const/4 v12, 0x1

    :goto_0
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    if-eqz v12, :cond_1

    const-string v0, "_dark"

    :goto_1
    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v13}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "content://miui.imagegalery.imageProvider"

    invoke-static {v1}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    move-object v4, v2

    move-object v5, v2

    invoke-virtual/range {v0 .. v5}, Landroid/content/ContentResolver;->query(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;

    move-result-object v10

    if-eqz v10, :cond_2

    :goto_2
    invoke-interface {v10}, Landroid/database/Cursor;->moveToNext()Z

    move-result v0

    if-eqz v0, :cond_2

    new-instance v11, Landroid/graphics/drawable/BitmapDrawable;

    invoke-virtual {v13}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const-string v1, "data"

    invoke-interface {v10, v1}, Landroid/database/Cursor;->getColumnIndex(Ljava/lang/String;)I

    move-result v1

    invoke-interface {v10, v1}, Landroid/database/Cursor;->getBlob(I)[B

    move-result-object v1

    invoke-static {v1}, Landroid/preference/MiuiPictureSelectionPreference;->getImage([B)Landroid/graphics/Bitmap;

    move-result-object v1

    invoke-direct {v11, v0, v1}, Landroid/graphics/drawable/BitmapDrawable;-><init>(Landroid/content/res/Resources;Landroid/graphics/Bitmap;)V

    goto :goto_2

    :cond_0
    const/4 v12, 0x0

    goto :goto_0

    :cond_1
    const-string v0, ""

    goto :goto_1

    :cond_2
    if-nez v11, :cond_3

    invoke-virtual {v13}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v4

    const-string v0, "content://miui.imagegalery.imageProvider"

    invoke-static {v0}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v5

    move-object v6, v2

    move-object v7, p0

    move-object v8, v2

    move-object v9, v2

    invoke-virtual/range {v4 .. v9}, Landroid/content/ContentResolver;->query(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;

    move-result-object v10

    :cond_3
    if-eqz v10, :cond_4

    :goto_3
    invoke-interface {v10}, Landroid/database/Cursor;->moveToNext()Z

    move-result v0

    if-eqz v0, :cond_4

    new-instance v11, Landroid/graphics/drawable/BitmapDrawable;

    invoke-virtual {v13}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const-string v1, "data"

    invoke-interface {v10, v1}, Landroid/database/Cursor;->getColumnIndex(Ljava/lang/String;)I

    move-result v1

    invoke-interface {v10, v1}, Landroid/database/Cursor;->getBlob(I)[B

    move-result-object v1

    invoke-static {v1}, Landroid/preference/MiuiPictureSelectionPreference;->getImage([B)Landroid/graphics/Bitmap;

    move-result-object v1

    invoke-direct {v11, v0, v1}, Landroid/graphics/drawable/BitmapDrawable;-><init>(Landroid/content/res/Resources;Landroid/graphics/Bitmap;)V

    goto :goto_3

    :cond_4
    if-eqz v10, :cond_5

    invoke-interface {v10}, Landroid/database/Cursor;->close()V

    :cond_5
    return-object v11
.end method

.method public static getImage([B)Landroid/graphics/Bitmap;
    .registers 3

    const/4 v0, 0x0

    array-length v1, p0

    invoke-static {p0, v0, v1}, Landroid/graphics/BitmapFactory;->decodeByteArray([BII)Landroid/graphics/Bitmap;

    move-result-object v0

    return-object v0
.end method

""",
        "required":    True,
        "reason":      "Legend MTCR new class from Framework_Legend.mtcr",
    },
]
