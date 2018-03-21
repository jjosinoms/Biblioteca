from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^cadastro/$', views.cadastro, name='cadastro'),
	url(r'^busca/$', views.busca, name='busca'),
	url(r'^busca/(?P<pk>[0-9]+)/$', views.detalhe, name='busca'),
	url(r'^livro/(?P<pk>[0-9]+)/$', views.detalhe, name='detalhe'),
	#url(r'^login/$', auth_views.login, name='login'),
	#url(r'^restrito/02A005ccVsW07987/131rTraw313125Wsa21/$', views.restrito, name='restrito'),
	
]	

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)