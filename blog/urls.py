from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name="home"),
        path("contact/", views.contact_form, name="contact"),
    path("subscribe/", views.subscription_form, name="subscribe"),
        path("search/", views.search_item, name="search"),
    path("<str:song_title>/", views.song, name="music-song"),
    ]