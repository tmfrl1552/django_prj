from django.urls import path
from . import views

app_name = 'api_user'
urlpatterns = [
    path('', views.AppUserView.as_view()),
    path('<str:uid>/', views.AppUserView.as_view())
]
