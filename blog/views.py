from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import *
from .forms import SubscriptionForm, ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def contact_form(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            message=form.cleaned_data["message"]
            subject=f"A feedback from {name}"
            send_mail(subject, message, from_email=email, recipient_list=[settings.DEFAULT_FROM_EMAIL])
            messages.success(request, "Your feedback has been submitted successfully")
            return redirect("blog:home")
        else:
            return render(request, "contact_form.html", {"form": form})
    else:
        return render(request, "contact_form.html", {"form": ContactForm()})

def subscription_form(request):
    if request.method == "GET":
        return render(request, "subscription_form.html", {"form": SubscriptionForm()})
    elif request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are subscribed successfully")
            return redirect("blog:home")
        else:
            messages.error(request, "Subscription failed. Please check the errors and try again")
            return render(request, 'subscription_form.html', {"form": form})

def home(request):
    genres=Genre.objects.all()
    artists=Artist.objects.all()
    albums=Album.objects.all()
    songs=Song.objects.all()
    context={"title": "Home",
    "artists": artists,
    "albums": albums,
    "songs": songs,
    "genres": genres}
    return render(request, "home.html", context)


def song(request, song_title):
    song=get_object_or_404(Song, title=song_title)
    context={"song": song,
    "title": song.title}
    return render(request, "song.html", context)

def search_item(request):
    if request.method == 'GET':
        query=request.GET.get('search')
        submitbutton=request.GET.get('submit')
        if query is not None:
            lookups=Q(genre__name__icontains=query)|Q(artist__name__icontains=query)|Q(title__icontains=query)
            songs=Song.objects.filter(lookups).distinct()
            context={'songs': songs,
            'submitbutton': submitbutton}
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')
