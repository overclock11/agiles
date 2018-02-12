from django.contrib import admin
from apps.promociones.models import User, Category, Favourite, Promotion, Commentary
from django.contrib.admin import AdminSite
from apps.promociones.views import update_profile

# Register your models here.

class PromotionsAdminSite(AdminSite):
    def get_urls(self):
        from django.conf.urls import url
        urls = super(PromotionsAdminSite, self).get_urls()
        # Note that custom urls get pushed to the list (not appended)
        # This doesn't work with urls += ...
        urls = [
            url(r'^profile/$', self.admin_view(update_profile))
        ] + urls
        return urls

admin_site = PromotionsAdminSite()
admin_site.register(Category)
admin_site.register(Favourite)
admin_site.register(Promotion)
admin_site.register(Commentary)

