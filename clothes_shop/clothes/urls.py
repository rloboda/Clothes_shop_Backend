from django.urls import path
from . import views

app_name = 'clothes'

urlpatterns = [
    path('', views.show_clothes, name='page'),
    path('new-cloth/', views.add_new_cloth, name='new-cloth'),
    path('<slug:slug>', views.show_cloth_item, name='item'),
]
