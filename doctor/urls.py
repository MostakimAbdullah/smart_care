from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('list', views.DoctorView)
router.register('designation', views.DesignationView)
router.register('specialization', views.SpecializationView)
router.register('availabletime', views.AvailabletimeView)
router.register('reviews', views.ReviewView)


urlpatterns = [
    path('', include(router.urls)),
]
