from django.urls import path
from django.conf import settings
import blog.views
urlpatterns = [
    path('',blog.views.allblogs , name = 'blog/allblogs')
]
