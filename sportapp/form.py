from django.forms import ModelForm
from .models import Comment
from .models import Registration
from django import forms
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class AddRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Registration
        fields = '__all__'
