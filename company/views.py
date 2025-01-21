from django.shortcuts import render
from django.http import HttpResponse  #<< เพิ่มใหม่   เพิ่อโชว์ข้อความ HelloWorld
from .models import *

def Home(request):
    allproduct = Product.objects.all()   #  SELECT * FROM Product
    context = {'allproduct': allproduct}   # contect คือตัวแปรที่ส่งไปที่ template
    return render(request, 'company/home.html', context)


def AboutUs(request):
    return render(request, 'company/aboutus.html')


def ContactUs(request):

    context = {}  #  สิ่งที่จะแนบไปกับ template

    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        print(title)
        print(email)
        print(detail)
        print('--------------------')
        # เมื่อมีการส่งข้อมูลมาจาก form ให้ทำการบันทึกลงใน database
        newrecord = ContactList()
        newrecord.title = title
        newrecord.email = email
        newrecord.detail = detail
        newrecord.save()
        context['message'] = 'บันทึกข้อมูลเรียบร้อยแล้ว'   # แจ้งเมื่อทำการบันทึกข้อมูลเรียบร้อยแล้ว ต้องมีบรรทัด 17 ด้วย

    return render(request, 'company/contact.html',context)  # follow line 17,34   