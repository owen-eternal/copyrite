from rest_framework import serializers
from .models import Track

class TrackSerializer(serializers.ModelSerializer):
    album = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Track
        fields = '__all__'
