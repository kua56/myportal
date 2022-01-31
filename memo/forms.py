from xml.etree.ElementTree import Comment
from django import forms

from memo.models import Memo

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ('title', 'desc')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        field = ('text', )