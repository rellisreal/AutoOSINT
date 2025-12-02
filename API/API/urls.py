"""
URL configuration for API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from back_api.views import (
    AgentTypeViewSet,
    CustomAuthToken,
    CustomOSINTQuery,
    CustomRefreshToken,
    is_authenticated,
)
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"agents", AgentTypeViewSet, basename="agent")
router.register(r"OSINTQueries", CustomOSINTQuery, basename="OSINTQuery")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", CustomAuthToken.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", CustomRefreshToken.as_view(), name="token_refresh"),
    path("api/token/verify", is_authenticated, name="token-verify"),
]

urlpatterns += router.urls
