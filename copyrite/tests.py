
from rest_framework import status
from copyrite.models import Album, Artist, Track
from django.urls.base import resolve, reverse
from rest_framework.test import APITestCase

class TestTrackApi(APITestCase):

    def setUp(self):
        artist = Artist.objects.create(artist_name='Yungengod', record_label='kolumbus beatz')
        album = Album.objects.create(album_name='omnipresence', release_date='2021-03-03', artist=artist)
        Track.objects.create(title='draftwork', duration=3, genre='hiphop', album=album)

    def tearDown(self):
        pass
        
    url = reverse('track-list')

    def test_tracklist(self):
        respond = self.client.get(self.url)
        self.assertEqual(respond.status_code, status.HTTP_200_OK)
        self.assertEqual(len(respond.data), 1)

