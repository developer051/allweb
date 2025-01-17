#อยากให้ Database ตัวไหนไป show หลังบ้านบ้าง
from django.contrib import admin
from .models import *                  #<< เพิ่มใหม่  [ ให้ Show ทุกตัวที่อยู่ใน models.py ทั้งหมด ]

admin.site.register(Product)            #<< ทำให้ Admin สามารถเข้าถึง Product database ได้
admin.site.register(ContactList)        #<< ทำให้ Admin สามารถเข้าถึง ContactList database ได้