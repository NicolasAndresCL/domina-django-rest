from django.contrib import admin

from movie.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date", "duration")
    search_fields = ["title"]
    ordering = ["release_date"]


admin.site.register(Movie, MovieAdmin)
