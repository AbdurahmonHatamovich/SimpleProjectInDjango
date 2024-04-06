from django.shortcuts import render
from django.views.generic import View
from .models import Students


def student_view(request):
    return render(request, 'student.html')

class StudentListView(View):
    def get(self,request):
        students = Students.objects.all()
        return render(request, 'student.html',{'students':students})



# class StudentDetailView(View):
#     def get(self,request,id):
#         student = Students.objects.get(id=id)
#         context = {'student':student}
#         return render(request, 'studentsdetail.html',context)


class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html')