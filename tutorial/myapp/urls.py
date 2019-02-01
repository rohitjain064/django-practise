from django.urls import path
from.views import *

urlpatterns=[
    path("",home,name="home"),
    path('studentform/',student,name='student_form'),
    path('registration',registration,name='registration'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('search/',search,name='search'),
]