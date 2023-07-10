"""
URL configuration for api_for_mom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import root_route

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls')),
    path('', include('followers.urls')),
    path('', include('newsletters.urls')),


]


# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.urls.resolvers import URLPattern, URLResolver

# # Define the root route view
# @api_view()
# def root_route(request):
#     # Get all the endpoints from the URL patterns
#     endpoints = get_endpoints(urlpatterns)

#     # Construct the welcome message
#     message = "Welcome to MOM NETWORK's Django REST Framework API!\n\nEndpoints:\n"
#     for endpoint in endpoints:
#         message += f"- {endpoint}\n"

#     return Response({"message": message})

# # Function to extract endpoints from URL patterns
# def get_endpoints(urlpatterns, prefix=''):
#     endpoints = []
#     for pattern in urlpatterns:
#         if isinstance(pattern, URLPattern):
#             endpoint = get_endpoint(pattern, prefix)
#             if endpoint:
#                 endpoints.append(endpoint)
#         elif isinstance(pattern, URLResolver):
#             endpoints.extend(get_endpoints(pattern.url_patterns, prefix + pattern.pattern.regex.pattern))

#     return endpoints

# # Function to extract endpoint from URL pattern
# def get_endpoint(pattern, prefix=''):
#     if pattern.callback:
#         return prefix + pattern.pattern.regex.pattern

#     return None

# urlpatterns = [
#     path('', root_route),
#     path('admin/', admin.site.urls),
#     path('api-auth/', include('rest_framework.urls')),
#     path('dj-rest-auth/', include('dj_rest_auth.urls')),
#     path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
#     path('', include('profiles.urls')),
# ]
