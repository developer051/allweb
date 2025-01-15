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
    description = models.TextField(null=True, blank=True)   #null=True, blank=True คือ ให้มันเป็นค่าว่างได้ ไม่ต้องกรอกก็ได้
    price = models.DecimalField(max_digits=5, decimal_places=2 ,null=True,blank=True) #decimal คือ ตัวเลขทศนิยม  , decimal_places=2 คือ จำนวนทศนิยม 2 ตำแหน่ง , null=True,blank=True คือ ให้มันเป็นค่าว่างได้ ไม่ต้องกรอกก็ได้
    quantity = models.IntegerField(null=True,blank=True) #null=True, blank=True คือ ให้มันเป็นค่าว่างได้ ไม่ต้องกรอกก็ได้
