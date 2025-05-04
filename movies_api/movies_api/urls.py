from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # 👈 Importación para redirección

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# 👇 Vista que redirige la raíz hacia /swagger/
def redirect_to_swagger(request):
    return redirect('/swagger/')

schema_view = get_schema_view(
    openapi.Info(
        title="Movie API",
        default_version="v1",
        description="API Description"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", redirect_to_swagger),  # 👈 Redirige la raíz hacia Swagger
    path("swagger/", schema_view.with_ui("swagger")),
    path("admin/", admin.site.urls),
    path("movie/", include("movie.urls")),
    path("user/", include("user.urls")),
]
