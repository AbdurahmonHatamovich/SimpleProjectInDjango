from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Students
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


def student_view(request):
    return render(request, 'student.html')

class StudentListView(LoginRequiredMixin,View):
    def get(self,request):
        students = Students.objects.all()
        return render(request, 'student.html',{'students':students})


class StudentDetailView(View):
    def get(self, request, student_id):
        search = request.GET.get('search')
        if search:
            students = Students.objects.filter(first_name__icontains=search) | Students.objects.filter(
                last_name__icontains=search)
            if students:
                context = {'students': students, 'search': search}
                return render(request, 'studentdetail.html', context)
            else:
                return render(request, 'not_found_page.html')
        else:
            student = Students.objects.get(id=student_id)
            context = {'student': student}
            return render(request, 'studentdetail.html', context)


class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html')

