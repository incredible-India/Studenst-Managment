from django.shortcuts import render
from django.views import View
from .forms import StudentForm
# Create your views here.

class index(View):
    def get(self, request):
        sform = StudentForm()
        return render(request, 'Student/index.html',{'sform': sform})
    