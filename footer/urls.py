from django.urls import path
from .api import FooterSnippetSerializerViewSet

urlpatterns = [
    path('', FooterSnippetSerializerViewSet.as_view({'get': 'list'}), name='home-list'),
    path('<slug:slug>/', FooterSnippetSerializerViewSet.as_view({'get': 'retrieve'}), name='home-detail'),
]