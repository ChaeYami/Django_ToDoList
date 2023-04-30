from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from todoapp.models import ToDoList
from todoapp.serializers import ToDoListSerializer,ToDoListCreateSerializer
import datetime


# ============================ 글 목록, 작성 클래스 (id 불필요) ============================  

class ToDoView(APIView): # /todo/
    
    # =================== 글 목록 =================== 
    
    def get(self, request): # => request.method == 'GET':
        todolists = ToDoList.objects.all()
        serializer = ToDoListSerializer(todolists, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)
            
    # =================== 글 작성 =================== 
    
    def post(self, request): # => request.method == 'POST':
        serializer = ToDoListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
# ============================ 글 상세, 수정 클래스 (id 필요) ============================ 
class ToDoDetailView(APIView): # /todo/id/
    
    # =================== 글 상세 =================== 
    
    def get(self, request,todo_id): # => request.method == 'GET':
        todolists = get_object_or_404(ToDoList,id=todo_id)
        # 로그인된 사용자의 글일때만
        if request.user == todolists.user:
            serializer = ToDoListSerializer(todolists)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("권한이 없습니다.",status=status.HTTP_400_BAD_REQUEST)
            
    # =================== 글 수정 =================== 
    
    def put(self, request,todo_id): # => request.method == 'PUT':
        todolists = get_object_or_404(ToDoList,id=todo_id) # db 불러오기
        # 로그인된 사용자의 글일때만
        if request.user == todolists.user:
            serializer = ToDoListCreateSerializer(todolists, data=request.data) 
            # 유효성검사를 통과하면
            if serializer.is_valid(): 
                is_complete = serializer.validated_data.get('is_complete') # 완료여부 불러오기
                completed_at = todolists.completed_at # 완료시간 필드 가져오기
                todolists.updated_at = datetime.datetime.now() # 업데이트 시간 
                
                # is_complete == True 이고 completea_at 필드가 비어있다면 --> 완료된 todo로 수정하면 (이미 완료된 todo를 수정했을 때는 시간이 업데이트 되지 않음)
                if is_complete and completed_at == None : 
                    todolists.completed_at = datetime.datetime.now() # 완료 시간 
                serializer.save(user=request.user) # db에 저장
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            
            else: # 유효성검사를 통과하지 못하면
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else: # 로그인된 사용자의 글이 아니라면 
            return Response("권한이 없습니다.",status=status.HTTP_400_BAD_REQUEST)
        
    # =================== 글 삭제 =================== 
    
    def delete(self, request,todo_id): # => request.method == 'DELETE':
        todolists = ToDoList.objects.get(id=todo_id) # db 불러오기
        if request.user == todolists.user: # 로그인된 사용자의 글일때만
            todolists.delete() # 삭제
            return Response("ToDo list 삭제완료!",status=status.HTTP_204_NO_CONTENT)
        else: # 로그인된 사용자의 글이 아니라면 
            return Response("권한이 없습니다",status=status.HTTP_403)