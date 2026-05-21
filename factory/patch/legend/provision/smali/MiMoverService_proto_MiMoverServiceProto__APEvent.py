TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'MiMoverService/proto/MiMoverServiceProto$APEvent.smali'
CLASS_FALLBACK_NAMES = ['MiMoverServiceProto$APEvent.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageV3;', '.implements Lcom/google/protobuf/MessageOrBuilder;', '.field private static final DEFAULT_INSTANCE:LMiMoverService/proto/MiMoverServiceProto$APEvent;', '.field public static final NAMETOKEN_FIELD_NUMBER:I = 0x1', '.field private static final PARSER:Lcom/google/protobuf/Parser;', '.field public static final PWDTOKEN_FIELD_NUMBER:I = 0x2']

PATCHES = [
    {
        'id': 'MiMoverService_proto_MiMoverServiceProto__APEvent__newBuilderForType',
        'method': '.method protected bridge synthetic newBuilderForType(Lcom/google/protobuf/GeneratedMessageV3$BuilderParent;)Lcom/google/protobuf/Message$Builder;',
        'method_name': 'newBuilderForType',
        'method_anchors': ['invoke-virtual {p0, p1}, LMiMoverService/proto/MiMoverServiceProto$APEvent;->newBuilderForType(Lcom/google/protobuf/GeneratedMessageV3$BuilderParent;)LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic newBuilderForType(Lcom/google/protobuf/GeneratedMessageV3$BuilderParent;)Lcom/google/protobuf/Message$Builder;
    .registers 2

    invoke-virtual {p0, p1}, LMiMoverService/proto/MiMoverServiceProto$APEvent;->newBuilderForType(Lcom/google/protobuf/GeneratedMessageV3$BuilderParent;)LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic newBuilderForType(Lcom/google/protobuf/GeneratedMessageV3$BuilderParent;)Lcom/google/protobuf/Message$Builder;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0, p1}, LMiMoverService/proto/MiMoverServiceProto$APEvent;->newBuilderForType(Lcom/google/protobuf/GeneratedMessageV3$BuilderParent;)LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'MiMoverService_proto_MiMoverServiceProto__APEvent__internalGetFieldAccessorTable',
        'method': '.method protected internalGetFieldAccessorTable()Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;',
        'method_name': 'internalGetFieldAccessorTable',
        'method_anchors': ['invoke-static {}, LMiMoverService/proto/MiMoverServiceProto;->-$$Nest$sfgetinternal_static_MiMoverService_proto_APEvent_fieldAccessorTable()Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;', 'invoke-virtual {p0, v0, v1}, Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;->ensureFieldAccessorsInitialized(Ljava/lang/Class;Ljava/lang/Class;)Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected internalGetFieldAccessorTable()Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;
    .registers 3

    invoke-static {}, LMiMoverService/proto/MiMoverServiceProto;->-$$Nest$sfgetinternal_static_MiMoverService_proto_APEvent_fieldAccessorTable()Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;

    move-result-object p0

    const-class v0, LMiMoverService/proto/MiMoverServiceProto$APEvent;

    const-class v1, LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;

    invoke-virtual {p0, v0, v1}, Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;->ensureFieldAccessorsInitialized(Ljava/lang/Class;Ljava/lang/Class;)Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected internalGetFieldAccessorTable()Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;
    .registers 3

    goto :goto_3

    nop

    :goto_0
    return-object p0

    :goto_1
    const-class v0, LMiMoverService/proto/MiMoverServiceProto$APEvent;

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {p0, v0, v1}, Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;->ensureFieldAccessorsInitialized(Ljava/lang/Class;Ljava/lang/Class;)Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;

    move-result-object p0

    goto :goto_0

    nop

    :goto_3
    invoke-static {}, LMiMoverService/proto/MiMoverServiceProto;->-$$Nest$sfgetinternal_static_MiMoverService_proto_APEvent_fieldAccessorTable()Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;

    move-result-object p0

    goto :goto_1

    nop

    :goto_4
    const-class v1, LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'MiMoverService_proto_MiMoverServiceProto__APEvent__newBuilderForType',
        'method': '.method protected newBuilderForType(Lcom/google/protobuf/GeneratedMessageV3$BuilderParent;)LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;',
        'method_name': 'newBuilderForType',
        'method_anchors': ['new-instance p0, LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;', 'invoke-direct {p0, p1, v0}, LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;-><init>(Lcom/google/protobuf/GeneratedMessageV3$BuilderParent;LMiMoverService/proto/MiMoverServiceProto-IA;)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected newBuilderForType(Lcom/google/protobuf/GeneratedMessageV3$BuilderParent;)LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;
    .registers 3

    new-instance p0, LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;-><init>(Lcom/google/protobuf/GeneratedMessageV3$BuilderParent;LMiMoverService/proto/MiMoverServiceProto-IA;)V

    return-object p0
.end method""",
        'replacement': """.method protected newBuilderForType(Lcom/google/protobuf/GeneratedMessageV3$BuilderParent;)LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;
    .registers 3

    goto :goto_2

    nop

    :goto_0
    return-object p0

    :goto_1
    const/4 v0, 0x0

    goto :goto_3

    nop

    :goto_2
    new-instance p0, LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;

    goto :goto_1

    nop

    :goto_3
    invoke-direct {p0, p1, v0}, LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;-><init>(Lcom/google/protobuf/GeneratedMessageV3$BuilderParent;LMiMoverService/proto/MiMoverServiceProto-IA;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
