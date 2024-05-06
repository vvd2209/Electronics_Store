from rest_framework.routers import DefaultRouter

from electronics_store.apps import ElectronicsStoreConfig
from electronics_store.views import SupplierViewSet, ProductViewSet, ContactViewSet

app_name = ElectronicsStoreConfig.name

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'contact', ContactViewSet, basename='contact')

urlpatterns = router.urls
