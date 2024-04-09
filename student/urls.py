from django.urls import path
from .views import StudentListView, LandingPageView, StudentDetailView
urlpatterns = [
    path('student/',StudentListView.as_view(),name='student'),
    path('',LandingPageView.as_view(),name='landing'),
    path('student/<int:student_id>/', StudentDetailView.as_view(), name='student-detail'),

]