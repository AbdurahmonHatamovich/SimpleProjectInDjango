from django.urls import path
from .views import StudentListView, LandingPageView, StudentDetailView,LoginPageView,RegistrationPageView

urlpatterns = [
    path('student/',StudentListView.as_view(),name='student'),
    path('',LandingPageView.as_view(),name='landing'),
    path('student/<int:student_id>/', StudentDetailView.as_view(), name='student-detail'),
    path('auth/login/', LoginPageView.as_view(), name='login'),
    path('auth/register/', RegistrationPageView.as_view(), name='register')

]