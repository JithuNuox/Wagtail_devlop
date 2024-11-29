from django.urls import path
from .api import BlogPageSerializerViewSet

urlpatterns = [
    path('', BlogPageSerializerViewSet.as_view({'get': 'list'}), name='blog-list'),
    path('<slug:slug>/', BlogPageSerializerViewSet.as_view({'get': 'retrieve'}), name='blog-detail'),
    # path('<slug:slug>/related/', BlogPageViewSet.as_view({'get': 'related'}), name='blog-related'),

]