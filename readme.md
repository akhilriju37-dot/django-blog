

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

media configure ------->
    settings.py --->
        MEDIA_URL = '/media/'
        MEDIA_ROOT = BASE_DIR /'media'

    urls.py ------>
        urlpatterns =[............
        .....]+static(settings.MEDIA_URL, document_root.MEDIA_ROOT)
