from django.urls import path
from admin_panel.views import *

app_name = 'admin_panel'

urlpatterns = [
    path('',dashboard, name='dashboard'),
]