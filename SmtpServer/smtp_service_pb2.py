# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: smtp_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'smtp_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12smtp_service.proto\x12\x04smtp\" \n\x0fSendMailRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"3\n\x10SendMailResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2C\n\x04SMTP\x12;\n\x08SendMail\x12\x15.smtp.SendMailRequest\x1a\x16.smtp.SendMailResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'smtp_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SENDMAILREQUEST']._serialized_start=28
  _globals['_SENDMAILREQUEST']._serialized_end=60
  _globals['_SENDMAILRESPONSE']._serialized_start=62
  _globals['_SENDMAILRESPONSE']._serialized_end=113
  _globals['_SMTP']._serialized_start=115
  _globals['_SMTP']._serialized_end=182
# @@protoc_insertion_point(module_scope)
