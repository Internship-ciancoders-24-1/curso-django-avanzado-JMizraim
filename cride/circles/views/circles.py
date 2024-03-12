"""Circles views."""

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Models
from cride.circles.models import Circle
from cride.circles.models import Membership

# Permissions
from cride.circles.permissions import IsCircleAdmin

# Serializers
from cride.circles.serializers import CircleModelSerializer


class CircleViewSet(viewsets.ModelViewSet):
    """Circle view set."""

    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer
    # permission_classes = (IsAuthenticated,)
    lookup_field = "slug_name"

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Circle.objects.all()
        if self.action == "list":
            return queryset.filter(is_public=True)
        return queryset

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        if self.action in ["update", "partial_update"]:
            permissions.append(IsCircleAdmin)
        return [p() for p in permissions]

    def perform_create(self, serializer):
        """Assign circle admin."""
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        membership = Membership(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitations=10,
        )
        membership.save()
        return circle
