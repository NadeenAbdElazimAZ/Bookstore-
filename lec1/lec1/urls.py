
from django.contrib import admin
from django.urls import path
from bookstore.views import welcome
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from users.views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', welcome, name='welcome home'),
    path('bookstore/', include('bookstore.urls')),
    path('users/', include('users.urls')),
    path('accounts/profile/',profile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 