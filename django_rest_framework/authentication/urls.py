from django.contrib import admin
from django.urls import path

from .views import RegisterView, UserList, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('users/', UserList.as_view(), name="users"),
    path('admin/', admin.site.urls),
    path('user/', UserView.as_view(), name="user"),

]
