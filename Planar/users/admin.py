from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'company',)
    #list_editable = ('is_active',)
    model = CustomUser
    #add field from models to the "add" form in admin site
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields':('company',)
            }
        )
    )
    #add field from models to the "edit" form in admin site
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields':('company',)
            }
        )
    )

admin.site.register(CustomUser,CustomUserAdmin)