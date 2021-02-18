from django.urls import path , include
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('chat/', include('chat.urls', namespace='chat')),
    path('admin/', admin.site.urls),
    path('login/',LoginView.as_view(),name="login_url"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
]