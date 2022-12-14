from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from users.models import CustomUser
from .eq_forms import ( Company_Form,
                        Equipment_Class_Form,
                        Equipment_Category_Form,
                        Equipment_Item_Form,
                        Equipment_Accessory_Form,
                        News_Form,
                        News_Images_Form,
                        Contacts_Form,
                    )
from .models import  (  Company,
                        Equipment_Class,
                        Equipment_Category,
                        Equipment_Item,
                        Equipment_Accessory,
                        News,
                        News_Images,
                        Contacts,
                    )


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
        elif model_name == Contacts.__name__:
            form = Contacts_Form(request.user)
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
            elif model_name == Contacts.__name__:
                form = Contacts_Form(request.user,request.POST, request.FILES)
                modelId=6 if request.user.is_superuser == False else 8
            #_______________________________________________________________)

            if form.is_valid():
                new_data = form.save(commit=False)

                if request.user.is_superuser == False:
                    new_data.company = request.user.company # <- auto set of "company" field if user in not superuser(admin)

                new_data.save()

                if model_name == Equipment_Accessory.__name__:
                    form.save_m2m()     # <-- saving "many to many" fields (must be final step of savin the form)

                return redirect(reverse('Main_site:edit_list', kwargs={ 'modelId': modelId })) #add modelId to request.path

        context = {'form':form}

        return render(request, 'add_data.html', context)
    else:
        return redirect('Main_site:catalog_home')




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
        elif model_name == Contacts.__name__:
            editable = Contacts.objects.get(slug=data_slug)
            form = Contacts_Form(request.user,instance=editable)
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
            elif model_name == Contacts.__name__:
                form = Contacts_Form(request.user,request.POST, request.FILES, instance=editable)
                modelId=6 if request.user.is_superuser == False else 8
            #_______________________________________________________________)

            if form.is_valid():
                upd_data = form.save(commit=False)

                if request.user.is_superuser == False:
                    upd_data.company = request.user.company

                upd_data.save()

                if model_name == Equipment_Accessory.__name__:
                    form.save_m2m()

                return redirect(reverse('Main_site:edit_list', kwargs={ 'modelId': modelId })) #adds modelId to request.path
                # return redirect('Main_site:edit_list')

        context = {'form':form}

        return render(request, 'add_data.html', context)
    else:
        return redirect('Main_site:catalog_home')






def Add_news(request):
    if request.user.is_authenticated:
        form = News_Form(request.user)
        form2 = News_Images_Form()
        if request.method == 'POST':
            form = News_Form(request.user,request.POST, request.FILES)
            form2 = News_Images_Form(request.POST, request.FILES)
            images = request.FILES.getlist('additional_imgs')
            modelId=5 if request.user.is_superuser == False else 7
            if form.is_valid() and form2.is_valid():
                add_news_data = form.save(commit=False)
                if request.user.is_superuser == False:
                    add_news_data.company = request.user.company
                add_news_data.issued = datetime.now()
                add_news_data.save()
                for image in images:
                    News_Images.objects.create(news = add_news_data, additional_imgs = image)
                return redirect(reverse('Main_site:edit_list', kwargs={ 'modelId': modelId }))
        context = { 'form':form,
                    'form2':form2,
                    }
        return render(request, 'add_news.html', context)
    else:
        return redirect('Main_site:catalog_home')



