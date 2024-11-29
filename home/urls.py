from django.urls import path
from .api import HomePageViewSet

urlpatterns = [
    path('', HomePageViewSet.as_view({'get': 'list'}), name='home-list'),
    path('<slug:slug>/', HomePageViewSet.as_view({'get': 'retrieve'}), name='home-detail'),
]