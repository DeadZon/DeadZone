.class public Lcom/android/kevin/MyUtils;
.super Ljava/lang/Object;
.source "MyUtils.java"


# direct methods
.method public constructor <init>()V
    .registers 1

    .line 5
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static getRIdentifier(Landroid/content/Context;Ljava/lang/String;)I
    .registers 5
    .param p0, "context"  # Landroid/content/Context;
    .param p1, "resourceName"  # Ljava/lang/String;

    .line 9
    const-string v0, ".android"

    invoke-virtual {p1, v0}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_16

    .line 10
    const-string v0, "android"

    .line 11
    .local v0, "packageName":Ljava/lang/String;
    invoke-virtual {p1}, Ljava/lang/String;->length()I

    move-result v1

    add-int/lit8 v1, v1, -0x8

    const/4 v2, 0x0

    invoke-virtual {p1, v2, v1}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object p1

    goto :goto_1a

    .line 13
    .end local v0  # "packageName":Ljava/lang/String;
    :cond_16
    invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v0

    .line 16
    .restart local v0  # "packageName":Ljava/lang/String;
    :goto_1a
    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    const/4 v2, 0x0

    invoke-virtual {v1, p1, v2, v0}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v1

    return v1
.end method
