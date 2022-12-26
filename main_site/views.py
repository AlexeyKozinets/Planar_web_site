from django.shortcuts import render, redirect, get_object_or_404
from .eq_forms import Company_Form, Equipment_Class_Form, Equipment_Category_Form, Equipment_Item_Form, Equipment_Accessory_Form
from .models import  Company, Equipment_Class, Equipment_Category, Equipment_Item, Equipment_Accessory
from django.urls import reverse
from users.models import CustomUser



def Home(request):
    #       ^ ___________________________________________ httpRequest object that contains metadata about the request
    return render(request, 'base.html')

#============================= SETTINGS =============================

def Add_data(request,model_name):

    #                   ^ _______________________________ created argument, which come from edit_list.html thru urls.py
    if request.user.is_authenticated:               # checking in case that user is not log in

        #_______________________________________________________________(
        if model_name == Company.__name__:
            form = Company_Form()
        elif model_name == Equipment_Class.__name__:     # <-- cheking the name of the model to add data to
            form = Equipment_Class_Form(request.user)                   # <-- "request.user" go to forms.py in def __init__()
                                                                        # of "Equipment_Class_Form"
            # as "user" to set condition to render of fields (means 'company' field) to users and admin
        elif model_name == Equipment_Category.__name__:
            form = Equipment_Category_Form(request.user)
        elif model_name == Equipment_Item.__name__:
            form = Equipment_Item_Form(request.user)
        elif model_name == Equipment_Accessory.__name__:
            form = Equipment_Accessory_Form(request.user)
        #_______________________________________________________________)

        if request.method == 'POST':
            #_______________________________________________________________(
            if model_name == Company.__name__:
                form = Company_Form(request.POST, request.FILES)
                modelId=1 if request.user.is_superuser == False else 2
            elif model_name == Equipment_Class.__name__:
                form = Equipment_Class_Form(request.user,request.POST, request.FILES)
                modelId=1 if request.user.is_superuser == False else 3
            elif model_name == Equipment_Category.__name__:
                form = Equipment_Category_Form(request.user,request.POST, request.FILES)
                modelId=2 if request.user.is_superuser == False else 4
            elif model_name == Equipment_Item.__name__:
                form = Equipment_Item_Form(request.user,request.POST, request.FILES)
                modelId=3 if request.user.is_superuser == False else 5
            elif model_name == Equipment_Accessory.__name__:
                form = Equipment_Accessory_Form(request.user,request.POST, request.FILES)
                modelId=4 if request.user.is_superuser == False else 6
            #_______________________________________________________________)

            if form.is_valid():
                new_data = form.save(commit=False)
                if request.user.is_superuser == False:
                    new_data.company = request.user.company             # <- auto set of "company" field if user in not superuser(admin)
                new_data.save()
                if model_name == Equipment_Accessory.__name__:
                    form.save_m2m()     # <-- saving "many to many" fields (must be final step of savin the form)

                return redirect(reverse('Main_site:edit_list', kwargs={ 'modelId': modelId })) #add modelId to request.path

        context = {'form':form}

        return render(request, 'add_data.html', context)
    else:
        return redirect('Main_site:home')




def Edit_data(request,model_name,data_slug):
    #                   ^_________^ _____________________________________ created arguments, which come from edit_list.html thru urls.py
    if request.user.is_authenticated:
        #_______________________________________________________________(
        if model_name == Company.__name__:
            editable = Company.objects.get(slug=data_slug)
            form = Company_Form(instance=editable)
        elif model_name == Equipment_Class.__name__ :
            editable = Equipment_Class.objects.get(slug=data_slug)               # <- !! change on get_object_or_404(Equipment_Category, id=pk)
            form = Equipment_Class_Form(request.user,instance=editable) # <- 'instace=editable' puts existing data into the form
        elif model_name == Equipment_Category.__name__:
            editable = Equipment_Category.objects.get(slug=data_slug)
            form = Equipment_Category_Form(request.user,instance=editable)
        elif model_name == Equipment_Item.__name__:
            editable = Equipment_Item.objects.get(slug=data_slug)
            form = Equipment_Item_Form(request.user,instance=editable)
        elif model_name == Equipment_Accessory.__name__:
            editable = Equipment_Accessory.objects.get(slug=data_slug)
            form = Equipment_Accessory_Form(request.user,instance=editable)
        else:
             return redirect('Main_site:home')
            #_______________________________________________________________)

        if request.method == 'POST':
            #_______________________________________________________________(
            if model_name == Company.__name__ and request.user.is_superuser:
                form = Company_Form(request.POST, request.FILES, instance=editable)
                modelId=1 if request.user.is_superuser == False else 2
            elif model_name == Equipment_Class.__name__:
                form = Equipment_Class_Form(request.user,request.POST, request.FILES, instance=editable)
                modelId=1 if request.user.is_superuser == False else 3
            elif model_name == Equipment_Category.__name__:
                form = Equipment_Category_Form(request.user,request.POST, request.FILES, instance=editable)
                modelId=2 if request.user.is_superuser == False else 4
            elif model_name == Equipment_Item.__name__:
                form = Equipment_Item_Form(request.user,request.POST, request.FILES, instance=editable)
                modelId=3 if request.user.is_superuser == False else 5
            elif model_name == Equipment_Accessory.__name__:
                form = Equipment_Accessory_Form(request.user,request.POST, request.FILES, instance=editable)
                modelId=4 if request.user.is_superuser == False else 6
            #_______________________________________________________________)

            if form.is_valid():
                upd_data = form.save(commit=False)
                if request.user.is_superuser == False:
                    upd_data.company = request.user.company
                upd_data.save()
                if model_name == Equipment_Accessory.__name__:
                    form.save_m2m()
                return redirect(reverse('Main_site:edit_list', kwargs={ 'modelId': modelId })) #add modelId to request.path
                # return redirect('Main_site:edit_list')

        context = {'form':form}

        return render(request, 'add_data.html', context)
    else:
        return redirect('Main_site:home')

