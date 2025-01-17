from django.shortcuts import render
from django.http import HttpResponse  #<< เพิ่มใหม่   เพิ่อโชว์ข้อความ HelloWorld
from .models import *

def Home(request):
    allproduct = Product.objects.all()   #  SELECT * FROM Product
    context = {'allproduct': allproduct}
    return render(request, 'company/home.html', context)


def AboutUs(request):
    return render(request, 'company/aboutus.html')


def ContactUs(request):
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        print(title)
        print(email)
        print(detail)
        print('--------------------')

    return render(request, 'company/contact.html')