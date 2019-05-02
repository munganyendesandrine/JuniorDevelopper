from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^today/$',views.content_of_day,name='juniordevapToday'),
    url('^lesson2/',views.lesson2,name ='lesson2'),
    url('^lesson3/',views.lesson3,name ='lesson3'),
    url('^lesson4/',views.lesson4,name ='lesson4'),

   
]