from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

# class PermissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Permission
#         fields = ['id', 'name']

# class RoleSerializer(serializers.ModelSerializer):
#     permissions = PermissionSerializer(many=True)

#     class Meta:
#         model = Role
#         fields = ['id', 'name', 'permissions']

# class UserSerializer(serializers.ModelSerializer):
#     role = RoleSerializer()
#     additional_permissions = PermissionSerializer(many=True)

#     class Meta:
#         model = get_user_model()
#         fields = ['id', 'username', 'email', 'role', 'additional_permissions']

User = get_user_model()

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
    user_permissions = serializers.PrimaryKeyRelatedField(many=True, queryset=Permission.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'password', 'groups', 'user_permissions']
        extra_kwargs = {
            'password': {'write_only': True},
            'user_permissions': {'required': False}
        }

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        user_permissions_data = validated_data.pop('user_permissions', [])
        
        user = User.objects.create_user(**validated_data, is_staff=True)  
        
        for group in groups_data:
            user.groups.add(group)
        
        for perm in user_permissions_data:
            user.user_permissions.add(perm)
        
        return user

    def update(self, instance, validated_data):
        groups_data = validated_data.pop('groups', [])
        user_permissions_data = validated_data.pop('user_permissions', [])

        instance = super().update(instance, validated_data)
        
        instance.groups.set(groups_data)
        instance.user_permissions.set(user_permissions_data)

        return instance