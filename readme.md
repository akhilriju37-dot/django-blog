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

create another page to seperate category
    -create a url in urls.py----->
        path('category/', include('blogs.urls'))

    create a url.py in blog app and create a url
        create a url pattern ----->
            urlpatterns = [
                path('<int:category_id>', views.post_by_category, name='post_by_category')
                ]   

    views.py at blog app and add a html file -------->
            try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')

        context = {
            'posts': posts,
            'category': category
        }
        return render(request, 'post_by_category.html', context)

    create a html file in templates ---->
        post_by_category.html------->
            add a category wise seperated

404 ERROR Page---------->
    Django is automatically dedect
    -create 404.html

    settings.py change--------->
        DEBUG = False
        ALLOWED_HOSTS = ['*']

