from django.urls import path
from main.views import mainView

urlpatterns = [
    path("manage", mainView.manageView, name='manage'),
    path("search", mainView.searchView, name='search'),
    path("", mainView.home_view, name='home')
]