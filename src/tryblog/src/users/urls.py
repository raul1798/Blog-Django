from django.conf.urls import include, url
from .models import CustomUser
from . import views


urlpatterns = [
    url(r'^cabinet/$', views.cabinet, name='cabinet'),
    url(r'^update_user/$', views.update_user, name='update_user'),
    url(r'^all/$', views.users, name='users'),
	url(r'get/(?P<customuser_pk>[0-9]+)/$', views.get_user, name='get_user'),  
]