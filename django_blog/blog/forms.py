from django import forms
from taggit.forms import TagWidget
from .models import Post

class PostForm(forms.ModelForm):
  tags = forms.CharField(required=False, widget=TagWidget)

class Meta:
  model = Post
  fields = ['title', 'content']
  widgets ={
    'tags': TagWidget(),
  }

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('content',)
    labels={
    'content': 'Commment',
    }
    widgets = {
    'content':forms.Textarea(attars={'class':'form-control','rows':4,'cols':50}),
    }
