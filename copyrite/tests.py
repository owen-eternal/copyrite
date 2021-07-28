import json
from datetime import datetime
from django.test.testcases import TestCase
from copyrite.viewsets import TrackViewSets
from copyrite.serializers import TrackSerializer
from rest_framework import status
from copyrite.models import Album, Artist, Track
from django.urls.base import resolve, reverse
from rest_framework.test import APIClient, APITestCase


class TestTrackApi(APITestCase):

    def setUp(self):

        artist_1 = Artist.objects.create(artist_name='Yungengod',
                            record_label='kolumbus beatz')
        album_1 = Album.objects.create(album_name='omnipresence',
                            release_date='2021-03-03', artist=artist_1)
        self.track_1 = Track.objects.create(title='draftwork', duration=3,
                            genre='hiphop', album=album_1)

        #####################################################################################################

        artist_2 = Artist.objects.create(artist_name='YungenGod',
                            record_label='Kolumbus Beats')
        album_2 = Album.objects.create(album_name='omnipresence',
                            release_date='2021-03-03', artist=artist_2)
        self.track_2 = Track.objects.create(title='Itches On My Hind',
                            duration=4, genre='hiphop', album=album_2)

        #####################################################################################################

        """DATA FOR TEST REQUEST"""

        self.track_payload = [

            # valid payload data 
            { 
                "id": 3,
                "title" : "going high",
                "duration" : 3,
                "genre" : "hip-hop",
                "album" : 2
            },

            # testing payload data
            { 
                "id": 3,
                "title" : "going high",
                "duration" : 3,
                "genre" : "hip-hop",
                "album" : 2
            }
        ]

        ####################################################################################################

        self.all_track = Track.objects.all()

        #####################################################################################################

    # mixin for both get requests.
    def get_requests(self, payload, url):

        self.assertEqual(payload.status_code, status.HTTP_200_OK)

        self.assertEqual(resolve(url).func.__name__, TrackViewSets.__name__)

        return [self.track_1, self.track_2]

    def test_get_track_list(self):

        # Absolute link
        track_url = reverse('track-list')

        # fetch data
        get_payload = self.client.get(track_url)

        # check if its a list
        self.assertIsInstance(get_payload.json(), list)

        # run first tests
        queryset = self.get_requests(get_payload, track_url)

        for id in range(len(queryset)):
            self.assertEqual(TrackSerializer(instance=queryset[id]).data, get_payload.json()[id])

    def test_get_single_track(self):

        # get obsolute link
        track_url = reverse('track-detail', kwargs={'pk': '1'})

        # get individual track payload.
        get_payload = self.client.get(track_url)

        # run first tests
        queryset = self.get_requests(get_payload, track_url)

        # check to see to see if queryset is a model instance
        self.assertIsInstance(queryset[0], Track)

        # check for the model string constructer
        self.assertEqual(str(queryset[0]), 'draftwork')

        # check data integrity
        self.assertEqual(TrackSerializer(instance=queryset[0]).data, 
                        get_payload.json())

    def test_create_track(self):

        # create post request to the backend
        response = self.client.post(reverse('track-list'), 
                    data=self.track_payload[0], 
                    format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        last_entry_index = len(self.all_track)-1

        # serialize the the last entry inside the database
        serialized_database_entry = TrackSerializer(instance=self.all_track[last_entry_index]).data

        # remove the date key
        serialized_database_entry.pop('date')

        # check for data integrity
        self.assertEqual(serialized_database_entry, self.track_payload[1])


class TestDataBase(APITestCase):

    def setUp(self):
        
        # dummy data
        self.artist = Artist.objects.create(artist_name='Yungengod', record_label='kolumbus beatz')

    def test_model_instance(self):

        # check to see to see if queryset is a model instance
        self.assertIsInstance(self.artist, Artist)

        # check for the model string constructer
        self.assertEqual(str(self.artist), 'Yungengod')
