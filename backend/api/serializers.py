from rest_framework import serializers 
from .models import *


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("name", "start_date", "end_date", "comments", "status")


