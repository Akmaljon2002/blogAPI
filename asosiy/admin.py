from django.contrib import admin
from .models import *

class MaqolaAdmin(admin.ModelAdmin):
    readonly_fields = ('korilganlik',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Eski obyekt tahrirlanayotganida
            return self.readonly_fields
        return self.readonly_fields

admin.site.register(Maqola, MaqolaAdmin)
admin.site.register(Murojaat)