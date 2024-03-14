from rest_framework import serializers
from .models import bus_details

class busdetailsser(serializers.ModelSerializer):
    class Meta:
        model = bus_details
        fields = "__all__"