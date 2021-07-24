from rest_framework.serializers import Serializer
from .models import Track
from rest_framework import viewsets, routers
from .serializers import TrackSerializer

class TrackViewSets(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

router = routers.DefaultRouter()
router.register('tracks', TrackViewSets)