from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from cride.utils.models import CRideModel

class User(CRideModel, AbstractUser):
    """
        Extiende de AbstractUser para personalizar
        el modelo de User por defecto
    """
    
    email = models.EmailField(
        "email_address",
        unique=True,
        error_messages={
            "unique": "A user with that email already exists."
        }
    )
    
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the formt: +9999999999.Up to 15 digits allowed."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True
    )
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    
    is_client = models.BooleanField(
        'client_status',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.' 'Clients are the main type of users.'
        )
    )
    
    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text="Set to true when the user have verified its email address."
    )
    
    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username