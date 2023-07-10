from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import HttpResponse

def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'posts/post_list.html', {'posts': post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return HttpResponse(post)