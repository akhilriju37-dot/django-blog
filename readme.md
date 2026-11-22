Username: djangoadmin
Password: 1234

# Django Blogging System

A simple blogging website built using Python and Django.

## 1. Display the Home Page

### Steps

1. Create a URL in `urls.py`.
2. Create a `home()` view function in `views.py`.
3. Create an HTML template for the home page.
4. Configure the templates directory in `settings.py`.

## 2. Adding Bootstrap and Static Files

### Steps

1. Visit the [Bootstrap website](https://getbootstrap.com/).
2. Select a suitable blog page design.
3. Download the HTML and CSS files or copy and paste the required code.
4. Create a `static` folder in your project.
5. Inside the static folder, create:
   - `css/` – For CSS files.
   - `images/` – For image files.
6. Load static files in your HTML template.

### Load Static Files in HTML

```django
{% load static %}
```

Add the CSS file:

```html
<link rel="stylesheet" href="{% static 'css/blog.css' %}">
```

### Configure Static Files in `settings.py`

```python
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

## 3. Git and GitHub Setup

### Step 1: Create a `.gitignore` File

1. Visit [gitignore.io](https://www.toptal.com/developers/gitignore).
2. Select Django.
3. Generate and save the file as `.gitignore` in your project root directory.

### Step 2: Initialize Git

```bash
git init
git add -A
git commit -m "Add Bootstrap blog homepage design"
```

### Step 3: Configure GitHub Repository

```bash
git branch -M main

git remote add origin https://github.com/akhilriju37-dot/django-blog.git

git push -u origin main
```

## 4. Create a Django App

### Step 1: Create the App

```bash
python manage.py startapp blogs
```

### Step 2: Register the App

Add `blogs` to `INSTALLED_APPS` in `settings.py`.

```python
INSTALLED_APPS = [
    # Existing Django apps
    'blogs',
]
```

### Step 3: Create Models

Create the required database models in:

```text
blogs/models.py
```

You can define models such as:

- Post
- Category
- Comment
## 5. Configure Media Files

Media files are user-uploaded files, such as blog featured images.

### Step 1: Configure Media Settings

Add the following settings in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Step 2: Configure Media URLs

In the project's main `urls.py`, import `static` and configure media file serving:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Existing URL patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Note:** This configuration is intended for development. Production media files should be served through a web server or cloud storage.

## 6. Create the Blog Model

Add the required blog fields in `blogs/models.py`.

### Blog Model Fields

| Field | Purpose |
|---|---|
| title | Blog post title |
| slug | SEO-friendly URL identifier |
| category | Blog category |
| featured_image | Blog featured image |
| short_description | Short summary of the blog |
| blog_body | Main blog content |
| status | Draft or Published |
| is_featured | Identifies featured blog posts |
| created_at | Blog creation date and time |
| updated_at | Last updated date and time |

### Step 1: Install Pillow

Pillow is required for handling image uploads.

```bash
pip install Pillow
```

### Step 2: Create and Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 7. Configure Django Admin for Blog

Register the Blog model in `blogs/admin.py`.

### Step 1: Create BlogAdmin Class

Create a custom admin class by inheriting from `admin.ModelAdmin`.

```python
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }

    list_display = (
        'title',
        'category',
        'status',
        'is_featured',
        'created_at',
    )

    search_fields = ('title', 'short_description')

    list_editable = ('status', 'is_featured',)
```

### Step 2: Register the Blog Model

```python
admin.site.register(Blog, BlogAdmin)
```

### Admin Features

- **prepopulated_fields:** Automatically generates the slug from the title while entering data in the admin panel.
- **list_display:** Displays selected fields in the admin list page.
- **search_fields:** Enables searching blog posts.
- **list_editable:** Allows editing selected fields directly from the list page.

## 8. Add Blog Status Choices

Create status choices to manage blog publishing.

| Status | Description |
|---|---|
| Draft | Blog is saved but not published. |
| Published | Blog is available to visitors. |

These choices help manage blog visibility.

## 9. Push Changes to GitHub

After completing the model and admin configuration, commit and push your changes.

```bash
git add -A
git commit -m "Add blog model, media configuration and admin features"
git push
```

## 10. Display Categories and Published Blogs on the Home Page

Fetch category information and published blog posts from the database and display them in `home.html`.

### Step 1: Update `views.py`

Pass the required data through the view context.

Example:

```python
context = {
    'categories': categories,
    'Published_Post': Published_Post,
}
```

Here:
- `categories` contains the available blog categories.
- `Published_Post` contains blog posts with Published status.

### Step 2: Display Categories in `home.html`

Use Django template loops to display categories dynamically.

```django
<ul class="list-group list-group-flush">
    {% for cat in categories %}
        <li class="list-group-item">
            {{ cat.category_name }}
        </li>
    {% empty %}
        <li class="list-group-item">
            No categories available.
        </li>
    {% endfor %}
