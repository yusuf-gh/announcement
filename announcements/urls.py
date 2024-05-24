

from django.urls import path
from .views import *

urlpatterns = [
    path("announcement/", AnnListView.as_view(), name="ann-get"),
    path("ann_update/<uuid:id>/", AnnRUD.as_view(), name="ann-updte"),
    path("get_user/<int:id>/", FilterByOwner.as_view(), name="ann-filter"),
    
    path("headerList/", HeaderListView.as_view(), name="cr_get_post"),
    path("header_rud/", HeaderRUD.as_view(), name="up_del"),
    
    path("cardList/", CardListView.as_view(), name="cr_get_post"),
    path("card_rud/", CardRUD.as_view(), name="up_del"),
    
    path("sectionList/", SectionListView.as_view(), name="cr_get_post"),
    path("section_rud/", SectionRUD.as_view(), name="up_del"),
    
    path("section2List/", Section2ListView.as_view(), name="cr_get_post"),
    path("section2_rud/", Section2RUD.as_view(), name="up_del")
    
    
]

    
