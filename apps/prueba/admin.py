from django.contrib import admin
from apps.prueba.models import User, Category, Favourite, Promotion, Commentary

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Favourite)
admin.site.register(Promotion)
admin.site.register(Commentary)