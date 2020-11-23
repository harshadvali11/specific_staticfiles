from django.shortcuts import render

# Create your views here.

def specific_static(request):
    return render(request,'static_files.html')