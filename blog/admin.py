from django.contrib import admin
from .models import *



class SongInline(admin.StackedInline):
    model = Song
    fk_name = "album"
    extra = 10

class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongInline]
    
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Subscriber)
admin.site.register(Song)

admin.site.site_header = "Entertainment site management"
admin.site.site_title = "Entertainment hipe GH"
admin.site.site_url = "/blog/"
admin.site.index_title = "dashboard"
