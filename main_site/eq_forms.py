from django import forms
from .models import Company, Equipment_Class, Equipment_Category, Equipment_Item, Equipment_Accessory


class Company_Form(forms.ModelForm):
    class Meta:
        model = Company
        fields = (  'is_published', 'head_img',
                    'company_name_ru', 'company_name_en',
                    'priority',
                    )


class Equipment_Class_Form(forms.ModelForm):
    class Meta:
        model = Equipment_Class
        fields = (  'is_published', 'company',
                    'class_name_ru', 'class_name_en',                   # <- multiLang:16) now we can indicate model field
                    'short_description_ru', 'short_description_en',     # with different languages (next: create *app_name*/urls.py)
                    'full_description_ru', 'full_description_en',
                    )

    def __init__(self,user,*args, **kwargs): # <-- is what we do when class "Equipment_Class_Form "is start working
                    #  ^ "request.user" from views.py
        super(Equipment_Class_Form,self).__init__(*args, **kwargs)
        #       ^___________________^__in python 3. these arguments can be not defined, but it is better for backward compatibility
        if user.is_superuser != True: # <-- condition that only superuser can see and edit 'company' field
            del self.fields['company'] # <-- removing 'company' field from 'fields' (fields is dict)




class Equipment_Category_Form(forms.ModelForm):
    class Meta:
        model = Equipment_Category
        fields = (  'is_published', 'company','equipment_class',
                    'category_name_ru', 'category_name_en',
                    'short_description_ru', 'short_description_en',
                    'full_description_ru', 'full_description_en',
                    )

    def __init__(self,user,*args, **kwargs):
        super(Equipment_Category_Form,self).__init__(*args, **kwargs)

        if user.is_superuser == False:
            self.fields['equipment_class'].queryset = Equipment_Class.objects.filter(company=user.company_id) # <- filtered 'Equipment_Class'dsta by 'company_id'
            del self.fields['company']

        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        else:
             self.fields['equipment_class'].queryset = Equipment_Class.objects.none()

        if 'equipment_class' in self.data:
            try:
                company_id = int(self.data.get('company'))
                self.fields['equipment_class'].queryset = Equipment_Class.objects.filter(company_id=company_id).order_by('company')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        #-------------------------------------------------------------------------------------------------------------------------------------
        elif self.instance.slug: # <- "slug" (field of models.py) from views.py: "editable = Company(or another).objects.get(slug=data_slug)"
            self.fields['equipment_class'].queryset = self.instance.company.equipment_class_set.order_by('class_name')
            #                                                           ^        ^           ^--- "_set" means get set
            #                                                           |        '--- filtered on "equipment_class" set
            #                                                           '--- filtered on "company" set
            # https://www.youtube.com/watch?v=LmYDXgYK1so&list=LL&index=44&t=1452s <-- explanation on 25:30
        #-------------------------------------------------------------------------------------------------------------------------------------
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





class Equipment_Item_Form(forms.ModelForm):
    class Meta:
        model = Equipment_Item
        fields = (  'is_published', 'company','equipment_class', 'equipment_category',  #
                    'item_name_ru', 'item_name_en',
                    'short_description_ru', 'short_description_en',
                    'full_description_ru', 'full_description_en',
                    )

    def __init__(self,user,*args, **kwargs):
        super(Equipment_Item_Form,self).__init__(*args, **kwargs)

        if user.is_superuser == False:
            self.fields['equipment_class'].queryset = Equipment_Class.objects.filter(company=user.company_id)
            self.fields['equipment_category'].queryset = Equipment_Category.objects.filter(company=user.company_id)
            del self.fields['company']

        else:
             self.fields['equipment_class'].queryset = Equipment_Class.objects.none()
             self.fields['equipment_category'].queryset = Equipment_Category.objects.none()

        if 'equipment_class' in self.data:
            try:
                company_id = int(self.data.get('company'))
                self.fields['equipment_class'].queryset = Equipment_Class.objects.filter(company_id=company_id).order_by('company')
            except (ValueError, TypeError):
                pass
        elif self.instance.slug:
            self.fields['equipment_class'].queryset = self.instance.company.equipment_class_set.order_by('class_name')

         #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if 'equipment_category' in self.data:
            try:
                equipment_class_id = int(self.data.get('equipment_class'))
                self.fields['equipment_category'].queryset = Equipment_Category.objects.filter(equipment_class_id=equipment_class_id).order_by('equipment_class')
            except (ValueError, TypeError):
                pass
        elif self.instance.slug:
            self.fields['equipment_category'].queryset = self.instance.equipment_class.equipment_category_set.order_by('category_name')
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



class Equipment_Accessory_Form(forms.ModelForm):
    class Meta:
        model = Equipment_Accessory
        fields = (  'is_published', 'company','equipment',
                    'accessory_name_ru', 'accessory_name_en',
                    'short_description_ru', 'short_description_en',
                    'full_description_ru', 'full_description_en',
                    )
        widgets = {     # <-- create list of all avalible "many to many" connections
            'equipment': forms.CheckboxSelectMultiple,
        }

    def __init__(self,user,*args, **kwargs):
        super(Equipment_Accessory_Form,self).__init__(*args, **kwargs)

        if user.is_superuser == False:
            self.fields['equipment'].queryset = Equipment_Item.objects.filter(company=user.company_id)
            del self.fields['company']

