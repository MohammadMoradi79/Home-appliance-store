from django.urls.conf import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('category', views.CategoryViewSet, basename='category')
router.register('product', views.ProductViewSet, basename='product')
urlpatterns = [
    path('', include(router.urls))
]