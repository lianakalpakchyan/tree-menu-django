from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^(?P<slug>.*)$', views.page_view, name='page'),
]
