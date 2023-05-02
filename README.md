# Django_ToDoList

📚 tacks
------
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/react-61DAFB?style=for-the-badge&logo=react&logoColor=black"> 

***

💖 Todo List를 DRF로 만들어보기 : 장고 심화 개인과제
------
> 2023.04.24 ~ 2023.04.30  
  
Django DRF 를 사용해 ToDoList 프로젝트 만들기!


🤔 기능
------
### 회원기능

1. 회원가입 `POST`
    - id : 데이터 고유 id(PK)
    - email : 아이디로 사용, `UNIQUE`
    - password : 비밀번호, 회원 가입이나 회원 수정 시에 해시
    - name : 이름
    - gender : 성별
    - age : 나이
    - introduction : 자기소개
2. 로그인
3. 회원 정보 수정 `PATCH`
4. 회원 탈퇴 `DELETE`

### TODO LIST

1. 게시글 CREATE - ToDo List 생성 `POST`
    - 로그인한 사용자만 가능
    - 테이블 필드
      - id : 데이터 고유 id
      - title : 제목
      - is_complete : 완료여부, `boolean`, `default = false`
      - created_at : 글 생성 시각
      - updated_at : 글 수정 시각, `default=None`
      - completion_at : 완료 시각, `default=None`, - 처음 is_complete필드가 `True`로 수정되었을 때만 시각 업데이트
      - user_id : User과 FK

2. 게시글 READ `GET`
    - 목록
        - ToDo List 목록
    - 상세페이지
        - 해당 ToDolist의 상세 페이지, **로그인된 사용자이면서 글 작성자일 때만 가능**
        
4. 게시글 UPDATE `PUT`
    - **로그인한 사용자이면서 글 작성자일 때만 가능**
    - 완료된 todo로 수정하면 completed_at 필드 업데이트 (이미 완료된 todo를 수정했을 때는 시간이 업데이트 되지 않음)

5. 게시글 DELETE `DELETE`
    - **로그인한 사용자이면서 글 작성자일 때만 가능**

### 추가 요구사항

1. 권한
    - 회원정보 수정/삭제 , 할일 조회/수정/삭제 시에 작성자 본인만 가능하도록
2. JWT 기반 인증
    - 토큰방식, `djangorestframework_simplejwt` 라이브러리 사용
3. 프론트구현
    - 회원가입, 로그인, 로그아웃 
    - 정보 수정(+ 권한)
***

ERD
------
![image](https://user-images.githubusercontent.com/120750451/235371006-0ea37f7f-cd8a-4375-a92b-73bef3d64e81.png)

