from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from athletes.urls import router as athletes_router

router = routers.DefaultRouter()
router.registry.extend(athletes_router.registry)

urlpatterns = [
    path('', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/registration/', include('rest_auth.registration.urls')),
    path('api/v1/', include('rest_auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
