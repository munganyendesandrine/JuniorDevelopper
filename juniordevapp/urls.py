from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^teacher/(\d+)', views.teacher, name='teacher')

    # url(r'^$',views.home,name = 'home'),
    # url(r'^profile/', views.profile, name='profile'),
    # url(r'^myProfile/(\d+)', views.myProfile, name='myProfile'),
    # url(r'^image/', views.image, name='image'),

]