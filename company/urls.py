from django.urls import path
from .views import *

urlpatterns = [
    path('', Home , name='home-page'),  #<< name คือชื่อเล่นของ path นี้
    path('aboutus/', AboutUs , name='aboutus-page'),  #<< name คือชื่อเล่นของ path นี้
]

