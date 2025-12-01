from back_api.models import AgentType, OSINTQuery
from rest_framework import serializers
from user_model.models import CustomUserClass


class AgentTypeSerializer(serializers.Serializer):
    vendor_name = serializers.CharField(max_length=30)
    vendor_description = serializers.CharField(max_length=200)
    vendor_api = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return AgentType(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("vendor_name", instance.name)
        instance.description = validated_data.get(
            "vendor_description", instance.description
        )
        instance.api = validated_data.get("vendor_api", instance.api)
        return instance


class OSINTQuerySerializer(serializers.Serializer):
    osint_agent = serializers.DjangoModelField(AgentType)
    osint_result = serializers.DictField()
    created_by = serializers.DjangoModelField(CustomUserClass)
    created_date = serializers.DateTimeField()
    updated_date = serializers.DateTimeField()

    def create(self, validated_data):
        return OSINTQuery(**validated_data)

    def update(self, instance, validated_data):
        instance.agent = validated_data.get("osint_agent", instance.agent)
        instance.result = validated_data.get("osint_result", instance.result)
        instance.created_by = validated_data.get("created_by", instance.created_by)
        instance.created_date = validated_data.get(
            "created_date", instance.created_date
        )
        instance.updated_date = validated_data.get(
            "updated_date", instance.updated_date
        )
        return instance
