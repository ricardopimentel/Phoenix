from django.conf.urls import url, include

urlpatterns = [
    url(r'^phoenix/', include('Phoenix.core.urls')),
]
