TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'MiMoverService/proto/MiMoverServiceProto$APEvent$Builder.smali'
CLASS_FALLBACK_NAMES = ['MiMoverServiceProto$APEvent$Builder.smali']
CLASS_ANCHORS = ['.super Lcom/google/protobuf/GeneratedMessageV3$Builder;', '.implements Lcom/google/protobuf/MessageOrBuilder;']

PATCHES = [
    {
        'id': 'MiMoverService_proto_MiMoverServiceProto__APEvent__Builder__internalGetFieldAccessorTable',
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

    goto :goto_0

    nop

    :goto_0
    invoke-static {}, LMiMoverService/proto/MiMoverServiceProto;->-$$Nest$sfgetinternal_static_MiMoverService_proto_APEvent_fieldAccessorTable()Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    const-class v0, LMiMoverService/proto/MiMoverServiceProto$APEvent;

    goto :goto_3

    nop

    :goto_2
    invoke-virtual {p0, v0, v1}, Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;->ensureFieldAccessorsInitialized(Ljava/lang/Class;Ljava/lang/Class;)Lcom/google/protobuf/GeneratedMessageV3$FieldAccessorTable;

    move-result-object p0

    goto :goto_4

    nop

    :goto_3
    const-class v1, LMiMoverService/proto/MiMoverServiceProto$APEvent$Builder;

    goto :goto_2

    nop

    :goto_4
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
