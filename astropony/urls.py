from django.conf.urls import include, url
from django.contrib import admin
from exoplanets.views import home, planets

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^planets/', planets, name='home'),

    url(r'^admin/', include(admin.site.urls)),
]
