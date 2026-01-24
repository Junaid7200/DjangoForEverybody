from django.contrib import admin
from mkt.models import Ad, Comment, Favorite
# Register your models here.

admin.site.register(Ad)
admin.site.register(Comment)
admin.site.register(Favorite)