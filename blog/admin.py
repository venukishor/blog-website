from django.contrib import admin
from .models import Profile
from .models import BlogPost
from .models import Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(BlogPost)
admin.site.register(Comment)