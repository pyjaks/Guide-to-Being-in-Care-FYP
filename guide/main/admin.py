from django.contrib import admin
from discussion_board.models import Category, Author, Post, Comment, Reply
# Register your models here.

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
