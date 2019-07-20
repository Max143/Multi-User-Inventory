from django.contrib import admin
from django.urls import path, include
# Register
from users import views as user_views

from django.contrib.auth import views as auth_views   # Class-bassed Views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stocks.urls')),
    path('', include('users.urls')),

    # Register URL
    path('register/', user_views.RegisterView, name='register'),

    # Login and Logout URL
    # # by default template_name = 'registration/login.html' below
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # Profile Views
    path('profile/', user_views.ProfileView, name='profile'),



]

