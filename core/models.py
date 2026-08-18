from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)

class StudentApplication(models.Model):
    STATUS = [('pending','Pending'), ('approved','Approved'), ('rejected','Rejected')]
    student_name = models.CharField(max_length=150)
    grade = models.CharField(max_length=20)
    parent_name = models.CharField(max_length=150)
    parent_phone = models.CharField(max_length=20)
    previous_school = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    audience = models.CharField(max_length=20, default='all')  # all, students, teachers
    created_at = models.DateTimeField(auto_now_add=True)

class Resource(models.Model):
    TYPE = [('note','Short Note'), ('exam','Past Exam'), ('worksheet','Worksheet'), ('book','Textbook')]
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE)
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50)  # students, teachers, compound, exam
    image = models.ImageField(upload_to='gallery/%Y/%m/')  # will use R2
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    # Generic relations for comments, saves
    comments = GenericRelation('Comment')
    saves = GenericRelation('Save')

class Story(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    comments = GenericRelation('Comment')
    saves = GenericRelation('Save')

class Achievement(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Meeting(models.Model):
    title = models.CharField(max_length=255)
    time = models.CharField(max_length=50)  # could be DateTimeField
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    name = models.CharField(max_length=150)
    rating = models.PositiveSmallIntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)  # for authenticated
    anonymous_name = models.CharField(max_length=100, blank=True)  # for public "You"
    text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    created_at = models.DateTimeField(auto_now_add=True)

class Save(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    created_at = models.DateTimeField(auto_now_add=True)

class ActivityLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class SiteSettings(models.Model):
    phone = models.CharField(max_length=50, default='+251 907 123 450')
    copyright_year = models.CharField(max_length=4, default='2026')
    developer_name = models.CharField(max_length=100, default='Murad Desiye', editable=False)

class AIAPISettings(models.Model):
    endpoint = models.URLField(blank=True)
    api_key = models.CharField(max_length=255, blank=True)
    model = models.CharField(max_length=50, default='gpt-3.5-turbo')