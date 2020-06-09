from django.urls import path
from . import views

app_name = 'api_comments'
urlpatterns = [
    path('', views.CommentsView.as_view()),  # User에 관한 API를 처리하는 view로 Request를 넘김
    path('<str:itype>', views.CommentsView.as_view()),
    path('call/<str:uimage>', views.TreemodelView.as_view()),
]
