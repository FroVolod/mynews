from django.forms import ModelForm, CharField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from allauth.account.forms import SignupForm

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


class MyCustomSignupForm(SignupForm):
    first_name = CharField(max_length=30, label='First Name', required=False)
    last_name = CharField(max_length=30, label='Last Name', required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
