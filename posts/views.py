from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
from .models import Post
from django.shortcuts import get_object_or_404




def home(request):
    all_posts = Post.objects.all()

    return render(request, 'posts/index.html', {'posts': all_posts})

def post(request,id):
    post = get_object_or_404(Post, id = id)
    return render(request, 'posts/post.html', {'post_dict': post})
    





