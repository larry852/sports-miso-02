from rest_framework import routers

from .views import SportViewSet, ModalityViewSet

router = routers.DefaultRouter()
router.register('sports', SportViewSet)
router.register('modalities', ModalityViewSet)
