from django.shortcuts import render
from blogs.models import Blog
from assignment.models import About

def home(request):
    featured_Post = Blog.objects.filter(status='published',is_featured=True).order_by('updated_at')
    latest_Posts = Blog.objects.filter(status='published', is_featured=False).order_by('updated_at')

    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        'featured_Post': featured_Post,
        'latest_Posts': latest_Posts,
        'about': about,
    }
    return render(request, 'home.html', context)
