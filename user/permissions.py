from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff