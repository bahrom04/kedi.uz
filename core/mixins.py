from modeltranslation.translator import translator

from django.conf import settings
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class TabbedTranslationMixin:
    def get_fieldsets(self, request, obj=None):
        if self.model not in translator._registry:
            return super().get_fieldsets(request, obj)
        non_translated_fields = []
        translated_fields = []
        excludes = self.get_exclude(request, obj) or tuple()
        for field in self.get_fields(request, obj):
            if field in excludes:
                continue
            if field in translator._registry[self.model].fields:
                translated_fields.append(field)
            elif all(not field.endswith(lang[0]) for lang in settings.LANGUAGES):
                non_translated_fields.append(field)
        fieldsets = tuple()
        if non_translated_fields:
            fieldsets += ((_("General "), {"fields": non_translated_fields}),)
        for language in settings.LANGUAGES:
            fieldsets += ((language[1], {"fields": list(map(lambda x: x + "_" + language[0], translated_fields))}),)
        return fieldsets


class TabbedTranslationAdmin(TabbedTranslationMixin, admin.ModelAdmin):
    pass


class TranslationRequiredMixin:
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in settings.LANGUAGES:
                form.base_fields[value].required = True
        return form

