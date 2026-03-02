from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe-list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe-detail'),
]