</ul>
```

### Step 3: Display Published Blog Posts

Loop through the published blog posts and display them dynamically.

```django
{% for post in Published_Post %}

    <!-- Blog Card -->
    src="{{ post.featured_image.url }}"
    
    {{ post.title }}
    {{ post.category }}
    {{ post.short_description }}

{% empty %}

    <p>No published blog posts available.</p>

{% endfor %}
```

**Result:** The home page displays categories and published blog posts directly from the database instead of using static HTML content.
## 11. Create a Separate Category Page

Create a separate page to display blog posts belonging to a specific category.

### Step 1: Configure URLs in the Main Project

In the main project's `urls.py`, include the URLs from the `blogs` app.

```python
from django.urls import path, include

urlpatterns = [
    # Existing URL patterns
    path('category/', include('blogs.urls')),
]
```

### Step 2: Create `urls.py` in the Blogs App

Create a new `urls.py` file inside the `blogs` app.

Add the following URL pattern:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>/', views.post_by_category, name='post_by_category'),
]
```

### Step 3: Create a Category View in `blogs/views.py`

Create a view to fetch blog posts belonging to the selected category.

```python
from django.shortcuts import render, redirect
from .models import Blog, Category

def post_by_category(request, category_id):

    # Fetch published posts belonging to the selected category
    posts = Blog.objects.filter(
        status='published',
        category_id=category_id
    )

    # Check whether the category exists
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return redirect('home')

    context = {
        'posts': posts,
        'category': category,
    }

    return render(request, 'post_by_category.html', context)
```

**Important line:**

```python
category = Category.objects.get(pk=category_id)
```

This retrieves the category using its primary key.

If the category does not exist, the user is redirected to the home page.

### Step 4: Create `post_by_category.html`

Create a new HTML file inside the templates directory.

```text
templates/
    post_by_category.html
```

Display the selected category and its blog posts.

```django
{% extends 'base.html' %}

{% block content %}

    <h2>{{ category }}</h2>

    {% for post in posts %}

        <h3>{{ post.title }}</h3>
        <p>{{ post.short_description }}</p>

    {% empty %}

        <p>No published posts available in this category.</p>

    {% endfor %}

{% endblock %}
```

**Result:** Each category has a separate page displaying only its published blog posts.

## 12. Configure a Custom 404 Error Page

A 404 error occurs when a requested page or resource does not exist.

Django automatically detects 404 errors. A custom 404 page can be created to display a user-friendly error message.

### Step 1: Create `404.html`

Create a new HTML file inside the templates directory.

```text
templates/
    404.html
```

Add your custom 404 error page design.

### Step 2: Update `settings.py`  -      This not using in this PROJECT

For testing the custom 404 page, change the following settings:

```python
DEBUG = False

ALLOWED_HOSTS = ['*']
```

**Important:**

- `DEBUG = False` enables Django's custom error-page handling.
- `ALLOWED_HOSTS = ['*']` allows requests from any host, but it is not recommended for production.
- For production, specify your actual domain name in `ALLOWED_HOSTS`.

Example:

```python
ALLOWED_HOSTS = ['example.com', 'www.example.com']
```

**Note:** A custom 404 page is optional for this project. Django can handle 404 errors without a custom template. The custom template is used to improve the user experience.

## 13. Implement Template Inheritance

Template inheritance helps avoid repeating the same HTML code across multiple pages.

Instead of writing the header, navigation bar, hero section and other common elements in every template, create a common `base.html` file.

### Step 1: Create `base.html`

Create a base template inside the templates directory.

```text
templates/
    base.html
    home.html
    post_by_category.html
```

### Step 2: Add Common HTML Components

Move the common website components into `base.html`.

Common components include:

- Header
- Navigation bar
- Hero section
- Search section
- Category section
- Pagination
- Footer

Use Django template blocks to define where individual page content should appear.

```django
<!-- Header -->
<!-- Navigation Bar -->
<!-- Hero Section -->

<!-- Main Content -->

{% block content %}

{% endblock %}

<!-- Search -->
<!-- Categories -->
<!-- Pagination -->
<!-- Footer -->
```

### Step 3: Extend `base.html` in Other Templates

In `post_by_category.html`, use template inheritance.

```django
{% extends 'base.html' %}

{% block content %}

    <h2>{{ category }}</h2>

    {% for post in posts %}

        <!-- Blog Post Content -->

    {% empty %}

        <p>No posts available.</p>

    {% endfor %}

{% endblock %}
```

