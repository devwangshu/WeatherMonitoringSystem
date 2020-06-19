from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin

from theme import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    path('accounts/', include('accounts.urls')),
    path('snippets/', include('snippets.urls')),
    path('wm_test/', include('wm_test.urls', namespace='weather_monitoring')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)