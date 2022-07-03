from django.contrib import admin
from .models import Cursos
from .models import MensajeUsuario

# Register your models here.

class AdminModel(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'mensaje')
    readonly_fields = ('created', 'updated')
    search_fields = ('id', 'nombre', 'mensaje')
    date_hierarchy = 'created'
    list_filter = ('id', 'nombre')
    ordering = ('nombre',)
    list_display_links = ('nombre', 'id',)

admin.site.register(Cursos, AdminModel)

class AdministrarMensajesUsuarios(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'mensaje')
    search_fields = ('id', 'curso')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    list_filter = ('id', 'curso', 'email')
    ordering = ('id',)
    list_display_links = ('nombre', 'id',)

admin.site.register(MensajeUsuario, AdministrarMensajesUsuarios)