from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
import uuid

class User(AbstractUser):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

        class JSONAPIMeta:
            resource_name = "users"
