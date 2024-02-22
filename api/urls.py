from django.urls import path
from api import views

urlpatterns = [
    path('create-user/', views.UsersCreateAPIView.as_view()),
    path('users/<int:chat_id>/', views.UserListAPIView.as_view()),

    path('category/', views.CategoryListAPIView.as_view()),
    path('category/<int:pk>/', views.GetCategoryAPIView.as_view()),

    path('question/<int:pk>/', views.QuestionnaireListAPIView.as_view()),

    path("question-user/", views.QuestionFilterAPIView.as_view())
    # path("question/<int:chat_id>/<int:category>/", views.QuestionFilterAPIView.as_view())
]
