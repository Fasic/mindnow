"""mindnow URL Configuration

"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth.decorators import login_required
from decorator_include import decorator_include

"""Schema creator for swagger: https://drf-yasg.readthedocs.io/"""
schema_view = get_schema_view(
    openapi.Info(
        title="Travelling Companion API",
        default_version='v1',
        description="This is an api preview for the \"Travelling Companion\" app",
        contact=openapi.Contact(email="wasicfilip@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

"""
URL definitions:
    admin/ - urls for admin portal
    api/ - API urls, for rest_api module
    auth/ - AUTH urls, for registration and login, mind_auth module
    default path '' - WEB urls for django template based WEB part of app
    
    SWAGGER URL-s:
        swagger/ - UI based documentation of API end points
        /swagger.json - file with json format of API end points
        /swagger.yaml - file with yaml format of API end points
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', decorator_include(login_required, 'travelling_companion.urls')),
    path('api/', include('rest_api.urls')),
    path('auth/', include('mind_auth.urls')),

    # SWAGGER URL-s
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
