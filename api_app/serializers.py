from rest_framework import serializers

from .models import Task#making serializers of this model


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ('id','title','completed',)#all this form is shown in task-detail
    