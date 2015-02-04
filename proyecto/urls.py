from django.conf.urls import include, url
from django.contrib import admin
from app.views import hora_actual, home, plus, minus, add, singin_form

urlpatterns = [
    # Examples:
     
    # url(r'^blog/', include('blog.urls')),    
    #url(r'^$', 'app.views.hora_actual', name='hora_actual')
    url(r'^$', 'app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^plus/(\d+)$', 'app.views.plus', name='plus'),
    url(r'^minus/(\d+)$', 'app.views.minus', name='minus'),
    url(r'^categoria/(\d+)$', 'app.views.categoria', name='categoria'),
    url(r'^add/$', 'app.views.add', name='add'),
    url(r'^singin/$', 'app.views.singin_form', name='singin'),
    url(r'^cerrar/$', 'app.views.cerrar_sesion', name='cerrar sesion'),
]
