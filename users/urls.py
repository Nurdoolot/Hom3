from django.urls import path
from .views import login_page, register_page, logout_user, profile

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_page, name='register'),
    path('profile/', profile, name='profile')
]