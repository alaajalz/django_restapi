from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('movies/', views.movies, name='movies'),
    path('movies/<int:did>/', views.movie, name='movie'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)