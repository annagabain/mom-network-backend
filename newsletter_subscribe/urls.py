from django.urls import path
from newsletter_subscribe import views

urlpatterns = [
    path('newsletter/', views.NewsletterListView.as_view()),
    path('newsletter/<int:pk>/', views.NewsletterDetailView.as_view()),

]
