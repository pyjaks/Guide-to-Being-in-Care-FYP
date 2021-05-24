from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm, modelformset_factory

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.add_input(Submit('submit', 'Submit'))


class NewReplyForm(ModelForm):
    helper = FormHelper()

    class Meta:
        model = Reply
        fields = ['content']
        labels = {
            'content': _('reply_content'),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.add_input(Submit('submit', 'Submit'))


NewReplyFormSet = modelformset_factory(Reply, fields=('content',))

