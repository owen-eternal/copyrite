from .viewsets import TrackViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tracks', TrackViewSets)