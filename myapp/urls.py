from django.urls import path
from . import views

from django.views.generic.base import RedirectView
# for redirecting

urlpatterns = [
    path('', views.myfunctioncall, name="index"),
    path('about/', views.myfunctionabout, name="about"),
    path('add/<int:a>/<int:b>', views.add, name="add"),
    path('intro/<str:name>/<int:age>', views.intro, name="intro"),
    path('mypage/', views.mypage, name='mypage'),
    path('mysecondpage/', views.mysecondpage, name='mysecondpage'),
    path('mythirdpage/', views.mythirdpage, name='mythirdpage'),
    path('myimagepage/', views.myimagepage, name='myimagepage'),
    path('myimagepage2/', views.myimagepage2, name='myimagepage2'),
    path('myimagepage3/', views.myimagepage3, name='myimagepage3'),
    path('myimagepage4/', views.myimagepage4, name='myimagepage4'),
    path('imagepage5/<str:imagename>', views.imagepage5, name='imagepage5'),
    path('myform/',views.myform,name='myform'),
    path('submitmyform',views.submitmyform,name='submitmyform'),
    path('myform2/',views.myform2,name='myform2'),
# nothing done 
    # path("new-form/", views.myform2(), name='new-form'),
    # path("old-form/", RedirectView.as_view(pattern_name='new-form')),
]
