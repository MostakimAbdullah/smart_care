from django.shortcuts import render
from rest_framework import viewsets,pagination
from doctor.serializers import DoctorSerializer,AvailabletimeSerializer,DesignationSerializer,SpecializationSerializer,ReviewSerializer
# Create your views here.
from doctor.models import Doctor,Designation,Specialization,Availabletime,Review
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100

class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    pagination_class = DoctorPagination
    serializer_class = DoctorSerializer

class SpecializationView(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class DesignationView(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class AvailabletimeView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Availabletime.objects.all()
    serializer_class = AvailabletimeSerializer

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


