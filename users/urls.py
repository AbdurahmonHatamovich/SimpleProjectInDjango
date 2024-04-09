from django.urls import path
from .views import RegistrationPageView,LoginPageView,LogoutPageView

urlpatterns = [
    path('auth/register/', RegistrationPageView.as_view(), name='register'),
    path('auth/login/', LoginPageView.as_view(), name='login'),
    path('auth/logout/', LogoutPageView.as_view(), name='logout')
]