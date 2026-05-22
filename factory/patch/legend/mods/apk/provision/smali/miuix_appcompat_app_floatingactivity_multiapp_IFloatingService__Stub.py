TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/floatingactivity/multiapp/IFloatingService$Stub.smali'
CLASS_FALLBACK_NAMES = ['IFloatingService$Stub.smali']
CLASS_ANCHORS = ['.super Landroid/os/Binder;', '.implements Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_floatingactivity_multiapp_IFloatingService__Stub__onTransact',
        'method': '.method protected onTransact(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z',
        'method_name': 'onTransact',
        'method_anchors': ['if-nez p3, :cond_0', 'invoke-super {p0, p1, p2, p3, p4}, Landroid/os/Binder;->onTransact(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z', 'return p0', 'const-string v2, "miuix.appcompat.app.floatingactivity.multiapp.IFloatingService"', 'if-eq p1, v0, :cond_5', 'if-eq p1, v0, :cond_4', 'if-eq p1, v0, :cond_3', 'if-eq p1, v0, :cond_2'],
        'type': 'method_replace',
        'search': """.method protected onTransact(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z
    .registers 8

    if-nez p3, :cond_0

    const/4 p3, 0x0

    invoke-super {p0, p1, p2, p3, p4}, Landroid/os/Binder;->onTransact(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z

    move-result p0

    return p0

    :cond_0
    const/4 v0, 0x2

    const/4 v1, 0x1

    const-string v2, "miuix.appcompat.app.floatingactivity.multiapp.IFloatingService"

    if-eq p1, v0, :cond_5

    const/4 v0, 0x3

    if-eq p1, v0, :cond_4

    const/4 v0, 0x4

    if-eq p1, v0, :cond_3

    const/4 v0, 0x5

    if-eq p1, v0, :cond_2

    const v0, 0x5f4e5446

    if-eq p1, v0, :cond_1

    invoke-super {p0, p1, p2, p3, p4}, Landroid/os/Binder;->onTransact(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z

    move-result p0

    return p0

    :cond_1
    invoke-virtual {p3, v2}, Landroid/os/Parcel;->writeString(Ljava/lang/String;)V

    return v1

    :cond_2
    invoke-virtual {p2, v2}, Landroid/os/Parcel;->enforceInterface(Ljava/lang/String;)V

    invoke-virtual {p2}, Landroid/os/Parcel;->readString()Ljava/lang/String;

    move-result-object p1

    invoke-virtual {p2}, Landroid/os/Parcel;->readInt()I

    move-result p2

    invoke-interface {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;->upDateRemoteActivityInfo(Ljava/lang/String;I)V

    invoke-virtual {p3}, Landroid/os/Parcel;->writeNoException()V

    return v1

    :cond_3
    invoke-virtual {p2, v2}, Landroid/os/Parcel;->enforceInterface(Ljava/lang/String;)V

    invoke-virtual {p2}, Landroid/os/Parcel;->readStrongBinder()Landroid/os/IBinder;

    move-result-object p1

    invoke-static {p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify$Stub;->asInterface(Landroid/os/IBinder;)Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify;

    move-result-object p1

    invoke-virtual {p2}, Landroid/os/Parcel;->readString()Ljava/lang/String;

    move-result-object p2

    invoke-interface {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;->unregisterServiceNotify(Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify;Ljava/lang/String;)V

    invoke-virtual {p3}, Landroid/os/Parcel;->writeNoException()V

    return v1

    :cond_4
    invoke-virtual {p2, v2}, Landroid/os/Parcel;->enforceInterface(Ljava/lang/String;)V

    invoke-virtual {p2}, Landroid/os/Parcel;->readStrongBinder()Landroid/os/IBinder;

    move-result-object p1

    invoke-static {p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify$Stub;->asInterface(Landroid/os/IBinder;)Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify;

    move-result-object p1

    invoke-virtual {p2}, Landroid/os/Parcel;->readString()Ljava/lang/String;

    move-result-object p2

    invoke-interface {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;->registerServiceNotify(Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify;Ljava/lang/String;)I

    move-result p0

    invoke-virtual {p3, p0}, Landroid/os/Parcel;->writeInt(I)V

    invoke-virtual {p3}, Landroid/os/Parcel;->writeNoException()V

    return v1

    :cond_5
    invoke-virtual {p2, v2}, Landroid/os/Parcel;->enforceInterface(Ljava/lang/String;)V

    invoke-virtual {p2}, Landroid/os/Parcel;->readInt()I

    move-result p1

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p4

    invoke-virtual {p4}, Ljava/lang/Class;->getClassLoader()Ljava/lang/ClassLoader;

    move-result-object p4

    invoke-virtual {p2, p4}, Landroid/os/Parcel;->readBundle(Ljava/lang/ClassLoader;)Landroid/os/Bundle;

    move-result-object p2

    invoke-interface {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;->callServiceMethod(ILandroid/os/Bundle;)Landroid/os/Bundle;

    move-result-object p0

    invoke-virtual {p3, p0}, Landroid/os/Parcel;->writeBundle(Landroid/os/Bundle;)V

    invoke-virtual {p3}, Landroid/os/Parcel;->writeNoException()V

    return v1
.end method""",
        'replacement': """.method protected onTransact(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z
    .registers 8

    goto :goto_21

    nop

    :goto_0
    invoke-virtual {p2, v2}, Landroid/os/Parcel;->enforceInterface(Ljava/lang/String;)V

    goto :goto_d

    nop

    :goto_1
    invoke-virtual {p3}, Landroid/os/Parcel;->writeNoException()V

    goto :goto_1a

    nop

    :goto_2
    const-string v2, "miuix.appcompat.app.floatingactivity.multiapp.IFloatingService"

    goto :goto_15

    nop

    :goto_3
    return p0

    :goto_4
    goto :goto_8

    nop

    :goto_5
    const/4 p3, 0x0

    goto :goto_12

    nop

    :goto_6
    invoke-virtual {p3}, Landroid/os/Parcel;->writeNoException()V

    goto :goto_22

    nop

    :goto_7
    const/4 v0, 0x3

    goto :goto_24

    nop

    :goto_8
    invoke-virtual {p3, v2}, Landroid/os/Parcel;->writeString(Ljava/lang/String;)V

    goto :goto_1f

    nop

    :goto_9
    invoke-virtual {p3}, Landroid/os/Parcel;->writeNoException()V

    goto :goto_18

    nop

    :goto_a
    invoke-virtual {p2, v2}, Landroid/os/Parcel;->enforceInterface(Ljava/lang/String;)V

    goto :goto_11

    nop

    :goto_b
    invoke-virtual {p3}, Landroid/os/Parcel;->writeNoException()V

    goto :goto_31

    nop

    :goto_c
    invoke-virtual {p2}, Landroid/os/Parcel;->readInt()I

    move-result p2

    goto :goto_2b

    nop

    :goto_d
    invoke-virtual {p2}, Landroid/os/Parcel;->readStrongBinder()Landroid/os/IBinder;

    move-result-object p1

    goto :goto_14

    nop

    :goto_e
    invoke-virtual {p2}, Landroid/os/Parcel;->readString()Ljava/lang/String;

    move-result-object p1

    goto :goto_c

    nop

    :goto_f
    invoke-interface {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;->registerServiceNotify(Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify;Ljava/lang/String;)I

    move-result p0

    goto :goto_33

    nop

    :goto_10
    invoke-static {p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify$Stub;->asInterface(Landroid/os/IBinder;)Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify;

    move-result-object p1

    goto :goto_13

    nop

    :goto_11
    invoke-virtual {p2}, Landroid/os/Parcel;->readInt()I

    move-result p1

    goto :goto_26

    nop

    :goto_12
    invoke-super {p0, p1, p2, p3, p4}, Landroid/os/Binder;->onTransact(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z

    move-result p0

    goto :goto_27

    nop

    :goto_13
    invoke-virtual {p2}, Landroid/os/Parcel;->readString()Ljava/lang/String;

    move-result-object p2

    goto :goto_f

    nop

    :goto_14
    invoke-static {p1}, Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify$Stub;->asInterface(Landroid/os/IBinder;)Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify;

    move-result-object p1

    goto :goto_37

    nop

    :goto_15
    if-ne p1, v0, :cond_0

    goto :goto_32

    :cond_0
    goto :goto_7

    nop

    :goto_16
    const v0, 0x5f4e5446

    goto :goto_34

    nop

    :goto_17
    invoke-virtual {p3, p0}, Landroid/os/Parcel;->writeBundle(Landroid/os/Bundle;)V

    goto :goto_1

    nop

    :goto_18
    return v1

    :goto_19
    goto :goto_0

    nop

    :goto_1a
    return v1

    :goto_1b
    invoke-interface {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;->unregisterServiceNotify(Lmiuix/appcompat/app/floatingactivity/multiapp/IServiceNotify;Ljava/lang/String;)V

    goto :goto_6

    nop

    :goto_1c
    invoke-virtual {p2, v2}, Landroid/os/Parcel;->enforceInterface(Ljava/lang/String;)V

    goto :goto_e

    nop

    :goto_1d
    const/4 v0, 0x2

    goto :goto_2e

    nop

    :goto_1e
    const/4 v0, 0x4

    goto :goto_25

    nop

    :goto_1f
    return v1

    :goto_20
    goto :goto_1c

    nop

    :goto_21
    if-eqz p3, :cond_1

    goto :goto_28

    :cond_1
    goto :goto_5

    nop

    :goto_22
    return v1

    :goto_23
    goto :goto_2d

    nop

    :goto_24
    if-ne p1, v0, :cond_2

    goto :goto_23

    :cond_2
    goto :goto_1e

    nop

    :goto_25
    if-ne p1, v0, :cond_3

    goto :goto_19

    :cond_3
    goto :goto_2c

    nop

    :goto_26
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p4

    goto :goto_2a

    nop

    :goto_27
    return p0

    :goto_28
    goto :goto_1d

    nop

    :goto_29
    invoke-virtual {p2}, Landroid/os/Parcel;->readStrongBinder()Landroid/os/IBinder;

    move-result-object p1

    goto :goto_10

    nop

    :goto_2a
    invoke-virtual {p4}, Ljava/lang/Class;->getClassLoader()Ljava/lang/ClassLoader;

    move-result-object p4

    goto :goto_35

    nop

    :goto_2b
    invoke-interface {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;->upDateRemoteActivityInfo(Ljava/lang/String;I)V

    goto :goto_9

    nop

    :goto_2c
    const/4 v0, 0x5

    goto :goto_30

    nop

    :goto_2d
    invoke-virtual {p2, v2}, Landroid/os/Parcel;->enforceInterface(Ljava/lang/String;)V

    goto :goto_29

    nop

    :goto_2e
    const/4 v1, 0x1

    goto :goto_2

    nop

    :goto_2f
    invoke-interface {p0, p1, p2}, Lmiuix/appcompat/app/floatingactivity/multiapp/IFloatingService;->callServiceMethod(ILandroid/os/Bundle;)Landroid/os/Bundle;

    move-result-object p0

    goto :goto_17

    nop

    :goto_30
    if-ne p1, v0, :cond_4

    goto :goto_20

    :cond_4
    goto :goto_16

    nop

    :goto_31
    return v1

    :goto_32
    goto :goto_a

    nop

    :goto_33
    invoke-virtual {p3, p0}, Landroid/os/Parcel;->writeInt(I)V

    goto :goto_b

    nop

    :goto_34
    if-ne p1, v0, :cond_5

    goto :goto_4

    :cond_5
    goto :goto_36

    nop

    :goto_35
    invoke-virtual {p2, p4}, Landroid/os/Parcel;->readBundle(Ljava/lang/ClassLoader;)Landroid/os/Bundle;

    move-result-object p2

    goto :goto_2f

    nop

    :goto_36
    invoke-super {p0, p1, p2, p3, p4}, Landroid/os/Binder;->onTransact(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z

    move-result p0

    goto :goto_3

    nop

    :goto_37
    invoke-virtual {p2}, Landroid/os/Parcel;->readString()Ljava/lang/String;

    move-result-object p2

    goto :goto_1b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
