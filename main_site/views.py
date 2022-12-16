from django.shortcuts import render, redirect, get_object_or_404
from .eq_forms import Equipment_Class_Form, Equipment_Category_Form, Equipment_Item_Form, Equipment_Acessory_Form
from .models import Equipment_Class, Equipment_Category, Equipment_Item, Equipment_Acessory
from django.urls import reverse



def Home(request):
    #       ^ ___________________________________________ httpRequest object that contains metadata about the request
    return render(request, 'base.html')



def Add_data(request,model_name):
    #                   ^ _______________________________ created argument, which come from edit_list.html thru urls.py
    if str(request.user) != 'AnonymousUser':            # checking in case that user is not log in

        #_______________________________________________________________(
        if model_name == Equipment_Class._meta.verbose_name_plural:     # <-- cheking the name of the model to add data to
            form = Equipment_Class_Form(request.user)                   # <-- "request.user" go to forms.py in def __init__()
                                                                        # of "Equipment_Class_Form"
            # as "user" to set condition to render of fields (means 'company' field) to users and admin
        elif model_name == Equipment_Category._meta.verbose_name_plural:
            form = Equipment_Category_Form(request.user)
        elif model_name == Equipment_Item._meta.verbose_name_plural:
            form = Equipment_Item_Form(request.user)
        elif model_name == Equipment_Acessory._meta.verbose_name_plural:
            form = Equipment_Acessory_Form(request.user)
        #_______________________________________________________________)

        if request.method == 'POST':
            #_______________________________________________________________(
            if model_name == Equipment_Class._meta.verbose_name_plural:
                form = Equipment_Class_Form(request.user,request.POST, request.FILES)
                modelId=1
            elif model_name == Equipment_Category._meta.verbose_name_plural:
                form = Equipment_Category_Form(request.user,request.POST, request.FILES)
                modelId=2
            elif model_name == Equipment_Item._meta.verbose_name_plural:
                form = Equipment_Item_Form(request.user,request.POST, request.FILES)
                modelId=3
            elif model_name == Equipment_Acessory._meta.verbose_name_plural:
                form = Equipment_Acessory_Form(request.user,request.POST, request.FILES)
                modelId=4
            #_______________________________________________________________)

            if form.is_valid():
                new_data = form.save(commit=False)
                if request.user.is_superuser == False:
                    new_data.company = request.user.company             # <- auto set of "company" field if user in not superuser(admin)
                new_data.save()
                if model_name == Equipment_Acessory._meta.verbose_name_plural:
                    form.save_m2m()     # <-- saving "many to many" fields (must be final step of savin the form)

                return redirect(reverse('Main_site:edit_list', kwargs={ 'modelId': modelId })) #add modelId to request.path

        context = {'form':form}

        return render(request, 'add_data.html', context)
    else:
        return redirect('Main_site:home')




def Edit_data(request,model_name,pk):
    #                   ^_________^ _____________________________________ created arguments, which come from edit_list.html thru urls.py
    if str(request.user) != 'AnonymousUser':
        #_______________________________________________________________(
        if model_name == Equipment_Class._meta.verbose_name_plural:
            editable = Equipment_Class.objects.get(id=pk)               # <- !! change on get_object_or_404(Equipment_Category, id=pk)
            form = Equipment_Class_Form(request.user,instance=editable) # <- 'instace=editable' puts existing data into the form
        elif model_name == Equipment_Category._meta.verbose_name_plural:
            editable = Equipment_Category.objects.get(id=pk)
            form = Equipment_Category_Form(request.user,instance=editable)
        elif model_name == Equipment_Item._meta.verbose_name_plural:
            editable = Equipment_Item.objects.get(id=pk)
            form = Equipment_Item_Form(request.user,instance=editable)
        elif model_name == Equipment_Acessory._meta.verbose_name_plural:
            editable = Equipment_Acessory.objects.get(id=pk)
            form = Equipment_Acessory_Form(request.user,instance=editable)
            #_______________________________________________________________)

        if request.method == 'POST':
            #_______________________________________________________________(
            if model_name == Equipment_Class._meta.verbose_name_plural:
                form = Equipment_Class_Form(request.user,request.POST, request.FILES, instance=editable)
                modelId=1
            elif model_name == Equipment_Category._meta.verbose_name_plural:
                form = Equipment_Category_Form(request.user,request.POST, request.FILES, instance=editable)
                modelId=2
            elif model_name == Equipment_Item._meta.verbose_name_plural:
                form = Equipment_Item_Form(request.user,request.POST, request.FILES, instance=editable)
                modelId=3
            elif model_name == Equipment_Acessory._meta.verbose_name_plural:
                form = Equipment_Acessory_Form(request.user,request.POST, request.FILES, instance=editable)
                modelId=4
            #_______________________________________________________________)

            if form.is_valid():
                upd_data = form.save(commit=False)
                if request.user.is_superuser == False:
                    upd_data.company = request.user.company
                upd_data.save()
                if model_name == Equipment_Acessory._meta.verbose_name_plural:
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
        Equipment_Class,
        Equipment_Category,
        Equipment_Item,
        Equipment_Acessory,
        ]

    if str(request.user) != 'AnonymousUser':        # checking in case that user is not log in
    #   ^____________________________________________ crutch! need to know how get 'AnonymousUser' without string converting
        if request.user.is_superuser == False:      # checking in case that user is not admin and data is need to be filtered

            models_list = [[i._meta.verbose_name_plural, i.objects.filter(company=request.user.company)] for i in models]
            #   |               ^_____________________ ref to the meta class in models.py
            #   |
            # models_list = [
            #                   [class_name, <filtered_class_names_set>],
            #                   [cat_name, <filtered_cat_names_set>],
            #                   [item_name, <filtered_item_names_set>],
            #                   ....,
            #                   ]
        else:
            models_list = [[i._meta.verbose_name_plural, i.objects.all()] for i in models]
            # models_list = [
            #                   [class_name, <all_class_names_set>],
            #                   [cat_name, <all_cat_names_set>],
            #                   [item_name, <all_item_names_set>],
            #                   ....,
            #                   ]

        context = { 'mod_list': models_list,
                    }

        return render(request, 'edit_list.html', context)
    else:
        return redirect('Main_site:home')
                        # ^___________________________ name of path in urls.py
