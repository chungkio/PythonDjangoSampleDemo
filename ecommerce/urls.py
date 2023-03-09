from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
  path('', views.list),
  path('checkout/', views.checkout, name='checkout'),
  path('cart/', views.cart, name='cart'),
  path("order/", views.order, name="order"),
  path('category/<slug:slug>', views.list, name='category'),
  path('product/<slug:slug>', views.Products, name='product'),
]