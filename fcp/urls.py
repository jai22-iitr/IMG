from django.urls import path , include
from django.contrib import admin

urlpatterns = [
    path('chat/', include('chat.urls', namespace='chat')),
    path('admin/', admin.site.urls),
]