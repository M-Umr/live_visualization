from django.urls import path
from visualization_app import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("", views.main_home, name="visualize_image"),
]