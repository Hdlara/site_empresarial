from django.contrib import admin

from .models import Cargo, Curso, Pessoa, Tecnologia, Expectativa, Experiencia

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'curso', 'icone', 'ativo', 'modificado')

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tecnologia', 'descricao', 'icone', 'ativo', 'modificado')

@admin.register(Expectativa)
class ExpectativaAdmin(admin.ModelAdmin):
    list_display = ('horario', 'modalidade', 'area', 'icone', 'ativo', 'modificado')

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'modalidade', 'cargo', 'periodoi', 'periodof', 'atividades', 'imagem', 'ativo', 'modificado')