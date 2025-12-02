from back_api.models import AgentType, OSINTQuery
from rest_framework import serializers


class AgentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentType
        fields = ["vendor_name", "vendor_description", "vendor_api"]


class OSINTQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = OSINTQuery
        fields = [
            "id",
            "osint_agent",
            "osint_result",
            "created_by",
            "created_date",
            "updated_date",
        ]
