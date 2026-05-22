TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'androidx/recyclerview/widget/SpringRecyclerView.smali'
CLASS_FALLBACK_NAMES = ['SpringRecyclerView.smali']
CLASS_ANCHORS = ['.super Landroidx/recyclerview/widget/RemixRecyclerView;', '.field private static final NESTED_SCROLL_HELPER:Ljava/lang/reflect/Field;', '.field private static final NON_EFFECT_FACTORY:Landroidx/recyclerview/widget/RecyclerView$EdgeEffectFactory;', '.field private static final VIEW_FLINGER:Ljava/lang/reflect/Field;']

PATCHES = [
    {
        'id': 'androidx_recyclerview_widget_SpringRecyclerView__init',
        'method': '.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V',
        'method_name': '<init>',
        'method_anchors': ['invoke-direct {p0, p1, p2, p3}, Landroidx/recyclerview/widget/RemixRecyclerView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V', 'new-instance p1, Ljava/util/ArrayList;', 'invoke-direct {p1}, Ljava/util/ArrayList;-><init>()V', 'iput-object p1, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringStateListeners:Ljava/util/List;', 'iput p1, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringX:F', 'iput p1, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringY:F', 'iput p1, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mManagedScrollState:I', 'new-instance p2, Landroidx/recyclerview/widget/SpringRecyclerView$1;'],
        'type': 'method_replace',
        'search': """.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 4

    invoke-direct {p0, p1, p2, p3}, Landroidx/recyclerview/widget/RemixRecyclerView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    new-instance p1, Ljava/util/ArrayList;

    invoke-direct {p1}, Ljava/util/ArrayList;-><init>()V

    iput-object p1, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringStateListeners:Ljava/util/List;

    const/4 p1, 0x0

    iput p1, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringX:F

    iput p1, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringY:F

    const/4 p1, 0x0

    iput p1, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mManagedScrollState:I

    new-instance p2, Landroidx/recyclerview/widget/SpringRecyclerView$1;

    invoke-direct {p2, p0}, Landroidx/recyclerview/widget/SpringRecyclerView$1;-><init>(Landroidx/recyclerview/widget/SpringRecyclerView;)V

    iput-object p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringHelper:Lmiuix/spring/view/SpringHelper;

    sget-boolean p2, Lmiuix/os/Build;->IS_INTERNATIONAL_BUILD:Z

    iput-boolean p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mInGlobalRomMode:Z

    new-instance p2, Landroidx/recyclerview/widget/SpringRecyclerView$SpringFlinger;

    const/4 p3, 0x0

    invoke-direct {p2, p0, p3}, Landroidx/recyclerview/widget/SpringRecyclerView$SpringFlinger;-><init>(Landroidx/recyclerview/widget/SpringRecyclerView;Landroidx/recyclerview/widget/SpringRecyclerView$1;)V

    iput-object p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringFlinger:Landroidx/recyclerview/widget/SpringRecyclerView$SpringFlinger;

    new-instance p2, Landroidx/recyclerview/widget/SpringRecyclerView$SpringNestedScrollingHelper;

    invoke-direct {p2, p0, p0}, Landroidx/recyclerview/widget/SpringRecyclerView$SpringNestedScrollingHelper;-><init>(Landroidx/recyclerview/widget/SpringRecyclerView;Landroid/view/View;)V

    iput-object p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringNestedScrollingHelper:Landroidx/recyclerview/widget/SpringRecyclerView$SpringNestedScrollingHelper;

    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView;->isNestedScrollingEnabled()Z

    move-result p3

    invoke-virtual {p2, p3}, Landroidx/core/view/NestedScrollingChildHelper;->setNestedScrollingEnabled(Z)V

    iget-object p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringFlinger:Landroidx/recyclerview/widget/SpringRecyclerView$SpringFlinger;

    invoke-direct {p0, p2}, Landroidx/recyclerview/widget/SpringRecyclerView;->replaceViewFlinger(Landroidx/recyclerview/widget/RemixRecyclerView$ViewFlinger;)V

    iget-object p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringNestedScrollingHelper:Landroidx/recyclerview/widget/SpringRecyclerView$SpringNestedScrollingHelper;

    invoke-direct {p0, p2}, Landroidx/recyclerview/widget/SpringRecyclerView;->replaceNestedScrollingHelper(Landroidx/core/view/NestedScrollingChildHelper;)V

    iget-boolean p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mInGlobalRomMode:Z

    if-eqz p2, :cond_0

    invoke-virtual {p0, p1}, Landroidx/recyclerview/widget/SpringRecyclerView;->setSpringEnabled(Z)V

    return-void

    :cond_0
    sget-object p1, Landroidx/recyclerview/widget/SpringRecyclerView;->NON_EFFECT_FACTORY:Landroidx/recyclerview/widget/RecyclerView$EdgeEffectFactory;

    invoke-super {p0, p1}, Landroidx/recyclerview/widget/RecyclerView;->setEdgeEffectFactory(Landroidx/recyclerview/widget/RecyclerView$EdgeEffectFactory;)V

    return-void
.end method""",
        'replacement': """.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 4

    invoke-direct {p0, p1, p2, p3}, Landroidx/recyclerview/widget/RemixRecyclerView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    new-instance p1, Ljava/util/ArrayList;

    invoke-direct {p1}, Ljava/util/ArrayList;-><init>()V

    iput-object p1, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringStateListeners:Ljava/util/List;

    const/4 p1, 0x0

    iput p1, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringX:F

    iput p1, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringY:F

    const/4 p1, 0x0

    iput p1, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mManagedScrollState:I

    new-instance p2, Landroidx/recyclerview/widget/SpringRecyclerView$1;

    invoke-direct {p2, p0}, Landroidx/recyclerview/widget/SpringRecyclerView$1;-><init>(Landroidx/recyclerview/widget/SpringRecyclerView;)V

    iput-object p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringHelper:Lmiuix/spring/view/SpringHelper;

    sget-boolean p2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    iput-boolean p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mInGlobalRomMode:Z

    new-instance p2, Landroidx/recyclerview/widget/SpringRecyclerView$SpringFlinger;

    const/4 p3, 0x0

    invoke-direct {p2, p0, p3}, Landroidx/recyclerview/widget/SpringRecyclerView$SpringFlinger;-><init>(Landroidx/recyclerview/widget/SpringRecyclerView;Landroidx/recyclerview/widget/SpringRecyclerView$1;)V

    iput-object p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringFlinger:Landroidx/recyclerview/widget/SpringRecyclerView$SpringFlinger;

    new-instance p2, Landroidx/recyclerview/widget/SpringRecyclerView$SpringNestedScrollingHelper;

    invoke-direct {p2, p0, p0}, Landroidx/recyclerview/widget/SpringRecyclerView$SpringNestedScrollingHelper;-><init>(Landroidx/recyclerview/widget/SpringRecyclerView;Landroid/view/View;)V

    iput-object p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringNestedScrollingHelper:Landroidx/recyclerview/widget/SpringRecyclerView$SpringNestedScrollingHelper;

    invoke-virtual {p0}, Landroidx/recyclerview/widget/RecyclerView;->isNestedScrollingEnabled()Z

    move-result p3

    invoke-virtual {p2, p3}, Landroidx/core/view/NestedScrollingChildHelper;->setNestedScrollingEnabled(Z)V

    iget-object p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringFlinger:Landroidx/recyclerview/widget/SpringRecyclerView$SpringFlinger;

    invoke-direct {p0, p2}, Landroidx/recyclerview/widget/SpringRecyclerView;->replaceViewFlinger(Landroidx/recyclerview/widget/RemixRecyclerView$ViewFlinger;)V

    iget-object p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mSpringNestedScrollingHelper:Landroidx/recyclerview/widget/SpringRecyclerView$SpringNestedScrollingHelper;

    invoke-direct {p0, p2}, Landroidx/recyclerview/widget/SpringRecyclerView;->replaceNestedScrollingHelper(Landroidx/core/view/NestedScrollingChildHelper;)V

    iget-boolean p2, p0, Landroidx/recyclerview/widget/SpringRecyclerView;->mInGlobalRomMode:Z

    if-eqz p2, :cond_0

    invoke-virtual {p0, p1}, Landroidx/recyclerview/widget/SpringRecyclerView;->setSpringEnabled(Z)V

    return-void

    :cond_0
    sget-object p1, Landroidx/recyclerview/widget/SpringRecyclerView;->NON_EFFECT_FACTORY:Landroidx/recyclerview/widget/RecyclerView$EdgeEffectFactory;

    invoke-super {p0, p1}, Landroidx/recyclerview/widget/RecyclerView;->setEdgeEffectFactory(Landroidx/recyclerview/widget/RecyclerView$EdgeEffectFactory;)V

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
