from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from publications.models import Comment, Publication


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class PublicationCreateForm(ModelForm):
    class Meta:
        model = Publication
        widgets = {
            'text': SummernoteWidget(),
        }
        fields = ('title', 'text',)
