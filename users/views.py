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


# ============================ 회원가입 클래스 (id,인증 불필요) ============================  
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

# ============================ 로그인 ============================  
class CustomTokenObtainPairView(TokenObtainPairView):  # TokenObtainPairView 상속
    serializer_class = CustomTokenObtainPairSerializer

# ============================ 회원정보, 수정, 탈퇴 클래스 (id,인증 필요) ============================  
class UserDetailView(APIView):
    # 로그인 되어 있는지
    permission_classes = [permissions.IsAuthenticated]
    
    # =================== 회원 상세정보 =================== 
    
    def get(self,request, user_id): # => request.method == 'GET':
        user = get_object_or_404(User,id=user_id) # user 정보 불러오기
        serializer = UserSerializer(user) # user 시리얼라이저 불러오기
        return Response(serializer.data, status=status.HTTP_200_OK)

    # =================== 회원 수정 =================== 
    
    def patch(self, request, user_id): # => request.method == 'PATCH':
        user = get_object_or_404(User, id=user_id) # user 정보 불러오기
        if request.user == user: # 요청한(로그인된) 사용자가 변경하려는 정보가 본인의 것이냐
            request.data.pop('email', None) # 이메일 필드를 수정할 수 없도록 처리
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():  # 유효성 검사를 통과했을 때
                serializer.save() # 수정
                return Response({"message": "수정 완료!"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "권한이 없습니다!"}, status=status.HTTP_403_FORBIDDEN)

    # =================== 회원 탈퇴 =================== 
    
    def delete(self, request, user_id): # => request.method == 'DELETE':
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            user.delete()
            return Response({"message":"삭제 완료!"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message":"권한이 없습니다!"}, status=status.HTTP_403_FORBIDDEN)

class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # 로그인여부확인

    def get(self, request):
        return Response("get 요청")