from django.contrib import admin
from django.urls import path, include
import app
import app.urls
from django.conf.urls.static import static
from django.conf import settings
import dashboard
import dashboard.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include(dashboard.urls)),
    path('', include(app.urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
