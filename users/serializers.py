from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    # 회원가입
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)  # 비밀번호 해싱
        user.save()  # DB에 저장
        return user

    # 회원 정보 수정
    def update(self, instance, validated_data):
        email = serializers.EmailField(read_only=True)
        user = super().update(instance, validated_data)
        password = validated_data.get('password')
        if password:
            user.set_password(password) # 비밀번호 해싱
            user.save()  # DB에 저장
        return user
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.gender = validated_data.get('gender', instance.gender)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.introduction = validated_data.get('introduction', instance.introduction)
        
    #     password = validated_data.get('password', None)
    #     if password:
    #         instance.set_password(password)  # 새로운 비밀번호 설정
        
    #     instance.save()  # DB에 저장
    #     return instance

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 만든 User 모델에 맞게
        token["email"] = user.email  
        token["name"] = user.name
        token["gender"] = user.gender
        token["age"] = user.age
        token["introduction"] = user.introduction

        return token
