from rest_framework import serializers
from todoapp.models import ToDoList




class ToDoListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    #이메일을 받아오기위한 변수작업

    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = ToDoList
        fields='__all__'



class ToDoListCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    #이메일을 받아오기위한 변수작업

    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = ToDoList
        fields=("title","is_complete","user")