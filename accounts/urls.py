from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.viewAccountIndex.as_view(),name="index"),
    path('my-account', views.my__acount,name="my-account"),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]