from rest_framework.permissions import BasePermission
from cride.circles.models import Membership


class IsCircleAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        """Verify if a user is an admin in the circle."""
        try:
            membership = Membership.objects.get(
                user=request.user, circle=obj, is_admin=True, is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True
