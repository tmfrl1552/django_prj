from django.urls import path
from . import views

app_name = 'api_children'
urlpatterns = [
    path('', views.ChildrenView.as_view()),
    path('<str:appuserId>/', views.ChildrenView.as_view()),
    path('<int:c_id>', views.ChildrenView.as_view()),
]
