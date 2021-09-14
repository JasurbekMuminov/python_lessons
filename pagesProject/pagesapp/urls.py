from django.urls import path
from .views import HomePageView,AboutPagesview

urlpatterns = [
    path('about/', AboutPagesview.as_view(), name = 'about'),
    path('',HomePageView.as_view(),name = 'home'),
]