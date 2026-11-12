from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
from .models import Post,Tags
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .forms import CommentForm




def home(request):
    all_posts = Post.objects.all().order_by('-id')
    paginator = Paginator(all_posts,2,allow_empty_first_page=True)
    page_number = request.GET.get('p',1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/index.html', {'posts': page_obj})

def post(request,id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            posturl = reverse('post',args=[id])
            return HttpResponseRedirect(posturl)
    
    form = CommentForm()
    return render(request, 'posts/post.html', {'post_dict': post, 'form': form,'comment':post.comment_set.all()})


def Tag(request,id):
    tag = Tags.objects.get(id=id)
    return render(request, 'posts/tags.html',{'tags' : tag.post_set.all()})
    
def search(request):
    query = request.GET.get('query', None)
    posts = Post.objects.filter(post_title=query)
    return render(request,'posts/search.html')
