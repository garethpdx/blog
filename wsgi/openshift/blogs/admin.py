from django.contrib import admin
from blogs.models import Post
from blogs.models import Comment

admin.site.register(Post)
admin.site.register(Comment)