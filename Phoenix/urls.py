from django.conf.urls import url, include

urlpatterns = [
    url(r'^phoenix/', include('Phoenix.core.urls')),
    url(r'^phoenix/devices-control/', include('Phoenix.devices.urls')),
]
