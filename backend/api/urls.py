from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view()),
    path('verify-otp/', views.OTPVerificationView.as_view()),
]