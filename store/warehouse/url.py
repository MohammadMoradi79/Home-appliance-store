from django.urls.conf import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from . import views

router = SimpleRouter()
router.register('category', views.CategoryViewSet, basename='category')
router.register('customer', views.CustomerViewSet, basename='customer')

nested_router_parent = routers.SimpleRouter()
nested_router_parent.register('product', views.ProductViewSet, basename='product')
nested_router = routers.NestedSimpleRouter(nested_router_parent, 'product', lookup='product')
nested_router.register('comment', views.CommentViewSet, basename='product-comment')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router_parent.urls)),
    path('', include(nested_router.urls)),
]
