# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/heartbeat.proto

import sys

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="protos/heartbeat.proto",
    package="",
    syntax="proto2",
    serialized_options=_b("Z#clusterfuzz/protos/untrusted_runner"),
    serialized_pb=_b(
        '\n\x16protos/heartbeat.proto"\x12\n\x10HeartbeatRequest"\x13\n\x11HeartbeatResponse2:\n\tHeartbeat\x12-\n\x04\x42\x65\x61t\x12\x11.HeartbeatRequest\x1a\x12.HeartbeatResponseB%Z#clusterfuzz/protos/untrusted_runner'
    ),
)


_HEARTBEATREQUEST = _descriptor.Descriptor(
    name="HeartbeatRequest",
    full_name="HeartbeatRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=26,
    serialized_end=44,
)


_HEARTBEATRESPONSE = _descriptor.Descriptor(
    name="HeartbeatResponse",
    full_name="HeartbeatResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=46,
    serialized_end=65,
)

DESCRIPTOR.message_types_by_name["HeartbeatRequest"] = _HEARTBEATREQUEST
DESCRIPTOR.message_types_by_name["HeartbeatResponse"] = _HEARTBEATRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HeartbeatRequest = _reflection.GeneratedProtocolMessageType(
    "HeartbeatRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_HEARTBEATREQUEST,
        __module__="protos.heartbeat_pb2"
        # @@protoc_insertion_point(class_scope:HeartbeatRequest)
    ),
)
_sym_db.RegisterMessage(HeartbeatRequest)

HeartbeatResponse = _reflection.GeneratedProtocolMessageType(
    "HeartbeatResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_HEARTBEATRESPONSE,
        __module__="protos.heartbeat_pb2"
        # @@protoc_insertion_point(class_scope:HeartbeatResponse)
    ),
)
_sym_db.RegisterMessage(HeartbeatResponse)


DESCRIPTOR._options = None

_HEARTBEAT = _descriptor.ServiceDescriptor(
    name="Heartbeat",
    full_name="Heartbeat",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=67,
    serialized_end=125,
    methods=[
        _descriptor.MethodDescriptor(
            name="Beat",
            full_name="Heartbeat.Beat",
            index=0,
            containing_service=None,
            input_type=_HEARTBEATREQUEST,
            output_type=_HEARTBEATRESPONSE,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_HEARTBEAT)

DESCRIPTOR.services_by_name["Heartbeat"] = _HEARTBEAT

# @@protoc_insertion_point(module_scope)
