from django.contrib import admin
from django.utils.html import format_html  # Import the format_html function
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')  # Customize the columns displayed

    # Optional: Method to display image preview in admin list view
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />'.format(obj.image.url))
        return ""

    image_preview.short_description = 'Image'


admin.site.register(Product, ProductAdmin)
