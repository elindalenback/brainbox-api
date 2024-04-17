from django.urls import path
from notebooks import views

urlpatterns = [
    path('notebooks/', views.NotebookList.as_view()),
    path('notebooks/<int:pk>/', views.NotebookDetail.as_view()),
]