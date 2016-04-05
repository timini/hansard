from django.contrib import admin
from chat.models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'created_at', 'updated_at')

admin.site.register(Comment, CommentAdmin)
