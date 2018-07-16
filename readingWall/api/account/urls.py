from django.urls import path
from api.account import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.UserCreate.as_view(), name='account-create')
]
