from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.viewIndex.as_view(), name="index"),
    path('about', views.viewAboutIndex.as_view()),
    path('load-more', views.loadMore, name="loadMore"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)