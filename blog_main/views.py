from django.shortcuts import render
from blogs.models import Category,Blog

def home(request):
    categories = Category.objects.all()
    featured_Post = Blog.objects.filter(status='published',is_featured=True).order_by('updated_at')
    latest_Posts = Blog.objects.filter(status='published', is_featured=False).order_by('updated_at')
    context = {
        'categories': categories,
        'featured_Post': featured_Post,
        'latest_Posts': latest_Posts
    }
    return render(request, 'home.html',context)
