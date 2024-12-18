# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import cookie_service_pb2 as cookie__service__pb2

GRPC_GENERATED_VERSION = '1.68.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in cookie_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CookieServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddCookie = channel.unary_unary(
                '/cookie.CookieService/AddCookie',
                request_serializer=cookie__service__pb2.CookieRequest_Add.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse.FromString,
                _registered_method=True)
        self.DeleteCookie = channel.unary_unary(
                '/cookie.CookieService/DeleteCookie',
                request_serializer=cookie__service__pb2.CookieRequest_Delete.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse.FromString,
                _registered_method=True)
        self.QueryCookie = channel.unary_unary(
                '/cookie.CookieService/QueryCookie',
                request_serializer=cookie__service__pb2.CookieRequest_Query.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse.FromString,
                _registered_method=True)
        self.TestCookie = channel.unary_unary(
                '/cookie.CookieService/TestCookie',
                request_serializer=cookie__service__pb2.CookieRequest_Test.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse.FromString,
                _registered_method=True)
        self.GetCookieByID = channel.unary_unary(
                '/cookie.CookieService/GetCookieByID',
                request_serializer=cookie__service__pb2.CookieRequest_ByID.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse_ByID.FromString,
                _registered_method=True)
        self.GetCookieByName = channel.unary_unary(
                '/cookie.CookieService/GetCookieByName',
                request_serializer=cookie__service__pb2.CookieRequest_ByName.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse_ByName.FromString,
                _registered_method=True)
        self.GetCookiesByEmail = channel.unary_unary(
                '/cookie.CookieService/GetCookiesByEmail',
                request_serializer=cookie__service__pb2.CookieRequest_ByEmail.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse_ByEmail.FromString,
                _registered_method=True)


class CookieServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddCookie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCookie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryCookie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestCookie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCookieByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCookieByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCookiesByEmail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CookieServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddCookie': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCookie,
                    request_deserializer=cookie__service__pb2.CookieRequest_Add.FromString,
                    response_serializer=cookie__service__pb2.CookieResponse.SerializeToString,
            ),
            'DeleteCookie': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCookie,
                    request_deserializer=cookie__service__pb2.CookieRequest_Delete.FromString,
                    response_serializer=cookie__service__pb2.CookieResponse.SerializeToString,
            ),
            'QueryCookie': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryCookie,
                    request_deserializer=cookie__service__pb2.CookieRequest_Query.FromString,
                    response_serializer=cookie__service__pb2.CookieResponse.SerializeToString,
            ),
            'TestCookie': grpc.unary_unary_rpc_method_handler(
                    servicer.TestCookie,
                    request_deserializer=cookie__service__pb2.CookieRequest_Test.FromString,
                    response_serializer=cookie__service__pb2.CookieResponse.SerializeToString,
            ),
            'GetCookieByID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCookieByID,
                    request_deserializer=cookie__service__pb2.CookieRequest_ByID.FromString,
                    response_serializer=cookie__service__pb2.CookieResponse_ByID.SerializeToString,
            ),
            'GetCookieByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCookieByName,
                    request_deserializer=cookie__service__pb2.CookieRequest_ByName.FromString,
                    response_serializer=cookie__service__pb2.CookieResponse_ByName.SerializeToString,
            ),
            'GetCookiesByEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCookiesByEmail,
                    request_deserializer=cookie__service__pb2.CookieRequest_ByEmail.FromString,
                    response_serializer=cookie__service__pb2.CookieResponse_ByEmail.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cookie.CookieService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cookie.CookieService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CookieService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddCookie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cookie.CookieService/AddCookie',
            cookie__service__pb2.CookieRequest_Add.SerializeToString,
            cookie__service__pb2.CookieResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteCookie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cookie.CookieService/DeleteCookie',
            cookie__service__pb2.CookieRequest_Delete.SerializeToString,
            cookie__service__pb2.CookieResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def QueryCookie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cookie.CookieService/QueryCookie',
            cookie__service__pb2.CookieRequest_Query.SerializeToString,
            cookie__service__pb2.CookieResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def TestCookie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cookie.CookieService/TestCookie',
            cookie__service__pb2.CookieRequest_Test.SerializeToString,
            cookie__service__pb2.CookieResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetCookieByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cookie.CookieService/GetCookieByID',
            cookie__service__pb2.CookieRequest_ByID.SerializeToString,
            cookie__service__pb2.CookieResponse_ByID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetCookieByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cookie.CookieService/GetCookieByName',
            cookie__service__pb2.CookieRequest_ByName.SerializeToString,
            cookie__service__pb2.CookieResponse_ByName.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetCookiesByEmail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cookie.CookieService/GetCookiesByEmail',
            cookie__service__pb2.CookieRequest_ByEmail.SerializeToString,
            cookie__service__pb2.CookieResponse_ByEmail.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
