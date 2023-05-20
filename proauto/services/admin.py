from django.contrib import admin
from .models import ServiceModel, WorkExampleModel, ImagesModel
# from nested_inline.admin import NestedStackedInline, NestedModelAdmin
import nested_admin

class ImagesInline(nested_admin.NestedStackedInline):
    model = ImagesModel
    extra = 0


class WorkExampleInline(nested_admin.NestedStackedInline):
    model = WorkExampleModel
    extra = 0
    inlines = [ImagesInline]


class ServiceAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title', 'min_price', 'description')
    inlines = [WorkExampleInline]


admin.site.register(ServiceModel, ServiceAdmin)