def Edit_news(request,news_slug):
    if request.user.is_authenticated:
        news_editable = News.objects.get(slug=news_slug)
        news_imgs_editable = News_Images.objects.filter(news__slug=news_slug)
        form = News_Form(request.user,instance=news_editable)
        form2 = News_Images_Form()
        if request.method == 'POST':
            form = News_Form(request.user,request.POST, request.FILES, instance=news_editable)
            form2 = News_Images_Form()
            images = request.FILES.getlist('additional_imgs')
            modelId=5 if request.user.is_superuser == False else 7
            if form.is_valid():
                upd_news_data = form.save(commit=False)
                if request.user.is_superuser == False:
                    upd_news_data.company = request.user.company
                upd_news_data.issued = datetime.now()
                upd_news_data.save()
                if images:
                    News_Images.objects.filter(news__slug=news_slug).delete()
                for image in images:
                    News_Images.objects.create(news = upd_news_data, additional_imgs = image)
                return redirect(reverse('Main_site:edit_list', kwargs={ 'modelId': modelId }))
        context = { 'form':form,
                    'form2':form2,
                    }
        return render(request, 'add_news.html', context)
    else:
        return redirect('Main_site:catalog_home')








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
        News,
        Contacts,
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
            elif data[0] == 'News':
                data[2] = data[2].order_by('company__priority', 'issued', )


        context = { 'mod_list': models_list,
                    }

        return render(request, 'edit_list.html', context)
    else:
        return redirect('Main_site:catalog_home')
                        # ^___________________________ name of path in *app*.urls.py

#============================= SETTINGS =============================




#============================= CATALOG =============================

def Catalog_home(request):
    companies = Company.objects.filter(is_published=True).order_by('priority',)
    classes = Equipment_Class.objects.filter(is_published=True).order_by('class_name',)
    accessories = [Equipment_Accessory.objects.filter(is_published=True, company=i,).order_by('id', ) for i in companies]
    context = { 'classes_list' : classes,
                'companies_list': companies,
                'accessories_list' : accessories,
                }
    return render(request, 'catalog_home.html', context)


def Catalog_classes(request, company_slug):
    classes = Equipment_Class.objects.filter(company__slug=company_slug).order_by('class_name', )
    accessories = Equipment_Accessory.objects.filter(is_published=True, company__slug=company_slug,).order_by('accessory_name', )
    context = { 'classes_list' : classes,
                'accessories_list' : accessories,
                }
    return render(request, 'catalog_classes.html', context)

def Catalog_categories(request, company_slug, class_slug):
    categories = Equipment_Category.objects.filter(equipment_class__slug=class_slug).order_by('category_name', )
    context = {'categories_list' : categories,}
    return render(request, 'catalog_categories.html', context)


def Catalog_items(request, company_slug, class_slug, category_slug):
    items = Equipment_Item.objects.filter(equipment_category__slug=category_slug).order_by('item_name', )
    context = {'items_list' : items,}
    return render(request, 'catalog_items.html', context)


def Catalog_item(request, company_slug, class_slug, category_slug, item_slug):
    item = Equipment_Item.objects.get(slug=item_slug)
    accessories = Equipment_Accessory.objects.filter(equipment__slug=item_slug).order_by('accessory_name', )
    context = { 'item' : item,
                'accessories_list':accessories
                }
    return render(request, 'catalog_item.html', context)


def Catalog_accessories(request, company_slug):
    accessories = Equipment_Accessory.objects.filter(company__slug=company_slug, is_published=True).order_by('accessory_name', )
    context = {'accessories_list' : accessories,}
    return render(request, 'catalog_accessories.html', context)


def Catalog_accessory(request, company_slug, accessory_slug):

    accessory = Equipment_Accessory.objects.get(slug=accessory_slug)
    context = {'accessory' : accessory,}
    return render(request, 'catalog_accessory.html', context)


#============================= CATALOG =============================



#============================= NEWS =============================

def Companys_News(request):
    news_list = News.objects.filter(company__is_published=True, is_published=True).order_by('-issued')
    page = request.GET.get('page',1)
    paginator = Paginator(news_list,2)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    context = {'pages': pages}
    return render(request, 'news_list.html', context)


def Company_News(request, news_slug):
    news = News.objects.get(slug = news_slug)
    multiple_imgs = News_Images.objects.filter(news__slug = news_slug)
    context = { 'news': news,
                'multiple_imgs' : multiple_imgs
                }
    return render(request,'news.html', context )

#============================= NEWS =============================


#============================= CONTACTS =============================

def Contacts_data(request):
    contacts = Contacts.objects.all().order_by('company__priority')
    context = {
        'contacts':contacts
    }
    return render(request, 'contacts.html', context)

#============================= CONTACTS =============================