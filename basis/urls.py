from basis import settings
from django.conf.urls import url, patterns
from django.contrib import admin

from network import views


urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^groups/', views.groups, name='groups'),
    url(r'^members/', views.members, name='members'),
    url(r'^photos/', views.photos, name='photos'),
    url(r'^profile/', views.profile, name='profile'),

    url(r'^admin/', admin.site.urls),
]


# if settings.DEBUG:
#     urlpatterns += patterns('',
#
#                             url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#                                 'document_root': settings.MEDIA_ROOT,
#                             }),
#     )
