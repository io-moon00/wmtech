from django.db import models
from django.utils.html import mark_safe

# Create your models here

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    card_image = models.ForeignKey(
            'Image', 
            on_delete=models.SET_NULL, 
            null=True, 
            blank=True, 
            related_name='card_image_for_product'
        )

    def __str__(self):
        return self.name
    
    def get_images(self):
        return Image.objects.filter(product=self)
    
    class Meta:
        verbose_name_plural = "Projects"
        verbose_name = "Project"


class Image(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.product.name} - {self.pk}'
    
    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>')

class Page(models.Model):
    PAGES = [
        ('home', 'Home'),
        ('impressum', 'Impressum'),
        ('legal', 'Datenschutzerklärung'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    page = models.CharField(max_length=10, choices=PAGES)

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    sequence = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['sequence']
    
class Section(models.Model):
    SECTIONS = [
        ('projects', 'Projekte'),
        ('features', 'Features'),
        ('about', 'Über Uns'),
        ('contact', 'Kontakt'),
    ]
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    background_image = models.ImageField(upload_to='sections/', null=True, blank=True)
    section = models.CharField(max_length=10, choices=SECTIONS, unique=True)

    def __str__(self):
        return self.title
    
    def img_preview(self): 
        return mark_safe(f'<img src = "{self.background_image.url}" width = "200"/>')
