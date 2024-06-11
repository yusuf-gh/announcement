

from django.urls import path
from .views import *

urlpatterns = [
    path("announcement/", AnnListView.as_view(), name="ann-get"),
    path("ann_update/<uuid:id>/", AnnRUD.as_view(), name="ann-updte"),
    path("get_add_byUser/<int:id>/", FilterByOwner.as_view(), name="ann-filter")
]

    
