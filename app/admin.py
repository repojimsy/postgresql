from django.contrib import admin
from app.models import Alumnos, Cursos, Docentes

class alumno_admin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'curso')
    list_filter = ('nombre',)

class curso_admin(admin.ModelAdmin):
    list_display = ('nombre', 'modalidad')
    list_filter = ('nombre',)

class docente_admin(admin.ModelAdmin):
    list_display = ('nombre','pais','correo')
    list_filter = ('pais',)


# Register your models here.
admin.site.register(Alumnos, alumno_admin)
admin.site.register(Cursos, curso_admin)
admin.site.register(Docentes, docente_admin)
