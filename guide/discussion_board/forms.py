from django.forms import ModelForm
from .models import Post, Comment


class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']


class NewCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

