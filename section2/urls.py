from django.urls import path
from .views import *

urlpatterns = [
    path("section2List/", Section2ListView.as_view(), name="cr_get_post"),
    path("section2Rud/<int:pk>/", Section2RUD.as_view(), name="up_del")
]