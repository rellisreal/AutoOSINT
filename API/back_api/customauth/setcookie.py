from rest_framework.response import Response


class SetCookie:
    def __init__(self):
        self.response = Response()  # Response()
        self.response.data = {"success": True}
        self.httponly = True
        self.secure = True
        self.samesite = "lax"
        self.path = "/"

    def set_auth_cookie(self, keyvalue):
        self.response.set_cookie(
            key="access_token",
            value=keyvalue,
            httponly=self.httponly,
            secure=self.secure,
            samesite=self.samesite,
            path=self.path,
        )

    def set_refresh_cookie(self, keyvalue):
        self.response.set_cookie(
            key="refresh_token",
            value=keyvalue,
            httponly=self.httponly,
            secure=self.secure,
            samesite=self.samesite,
            path=self.path,
        )
