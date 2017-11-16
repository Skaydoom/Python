from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='loginsys'),
    url(r'^logout/$', views.logout, name='loginsys'),
    url(r'^register/$', views.register, name='loginsys'),
]
