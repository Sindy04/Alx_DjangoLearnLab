
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

from django.db.models import Q

def search(request):
  query = request.GET.get('query','')
  posts = Post.objects.filter(
    Q(title__icontains=query)  |
    Q(tags__name__icontains=query) |
    Q(content__icontains=query)
    
  )
  return render(request, 'search_result.html', {'posts': posts})

#CRUD operation

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import CommentForm

class CommentCreateView(CreateView):
model = comment
form_class = CommentForm
template_name = 'comment_form.html'

def form_valid(self, form):
  form.instance.post_id=self.kwargs['pk']
  return super().form_valid(form)

def get_success_url(self):
  return reverse('post_detail',kwargs={'pk':self.kwargs['pk']})
  
class CommentUpdateView(UpdateView):
model = comment
form_class = CommentForm
template_name = 'comment_form.html'

def get_success_url(self):
  return reverse('post_detail',kwargs={'pk': views.py})

class CommentDeleteView(DeleteView):
  model = Comment
  template_name = 'comment_confirm_delete.html'

def get_success_url(self):
  return reverse('post-detail',kwargs={'pk':(views.py)})

POST", method, save()
