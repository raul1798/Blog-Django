from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'article/$', views.article, name='article'),
    url(r'all/$', views.all_articles, name='all_articles'),
    url(r'get/(?P<article_pk>[0-9]+)/$', views.get_article, name='get_article'), 
    url(r'contact/$', views.contactView, name='contact'), 
    url(r'contactView/$', views.contactView, name='contactView'),  
 ]