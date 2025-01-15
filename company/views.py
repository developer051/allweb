from django.shortcuts import render
from django.http import HttpResponse  #<< เพิ่มใหม่   เพิ่อโชว์ข้อความ HelloWorld


def Home(request):
    return render(request, 'company/home.html')


def AboutUs(request):
    return render(request, 'company/aboutus.html')


def ContactUs(request):
    return render(request, 'company/contact.html')