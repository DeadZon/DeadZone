"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView.smali
Patches      : 7
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView.smali'
CLASS_FALLBACK_NAMES = ['ModernStatusBarMobileView.smali']
CLASS_ANCHORS        = ['invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/pipeline/shared/ui/view/ModernStatusBarView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V', 'iput p1, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->subId:I', 'invoke-direct {p1, p0}, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;-><init>(Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;)V', 'iput-object p1, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->injector:Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;', 'invoke-static {p0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;']

PATCHES = [
    {
        'id':             'p0000_constructAndBind',
        'type':           'method_add',
        'method':         '.method public static constructAndBind(Landroid/content/Context;Lcom/android/systemui/statusbar/pipeline/mobile/ui/MobileViewLogger;Ljava/lang/String;Lcom/android/systemui/statusbar/pipeline/mobile/ui/viewmodel/LocationBasedMobileViewModel;Lcom/android/systemui/statusbar/pipeline/mobile/ui/viewmodel/MiuiMobileIconViewModel;)Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;',
        'method_name':    'constructAndBind',
        'method_anchors': ['invoke-static {p0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;', 'invoke-virtual {p0, v0, v1}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;', 'iget-object v0, p3, Lcom/android/systemui/statusbar/pipeline/mobile/ui/viewmodel/LocationBasedMobileViewModel;->commonImpl:Lcom/android/systemui/statusbar/pipeline/mobile/ui/viewmodel/MobileIconViewModelCommon;'],
        'search':         None,
        'replacement':    '.method public static constructAndBind(Landroid/content/Context;Lcom/android/systemui/statusbar/pipeline/mobile/ui/MobileViewLogger;Ljava/lang/String;Lcom/android/systemui/statusbar/pipeline/mobile/ui/viewmodel/LocationBasedMobileViewModel;Lcom/android/systemui/statusbar/pipeline/mobile/ui/viewmodel/MiuiMobileIconViewModel;)Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;\n    .registers 8\n\n    invoke-static {p0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;\n\n    move-result-object p0\n\n    const v0, 0x7f0e0466\n\n    const/4 v1, 0x0\n\n    invoke-virtual {p0, v0, v1}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;\n\n    move-result-object p0\n\n    check-cast p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;\n\n    iget-object v0, p3, Lcom/android/systemui/statusbar/pipeline/mobile/ui/viewmodel/LocationBasedMobileViewModel;->commonImpl:Lcom/android/systemui/statusbar/pipeline/mobile/ui/viewmodel/MobileIconViewModelCommon;\n\n    invoke-interface {v0}, Lcom/android/systemui/statusbar/pipeline/mobile/ui/viewmodel/MobileIconViewModelCommon;->getSubscriptionId()I\n\n    move-result v0\n\n    invoke-virtual {p0, v0}, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->setSubId(I)V\n\n    new-instance v0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView$Companion$$ExternalSyntheticLambda0;\n\n    invoke-direct {v0, p0, p3, p4, p1}, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView$Companion$$ExternalSyntheticLambda0;-><init>(Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;Lcom/android/systemui/statusbar/pipeline/mobile/ui/viewmodel/LocationBasedMobileViewModel;Lcom/android/systemui/statusbar/pipeline/mobile/ui/viewmodel/MiuiMobileIconViewModel;Lcom/android/systemui/statusbar/pipeline/mobile/ui/MobileViewLogger;)V\n\n    invoke-virtual {p0, p2, v0}, Lcom/android/systemui/statusbar/pipeline/shared/ui/view/ModernStatusBarView;->initView(Ljava/lang/String;Lkotlin/jvm/functions/Function0;)V\n\n    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;\n\n    iget-object p2, p3, Lcom/android/systemui/statusbar/pipeline/mobile/ui/viewmodel/LocationBasedMobileViewModel;->location:Lcom/android/systemui/statusbar/phone/StatusBarLocation;\n\n    invoke-virtual {p2}, Ljava/lang/Enum;->name()Ljava/lang/String;\n\n    move-result-object p2\n\n    sget-object p4, Lcom/android/systemui/log/core/LogLevel;->INFO:Lcom/android/systemui/log/core/LogLevel;\n\n    new-instance v0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/MobileViewLogger$$ExternalSyntheticLambda0;\n\n    const/4 v2, 0x1\n\n    invoke-direct {v0, v2}, Lcom/android/systemui/statusbar/pipeline/mobile/ui/MobileViewLogger$$ExternalSyntheticLambda0;-><init>(I)V\n\n    iget-object p1, p1, Lcom/android/systemui/statusbar/pipeline/mobile/ui/MobileViewLogger;->buffer:Lcom/android/systemui/log/LogBuffer;\n\n    const-string v2, "MobileViewLogger"\n\n    invoke-virtual {p1, v2, p4, v0, v1}, Lcom/android/systemui/log/LogBuffer;->obtain(Ljava/lang/String;Lcom/android/systemui/log/core/LogLevel;Lkotlin/jvm/functions/Function1;Ljava/lang/Throwable;)Lcom/android/systemui/log/core/LogMessage;\n\n    move-result-object p4\n\n    invoke-static {p0}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I\n\n    move-result v0\n\n    invoke-static {v0}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;\n\n    move-result-object v0\n\n    move-object v1, p4\n\n    check-cast v1, Lcom/android/systemui/log/LogMessageImpl;\n\n    iput-object v0, v1, Lcom/android/systemui/log/LogMessageImpl;->str1:Ljava/lang/String;\n\n    invoke-static {p3}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I\n\n    move-result p3\n\n    invoke-static {p3}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;\n\n    move-result-object p3\n\n    iput-object p3, v1, Lcom/android/systemui/log/LogMessageImpl;->str2:Ljava/lang/String;\n\n    iput-object p2, v1, Lcom/android/systemui/log/LogMessageImpl;->str3:Ljava/lang/String;\n\n    invoke-virtual {p1, p4}, Lcom/android/systemui/log/LogBuffer;->commit(Lcom/android/systemui/log/core/LogMessage;)V\n\n    return-object p0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0001_getInjector',
        'type':           'method_add',
        'method':         '.method public getInjector()Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;',
        'method_name':    'getInjector',
        'method_anchors': ['iget-object p0, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->injector:Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;'],
        'search':         None,
        'replacement':    '.method public getInjector()Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;\n    .registers 1\n\n    iget-object p0, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->injector:Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;\n\n    return-object p0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0002_getSubId',
        'type':           'method_add',
        'method':         '.method public getSubId()I',
        'method_name':    'getSubId',
        'method_anchors': ['iget p0, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->subId:I'],
        'search':         None,
        'replacement':    '.method public getSubId()I\n    .registers 1\n\n    iget p0, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->subId:I\n\n    return p0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0003_onFinishInflate',
        'type':           'method_add',
        'method':         '.method public onFinishInflate()V',
        'method_name':    'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V', 'iget-object p0, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->injector:Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;', 'iget-object v0, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;->mobileView:Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;'],
        'search':         None,
        'replacement':    '.method public onFinishInflate()V\n    .registers 3\n\n    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V\n\n    iget-object p0, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->injector:Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;->mobileView:Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;\n\n    const v1, 0x7f0b07ac\n\n    invoke-virtual {v0, v1}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;\n\n    move-result-object v1\n\n    check-cast v1, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorContainer;\n\n    iput-object v1, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;->container:Lcom/android/systemui/statusbar/views/MobileSignalAnimatorContainer;\n\n    if-eqz v1, :cond_0\n\n    iget-object p0, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;->animatable:Lcom/android/systemui/statusbar/views/MiuiStatusIconContainer;\n\n    invoke-virtual {v1, p0}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorContainer;->setAnimatable(Lcom/android/systemui/statusbar/views/IAnimatable;)V\n\n    invoke-virtual {v0}, Lcom/android/systemui/statusbar/pipeline/shared/ui/view/ModernStatusBarView;->getAnimHelper()Lcom/android/systemui/statusbar/anim/StatusBarIconAnimHelper;\n\n    move-result-object p0\n\n    invoke-virtual {v1, p0}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorContainer;->setParentAnimHelper(Lcom/android/systemui/statusbar/anim/StatusBarIconAnimHelper;)V\n\n    :cond_0\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0004_setSubId',
        'type':           'method_add',
        'method':         '.method public setSubId(I)V',
        'method_name':    'setSubId',
        'method_anchors': ['iput p1, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->subId:I'],
        'search':         None,
        'replacement':    '.method public setSubId(I)V\n    .registers 2\n\n    iput p1, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->subId:I\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0005_toString',
        'type':           'method_add',
        'method':         '.method public toString()Ljava/lang/String;',
        'method_name':    'toString',
        'method_anchors': ['invoke-virtual {p0}, Lcom/android/systemui/statusbar/pipeline/shared/ui/view/ModernStatusBarView;->getSlot()Ljava/lang/String;', 'iget v1, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->subId:I', 'invoke-virtual {p0}, Lcom/android/systemui/statusbar/pipeline/shared/ui/view/ModernStatusBarView;->getBinding$packages__apps__MiuiSystemUI__packages__SystemUI__android_common__MiuiSystemUI_core()Lcom/android/systemui/statusbar/pipeline/shared/ui/binder/ModernStatusBarViewBinding;'],
        'search':         None,
        'replacement':    '.method public toString()Ljava/lang/String;\n    .registers 8\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/pipeline/shared/ui/view/ModernStatusBarView;->getSlot()Ljava/lang/String;\n\n    move-result-object v0\n\n    iget v1, p0, Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileView;->subId:I\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/pipeline/shared/ui/view/ModernStatusBarView;->getBinding$packages__apps__MiuiSystemUI__packages__SystemUI__android_common__MiuiSystemUI_core()Lcom/android/systemui/statusbar/pipeline/shared/ui/binder/ModernStatusBarViewBinding;\n\n    move-result-object v2\n\n    invoke-interface {v2}, Lcom/android/systemui/statusbar/pipeline/shared/ui/binder/ModernStatusBarViewBinding;->isCollecting()Z\n\n    move-result v2\n\n    invoke-virtual {p0}, Lcom/android/systemui/statusbar/pipeline/shared/ui/view/ModernStatusBarView;->getVisibleState()I\n\n    move-result v3\n\n    invoke-static {v3}, Lcom/android/systemui/statusbar/StatusBarIconView;->getVisibleStateString(I)Ljava/lang/String;\n\n    move-result-object v3\n\n    invoke-super {p0}, Landroid/widget/FrameLayout;->toString()Ljava/lang/String;\n\n    move-result-object p0\n\n    const-string v4, "ModernStatusBarMobileView(slot=\\\'"\n\n    const-string v5, "\\\', subId="\n\n    const-string v6, ", isCollecting="\n\n    invoke-static {v1, v4, v0, v5, v6}, Landroidx/datastore/preferences/protobuf/ByteString$$ExternalSyntheticOutline0;->m(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    move-result-object v0\n\n    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;\n\n    const-string v1, ", visibleState="\n\n    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    const-string v1, "); viewString="\n\n    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n\n    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;\n\n    move-result-object p0\n\n    return-object p0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
    {
        'id':             'p0006_field__field_public_inject',
        'type':           'field_add',
        'method':         '.field public injector:Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field public injector:Lcom/android/systemui/statusbar/pipeline/mobile/ui/view/ModernStatusBarMobileViewInjector;',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added field',
    },
]
