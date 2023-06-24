from django.urls import path
from . import views


urlpatterns =[
    path('',views.dasboard, name='dasboard'),
    path('home/',views.home, name='home'),
    path('blog/', views.blog,name='blog'),
    path('about/', views.about, name='about'),
    path('contract', views.contract, name='contract'),
]