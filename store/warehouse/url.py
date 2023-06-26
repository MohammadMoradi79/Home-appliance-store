from django.urls.conf import path
from . import views


urlpatterns = [
    path('hello/', views.hello_world),
]