from django.urls import path
from polls import views

urlpatterns = [
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(),
         name='question-detail'),
    path('questions/<int:question_id>/choices/', views.ChoiceList.as_view(),
         name='choice-list'),
    path('questions/<int:question_id>/choices/<int:pk>/',
         views.ChoiceDetail.as_view(), name='choice-detail'),
]
