from django.urls import path , include
from django.contrib import admin
from chat import views
from django.conf import settings
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('chat/', include('chat.urls', namespace='chat')),
    path('admin/', admin.site.urls),
    path('login/',LoginView.as_view(),name="login_url"),
    path('logout/',LogoutView.as_view(next_page='login_url'),name="logout"),
	path('register/',views.registerView,name="register_url"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
