from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    # Optional: Implement pagination
    # pagination_class = StandardResultsSetPagination

# class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = [IsAuthenticated]

#     # Optional: Restrict permissions based on custom logic
#     def get_permissions(self):
#         if self.request.method in ['PUT', 'PATCH', 'DELETE']:
#             self.permission_classes = [IsAdminOrOwner] 
#         return super().get_permissions()
