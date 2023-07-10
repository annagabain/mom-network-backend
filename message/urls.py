from django.urls import path
from message import views


urlpatterns = [
    path('messages/', views.MessageListView.as_view()),
    path('messages/<int:pk>', views.MessageDetailView().as_view()),
]
