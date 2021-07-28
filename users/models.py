from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    """Profile model.
    Model that extends the base data with other
    information for user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=30, blank=True)
    position = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50, blank=True)
    time_zone = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username
