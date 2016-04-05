from django.db import models
from users.models import User
import uuid


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Comment(DateMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User)

    class JSONAPIMeta:
        resource_name = "comments"
