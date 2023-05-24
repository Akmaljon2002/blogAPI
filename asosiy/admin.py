from django.contrib import admin
from .models import *

class MaqolaAdmin(admin.ModelAdmin):
    readonly_fields = ('korilganlik',)
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Eski obyekt tahrirlanayotganida
            return self.readonly_fields
        return self.readonly_fields
    list_display = ("id", "sarlavha", "sana", "bosh_sahifa_uchun", "korilganlik")
    search_fields = ("sarlavha", "sarlavhaeng", "sarlavharu")
    list_editable = ("bosh_sahifa_uchun", )
    list_display_links = ("sarlavha", )
    list_filter = ("sarlavha", "id", "bosh_sahifa_uchun")
admin.site.register(Maqola, MaqolaAdmin)



admin.site.register(Murojaat)
admin.site.register(Menu)

class Home_pageAdmin(admin.ModelAdmin):
    search_fields = ("ism", "ismru")
admin.site.register(Home_page, Home_pageAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ("url",)


admin.site.register(Video, VideoAdmin)
admin.site.register(Ijtimoiy_tarmoq_url)
admin.site.register(Haqida_toliq)
admin.site.register(Faoliyat_joy)
admin.site.register(Hamkor)
