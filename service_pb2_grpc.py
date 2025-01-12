# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import service_pb2 as service__pb2

GRPC_GENERATED_VERSION = '1.69.0'
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
        + f' but the generated code in service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class StatisticsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get_Prices_Graph = channel.unary_unary(
                '/Statistics/Get_Prices_Graph',
                request_serializer=service__pb2.HelloRequest.SerializeToString,
                response_deserializer=service__pb2.GraphReply.FromString,
                _registered_method=True)
        self.Get_all_products = channel.unary_unary(
                '/Statistics/Get_all_products',
                request_serializer=service__pb2.HelloRequest.SerializeToString,
                response_deserializer=service__pb2.AllProductsReply.FromString,
                _registered_method=True)


class StatisticsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get_Prices_Graph(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get_all_products(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StatisticsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get_Prices_Graph': grpc.unary_unary_rpc_method_handler(
                    servicer.Get_Prices_Graph,
                    request_deserializer=service__pb2.HelloRequest.FromString,
                    response_serializer=service__pb2.GraphReply.SerializeToString,
            ),
            'Get_all_products': grpc.unary_unary_rpc_method_handler(
                    servicer.Get_all_products,
                    request_deserializer=service__pb2.HelloRequest.FromString,
                    response_serializer=service__pb2.AllProductsReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Statistics', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('Statistics', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Statistics(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get_Prices_Graph(request,
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
            '/Statistics/Get_Prices_Graph',
            service__pb2.HelloRequest.SerializeToString,
            service__pb2.GraphReply.FromString,
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
    def Get_all_products(request,
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
            '/Statistics/Get_all_products',
            service__pb2.HelloRequest.SerializeToString,
            service__pb2.AllProductsReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
