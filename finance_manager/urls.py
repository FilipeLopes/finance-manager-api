"""finance_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from items.api.viewsets import ItemViewSet
from categories.api.viewsets import CategoryViewSet
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserDetailAPI, RegisterUserAPIView, UserLogInAPI, UserLogoutAPI

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'categories', CategoryViewSet)
urlpatterns = [
    path('financemanager/', include(router.urls)),
    path('admin/', admin.site.urls),
    path("financemanager/get-details/", UserDetailAPI.as_view()),
    path('financemanager/register/', RegisterUserAPIView.as_view()),
    path('financemanager/login/', UserLogInAPI.as_view()),
    path('financemanager/logout/', UserLogoutAPI.as_view()),

    path('api-token-auth/', obtain_auth_token),
]
