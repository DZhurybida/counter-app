# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ory/keto/acl/v1alpha1/write_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from counter_app.ory.keto.acl.v1alpha1 import (
    acl_pb2 as ory_dot_keto_dot_acl_dot_v1alpha1_dot_acl__pb2,
)


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n)ory/keto/acl/v1alpha1/write_service.proto\x12\x15ory.keto.acl.v1alpha1\x1a\x1fory/keto/acl/v1alpha1/acl.proto"i\n\x1dTransactRelationTuplesRequest\x12H\n\x15relation_tuple_deltas\x18\x01 \x03(\x0b\x32).ory.keto.acl.v1alpha1.RelationTupleDelta"\xce\x01\n\x12RelationTupleDelta\x12@\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x30.ory.keto.acl.v1alpha1.RelationTupleDelta.Action\x12<\n\x0erelation_tuple\x18\x02 \x01(\x0b\x32$.ory.keto.acl.v1alpha1.RelationTuple"8\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\n\n\x06INSERT\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02"4\n\x1eTransactRelationTuplesResponse\x12\x12\n\nsnaptokens\x18\x01 \x03(\t"\xd5\x01\n\x1b\x44\x65leteRelationTuplesRequest\x12G\n\x05query\x18\x01 \x01(\x0b\x32\x38.ory.keto.acl.v1alpha1.DeleteRelationTuplesRequest.Query\x1am\n\x05Query\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\x12\x10\n\x08relation\x18\x03 \x01(\t\x12/\n\x07subject\x18\x04 \x01(\x0b\x32\x1e.ory.keto.acl.v1alpha1.Subject"\x1e\n\x1c\x44\x65leteRelationTuplesResponse2\x97\x02\n\x0cWriteService\x12\x85\x01\n\x16TransactRelationTuples\x12\x34.ory.keto.acl.v1alpha1.TransactRelationTuplesRequest\x1a\x35.ory.keto.acl.v1alpha1.TransactRelationTuplesResponse\x12\x7f\n\x14\x44\x65leteRelationTuples\x12\x32.ory.keto.acl.v1alpha1.DeleteRelationTuplesRequest\x1a\x33.ory.keto.acl.v1alpha1.DeleteRelationTuplesResponseB\x94\x01\n\x18sh.ory.keto.acl.v1alpha1B\x11WatchServiceProtoP\x01Z3github.com/ory/keto/proto/ory/keto/acl/v1alpha1;acl\xaa\x02\x15Ory.Keto.Acl.V1Alpha1\xca\x02\x15Ory\\Keto\\Acl\\V1alpha1b\x06proto3'
)


_TRANSACTRELATIONTUPLESREQUEST = DESCRIPTOR.message_types_by_name[
    "TransactRelationTuplesRequest"
]
_RELATIONTUPLEDELTA = DESCRIPTOR.message_types_by_name["RelationTupleDelta"]
_TRANSACTRELATIONTUPLESRESPONSE = DESCRIPTOR.message_types_by_name[
    "TransactRelationTuplesResponse"
]
_DELETERELATIONTUPLESREQUEST = DESCRIPTOR.message_types_by_name[
    "DeleteRelationTuplesRequest"
]
_DELETERELATIONTUPLESREQUEST_QUERY = _DELETERELATIONTUPLESREQUEST.nested_types_by_name[
    "Query"
]
_DELETERELATIONTUPLESRESPONSE = DESCRIPTOR.message_types_by_name[
    "DeleteRelationTuplesResponse"
]
_RELATIONTUPLEDELTA_ACTION = _RELATIONTUPLEDELTA.enum_types_by_name["Action"]
TransactRelationTuplesRequest = _reflection.GeneratedProtocolMessageType(
    "TransactRelationTuplesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRANSACTRELATIONTUPLESREQUEST,
        "__module__": "ory.keto.acl.v1alpha1.write_service_pb2"
        # @@protoc_insertion_point(class_scope:ory.keto.acl.v1alpha1.TransactRelationTuplesRequest)
    },
)
_sym_db.RegisterMessage(TransactRelationTuplesRequest)

