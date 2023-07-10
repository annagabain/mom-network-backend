from django.urls import path
from message import views


urlpatterns = [
    path('messages/', views.MessageListCreateView.as_view()),
    # path('messages/<int:pk>', views.ProfileDetail.as_view()),

]
