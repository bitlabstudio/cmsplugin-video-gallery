"""Admin classes for the video_gallery app."""
from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdmin

from . import models


class MovieAdmin(PlaceholderAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Movie, MovieAdmin)
