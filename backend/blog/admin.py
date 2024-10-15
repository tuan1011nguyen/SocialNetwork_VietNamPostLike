from django.contrib import admin
from .models import Post, Like, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','image', 'date_post', 'no_of_likes')  # Update 'like' to 'no_of_likes'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','content_cmt','date_cmt')
admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Comment,CommentAdmin)
