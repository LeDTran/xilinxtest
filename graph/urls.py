from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.Graph.as_view(), name='Graph'),
    url(r'^export/csv/$', views.ExportGraphCSV, name='ExportGraphCSV'),
]