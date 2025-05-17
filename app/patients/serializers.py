from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        
        user = self.context['request'].user
        return Patient.objects.create(user=user, **validated_data)
