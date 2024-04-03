from django.urls import path

from .views import NewsCreateView,ListNewView,DetailNewView,EditNewView,DeleteNewView

urlpatterns = [
    path('add/',NewsCreateView.as_view(), name='add-news'),
    path('<int:pk>/', DetailNewView.as_view(), name='show-news'),
    path('edit/<int:pk>/', EditNewView.as_view(), name='edit-news'),
    path('delete/<int:pk>/', DeleteNewView.as_view(), name='delete-news'),
    path('',ListNewView.as_view(), name='list-news')
]