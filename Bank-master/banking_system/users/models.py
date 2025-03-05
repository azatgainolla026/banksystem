from decimal import Decimal
from django.db import models, transaction
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import F

class UserAccount(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

