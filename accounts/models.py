from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "A user with that username already exists.",
        }, null=True, blank=True
    )
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField('Email Address', unique=True, error_messages={
        'unique': "A user with that email already exists.",
    })
    last_login = models.DateTimeField(auto_now=False, null=True, blank=True)
    last_request = models.DateTimeField(auto_now=False, null=True, blank=True)
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
   
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ,
    )
    date_joined = models.DateField('date joined', default=timezone.now, null=True, blank=True)
    objects = UserManager()
    EMAIL_FIELD = 'username'
    USERNAME_FIELD = 'username'
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name




User = MyUser()
