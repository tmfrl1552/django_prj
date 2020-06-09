from django.urls import path
from . import views

app_name = 'api_rsult'
urlpatterns = [
    path('', views.ResultView.as_view()),  # User에 관한 API를 처리하는 view로 Request를 넘김
    path('<str:appuserId>/<str:childrenName>', views.ResultView.as_view())
]
