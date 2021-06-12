from django.contrib import admin
from home.models import Publicaciones, Contacto, RedesSociales

# Register your models here.
class PublicacionesDisplay(admin.ModelAdmin):
    list_display = ['titulo']
    list_filter = ('titulo',)

class ContactoDisplay(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'fecha']
    list_filter = ('nombre', 'email', 'fecha')

class RedesDisplay(admin.ModelAdmin):
    list_display = ['nombre', 'link']
    list_filter = ('nombre', 'link')

admin.site.register(Publicaciones, PublicacionesDisplay)
admin.site.register(Contacto, ContactoDisplay)
admin.site.register(RedesSociales, RedesDisplay)