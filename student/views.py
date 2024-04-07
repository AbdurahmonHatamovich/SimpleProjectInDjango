from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Students
from django.contrib.auth.models import User


def student_view(request):
    return render(request, 'student.html')

class StudentListView(View):
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




class RegistrationPageView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if password_1 == password_2:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username)
            user.set_password(password_1)
            user.save()
            return redirect('landing')
        else:
            return render(request, 'auth/register.html')


class LoginPageView(View):
    def get(self, request):
        return render(request, 'auth/login.html')


    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username=username,password=password)
        if user:
            return redirect('landing')
        else:
            return render(request, 'usernotfound.html')