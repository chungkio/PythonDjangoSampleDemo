from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
  path('', views.list),
  path('<slug:slug>', views.post, name='post'),
]