from django import forms
from django.forms import ModelForm
from models import Categoria, Enlace

class EnlaceForm(ModelForm):
	class Meta:
		model = Enlace
		exclude = ("votos", "usuario", )

#class CategoriaForm(ModelForm):
#	class Meta:
#		model = Categoria