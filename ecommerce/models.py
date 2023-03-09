from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]

class Categories(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True,blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(null=True,blank=True, upload_to='products/uploads/%Y/%m/%d/')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Categories, self).save(*args, **kwargs)


class Products(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    images = models.ImageField(null=True, blank=True, upload_to='products/uploads/%Y/%m/%d/')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    sale_price = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='products')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products', args=[str(self.slug)])
