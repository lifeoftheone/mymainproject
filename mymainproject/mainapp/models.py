from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    helps django work with our custom model
    """
    def create_user(self, email, name, gender, mobile, password=None):
        """
        create a new user object
        """
        if not email:
            raise ValueError('user must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, gender=gender, mobile=mobile)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, gender, mobile, password):
        """
        create a save the new superuser with the given detail
        """
        user = self.create_user(email, name, gender, mobile, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    represent a user inside our system
    """
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=6)
    mobile = models.CharField(max_length=16, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'gender', 'mobile']

    def get_full_name(self):
        """
        use to get the full name of the user
        """
        return self.name

    def __str__(self):
        """
        django uses this when it need to convert the object into string
        """
        return self.email

class Blog(models.Model):
    """
    create a table for blog
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    """
    Create a comment table in database
    """
    blog_id = models.CharField(max_length=100)
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=64, default="")
    comment = models.TextField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)