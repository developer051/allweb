from django.db import models

'''
Product
    - title (Char)
    - description (Text)
    - price (decimal)
    - quantity (Int)

'''

class Product(models.Model):
    title = models.CharField(max_length=100) 
    description = models.TextField(null=True, blank=True)  
    price = models.DecimalField(max_digits=5, decimal_places=2 ,null=True,blank=True) 
    quantity = models.IntegerField(default=1,null=True,blank=True)
    instock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    


class ContactList(models.Model):
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    






'''
รัน 2 คำสั่งนี้เพื่อสร้างตารางในฐานข้อมูลทุกครั้งที่สร้าง model ใหม่

python manage.py makemigrations
python manage.py migrate
'''