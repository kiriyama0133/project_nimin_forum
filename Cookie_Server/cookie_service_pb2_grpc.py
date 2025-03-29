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
                '/Cookies.CookieService/AddCookie',
                request_serializer=cookie__service__pb2.CookieRequest_Add.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse.FromString,
                _registered_method=True)
        self.DeleteCookie = channel.unary_unary(
                '/Cookies.CookieService/DeleteCookie',
                request_serializer=cookie__service__pb2.CookieRequest_Delete.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse.FromString,
                _registered_method=True)
        self.QueryCookie = channel.unary_unary(
                '/Cookies.CookieService/QueryCookie',
                request_serializer=cookie__service__pb2.CookieRequest_Query.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse.FromString,
                _registered_method=True)
        self.TestCookie = channel.unary_unary(
                '/Cookies.CookieService/TestCookie',
                request_serializer=cookie__service__pb2.CookieRequest_Test.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse.FromString,
                _registered_method=True)
        self.GetCookieByID = channel.unary_unary(
                '/Cookies.CookieService/GetCookieByID',
                request_serializer=cookie__service__pb2.CookieRequest_ByID.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse_ByID.FromString,
                _registered_method=True)
        self.GetCookieByName = channel.unary_unary(
                '/Cookies.CookieService/GetCookieByName',
                request_serializer=cookie__service__pb2.CookieRequest_ByName.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse_ByName.FromString,
                _registered_method=True)
        self.GetCookiesByEmail = channel.unary_unary(
                '/Cookies.CookieService/GetCookiesByEmail',
                request_serializer=cookie__service__pb2.CookieRequest_ByEmail.SerializeToString,
                response_deserializer=cookie__service__pb2.CookieResponse_ByEmail.FromString,
                _registered_method=True)
        self.Login = channel.unary_unary(
                '/Cookies.CookieService/Login',
                request_serializer=cookie__service__pb2.LoginInfomation.SerializeToString,
                response_deserializer=cookie__service__pb2.LoginResponse.FromString,
                _registered_method=True)
        self.Rigister = channel.unary_unary(
                '/Cookies.CookieService/Rigister',
                request_serializer=cookie__service__pb2.RigisterInfomation.SerializeToString,
                response_deserializer=cookie__service__pb2.RigisterResponse.FromString,
                _registered_method=True)
        self.SendMail_C = channel.unary_unary(
                '/Cookies.CookieService/SendMail_C',
                request_serializer=cookie__service__pb2.SendMailRequest.SerializeToString,
                response_deserializer=cookie__service__pb2.SendMailResponse.FromString,
                _registered_method=True)
        self.redisAdd = channel.unary_unary(
                '/Cookies.CookieService/redisAdd',
                request_serializer=cookie__service__pb2.RedisAdd.SerializeToString,
                response_deserializer=cookie__service__pb2.RedisAddResponse.FromString,
                _registered_method=True)
        self.redisGet = channel.unary_unary(
                '/Cookies.CookieService/redisGet',
                request_serializer=cookie__service__pb2.RedisGet.SerializeToString,
                response_deserializer=cookie__service__pb2.RedisGetResponse.FromString,
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

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Rigister(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMail_C(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def redisAdd(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def redisGet(self, request, context):
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
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=cookie__service__pb2.LoginInfomation.FromString,
                    response_serializer=cookie__service__pb2.LoginResponse.SerializeToString,
            ),
            'Rigister': grpc.unary_unary_rpc_method_handler(
                    servicer.Rigister,
                    request_deserializer=cookie__service__pb2.RigisterInfomation.FromString,
                    response_serializer=cookie__service__pb2.RigisterResponse.SerializeToString,
            ),
            'SendMail_C': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMail_C,
                    request_deserializer=cookie__service__pb2.SendMailRequest.FromString,
                    response_serializer=cookie__service__pb2.SendMailResponse.SerializeToString,
            ),
            'redisAdd': grpc.unary_unary_rpc_method_handler(
                    servicer.redisAdd,
                    request_deserializer=cookie__service__pb2.RedisAdd.FromString,
                    response_serializer=cookie__service__pb2.RedisAddResponse.SerializeToString,
            ),
            'redisGet': grpc.unary_unary_rpc_method_handler(
                    servicer.redisGet,
                    request_deserializer=cookie__service__pb2.RedisGet.FromString,
                    response_serializer=cookie__service__pb2.RedisGetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Cookies.CookieService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('Cookies.CookieService', rpc_method_handlers)


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
            '/Cookies.CookieService/AddCookie',
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
            '/Cookies.CookieService/DeleteCookie',
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
            '/Cookies.CookieService/QueryCookie',
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
            '/Cookies.CookieService/TestCookie',
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
            '/Cookies.CookieService/GetCookieByID',
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
            '/Cookies.CookieService/GetCookieByName',
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
            '/Cookies.CookieService/GetCookiesByEmail',
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

    @staticmethod
    def Login(request,
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
            '/Cookies.CookieService/Login',
            cookie__service__pb2.LoginInfomation.SerializeToString,
            cookie__service__pb2.LoginResponse.FromString,
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
    def Rigister(request,
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
            '/Cookies.CookieService/Rigister',
            cookie__service__pb2.RigisterInfomation.SerializeToString,
            cookie__service__pb2.RigisterResponse.FromString,
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
    def SendMail_C(request,
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
            '/Cookies.CookieService/SendMail_C',
            cookie__service__pb2.SendMailRequest.SerializeToString,
            cookie__service__pb2.SendMailResponse.FromString,
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
    def redisAdd(request,
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
            '/Cookies.CookieService/redisAdd',
            cookie__service__pb2.RedisAdd.SerializeToString,
            cookie__service__pb2.RedisAddResponse.FromString,
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
    def redisGet(request,
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
            '/Cookies.CookieService/redisGet',
            cookie__service__pb2.RedisGet.SerializeToString,
            cookie__service__pb2.RedisGetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
