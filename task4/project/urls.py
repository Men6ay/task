from django.urls import path
from .views import index, create, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('detete/<int:id>/', delete, name='delete'),
    path('update/<int:id>', update, name='update'),
]