from rest_framework import serializers
from leads.models import Lead

# Lead Serializer
class LeadSerializer(serialiers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
