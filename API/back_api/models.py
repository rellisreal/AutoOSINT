import uuid

from django.db import models
from user_model.models import CustomUserClass


class AgentType(models.Model):
    vendor_name = models.CharField(max_length=30)
    vendor_description = models.CharField(max_length=200)
    vendor_api = models.CharField(max_length=100)

    def __str__(self):
        return self.vendor_name


class OSINTQuery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    osint_agent = models.ForeignKey(AgentType, on_delete=models.DO_NOTHING)
    osint_result = models.TextField()
    created_by = models.ForeignKey(CustomUserClass, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_created=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Create your models here.
