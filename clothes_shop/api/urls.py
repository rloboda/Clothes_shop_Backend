from django.urls import path
from .views import ItemListCreateView, ItemDetailView

app_name = 'clothes'

urlpatterns = [
    path('cloth', ItemListCreateView.as_view(), name='cloth-list'),
    path('cloth/<str:slug>', ItemDetailView.as_view(), name='cloth-detail'),
]
