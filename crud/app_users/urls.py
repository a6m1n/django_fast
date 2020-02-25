from django.urls import path

from app_users import views

urlpatterns = [
    path("", views.UsersViews.as_view(), name="list_page"),
    path("<int:pk>/", views.UserDetailView.as_view(), name="detail_page"),
    path("create/", views.CreateUserView.as_view(), name="create_page"),
    path("<int:pk>/change", views.UserUpdate.as_view(), name="update_page"),
    path("delete", views.UserDelete.as_view(), name="delete_page"),
]
