from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.index, name='index.html'),
    # Add other URL patterns here
]
