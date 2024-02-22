from django.db import models

# Create your models here.

class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default='', blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default='', blank=True, null=False)
    duration = models.FloatField(default=None, blank=True, null=False)

    #Model Manager creation
    object = models.Manager()

    #Displays the object output values in string form
    def __str__(self):
        display_course = '{0.title}: {0.instructor_name}'
        #Returns the input value of title and instructor name
        #in tuple display instead of default tites
        return display_course.format(self)

    #displays model name as University Class in the brower admin page
    class Meta:
        verbose_name_plural = "University Class"


