from django.urls import path
from . import views


urlpatterns = [
    # URL маршруты для API
    path('polls/', views.PollList.as_view()),
    path('polls/<int:pk>/', views.PollDetail.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    # Другие URL маршруты приложения
]
