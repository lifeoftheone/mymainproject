from django.shortcuts import render, redirect
from .models import *
from .forms import AddUpdateBlogForm, UserProfileForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required


def homepage(request):
    """
    Function to retrieve and display all employee records.
    Returns:
        Return a html file with particular name with all the records
    """
    context = {'homepage': Blog.objects.all().order_by('-date')}
    return render(request, "mainapp/homepage.html", context)


def blog(request, id):
    """
    Function to retrieve and display  blog of particular id.
    Returns:
        Return a html file with particular blog and details.
    """
    blogs = Blog.objects.get(pk=id)
    return render(request, 'mainapp/blog.html', {'blogs': blogs})


def userlogin(request):
    """
    Function to login the user with the emailid and password.
    Returns:
        Return a home page after login.
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            print(request.user.is_staff)
            print(request.user)
            print(request.user.name)
            print(request.user.gender)
            print(request.session)

            return redirect('/teamblog/bloghomepage')
        else:
            return render(request, 'mainapp/login.html', {'error': 'User name and password invaild'})
    else:
        return render(request, 'mainapp/login.html')


def userlogout(request):
    """
    logout the user
    """
    logout(request)
    return redirect('/teamblog/')


@login_required(login_url='login')
def blog_homepage(request):
    """
    Function to retrieve and display all employee records.
    Returns:
        Return a html file with particular name with all the records
    """
    context = {'blogs': Blog.objects.all().order_by('-date')}
    return render(request, 'mainapp/bloghomepage.html', context)


@login_required(login_url='login')
def register(request):
    """
    Function to register the user.
    Returns:
        After registering the user it redirect to home.
    """
    if request.user.is_staff:
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/teamblog/bloghomepage/')
            else:
                return render(request, 'mainapp/register.html', {'error': 'regestration failed'})
        else:
            return render(request, 'mainapp/register.html')
    else:
        return redirect("/teamblog/bloghomepage")


@login_required(login_url='login')
def add_update_blog(request, id=0):
    """
    Function to save and update new or old records.
    Args:
        request,id
    Returns:
        Return to home after adding a blog.
    """
    if request.method == "GET":
        if id == 0:
            return render(request, 'mainapp/add_update_blog.html',{'name': request.user.name,'email': request.user})
        else:
            blog = Blog.objects.get(pk=id)
            return render(request, "mainapp/add_update_blog.html", {'blog': blog})
    else:
        if id == 0:
            form = AddUpdateBlogForm(request.POST)
        else:
            blog = Blog.objects.get(pk=id)
            form = AddUpdateBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/teamblog/bloghomepage/')


def blog_delete(request, id):
    """
    Function to delete.
    Args:
        id
    Returns:
        Return to home with details
    """
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('/teamblog/bloghomepage/')


def comment(request, id):
    """
    Function to post a comment
    Args:
        request,id
    Returns:
        Return to homepage
    """
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        blog = Blog.objects.filter(id=id)
        for blog in blog:
            a = blog.email
        if a == email:
            return render(request, 'mainapp/comment.html', {'error': 'user can not comment on your own post'})
        else:
            comments = Comment.objects.create(blog_id=id, name=name, email=email, comment=comment)
            comments.save()
            return redirect('/teamblog/')
    else:
        blog = {Blog.objects.filter(id=id)}
        return render(request, 'mainapp/comment.html', {'blog': blog}, )


def readcomment(request, id):
    """
    Function to retrieve and display all  records.
    Returns:
        Return a html page which display the records.
    """

    comments = {'comments': Comment.objects.filter(blog_id=id).order_by('-date')}
    return render(request, 'mainapp/readcomment.html', comments)
