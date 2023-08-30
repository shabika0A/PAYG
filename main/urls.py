from django.urls import path
from . import views

urlpatterns=[
    path('',views.home , name='home'),
    path('home',views.home , name='home'),
    path('sign-up',views.sign_up , name='sign_up'),
    path('get-data',views.list_users , name='data'),

]