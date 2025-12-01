from back_api.models import AgentType
from back_api.serializers import AgentTypeSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

# from user_model.models import CustomUserClass


class AgentTypeViewSet(viewsets.ViewSet):
    """
    A ViewSet for listing or retrieving different agents.
    """

    def list(self, request):
        queryset = AgentType.objects.all()
        serializer = AgentTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = AgentType.objects.all()
        agent = get_object_or_404(queryset, pk=pk)
        serializer = AgentTypeSerializer(agent)
        return Response(serializer.data)
