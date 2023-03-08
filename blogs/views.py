from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from .models import Post

# Create your views here.
def list(request):
    if 's' in request.GET and request.GET['s']:
        text = request.GET.get('s')
        if text != '':
            Data = {'Posts': Post.objects.filter(Q(title__icontains = text)) }
    else:
        Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blogs/list-post.html', Data)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Bài viết không tồn tại")
    
    return render(request, 'blogs/post.html', {'post': post})
