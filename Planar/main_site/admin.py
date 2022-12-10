
from django.contrib import admin

from .models import  Company, Equipment_Class, Equipment_Category, Equipment_Item, Equipment_Acessory
from modeltranslation.admin import TranslationAdmin                 # <- multiLang:13) import TranslationAdmin (next: admin.py)


# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('id','company_name', 'is_published')
#     list_display_links = ('company_name',)
#     list_editable = ('is_published',)

class CompanyAdmin(TranslationAdmin):                               # <- multiLang:14) instead of "admin.ModelAdmin" is need
    list_display = ('id','company_name', 'is_published')            # to inherit from TranslationAdmin (this allow to hide
                                                                    # prime field of model and display only tranlatable fields)
    list_display_links = ('company_name',)                          # (next: admin.py)
    list_editable = ('is_published',)

class Equipment_ClassAdmin(TranslationAdmin):
    list_display = ('id','class_name', 'company', 'is_published')
    list_display_links = ('id','class_name',)
    list_editable = ('is_published',)
    list_filter = ('company',)

class Equipment_CategoryAdmin(TranslationAdmin):
    list_display = ('id','category_name','equipment_class', 'company', 'is_published')
    list_display_links = ('id','category_name',)
    list_editable = ('is_published',)
    list_filter = ('company',)

class Equipment_ItemAdmin(TranslationAdmin):
    list_display = ('id', 'item_name', 'equipment_category','equipment_class', 'company', 'is_published')
    list_display_links = ('id','item_name',)
    list_editable = ('is_published',)
    list_filter = ('company',)

class Equipment_AcessoryAdmin(TranslationAdmin):
    list_display = ('id', 'acessory_name', 'company', 'is_published')
    list_display_links = ('id','acessory_name',)
    list_editable = ('is_published',)
    list_filter = ('company',)
    filter_horizontal = ['equipment',]


admin.site.register(Company,CompanyAdmin)                           # <- multiLang:15) add *model_name*Admin to register
admin.site.register(Equipment_Class,Equipment_ClassAdmin)           # (also can be simpy decorated) (next: forms.py)
admin.site.register(Equipment_Category,Equipment_CategoryAdmin)
admin.site.register(Equipment_Item,Equipment_ItemAdmin)
admin.site.register(Equipment_Acessory,Equipment_AcessoryAdmin)