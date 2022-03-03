from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email = email , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
        
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("super user must have is_staff True")
        
        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    mobile = models.CharField(max_length=10, unique=True, blank=True, null=True)
    country_code = models.CharField(max_length=8, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images',  blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    username = None
    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]
    

