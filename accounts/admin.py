from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from vira.Model.CancerType import CancerType

admin.site.site_header = 'Berktug Kullanici Yönetim Paneli '  # default: "Django Administration"
admin.site.index_title = 'Sistem Yönetimi'  # default: "Site administration"
admin.site.site_title = 'Admin'  # default: "Django site admin"


app_models = apps.get_app_config('vira').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass

# admin.site.register(CancerType)

