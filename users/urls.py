from django.urls import path, include
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path("signup/", views.UserView.as_view(), name="user_view"),
    path('<int:user_id>/', views.UserDetailView.as_view(), name='user_detail_view'),
    # path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path(
        "api/token/",
        views.CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
