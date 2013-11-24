from django.contrib import admin

from raas.models import DomainConfig
from raas.models import DocumentFile


class DomainConfigAdmin(admin.ModelAdmin):
    list_display = ('user', 'domain', 'number_of_rec', 'filename', 'created', 'updated')
    list_display_links = ('domain',)
    ordering = ['user', 'domain']


class DocumentFileAdmin(admin.ModelAdmin):
    list_display = ('domain', 'file', 'created', 'updated', 'status')
    list_display_links = ('domain',)
    ordering = ['domain']

    def assoc_domain(self, obj):
        return '%s' % (obj.domain.domain)
    assoc_domain.short_description = 'Domain'

admin.site.register(DomainConfig, DomainConfigAdmin)
admin.site.register(DocumentFile, DocumentFileAdmin)

