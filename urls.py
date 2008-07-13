from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^admin/', include('django.contrib.admin.urls')),
)

# This allows Django to serve static files when you're developing your project.
# You'll have to do something else in production.
# More information: http://www.djangoproject.com/documentation/static_files/
# -----------------------------------------------------------------------------
if settings.DEBUG:
    urlpatterns += patterns("django.views",
        url(r"^static/(?P<path>.*)", "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )
