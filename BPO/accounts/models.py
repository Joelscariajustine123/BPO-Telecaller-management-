# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     phone_number = models.CharField(max_length=15, unique=True ,default=None)
#     Role_CHOICES = [
#         ('admin', 'Admin'),
#         ('telecaller', 'Telecaller'),
#         ('manager', 'Manager'),
#         ('lead', 'Lead'),
#         ('superuser', 'Superuser'),
#     ]
#     role = models.CharField(max_length=20, choices=Role_CHOICES,default='telecaller')

    # managed_by = models.ForeignKey(
    #     'self', 
    #     on_delete=models.CASCADE, 
    #     null=True, 
    #     blank=True,
    #     related_name='staff'
    # )

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='customuser_set',  # Unique related_name
    #     blank=True,
    #     help_text=('The groups this user belongs to. A user will get all permissions '
    #                'granted to each of their groups.'),
    #     related_query_name='user',
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='customuser_set',  # Unique related_name
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     related_query_name='user',
    # )



from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # phone_number = models.CharField(max_length=15, unique=True, default=None)
    phone_number = models.CharField(
    max_length=15, 
    unique=True,
    null=True,        # allows NULL in DB
    blank=True,       # allows empty value in forms
)

    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('telecaller', 'Telecaller'),
        ('manager', 'Manager'),
        ('lead', 'Lead'),
        ('superuser', 'Superuser'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='telecaller')
