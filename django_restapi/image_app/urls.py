from django.conf.urls import include, url
from . import views

app_name = 'image_app'
urlpatterns = [
    url(r'^userimage/$', views.UserimageCreateAPIView.as_view()),
    url(r'^userprofile/$', views.UserprofileCreateAPIView.as_view()),
]