from rest_framework import permissions


class AnonPermissionOnly(permissions.BasePermission):
    message = "You are already authenticated"
    """
    Non-authenticated users only
    """

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only owner of an object to edit it.
    Assumes the model instance has an owner attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user