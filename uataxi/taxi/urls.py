from django.conf.urls import patterns, url
from taxi import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', views.Detail.as_view(), name='detail'),
)
