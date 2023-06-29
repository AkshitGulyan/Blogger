from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from . import templates
from django.contrib.auth.models import User

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class postdetailsview(DetailView):
    model=Post
    template_name = 'postdetails.html'

class addpostview(CreateView):
    model=Post
    template_name = 'addpost.html'
    fields = '__all__'

def form_submit(request):
    if request.method == 'POST':
        title_val = request.POST.get('title')
        user_val = request.POST.get('username')
        email_val = request.POST.get('email')
        password_val = request.POST.get('password')
        firstname_val = request.POST.get('first_name')
        lastname_val = request.POST.get('last_name')
        body_val = request.POST.get('body')
        user = User.objects.create_user(username=user_val, email=email_val, password=password_val, first_name=firstname_val, last_name=lastname_val)
        Post.objects.create(title=title_val, author=user, body=body_val)
        
        # Redirect to a success page or another URL
        return redirect('home')

    return render(request, 'templates/addpost.html')