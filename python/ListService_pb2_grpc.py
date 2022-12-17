# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ListService_pb2 as ListService__pb2


class ListServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetList = channel.unary_unary(
                '/list_service.ListService/GetList',
                request_serializer=ListService__pb2.EmptyMessage.SerializeToString,
                response_deserializer=ListService__pb2.List.FromString,
                )
        self.Append = channel.unary_unary(
                '/list_service.ListService/Append',
                request_serializer=ListService__pb2.ListItem.SerializeToString,
                response_deserializer=ListService__pb2.List.FromString,
                )
        self.Insert = channel.unary_unary(
                '/list_service.ListService/Insert',
                request_serializer=ListService__pb2.ListItemInsert.SerializeToString,
                response_deserializer=ListService__pb2.List.FromString,
                )
        self.Delete = channel.unary_unary(
                '/list_service.ListService/Delete',
                request_serializer=ListService__pb2.ListItem.SerializeToString,
                response_deserializer=ListService__pb2.List.FromString,
                )
        self.Find = channel.unary_unary(
                '/list_service.ListService/Find',
                request_serializer=ListService__pb2.ListItem.SerializeToString,
                response_deserializer=ListService__pb2.ListItemPosition.FromString,
                )
        self.Sort = channel.unary_unary(
                '/list_service.ListService/Sort',
                request_serializer=ListService__pb2.ListSort.SerializeToString,
                response_deserializer=ListService__pb2.List.FromString,
                )


class ListServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetList(self, request, context):
        """Get list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Append(self, request, context):
        """Append value to list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Insert(self, request, context):
        """Insert value to list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete value from list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Find(self, request, context):
        """Find value in list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sort(self, request, context):
        """Sort list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ListServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetList,
                    request_deserializer=ListService__pb2.EmptyMessage.FromString,
                    response_serializer=ListService__pb2.List.SerializeToString,
            ),
            'Append': grpc.unary_unary_rpc_method_handler(
                    servicer.Append,
                    request_deserializer=ListService__pb2.ListItem.FromString,
                    response_serializer=ListService__pb2.List.SerializeToString,
            ),
            'Insert': grpc.unary_unary_rpc_method_handler(
                    servicer.Insert,
                    request_deserializer=ListService__pb2.ListItemInsert.FromString,
                    response_serializer=ListService__pb2.List.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=ListService__pb2.ListItem.FromString,
                    response_serializer=ListService__pb2.List.SerializeToString,
            ),
            'Find': grpc.unary_unary_rpc_method_handler(
                    servicer.Find,
                    request_deserializer=ListService__pb2.ListItem.FromString,
                    response_serializer=ListService__pb2.ListItemPosition.SerializeToString,
            ),
            'Sort': grpc.unary_unary_rpc_method_handler(
                    servicer.Sort,
                    request_deserializer=ListService__pb2.ListSort.FromString,
                    response_serializer=ListService__pb2.List.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'list_service.ListService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ListService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/GetList',
            ListService__pb2.EmptyMessage.SerializeToString,
            ListService__pb2.List.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Append(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Append',
            ListService__pb2.ListItem.SerializeToString,
            ListService__pb2.List.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Insert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Insert',
            ListService__pb2.ListItemInsert.SerializeToString,
            ListService__pb2.List.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Delete',
            ListService__pb2.ListItem.SerializeToString,
            ListService__pb2.List.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Find(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Find',
            ListService__pb2.ListItem.SerializeToString,
            ListService__pb2.ListItemPosition.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sort(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Sort',
            ListService__pb2.ListSort.SerializeToString,
            ListService__pb2.List.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
