from django.shortcuts import render
from blog.models import Post
# Create your views here.

def home(request):
    return render(request, "home.html")

from django.views.generic import ListView, DetailView

class PostsListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post