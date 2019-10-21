from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from filmoteca_api.views.movie_views import *
from filmoteca_api.views.user_views import *

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('movie/', movie_list),
    path('movie/<int:pk>', movie_detail),
    path('movie/name/<str:name>', movie_name),
    path('movie/genre/<str:genre>', movie_genre),
    path('movie/director/<str:director>', movie_director),
    path('movie/recommendation', movie_recommendation),
]

urlpatterns = format_suffix_patterns(urlpatterns)
