from django.db import models


# Create your models here.

PREFIX_CHOICES = {
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
}
class Profiles(models.Model):
    prefix = models.CharField(max_length=10, default='', choices=PREFIX_CHOICES)
    FirstName = models.CharField(max_length=20, default="", blank=True, null=False)
    LastName = models.CharField(max_length=20, default="", blank=True, null=False)
    Email = models.CharField(max_length=50, default="", blank=True, null=False)
    Username = models.CharField(max_length=20, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.FirstName
