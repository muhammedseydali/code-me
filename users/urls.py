from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# urlpatterns = [
#     path('', UserListCreateView.as_view(), name='user-list-create'),
#     path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
#     path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
#     path('roles/<int:pk>/', RoleDetailView.as_view(), name='role-detail'),
#     path('permissions/', PermissionListCreateView.as_view(), name='permission-list-create'),
#     path('permissions/<int:pk>/', PermissionDetailView.as_view(), name='permission-detail'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

from django.urls import path
from .views import UserListCreateAPIView, UserDetailAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
