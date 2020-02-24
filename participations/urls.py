from rest_framework import routers

from participations.views import CommentaryViewSet

router = routers.DefaultRouter()
router.register('commentaries', CommentaryViewSet)
