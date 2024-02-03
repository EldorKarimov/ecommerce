from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    first_name = models.CharField(_('first name'), max_length = 50)
    last_name = models.CharField(_('last name'), max_length = 50)
    email = models.EmailField(_('Email address'), unique = True)
    phone_number = models.CharField(_('Phone number'), max_length = 20, blank = True)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]