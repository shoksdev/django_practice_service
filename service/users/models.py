from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import FIOValidator


class CustomUser(AbstractUser):
    full_name_validator = FIOValidator()
    full_name = models.CharField(max_length=255, verbose_name='ФИО', validators=[full_name_validator],
                                 help_text=_('Required. 255 characters or fewer. Letters, hyphens and spaces'))
    email = models.EmailField(_("email address"))

    def __str__(self):
        return self.username
