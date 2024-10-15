from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="index"), 
    path("base/", views.home, name='home'),
    path("about/", views.about, name="about"), 
    path("login/", views.getLogIn, name="login"), 
    path("register/", views.getSignUp, name="register"), 
    path('post/new/', views.home, name='post-create'),
    path('like-post/', views.like_post, name='like-post'),
    path("post/<int:post_id>/comments/", views.home, name='comments'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)