from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(label='Nombre del Curso', max_length=50, required=True)
    comision = forms.IntegerField(label='Comision', required=True)
    nombreAlumno = forms.CharField(label='Nombre del Alumno', max_length=50, required=True)
    
class ArticuloForm(forms.Form):
    nombre = forms.CharField(label='Nombre del Articulo', max_length=50, required=True)
    marca = forms.CharField(label='Marca', max_length=50, required=True)
    modelo = forms.CharField(label='Modelo', max_length=50, required=True)
    origen = forms.CharField(label='Origen', max_length=50, required=True)
    
class PartnerForm(forms.Form):
    nombre = forms.CharField(label='Nombre del Partner', max_length=50, required=True)
    antiguedad = forms.IntegerField(label='Año de asociacion', required=True)
    
class OfertaForm(forms.Form):
    nombre = forms.CharField(label='Nombre del Articulo', max_length=50, required=True)
    marca = forms.CharField(label='Marca del Articulo', max_length=50, required=True)
    modelo = forms.CharField(label='Modelo del Articulo', max_length=50, required=True)
    descuentoEspecial = forms.CharField(label='Porcentaje de descuento', max_length=50, required=True)