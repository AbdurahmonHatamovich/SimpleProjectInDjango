from django.shortcuts import render
from django.views import View
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin

class BooksListView(LoginRequiredMixin,View):
    def get(self,request):
        search = request.GET.get('search')
        print(f"|||||||||||||||||||||||||||||||{request.GET}")
        if not search:
            books = Book.objects.all()
            context = {
                'books': books ,'search':search
            }
            return render(request, 'library.html', context)
        else:
            books = Book.objects.filter(title__icontains=search)
            if books:
                context = {
                    'books': books, 'search':search
                }
                return render(request, 'library.html', context)
            else:
                return render(request, 'not_found_page.html')





class BooksDetailView(View):
    def get(self,request,id):
        book = Book.objects.get(id=id)
        context = {'book': book}
        return render(request,'bookdetail.html',context)