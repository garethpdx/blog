from django.contrib import admin
from models import Post
from models import Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'hidden')

admin.site.register(Comment)
