TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/LottieTask$LottieFutureTask.smali'
CLASS_FALLBACK_NAMES = ['LottieTask$LottieFutureTask.smali']
CLASS_ANCHORS = ['.super Ljava/util/concurrent/FutureTask;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_LottieTask__LottieFutureTask__done',
        'method': '.method protected done()V',
        'method_name': 'done',
        'method_anchors': ['invoke-virtual {p0}, Ljava/util/concurrent/FutureTask;->isCancelled()Z', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lcom/airbnb/lottie/LottieTask$LottieFutureTask;->this$0:Lcom/airbnb/lottie/LottieTask;', 'invoke-virtual {p0}, Ljava/util/concurrent/FutureTask;->get()Ljava/lang/Object;', 'check-cast v1, Lcom/airbnb/lottie/LottieResult;', 'invoke-static {v0, v1}, Lcom/airbnb/lottie/LottieTask;->access$000(Lcom/airbnb/lottie/LottieTask;Lcom/airbnb/lottie/LottieResult;)V', 'return-void', 'iget-object p0, p0, Lcom/airbnb/lottie/LottieTask$LottieFutureTask;->this$0:Lcom/airbnb/lottie/LottieTask;'],
        'type': 'method_replace',
        'search': """.method protected done()V
    .registers 3

    invoke-virtual {p0}, Ljava/util/concurrent/FutureTask;->isCancelled()Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    :try_start_0
    iget-object v0, p0, Lcom/airbnb/lottie/LottieTask$LottieFutureTask;->this$0:Lcom/airbnb/lottie/LottieTask;

    invoke-virtual {p0}, Ljava/util/concurrent/FutureTask;->get()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/airbnb/lottie/LottieResult;

    invoke-static {v0, v1}, Lcom/airbnb/lottie/LottieTask;->access$000(Lcom/airbnb/lottie/LottieTask;Lcom/airbnb/lottie/LottieResult;)V
    :try_end_0
    .catch Ljava/lang/InterruptedException; {:try_start_0 .. :try_end_0} :catch_0
    .catch Ljava/util/concurrent/ExecutionException; {:try_start_0 .. :try_end_0} :catch_0

    return-void

    :catch_0
    move-exception v0

    iget-object p0, p0, Lcom/airbnb/lottie/LottieTask$LottieFutureTask;->this$0:Lcom/airbnb/lottie/LottieTask;

    new-instance v1, Lcom/airbnb/lottie/LottieResult;

    invoke-direct {v1, v0}, Lcom/airbnb/lottie/LottieResult;-><init>(Ljava/lang/Throwable;)V

    invoke-static {p0, v1}, Lcom/airbnb/lottie/LottieTask;->access$000(Lcom/airbnb/lottie/LottieTask;Lcom/airbnb/lottie/LottieResult;)V

    :goto_0
    return-void
.end method""",
        'replacement': """.method protected done()V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    return-void

    :goto_1
    invoke-static {p0, v1}, Lcom/airbnb/lottie/LottieTask;->access$000(Lcom/airbnb/lottie/LottieTask;Lcom/airbnb/lottie/LottieResult;)V

    :goto_2
    goto :goto_0

    nop

    :goto_3
    if-nez v0, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_9

    nop

    :goto_4
    invoke-virtual {p0}, Ljava/util/concurrent/FutureTask;->isCancelled()Z

    move-result v0

    goto :goto_3

    nop

    :goto_5
    iget-object p0, p0, Lcom/airbnb/lottie/LottieTask$LottieFutureTask;->this$0:Lcom/airbnb/lottie/LottieTask;

    goto :goto_8

    nop

    :goto_6
    return-void

    :catch_0
    move-exception v0

    goto :goto_5

    nop

    :goto_7
    invoke-direct {v1, v0}, Lcom/airbnb/lottie/LottieResult;-><init>(Ljava/lang/Throwable;)V

    goto :goto_1

    nop

    :goto_8
    new-instance v1, Lcom/airbnb/lottie/LottieResult;

    goto :goto_7

    nop

    :goto_9
    goto :goto_2

    :goto_a
    :try_start_0
    iget-object v0, p0, Lcom/airbnb/lottie/LottieTask$LottieFutureTask;->this$0:Lcom/airbnb/lottie/LottieTask;

    invoke-virtual {p0}, Ljava/util/concurrent/FutureTask;->get()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/airbnb/lottie/LottieResult;

    invoke-static {v0, v1}, Lcom/airbnb/lottie/LottieTask;->access$000(Lcom/airbnb/lottie/LottieTask;Lcom/airbnb/lottie/LottieResult;)V
    :try_end_0
    .catch Ljava/lang/InterruptedException; {:try_start_0 .. :try_end_0} :catch_0
    .catch Ljava/util/concurrent/ExecutionException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
