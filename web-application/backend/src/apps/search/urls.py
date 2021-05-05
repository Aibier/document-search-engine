from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path("files", views.search, name="search"),
    path('files/<str:id>/', views.retrieve_file_details, name='file_detail'),
]
