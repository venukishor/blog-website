from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Home,name='Home'),
    path('logout/',views.logout_view,name='logout_view'),
    path('register/',views.Register,name='Register'),
    path('login/',views.Login,name='Login'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('blogs/',views.blogs,name='blogs'),
    path('add_blogs/',views.add_blogs,name='add_blogs'),
    path('blog_comments/',views.blogs_comments,name='blog_comments'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)