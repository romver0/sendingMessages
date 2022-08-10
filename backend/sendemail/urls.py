from django.urls import path

from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('abs/', sendingUserView, name='sending_user'),
    path('eafdas/', sendingUsersView, name='sending_users'),
    path('success/', success_view, name='success'),
]
