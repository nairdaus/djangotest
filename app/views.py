from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import Context
from django.template.context import RequestContext
from django.template.loader import get_template
from forms import EnlaceForm
from models import Categoria, Enlace

def singin_form(request):
	if  not request.user.is_anonymous:
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario           = request.POST['username']
			clave             = request.POST['password']
			user_authenticate = authenticate(username=usuario, password=clave)
			if user_authenticate is not None:
				if user_authenticate.is_active:
					login(request, user_authenticate)
					return HttpResponseRedirect('/')
				else:
					return render_to_response('index.html', context_instance=RequestContext(request))
			else:
				return render_to_response('index.html', context_instance=RequestContext(request))
	else:
		formulario=AuthenticationForm()
	return render_to_response('form.html', {'form': formulario}, context_instance=RequestContext(request))

def home(request):
	categorias = Categoria.objects.all()
	enlaces    = Enlace.objects.order_by("-votos").all()
	template   = "index.html"
	return render(request, template, {'categorias': categorias, 'enlaces': enlaces})

def categoria(request, id_categoria):
	categorias = Categoria.objects.all()
	cat        = get_object_or_404(Categoria, pk=id_categoria)
	enlaces    = Enlace.objects.filter(categoria = cat)
	template   = "index.html"
	return render(request, template, locals())

@login_required(login_url='/singin')
def minus(request, id_enlace):
	enlace       = Enlace.objects.get(pk=id_enlace)
	enlace.votos = enlace.votos - 1
	enlace.save()
	return HttpResponseRedirect("/")

@login_required(login_url='/singin')
def plus(request, id_enlace):
	enlace       = Enlace.objects.get(pk=id_enlace)
	enlace.votos = enlace.votos + 1
	enlace.save()
	return HttpResponseRedirect("/")

@login_required(login_url='/singin')
def  add(request):
	categorias = Categoria.objects.all()
	if request.method == 'POST':
		form = EnlaceForm(request.POST)
		if form.is_valid():
			enlace = form.save(commit = False)
			enlace.usuario = request.user
			enlace.save()
			return HttpResponseRedirect("/")
	else:
		form = EnlaceForm()
	
	template = "form.html"
	return render_to_response(template,context_instance = RequestContext(request, locals()))
@login_required(login_url='/')
def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect('/')
	
#@login_required(login_url = '/singin')
#def add_categori(request):
#	if request.method = 'POST':
#		pass

def hora_actual(request):	
	#ahora = datetime.now()
	#t = get_template("hora.html")
	#c = Context({"hora": ahora, "usuario": 'Adrian'})
	#html = t.render(c)
	#return HttpResponse(html)
	now = datetime.now()
	return render_to_response('hora.html',{'hora': now, 'usuario':'Adrian'} )



