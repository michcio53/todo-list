from rest_framework.permissions import BasePermission, SAFE_METHODS
from .literals import ERROR_YOU_MUST_BE_OWNER


class IsOwnerOrRead(BasePermission):
    message = ERROR_YOU_MUST_BE_OWNER
    safe_methods = ['GET', 'PUT']

    def has_permission(self, request, view):
        if request.method in self.safe_methods:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
