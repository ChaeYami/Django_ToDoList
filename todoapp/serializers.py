from rest_framework import serializers
from todoapp.models import ToDoList

class ToDoListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = ToDoList
        fields='__all__'
        
    def get_user(self, obj):
        return obj.user.email




class ToDoListCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = ToDoList
        fields=("title","is_complete","user")
        
    def get_user(self, obj):
        return obj.user.email