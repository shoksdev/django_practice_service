from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class FIOValidator(validators.RegexValidator):
    regex = r"[а-яёА-ЯЁ\-]+\s+[а-яёА-ЯЁ\-]+(?:\s+[а-яёА-ЯЁ\-]+)?"
    message = _(
        "Enter a valid Name Patronymic. This value may contain only letters, hyphen and spaces."
    )
    flags = 0
