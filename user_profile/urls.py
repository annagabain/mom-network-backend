from django.urls import path
from user_profile import views


urlpatterns = [
    path('user_profile/', views.ProfileList.as_view()),
]
