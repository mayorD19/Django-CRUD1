from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostCreateView(CreateView):
    model = Post

    fields = "__all__" , 
    success_url = reverse_lazy('blog:all')
    template_name = "post_form.html"


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class  PostUpdateView(UpdateView):
    model = Post

    fields = "__all__",
    success_url  = reverse_lazy('blog:all')

class PostDeleteView(DeleteView):
    model = Post

    fields = "__all__",
    success_url = reverse_lazy('blog:all')

    template_name = 'post_confirm_delete.html'
