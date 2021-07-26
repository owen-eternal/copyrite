from copyrite.serializers import TrackSerializer
from rest_framework import status
from copyrite.models import Album, Artist, Track
from django.urls.base import reverse
from rest_framework.test import APITestCase

class TestTrackApi(APITestCase):

    track_url = reverse('track-list')

    def setUp(self):

        artist_1 = Artist.objects.create(artist_name='Yungengod', record_label='kolumbus beatz')
        album_1 = Album.objects.create(album_name='omnipresence', release_date='2021-03-03', artist=artist_1)
        self.track_1 = Track.objects.create(title='draftwork', duration=3, genre='hiphop', album=album_1)

        #####################################################################################################

        artist_2 = Artist.objects.create(artist_name='YungenGod', record_label='Kolumbus Beats')
        album_2= Album.objects.create(album_name='omnipresence', release_date='2021-03-03', artist=artist_2)
        self.track_2 = Track.objects.create(title='Itches On My Hind', duration=4, genre='hiphop', album=album_2)
        
    def tearDown(self):
        pass

    def test_tracklist(self):

        #fetch data 
        get_payload = self.client.get(self.track_url)

        #check for status code.
        self.assertEqual(get_payload.status_code, status.HTTP_200_OK)

        #check if the get_payload is a list
        self.assertIsInstance(get_payload.json(), list)

        #list of querysets
        queryset = [self.track_1, self.track_2]
    
        for id in range(len(queryset)):
            self.assertEqual(TrackSerializer(instance=queryset[id]).data, get_payload.json()[id])
        