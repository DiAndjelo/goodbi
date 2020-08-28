from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from core.models import Passenger


class PassengerResource(resources.ModelResource):
    class Meta:
        model = Passenger


class PassengerAdmin(ImportExportModelAdmin):
    resource_class = PassengerResource


admin.site.register(Passenger, PassengerAdmin)