**Benefits of Template Inheritance:**

- Avoids duplicate HTML code.
- Makes the project easier to maintain.
- Allows common components to be updated in one place.
- Keeps individual page templates simple.

## 14. Create Context Processors

Context processors allow you to make common data available across multiple templates without passing the same data separately from every view.

For example, categories can be displayed in the navigation bar or sidebar on every page.

### Step 1: Create `context_processors.py`

Create a new Python file inside the `blogs` app.

```text
blogs/
    context_processors.py
```

### Step 2: Create a Context Processor Function

Add the following code:

```python
from .models import Category

def get_categories(request):

    categories = Category.objects.all()

    return {
        'categories': categories
    }
```

This function retrieves all categories and makes them available through the template context.

### Step 3: Register the Context Processor

Open `settings.py`.

Navigate to:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Existing context processors

                'blogs.context_processors.get_categories',
            ],
        },
    },
]
```

### Step 4: Access Categories in Any Template

Now you can access the categories directly in any template without passing them from individual views.

Example:

```django
{% for cat in categories %}
<a class="list-group-item" href="{% url 'post_by_category' cat.id %}">
    <li>
        {{ cat.category_name }}
    </li>

{% empty %}

    <li>No categories available.</li>

{% endfor %}
```

**Benefits of Context Processors:**

- Makes common data available across templates.
- Reduces repetitive code in views.
- Useful for navigation bars, category sidebars and common website components.

## 15. Create a Single Blog Detail Page

Create a separate page to display the complete details of an individual blog post.

### Step 1: Configure Slug-Based URL

Open the main project's `urls.py` and add the following URL pattern:

```python
path('blog/<slug:slug>/', BlogsViews.blogs, name='blogs'),
```

The slug is used to identify individual blog posts through SEO-friendly URLs.

Example:

```text
http://127.0.0.1:8000/getting-started-with-django/
```

### Step 2: Create a Blog Detail View

Open `blogs/views.py` and create a function to retrieve the selected blog post.

```python
from django.shortcuts import render, get_object_or_404
from .models import Blog

def blogs(request, slug):

    single_blog = get_object_or_404(
        Blog,
        slug=slug,
        status='published'
    )

    context = {
        'single_blog': single_blog,
    }

    return render(request, 'blogs.html', context)
```

**Explanation:**

- `get_object_or_404()` retrieves the blog using its slug.
- `status='published'` ensures that only published blogs are accessible.
- If the blog does not exist or is not published, Django returns a 404 error.
- The selected blog is passed to the template through the context.

### Step 3: Create `blogs.html`

Create a new HTML file inside the templates directory.

```text
templates/
    blogs.html
```

Extend the base template:

```django
{% extends 'base.html' %}

{% block content %}

    <h1>{{ single_blog.title }}</h1>

    <p>{{ single_blog.short_description }}</p>

    <img src="{{ single_blog.featured_image.url }}"
         alt="{{ single_blog.title }}">

    <div>
        {{ single_blog.blog_body }}
    </div>

{% endblock %}
```

**Result:** Clicking a blog post on the homepage opens its individual detail page.

---

## 16. Create an Assignment App

Create a separate Django app to manage website information, such as About details and social media links.

### Step 1: Create the App

Run the following command:

```bash
python manage.py startapp assignment
```

### Step 2: Register the App

Add the app to `INSTALLED_APPS` in `settings.py`.

```python
INSTALLED_APPS = [
    # Existing applications
    'blogs',
    'assignment',
]
```

### Step 3: Create the About Model

Open `assignment/models.py` and create an `About` model.

**Fields:**

| Field | Purpose |
|---|---|
| about_heading | Heading for the About section |
| about_description | Description of the website |
| created_at | Record creation date and time |
| updated_at | Last modification date and time |

Example:

```python
from django.db import models

class About(models.Model):
    about_heading = models.CharField(max_length=200)
    about_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about_heading
```

### Step 4: Create the SocialLinks Model

Create another model to store social media links.

**Fields:**

| Field | Purpose |
|---|---|
| platform | Social media platform name |
| link | Social media profile URL |
| created_at | Record creation date and time |
| updated_at | Last modification date and time |

Example:

```python
class SocialLinks(models.Model):
    platform = models.CharField(max_length=100)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform
```

### Step 5: Create a Social Links Context Processor

Create a `context_processors.py` file inside the `assignment` app.

```text
assignment/
    context_processors.py
```

Add the following function:

```python
from .models import SocialLinks

def get_social_links(request):

    social_links = SocialLinks.objects.all()

    return {
        'social_links': social_links
    }
