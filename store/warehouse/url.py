from django.urls.conf import path
from . import views


urlpatterns = [
    path('product/', views.product_list),
]