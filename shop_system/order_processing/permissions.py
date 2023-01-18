from rest_framework.permissions import BasePermission


class IsAccountantandCashier(BasePermission):
    allowed_user_roles = ('accountant', 'cashier', )

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role in self.allowed_user_roles:
                return True
        return False
