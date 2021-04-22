from django.contrib import admin
from discussion_board.models import Category, Author, Post
# Register your models here.

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)
