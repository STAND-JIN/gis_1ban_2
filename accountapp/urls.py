from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import introduce, AccountCreateView, AccountDetailView

app_name = 'accountapp'

urlpatterns = [
    path('introduce/', introduce, name='introduce'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'),
         name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),

    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail')
]