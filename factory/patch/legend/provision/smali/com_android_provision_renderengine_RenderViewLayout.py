TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/renderengine/RenderViewLayout.smali'
CLASS_FALLBACK_NAMES = ['RenderViewLayout.smali']
CLASS_ANCHORS = ['.super Landroid/view/ViewGroup;']

PATCHES = [
    {
        'id': 'com_android_provision_renderengine_RenderViewLayout__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-virtual {p0}, Landroid/view/ViewGroup;->getChildCount()I', 'if-nez p1, :cond_0', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getWidth()I', 'iget p3, p0, Lcom/android/provision/renderengine/RenderViewLayout;->mChildScale:F', 'invoke-static {p2, p3}, Ljava/lang/Math;->ceil(D)D', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getHeight()I', 'iget p4, p0, Lcom/android/provision/renderengine/RenderViewLayout;->mChildScale:F', 'invoke-static {p3, p4}, Ljava/lang/Math;->ceil(D)D'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 10

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result p1

    if-nez p1, :cond_0

    goto :goto_1

    :cond_0
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getWidth()I

    move-result p2

    int-to-float p2, p2

    iget p3, p0, Lcom/android/provision/renderengine/RenderViewLayout;->mChildScale:F

    mul-float/2addr p2, p3

    float-to-double p2, p2

    invoke-static {p2, p3}, Ljava/lang/Math;->ceil(D)D

    move-result-wide p2

    double-to-int p2, p2

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getHeight()I

    move-result p3

    int-to-float p3, p3

    iget p4, p0, Lcom/android/provision/renderengine/RenderViewLayout;->mChildScale:F

    mul-float/2addr p3, p4

    float-to-double p3, p3

    invoke-static {p3, p4}, Ljava/lang/Math;->ceil(D)D

    move-result-wide p3

    double-to-int p3, p3

    const/4 p4, 0x0

    :goto_0
    if-ge p4, p1, :cond_2

    invoke-virtual {p0, p4}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object p5

    invoke-virtual {p5}, Landroid/view/View;->getVisibility()I

    move-result v0

    const/16 v1, 0x8

    if-eq v0, v1, :cond_1

    iget v0, p0, Lcom/android/provision/renderengine/RenderViewLayout;->mChildScale:F

    const/high16 v1, 0x3f800000

    div-float v0, v1, v0

    invoke-virtual {p5, v0}, Landroid/view/View;->setScaleX(F)V

    iget v0, p0, Lcom/android/provision/renderengine/RenderViewLayout;->mChildScale:F

    div-float/2addr v1, v0

    invoke-virtual {p5, v1}, Landroid/view/View;->setScaleY(F)V

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getWidth()I

    move-result v0

    sub-int/2addr v0, p2

    int-to-float v0, v0

    const/high16 v1, 0x3f000000

    mul-float/2addr v0, v1

    float-to-int v0, v0

    add-int v2, v0, p2

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getHeight()I

    move-result v3

    sub-int/2addr v3, p3

    int-to-float v3, v3

    mul-float/2addr v3, v1

    float-to-int v1, v3

    add-int v3, v1, p3

    invoke-virtual {p5, v0, v1, v2, v3}, Landroid/view/View;->layout(IIII)V

    :cond_1
    add-int/lit8 p4, p4, 0x1

    goto :goto_0

    :cond_2
    :goto_1
    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 10

    goto :goto_7

    nop

    :goto_0
    const/16 v1, 0x8

    goto :goto_a

    nop

    :goto_1
    iget v0, p0, Lcom/android/provision/renderengine/RenderViewLayout;->mChildScale:F

    goto :goto_9

    nop

    :goto_2
    float-to-int v1, v3

    goto :goto_1f

    nop

    :goto_3
    mul-float/2addr p2, p3

    goto :goto_2a

    nop

    :goto_4
    invoke-virtual {p5, v0}, Landroid/view/View;->setScaleX(F)V

    goto :goto_1

    nop

    :goto_5
    iget v0, p0, Lcom/android/provision/renderengine/RenderViewLayout;->mChildScale:F

    goto :goto_b

    nop

    :goto_6
    if-lt p4, p1, :cond_0

    goto :goto_1a

    :cond_0
    goto :goto_16

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result p1

    goto :goto_30

    nop

    :goto_8
    double-to-int p3, p3

    goto :goto_f

    nop

    :goto_9
    div-float/2addr v1, v0

    goto :goto_1b

    nop

    :goto_a
    if-ne v0, v1, :cond_1

    goto :goto_27

    :cond_1
    goto :goto_5

    nop

    :goto_b
    const/high16 v1, 0x3f800000

    goto :goto_11

    nop

    :goto_c
    float-to-double p3, p3

    goto :goto_2e

    nop

    :goto_d
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getHeight()I

    move-result v3

    goto :goto_22

    nop

    :goto_e
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getWidth()I

    move-result v0

    goto :goto_1e

    nop

    :goto_f
    const/4 p4, 0x0

    :goto_10
    goto :goto_6

    nop

    :goto_11
    div-float v0, v1, v0

    goto :goto_4

    nop

    :goto_12
    const/high16 v1, 0x3f000000

    goto :goto_25

    nop

    :goto_13
    mul-float/2addr v3, v1

    goto :goto_2

    nop

    :goto_14
    goto :goto_1a

    :goto_15
    goto :goto_32

    nop

    :goto_16
    invoke-virtual {p0, p4}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object p5

    goto :goto_24

    nop

    :goto_17
    float-to-int v0, v0

    goto :goto_28

    nop

    :goto_18
    return-void

    :goto_19
    goto :goto_10

    :goto_1a
    goto :goto_18

    nop

    :goto_1b
    invoke-virtual {p5, v1}, Landroid/view/View;->setScaleY(F)V

    goto :goto_e

    nop

    :goto_1c
    add-int/lit8 p4, p4, 0x1

    goto :goto_19

    nop

    :goto_1d
    int-to-float v3, v3

    goto :goto_13

    nop

    :goto_1e
    sub-int/2addr v0, p2

    goto :goto_23

    nop

    :goto_1f
    add-int v3, v1, p3

    goto :goto_26

    nop

    :goto_20
    iget p3, p0, Lcom/android/provision/renderengine/RenderViewLayout;->mChildScale:F

    goto :goto_3

    nop

    :goto_21
    double-to-int p2, p2

    goto :goto_2b

    nop

    :goto_22
    sub-int/2addr v3, p3

    goto :goto_1d

    nop

    :goto_23
    int-to-float v0, v0

    goto :goto_12

    nop

    :goto_24
    invoke-virtual {p5}, Landroid/view/View;->getVisibility()I

    move-result v0

    goto :goto_0

    nop

    :goto_25
    mul-float/2addr v0, v1

    goto :goto_17

    nop

    :goto_26
    invoke-virtual {p5, v0, v1, v2, v3}, Landroid/view/View;->layout(IIII)V

    :goto_27
    goto :goto_1c

    nop

    :goto_28
    add-int v2, v0, p2

    goto :goto_d

    nop

    :goto_29
    mul-float/2addr p3, p4

    goto :goto_c

    nop

    :goto_2a
    float-to-double p2, p2

    goto :goto_2f

    nop

    :goto_2b
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getHeight()I

    move-result p3

    goto :goto_2d

    nop

    :goto_2c
    iget p4, p0, Lcom/android/provision/renderengine/RenderViewLayout;->mChildScale:F

    goto :goto_29

    nop

    :goto_2d
    int-to-float p3, p3

    goto :goto_2c

    nop

    :goto_2e
    invoke-static {p3, p4}, Ljava/lang/Math;->ceil(D)D

    move-result-wide p3

    goto :goto_8

    nop

    :goto_2f
    invoke-static {p2, p3}, Ljava/lang/Math;->ceil(D)D

    move-result-wide p2

    goto :goto_21

    nop

    :goto_30
    if-eqz p1, :cond_2

    goto :goto_15

    :cond_2
    goto :goto_14

    nop

    :goto_31
    int-to-float p2, p2

    goto :goto_20

    nop

    :goto_32
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getWidth()I

    move-result p2

    goto :goto_31

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
