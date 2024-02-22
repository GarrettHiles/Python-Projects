from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=50, default='', blank=True, null=False)
    state = models.CharField(max_length=2, default='', blank=True, null=False)
    campus_id = models.IntegerField(default=0, blank=True, null=False)

    object = models.Manager()

    # Displays the object output values in string form
    def __str__(self):
        display_campus = '{0.campus_name}'
        # Returns the input value of title and instructor name
        # in tuple display instead of default title
        return display_campus.format(self)

    #displays model name as University Campus in the browser admin page
    class Meta:
        verbose_name_plural = "University Campus"
