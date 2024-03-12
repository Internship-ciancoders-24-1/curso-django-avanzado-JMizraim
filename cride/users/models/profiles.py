""" Profile model """

# Django
from django.db import models

# Utilities
from cride.utils.models import CRideModel

class Profile (CRideModel):
    """ Schema """ 
    user = models.OneToOneField("users.User", on_delete=models.CASCADE) # Elimina en cascada
    picture = models.ImageField(
        "profile picture",
        upload_to="users/pictures/",
        blank=True, #no requerido
        null=True #null
    )
    biography = models.TextField(max_length=500, blank=True)
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="User's reputation based on the rides taken and offered"
    )
    
    def __str__(self):
        """Return user's str representation"""
        return str(self.user)