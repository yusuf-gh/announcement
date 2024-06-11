from django.urls import path
from .views import UsersListView, UsersRUD

urlpatterns = [
    path("users/", UsersListView.as_view(), name="get_users_list"),
    path("update/<int:pk>/", UsersRUD.as_view(), name="get_update_putpatch_delete")
    
]