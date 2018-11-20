from django.conf.urls import url
from Phoenix.core import views


urlpatterns = [
    url(r'^$', views.home, name='Home'),
]