import logging

from back_api.customauth.setcookie import SetCookie
from back_api.models import AgentType
from back_api.serializers import AgentTypeSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from user_model.models import CustomUserClass
logger = logging.getLogger("django")


class CustomAuthToken(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)

            access_token = response.data["access"]
            refresh_token = response.data["refresh"]

            cookieinst = SetCookie()
            cookieinst.set_auth_cookie(access_token)
            cookieinst.set_refresh_cookie(refresh_token)
            return cookieinst.response
        except Exception as e:
            logger.debug(str(e))
            return Response({"success": False})


class CustomRefreshToken(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            access_token = response.data["access"]

            refreshinst = SetCookie()
            refreshinst.set_auth_cookie(access_token)

            return refreshinst.response

        except Exception as e:
            logger.debug(str(e))
            return Response({"refresh": False})


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
