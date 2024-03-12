"""Users views"""

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from cride.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
    AccountVerificationSerializer,
)
from rest_framework import status, viewsets
from rest_framework.decorators import action

# Django
from cride.users.models import User


class UserViewSet(viewsets.ModelViewSet):
    """User view set."""

    queryset = User.objects.filter(is_active=True, is_client=True)
    serializer_class = UserModelSerializer
    lookup_field = "username"

    # def get_permissions(self):
    #     """Assign permissions based on action."""
    #     if self.action in ["signup", "login", "verify"]:
    #         permissions = [AllowAny]
    #     elif self.action in ["retrieve", "update", "partial_update"]:
    #         permissions = [IsAuthenticated, IsAccountOwner]
    #     else:
    #         permissions = [IsAuthenticated]
    #     return [p() for p in permissions]

    @action(detail=False, methods=["post"])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {"user": UserModelSerializer(user).data, "access_token": token}
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def verify(self, request):
        """Account verification."""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {"message": "Congratulation, now go share some rides!"}
        return Response(data, status=status.HTTP_200_OK)


# class UserLoginAPIView(APIView):
#     """User login API view."""

#     def post(self, request, *args, **kwargs):
#         """Handle HTTP POST request."""
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user, token = serializer.save()
#         data = {"user": UserModelSerializer(user).data, "access_token": token}
#         return Response(data, status=status.HTTP_201_CREATED)


# class UserSignUpAPIView(APIView):
#     """User signup API view."""

#     def post(self, request, *args, **kwargs):
#         """Handle HTTP POST request."""
#         serializer = UserSignUpSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         data = UserModelSerializer(user).data
#         return Response(data, status=status.HTTP_201_CREATED)


# class AccountVerificationAPIView(APIView):
#     """User signup API view."""

#     def post(self, request, *args, **kwargs):
#         """Handle HTTP POST request."""
#         serializer = AccountVerificationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = {"message": "Congratulation, now go share some rides!"}
#         return Response(data, status=status.HTTP_200_OK)
