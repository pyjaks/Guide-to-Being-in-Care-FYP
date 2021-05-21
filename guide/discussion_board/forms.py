from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Post, Comment, Reply


class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']


class NewCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class NewReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        labels = {
            'content': _('reply_content'),
        }

