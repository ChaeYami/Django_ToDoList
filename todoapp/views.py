from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from todoapp.models import ToDoList
from todoapp.serializers import ToDoListSerializer,ToDoListCreateSerializer
import datetime



# Create your views here.
class ToDoView(APIView): # /todo/
    # 글 목록
    def get(self, request):
        todolists = ToDoList.objects.all()
        serializer = ToDoListSerializer(todolists, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)
            
    # 글 작성
    def post(self, request):
        serializer = ToDoListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class ToDoDetailView(APIView): # /todo/id/
    # 글 상세
    def get(self, request,todo_id):
        todolists = get_object_or_404(ToDoList,id=todo_id)
        if request.user == todolists.user:
            serializer = ToDoListSerializer(todolists)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("권한이 없습니다.",status=status.HTTP_400_BAD_REQUEST)
            
    # 글 수정
    def put(self, request,todo_id):
        todolists = get_object_or_404(ToDoList,id=todo_id) # db 불러오기
        if request.user == todolists.user: # 
            serializer = ToDoListCreateSerializer(todolists, data=request.data)
            if serializer.is_valid():
                is_complete = serializer.validated_data.get('is_complete')
                if is_complete:
                    todolists.completed_at = datetime.datetime.now()
                serializer.save(user=request.user)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.",status=status.HTTP_400_BAD_REQUEST)
        
    # 글 삭제
    def delete(self, request,todo_id):
        todolists = ToDoList.objects.get(id=todo_id)
        if request.user == todolists.user:
            todolists.delete()
            return Response("ToDo list 삭제완료!",status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다",status=status.HTTP_403)