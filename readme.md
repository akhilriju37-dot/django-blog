View in home page ----------------->
    -create url 
    -views create a home() 
    -create templates in html page 
    -add templates in settings DIRS


Adding Bootstrap ----------------------->
    -Go to the bootstrap website Select for Blog Page
    -Download and add the html,css code OR copy / paste
    -Create a static folder
        - Create css and images
    -load static folder in html file 
        -{% load static %}
        - <link rel="stylesheet" href={% static 'css/blog.css' %}>
        -Add settings.py
            -static root = base dir / 'static'
            -staticfiles dirs = [
                'project folder name / static folder name'
            ]

