from django.db import models


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
STUDENT_CHOICES = (
    ('IT', 'IT student'),
    ('nonIT', 'non-IT student')
)


class Courses(models.Model):
    courseTitle = models.CharField(max_length=100, blank=True, null=True)
    courseChoices = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.courseTitle

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class StudentsRegisterModel(models.Model):
    courseOfStudy = models.ManyToManyField('Courses', related_name='my_courses')
    studentType = models.CharField(max_length=5, choices=STUDENT_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='ampmedia/students')
    occupation = models.CharField(max_length=200)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'student'
        verbose_name_plural = 'students'
