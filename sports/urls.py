
from rest_framework import routers
from athletes.views import AthleteViewSet

router = routers.DefaultRouter()
router.register('sports', SportViewSet)
