from django.urls import path
from visualization_app import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("page/", views.home, name="visualization_page"),
]