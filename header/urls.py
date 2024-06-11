from django.urls import path
from .views import *

urlpatterns = [
    path("headerList/", HeaderListView.as_view(), name="cr_get_post"),
    path("headerRud/<int:pk>/", HeaderRUD.as_view(), name="up_del"),
]
