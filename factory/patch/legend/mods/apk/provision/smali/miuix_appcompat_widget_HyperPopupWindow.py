TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/widget/HyperPopupWindow.smali'
CLASS_FALLBACK_NAMES = ['HyperPopupWindow.smali']
CLASS_ANCHORS = ['.super Lmiuix/popupwidget/widget/PopupWindow;']

PATCHES = [
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__doCollapseAnimation',
        'method': '.method protected doCollapseAnimation()V',
        'method_name': 'doCollapseAnimation',
        'method_anchors': ['iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;', 'invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$000(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;', 'iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;', 'invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1200(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Lmiuix/smooth/SmoothFrameLayout2;', 'iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;', 'invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1300(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;', 'invoke-virtual/range {v25 .. v25}, Landroid/widget/FrameLayout;->getWidth()I', 'invoke-virtual {v2, v3}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->setMeasureWidth(I)V'],
        'type': 'method_replace',
        'search': """.method protected doCollapseAnimation()V
    .registers 29

    move-object/from16 v1, p0

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$000(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    move-result-object v0

    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1200(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Lmiuix/smooth/SmoothFrameLayout2;

    move-result-object v25

    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1300(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;

    move-result-object v2

    invoke-virtual/range {v25 .. v25}, Landroid/widget/FrameLayout;->getWidth()I

    move-result v3

    invoke-virtual {v2, v3}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->setMeasureWidth(I)V

    iget-object v0, v0, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;

    iget-object v3, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mMainPopContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v3}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1000(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Landroid/graphics/Rect;

    move-result-object v3

    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1000(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Landroid/graphics/Rect;

    move-result-object v4

    invoke-static {v3, v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->getUnionBounds(Landroid/graphics/Rect;Landroid/graphics/Rect;)Landroid/graphics/Rect;

    move-result-object v4

    invoke-virtual {v4}, Landroid/graphics/Rect;->width()I

    move-result v6

    invoke-virtual {v4}, Landroid/graphics/Rect;->height()I

    move-result v8

    iget v5, v3, Landroid/graphics/Rect;->left:I

    iget v7, v4, Landroid/graphics/Rect;->left:I

    sub-int/2addr v5, v7

    iget v7, v3, Landroid/graphics/Rect;->top:I

    iget v9, v4, Landroid/graphics/Rect;->top:I

    sub-int/2addr v7, v9

    invoke-virtual {v3}, Landroid/graphics/Rect;->width()I

    move-result v9

    add-int/2addr v9, v5

    invoke-virtual {v3}, Landroid/graphics/Rect;->height()I

    move-result v3

    add-int/2addr v3, v7

    invoke-virtual/range {v25 .. v25}, Landroid/widget/FrameLayout;->getLeft()I

    move-result v10

    invoke-virtual/range {v25 .. v25}, Landroid/widget/FrameLayout;->getTop()I

    move-result v12

    invoke-virtual/range {v25 .. v25}, Landroid/widget/FrameLayout;->getRight()I

    move-result v14

    invoke-virtual/range {v25 .. v25}, Landroid/widget/FrameLayout;->getBottom()I

    move-result v16

    iget v11, v0, Landroid/graphics/Rect;->left:I

    iget v13, v4, Landroid/graphics/Rect;->left:I

    sub-int/2addr v11, v13

    iget v15, v0, Landroid/graphics/Rect;->top:I

    iget v4, v4, Landroid/graphics/Rect;->top:I

    sub-int/2addr v15, v4

    move-object/from16 v24, v2

    iget v2, v0, Landroid/graphics/Rect;->right:I

    sub-int/2addr v2, v13

    iget v0, v0, Landroid/graphics/Rect;->bottom:I

    sub-int v17, v0, v4

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1400(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1500(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)I

    move-result v22

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1600(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)I

    move-result v23

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1700(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)I

    move-result v18

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1800(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)I

    move-result v19

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1900(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)I

    move-result v20

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$2000(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)I

    move-result v21

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$2100(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Landroid/widget/ListView;

    move-result-object v0

    const/4 v4, 0x0

    invoke-virtual {v0, v4}, Landroid/widget/ListView;->setScrollBarStyle(I)V

    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    const/4 v4, 0x1

    invoke-static {v0, v4}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$2202(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;Z)Z

    new-instance v0, Lmiuix/animation/base/AnimConfig;

    invoke-direct {v0}, Lmiuix/animation/base/AnimConfig;-><init>()V

    move-object v4, v0

    new-instance v0, Lmiuix/appcompat/widget/HyperPopupWindow$2;

    move v13, v15

    move v15, v2

    const/4 v2, 0x0

    move-object/from16 v26, v4

    const/4 v4, 0x0

    move/from16 v27, v9

    move v9, v3

    move v3, v5

    move v5, v7

    move/from16 v7, v27

    move-object/from16 v27, v26

    invoke-direct/range {v0 .. v25}, Lmiuix/appcompat/widget/HyperPopupWindow$2;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow;IIIIIIIIIIIIIIIIIIIIIILmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;Lmiuix/smooth/SmoothFrameLayout2;)V

    move-object v1, v0

    move-object/from16 v0, v25

    filled-new-array {v1}, [Lmiuix/animation/listener/TransitionListener;

    move-result-object v1

    move-object/from16 v4, v27

    invoke-virtual {v4, v1}, Lmiuix/animation/base/AnimConfig;->addListeners([Lmiuix/animation/listener/TransitionListener;)Lmiuix/animation/base/AnimConfig;

    move-result-object v1

    const/4 v2, 0x2

    new-array v2, v2, [F

    fill-array-data v2, :array_0

    const/4 v3, -0x2

    invoke-virtual {v1, v3, v2}, Lmiuix/animation/base/AnimConfig;->setEase(I[F)Lmiuix/animation/base/AnimConfig;

    filled-new-array/range {v24 .. v24}, [Ljava/lang/Object;

    move-result-object v2

    invoke-static {v2}, Lmiuix/animation/Folme;->useValue([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object v2

    const/4 v3, 0x0

    invoke-static {v3}, Ljava/lang/Float;->valueOf(F)Ljava/lang/Float;

    move-result-object v3

    const-string v4, "fraction"

    filled-new-array {v4, v3}, [Ljava/lang/Object;

    move-result-object v5

    invoke-interface {v2, v5}, Lmiuix/animation/FolmeStyle;->setTo([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object v2

    const/high16 v5, 0x3f800000

    invoke-static {v5}, Ljava/lang/Float;->valueOf(F)Ljava/lang/Float;

    move-result-object v5

    filled-new-array {v4, v5, v1}, [Ljava/lang/Object;

    move-result-object v1

    invoke-interface {v2, v1}, Lmiuix/animation/FolmeStyle;->to([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    invoke-virtual/range {v24 .. v24}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->getCornerRadius()F

    move-result v1

    invoke-virtual {v0, v1}, Lmiuix/smooth/SmoothFrameLayout2;->setCornerRadius(F)V

    filled-new-array/range {v24 .. v24}, [Ljava/lang/Object;

    move-result-object v0

    invoke-static {v0}, Lmiuix/animation/Folme;->useValue([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object v0

    invoke-static/range {v24 .. v24}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->access$2500(Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;)Lmiuix/animation/property/FloatProperty;

    move-result-object v1

    invoke-static {}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->access$2600()Lmiuix/animation/base/AnimConfig;

    move-result-object v2

    filled-new-array {v1, v3, v2}, [Ljava/lang/Object;

    move-result-object v1

    invoke-interface {v0, v1}, Lmiuix/animation/FolmeStyle;->to([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    filled-new-array/range {v24 .. v24}, [Ljava/lang/Object;

    move-result-object v0

    invoke-static {v0}, Lmiuix/animation/Folme;->useValue([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object v0

    invoke-static/range {v24 .. v24}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->access$2700(Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;)Lmiuix/animation/property/FloatProperty;

    move-result-object v1

    invoke-static/range {v24 .. v24}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->access$2800(Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;)Lmiuix/animation/base/AnimConfig;

    move-result-object v2

    filled-new-array {v1, v3, v2}, [Ljava/lang/Object;

    move-result-object v1

    invoke-interface {v0, v1}, Lmiuix/animation/FolmeStyle;->to([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    return-void

    nop

    :array_0
    .array-data 4
        0x3f733333
        0x3e4ccccd
    .end array-data
.end method""",
        'replacement': """.method protected doCollapseAnimation()V
    .registers 29

    goto :goto_a

    nop

    :goto_0
    move v13, v15

    goto :goto_43

    nop

    :goto_1
    invoke-virtual/range {v25 .. v25}, Landroid/widget/FrameLayout;->getRight()I

    move-result v14

    goto :goto_7

    nop

    :goto_2
    const/4 v3, -0x2

    goto :goto_5c

    nop

    :goto_3
    iget v11, v0, Landroid/graphics/Rect;->left:I

    goto :goto_4b

    nop

    :goto_4
    const/4 v4, 0x0

    goto :goto_6f

    nop

    :goto_5
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_41

    nop

    :goto_6
    invoke-static/range {v24 .. v24}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->access$2800(Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;)Lmiuix/animation/base/AnimConfig;

    move-result-object v2

    goto :goto_14

    nop

    :goto_7
    invoke-virtual/range {v25 .. v25}, Landroid/widget/FrameLayout;->getBottom()I

    move-result v16

    goto :goto_3

    nop

    :goto_8
    move v9, v3

    goto :goto_12

    nop

    :goto_9
    filled-new-array {v1, v3, v2}, [Ljava/lang/Object;

    move-result-object v1

    goto :goto_10

    nop

    :goto_a
    move-object/from16 v1, p0

    goto :goto_59

    nop

    :goto_b
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$2000(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)I

    move-result v21

    goto :goto_5

    nop

    :goto_c
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1600(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)I

    move-result v23

    goto :goto_3b

    nop

    :goto_d
    const/4 v2, 0x2

    goto :goto_3a

    nop

    :goto_e
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1400(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Landroid/view/View;

    move-result-object v0

    goto :goto_42

    nop

    :goto_f
    invoke-virtual {v4, v1}, Lmiuix/animation/base/AnimConfig;->addListeners([Lmiuix/animation/listener/TransitionListener;)Lmiuix/animation/base/AnimConfig;

    move-result-object v1

    goto :goto_d

    nop

    :goto_10
    invoke-interface {v0, v1}, Lmiuix/animation/FolmeStyle;->to([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    goto :goto_35

    nop

    :goto_11
    move-object/from16 v26, v4

    goto :goto_22

    nop

    :goto_12
    move v3, v5

    goto :goto_70

    nop

    :goto_13
    invoke-virtual/range {v25 .. v25}, Landroid/widget/FrameLayout;->getTop()I

    move-result v12

    goto :goto_1

    nop

    :goto_14
    filled-new-array {v1, v3, v2}, [Ljava/lang/Object;

    move-result-object v1

    goto :goto_30

    nop

    :goto_15
    invoke-static {v5}, Ljava/lang/Float;->valueOf(F)Ljava/lang/Float;

    move-result-object v5

    goto :goto_5f

    nop

    :goto_16
    const-string v4, "fraction"

    goto :goto_24

    nop

    :goto_17
    invoke-virtual/range {v25 .. v25}, Landroid/widget/FrameLayout;->getWidth()I

    move-result v3

    goto :goto_54

    nop

    :goto_18
    move/from16 v7, v27

    goto :goto_3e

    nop

    :goto_19
    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1200(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Lmiuix/smooth/SmoothFrameLayout2;

    move-result-object v25

    goto :goto_1a

    nop

    :goto_1a
    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_53

    nop

    :goto_1b
    iget v4, v4, Landroid/graphics/Rect;->top:I

    goto :goto_47

    nop

    :goto_1c
    move/from16 v27, v9

    goto :goto_8

    nop

    :goto_1d
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_c

    nop

    :goto_1e
    move-object/from16 v0, v25

    goto :goto_4f

    nop

    :goto_1f
    sub-int/2addr v7, v9

    goto :goto_56

    nop

    :goto_20
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_65

    nop

    :goto_21
    iget v5, v3, Landroid/graphics/Rect;->left:I

    goto :goto_6d

    nop

    :goto_22
    const/4 v4, 0x0

    goto :goto_1c

    nop

    :goto_23
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1700(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)I

    move-result v18

    goto :goto_57

    nop

    :goto_24
    filled-new-array {v4, v3}, [Ljava/lang/Object;

    move-result-object v5

    goto :goto_5b

    nop

    :goto_25
    add-int/2addr v3, v7

    goto :goto_5a

    nop

    :goto_26
    move-object/from16 v24, v2

    goto :goto_39

    nop

    :goto_27
    invoke-static {v3, v4}, Lmiuix/appcompat/widget/HyperPopupWindow;->getUnionBounds(Landroid/graphics/Rect;Landroid/graphics/Rect;)Landroid/graphics/Rect;

    move-result-object v4

    goto :goto_72

    nop

    :goto_28
    invoke-static {v2}, Lmiuix/animation/Folme;->useValue([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object v2

    goto :goto_29

    nop

    :goto_29
    const/4 v3, 0x0

    goto :goto_31

    nop

    :goto_2a
    sub-int v17, v0, v4

    goto :goto_32

    nop

    :goto_2b
    iget-object v3, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mMainPopContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_34

    nop

    :goto_2c
    iget v9, v4, Landroid/graphics/Rect;->top:I

    goto :goto_1f

    nop

    :goto_2d
    sub-int/2addr v11, v13

    goto :goto_40

    nop

    :goto_2e
    sub-int/2addr v2, v13

    goto :goto_68

    nop

    :goto_2f
    new-instance v0, Lmiuix/animation/base/AnimConfig;

    goto :goto_4c

    nop

    :goto_30
    invoke-interface {v0, v1}, Lmiuix/animation/FolmeStyle;->to([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    goto :goto_6c

    nop

    :goto_31
    invoke-static {v3}, Ljava/lang/Float;->valueOf(F)Ljava/lang/Float;

    move-result-object v3

    goto :goto_16

    nop

    :goto_32
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_e

    nop

    :goto_33
    invoke-static {}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->access$2600()Lmiuix/animation/base/AnimConfig;

    move-result-object v2

    goto :goto_9

    nop

    :goto_34
    invoke-static {v3}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1000(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Landroid/graphics/Rect;

    move-result-object v3

    goto :goto_60

    nop

    :goto_35
    filled-new-array/range {v24 .. v24}, [Ljava/lang/Object;

    move-result-object v0

    goto :goto_58

    nop

    :goto_36
    const/4 v2, 0x0

    goto :goto_11

    nop

    :goto_37
    invoke-direct/range {v0 .. v25}, Lmiuix/appcompat/widget/HyperPopupWindow$2;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow;IIIIIIIIIIIIIIIIIIIIIILmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;Lmiuix/smooth/SmoothFrameLayout2;)V

    goto :goto_51

    nop

    :goto_38
    invoke-virtual {v0, v1}, Lmiuix/smooth/SmoothFrameLayout2;->setCornerRadius(F)V

    goto :goto_48

    nop

    :goto_39
    iget v2, v0, Landroid/graphics/Rect;->right:I

    goto :goto_2e

    nop

    :goto_3a
    new-array v2, v2, [F

    fill-array-data v2, :array_0

    goto :goto_2

    nop

    :goto_3b
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_23

    nop

    :goto_3c
    iget-object v2, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_19

    nop

    :goto_3d
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_b

    nop

    :goto_3e
    move-object/from16 v27, v26

    goto :goto_37

    nop

    :goto_3f
    move-object v4, v0

    goto :goto_45

    nop

    :goto_40
    iget v15, v0, Landroid/graphics/Rect;->top:I

    goto :goto_1b

    nop

    :goto_41
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$2100(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Landroid/widget/ListView;

    move-result-object v0

    goto :goto_4

    nop

    :goto_42
    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_20

    nop

    :goto_43
    move v15, v2

    goto :goto_36

    nop

    :goto_44
    move-object/from16 v4, v27

    goto :goto_f

    nop

    :goto_45
    new-instance v0, Lmiuix/appcompat/widget/HyperPopupWindow$2;

    goto :goto_0

    nop

    :goto_46
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_4d

    nop

    :goto_47
    sub-int/2addr v15, v4

    goto :goto_26

    nop

    :goto_48
    filled-new-array/range {v24 .. v24}, [Ljava/lang/Object;

    move-result-object v0

    goto :goto_49

    nop

    :goto_49
    invoke-static {v0}, Lmiuix/animation/Folme;->useValue([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object v0

    goto :goto_55

    nop

    :goto_4a
    invoke-virtual/range {v24 .. v24}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->getCornerRadius()F

    move-result v1

    goto :goto_38

    nop

    :goto_4b
    iget v13, v4, Landroid/graphics/Rect;->left:I

    goto :goto_2d

    nop

    :goto_4c
    invoke-direct {v0}, Lmiuix/animation/base/AnimConfig;-><init>()V

    goto :goto_3f

    nop

    :goto_4d
    const/4 v4, 0x1

    goto :goto_50

    nop

    :goto_4e
    iget-object v0, v0, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;

    goto :goto_2b

    nop

    :goto_4f
    filled-new-array {v1}, [Lmiuix/animation/listener/TransitionListener;

    move-result-object v1

    goto :goto_44

    nop

    :goto_50
    invoke-static {v0, v4}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$2202(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;Z)Z

    goto :goto_2f

    nop

    :goto_51
    move-object v1, v0

    goto :goto_1e

    nop

    :goto_52
    invoke-virtual {v4}, Landroid/graphics/Rect;->height()I

    move-result v8

    goto :goto_21

    nop

    :goto_53
    invoke-static {v2}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1300(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;

    move-result-object v2

    goto :goto_17

    nop

    :goto_54
    invoke-virtual {v2, v3}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->setMeasureWidth(I)V

    goto :goto_4e

    nop

    :goto_55
    invoke-static/range {v24 .. v24}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->access$2500(Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;)Lmiuix/animation/property/FloatProperty;

    move-result-object v1

    goto :goto_33

    nop

    :goto_56
    invoke-virtual {v3}, Landroid/graphics/Rect;->width()I

    move-result v9

    goto :goto_63

    nop

    :goto_57
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_67

    nop

    :goto_58
    invoke-static {v0}, Lmiuix/animation/Folme;->useValue([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object v0

    goto :goto_61

    nop

    :goto_59
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_6e

    nop

    :goto_5a
    invoke-virtual/range {v25 .. v25}, Landroid/widget/FrameLayout;->getLeft()I

    move-result v10

    goto :goto_13

    nop

    :goto_5b
    invoke-interface {v2, v5}, Lmiuix/animation/FolmeStyle;->setTo([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object v2

    goto :goto_71

    nop

    :goto_5c
    invoke-virtual {v1, v3, v2}, Lmiuix/animation/base/AnimConfig;->setEase(I[F)Lmiuix/animation/base/AnimConfig;

    goto :goto_5e

    nop

    :goto_5d
    invoke-static {v4}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1000(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Landroid/graphics/Rect;

    move-result-object v4

    goto :goto_27

    nop

    :goto_5e
    filled-new-array/range {v24 .. v24}, [Ljava/lang/Object;

    move-result-object v2

    goto :goto_28

    nop

    :goto_5f
    filled-new-array {v4, v5, v1}, [Ljava/lang/Object;

    move-result-object v1

    goto :goto_6b

    nop

    :goto_60
    iget-object v4, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_5d

    nop

    :goto_61
    invoke-static/range {v24 .. v24}, Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;->access$2700(Lmiuix/appcompat/widget/HyperPopupWindow$ViewBounds;)Lmiuix/animation/property/FloatProperty;

    move-result-object v1

    goto :goto_6

    nop

    :goto_62
    iget v7, v3, Landroid/graphics/Rect;->top:I

    goto :goto_2c

    nop

    :goto_63
    add-int/2addr v9, v5

    goto :goto_64

    nop

    :goto_64
    invoke-virtual {v3}, Landroid/graphics/Rect;->height()I

    move-result v3

    goto :goto_25

    nop

    :goto_65
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1500(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)I

    move-result v22

    goto :goto_1d

    nop

    :goto_66
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1900(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)I

    move-result v20

    goto :goto_3d

    nop

    :goto_67
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1800(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)I

    move-result v19

    goto :goto_6a

    nop

    :goto_68
    iget v0, v0, Landroid/graphics/Rect;->bottom:I

    goto :goto_2a

    nop

    :goto_69
    sub-int/2addr v5, v7

    goto :goto_62

    nop

    :goto_6a
    iget-object v0, v1, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_66

    nop

    :goto_6b
    invoke-interface {v2, v1}, Lmiuix/animation/FolmeStyle;->to([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    goto :goto_4a

    nop

    :goto_6c
    return-void

    nop

    :array_0
    .array-data 4
        0x3f733333
        0x3e4ccccd
    .end array-data

    :goto_6d
    iget v7, v4, Landroid/graphics/Rect;->left:I

    goto :goto_69

    nop

    :goto_6e
    invoke-static {v0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$000(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    move-result-object v0

    goto :goto_3c

    nop

    :goto_6f
    invoke-virtual {v0, v4}, Landroid/widget/ListView;->setScrollBarStyle(I)V

    goto :goto_46

    nop

    :goto_70
    move v5, v7

    goto :goto_18

    nop

    :goto_71
    const/high16 v5, 0x3f800000

    goto :goto_15

    nop

    :goto_72
    invoke-virtual {v4}, Landroid/graphics/Rect;->width()I

    move-result v6

    goto :goto_52

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__doExpandAnimation',
        'method': '.method protected doExpandAnimation(Landroid/view/View;Landroid/widget/ListAdapter;)V',
        'method_name': 'doExpandAnimation',
        'method_anchors': ['iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;', 'invoke-virtual {v0}, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->clone()Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;', 'iget-object v0, v6, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;', 'invoke-static {p1, v0}, Lmiuix/internal/util/ViewUtils;->getBoundsInWindow(Landroid/view/View;Landroid/graphics/Rect;)V', 'iget-object v0, v6, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;', 'iget v1, v0, Landroid/graphics/Rect;->left:I', 'iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow;->mRootBounds:Landroid/graphics/Rect;', 'iget v3, v2, Landroid/graphics/Rect;->left:I'],
        'type': 'method_replace',
        'search': """.method protected doExpandAnimation(Landroid/view/View;Landroid/widget/ListAdapter;)V
    .registers 10

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    invoke-virtual {v0}, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->clone()Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    move-result-object v6

    iget-object v0, v6, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;

    invoke-static {p1, v0}, Lmiuix/internal/util/ViewUtils;->getBoundsInWindow(Landroid/view/View;Landroid/graphics/Rect;)V

    iget-object v0, v6, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;

    iget v1, v0, Landroid/graphics/Rect;->left:I

    iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow;->mRootBounds:Landroid/graphics/Rect;

    iget v3, v2, Landroid/graphics/Rect;->left:I

    add-int/2addr v1, v3

    iput v1, v0, Landroid/graphics/Rect;->left:I

    iget v1, v0, Landroid/graphics/Rect;->right:I

    iget v3, v2, Landroid/graphics/Rect;->left:I

    add-int/2addr v1, v3

    iput v1, v0, Landroid/graphics/Rect;->right:I

    iget v1, v0, Landroid/graphics/Rect;->top:I

    iget v4, v2, Landroid/graphics/Rect;->top:I

    add-int/2addr v1, v4

    iput v1, v0, Landroid/graphics/Rect;->top:I

    iget v1, v0, Landroid/graphics/Rect;->bottom:I

    iget v4, v2, Landroid/graphics/Rect;->top:I

    add-int/2addr v1, v4

    iput v1, v0, Landroid/graphics/Rect;->bottom:I

    iget-object v0, v6, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mDecorViewBounds:Landroid/graphics/Rect;

    iget v1, v2, Landroid/graphics/Rect;->right:I

    iget v2, v2, Landroid/graphics/Rect;->bottom:I

    invoke-virtual {v0, v3, v4, v1, v2}, Landroid/graphics/Rect;->set(IIII)V

    new-instance v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    iget-object v3, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    iget-object v5, p0, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryPopupStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    move-object v2, p0

    move-object v4, p2

    invoke-direct/range {v1 .. v6}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow;Landroid/content/Context;Landroid/widget/ListAdapter;Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V

    iput-object v1, v2, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-virtual {v1}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->inflate()V

    iget-object p0, v2, Lmiuix/appcompat/widget/HyperPopupWindow;->mMainPopContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-static {p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1200(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Lmiuix/smooth/SmoothFrameLayout2;

    move-result-object p0

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getWidth()I

    move-result p0

    iget-object p2, v2, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-virtual {p2, p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->setMinWidth(I)V

    iget-object p0, v2, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    iget-object p2, v2, Lmiuix/appcompat/widget/HyperPopupWindow;->mContainer:Landroid/view/ViewGroup;

    iget-object v0, v2, Lmiuix/appcompat/widget/HyperPopupWindow;->mRootBounds:Landroid/graphics/Rect;

    const/4 v1, 0x1

    invoke-virtual {p0, p1, p2, v0, v1}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->show(Landroid/view/View;Landroid/view/ViewGroup;Landroid/graphics/Rect;Z)Z

    return-void
.end method""",
        'replacement': """.method protected doExpandAnimation(Landroid/view/View;Landroid/widget/ListAdapter;)V
    .registers 10

    goto :goto_17

    nop

    :goto_0
    invoke-virtual {v0, v3, v4, v1, v2}, Landroid/graphics/Rect;->set(IIII)V

    goto :goto_6

    nop

    :goto_1
    iput v1, v0, Landroid/graphics/Rect;->bottom:I

    goto :goto_27

    nop

    :goto_2
    iget v4, v2, Landroid/graphics/Rect;->top:I

    goto :goto_1e

    nop

    :goto_3
    iget-object p2, v2, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_24

    nop

    :goto_4
    invoke-direct/range {v1 .. v6}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;-><init>(Lmiuix/appcompat/widget/HyperPopupWindow;Landroid/content/Context;Landroid/widget/ListAdapter;Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;)V

    goto :goto_11

    nop

    :goto_5
    invoke-virtual {v0}, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->clone()Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    move-result-object v6

    goto :goto_22

    nop

    :goto_6
    new-instance v1, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_8

    nop

    :goto_7
    iget v1, v0, Landroid/graphics/Rect;->top:I

    goto :goto_18

    nop

    :goto_8
    iget-object v3, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContext:Landroid/content/Context;

    goto :goto_b

    nop

    :goto_9
    iget v1, v0, Landroid/graphics/Rect;->left:I

    goto :goto_12

    nop

    :goto_a
    add-int/2addr v1, v4

    goto :goto_1a

    nop

    :goto_b
    iget-object v5, p0, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryPopupStrategy:Lmiuix/popupwidget/internal/strategy/IPopupWindowStrategy;

    goto :goto_d

    nop

    :goto_c
    add-int/2addr v1, v3

    goto :goto_19

    nop

    :goto_d
    move-object v2, p0

    goto :goto_10

    nop

    :goto_e
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getWidth()I

    move-result p0

    goto :goto_3

    nop

    :goto_f
    invoke-virtual {v1}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->inflate()V

    goto :goto_23

    nop

    :goto_10
    move-object v4, p2

    goto :goto_4

    nop

    :goto_11
    iput-object v1, v2, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_f

    nop

    :goto_12
    iget-object v2, p0, Lmiuix/appcompat/widget/HyperPopupWindow;->mRootBounds:Landroid/graphics/Rect;

    goto :goto_2c

    nop

    :goto_13
    return-void

    :goto_14
    invoke-static {p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->access$1200(Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;)Lmiuix/smooth/SmoothFrameLayout2;

    move-result-object p0

    goto :goto_e

    nop

    :goto_15
    iget v1, v0, Landroid/graphics/Rect;->right:I

    goto :goto_29

    nop

    :goto_16
    const/4 v1, 0x1

    goto :goto_1c

    nop

    :goto_17
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mPopupWindowSpec:Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;

    goto :goto_5

    nop

    :goto_18
    iget v4, v2, Landroid/graphics/Rect;->top:I

    goto :goto_a

    nop

    :goto_19
    iput v1, v0, Landroid/graphics/Rect;->left:I

    goto :goto_15

    nop

    :goto_1a
    iput v1, v0, Landroid/graphics/Rect;->top:I

    goto :goto_1d

    nop

    :goto_1b
    iput v1, v0, Landroid/graphics/Rect;->right:I

    goto :goto_7

    nop

    :goto_1c
    invoke-virtual {p0, p1, p2, v0, v1}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->show(Landroid/view/View;Landroid/view/ViewGroup;Landroid/graphics/Rect;Z)Z

    goto :goto_13

    nop

    :goto_1d
    iget v1, v0, Landroid/graphics/Rect;->bottom:I

    goto :goto_2

    nop

    :goto_1e
    add-int/2addr v1, v4

    goto :goto_1

    nop

    :goto_1f
    add-int/2addr v1, v3

    goto :goto_1b

    nop

    :goto_20
    iget v2, v2, Landroid/graphics/Rect;->bottom:I

    goto :goto_0

    nop

    :goto_21
    iget-object p2, v2, Lmiuix/appcompat/widget/HyperPopupWindow;->mContainer:Landroid/view/ViewGroup;

    goto :goto_2b

    nop

    :goto_22
    iget-object v0, v6, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;

    goto :goto_28

    nop

    :goto_23
    iget-object p0, v2, Lmiuix/appcompat/widget/HyperPopupWindow;->mMainPopContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_14

    nop

    :goto_24
    invoke-virtual {p2, p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->setMinWidth(I)V

    goto :goto_26

    nop

    :goto_25
    iget v1, v2, Landroid/graphics/Rect;->right:I

    goto :goto_20

    nop

    :goto_26
    iget-object p0, v2, Lmiuix/appcompat/widget/HyperPopupWindow;->mSecondaryContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_21

    nop

    :goto_27
    iget-object v0, v6, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mDecorViewBounds:Landroid/graphics/Rect;

    goto :goto_25

    nop

    :goto_28
    invoke-static {p1, v0}, Lmiuix/internal/util/ViewUtils;->getBoundsInWindow(Landroid/view/View;Landroid/graphics/Rect;)V

    goto :goto_2a

    nop

    :goto_29
    iget v3, v2, Landroid/graphics/Rect;->left:I

    goto :goto_1f

    nop

    :goto_2a
    iget-object v0, v6, Lmiuix/popupwidget/internal/strategy/PopupWindowSpec;->mAnchorViewBounds:Landroid/graphics/Rect;

    goto :goto_9

    nop

    :goto_2b
    iget-object v0, v2, Lmiuix/appcompat/widget/HyperPopupWindow;->mRootBounds:Landroid/graphics/Rect;

    goto :goto_16

    nop

    :goto_2c
    iget v3, v2, Landroid/graphics/Rect;->left:I

    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__prepareContentView',
        'method': '.method protected prepareContentView()V',
        'method_name': 'prepareContentView',
        'method_anchors': ['iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;', 'iget v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow;->mAnimationExtensionMargin:I', 'invoke-virtual {v0, v1, v1, v1, v1}, Landroid/widget/FrameLayout;->setPadding(IIII)V', 'invoke-super {p0}, Lmiuix/popupwidget/widget/PopupWindow;->prepareContentView()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected prepareContentView()V
    .registers 3

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;

    iget v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow;->mAnimationExtensionMargin:I

    invoke-virtual {v0, v1, v1, v1, v1}, Landroid/widget/FrameLayout;->setPadding(IIII)V

    invoke-super {p0}, Lmiuix/popupwidget/widget/PopupWindow;->prepareContentView()V

    return-void
.end method""",
        'replacement': """.method protected prepareContentView()V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    invoke-super {p0}, Lmiuix/popupwidget/widget/PopupWindow;->prepareContentView()V

    goto :goto_4

    nop

    :goto_1
    invoke-virtual {v0, v1, v1, v1, v1}, Landroid/widget/FrameLayout;->setPadding(IIII)V

    goto :goto_0

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mRootView:Landroid/widget/FrameLayout;

    goto :goto_3

    nop

    :goto_3
    iget v1, p0, Lmiuix/appcompat/widget/HyperPopupWindow;->mAnimationExtensionMargin:I

    goto :goto_1

    nop

    :goto_4
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__showWithAnim',
        'method': '.method protected showWithAnim(I)V',
        'method_name': 'showWithAnim',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mWindowAnimationEnabled:Z', 'if-nez v0, :cond_0', 'iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;', 'if-nez v0, :cond_0', 'iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;', 'sget v1, Lmiuix/appcompat/R$id;->spring_back:I', 'invoke-virtual {v0, v1}, Landroid/view/View;->findViewById(I)Landroid/view/View;', 'invoke-virtual {v0}, Landroid/view/View;->getParent()Landroid/view/ViewParent;'],
        'type': 'method_replace',
        'search': """.method protected showWithAnim(I)V
    .registers 4

    iget-boolean v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mWindowAnimationEnabled:Z

    if-nez v0, :cond_0

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    if-nez v0, :cond_0

    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    sget v1, Lmiuix/appcompat/R$id;->spring_back:I

    invoke-virtual {v0, v1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    check-cast v0, Landroid/view/View;

    new-instance v1, Lmiuix/popupwidget/widget/PopupAnimHelper;

    invoke-direct {v1, v0}, Lmiuix/popupwidget/widget/PopupAnimHelper;-><init>(Landroid/view/View;)V

    iput-object v1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    :cond_0
    invoke-super {p0, p1}, Lmiuix/popupwidget/widget/PopupWindow;->showWithAnim(I)V

    return-void
.end method""",
        'replacement': """.method protected showWithAnim(I)V
    .registers 4

    goto :goto_c

    nop

    :goto_0
    if-eqz v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_6

    nop

    :goto_1
    return-void

    :goto_2
    if-eqz v0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_e

    nop

    :goto_3
    sget v1, Lmiuix/appcompat/R$id;->spring_back:I

    goto :goto_9

    nop

    :goto_4
    iput-object v1, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    :goto_5
    goto :goto_8

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mContentView:Landroid/view/View;

    goto :goto_3

    nop

    :goto_7
    invoke-direct {v1, v0}, Lmiuix/popupwidget/widget/PopupAnimHelper;-><init>(Landroid/view/View;)V

    goto :goto_4

    nop

    :goto_8
    invoke-super {p0, p1}, Lmiuix/popupwidget/widget/PopupWindow;->showWithAnim(I)V

    goto :goto_1

    nop

    :goto_9
    invoke-virtual {v0, v1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_a

    nop

    :goto_a
    invoke-virtual {v0}, Landroid/view/View;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    goto :goto_d

    nop

    :goto_b
    new-instance v1, Lmiuix/popupwidget/widget/PopupAnimHelper;

    goto :goto_7

    nop

    :goto_c
    iget-boolean v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mWindowAnimationEnabled:Z

    goto :goto_2

    nop

    :goto_d
    check-cast v0, Landroid/view/View;

    goto :goto_b

    nop

    :goto_e
    iget-object v0, p0, Lmiuix/popupwidget/widget/PopupWindow;->mAnimHelper:Lmiuix/popupwidget/widget/PopupAnimHelper;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_widget_HyperPopupWindow__updateLocation',
        'method': '.method protected updateLocation(Landroid/view/View;)V',
        'method_name': 'updateLocation',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow;->mMainPopContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;', 'invoke-virtual {p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->update()Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected updateLocation(Landroid/view/View;)V
    .registers 2

    iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow;->mMainPopContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    invoke-virtual {p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->update()Z

    return-void
.end method""",
        'replacement': """.method protected updateLocation(Landroid/view/View;)V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;->update()Z

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/widget/HyperPopupWindow;->mMainPopContentHolder:Lmiuix/appcompat/widget/HyperPopupWindow$PopupContentHolder;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