RelationTupleDelta = _reflection.GeneratedProtocolMessageType(
    "RelationTupleDelta",
    (_message.Message,),
    {
        "DESCRIPTOR": _RELATIONTUPLEDELTA,
        "__module__": "ory.keto.acl.v1alpha1.write_service_pb2"
        # @@protoc_insertion_point(class_scope:ory.keto.acl.v1alpha1.RelationTupleDelta)
    },
)
_sym_db.RegisterMessage(RelationTupleDelta)

TransactRelationTuplesResponse = _reflection.GeneratedProtocolMessageType(
    "TransactRelationTuplesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRANSACTRELATIONTUPLESRESPONSE,
        "__module__": "ory.keto.acl.v1alpha1.write_service_pb2"
        # @@protoc_insertion_point(class_scope:ory.keto.acl.v1alpha1.TransactRelationTuplesResponse)
    },
)
_sym_db.RegisterMessage(TransactRelationTuplesResponse)

DeleteRelationTuplesRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteRelationTuplesRequest",
    (_message.Message,),
    {
        "Query": _reflection.GeneratedProtocolMessageType(
            "Query",
            (_message.Message,),
            {
                "DESCRIPTOR": _DELETERELATIONTUPLESREQUEST_QUERY,
                "__module__": "ory.keto.acl.v1alpha1.write_service_pb2"
                # @@protoc_insertion_point(class_scope:ory.keto.acl.v1alpha1.DeleteRelationTuplesRequest.Query)
            },
        ),
        "DESCRIPTOR": _DELETERELATIONTUPLESREQUEST,
        "__module__": "ory.keto.acl.v1alpha1.write_service_pb2"
        # @@protoc_insertion_point(class_scope:ory.keto.acl.v1alpha1.DeleteRelationTuplesRequest)
    },
)
_sym_db.RegisterMessage(DeleteRelationTuplesRequest)
_sym_db.RegisterMessage(DeleteRelationTuplesRequest.Query)

DeleteRelationTuplesResponse = _reflection.GeneratedProtocolMessageType(
    "DeleteRelationTuplesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETERELATIONTUPLESRESPONSE,
        "__module__": "ory.keto.acl.v1alpha1.write_service_pb2"
        # @@protoc_insertion_point(class_scope:ory.keto.acl.v1alpha1.DeleteRelationTuplesResponse)
    },
)
_sym_db.RegisterMessage(DeleteRelationTuplesResponse)

_WRITESERVICE = DESCRIPTOR.services_by_name["WriteService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\030sh.ory.keto.acl.v1alpha1B\021WatchServiceProtoP\001Z3github.com/ory/keto/proto/ory/keto/acl/v1alpha1;acl\252\002\025Ory.Keto.Acl.V1Alpha1\312\002\025Ory\\Keto\\Acl\\V1alpha1"
    _TRANSACTRELATIONTUPLESREQUEST._serialized_start = 101
    _TRANSACTRELATIONTUPLESREQUEST._serialized_end = 206
    _RELATIONTUPLEDELTA._serialized_start = 209
    _RELATIONTUPLEDELTA._serialized_end = 415
    _RELATIONTUPLEDELTA_ACTION._serialized_start = 359
    _RELATIONTUPLEDELTA_ACTION._serialized_end = 415
    _TRANSACTRELATIONTUPLESRESPONSE._serialized_start = 417
    _TRANSACTRELATIONTUPLESRESPONSE._serialized_end = 469
    _DELETERELATIONTUPLESREQUEST._serialized_start = 472
    _DELETERELATIONTUPLESREQUEST._serialized_end = 685
    _DELETERELATIONTUPLESREQUEST_QUERY._serialized_start = 576
    _DELETERELATIONTUPLESREQUEST_QUERY._serialized_end = 685
    _DELETERELATIONTUPLESRESPONSE._serialized_start = 687
    _DELETERELATIONTUPLESRESPONSE._serialized_end = 717
    _WRITESERVICE._serialized_start = 720
    _WRITESERVICE._serialized_end = 999
# @@protoc_insertion_point(module_scope)
