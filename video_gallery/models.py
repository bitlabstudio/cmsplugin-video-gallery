"""
Models for the video_gallery app.

A video gallery is just a list of movies that belong together. We group them
by using the ``Category`` model, therefore each category is one "gallery".

"""
from os.path import basename

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField


class Category(models.Model):
    """
    Is used to categorize movies.

    :name: The human readable name of the category.
    :slug: The slug of the category

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    slug = models.SlugField(
        max_length=32,
        verbose_name=_('Slug'),
    )

    def __unicode__(self):
        return self.name


class MovieManager(models.Manager):
    """Custom manager for the ``Movie`` model."""
    def published(self):
        """
        Returns the published movies.

        """
        qs = self.get_query_set()
        qs = qs.filter(is_published=True)
        return qs


class Movie(models.Model):
    """
    Can be placed as a CMS plugin or shown in a category list view.

    TODO: Add field descriptions

    """
    category = models.ForeignKey(
        Category,
        verbose_name=_('Category'),
        null=True, blank=True,
    )

    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )

    date = models.DateTimeField(
        verbose_name=_('Date'),
        blank=True, null=True,
    )

    location = models.CharField(
        max_length=100,
        verbose_name=_('Location'),
        blank=True, null=True,
    )

    description = PlaceholderField(
        'description',
        verbose_name=_('Description'),
    )

    movie = models.FileField(
        _('Movie file'),
        upload_to='video_gallery_movies',
        help_text=_('use .flv file or h264 encoded video file'),
        blank=True, null=True,
    )

    movie_url = models.CharField(
        _('Movie url'),
        max_length=255,
        help_text=_(
            'Youtube embed url.'
            ' Example: http://www.youtube.com/embed/wrED69Ti3l4?feature=player_detailpage'),
        blank=True, null=True,
    )

    image = models.ImageField(
        _('image'),
        upload_to='video_gallery_thumbnails',
        help_text=_('Preview image file'),
        null=True, blank=True,
    )

    width = models.PositiveSmallIntegerField(_('width'))

    height = models.PositiveSmallIntegerField(_('height'))

    auto_play = models.BooleanField(
        _('Auto play'),
        default=False,
    )

    auto_hide = models.BooleanField(
        _('Auto hide'),
        default=False,
    )

    fullscreen = models.BooleanField(
        _('Fullscreen'),
        default=True,
    )

    loop = models.BooleanField(
        _('Loop'),
        default=False,
    )

    is_published = models.BooleanField(
        _('Is published'),
        default=False,
    )

    objects = MovieManager()

    def __unicode__(self):
        if self.title:
            return self.title
        if self.movie:
            name = self.movie.path
        else:
            name = self.movie_url
        return u"%s" % basename(name)

    def get_height(self):
        return "%s" % (self.height)

    def get_width(self):
        return "%s" % (self.width)

    def get_movie(self):
        if self.movie:
            return self.movie.url
        else:
            return self.movie_url

    def get_absolute_url(self):
        kwargs = {'pk': self.pk, }
        if self.category:
            kwargs.update({'category': self.category.slug, })
        return reverse('video_gallery_movie_detail', kwargs=kwargs)


class MoviePlugin(CMSPlugin):
    """Plugin model to link to a specific movie instance."""
    movie = models.ForeignKey(
        Movie,
        verbose_name=_('Movie'),
    )
