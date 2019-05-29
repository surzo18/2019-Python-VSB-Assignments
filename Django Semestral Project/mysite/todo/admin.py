from django.contrib import admin

from .models import Film
from .models import Actor
from .models import Genre
from .models import Comment
from .models import Star


# Register your models here.
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ( 'id','film_name')

@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ( 'id','film_name','user','value')

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Comment)
