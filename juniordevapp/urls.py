from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^today/$',views.content_of_day,name='juniordevapToday'),
    url('^lesson1/',views.lesson1,name ='lesson1'),
]