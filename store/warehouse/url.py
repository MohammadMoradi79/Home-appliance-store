from django.urls.conf import path
from . import views


urlpatterns = [
    path('category/', views.category_list),
]