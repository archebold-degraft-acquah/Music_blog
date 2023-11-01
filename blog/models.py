from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# defining models


class Subscriber(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Genre(models.Model):
    name= models.CharField(max_length=100, help_text="separate words with dashes instead of spaces")

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-name"]
    

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='artists', null=True)

    def __str__(self):
        return self.name

class Meta:
    ordering = ["-name"]


class Album(models.Model):
    name=models.CharField(max_length=100, help_text="Enter album name. If the song you are publishing has no album name, type 'Unknown' or 'Unknown album'")
    album_image=models.FileField(upload_to="albums", blank=True, null=True)
    record_label=models.CharField(max_length=100, blank=True, null=True)
    album_date=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class Song(models.Model):
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist=models.ForeignKey(Artist, on_delete=models.CASCADE)
    album=models.ForeignKey(Album, on_delete=models.CASCADE, blank=False, null=True)
    title=models.CharField(max_length=100, default="unknown-track")
    short_description=models.TextField(max_length=1000, blank=True, help_text="A short description about the song")
    audio_file = models.FileField(upload_to='songs')
    audiomak_link=models.URLField(max_length=200, blank=True, null=True)
    release_date = models.DateField(null=True)
    notification = models.BooleanField("Notify your subscribers about this song (Required)", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:music-song', args=[self.title])

    def get_song_artist_name(self):
        return self.artist.name

    def get_song_genre_name(self):
        return self.genre.name

    def get_song_album_name(self):
        if self.album.name == "unknown":
            return "unknown album".lower()
        else:
            return self.album.name

    class Meta:
        ordering = ["-title"]


@receiver(post_save, sender=Song)
def email_notification(sender, instance, created, **kwargs):
    if created and instance.notification == True:
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            send_mail("A new song added", "New songs added", from_email="archebolddegraftacquah@gmail.com", recipient_list=[subscriber.email], html_message="<h1>We've added a new song. Check out!</h1>")

