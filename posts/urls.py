from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("<int:id>/",views.post,name="post"),
    path("tag/<int:id>",views.Tag,name='tag'),
]