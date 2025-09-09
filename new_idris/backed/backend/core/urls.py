from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# import your app viewsets (create these files as below)
from app.api_views import ProductViewSet, CategoryViewSet, CartAPIView, PlaceOrderAPIView, OrderViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT auth
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API
    path('api/', include(router.urls)),
    path('api/cart/', CartAPIView.as_view(), name='api-cart'),
    path('api/checkout/', PlaceOrderAPIView.as_view(), name='api-checkout'),

    # keep existing dashboard pages (if present)
    path('dashboard/', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
