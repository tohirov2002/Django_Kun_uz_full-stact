from django.urls import path,re_path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]