from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, AttendeeViewSet, SessionViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'attendees', AttendeeViewSet)
router.register(r'sessions', SessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
