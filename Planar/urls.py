
from django.conf.urls.i18n import i18n_patterns                     # <- multiLang:20) import "i18n_patterns","admin",
from django.contrib import admin                                    # "path" and " include" (next: *project_name*/urls.py)
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += i18n_patterns(                                       # <- multiLang:21) add to the "urlpatterns" i18n_patterns()
    path('', include('main_site.urls', namespace='Main_site')),     # which will include urls from *app_name*/urls.py ["namespace="
    path('', include('users.urls', namespace='Users')),             # is required (name of app urls {step:16})] and "i18n/" path
    path('i18n/', include('django.conf.urls.i18n')),                # (this add http://.../*lang*/app_urls/, but "admin/" path
)                                                                   # will not have http://.../*lang(ru,en,fr,...)*/admin/ )
                                                                    # (next: *project_name*/urls.py)

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]


                                                                    # multiLang:22) in templates instead {% url 'urls_name' i.0 %}
                                                                    # need write {% url '*urls_app_name*:urls_name' i.0 %}
                                                                    # for example:
                                                                    # {% url 'add_data' i.0 %} -> {% url 'Main_site:add_data' i.0 %}
                                                                    # (next: *project_name*/urls.py)

                                                                    # multiLang:23) form for language choosing is in base.html and
                                                                    # (next: *project_name*/urls.py)

                                                                    # multiLang:24) for new models or new fields need te repeat
                                                                    # steps: 7 - 17 (end)