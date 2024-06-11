from django.urls import path
from .views import *

urlpatterns = [
    path("cardList/", CardListView.as_view(), name="cr_get_post"),
    path("cardRud/<int:pk>/", CardRUD.as_view(), name="up_del")
]