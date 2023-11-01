from django.test import TestCase, Client
from .models import Song, Artist, Genre, Album

# Create your tests here.

class SongTestCase(TestCase):
    def setUp(self):
        genre=Genre.objects.create(name="gospel")
        artist=Artist.objects.create(name="francis plaka")
        album=Album.objects.create(name="unknown")
        Song.objects.create(genre=genre, artist=artist, album=album)


    def test_song_genre(self):
        song = Song.objects.get(genre__name="gospel")
        self.assertEqual(song.get_song_genre_name(), 'gospel')


    def test_song_artist(self):
        song = Song.objects.get(artist__name="francis plaka")
        self.assertEqual(song.get_song_artist_name(), 'francis plaka')


    def test_get_song_album(self):
        song = Song.objects.get(album__name="unknown")
        self.assertEqual(song.get_song_album_name(), "unknown album")

class HomeTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_blog_index(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)