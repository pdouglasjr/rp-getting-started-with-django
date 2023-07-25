from django.shortcuts import render

from .models import Comment, Post

# Create your views here.
def blog_index(request):
    # Grab all posts from DB
    posts = Post.objects.all()

    # Create data context to send back to requestor
    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog_index.html', context)

def blog_category(request, category):
    # Grab all posts in the category from the DB
    posts = Post.object.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )

    # Create data context to send back to requesetor
    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, 'blog/blog_category.html', context)

def blog_detail(request, pk):
    # Grab the requested post from the DB
    post = Post.object.get(pk=pk)
    
    # Grab the comments for the post
    comments = Comment.objects.filter(post=post)

    # Create data context to send back to requestor
    context = {
        "post": post,
        "comment": comments,
    }

    return render(request, 'blog_detail.html', context)