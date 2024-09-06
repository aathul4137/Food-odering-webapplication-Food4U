from django.contrib import admin

from appfood4u.models import Category, Myimage, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description', 'price', 'category']
    list_filter = ['category']
    search_fields = ['product_name', 'description']
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    
class MyimageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']
    search_fields = ['product__product_name']

    
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Myimage,MyimageAdmin)
