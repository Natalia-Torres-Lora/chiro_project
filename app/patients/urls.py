from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')

# Include the router URLs
urlpatterns = [
    path('', include(router.urls)),
]
