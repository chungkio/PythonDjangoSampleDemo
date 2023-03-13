from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from tinymce.models import HTMLField 

# Create your models here.
STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]

class Categories(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True,blank=True)
    description = HTMLField()
    image = models.ImageField(null=True,blank=True, upload_to='blogs/uploads/%Y/%m/%d/')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Categories, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    body = HTMLField()
    images = models.ImageField(null=True, blank=True, upload_to='blogs/uploads/%Y/%m/%d/')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='posts')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', args=[str(self.slug)])
