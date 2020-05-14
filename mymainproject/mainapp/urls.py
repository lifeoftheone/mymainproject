from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('blog/<int:id>/', views.blog, name='blog'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('bloghomepage/', views.blog_homepage, name='bloghomepage'),
    path('register/', views.register, name='register'),
    path('add_update_blog/<int:id>/', views.add_update_blog, name='add_update_blog'),
    path('delete/<int:id>/', views.blog_delete, name='blog_delete'),
    path('comment/<int:id>/', views.comment, name='comment'),
    path('readcomment/<int:id>/', views.readcomment, name='readcomment'),

]
