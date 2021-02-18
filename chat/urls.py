from django.urls import path, re_path

from . import views
from .views import index, room
from django.contrib.auth.views import LoginView,LogoutView

from django.contrib.auth.views import LoginView,LogoutView
app_name = 'chat'

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
    path('login/',LoginView.as_view(),name="login_url"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
	path('register/',views.registerView,name="register_url"),

]