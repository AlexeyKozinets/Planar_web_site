
from django.urls import path                                    # <- multiLang:17) import "path" and name of
from main_site import views                                     # views func (next: *app_name*/urls.py)

app_name = 'Main_site'                                          # <- multiLang:18) give a name to this app urls file
                                                                # like ("app_name=" var name is required) (next: *app_name*/urls.py)

urlpatterns = [                                                 # <- multiLang:19) make standart urlpatterns list
    path('', views.Home, name='home'),                          # (only developing urls) (next: *project_name*/urls.py)
    path('list/<str:model_name>:add/', views.Add_data, name='add_data'),
    path('list/<str:model_name>:<slug:data_slug>/', views.Edit_data, name='edit_data'),
                    # ^_______________^___variables from edit_list.html, which relate with views.py
    path('list_default:<str:modelId>/', views.Edit_list, name='edit_list'),
]


urlpatterns += [
    path('ajax/load-classes/', views.load_classes, name='ajax_load_classes'), # AJAX
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'), # AJAX
]