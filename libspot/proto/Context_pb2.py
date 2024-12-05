# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: context.proto
"""Generated protocol buffer code."""
import ContextPage_pb2 as context__page__pb2
import Restrictions_pb2 as restrictions__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name="context.proto",
    package="spotify.player.proto",
    syntax="proto2",
    serialized_options=b"\n\023com.spotify.contextH\002",
    create_key=_descriptor._internal_create_key,
    serialized_pb=
    b'\n\rcontext.proto\x12\x14spotify.player.proto\x1a\x12\x63ontext_page.proto\x1a\x12restrictions.proto"\x90\x02\n\x07\x43ontext\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12=\n\x08metadata\x18\x03 \x03(\x0b\x32+.spotify.player.proto.Context.MetadataEntry\x12\x38\n\x0crestrictions\x18\x04 \x01(\x0b\x32".spotify.player.proto.Restrictions\x12\x30\n\x05pages\x18\x05 \x03(\x0b\x32!.spotify.player.proto.ContextPage\x12\x0f\n\x07loading\x18\x06 \x01(\x08\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x17\n\x13\x63om.spotify.contextH\x02',
    dependencies=[
        context__page__pb2.DESCRIPTOR,
        restrictions__pb2.DESCRIPTOR,
    ],
)

_CONTEXT_METADATAENTRY = _descriptor.Descriptor(
    name="MetadataEntry",
    full_name="spotify.player.proto.Context.MetadataEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="spotify.player.proto.Context.MetadataEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="spotify.player.proto.Context.MetadataEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=305,
    serialized_end=352,
)

_CONTEXT = _descriptor.Descriptor(
    name="Context",
    full_name="spotify.player.proto.Context",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="uri",
            full_name="spotify.player.proto.Context.uri",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="url",
            full_name="spotify.player.proto.Context.url",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="spotify.player.proto.Context.metadata",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="restrictions",
            full_name="spotify.player.proto.Context.restrictions",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="pages",
            full_name="spotify.player.proto.Context.pages",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="loading",
            full_name="spotify.player.proto.Context.loading",
            index=5,
            number=6,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _CONTEXT_METADATAENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=80,
    serialized_end=352,
)

_CONTEXT_METADATAENTRY.containing_type = _CONTEXT
_CONTEXT.fields_by_name["metadata"].message_type = _CONTEXT_METADATAENTRY
_CONTEXT.fields_by_name[
    "restrictions"].message_type = restrictions__pb2._RESTRICTIONS
_CONTEXT.fields_by_name["pages"].message_type = context__page__pb2._CONTEXTPAGE
DESCRIPTOR.message_types_by_name["Context"] = _CONTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Context = _reflection.GeneratedProtocolMessageType(
    "Context",
    (_message.Message, ),
    {
        "MetadataEntry":
        _reflection.GeneratedProtocolMessageType(
            "MetadataEntry",
            (_message.Message, ),
            {
                "DESCRIPTOR": _CONTEXT_METADATAENTRY,
                "__module__": "context_pb2"
                # @@protoc_insertion_point(class_scope:spotify.player.proto.Context.MetadataEntry)
            },
        ),
        "DESCRIPTOR":
        _CONTEXT,
        "__module__":
        "context_pb2"
        # @@protoc_insertion_point(class_scope:spotify.player.proto.Context)
    },
)
_sym_db.RegisterMessage(Context)
_sym_db.RegisterMessage(Context.MetadataEntry)

DESCRIPTOR._options = None
_CONTEXT_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
