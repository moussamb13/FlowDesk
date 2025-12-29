# --------------------------------------------------------
# Custom User model for FlowDesk
# Using email as the unique identifier instead of username
# Includes full_name, staff/admin flags, and date_joined
# --------------------------------------------------------

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

# Manager class to handle user creation
# --------------------------------------------------------
# CustomUserManager defines how to create normal users
# and superusers
# --------------------------------------------------------
class CustomUserManager(BaseUserManager):
    
    # Create a normal user
    def create_user(self, email, password=None, **extra_fields):
        # Ensure an email is provided
        if not email:
            raise ValueError("The Email field must be set")
        
        # Normalize email (lowercase domain)
        email = self.normalize_email(email)
        
        # Create user instance
        user = self.model(email=email, **extra_fields)
        
        # Hash the password
        user.set_password(password)
        
        # Save user to database
        user.save(using=self._db)
        return user

    # Create a superuser (admin)
    def create_superuser(self, email, password=None, **extra_fields):
        # Ensure admin flags are set
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        # Use create_user to actually create it
        return self.create_user(email, password, **extra_fields)

# --------------------------------------------------------
# The actual User model
# --------------------------------------------------------
class User(AbstractBaseUser, PermissionsMixin):
    # Unique email field (used as login)
    email = models.EmailField(unique=True)
    
    # Optional full name
    full_name = models.CharField(max_length=150, blank=True)
    
    # Active flag for soft-delete / deactivate
    is_active = models.BooleanField(default=True)
    
    # Staff/admin flag
    is_staff = models.BooleanField(default=False)
    
    # Automatically store the join date
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Connect manager
    objects = CustomUserManager()
    
    # Field used for login
    USERNAME_FIELD = 'email'
    
    # Required fields for superuser creation (none extra)
    REQUIRED_FIELDS = []
    
    # String representation of the user
    def __str__(self):
        return self.email
