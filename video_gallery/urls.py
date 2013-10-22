"""URLs for the video_gallery app."""
from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView

from .models import Movie
from .views import CategoryDetailView, MovieListView


urlpatterns = patterns(
    '',
    url(r'^$',
        MovieListView.as_view(),
        name='video_gallery_movie_list',),
    url(r'(?P<pk>\d+)/$',
        DetailView.as_view(model=Movie),
        name='video_gallery_movie_detail'),
    url(r'(?P<category>[^/]*)/$',
        CategoryDetailView.as_view(),
        name='video_gallery_category_detail',),
    url(r'(?P<category>[^/]*)/(?P<pk>\d+)/$',
        DetailView.as_view(model=Movie),
        name='video_gallery_movie_detail'),
)
