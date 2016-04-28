from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.upload, name = 'upload'),
    url(r'^execute/$', views.execute, name = 'execute'),
    url(r'^help/$', views.help, name = 'help'),
    url(r'^results/$', views.results, name = 'results'),
    url(r'^loading/$', views.loading, name = 'loading'),
]
