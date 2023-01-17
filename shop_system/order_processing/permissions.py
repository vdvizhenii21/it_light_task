from rest_framework.permissions import BasePermission


class IsAccountant(BasePermission):
    allowed_user_roles = ('accountant', )

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role in self.allowed_user_roles:
                return True
        return False