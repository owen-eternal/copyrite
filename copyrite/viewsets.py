from .models import Track
from rest_framework import viewsets
from .serializers import TrackSerializer

class TrackViewSets(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer