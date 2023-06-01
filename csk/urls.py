from django.urls import path
from csk.views import *
app_name='csk'

urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
]