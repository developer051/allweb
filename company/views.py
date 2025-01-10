#ไว้ใส่ Program ที่เขียนเพื่อโชว์ใน website
#---------------------------------

from django.shortcuts import render
from django.http import HttpResponse  #<< เพิ่มใหม่   เพิ่อโชว์ข้อความ HelloWorld



# def Home(request):
#     return HttpResponse('<h1>Apps is COMPANY </h1> <br> <p>by Supachai Ocharos</p>')  #br คื่อการขึ้นบรรทัดใหม่

def Home(request):
    return render(request, 'company/home.html')