from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views
# from views import Graph

urlpatterns = [
    url(r'^$', views.Graph.as_view(), name='graph'),
    # url(r'^$', views.Graph, name='graph'),
]