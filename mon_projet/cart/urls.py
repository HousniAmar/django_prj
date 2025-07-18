from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('api/cart/', views.get_cart, name='get_cart'),
    path('api/cart/add/', views.add_to_cart, name='add_to_cart'),
    path('api/cart/item/<int:item_id>/update/', views.update_cart_item, name='update_cart_item'),
    path('api/cart/item/<int:item_id>/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('api/cart/clear/', views.clear_cart, name='clear_cart'),
]