from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, OrderViewSet
from .views.flash_sale import FlashSaleViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'flash-sales', FlashSaleViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]
