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
    def update(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)  # 비밀번호 해싱
        user.save()  # DB에 저장
        return user


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
