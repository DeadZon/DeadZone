.class Lcom/android/systemui/navigationbar/gestural/NavigationHandle$1;
.super Landroid/database/ContentObserver;
.source "NavigationHandle.java"


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/navigationbar/gestural/NavigationHandle;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/navigationbar/gestural/NavigationHandle;


# direct methods
.method constructor <init>(Lcom/android/systemui/navigationbar/gestural/NavigationHandle;Landroid/os/Handler;)V
    .registers 3
    .param p1, "this$0"  # Lcom/android/systemui/navigationbar/gestural/NavigationHandle;
    .param p2, "arg0"  # Landroid/os/Handler;

    .line 35
    iput-object p1, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle$1;->this$0:Lcom/android/systemui/navigationbar/gestural/NavigationHandle;

    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V

    return-void
.end method


# virtual methods
.method public onChange(ZLandroid/net/Uri;)V
    .registers 4
    .param p1, "selfChange"  # Z
    .param p2, "uri"  # Landroid/net/Uri;

    .line 38
    invoke-super {p0, p1, p2}, Landroid/database/ContentObserver;->onChange(ZLandroid/net/Uri;)V

    .line 39
    iget-object v0, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle$1;->this$0:Lcom/android/systemui/navigationbar/gestural/NavigationHandle;

    invoke-static {v0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->access$000(Lcom/android/systemui/navigationbar/gestural/NavigationHandle;)V

    .line 40
    iget-object v0, p0, Lcom/android/systemui/navigationbar/gestural/NavigationHandle$1;->this$0:Lcom/android/systemui/navigationbar/gestural/NavigationHandle;

    invoke-virtual {v0}, Lcom/android/systemui/navigationbar/gestural/NavigationHandle;->invalidate()V

    .line 41
    return-void
.end method
