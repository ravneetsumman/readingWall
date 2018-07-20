from django.db import models

# Create your models here.
class Connections(models.Model):
    AVAILABLE = 0
    PENDING = 1
    ACCEPTED = 2
    REJECTED = 3
    CANCELLED = 4
    STATUS_CHOICES = (
        (PENDING, 'pending'),
        (ACCEPTED, 'accepted'),
        (REJECTED, 'rejected'),
        (CANCELLED, 'cancelled'),
    )
    friendreq_by = models.ForeignKey('auth.User', related_name='requestedby', on_delete=models.CASCADE)
    friendreq_to = models.ForeignKey('auth.User', related_name='requestedto', on_delete=models.CASCADE)
    request_status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Feed(models.Model):
    owner = models.ForeignKey('auth.User', related_name='wallposts', on_delete=models.CASCADE)
    blog_url = models.CharField(max_length=255, blank=True)
    context = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
