from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('my-account', views.AccountView.as_view(), name="my-account"),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
]