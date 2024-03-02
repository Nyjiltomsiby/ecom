from django.contrib import admin

from shopper.models import Category,Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug','description']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product)
