from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicationViewSet

# The router automatically creates URLs like /api/medications/
router = DefaultRouter()
router.register(r'medications', MedicationViewSet, basename='medication')

urlpatterns = [
    path('', include(router.urls)),
]