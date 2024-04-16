from django.urls import path
from . import views

urlpatterns = [
    path('tags/', views.TagListCreateView.as_view(), name='tag-list-create'),
]