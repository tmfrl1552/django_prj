from django.conf.urls import include, url
from . import views

app_name = 'image_app'
urlpatterns = [
    url(r'^upload/$', views.ImageCreateAPIView.as_view()),
]