from django.urls import path
from newsletters import views

urlpatterns = [
    path('newsletter/', views.NewsletterListView.as_view()),
    path('newsletter/<int:pk>/', views.NewsletterDetailView.as_view()),

]
