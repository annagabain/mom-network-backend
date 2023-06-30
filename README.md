# Django Rest Framework API 
## for the 
# Mom Network project

## Live: https://mom-network-backend.herokuapp.com/

### The Database

<img width="70%" alt="database diagram" src="src/drawsql-mom-network-database-diagram-export-2023-06-27.png">

### Initial Terminal commands

- Install Django:  pip3 install django

- Create Project:  django-admin startproject api_for_mom .

- Install Cloudinary Storage:  pip install django-cloudinary-storage

- Install Pillow (Image Processing):  pip install Pillow

- Create env.py file and store the Cloudinary url value

- In settings.py, add Cloudinary to installed apps and create storage


### Other Terminal commands and repeated App creation process

1. Create the App: python manage.py startapp *my_app_name*
2. Make a  Model: 
  - from django.db import models
  - from django.contrib.auth.models import User
  - class *my_Model_name*(models.Model):
  - all the fields, methods and the Meta class
3. Create a Serializer for this Model: create the serializers.py file, inside that file: 
  - from rest_framework import serializers,  
  - .models import *my_model_name*
4. Make generic Viewset, in views.py:
  - from rest_framework.views import APIView
  - from .models import *my_Model_name*
  - from .serializers import *my_Serializer_name*
  - other imports
5. Create the Route(s) in urls.py


### Deployment 

### Sources & Credits

Build a REST API with Django REST Framework:  https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c

### Tools

Draw SQL Graph: https://drawsql.app/

### Acknowledgments

Richard Wells - the course mentor for friendly guidance, help with refactoring some code and numerous project feedback sessions