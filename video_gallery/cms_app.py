"""CMS apphook for the video_gallery app."""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class VideoGalleryApphook(CMSApp):
    name = _("Video Gallery Apphook")
    urls = ["video_gallery.urls"]


apphook_pool.register(VideoGalleryApphook)
