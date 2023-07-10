from django.urls import path
from page import views

urlpatterns = [
    path('page/', views.PageListCreateView().as_view()),
    path('page/<int:pk>/', views.PageDetailView().as_view()),

]
