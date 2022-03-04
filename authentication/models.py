from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as lazy
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from student import settings


class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**fields):
        if not email:
            raise ValueError(lazy('Please provide valid email'))

        email=self.normalize_email(email)
        new_user=self.models(email=email,**fields)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self,email,password,**fields):
        fields.setdefault('is_stuff',True)
        fields.setdefault('is_active', True)
        fields.setdefault('is_superuser', True)

        if fields.get('is_stuff') is not True:
            raise ValueError(lazy('User should be Employee'))

        if fields.get('is_active') is not True:
            raise ValueError(lazy('User should be Active Employee'))

        if fields.get('is_superuser') is not True:
            raise ValueError(lazy('User is not Super User'))

        return self.create_user(email, **fields)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

class User(AbstractBaseUser):
    username = models.CharField(lazy('Username'), max_length=40, unique=True)
    email = models.CharField(lazy('Email'), max_length=80, unique=True)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    date_joined = models.DateTimeField(lazy('Date'), auto_now_add=True)
    REQUIRED_FIELDS = ['username', 'phone_number', 'is_staff']
    USERNAME_FIELD = 'email'
    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return f"User {self.username}"



