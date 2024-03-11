""" Circle model """

from django.db import models

from cride.utils.models import CRideModel


class Circle(CRideModel):
    """Schema.

    A circle is a private group where rides are offered and taken
    by its members. To join a circle a user must receive an unique
    invitation code from an existing circle member.
    """

    name = models.CharField("circle name", max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField("circle description", max_length=256)
    picture = models.ImageField(upload_to="circles/picture", blank=True, null=True)

    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        "verified circle",
        default=False,
        help_text="Verified circles are also know as official communities.",
    )
    is_public = models.BooleanField(
        default=True,
        help_text="Public circles are listed in the main page so everyone know about their existence.",
    )

    is_limited = models.BooleanField(
        "limited",
        default=False,
        help_text="Limited circles can grow up to a fixed number of members.",
    )

    members_limit = models.PositiveIntegerField(
        default=0,
        help_text="If circle is limited, this will be the limit on the number of members."
    )
    
    def __str__(self):
        """ Return circle name"""
        return self.name;

    class Meta(CRideModel.Meta):
        
        ordering = ['-rides_taken', '-rides_offered']