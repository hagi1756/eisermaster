# from django.contrib import admin
# from core.models import Category,Product,Blog,ContactUs,Setting,Contact
# from modeltranslation.admin import TranslationAdmin

# admin.site.register(Category)
# # admin.site.register(Product)
# # admin.site.register(Blog)
# admin.site.register(ContactUs)
# admin.site.register(Setting)
# admin.site.register(Contact)

# @admin.register(Product)
# class ProductAdmin(TranslationAdmin):
#     list_display=('name','size','price','category')
#     search_fields=('name','price',"category__name")
#     list_filter=('category','size')
#     readonly_fields=('like',)
#     fields=('name','price','category','color','size','like','is_active')
#     ordering=('price',)



# class BlogAdmin(admin.ModelAdmin):
#     list_display=('title','created_at','slug')
#     search_fields=('title','description',)
#     list_filter=('created_at',)
#     fields=('title','slug','description','image','is_active',)
#     ordering=('created_at','is_active')

# # admin.site.register(Product,ProductAdmin)
# admin.site.register(Blog,BlogAdmin)

# admin.site.site_header = "Eiser Master"  # Bu ana sayfada görünecek başlık
# admin.site.site_title = "Eiser Master"   # Tarayıcı sekmesinde görünecek başlık



from django.contrib import admin
from core.models import Category, Product, Blog, ContactUs, Setting, Contact
from modeltranslation.admin import TranslationAdmin
from excel_response import ExcelResponse

admin.site.register(Category)
admin.site.register(ContactUs)
admin.site.register(Setting)
admin.site.register(Contact)


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'size', 'price', 'category')
    search_fields = ('name', 'price', "category__name",'size',)
    list_filter = ('category', 'size')
    readonly_fields = ('like',)
    fields = ('name', 'price', 'category', 'color', 'size', 'like', 'is_active')
    ordering = ('price',)


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ('title', 'created_at', 'slug')
    search_fields = ('title', 'description',)
    list_filter = ('created_at',)
    fields = ('title', 'slug', 'description', 'image', 'is_active',)
    ordering = ('created_at', 'is_active')

    actions = ['excel_export']

    def excel_export(self, request, queryset):
        data = []
        for blog in queryset:
            data.append([blog.title,  blog.description,  blog.created_at])
        return ExcelResponse(data, output_filename ='blogs')
    excel_export.short_description = " Export to Excel" 




admin.site.site_header = "Eiser Master"  # Bu ana sayfada görünecek başlık
admin.site.site_title = "Eiser Master"   # Tarayıcı sekmesinde görünecek başlık
