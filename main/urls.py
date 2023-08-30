from django.urls import path, include
from . import views

from rest_framework.authtoken.views import obtain_auth_token
from .views import CostAPIView 

urlpatterns=[
    path('',views.home , name='home'),
    path('home',views.home , name='home'),
    path('sign-up',views.sign_up , name='sign_up'),
    path('get-data',views.list_users , name='data'),
    path('api/token/', obtain_auth_token, name='token_obtain_pair'),
    path('api/cost/', CostAPIView.as_view(), name='user_cost'),

]