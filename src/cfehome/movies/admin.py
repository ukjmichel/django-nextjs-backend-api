from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MovieEntry, Rating


# Custom admin view for MovieEntry
class MovieEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "director", "release_date", "genre", "average_rating")
    search_fields = ("title", "director", "genre")
    list_filter = ("genre", "release_date")


# Custom admin view for Rating
class RatingAdmin(admin.ModelAdmin):
    list_display = ("movie", "user", "score", "comment", "created_at")
    search_fields = ("movie__title", "user__username")
    list_filter = ("score",)


# Register the models with the admin site
admin.site.register(MovieEntry, MovieEntryAdmin)
admin.site.register(Rating, RatingAdmin)
