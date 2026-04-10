from django.urls import path, include

urlpatterns = [
    path('', include('directive.urls')),
]