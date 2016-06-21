from django.conf.urls import include, url
from django.contrib import admin
from exoplanets.views import home, planets, PlanetUpdate, PlanetDetails, missionlist

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^planets/$', planets, name='home'),
    url(r'^planet/(?P<pk>[0-9]+)/update/$', PlanetUpdate.as_view(), name="update_planet" ),
    url(r'^planet/(?P<pk>[0-9]+)/$', PlanetDetails.as_view(), name="planet_detail" ),
    url(r'^missionplanets/(?P<mission>\w+)/$', missionlist),

    url(r'^admin/', include(admin.site.urls)),
]
