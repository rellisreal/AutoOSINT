import logging

from back_api.customauth.setcookie import SetCookie
from back_api.models import AgentType, OSINTQuery
from back_api.serializers import AgentTypeSerializer, OSINTQuerySerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
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


@api_view(["POST"])
@permission_classes({IsAuthenticated})
def is_authenticated(request):
    return Response({"authenticated": True})


class AgentTypeViewSet(viewsets.ModelViewSet):
    serializer_class = AgentTypeSerializer
    queryset = AgentType.objects.all()
    permission_classes = [IsAuthenticated]


class CustomOSINTQuery(viewsets.ModelViewSet):
    serializer_class = OSINTQuerySerializer
    queryset = OSINTQuery.objects.all()
    permission_classes = [IsAuthenticated]
