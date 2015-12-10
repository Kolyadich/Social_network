from basis import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin
from network import views


urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^groups/', views.groups, name='groups'),
    url(r'^members/', views.members, name='members'),
    url(r'^photos/', views.photos, name='photos'),
    url(r'^profile/', views.profile, name='profile'),

    url(r'^admin/', include(admin.site.urls)),
]


# urlpatterns += patterns('',
#     (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
# )