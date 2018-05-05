from rest_framework import serializers
from .models import SavedEmployees


class EmployeeSerializer(serializers.ModelSerializer):
    fields = '__all__'

    class Meta:
        model = SavedEmployees
