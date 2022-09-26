from django.contrib import admin
from .models import Usuario

# Register your models here.

class usuarioAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'cpf', 'data_nascimento', 'endereco', 'email']
    search_fields = ['nome_completo']

admin.site.register(Usuario, usuarioAdmin)