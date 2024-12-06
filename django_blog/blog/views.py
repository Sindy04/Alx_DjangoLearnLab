
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreativeView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequireMixin, UserPassesTestMaxin
from .models import Post

class PostListView(ListView):
  model = Post
  template_name = 'post_list.html'

class PostDetailView
   model = Post
   template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'content']
  template_name = 'post_form.html'

def form_valid(self, form):
  form.instance.author = self.request.user
  return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['title','content']
  template_name = 'post_form.html'

def test_func(self):
  post = self.get_object()
  return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
  model = Post
  template_name ='post_confirm_delete.html'
  success_url = '/posts/'
  def test_func(self):
    post = self.get_object()
    return self.request.user == post.author




