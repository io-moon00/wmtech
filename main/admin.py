from django.contrib import admin
from .models import Product, Page, Image, Feature, Section

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  # Number of empty forms to display

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Page)
admin.site.register(Image)
admin.site.register(Feature)
admin.site.register(Section)