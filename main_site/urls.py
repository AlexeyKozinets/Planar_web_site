
from django.urls import path                                    # <- multiLang:17) import "path" and name of
from main_site import views                                     # views func (next: *app_name*/urls.py)

app_name = 'Main_site'                                          # <- multiLang:18) give a name to this app urls file
                                                                # like ("app_name=" var name is required) (next: *app_name*/urls.py)

urlpatterns = [                                                 # <- multiLang:19) make standart urlpatterns list
    path('', views.Home, name='home'),                          # (only developing urls) (next: *project_name*/urls.py)
    path('settings/add_<str:model_name>/', views.Add_data, name='add_data'),
    path('settings/<str:model_name>_edit_<slug:data_slug>/', views.Edit_data, name='edit_data'),
                    # ^_______________^___variables from edit_list.html, which relate with views.py
    path('settings_<str:modelId>/', views.Edit_list, name='edit_list'),
    path('sign/', views.Edit_list, name='edit_list'),
    path('news/', views.Companys_News, name='news_list'),
    path('news/<slug:news_slug>/', views.Company_News, name='news'),
    path('catalog/', views.Catalog_home, name='catalog_home'),
    path('catalog/<slug:company_slug>/', views.Catalog_classes, name='catalog_classes'),
    path('catalog/<slug:company_slug>/<slug:class_slug>/', views.Catalog_categories, name='catalog_categories'),
    path('catalog/<slug:company_slug>/<slug:class_slug>/<slug:category_slug>/', views.Catalog_items, name='catalog_items'),
    path('catalog/<slug:company_slug>/<slug:class_slug>/<slug:category_slug>/<slug:item_slug>/', views.Catalog_item, name='catalog_item'),
]


urlpatterns += [
    path('ajax/load-classes/', views.load_classes, name='ajax_load_classes'), # AJAX
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'), # AJAX
]