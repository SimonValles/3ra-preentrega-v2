from django.contrib import admin
from .models import Articulo, Partner, Oferta, Curso

# Register your models here.
admin.site.register(Articulo)
admin.site.register(Partner)
admin.site.register(Oferta)
admin.site.register(Curso)