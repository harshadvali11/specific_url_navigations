from django.urls import path
from rcb.views import *

app_name='rcb'

urlpatterns=[
    path('virat/',virat,name='virat'),
]