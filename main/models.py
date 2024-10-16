from django.db import models

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


class Image(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.product.name} - {self.pk}'

class Page(models.Model):
    PAGES = [
        ('home', 'Home'),
        ('impressum', 'Impressum'),
        ('legal', 'Datenschutzerklärung'),
    ]
    image = models.ImageField(upload_to='pages/', null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    page = models.CharField(max_length=10, choices=PAGES)

class Feature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
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
