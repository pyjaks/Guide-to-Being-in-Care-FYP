from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _

from .models import Post, Comment, Reply


class NewPostForm(ModelForm):
    helper = FormHelper()

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


class NewCommentForm(ModelForm):
    helper = FormHelper()

    class Meta:
        model = Comment
        fields = ['content']


class NewReplyForm(ModelForm):
    helper = FormHelper()

    class Meta:
        model = Reply
        fields = ['content']
        labels = {
            'content': _('reply_content'),
        }

