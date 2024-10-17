from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Product, Page, Image, Feature, Section

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  # Number of empty forms to display

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['__str__', 'img_preview']

class SectionAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['__str__', 'img_preview']

class FeatureAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['__str__', 'sequence']
    list_editable = ['sequence']

class PageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'page']


admin.site.register(Product, ProductAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Section, SectionAdmin)