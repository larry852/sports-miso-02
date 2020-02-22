
from rest_framework import routers
from athletes.views import AthleteViewSet
from sports.views import SportViewSet

router = routers.DefaultRouter()
router.register('athletes', AthleteViewSet)
router.register('sports', SportViewSet)
