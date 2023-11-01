from django.contrib.sitemaps import Sitemap
from blog.models import Song

class SongSitemap(Sitemap):
    changefreq="always"
    priority=0.5
    def items(self):
        return Song.objects.all()
    def lastmod(self, obj):
        return obj.release_date