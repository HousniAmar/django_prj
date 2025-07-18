from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='products'),
     path('dashboard/', views.product_dashboard, name='product_dashboard'),
]