```

This function makes social media links available across all templates.

### Step 6: Register the Context Processor

Open `settings.py` and navigate to `TEMPLATES → OPTIONS → context_processors`.

Add:

```python
'assignment.context_processors.get_social_links',
```

**Note:** Use `assignment.context_processors`, not `blogs.context_processors`, because the function belongs to the assignment app.

---

## 17. Configure Django Admin for About

Register the About model in `assignment/admin.py`.

### Step 1: Create AboutAdmin Class

Use a custom admin class to allow only one About record.

```python
from django.contrib import admin
from .models import About, SocialLinks

class AboutAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        count = About.objects.all().count()

        if count == 0:
            return True

        return False
```

### Step 2: Register the About Model

```python
admin.site.register(About, AboutAdmin)
```

**Explanation:**

- `has_add_permission()` controls whether a new About record can be added.
- If no About record exists, the admin can add one.
- If one already exists, the Add button is disabled.

### Step 3: Register SocialLinks

```python
admin.site.register(SocialLinks)
```

You can now manage social media links through the Django admin panel.

**Note:** This implementation prevents adding a second About record through the standard Django admin interface. It does not enforce a database-level singleton constraint or prevent duplicate records created through other methods.

---

## 18. Implement Blog Search Functionality

Create a search feature that allows visitors to find published blog posts using keywords.

### Step 1: Configure the Search URL

Open the main project's `urls.py` and add:

```python
path('blogs/search/', BlogsViews.search, name='search'),
```

### Step 2: Create the Search View

Open `blogs/views.py` and create the search function.

```python
from django.db.models import Q
from .models import Blog

def search(request):

    keyword = request.GET.get('keyword', '').strip()

    blogs = Blog.objects.none()

    if keyword:
        blogs = Blog.objects.filter(
            Q(title__icontains=keyword) |
            Q(short_description__icontains=keyword) |
            Q(blog_body__icontains=keyword),
            status='published'
        )

    context = {
        'blogs': blogs,
        'keyword': keyword,
    }

    return render(request, 'search.html', context)
```

### Understanding the Search Query

**Q Objects:**

`Q` objects allow multiple query conditions to be combined using logical operators.

| Query | Purpose |
|---|---|
| `title__icontains` | Searches blog titles |
| `short_description__icontains` | Searches short descriptions |
| `blog_body__icontains` | Searches blog content |
| `\|` | Represents OR condition |
| `status='published'` | Displays only published blogs |

**Example:**

If a visitor searches for `Django`, the search function checks the title, short description and blog body for matching content.

### Step 3: Create `search.html`

Create a new HTML template:

```text
templates/
    search.html
```

Extend the base template:

```django
{% extends 'base.html' %}

{% block content %}

    <h2>Search Results</h2>

    <p>Search keyword: {{ keyword }}</p>

    {% for post in blogs %}

        <div class="blog-card">

            <h3>{{ post.title }}</h3>

            <p>{{ post.short_description }}</p>

            <a href="{% url 'blogs' post.slug %}">
                Read More
            </a>

        </div>

    {% empty %}

        <p>No blog posts found.</p>

    {% endfor %}

{% endblock %}
```

### Step 4: Add the Search Form

Add the search form to your `base.html` or navbar.

```django
<form action="{% url 'search' %}" method="GET">

    <input
        type="text"
        name="keyword"
        placeholder="Search blogs..."
        value="{{ request.GET.keyword }}"
    >

    <button type="submit">
        Search
    </button>

</form>
```

**Result:** Visitors can search published blog posts using keywords and view matching results on a separate search page.

---

## 19. Create and Apply Migrations

After creating the models in the assignment app, run the migration commands.

```bash
python manage.py makemigrations
python manage.py migrate
```

These commands create and apply the database tables for the About and SocialLinks models.

Create Registration page------------>
    create form.py file in blog_main--------->
        from django.contrib.auth.models import User
        from django.contrib.auth.models import User
        from django.contrib.auth.forms import UserCreationForm

        class RegistrationForm(UserCreationForm):
            class Meta:
                model = User
                fields = ('email','username','password1','password2')
        
    create url in blog_main/urls.py------->
        path('register/', views.register, name='register'),
    
    blog_main/views.py----------->
        
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html',context)
    create register.html---------->
        {% block content %}
            {% load crispy_forms_tags %}
                {% csrf_token %}
                {{ form | crispy }}
        {% endblock %}
    
    Using Django crispy forms----------->
        Run in Terminal
            pip install django-crispy-forms
            pip install crispy-bootstrap4
        Add crispy in settings.py------->
            CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
            CRISPY_TEMPLATE_PACK = 'bootstrap4'
            INSTALLED_APPS = (
                ...
                'crispy_forms',
                'crispy_bootstrap4',
            )
