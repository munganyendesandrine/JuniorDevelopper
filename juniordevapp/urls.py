from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.content,name = 'content'),
    url('^today/$',views.content_of_day,name='juniordevapToday')
]