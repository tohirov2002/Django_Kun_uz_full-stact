from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('news/', include('app_news.urls')),
    path('accounts/', include('users.urls')),
    path('', include('app_pages.urls')),
]
