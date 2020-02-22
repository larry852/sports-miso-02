from rest_framework import routers

from sports.views import SportViewSet

router = routers.DefaultRouter()
router.register('sports', SportViewSet)
