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