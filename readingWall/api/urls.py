from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from api.account.views import UserCreate
from api.connections.views import Friends
#from api import views
#from api.connections import views

urlpatterns = [
    #url/path for account package
    path('users/', UserCreate.as_view(), name='account-create'),
    path('auth/', include('rest_framework.urls', # ADD THIS URL
                               namespace='rest_framework')),
    path('get-token/', obtain_auth_token),
    #path for Connections
    path('connections/', Friends.as_view(), name='connections'),
]
