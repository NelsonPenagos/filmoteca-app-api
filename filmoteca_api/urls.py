from django.conf.urls import url
from filmoteca_api.views import *

urlpatterns = [
    url('movie/$', MovieListView.as_view())
]

