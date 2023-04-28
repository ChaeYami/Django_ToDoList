from rest_framework.views import APIView
from rest_framework import status, permissions  # permission_classes 사용
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer
from rest_framework.generics import get_object_or_404  # 데이터 가져오기 + 없을 때 에러처리
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class UserView(APIView):
    # 회원가입
    def post(self, request):  # => request.method == 'POST':
        serializer = UserSerializer(data=request.data)  # 데이터 받아오기
        if serializer.is_valid():  # 유효성 검사 통과
            serializer.save()  # 받아온 데이터 db에 저장
            return Response(
                {"message": "가입완료!"}, status=status.HTTP_201_CREATED)  # 정상 생성 (등록) 상태
        else:  # 유효성 검사 만족 X -> 입력값에 문제
            return Response(
                {"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST
            )  # 에러를 반환, 잘못된 요청 상태

# 로그인
class CustomTokenObtainPairView(TokenObtainPairView):  # TokenObtainPairView 상속
    serializer_class = CustomTokenObtainPairSerializer


class UserDetailView(APIView):
    # 로그인 되어 있는지
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request, user_id):
        user = get_object_or_404(User,id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 회원 수정
    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        
        if request.user == user:
            serializer = UserSerializer(user, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"수정완료!"}, status=status.HTTP_200_OK)
            else:
                return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"권한이 없습니다!"}, status=status.HTTP_403_FORBIDDEN)

    # 회원 삭제
    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            user.delete()
            return Response({"message":"삭제 완료!"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)


class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated] # 로그인한 유저만 로그아웃

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist() # refresh_token을 블랙리스트에 추가
            return Response({"message": "로그아웃 되었습니다."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
