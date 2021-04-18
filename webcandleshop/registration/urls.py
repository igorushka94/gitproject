from django.urls import path
from .views import index, signup

urlpatterns = [
	path('', signup),
]