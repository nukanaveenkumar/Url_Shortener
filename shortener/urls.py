
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page for URL shortening
    path('<str:short_url>/', views.redirect_to_original, name='redirect_to_original'),  # Redirect for shortened URL
]

