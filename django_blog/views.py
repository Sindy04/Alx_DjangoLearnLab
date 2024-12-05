from django.shortcuts import render, request
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import UserCreationForm
from django.contrib.auth.decorators import lgin_required

def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username, password=password)
    if user is not None:
      login(requst,user)
      return redirect('home)
      return render(request, 'login.html')

def logout_view(request):
  logout(request)
  return redirect('home')

def register_view(request):
  if request.method =='POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
    else:
      form = UserCreationForm()
      return render(request, 'register.html',{'form':form})

@login_required
def profile_view(request):
  return render(request,'profile.html')
