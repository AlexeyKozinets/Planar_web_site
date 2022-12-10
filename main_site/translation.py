# this file add to the selected fields of the model additional fields for different number of laguages
# the number of languages depend of "LANGUAGES = [,]" in in settings.py



from modeltranslation.translator import register, TranslationOptions    # <- multiLang:8) import these modules (next: translation.py)
from .models import (
    Company,
    Equipment_Class,
    Equipment_Category,
    Equipment_Item,
    Equipment_Acessory,
)                                                                       # <- multiLang:9) import models from model.py which fields
                                                                        # is need to be tansladed  (next: translation.py)

@register(Company)                                                      # <- multiLang:10) decorate "register" by class which name
class CompanyTranslationOptions(TranslationOptions):                    # include name of model and "TranslationOptions";
    fields = ('company_name',)                                          # "fields" include those fields names which is need to be translated (next: console)
    required_languages = ('ru', 'en')                                   # "required_languages" makes pointed fields in "fields" are required

                                                                        # <- multiLang:11) python manage.py makemigrations (next: console)
                                                                        # <- multiLang:12) python manage.py migrate (next: admin.py)

@register(Equipment_Class)
class Equipment_ClassTranslationOptions(TranslationOptions):
    fields = ('class_name', 'short_description', 'full_description',)
    required_languages = ('ru', 'en')

@register(Equipment_Category)
class Equipment_CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', 'short_description', 'full_description',)
    required_languages = ('ru', 'en')

@register(Equipment_Item)
class Equipment_CategoryTranslationOptions(TranslationOptions):
    fields = ('item_name', 'short_description', 'full_description',)
    required_languages = ('ru', 'en')

@register(Equipment_Acessory)
class Equipment_AcessoryTranslationOptions(TranslationOptions):
    fields = ('acessory_name', 'short_description', 'full_description',)
    required_languages = ('ru', 'en')


