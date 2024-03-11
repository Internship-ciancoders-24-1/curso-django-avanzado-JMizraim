from rest_framework import serializers
from cride.circles.models import Circle
from rest_framework.validators import UniqueValidator


# Convierte los datos
class CircleSerializer(serializers.Serializer):
    """Circle serializer."""

    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_taken = serializers.IntegerField()
    rides_offered = serializers.IntegerField()


class CreateCircleSerializer(serializers.Serializer):
    """Create circle serializer."""

    name = serializers.CharField(max_length=140)
    slug_name = serializers.SlugField(
        max_length=40, validators=[UniqueValidator(queryset=Circle.objects.all())]
    )
    about = serializers.CharField(max_length=256, required=False)

    def create(self, data):
        return Circle.objects.create(**data)
