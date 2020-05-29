from django.urls import path
from . import views
from .views import (
    home,
    post_new
    )

urlpatterns = [
    path('', views.home, name='landing-home'),
    path('landing/submit/', views.post_new, name='post_new')
]
