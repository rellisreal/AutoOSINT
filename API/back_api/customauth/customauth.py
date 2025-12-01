import logging

from rest_framework_simplejwt.authentication import JWTAuthentication

logger = logging.getLogger("django")


class CookieAuthenticaiton(JWTAuthentication):
    def authenticate(self, request):
        try:
            access_token = request.COOKIES.get("access_token")
            validated_token = self.get_validated_token(access_token)
            user = self.get_user(validated_token)
            return (user, validated_token)
        except Exception as e:
            logger.debug(str(e))
            return None
