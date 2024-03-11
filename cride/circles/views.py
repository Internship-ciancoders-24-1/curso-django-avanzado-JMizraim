"""Circles views"""

# Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse, HttpResponse

from cride.circles.models import Circle
from cride.circles.serializers import CircleSerializer, CreateCircleSerializer


@api_view(["GET"])
def list_circles(request):
    circles = Circle.objects.filter(is_public=True)

    # Serializer de muchos registros
    serializer = CircleSerializer(circles, many=True)

    return Response(serializer.data)


@api_view(["POST"])
def create_circle(request):
    """Create circle"""

    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    circle = serializer.save()

    return Response(CircleSerializer(circle).data)
