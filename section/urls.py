from django.urls import path
from .views import *

urlpatterns = [
    path("sectionList/", SectionListView.as_view(), name="cr_get_post"),
    path("sectionRud/<int:pk>/", SectionRUD.as_view(), name="up_del"),
]