from django.contrib import admin
from .models import ServiceModel, WorkExampleModel, ImagesModel
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class ImagesInline(NestedStackedInline):
    model = ImagesModel
    extra = 0


class WorkExampleInline(NestedStackedInline):
    model = WorkExampleModel
    extra = 0
    inlines = [ImagesInline]


class ServiceAdmin(NestedModelAdmin):
    list_display = ('title', 'min_price', 'description')
    inlines = [WorkExampleInline]


admin.site.register(ServiceModel, ServiceAdmin)
