"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/controlcenter/shade/ControlCenterHeaderView.smali
Patches      : 5
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/controlcenter/shade/ControlCenterHeaderView.smali'
CLASS_FALLBACK_NAMES = ['ControlCenterHeaderView.smali']
CLASS_ANCHORS        = ['invoke-direct {p0, p1, v0}, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V', 'invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V', 'invoke-direct {p0, p1, p2, p3}, Landroidx/constraintlayout/widget/ConstraintLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V', 'invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;', 'iput-object v0, p0, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;']

PATCHES = [
    {
        'id':             'p0000__init_',
        'type':           'method_replace',
        'method':         '.method public constructor <init>(Landroid/content/Context;)V',
        'method_name':    '<init>',
        'method_anchors': ['invoke-direct {p0, p1, v0}, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V'],
        'search':         '.method public constructor <init>(Landroid/content/Context;)V\n    .registers 8\n\n    const/4 v4, 0x6\n\n    const/4 v5, 0x0\n\n    const/4 v2, 0x0\n\n    const/4 v3, 0x0\n\n    move-object v0, p0\n\n    move-object v1, p1\n\n    invoke-direct/range {v0 .. v5}, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;IILkotlin/jvm/internal/DefaultConstructorMarker;)V\n\n    return-void\n.end method\n',
        'replacement':    '.method public constructor <init>(Landroid/content/Context;)V\n    .registers 3\n\n    const/4 v0, 0x0\n\n    invoke-direct {p0, p1, v0}, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI generated generated dex rule modified class',
    },
    {
        'id':             'p0001__init_',
        'type':           'method_replace',
        'method':         '.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V',
        'method_name':    '<init>',
        'method_anchors': ['invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V'],
        'search':         '.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 9\n\n    const/4 v4, 0x4\n\n    const/4 v5, 0x0\n\n    const/4 v3, 0x0\n\n    move-object v0, p0\n\n    move-object v1, p1\n\n    move-object v2, p2\n\n    invoke-direct/range {v0 .. v5}, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;IILkotlin/jvm/internal/DefaultConstructorMarker;)V\n\n    return-void\n.end method\n',
        'replacement':    '.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V\n    .registers 4\n\n    const/4 v0, 0x0\n\n    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI generated generated dex rule modified class',
    },
    {
        'id':             'p0002__init_',
        'type':           'method_replace',
        'method':         '.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V',
        'method_name':    '<init>',
        'method_anchors': ['invoke-direct {p0, p1, p2, p3}, Landroidx/constraintlayout/widget/ConstraintLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V', 'invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;', 'iput-object v0, p0, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;'],
        'search':         '.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 4\n\n    invoke-direct {p0, p1, p2, p3}, Landroidx/constraintlayout/widget/ConstraintLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    return-void\n.end method\n',
        'replacement':    '.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n    .registers 5\n\n    invoke-direct {p0, p1, p2, p3}, Landroidx/constraintlayout/widget/ConstraintLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V\n\n    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;\n\n    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;\n\n    iput-object v0, p0, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI generated generated dex rule modified class',
    },
    {
        'id':             'p0003_onMeasure',
        'type':           'method_add',
        'method':         '.method public onMeasure(II)V',
        'method_name':    'onMeasure',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroidx/constraintlayout/widget/ConstraintLayout;->onMeasure(II)V', 'iget-object v0, p0, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;', 'invoke-virtual {p0}, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;->getMeasuredWidth()I'],
        'search':         None,
        'replacement':    '.method public onMeasure(II)V\n    .registers 5\n\n    invoke-super {p0, p1, p2}, Landroidx/constraintlayout/widget/ConstraintLayout;->onMeasure(II)V\n\n    iget-object v0, p0, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;\n\n    if-eqz v0, :cond_0\n\n    invoke-virtual {p0}, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;->getMeasuredWidth()I\n\n    move-result v0\n\n    iget-object v1, p0, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;\n\n    iget v1, v1, Lcom/android/systemui/newstatusbar/controllers/ElementController;->statusBarHeight:I\n\n    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/controlcenter/shade/ControlCenterHeaderView;->setMeasuredDimension(II)V\n\n    :cond_0\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0004_field__field_private_final',
        'type':           'field_add',
        'method':         '.field private final controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field private final controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added field',
    },
]
