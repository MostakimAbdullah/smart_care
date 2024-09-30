from rest_framework import serializers
from doctor.models import Doctor,Specialization,Designation,Availabletime,Review


class DoctorSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    # designation = serializers.StringRelatedField(many=True)
    # specialization = serializers.StringRelatedField(many=True)
    # available_time = serializers.StringRelatedField(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'


class AvailabletimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availabletime
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    # reviewer = serializers.StringRelatedField(many=False)
    # doctor = serializers.StringRelatedField(many=False)
    class Meta:
        model = Review
        fields = '__all__'