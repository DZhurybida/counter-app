# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from counter_app.ory.keto.acl.v1alpha1 import (
    check_service_pb2 as ory_dot_keto_dot_acl_dot_v1alpha1_dot_check__service__pb2,
)


class CheckServiceStub(object):
    """The service that performs authorization checks
    based on the stored Access Control Lists.

    This service is part of the [read-APIs](../concepts/api-overview.mdx#read-apis).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Check = channel.unary_unary(
            "/ory.keto.acl.v1alpha1.CheckService/Check",
            request_serializer=ory_dot_keto_dot_acl_dot_v1alpha1_dot_check__service__pb2.CheckRequest.SerializeToString,
            response_deserializer=ory_dot_keto_dot_acl_dot_v1alpha1_dot_check__service__pb2.CheckResponse.FromString,
        )


class CheckServiceServicer(object):
    """The service that performs authorization checks
    based on the stored Access Control Lists.

    This service is part of the [read-APIs](../concepts/api-overview.mdx#read-apis).
    """

    def Check(self, request, context):
        """Performs an authorization check."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CheckServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Check": grpc.unary_unary_rpc_method_handler(
            servicer.Check,
            request_deserializer=ory_dot_keto_dot_acl_dot_v1alpha1_dot_check__service__pb2.CheckRequest.FromString,
            response_serializer=ory_dot_keto_dot_acl_dot_v1alpha1_dot_check__service__pb2.CheckResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "ory.keto.acl.v1alpha1.CheckService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class CheckService(object):
    """The service that performs authorization checks
    based on the stored Access Control Lists.

    This service is part of the [read-APIs](../concepts/api-overview.mdx#read-apis).
    """

    @staticmethod
    def Check(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ory.keto.acl.v1alpha1.CheckService/Check",
            ory_dot_keto_dot_acl_dot_v1alpha1_dot_check__service__pb2.CheckRequest.SerializeToString,
            ory_dot_keto_dot_acl_dot_v1alpha1_dot_check__service__pb2.CheckResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