#++++++++++++++++++++++++++++++++++++++++++
def load_classes(request):
    company_id = request.GET.get('company_id')
    cLasses = Equipment_Class.objects.filter(company_id=company_id)
    return render(request, 'class_dropdown_list_options.html', {'cLasses': cLasses})
#++++++++++++++++++++++++++++++++++++++++++


#++++++++++++++++++++++++++++++++++++++++++
def load_categories(request):
    equipment_class_id = request.GET.get('class_id')
    cAtegories = Equipment_Category.objects.filter(equipment_class_id=equipment_class_id)
    return render(request, 'category_dropdown_list_options.html', {'cAtegories': cAtegories})
#++++++++++++++++++++++++++++++++++++++++++


def Edit_list(request, modelId):
    models = [
        CustomUser,
        Company,
        Equipment_Class,
        Equipment_Category,
        Equipment_Item,
        Equipment_Accessory,
    ]


    if request.user.is_superuser == False:
        selected_models = models[2:]

    if request.user.is_authenticated:        # checking in case that user is not log in

        if request.user.is_superuser == False:      # checking in case that user is not admin and data is need to be filtered
            models_list = [[i.__name__, i._meta.verbose_name_plural, i.objects.filter(company=request.user.company)] for i in selected_models]
            #   |             ^_model_name   ^_____________________ ref to the meta class in models.py
            #   |
            # models_list = [
            #                   [model_name,    class_metaVerboseName,  <filtered_class_names_set>],
            #                   [cat_name,      cat_metaVerboseName,    <filtered_cat_names_set>],
            #                   [item_name,     item_metaVerboseName,   <filtered_item_names_set>],
            #                   ....,
            #                   ]
        else:
            models_list = [[i.__name__, i._meta.verbose_name_plural, i.objects.all()] for i in models]  # need change all models names fields on "name"
            # models_list = [                                                                           # instead "company_name", "class_name", etc
            #                   [model_name,    class_metaVerboseName,  <all_class_names_set>],
            #                   [cat_name,      cat_metaVerboseName,    <all_cat_names_set>],
            #                   [item_name,     item_metaVerboseName,   <all_item_names_set>],
            #                   ....,
            #                   ]


        for data in models_list: #<- smart sorting
            if data[0] == 'CustomUser':
                data[2] = data[2].order_by('company__priority', 'username', )
            elif data[0] == 'Company':
                data[2] = data[2].order_by('priority')
            elif data[0] == 'Equipment_Class':
               data[2] = data[2].order_by('company__priority', 'class_name', )
            elif data[0] == 'Equipment_Category':
                data[2] = data[2].order_by('company__priority', 'equipment_class', 'category_name', )
            elif data[0] == 'Equipment_Item':
                data[2] = data[2].order_by('company__priority', 'equipment_class', 'equipment_category', 'item_name', )
            elif data[0] == 'Equipment_Accessory':
                data[2] = data[2].order_by('company__priority', 'accessory_name', )


        context = { 'mod_list': models_list,
                    }

        return render(request, 'edit_list.html', context)
    else:
        return redirect('Main_site:home')
                        # ^___________________________ name of path in *app*.urls.py

#============================= SETTINGS =============================




#============================= CATALOG =============================

def Catalog_home(request):
    companies = Company.objects.all().order_by('priority',)
    classes = Equipment_Class.objects.all().order_by('class_name',)
    context = { 'classes_list' : classes,
                'companies_list': companies,
                }
    return render(request, 'catalog_home.html', context)



def Catalog_categories(request, slug1):
    categories = Equipment_Category.objects.filter(equipment_class__slug=slug1).order_by('category_name', )
    context = {'categories_list' : categories,}
    return render(request, 'catalog_categories.html', context)



def Catalog_items(request, slug1, slug2):
    items = Equipment_Item.objects.filter(equipment_category__slug=slug2).order_by('item_name', )
    context = {'items_list' : items,}
    return render(request, 'catalog_items.html', context)


def Catalog_item(request, slug1, slug2, slug3):
    item = Equipment_Item.objects.get(slug=slug3)
    accessories = Equipment_Accessory.objects.filter(equipment__slug=slug3).order_by('accessory_name', )
    context = { 'item' : item,
                'accessories_list':accessories
                }
    return render(request, 'catalog_item.html', context)


#============================= CATALOG =============================