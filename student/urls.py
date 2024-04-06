from django.urls import path
from .views import StudentListView,LandingPageView
urlpatterns = [
    path('student/',StudentListView.as_view(),name='student'),
    path('',LandingPageView.as_view(),name='landing')

]