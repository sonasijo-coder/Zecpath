from .models import Job , Application
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):

  posted_by = serializers.ReadOnlyField(source = 'posted_by.username')

  class Meta:
    model =Job
    fields = '__all__'
    read_only_fields = ['id' , 'created_at']