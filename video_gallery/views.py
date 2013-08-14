"""
Views of the video_gallery app.

The views might be a bit confusing at first but I wanted to stick to the
naming conventions for Django views.

Both the ``CategoryDetailView`` and the ``MovieListView`` should have an
almost identical template. They both display a list of movies. The latter view
just displays all movies and the former displays all movies that belong to
a certain category.

"""
from django.views.generic import DetailView, ListView

from .models import Category, Movie


class VideoGalleryViewMixin(object):
    """Mixin that adds common template contexts for views of this app."""
    def get_context_data(self, **kwargs):
        ctx = super(VideoGalleryViewMixin, self).get_context_data(**kwargs)
        ctx.update({'categories': Category.objects.all(), })
        if 'category' in self.kwargs:
            active_category = Category.objects.get(
                slug=self.kwargs.get('category'))
            ctx.update({'active_category': active_category, })
        return ctx


class MovieListView(VideoGalleryViewMixin, ListView):
    """View that displays all movies."""
    model = Movie

    def get_queryset(self):
        return Movie.objects.published()


class CategoryDetailView(VideoGalleryViewMixin, DetailView):
    """
    View that displays a list of movies that belong to the given category.

    """
    model = Category
    slug_url_kwarg = 'category'

    def get_context_data(self, **kwargs):
        ctx = super(CategoryDetailView, self).get_context_data(**kwargs)
        if self.kwargs.get('category'):
            movies = Movie.objects.published().filter(category=self.object)
        else:
            movies = Movie.objects.published()
        ctx.update({'movies': movies, })
        return ctx
