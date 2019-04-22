"""django_rest_framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path

from posts_app.views import PostAPI, CommentCreateAPI

urlpatterns = [
    path('', PostAPI.as_view(), name="posts"),
    re_path(r'^(?P<post_id>[0-9]+)$', PostAPI.as_view(), name='posts'),
    path('<int:post_id>/comments/', CommentCreateAPI.as_view(), name="comments"),

]
