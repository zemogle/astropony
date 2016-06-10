from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'exoplanets.views.home', name='home'),
    url(r'^planets/', 'exoplanets.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
]
